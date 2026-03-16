---
title: Windows 操作系统基础
draft: false
---

## Windows 操作系统基础

## 为什么要配置 Windows？

开箱即用的 Windows 是为普通用户设计的 —— 不是为开发者。隐藏文件看不见，文件扩展名被遮蔽，内置搜索……只能说不怎么快。这篇指南能在几分钟内把 Windows 变成对开发者友好的环境。

---

## 快速搜索：认识 Everything

### Windows 搜索的问题

老实说：Windows 的内置搜索又慢又吃资源，找实际文件基本没用。启动应用还行，但试试在你硬盘某处找一个特定的 `.json` 文件？祝你好运。

**Everything** 就是解决方案。它是一个闪电般快速的搜索工具，按文件名索引你的整个驱动器。找任何文件只需要*毫秒*。

### 步骤一：安装 Everything

打开 PowerShell，运行：

```powershell
winget install voidtools.Everything
```

> **命令解释**：
> - `winget`：Windows 内置的包管理器
> - `install`：要执行的动作
> - `voidtools.Everything`：Everything 的唯一 ID（可通过 `winget search everything` 找到）

![](./images/Windows/file-20260111122150310.png)

### 步骤二：启动并搜索

安装后，桌面上会出现 **Everything** 快捷方式。双击打开。

![](./images/Windows/file-20260111122844126.png)

在搜索框输入任何内容 —— 文件名、部分名称，甚至文件内容（如果启用内容搜索）。结果立刻出现。

![](./images/Windows/file-20260111123112848.png)

💡 **小贴士**：按 `Ctrl + Space`（或你设置的自定义快捷键）可以在任何地方调出 Everything。就像拥有了搜索超能力。

---

## 系统语言设置

如果你的 Windows 是中文的，想切换成英文（或反过来），操作如下：

### 步骤一：打开设置

按 `Win`，输入 "settings"，然后按回车。

![](./images/1.OS/file-20260113152828153.png)

### 步骤二：进入语言设置

依次点击 **Time & language** → **Language & region**。

![](./images/1.OS/file-20260113152828152.png)

### 步骤三：添加或更改语言

在这里你可以添加新语言并将你喜欢的设为默认。Windows 会下载语言包，在你注销并重新登录后生效。

![](./images/1.OS/file-20260113152828151.png)

---

## 文件管理要点

### 文件资源管理器：你的文件指挥中心

Windows 使用**文件资源管理器**进行文件管理。快速访问：按 `Win + E` 或点击任务栏中的文件夹图标。

---

### 显示文件扩展名和隐藏文件

⚠️ **开发者必读**：默认情况下，Windows 隐藏文件扩展名（所以 `script.sh` 只显示为 `script`）并隐藏系统文件。当你处理 `.gitignore`、`.env` 等配置文件，或区分 `.json` 和 `.js` 时，这简直是噩梦。

让我们修复这个问题：

#### 步骤一：打开文件资源管理器，点击右上角的 **...** 图标，选择 **Options**。

![](./images/1.OS/file-20260113152828149.png)

#### 步骤二：切换到 **View** 标签。进行以下更改：

- ✅ 勾选 **Show hidden files, folders, and drives**
- ❌ 取消勾选 **Hide extensions for known file types**

![](./images/1.OS/file-20260113152828148.png)

#### 步骤三：点击 **Apply** → **OK**。

![](./images/1.OS/file-20260113152828147.png)

💡 **小贴士**：现在你能看到 `.gitignore`、`.env` 等文件，每个文件都会显示真实的扩展名。好多了。

---

### 文件路径栏

在文件资源管理器顶部，你会看到显示当前位置的路径栏。点击路径中的任何文件夹可以立即跳转。

![](./images/1.OS/file-20260113152828144.png)

💡 **小贴士**：在文件资源管理器中右键点击任何文件夹，选择 **Open in Terminal** 可以启动一个已经导航到该位置的终端。运行脚本时超级方便。

![](./images/1.OS/file-20260113152828146.png)

---

## 保持桌面整洁

杂乱的桌面等于杂乱的大脑。让我们好好整理你的应用。

### 将应用固定到开始菜单或任务栏

按 `Win`，搜索一个应用（比如 Everything），然后：

- **Pin to Start** → 添加到开始菜单磁贴
- **Pin to taskbar** → 添加到底部任务栏，一键访问

![](./images/1.OS/file-20260113152828142.png)

Now press `Win` again — you'll see your pinned apps ready to launch.
再按一次 `Win` —— 你会看到固定的应用随时可以启动。

![](./images/Windows/file-20260111123743239.png)

| 位置 | 最适合 |
|------|--------|
| **任务栏** | 每日必用（终端、VS Code、浏览器）|
| **开始菜单** | 偶尔使用的应用（设置、特定工具）|
| **桌面** | 仅限临时文件 —— 保持干净！|

---

## 总结

1. **安装 Everything** 获得闪电般快速的文件搜索
2. **更改系统语言** 在设置 → 时间和语言 → 语言和区域
3. **显示文件扩展名** 在文件资源管理器选项中（开发者必做！）
4. **显示隐藏文件** 以看到 `.gitignore` 等配置文件
5. **使用路径栏** 快速导航和打开终端
6. **固定应用** 到开始菜单或任务栏 —— 保持桌面干净

*你的 Windows 机器现在对开发者友好了。这些小调整会在未来为你节省无数小时的沮丧。*
