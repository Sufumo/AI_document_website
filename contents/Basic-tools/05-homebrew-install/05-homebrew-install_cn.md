---
permalink: /contents/Basic-tools/05-homebrew-install/zh/
lang: zh


layout: doc
title: Homebrew 安装与基础使用
---

# Homebrew 安装与基础使用

**大局观：Homebrew 是什么？**

想象一下如果 Mac App Store 住在你的终端里 —— 不用点击，不用把应用拖到文件夹，只需输入一条命令，软件就安装好了。这就是 **Homebrew**（简称 `brew`）。它是 macOS 缺失的包管理器，对于任何开发工作流来说都是绝对必备的。

| 它能做什么 | 为什么你需要在 |
|------------|----------------|
| 通过命令行安装软件 | 再也不需要 DMG 文件和拖到应用程序文件夹 |
| 自动管理依赖关系 | 一切都能正常工作 |
| 保持软件更新 | 一条命令更新所有东西 |
| 干净地卸载 | 不会有残留文件到处散落 |

---

## 步骤一：获取安装命令

打开 Homebrew 官网：[https://brew.sh](https://brew.sh/)

![](./images/Toolkit/image25.png)

首页上有一个醒目的安装命令。这是你的入场券。点击复制按钮把它复制下来。

---

## 步骤二：打开终端

按 `Command + 空格`，输入 "Terminal"，然后按回车。

![](./images/Toolkit/image26.png)

如果你需要复习终端基础知识，先看看 [Terminal 基础](../../../Basic-tools/01-terminal-basics/zh)。

---

## 步骤三：运行魔法咒语

把这一整条命令复制粘贴到你的终端：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

> **命令解释**：
> - `curl -fsSL`：从网上下载脚本（静默、安全地）
> - `/bin/bash -c`：用 Bash 运行那个脚本
> - 脚本会处理剩下的一切 —— 下载、安装、配置

![](./images/Toolkit/image27.png)

按下回车，让魔法开始。

---

## 步骤四：输入密码

当提示时，输入你的 Mac 登录密码。

![](./images/Toolkit/image320.png)

⚠️ **重要**：当你输入密码时，**屏幕上什么都不会显示** —— 没有星号，没有圆点，什么都没有。这是安全特性，不是 bug。只管输入密码然后按回车。

输完后按回车。

![](./images/Toolkit/image330.png)

---

## 步骤五：耐心等待

Homebrew 现在会下载和安装一堆东西。这可能需要几分钟到更长时间，取决于你的网络连接。去倒杯咖啡，活动活动腿脚，或者思考一下人生的意义。

![](./images/Toolkit/image340.png)

💡 **小贴士**：如果安装看起来卡住了，别慌。它可能只是在下载大文件。给它点时间。

---

## 步骤六：验证安装

安装完成后，运行以下命令验证一切正常：

```bash
brew --version
```

你应该看到类似这样的输出：

```
Homebrew 4.x.x
```

如果看到版本号，恭喜 —— Homebrew 已经准备好为你服务了！

---

## 常用 Homebrew 命令

Homebrew 安装好了，下面是你最常用的命令：

| 命令 | 作用 | 示例 |
|------|------|------|
| `brew search <名称>` | 搜索软件包 | `brew search node` |
| `brew install <名称>` | 安装软件包 | `brew install node` |
| `brew list` | 显示已安装的软件包 | `brew list` |
| `brew upgrade` | 更新所有软件包 | `brew upgrade` |
| `brew update` | 更新 Homebrew 本身 | `brew update` |
| `brew uninstall <名称>` | 卸载软件包 | `brew uninstall node` |
| `brew info <名称>` | 显示软件包详情 | `brew info node` |

---

## 总结

1. **Homebrew** = macOS 缺失的包管理器
2. **获取命令** 从 [brew.sh](https://brew.sh)
3. **粘贴到终端** 并运行
4. **输入密码**（屏幕上不会显示 —— 这是正常的）
5. **等待** 安装完成
6. **验证** 用 `brew --version`
7. **开始安装** 软件用 `brew install <名称>`

---

*你的 Mac 刚刚变得强大了许多。欢迎来到命令行生活方式 —— 回不去了。*
