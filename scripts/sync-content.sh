#!/usr/bin/env bash
# 将项目 contents 目录同步到 Hugo 的 contents，并转换为 Hugo 多语言格式
# _cn.md -> index.zh.md, _en.md -> index.en.md

set -e
shopt -s nullglob  # 空目录时 * 不展开为字面量
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HUGO_DIR="$(dirname "$SCRIPT_DIR")"
PROJECT_ROOT="$(dirname "$HUGO_DIR")"
SRC="$PROJECT_ROOT/contents"
DEST="$HUGO_DIR/contents"

echo "Syncing content from $SRC to $DEST"

# 清空目标目录（保留结构）
rm -rf "$DEST"
mkdir -p "$DEST"

# 递归处理
process_dir() {
  local src_dir="$1"
  local dest_dir="$2"
  local rel_path="${src_dir#$SRC/}"
  
  # 创建目标目录
  mkdir -p "$dest_dir"
  
  for item in "$src_dir"/*; do
    local name=$(basename "$item")
    
    # 跳过 .obsidian、images 等目录（images 作为资源在 doc 处理时复制）
    if [[ "$name" == .* || "$name" == "images" ]]; then
      continue
    fi
    
    if [[ -d "$item" ]]; then
      # 检查是否是文档目录（包含 _cn.md 或 _en.md）
      local base_name=""
      local has_cn=false
      local has_en=false
      
      for f in "$item"/*.md; do
        [[ -e "$f" ]] || continue
        local fn=$(basename "$f")
        if [[ "$fn" == *"_cn.md" ]]; then
          has_cn=true
          base_name="${fn%_cn.md}"
        elif [[ "$fn" == *"_en.md" ]]; then
          has_en=true
          base_name="${fn%_en.md}"
        fi
      done
      
      if [[ "$has_cn" == true || "$has_en" == true ]]; then
        # 这是文档目录，创建 index.zh.md 和 index.en.md
        mkdir -p "$dest_dir/$name"
        
        # 复制图片等资源
        if [[ -d "$item/images" ]]; then
          cp -r "$item/images" "$dest_dir/$name/"
        fi
        
        # 转换并复制 markdown
        if [[ "$has_cn" == true && -f "$item/${base_name}_cn.md" ]]; then
          convert_frontmatter "$item/${base_name}_cn.md" "$dest_dir/$name/index.zh.md" zh
        fi
        if [[ "$has_en" == true && -f "$item/${base_name}_en.md" ]]; then
          convert_frontmatter "$item/${base_name}_en.md" "$dest_dir/$name/index.en.md" en
        fi
      else
        # 普通子目录，递归处理
        process_dir "$item" "$dest_dir/$name"
      fi
    else
      # 文件：复制非 md 文件，或顶层 md
      if [[ "$name" != *.md ]]; then
        cp "$item" "$dest_dir/"
      fi
    fi
  done
}

# 转换 frontmatter 为 Hugo 格式
convert_frontmatter() {
  local src="$1"
  local dest="$2"
  local lang="$3"
  
  # 提取 title（从第一个 frontmatter 块）
  local title=$(awk '/^---$/{c++} c==1 && /^title:/{sub(/^title:[ \t]+/,""); print; exit}' "$src")
  [[ -z "$title" ]] && title="Untitled"
  
  # 提取正文（跳过第一个 frontmatter 块，保留其后的所有内容）
  local body=$(awk '/^---$/{c++} c==2 && /^---$/{next} c>=2' "$src")
  
  # 写入 Hugo 格式
  {
    echo "---"
    echo "title: $title"
    echo "draft: false"
    echo "---"
    echo "$body"
  } > "$dest"
}

# 执行同步
process_dir "$SRC" "$DEST"

# 创建首页（Hugo 根级 _index）
cat > "$DEST/_index.zh.md" << 'EOF'
---
title: AI 培训文档中心
---

欢迎来到 AI 培训文档中心。从左侧导航选择您需要的文档。
EOF

cat > "$DEST/_index.en.md" << 'EOF'
---
title: AI Tutorial Documentation
---

Welcome to the AI Tutorial Documentation Center. Select the document you need from the left navigation.
EOF

echo "Content sync complete."
