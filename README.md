# AI 文档中心

基于 Jekyll 的文档博客网站，采用 Typora 风格渲染 Markdown，通过 GitHub Actions 自动部署到 GitHub Pages。

## 项目结构

```
AI_document_website/
├── _config.yml          # Jekyll 配置
├── _layouts/
│   ├── default.html     # 默认布局
│   ├── doc.html         # 文档页布局（含侧边栏目录）
│   └── home.html        # 首页布局
├── assets/
│   ├── css/style.css    # Typora 风格样式
│   └── js/toc.js        # 自动目录生成
├── index.md             # 首页
├── contents/
│   └── md-versions/     # 文档源文件
│       ├── 01-agents-configuration/
│       │   ├── 01-GLM-configuration.md
│       │   ├── 02-KIMI-configuration.md
│       │   └── assets/  # 图片资源
│       └── 02-apps-usage/
│           ├── 01-vscode-usage.md
│           └── assets/
├── .github/workflows/
│   └── jekyll.yml       # CI/CD 工作流
├── Gemfile
└── .ruby-version
```

## 添加新文档

1. 在 `contents/md-versions/` 下创建或选择分类目录
2. 添加 `.md` 文件，在开头加入 front matter：

```yaml
---
layout: doc
title: 文档标题
---
```

3. 在 `_config.yml` 的 `doc_categories` 中注册新文档，以便在首页显示

## 本地开发

需要 Ruby 3.1+，建议使用 rbenv 或 rvm 管理 Ruby 版本。

```bash
bundle install
bundle exec jekyll serve
```

访问 http://localhost:4000 预览。

## 部署

推送到 `main` 或 `master` 分支后，GitHub Actions 会自动构建并部署到 GitHub Pages。

在仓库 Settings → Pages 中，将 Source 设置为 **GitHub Actions**。
