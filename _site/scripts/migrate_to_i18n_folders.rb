#!/usr/bin/env ruby
# 将 contents/ 下的单文件 .md 重构为文件夹形式，支持 i18n
# 用法: ruby scripts/migrate_to_i18n_folders.rb
# 前置: 删除已存在的文件夹形式（如 contents/Apps/01-vscode-usage）后再运行

require 'fileutils'
require 'uri'

CONTENTS_DIR = File.expand_path('../contents', __dir__)

def extract_image_paths(md_content)
  # 匹配 ![](path) 或 ![alt](path)
  md_content.scan(/!\[.*?\]\((.*?)\)/).flatten.uniq
end

def resolve_image_path(path, category_dir)
  path = path.strip
  return nil if path.start_with?('http://', 'https://', '//')
  path = URI.decode_www_form_component(path) if path.include?('%')
  path = path.sub(%r{^\./}, '')
  path = path.sub(%r{^images/}, '')
  src = File.join(category_dir, 'images', path)
  File.exist?(src) ? src : nil
end

def copy_image(src, dest_dir)
  base = File.basename(src)
  # 保留子目录结构，如 images/5.Claude Code Workshop/file.png
  rel_under_images = src.sub(%r{.*/images/}, '')
  dest_subdir = File.join(dest_dir, 'images', File.dirname(rel_under_images))
  FileUtils.mkdir_p(dest_subdir)
  dest_file = File.join(dest_dir, 'images', rel_under_images)
  FileUtils.cp(src, dest_file, preserve: true) unless File.exist?(dest_file) && File.mtime(src) <= File.mtime(dest_file)
  'images/' + rel_under_images
end

def migrate_md_to_folder(md_path)
  category_dir = File.dirname(md_path)
  base_name = File.basename(md_path, '.md')
  folder_path = File.join(category_dir, base_name)

  # 若目标文件夹已存在，跳过（避免覆盖已有 _cn/_en 分离内容）
  if File.directory?(folder_path)
    puts "  [SKIP] #{folder_path} already exists"
    return
  end

  content = File.read(md_path, encoding: 'UTF-8')
  image_paths = extract_image_paths(content)

  FileUtils.mkdir_p(folder_path)
  images_dest = File.join(folder_path, 'images')
  FileUtils.mkdir_p(images_dest)

  copied = []
  image_paths.each do |img_ref|
    src = resolve_image_path(img_ref, category_dir)
    next unless src
    rel_path = copy_image(src, folder_path)
    copied << rel_path
  end

  # 写入 _cn 和 _en，内容相同（本步骤不改变内容）
  cn_path = File.join(folder_path, "#{base_name}_cn.md")
  en_path = File.join(folder_path, "#{base_name}_en.md")
  File.write(cn_path, content, encoding: 'UTF-8')
  File.write(en_path, content, encoding: 'UTF-8')

  File.delete(md_path)
  puts "  [OK] #{md_path} -> #{folder_path}/ (#{base_name}_cn.md, #{base_name}_en.md, #{copied.size} images)"
end

def main
  puts "Migrating contents/*.md to folder form (_cn, _en + images)..."
  count = 0
  Dir.glob(File.join(CONTENTS_DIR, '*', '*.md')).each do |md_path|
    next if md_path.include?('/.')
    # 只处理直接位于分类目录下的 md，不处理子目录内的
    rel = md_path.sub("#{CONTENTS_DIR}/", '')
    parts = rel.split('/')
    next unless parts.size == 2 && parts[1].end_with?('.md')
    next if parts[1].start_with?('index', 'README')
    migrate_md_to_folder(md_path)
    count += 1
  end
  puts "Done. Migrated #{count} documents."
end

main
