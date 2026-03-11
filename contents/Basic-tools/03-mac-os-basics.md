---
layout: doc
title: Mac OS Basics · Mac 操作系统基础
---

# Mac OS Basics
**Mac 操作系统基础**

## The Big Picture: Why Configure macOS?
**大局观：为什么要配置 macOS？**

macOS is already pretty developer-friendly out of the box, but there are a few hidden settings that can make your life significantly easier. From finding files to managing your workspace, this guide covers the essentials every developer should know.
macOS 开箱即用就已经对开发者相当友好了，但有一些隐藏设置能让你的生活轻松很多。从查找文件到管理工作空间，这篇指南涵盖了每个开发者都应该知道的基础知识。

---

## Quick Search: Spotlight
**快速搜索：Spotlight**

### The Built-in Superpower
**内置超能力**

macOS comes with **Spotlight Search** — and it's actually good. No need to install anything extra.
macOS 自带 **Spotlight 搜索** —— 而且它真的很好用。不需要安装任何额外的东西。

Press `Command + Space` and start typing. Spotlight searches apps, files, emails, contacts, even does calculations and currency conversions.
按 `Command + 空格` 开始输入。Spotlight 可以搜索应用、文件、邮件、联系人，甚至可以做计算和货币换算。

![](./images/Mac/file-20260107123351255.png)

![](./images/Mac/file-20260107123528095.png)

💡 **Pro Tip**: Spotlight learns from your usage. The more you use it, the smarter it gets at predicting what you're looking for.
💡 **小贴士**：Spotlight 会学习你的使用习惯。你用得越多，它就越聪明，越能预测你要找什么。

---

## System Language Settings
**系统语言设置**

Want to switch between English and Chinese? Here's how:
想在中英文之间切换？操作如下：

### Step 1: Open Language Settings
**步骤一：打开语言设置**

Go to **System Settings** → **General** → **Language & Region**.
进入 **System Settings（系统设置）** → **General（通用）** → **Language & Region（语言与区域）**。

![](./images/Mac/file-20260106175129911.png)

### Step 2: Add and Prioritize Your Language
**步骤二：添加并优先你的语言**

Add **English** (or your preferred language) to "Preferred Languages" and drag it to the top. macOS will update after a restart or logout.
将 **English**（或你偏好的语言）添加到"Preferred Languages"，并拖到顶部。macOS 会在重启或注销后更新。

![](./images/Mac/file-20260106175220146.png)

---

## File Management Essentials
**文件管理要点**

### Finder: Your File Command Center
**Finder：你的文件指挥中心**

**Finder** is the heart of file management on macOS. Click the smiley face icon in your Dock (bottom left by default) to open it.
**Finder** 是 macOS 文件管理的核心。点击 Dock 中的笑脸图标（默认在左下角）打开它。

![](./images/Mac/file-20260106180402157.png)

---

### Show File Extensions & Hidden Files
**显示文件扩展名和隐藏文件**

⚠️ **Critical for Developers**: By default, macOS hides file extensions and system files. When you're working with `.gitignore`, `.env`, `.zshrc`, you need to see these.
⚠️ **开发者必读**：默认情况下，macOS 隐藏文件扩展名和系统文件。当你处理 `.gitignore`、`.env`、`.zshrc` 时，你需要看到这些。

**Show File Extensions:**
**显示文件扩展名：**

1. Open **Finder** → **Settings** (or press `Command + ,`)
1. 打开 **Finder** → **Settings**（或按 `Command + ,`）

2. Click **Advanced** → Check **Show all filename extensions**
2. 点击 **Advanced（高级）** → 勾选 **Show all filename extensions**

![](./images/Mac/file-20260106180156222.png)

**Show Hidden Files:**
**显示隐藏文件：**

Press `Command + Shift + .` to toggle hidden files visibility. Press it again to hide them.
按 `Command + Shift + .` 可以切换隐藏文件的可见性。再按一次可以隐藏它们。

💡 **Pro Tip**: Files starting with a dot (like `.gitignore`) are hidden by default on Unix-based systems. This shortcut is your best friend.
💡 **小贴士**：以点开头的文件（如 `.gitignore`）在基于 Unix 的系统中默认是隐藏的。这个快捷键是你最好的朋友。

---

### The Path Bar
**路径栏**

Knowing where you are in the file system is crucial. Let's enable the path bar:
知道自己在文件系统中的位置很重要。让我们启用路径栏：

**Step 1**: In Finder, go to **View** → **Show Path Bar**
**步骤一**：在 Finder 中，进入 **View** → **Show Path Bar**

![](./images/Mac/file-20260107163525369.png)

Now you'll see your current location at the bottom of every Finder window.
现在你会在每个 Finder 窗口底部看到当前位置。

**Step 2**: Right-click anywhere in the path bar to open a terminal at that location
**步骤二**：右键点击路径栏中的任意位置，在该位置打开终端

![](./images/Mac/file-20260109145541008.png)

Select **Open in Terminal** and you're ready to run commands.
选择 **Open in Terminal**，你就可以运行命令了。

![](./images/Mac/file-20260109145641593.png)

---

### File Compression Made Easy
**轻松压缩文件**

**Compress**: Right-click any file or folder → Select **Compress "..."** → Creates a `.zip` file
**压缩**：右键点击任何文件或文件夹 → 选择 **Compress "..."** → 创建一个 `.zip` 文件

![](./images/Mac/file-20260106180748623.png)

**Extract**: Just double-click any `.zip` file — macOS handles it natively
**解压**：双击任何 `.zip` 文件 —— macOS 原生支持

![](./images/Mac/file-20260107121928478.png)

No extra software needed. It just works.
不需要额外的软件。它就是能用。

---

## Keep Your Dock Clean
**保持 Dock 整洁**

The Dock is prime real estate. A cluttered Dock means a cluttered workflow. Here's how to keep it organized:
Dock 是黄金地段。杂乱的 Dock 意味着杂乱的工作流。以下是如何保持整洁：

**Remove Unused Apps:**
**移除不用的应用：**

Right-click (or two-finger click) any Dock icon → **Options** → **Remove from Dock**
右键点击（或双指点击）任何 Dock 图标 → **Options** → **Remove from Dock**

![](./images/Mac/file-20260106175556075.png)

| What to Keep | What to Remove |
|--------------|----------------|
| Daily apps (Terminal, VS Code, Browser) | Apps you rarely use |
| Apps you're learning | Duplicates or alternatives |
| Communication tools | Installers, one-time tools |

| 保留什么 | 移除什么 |
|----------|----------|
| 每日应用（终端、VS Code、浏览器）| 很少用的应用 |
| 正在学习的应用 | 重复的或替代品 |
| 沟通工具 | 安装程序、一次性工具 |

---

## Trackpad Optimization
**触控板优化**

The Mac trackpad is best-in-class. Let's make it even better.
Mac 触控板是业界最好的。让我们让它变得更好。

### Enable Tap to Click
**启用轻点点按**

No more physically pressing down. A light tap is all you need.
不再需要物理按下。轻轻一点就够了。

Go to **System Settings** → **Trackpad** → Enable **Tap to click**
进入 **System Settings** → **Trackpad（触控板）** → 开启 **Tap to click（轻点点按）**

![](./images/Mac/file-20260107122542163.png)

You can also customize other trackpad behaviors to match your preferences.
你也可以根据自己的习惯自定义其他触控板行为。

![](./images/Mac/file-20260107124740080.png)

### Customize Gestures
**自定义手势**

| Feature | What It Does | Default |
|---------|--------------|---------|
| **Look up & data detectors** | Quick dictionary lookup | Three-finger tap on a word |
| **Secondary click** | Right-click functionality | Two-finger tap or click in corner |

| 功能 | 作用 | 默认设置 |
|------|------|----------|
| **Look up & data detectors** | 快速查字典 | 三指轻点单词 |
| **Secondary click** | 右键功能 | 双指点按或点击角落 |

![](./images/Mac/file-20260107180059440.png)

![](./images/Mac/file-20260107180237427.png)

💡 **Pro Tip**: Spend 5 minutes in System Settings → Trackpad exploring all the gestures. Muscle memory will thank you later.
💡 **小贴士**：花 5 分钟在 System Settings → Trackpad 里探索所有手势。肌肉记忆以后会感谢你的。

---

## File Sharing with AirDrop
**用 AirDrop 共享文件**

### The Apple Ecosystem Superpower
**苹果生态超能力**

**AirDrop** lets you instantly share files between Mac, iPhone, and iPad — no internet required, no file size limits, no hassle.
**AirDrop** 让你在 Mac、iPhone 和 iPad 之间即时共享文件 —— 不需要网络，没有文件大小限制，没有麻烦。

### How to Use AirDrop
**如何使用 AirDrop**

**Step 1**: Open AirDrop from the Control Center (top-right corner of your screen)
**步骤一**：从控制中心打开 AirDrop（屏幕右上角）

![](./images/Mac/file-20260107175549496.png)

**Step 2**: In any app, click the **Share** button and select **AirDrop**
**步骤二**：在任意应用中，点击 **Share** 按钮，选择 **AirDrop**

![](./images/Mac/file-20260106180901363.png)

![](./images/Mac/file-20260107171018286.png)

**Step 3**: Select the recipient from the list of nearby devices
**步骤三**：从附近的设备列表中选择接收者

![](./images/Mac/file-20260107171354103.png)

### Find Your Mac's Name
**找到你的 Mac 名称**

To make sure people can find you, check your Mac's name:
确保别人能找到你，检查你的 Mac 名称：

Click the **Apple menu** → **About This Mac** → **More Info**
点击 **Apple 菜单** → **About This Mac** → **More Info**

![](./images/Mac/file-20260107175634492.png)

![](./images/Mac/file-20260107175752932.png)

Your Mac's name appears here. This is what others will see when they try to AirDrop to you.
你的 Mac 名称会显示在这里。这就是别人给你 AirDrop 时会看到的名称。

---

## Summary

1. **Spotlight Search**: `Command + Space` for instant search
2. **Language Settings**: System Settings → General → Language & Region
3. **Show file extensions**: Finder Settings → Advanced → Show all filename extensions
4. **Show hidden files**: `Command + Shift + .`
5. **Path bar**: View → Show Path Bar (right-click to open Terminal)
6. **Clean Dock**: Remove unused apps, keep only essentials
7. **Trackpad**: Enable "Tap to click" for efficiency
8. **AirDrop**: Instant file sharing across Apple devices

**总结**

1. **Spotlight 搜索**：`Command + 空格` 即时搜索
2. **语言设置**：系统设置 → 通用 → 语言与区域
3. **显示文件扩展名**：Finder 设置 → 高级 → 显示所有文件扩展名
4. **显示隐藏文件**：`Command + Shift + .`
5. **路径栏**：显示 → 显示路径栏（右键可打开终端）
6. **整洁的 Dock**：移除不用的应用，只保留必要的
7. **触控板**：启用「轻点点按」提高效率
8. **AirDrop**：在苹果设备间即时共享文件

---

*Your Mac is now dialed in for developer productivity. These aren't just tips — they're the foundation of an efficient workflow.*
*你的 Mac 现在已经为开发者生产力调整好了。这些不仅仅是技巧 —— 它们是高效工作流的基础。*
