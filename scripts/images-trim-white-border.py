#!/usr/bin/env python3
"""
与 images-to-canvas-jpg.py 相反：去掉图片四周「接近纯白」的空白边，只保留有内容区域。

- 遍历方式相同：默认 contents 下各文章目录（含 images/），仅处理 .md 里 ![](images/...) 引用到的文件。
- 跳过 http(s) 外链；原地覆盖同一路径（格式与扩展名不变）。
- 认为「背景」：RGBA 下 alpha < 阈值，或 RGB 通道均 ≥ 255 - tolerance（默认容忍截图抗锯齿灰边）。
- 若裁剪结果与原始尺寸相同、或整图无内容，则跳过写入。
- 写入时先临时文件再 os.replace，与 images-to-canvas-jpg.py 一致。

依赖：pip install Pillow

用法：
  python3 scripts/images-trim-white-border.py
  python3 scripts/images-trim-white-border.py --apply
  python3 scripts/images-trim-white-border.py --root contents/gsi --apply
  python3 scripts/images-trim-white-border.py --tolerance 12 --padding 2 --apply
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

IMAGE_EXT_IN = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff", ".tif"}

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


def collect_refs_from_md(article_dir: Path, images: Path) -> dict[Path, set[str]]:
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


def content_bbox_rgba(
    rgba,
    *,
    tolerance: int,
    alpha_threshold: int,
) -> tuple[int, int, int, int] | None:
    """非背景像素的轴对齐包围盒 (left, top, right, bottom)，right/bottom 为 PIL crop 用的开区间下标。"""
    from PIL import Image

    if rgba.mode != "RGBA":
        rgba = rgba.convert("RGBA")
    w, h = rgba.size
    if w <= 0 or h <= 0:
        return None

    data = rgba.getdata()
    tol = max(0, min(255, tolerance))
    ath = max(0, min(255, alpha_threshold))

    min_x, min_y = w, h
    max_x, max_y = -1, -1

    i = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = data[i]
            i += 1
            if a < ath:
                continue
            if r >= 255 - tol and g >= 255 - tol and b >= 255 - tol:
                continue
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    if max_x < min_x or max_y < min_y:
        return None

    # PIL crop box: (left, upper, right, lower) with lower/right exclusive
    return (min_x, min_y, max_x + 1, max_y + 1)


def apply_padding(
    box: tuple[int, int, int, int],
    w: int,
    h: int,
    padding: int,
) -> tuple[int, int, int, int]:
    l, t, r, b = box
    pad = max(0, padding)
    l = max(0, l - pad)
    t = max(0, t - pad)
    r = min(w, r + pad)
    b = min(h, b + pad)
    return (l, t, r, b)


def trim_white_border(
    img,
    *,
    tolerance: int,
    alpha_threshold: int,
    padding: int,
):
    """返回 (裁剪后的 Image 或 None, 是否发生变化)。"""
    from PIL import Image

    if getattr(img, "is_animated", False):
        return None, False

    w, h = img.size
    rgba = img.convert("RGBA")
    box = content_bbox_rgba(rgba, tolerance=tolerance, alpha_threshold=alpha_threshold)
    if box is None:
        return None, False

    l, t, r, b = apply_padding(box, w, h, padding)
    if l >= r or t >= b:
        return None, False

    if (l, t, r, b) == (0, 0, w, h):
        return None, False

    cropped = img.crop((l, t, r, b))
    return cropped, True


def save_image_replace(img, final_path: Path, *, quality: int) -> None:
    """按扩展名写回；JPEG 用 quality；其余用各自合理默认。"""
    from PIL import Image

    final_path.parent.mkdir(parents=True, exist_ok=True)
    ext = final_path.suffix.lower()
    suffix = ext if ext else ".png"

    fd, tmp = tempfile.mkstemp(suffix=suffix, dir=final_path.parent)
    os.close(fd)
    tmp_path = Path(tmp)
    try:
        out = img
        if ext in (".jpg", ".jpeg"):
            if out.mode == "RGBA":
                rgb = Image.new("RGB", out.size, (255, 255, 255))
                rgb.paste(out, mask=out.split()[3])
                out = rgb
            else:
                out = out.convert("RGB")
            out.save(tmp_path, "JPEG", quality=quality, optimize=True)
        elif ext == ".png":
            out.save(tmp_path, "PNG", optimize=True)
        elif ext == ".webp":
            out.save(tmp_path, "WEBP", quality=quality, method=6)
        elif ext == ".gif":
            out.save(tmp_path, "GIF", save_all=False)
        elif ext in (".bmp",):
            out.save(tmp_path, "BMP")
        elif ext in (".tiff", ".tif"):
            out.save(tmp_path, "TIFF", compression="tiff_lzw")
        else:
            out.save(tmp_path)
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
    *,
    tolerance: int,
    alpha_threshold: int,
    padding: int,
    quality: int,
    apply: bool,
) -> tuple[int, int]:
    """返回 (成功裁剪写入数, 跳过数含无变化/失败)。"""
    from PIL import Image

    images = article_dir / "images"
    refs_map = collect_refs_from_md(article_dir, images)
    if not refs_map:
        return 0, 0

    try:
        label_base = article_dir.resolve().relative_to(repo)
    except ValueError:
        label_base = article_dir.name

    ok = 0
    skipped = 0

    for src in sorted(refs_map.keys(), key=lambda p: str(p)):
        rel = src.relative_to(article_dir).as_posix()
        label = str(label_base)

        if src.suffix.lower() == ".gif":
            try:
                probe = Image.open(src)
                if getattr(probe, "is_animated", False):
                    print(f"  [跳过] {label}: {rel}（动画 GIF 不处理）")
                    skipped += 1
                    probe.close()
                    continue
                probe.close()
            except OSError as e:
                print(f"  [跳过] {label}: {rel}: {e}", file=sys.stderr)
                skipped += 1
                continue

        if apply:
            try:
                img = Image.open(src)
                img.load()
            except OSError as e:
                print(f"  [跳过] {label}: 无法打开 {rel}: {e}", file=sys.stderr)
                skipped += 1
                continue
            try:
                cropped, changed = trim_white_border(
                    img,
                    tolerance=tolerance,
                    alpha_threshold=alpha_threshold,
                    padding=padding,
                )
            finally:
                img.close()

            if not changed or cropped is None:
                print(f"  [不变] {label}: {rel}")
                skipped += 1
                continue

            try:
                save_image_replace(cropped, src, quality=quality)
            except OSError as e:
                print(f"  [失败] {label}: {rel}: {e}", file=sys.stderr)
                skipped += 1
                continue
            finally:
                cropped.close()

            ok += 1
            print(f"  [裁剪] {label}: {rel}")
        else:
            try:
                img = Image.open(src)
                img.load()
            except OSError as e:
                print(f"  [跳过] {label}: 无法打开 {rel}: {e}", file=sys.stderr)
                skipped += 1
                continue
            try:
                _, changed = trim_white_border(
                    img,
                    tolerance=tolerance,
                    alpha_threshold=alpha_threshold,
                    padding=padding,
                )
            finally:
                img.close()

            if changed:
                ok += 1
                print(f"  [将裁剪] {label}: {rel}")
            else:
                skipped += 1
                print(f"  [将跳过] {label}: {rel}（无白边或无可裁区域）")

    return ok, skipped


def main() -> int:
    if not try_import_pil():
        print("请先安装 Pillow: pip install Pillow", file=sys.stderr)
        return 1

    ap = argparse.ArgumentParser(
        description="去掉 Markdown 引用图片四周接近纯白的边（与 images-to-canvas-jpg.py 相反）"
    )
    ap.add_argument(
        "--root",
        type=Path,
        default=None,
        help="与 flatten-apps 一致：contents 或 contents/Apps 等",
    )
    ap.add_argument(
        "--contents",
        type=Path,
        default=None,
        help="仓库 contents 路径（默认：仓库下 contents）",
    )
    ap.add_argument(
        "--tolerance",
        type=int,
        default=8,
        help="RGB 与 255 的差距在此以内视为白边（0-255，默认 8）",
    )
    ap.add_argument(
        "--alpha-threshold",
        type=int,
        default=10,
        help="RGBA 下 alpha 低于此值视为透明背景（默认 10）",
    )
    ap.add_argument(
        "--padding",
        type=int,
        default=0,
        help="裁剪后再向外保留的像素边距（默认 0）",
    )
    ap.add_argument(
        "--quality",
        type=int,
        default=90,
        help="JPEG/WebP 质量 1-95（默认 90）",
    )
    ap.add_argument("--apply", action="store_true", help="原地写回图片")
    args = ap.parse_args()

    if not 0 <= args.tolerance <= 255:
        print("错误：--tolerance 须在 0-255", file=sys.stderr)
        return 1
    if not 0 <= args.alpha_threshold <= 255:
        print("错误：--alpha-threshold 须在 0-255", file=sys.stderr)
        return 1
    if args.quality < 1 or args.quality > 95:
        print("错误：--quality 须在 1-95", file=sys.stderr)
        return 1

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

    print(
        f"白边判定：RGB≥{255 - args.tolerance} 且 alpha≥{args.alpha_threshold} 为背景；"
        f"padding={args.padding}"
    )
    print(f"文章目录数: {len(article_dirs)}")
    if not args.apply:
        print("当前为预览，不加 --apply 不会写入。\n")

    total_ok = 0
    total_skip = 0
    for ad in article_dirs:
        o, s = process_article(
            ad,
            repo,
            tolerance=args.tolerance,
            alpha_threshold=args.alpha_threshold,
            padding=args.padding,
            quality=args.quality,
            apply=args.apply,
        )
        total_ok += o
        total_skip += s

    if not args.apply:
        print(f"\n预览：将裁剪约 {total_ok} 张，跳过约 {total_skip} 张。确认后请加 --apply。")
    else:
        print(f"\n完成：已裁剪写回 {total_ok} 张；跳过/不变 {total_skip} 张。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
