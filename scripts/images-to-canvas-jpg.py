#!/usr/bin/env python3
"""
按 Markdown 中引用的本地图片路径，将对应文件转为 1000×667 白底画布 JPG，
更新 .md 链接为新的 .jpg 路径，并删除已替换的源文件。

- 遍历方式与 flatten-apps-images.py 一致：默认 contents 下各「文章」目录（含 images/）。
- 仅处理 ![](images/...) 形式的本地链接；http(s) 跳过。
- 输出文件名：与源文件同主文件名、扩展名为 .jpg（如 foo.png → foo.jpg）。
- 若源已是 foo.jpg 且输出仍为 foo.jpg，先写入临时文件再 os.replace，避免误删新文件。
- 若源为 foo.png 与 foo.jpg 均被引用，优先用 png 作源，链接统一改为 images/foo.jpg。

依赖：pip install Pillow

用法：
  python3 scripts/images-to-canvas-jpg.py
  python3 scripts/images-to-canvas-jpg.py --apply
  python3 scripts/images-to-canvas-jpg.py --root contents/Apps --apply
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote, unquote

CANVAS_W_DEFAULT = 1000
CANVAS_H_DEFAULT = 667
WHITE = (255, 255, 255)

IMAGE_EXT_IN = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff", ".tif"}

# ![alt](url)
MD_IMG = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def parse_link_target(inner: str) -> str:
    inner = inner.strip()
    if inner.startswith("<"):
        end = inner.find(">")
        inner = inner[1:end] if end != -1 else inner[1:]
    else:
        if ' "' in inner:
            inner = inner.split(' "', 1)[0]
        elif " '" in inner:
            inner = inner.split(" '", 1)[0]
    return inner.strip()


def is_http(url: str) -> bool:
    import re

    return bool(re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I))


def rel_under_article(raw_url: str) -> str | None:
    raw = parse_link_target(raw_url)
    if not raw or is_http(raw):
        return None
    raw = unquote(raw.split("#", 1)[0].split("?", 1)[0])
    raw = raw.lstrip("./")
    if raw.startswith("/"):
        return None
    if not raw.lower().startswith("images/"):
        return None
    return raw.replace("\\", "/")


def try_import_pil():
    try:
        from PIL import Image  # noqa: F401

        return True
    except ImportError:
        return False


def discover_article_dirs(root: Path) -> list[Path]:
    """与 flatten-apps-images.py 相同：文章目录列表。"""
    root = root.resolve()
    if not root.is_dir():
        return []

    if (root / "images").is_dir():
        has_child_articles = any(
            (p / "images").is_dir()
            for p in root.iterdir()
            if p.is_dir() and p.name != "images"
        )
        if not has_child_articles:
            return [root]

    direct = [
        p
        for p in root.iterdir()
        if p.is_dir()
        and not p.name.startswith((".", "_"))
        and (p / "images").is_dir()
    ]
    if direct:
        return sorted(direct)

    out: list[Path] = []
    for cat in sorted(root.iterdir()):
        if not cat.is_dir() or cat.name.startswith((".", "_")):
            continue
        for art in sorted(cat.iterdir()):
            if (
                art.is_dir()
                and not art.name.startswith(".")
                and (art / "images").is_dir()
            ):
                out.append(art)
    return sorted(out)


def to_rgb(img):
    from PIL import Image

    if img.mode == "RGBA":
        bg = Image.new("RGB", img.size, WHITE)
        bg.paste(img, mask=img.split()[3])
        return bg
    if img.mode == "P":
        img = img.convert("RGBA")
        return to_rgb(img)
    if img.mode != "RGB":
        return img.convert("RGB")
    return img


def fit_and_center_on_canvas(img, canvas_w: int, canvas_h: int):
    from PIL import Image

    img = to_rgb(img)
    w, h = img.size
    if w <= 0 or h <= 0:
        raise ValueError("无效图片尺寸")

    scale = min(canvas_w / w, canvas_h / h)
    new_w = max(1, int(round(w * scale)))
    new_h = max(1, int(round(h * scale)))
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (canvas_w, canvas_h), WHITE)
    x = (canvas_w - new_w) // 2
    y = (canvas_h - new_h) // 2
    canvas.paste(resized, (x, y))
    return canvas


def build_lookup(old_to_new: dict[str, str]) -> dict[str, str]:
    m: dict[str, str] = {}
    for old, new in old_to_new.items():
        variants = {
            old,
            unquote(old),
            "/".join(quote(p, safe="") for p in old.split("/")),
        }
        for v in variants:
            m[v] = new
            m["./" + v] = new
    return m


def md_path_for_link(rel_posix: str) -> str:
    return "/".join(quote(seg, safe="/-_.~") for seg in rel_posix.split("/"))


def replace_md_images(text: str, lookup: dict[str, str]) -> str:
    out: list[str] = []
    pos = 0
    for m in MD_IMG.finditer(text):
        out.append(text[pos : m.start()])
        alt, inner = m.group(1), m.group(2)
        rest = inner
        title = ""
        if ' "' in inner:
            a, b = inner.split(' "', 1)
            rest, title = a, ' "' + b
        elif " '" in inner:
            a, b = inner.split(" '", 1)
            rest, title = a, " '" + b

        raw = parse_link_target(rest.strip())
        rel = rel_under_article(raw)
        if not rel:
            out.append(m.group(0))
            pos = m.end()
            continue

        new_rel = lookup.get(rel) or lookup.get(unquote(rel)) or lookup.get(rel.lstrip("./"))
        if not new_rel:
            out.append(m.group(0))
            pos = m.end()
            continue

        new_rel = new_rel.replace("\\", "/")
        path_enc = md_path_for_link(new_rel)
        out.append(f"![{alt}]({path_enc}{title})")
        pos = m.end()

    out.append(text[pos:])
    return "".join(out)


def collect_refs_from_md(article_dir: Path, images: Path) -> dict[Path, set[str]]:
    """绝对路径 -> 该文件在 md 中出现过的相对路径（posix）集合。"""
    refs: dict[Path, set[str]] = defaultdict(set)

    for md in article_dir.glob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in MD_IMG.finditer(text):
            inner = m.group(2)
            rest = inner
            if ' "' in inner:
                rest = inner.split(' "', 1)[0]
            elif " '" in inner:
                rest = inner.split(" '", 1)[0]
            raw = parse_link_target(rest.strip())
            rel = rel_under_article(raw)
            if not rel:
                continue
            rel_norm = unquote(rel).replace("\\", "/")
            abs_p = (article_dir / rel_norm).resolve()
            if not abs_p.is_file():
                continue
            try:
                abs_p.relative_to(images.resolve())
            except ValueError:
                continue
            if abs_p.suffix.lower() not in IMAGE_EXT_IN:
                continue
            refs[abs_p].add(rel_norm)
    return dict(refs)


def pick_best_source(paths: list[Path]) -> Path:
    """同 stem 多引用时优先 png/webp/gif 再 jpg。"""
    order = {".png": 0, ".webp": 1, ".gif": 2, ".bmp": 3, ".jpg": 5, ".jpeg": 5, ".tiff": 4, ".tif": 4}

    def key(p: Path) -> tuple[int, str]:
        ext = p.suffix.lower()
        return (order.get(ext, 10), str(p))

    return sorted(paths, key=key)[0]


def dest_jpg_for(src: Path) -> Path:
    return src.parent / f"{src.stem}.jpg"


def save_jpeg_replace(
    pil_canvas,
    final_path: Path,
    quality: int,
) -> None:
    """写入 final_path；若需覆盖已存在文件，先写临时文件再 os.replace。"""
    final_path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(suffix=".jpg", dir=final_path.parent)
    os.close(fd)
    tmp_path = Path(tmp)
    try:
        pil_canvas.save(tmp_path, "JPEG", quality=quality, optimize=True)
        os.replace(tmp_path, final_path)
    except BaseException:
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except OSError:
                pass
        raise


def process_article(
    article_dir: Path,
    repo: Path,
    canvas_w: int,
    canvas_h: int,
    quality: int,
    apply: bool,
) -> tuple[int, int]:
    """返回 (成功转换数, 涉及 md 映射数)。"""
    from PIL import Image

    images = article_dir / "images"
    refs_map = collect_refs_from_md(article_dir, images)
    if not refs_map:
        return 0, 0

    # 按「目标 foo.jpg」分组
    by_dest: dict[Path, list[Path]] = defaultdict(list)
    for src in refs_map:
        by_dest[dest_jpg_for(src)].append(src)

    old_to_new: dict[str, str] = {}
    ok = 0

    for dest_jpg, srcs in sorted(by_dest.items(), key=lambda x: str(x[0])):
        src = pick_best_source(srcs)
        rel_new = dest_jpg.relative_to(article_dir).as_posix()

        try:
            label = article_dir.resolve().relative_to(repo)
        except ValueError:
            label = article_dir.name

        rel_src = src.relative_to(article_dir).as_posix()

        def record_mapping() -> None:
            for p in srcs:
                for rel_old in refs_map[p]:
                    if rel_old != rel_new:
                        old_to_new[rel_old] = rel_new

        if apply:
            try:
                img = Image.open(src)
                img.load()
            except OSError as e:
                print(f"  [跳过] {label}: 无法打开 {rel_src}: {e}", file=sys.stderr)
                continue
            try:
                out = fit_and_center_on_canvas(img, canvas_w, canvas_h)
                save_jpeg_replace(out, dest_jpg, quality)
            except OSError as e:
                print(f"  [失败] {label}: {rel_src} → {rel_new}: {e}", file=sys.stderr)
                continue
            ok += 1
            print(f"  [{label}]  {rel_src} → {rel_new}")
            record_mapping()

            # 删除源文件：仅当与输出路径不是同一文件（原地 jpg→jpg 不删）
            for p in srcs:
                if p.resolve() == dest_jpg.resolve():
                    continue
                try:
                    p.unlink()
                    print(f"    已删除 {p.relative_to(article_dir)}")
                except OSError as e:
                    print(f"    [警告] 无法删除 {p.name}: {e}", file=sys.stderr)
        else:
            print(f"  [{label}]  {rel_src} → {rel_new}")
            if len(srcs) > 1:
                print(
                    f"    （合并引用，将删除非同路径源: {[p.name for p in srcs if p.resolve() != dest_jpg.resolve()]}）"
                )
            ok += 1
            record_mapping()

    if not old_to_new:
        return ok, 0

    if apply:
        lookup = build_lookup(old_to_new)
        for md_path in sorted(article_dir.glob("*.md")):
            old_text = md_path.read_text(encoding="utf-8")
            new_text = replace_md_images(old_text, lookup)
            if new_text != old_text:
                md_path.write_text(new_text, encoding="utf-8")
                print(f"  已更新 {md_path.name}")

    return ok, len(old_to_new)


def main() -> int:
    if not try_import_pil():
        print("请先安装 Pillow: pip install Pillow", file=sys.stderr)
        return 1

    ap = argparse.ArgumentParser(
        description="按 Markdown 引用将图片转为画布 JPG 并更新链接"
    )
    ap.add_argument(
        "--root",
        type=Path,
        default=None,
        help="与 flatten-apps 一致：contents 或 contents/Apps 等",
    )
    ap.add_argument("--contents", type=Path, default=None, help="仓库 contents 路径（默认：仓库下 contents）")
    ap.add_argument("--canvas-w", type=int, default=CANVAS_W_DEFAULT)
    ap.add_argument("--canvas-h", type=int, default=CANVAS_H_DEFAULT)
    ap.add_argument("--quality", type=int, default=90, help="JPEG 质量 1-95")
    ap.add_argument("--apply", action="store_true", help="写入图片与 Markdown")
    args = ap.parse_args()

    script_dir = Path(__file__).resolve().parent
    repo = script_dir.parent
    contents_root = (args.contents or (repo / "contents")).resolve()

    root = (args.root or contents_root).resolve()
    if not root.is_dir():
        print(f"错误：目录不存在 {root}", file=sys.stderr)
        return 1

    article_dirs = discover_article_dirs(root)
    if not article_dirs:
        print(f"未找到含 images/ 的文章目录：{root}", file=sys.stderr)
        return 0

    cw, ch = args.canvas_w, args.canvas_h
    if cw <= 0 or ch <= 0:
        print("错误：画布宽高须为正数", file=sys.stderr)
        return 1

    print(f"画布: {cw}×{ch}，按 .md 中 images/ 引用转换 → JPG，更新链接并删除旧源（非同一路径）")
    print(f"文章目录数: {len(article_dirs)}")
    if not args.apply:
        print("当前为预览，不加 --apply 不会写入。\n")

    total_ok = 0
    total_map = 0
    for ad in article_dirs:
        o, m = process_article(ad, repo, cw, ch, args.quality, args.apply)
        total_ok += o
        total_map += m

    if not args.apply:
        print(f"\n预览：约 {total_ok} 次转换，{total_map} 条路径映射。确认后请加 --apply。")
    else:
        print(f"\n完成：{total_ok} 个输出文件已写入。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
