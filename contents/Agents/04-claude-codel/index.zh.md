---
title: Claude Code 使用教程
draft: false
prev: Agents/01-GLM-configuration
next: Extensions/01-skills
---

>[!TIP]
>
> 本教程假设你知道怎么打开终端、运行基本命令。如果听起来有点慌，先花5分钟看看 [Terminal 基础](../../../Basic-tools/01-terminal-basics)，绝对物超所值。


# Claude Code 使用教程

## 安装

### 在 Windows 上安装 Claude Code

>[!NOTE]
>
> 在安装 Claude Code 前请参照 [winget 基础](../../../Basic-tools/04-winget-basics) 教程了解 winget 的使用方法。

按下 `Win` 键搜索 PowerShell 并打开。

![](images/04-claude-codel-20260113152908875.jpg)

在命令行输入 `winget install Anthropic.ClaudeCode` 并按下回车安装 Claude Code。

![](images/04-claude-codel-20260113152908873.jpg)

等待安装完成。

![](images/04-claude-codel-20260113152908869.jpg)

---

### 在 Mac 上安装 Claude Code

>[!NOTE]
>
> 在安装 Claude Code 前请参照 [Homebrew](../../../Basic-tools/05-homebrew-install) 教程安装 Homebrew。

按 `Command + 空格` 搜索 **Terminal** 并打开。

![](images/04-claude-codel-20260113152908876-1.jpg)

在打开的窗口中输入 `brew install --cask claude-code` 并按下 `Enter`，等待安装完成即可成功安装 Claude Code。

![](images/04-claude-codel-20260120130522281.jpg)

![](images/04-claude-codel-20260120130739744.jpg)

> **命令解释：**
>
> - `brew`：安装程序。用于 Mac 的"Homebrew"工具的主命令，用来帮助您安装其他软件。
> - `install`：安装。告诉 Homebrew 开始安装。
> - `--cask`：告诉 Homebrew 安装的是图形界面程序（GUI），而非仅仅是命令行工具。
> - `claude-code`：要安装的软件名称。

---

## 界面概览

在终端输入 `claude` 即可打开 Claude Code 的窗口。

![](images/image36.jpg)

下面是对 Claude Code 窗口元素的简单介绍。在后续章节中，我们会详细介绍它们。

![](images/04-claude-codel-20260113152908866.jpg)

---

## 四个模式

**一张图看懂四种模式：**

| 模式 | 作用 | 适用场景 |
|------|------|----------|
| **绕过权限模式** | 无需确认自动执行 | 重复性任务、信任的工作流 |
| **规划模式** | 先规划后执行 | 复杂项目、高风险任务 |
| **自动接受编辑** | 自动应用文件修改 | 快速迭代、信任的修改 |
| **快捷键帮助** | 显示所有命令和快捷键 | 新手用户、探索功能 |

### 1. 绕过权限模式

允许Claude直接执行命令而无需每次确认。它打破了传统 AI 助手**"请求-确认-执行"**的循环，将决策权完全交给模型。

**适用情况：**

- ✅ 处理大量重复性操作时
- ✅ 信任Claude的操作且希望提高效率
- ✅ 自动化工作流程

![](images/image38.jpg)

---

### 2. 规划模式

Claude 会先制定完整计划，经你批准后再执行。它提供了一个 **「对齐时刻」**。用户可以在执行前指出计划中的逻辑漏洞，避免在错误的路径上浪费 **Token**。

**适用情况：**

- ✅ 复杂项目需要全局视角
- ✅ 希望在执行前审查整体方案
- ✅ 重要或风险较高的任务

![](images/image39.jpg)

---

### 3. 自动接受编辑

Claude的文件修改自动应用，无需逐个确认。该模式假设 **AI** 的局部修改是正确的, 可以在 Claude 完成一系列修改后，统一查看变更，而不是在修改过程中被不断的弹窗打断。

**适用情况：**

- ✅ 快速迭代开发
- ✅ 信任Claude的代码修改
- ✅ 减少交互中断

![](images/image40.jpg)

---

### 4. 快捷键帮助

显示所有可用命令和快捷键的帮助菜单。通过命令行的交互式反馈，减少了用户切换到浏览器查阅官方文档的需求。

**适用情况：**

- ✅ 初次使用Claude Code
- ✅ 忘记特定命令时
- ✅ 探索功能和提高效率

![](images/image41.jpg)

---

## 更换默认模式为绕过权限模式

### Windows

打开 `This PC → C: → Users → **Your user name** → .claude → settings.json` 的路径。

>[!NOTE]
>
> **Your user name** 是您电脑的登录名，可通过 `win` 键查看。

![](images/04-claude-codel-20260113152919863.jpg)

![](images/04-claude-codel-20260113152919861.jpg)

添加以下字段到 settings.json 文件中：

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions"
  }
}
```

> **字段解释**：
> - `"permissions"`：权限控制系统配置
> - `"defaultMode"`：默认模式
> - `"bypassPermissions"`：将该模式添加为 Claude Code 启动默认模式

![](images/04-claude-codel-20260113152919858.jpg)

重新启动 Claude Code, 可以发现 `bypass permissions` 模式已被打开。

![](images/04-claude-codel-20260113152919854.jpg)

---

### Mac

打开 `Home → .claude → settings.json` 的路径。

![](images/04-claude-codel-20260113152919853.jpg)

添加以下字段到 settings.json 文件中：

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions"
  }
}
```

> **字段解释**：
> - `"permissions"`：权限控制系统配置
> - `"defaultMode"`：默认模式
> - `"bypassPermissions"`：将该模式添加为 Claude Code 启动默认模式

![](images/04-claude-codel-20260113152919858.jpg)

重新启动 Claude Code, 可以发现 `bypass permissions` 模式已被打开。

![](images/04-claude-codel-20260113152919854.jpg)

---

## 常用命令

除了网页端的 LLM 问答功能外，Claude Code 还提供了一系列指令，能够高效地管理对话生命周期与上下文进程。

| 命令 | 作用 | 使用场景 |
|------|------|----------|
| `/compact` | 压缩上下文 | 剩20%空间时使用 |
| `/export` | 导出聊天记录 | 参考或分享 |
| `/config` | 打开配置 | 修改默认设置 |
| `/model` | 切换AI模型 | 改变模型能力 |
| `/context` | 显示Token使用 | 监控上下文使用 |
| `/clear` | 重置会话 | 重新开始 |
| `/mcp` | 管理MCP扩展 | 查看已安装工具 |
| `/agents` | 管理子Agent | 独立上下文任务 |
| `/usage` | 查看使用统计 | 账户级别消费 |

### 1. `/compact`

压缩上下文；当空间剩 20% 时建议主动使用，提升上下文利用效率。

![](images/image42.jpg)

>[!TIP]
>
> 一般而言，Claude Code 会自动压缩上下文，因而不必要主动压缩上下文。

![](images/image43.jpg)

---

### 2. `/export`

导出聊天记录；可将记录再发给 AI 参考。

![](images/image44.jpg)

![](images/image45.jpg)

---

### 3. `/config`

该命令能调出Claude Code的配置窗口，修改默认配置。

![](images/image46.jpg)

---

### 4. `/model`

该命令能切换Claude Code使用的大语言模型。

**模型选项：**

| 模型 | 能力 | 适用场景 |
|------|------|----------|
| **Sonnet 4.5** | 平衡性能和速度的中级模型 | 大多数编程任务、代码重构、bug修复 |
| **Opus 4.5** | 最强大的模型，处理复杂工作 | 系统设计、复杂算法、关键项目 |
| **Haiku 4.5** | 最快速的模型，快速响应 | 快速查询、简单脚本、语法检查 |

![](images/image47.jpg)

---

### 5. `/context`

该命令用于查看当前会话的 **Token** 统计。

>[!TIP]
>
> 可以将 **上下文 Token 数**理解为一个滑动窗口：一旦达到上限，模型会挤掉最早的记忆来腾出空间。如果你发现 Claude 开始遗忘指令或重复已解决的问题，通常是因为关键上下文已超出窗口范围。此时，建议使用 **/compact** 命令来精简并压缩上下文。

![](images/image48.jpg)

---

### 6. `/clear`

重置会话并清空上下文。

![](images/image49.jpg)

---

### 7. `/mcp`

管理 **MCP** 扩展工具；可查看已安装工具，使用格式为 "用 XX mcp 做 XX"。

>[!TIP]
>
> **MCP** 为 AI 模型与外部数据、工具（如数据库、本地文件或 GitHub）之间搭建统一的连接桥梁。含 **Context 7**（取最新文档）、**Firecrawl**（网页内容抓取）、**Playwright**（浏览器自动化）等。

![](images/image50.jpg)

---

### 8. `/agents`

可设置的不同子 **Agent**，处理不同任务，每个子 **Agent** 有独立上下文。

![](images/image51.jpg)

---

### 9. `/usage`

查看您的 **Token** 使用统计和账户级别的消费信息。

>[!TIP]
>
> 与 **/context**（显示当前会话的 Token 使用）不同，**/usage** 显示您的整体账户使用情况，包括历史数据和所有会话的消费统计。

![](images/04-claude-codel-20260113152908868.jpg)

---

## 特殊输入模式

**三种特殊输入模式：**

| 前缀 | 作用 | 适用场景 |
|------|------|----------|
| **!** | 直接执行系统命令 | 文件操作、Git管理、包安装 |
| **/** | 调用Claude内置功能 | 工具核心操作入口 |
| **@** | 引用文件/目录 | 代码分析或修改 |
| **&** | 后台执行 | 长时间运行的操作 |

### 1. **!**（Bash 模式）

**Bash 模式**：直接执行系统命令（如 `!pwd`），不消耗 AI **Token**，速度快，适合文件操作、Git 管理、包安装等。

>[!TIP]
>
> `pwd` 为 Bash 命令，会打印当前目录的完整路径。

![](images/image52.jpg)

---

### 2. **/**（命令模式）

**命令模式**：用于调用 Claude 内置功能（如 `/clear` 清空上下文、`/model` 切换 AI 模型、`/cost` 查看 **Token** 消耗），是工具的核心操作入口。

![](images/image53.jpg)

---

### 3. **@**（文件路径模式）

**文件路径模式**：用于快速引用项目中的文件或目录（如 `@.zshrc`），方便 AI 定位代码文件进行分析或修改。

![Graphical user interface, text AI-generated content may be ncorrect.](images/image54.jpg)

---

### 4. **&**（后台模式）

**后台模式**：让任务在后台执行，适合长时间运行的操作。但该模式需要访问 <https://claude.ai/code> 完成 Claude Code 的设置，并配置远程执行环境，让 Claude Code 能够在云端运行代码，才能使用该模式，否则会报以下的错误：

![](images/image55.jpg)

---

## 键盘快捷键

| 快捷键 | 中文解释 |
|--------|----------|
| **输入相关** | |
| `double esc` | 将代码或对话恢复到之前的状态 |
| `shift + tab` | 接受编辑建议 |
| `Control + o` | 显示详细输出 |
| `Control + t` | 显示待办列表 |
| `shift + ↵` | 换行输入 |
| **通用快捷键** | |
| `Control + _` | 删除当前的全部输入 |
| `Control + z` | 挂起当前会话 |
| `Control + v` | 粘贴图片给AI |
| `option + p` | 切换 AI 模型 |
| `Control + s` | 暂存提示词，下次提交后出现 |

---

## 自定义命令

**Claude Code 提供了自定义命令的方法，可以创建可复用的个人快捷方式。**

### 方法一：创建 Markdown 文件

在家目录的 **`~/.claude/commands`** 文件夹中创建一个作为提词的可重复使用 Markdown 文件，文件名即为命令名称，然后即可在 Claude Code 中快速调用。该命令会复用 Markdown 中的提词，在当前工作目录完成任务。使用方式与 3.4.1 节一致，使用 **`/ + 命令`** 的语法进行调用。

![](images/image56.jpg)

---

### 方法二：让 Claude 创建命令

或者，也可以通过直接要求 Claude Code 生成自定义命令的方式添加命令。但是需要注意，通过这种方式添加的命令，可能需要重启 Claude Code 才能看到新添加的命令。

**提词示例：**

```
给我创建一个slash command，命名为`/memo`，这个command的作用是为当前项目创建一个memo记录进度和成果，便于重新开启对话时能在任务断开的地方继续进行。产出物是一个`memo.md`。
```

![](images/image57.jpg)

---

*有问题？卡住了？查阅官方文档。或者直接问 Claude，它就在那。*
