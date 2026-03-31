#!/usr/bin/env ruby
# 为 _en 和 _cn 文件添加 permalink，支持多语言 URL
# _en -> /contents/Category/DocName/ (默认)
# _cn -> /contents/Category/DocName/zh/

CONTENTS = File.expand_path('../contents', __dir__)

def add_permalink(path, permalink, lang_code)
  content = File.read(path, encoding: 'UTF-8')
  return unless content.start_with?('---')
  parts = content.split(/^---\s*$/, 3)
  return unless parts.size >= 3
  fm = parts[1].sub(/^permalink:.*\n?/, '').sub(/^lang:.*\n?/, '')
  fm = "permalink: #{permalink}\nlang: #{lang_code}\n" + fm
  new_content = "---\n#{fm}---\n#{parts[2]}"
  File.write(path, new_content, encoding: 'UTF-8')
end

Dir.glob(File.join(CONTENTS, '**', '*_en.md')).each do |path|
  next if path.include?('/.')
  rel = File.dirname(path).sub("#{CONTENTS}/", '')
  permalink = "/contents/#{rel}/"
  add_permalink(path, permalink, 'en')
  puts "  [en] #{rel} -> #{permalink}"
end

Dir.glob(File.join(CONTENTS, '**', '*_cn.md')).each do |path|
  next if path.include?('/.')
  rel = File.dirname(path).sub("#{CONTENTS}/", '')
  permalink = "/contents/#{rel}/zh/"
  add_permalink(path, permalink, 'zh')
  puts "  [zh] #{rel} -> #{permalink}"
end

puts "Done."
