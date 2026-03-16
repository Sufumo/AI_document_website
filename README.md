# AI 文档中心

基于 Hugo 的 AI 培训文档网站，支持中英文多语言切换。

## 快速开始

### 本地预览

```bash
hugo server
```

访问 http://localhost:1313

### 构建发布

```bash
hugo --minify
```

输出在 `public/` 目录。

## 项目结构

```
├── config/           # Hugo 配置
├── contents/         # 文档内容（index.zh.md / index.en.md）
├── layouts/          # 模板
├── static/           # 静态资源
├── i18n/             # 多语言文案
├── scripts/          # 工具脚本
└── public/           # 构建输出（不提交 git）
```

## 添加新文档

1. 在 `contents/` 下按分类创建目录（如 `Agents/新文档名/`）
2. 添加 `index.zh.md` 和 `index.en.md`
3. 重新构建

## 部署

推送到 `main` 或 `master` 分支后，GitHub Actions 会自动构建并部署到 GitHub Pages。

在仓库 **Settings → Pages** 中，将 Source 设置为 **GitHub Actions**。
