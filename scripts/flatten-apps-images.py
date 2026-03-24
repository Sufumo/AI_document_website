#!/usr/bin/env python3
"""
将 contents 下各文章目录中 images/ 内的图片先全部剪切到根目录，再按规则重命名。

阶段 1（必须先做，避免子目录名混进最终文件名）：
  - 将 images/ 任意子目录下的图片文件全部移动到 images/ 根目录，仅保留原 basename（冲突时 -2、-3…）；
  - 再扫描 .md，用映射表更新其中指向旧路径的链接。

阶段 2：
  - 仅对已在 images/ 根目录下的文件重命名：Pasted image…、file-…；
  - 不再根据「嵌套路径」生成 prefix-yyy-test.jpg 这类名字（已删除该逻辑）。

  prefix 默认为 images 的上一级目录名。

默认仅打印计划；使用 --apply 执行。

根目录 --root 默认为仓库下的 contents/，会遍历所有「分类/文章/images」
（如 Basic-tools/01-terminal-basics、Apps/01-vscode-usage）。
若只处理某一分类，可传 --root contents/Apps。

用法：
  python3 scripts/flatten-apps-images.py
  python3 scripts/flatten-apps-images.py --apply
  python3 scripts/flatten-apps-images.py --root contents/Apps
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}

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


def pasted_new_basename(filename: str, prefix: str) -> str | None:
    m = re.match(r"(?i)^Pasted image\s+(.+)\.([a-z0-9]+)$", filename)
    if not m:
        return None
    id_part = re.sub(r"\s+", "", m.group(1))
    ext = m.group(2).lower()
    return f"{prefix}-{id_part}.{ext}"


def file_dated_new_basename(filename: str, prefix: str) -> str | None:
    m = re.match(r"(?i)^file-(.+)\.([a-z0-9]+)$", filename)
    if not m:
        return None
    id_part = re.sub(r"\s+", "-", m.group(1).strip())
    id_part = re.sub(r"-+", "-", id_part).strip("-")
    ext = m.group(2).lower()
    return f"{prefix}-{id_part}.{ext}"


def desired_dest(images: Path, f: Path, prefix: str) -> Path | None:
    """
    阶段 2 仅处理已在 images/ 根目录下的文件（阶段 1 已扁平化）。
    只重命名 Pasted image…、file-…；其它文件保持原名。
    """
    rel = f.relative_to(images)
    if len(rel.parts) > 1:
        return None
    name = f.name

    nb = pasted_new_basename(name, prefix)
    if nb:
        dest = images / nb
        if f.resolve() == dest.resolve():
            return None
        return dest

    fb = file_dated_new_basename(name, prefix)
    if fb:
        dest = images / fb
        if f.resolve() == dest.resolve():
            return None
        return dest

    return None


def resolve_collisions(moves: list[tuple[Path, Path]]) -> list[tuple[Path, Path]]:
    occupied: set[Path] = set()
    out: list[tuple[Path, Path]] = []
    for src, dest in sorted(moves, key=lambda t: (len(t[0].parts), str(t[0]))):
        final = dest
        n = 1
        while final in occupied:
            n += 1
            final = dest.parent / f"{dest.stem}-{n}{dest.suffix}"
        occupied.add(final)
        out.append((src, final))
    return out


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


def plan_flatten_nested_to_root(images: Path) -> list[tuple[Path, Path]]:
    """
    将 images/ 下所有子目录中的图片剪切到 images/ 根目录（仅 basename，冲突时加后缀）。
    必须先于阶段 2，避免阶段 2 对嵌套路径使用「路径拼进文件名」的旧规则。
    """
    moves: list[tuple[Path, Path]] = []
    for f in sorted(images.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in IMAGE_EXT:
            continue
        rel = f.relative_to(images)
        if len(rel.parts) <= 1:
            continue
        dest = images / rel.name
        if f.resolve() == dest.resolve():
            continue
        moves.append((f, dest))

    if not moves:
        return []
    return resolve_collisions(moves)


def file_set_after_phase1(images: Path, p1_final: list[tuple[Path, Path]]) -> list[Path]:
    """用于预览阶段 2：模拟阶段 1 完成后的文件集合。"""
    paths: set[Path] = set()
    for f in images.rglob("*"):
        if f.is_file() and f.suffix.lower() in IMAGE_EXT:
            paths.add(f.resolve())

    for src, dest in p1_final:
        try:
            paths.discard(src.resolve())
        except KeyError:
            pass
        paths.add(dest.resolve())
    return [Path(p) for p in sorted(paths)]


def plan_phase2_rename(
    images: Path, prefix: str, file_paths: list[Path] | None = None
) -> list[tuple[Path, Path]]:
    """若给定 file_paths（绝对路径列表），只对这些路径计算重命名；否则扫描 images 下全部图片。"""
    moves: list[tuple[Path, Path]] = []
    if file_paths is not None:
        candidates = file_paths
    else:
        candidates = [
            f
            for f in sorted(images.rglob("*"))
            if f.is_file() and f.suffix.lower() in IMAGE_EXT
        ]

    for f in candidates:
        try:
            f = f.resolve()
            _ = f.relative_to(images.resolve())
        except ValueError:
            continue
        f = Path(f)
        dest = desired_dest(images, f, prefix)
        if dest is None:
            continue
        moves.append((f, dest))

    if not moves:
        return []
    return resolve_collisions(moves)


def build_plain_map(final_moves: list[tuple[Path, Path]], article_dir: Path) -> dict[str, str]:
    m: dict[str, str] = {}
    for src, dest in final_moves:
        old = src.relative_to(article_dir).as_posix()
        new = dest.relative_to(article_dir).as_posix()
        m[old] = new
    return m


def discover_article_dirs(root: Path) -> list[Path]:
    """
    - 若 root 的直接子目录里已有「文章/images」（如 contents/Apps/01-vscode-usage），
      则每个含 images 的子目录即一篇文章。
    - 否则视为 root=contents：遍历 分类/文章/images（如 Basic-tools/01-terminal-basics）。
    """
    root = root.resolve()
    if not root.is_dir():
        return []

    # 单篇文章目录：…/01-terminal-basics（直接含 images/，且没有「子文章目录」）
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


def run(root: Path, prefix_override: str | None, apply: bool) -> int:
    root = root.resolve()
    if not root.is_dir():
        print(f"错误：目录不存在 {root}", file=sys.stderr)
        return 1

    article_dirs = discover_article_dirs(root)
    if not article_dirs:
        print(f"未找到含 images/ 的文章目录：{root}", file=sys.stderr)
        return 0

    total_p1 = 0
    total_p2 = 0

    for article_dir in sorted(article_dirs):
        prefix = prefix_override if prefix_override is not None else article_dir.name
        images = article_dir / "images"

        _rel = article_dir.relative_to(root)
        _label = article_dir.name if str(_rel) == "." else str(_rel)
        print(f"\n[{_label}]  prefix={prefix}")

        # ---------- 阶段 1：全部剪切到根目录（先于重命名）----------
        p1_final = plan_flatten_nested_to_root(images)
        print("  --- 阶段1：images 子目录 → 根目录（basename）---")
        if not p1_final:
            print("  （无嵌套文件，跳过）")
        else:
            for src, dest in p1_final:
                print(f"  {src.relative_to(article_dir)} → {dest.relative_to(article_dir)}")
            total_p1 += len(p1_final)

        p1_lookup: dict[str, str] = {}
        if p1_final:
            p1_lookup = build_lookup(build_plain_map(p1_final, article_dir))

        print("  --- 阶段2：重命名为 {prefix}-… ---".replace("{prefix}", prefix))

        if apply:
            if p1_final:
                for src, dest in sorted(
                    p1_final, key=lambda t: (-len(t[0].parts), str(t[0]))
                ):
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    if dest.exists() and src.resolve() != dest.resolve():
                        print(f"  [错误] 目标已存在，跳过: {dest}", file=sys.stderr)
                        continue
                    src.rename(dest)

                for d in sorted(
                    [p for p in images.rglob("*") if p.is_dir()],
                    key=lambda p: len(p.parts),
                    reverse=True,
                ):
                    try:
                        if d != images and not any(d.iterdir()):
                            d.rmdir()
                    except OSError:
                        pass

                for md_path in sorted(article_dir.glob("*.md")):
                    old_text = md_path.read_text(encoding="utf-8")
                    new_text = replace_md_images(old_text, p1_lookup)
                    if new_text != old_text:
                        md_path.write_text(new_text, encoding="utf-8")
                        print(f"  [阶段1] 已更新 {md_path.name}")

            p2_run = plan_phase2_rename(images, prefix, None)
            for src, dest in p2_run:
                print(f"  {src.relative_to(article_dir)} → {dest.relative_to(article_dir)}")
            total_p2 += len(p2_run)

            if p2_run:
                p2_lookup = build_lookup(build_plain_map(p2_run, article_dir))
                for src, dest in sorted(
                    p2_run, key=lambda t: (-len(t[0].parts), str(t[0]))
                ):
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    if dest.exists() and src.resolve() != dest.resolve():
                        print(f"  [错误] 目标已存在，跳过: {dest}", file=sys.stderr)
                        continue
                    src.rename(dest)

                for d in sorted(
                    [p for p in images.rglob("*") if p.is_dir()],
                    key=lambda p: len(p.parts),
                    reverse=True,
                ):
                    try:
                        if d != images and not any(d.iterdir()):
                            d.rmdir()
                    except OSError:
                        pass

                for md_path in sorted(article_dir.glob("*.md")):
                    old_text = md_path.read_text(encoding="utf-8")
                    new_text = replace_md_images(old_text, p2_lookup)
                    if new_text != old_text:
                        md_path.write_text(new_text, encoding="utf-8")
                        print(f"  [阶段2] 已更新 {md_path.name}")
        else:
            if p1_final:
                virtual_files = file_set_after_phase1(images, p1_final)
                p2_preview = plan_phase2_rename(images, prefix, virtual_files)
            else:
                p2_preview = plan_phase2_rename(images, prefix, None)
            for src, dest in p2_preview:
                print(f"  {src.relative_to(article_dir)} → {dest.relative_to(article_dir)}")
            total_p2 += len(p2_preview)

    if not apply:
        print(
            f"\n预览：阶段1 共 {total_p1} 个文件，阶段2 共 {total_p2} 个文件。"
            " 确认后请加 --apply。"
        )
    else:
        print(f"\n完成：阶段1 {total_p1} 个文件，阶段2 {total_p2} 个文件。")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="先按 Markdown 扁平化 images，再按规则重命名"
    )
    ap.add_argument(
        "--root",
        type=Path,
        default=None,
        help="根目录（默认：仓库 contents，遍历全部分类下的文章；可改为 contents/Apps 只跑 Apps）",
    )
    ap.add_argument(
        "--prefix",
        type=str,
        default=None,
        metavar="STR",
        help="覆盖默认前缀；默认使用各文章目录名",
    )
    ap.add_argument("--apply", action="store_true", help="执行移动与重命名并更新 Markdown")
    args = ap.parse_args()

    script_dir = Path(__file__).resolve().parent
    repo = script_dir.parent
    root = (args.root or (repo / "contents")).resolve()

    return run(root, args.prefix, args.apply)


if __name__ == "__main__":
    sys.exit(main())
