#!/usr/bin/env python3
"""
扫描 contents 下每个含 images/ 的工作目录：读取该目录内全部 .md 中引用的本地图片，
删除 images/ 下未被任何 .md 引用的文件（可选清理空子目录）。

默认仅预览；使用 --apply 才会真正删除。

用法：
  python3 scripts/cleanup-unused-images.py
  python3 scripts/cleanup-unused-images.py --apply
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

# Markdown: ![alt](url) 或 ![alt](url "title")
MD_IMG = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
# HTML: <img src="...">
HTML_IMG = re.compile(
    r"<img\b[^>]*\bsrc\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))",
    re.IGNORECASE,
)


def parse_link_target(inner: str) -> str:
    """从 ![](...) 的内层取出 URL，去掉尖括号与可选 title。"""
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


def collect_referenced_images(article_dir: Path, images_root: Path) -> set[Path]:
    """解析 article_dir 下所有 .md，收集指向 images_root 下（含子路径）的已解析绝对路径。"""
    refs: set[Path] = set()
    images_root = images_root.resolve()

    for md_path in sorted(article_dir.glob("*.md")):
        try:
            text = md_path.read_text(encoding="utf-8")
        except OSError as e:
            print(f"  [跳过] 无法读取 {md_path}: {e}", file=sys.stderr)
            continue

        candidates: list[str] = []
        for m in MD_IMG.finditer(text):
            candidates.append(parse_link_target(m.group(1)))
        for m in HTML_IMG.finditer(text):
            for g in m.groups():
                if g:
                    candidates.append(g.strip())
                    break

        for raw in candidates:
            raw = raw.strip()
            if not raw or re.match(r"^[a-z][a-z0-9+.-]*:", raw, re.I):
                # http(s):、mailto: 等
                continue
            if raw.startswith(("/", "\\")) and not raw.startswith("//"):
                # 站点根路径，不当作本目录 images
                continue

            # 相对路径：相对当前 md 所在目录
            path_part = unquote(raw.split("#", 1)[0].split("?", 1)[0])
            try:
                resolved = (article_dir / path_part).resolve()
            except (OSError, ValueError):
                continue

            try:
                resolved.relative_to(images_root)
            except ValueError:
                continue
            if resolved.is_file():
                refs.add(resolved)

    return refs


def list_image_files(images_root: Path) -> list[Path]:
    out: list[Path] = []
    if not images_root.is_dir():
        return out
    for p in images_root.rglob("*"):
        if p.is_file():
            out.append(p.resolve())
    return out


def remove_empty_dirs(bottom_up_root: Path) -> None:
    """自下而上删除空目录（不删除 bottom_up_root 本身）。"""
    for d in sorted(
        [p for p in bottom_up_root.rglob("*") if p.is_dir()],
        key=lambda x: len(x.parts),
        reverse=True,
    ):
        try:
            if d != bottom_up_root and not any(d.iterdir()):
                d.rmdir()
        except OSError:
            pass


def process_article(article_dir: Path, contents_root: Path, apply: bool) -> tuple[int, int]:
    """
    处理单个工作目录。返回 (将删除文件数, 已引用文件数)。
    apply=False 时仍统计将删除数，但不删。
    """
    images_root = article_dir / "images"
    if not images_root.is_dir():
        return 0, 0

    referenced = collect_referenced_images(article_dir, images_root)
    on_disk = list_image_files(images_root)
    to_delete = [p for p in on_disk if p not in referenced]

    try:
        display = article_dir.relative_to(contents_root)
    except ValueError:
        display = article_dir

    if to_delete:
        print(f"\n{display}  images/: 磁盘 {len(on_disk)} 个文件，文中引用 {len(referenced)} 个，将删除 {len(to_delete)} 个")
        for p in sorted(to_delete):
            try:
                rel_p = p.relative_to(article_dir)
            except ValueError:
                rel_p = p
            if apply:
                try:
                    p.unlink()
                    print(f"  已删除  {rel_p}")
                except OSError as e:
                    print(f"  [失败] {rel_p}: {e}", file=sys.stderr)
            else:
                print(f"  [预览] {rel_p}")

    if apply and to_delete:
        remove_empty_dirs(images_root)

    return len(to_delete), len(referenced)


def find_work_dirs(contents_root: Path) -> list[Path]:
    """找出所有「直接包含 images 子目录」的目录（不进入 images 继续向下 walk）。"""
    work: list[Path] = []
    for root, dirs, _files in os.walk(contents_root, topdown=True):
        if "images" in dirs:
            work.append(Path(root))
        dirs[:] = [d for d in dirs if d != "images"]
    return sorted(work)


def main() -> int:
    parser = argparse.ArgumentParser(description="删除各文章目录 images/ 中未被同目录 .md 引用的图片")
    parser.add_argument(
        "--contents",
        type=Path,
        default=None,
        help="contents 根目录（默认：脚本所在仓库的 contents/）",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="真正删除文件（默认仅预览）",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    contents_root = (args.contents or (repo_root / "contents")).resolve()

    if not contents_root.is_dir():
        print(f"错误：目录不存在 {contents_root}", file=sys.stderr)
        return 1

    work_dirs = find_work_dirs(contents_root)
    if not work_dirs:
        print(f"未找到含 images/ 的子目录：{contents_root}")
        return 0

    if not args.apply:
        print("当前为预览模式（不会删除）。确认无误后请加 --apply 执行删除。\n")

    total_delete = 0
    for wd in work_dirs:
        n_del, _n_ref = process_article(wd, contents_root, apply=args.apply)
        total_delete += n_del

    if not args.apply:
        print(f"\n预览合计：将删除 {total_delete} 个文件。使用 --apply 执行删除。")
    else:
        print(f"\n完成：已删除 {total_delete} 个文件。")

    return 0


if __name__ == "__main__":
    sys.exit(main())
