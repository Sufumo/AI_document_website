---
title: VSCode 优雅上手指南
draft: false
prev: Extensions/02-mcp
next: Apps/03-obsidian-notes
---
# VSCode 介绍

## VSCode 是什么？为什么推荐 VS Code？

Visual Studio Code 本质上是一个用来查看、编辑和管理你电脑中文件的工作界面，而不是文件真正存放的地方。可以把电脑想成一个房间，所有文件都安静地放在文件柜里；VS Code 更像是一张桌面，当你打开它时，只是把需要的文件拿出来摊在桌面上进行操作。你在桌面上做的任何修改，比如编辑、保存或删除，都会直接影响文件柜里的原始文件。

从这个角度看，VS Code 可以理解为把文件浏览、搜索和文本编辑整合在一起的一款工具，让你在同一个界面里完成查找、查看和修改文件的工作。同时，它还可以通过安装插件不断扩展能力，例如像 Claude Code 这样的工具，也可以直接在 VS Code 中使用，从而把开发和 AI 辅助操作放在同一个环境里完成。

![](./images/Pasted%20image%2020260310143657.png)

---

## 第一部分：VS Code 安装

### 快速安装（推荐 ✨）

>[!TIP]
>
> 本章节默认你已经具备基础终端与命令行能力。若还不熟悉，建议先花 5 分钟阅读 [Terminal 基础](../../../Basic-tools/01-terminal-basics) 和 [Homebrew 安装](../../../Basic-tools/05-homebrew-install)，后续会轻松许多。


按 `Option + Space` 打开搜索，输入 **Terminal**，然后按 Enter。

![](./images/Pasted%20image%2020260303190946.png)

将下面这段“魔法咒语”复制到终端并回车：

```bash
brew install --cask visual-studio-code
```

![](./images/Pasted%20image%2020260305170644.png)

> **命令解释：**
>
> - `brew`：macOS 常用包管理工具 Homebrew
> - `install`：执行安装
> - `--cask`：安装带图形界面的应用
> - `visual-studio-code`：VS Code 的软件包名

>[!NOTE]
>
> 如果你还没安装 Homebrew，请先完成 [Homebrew 安装](../../../Basic-tools/05-homebrew-install)。

当终端恢复可输入状态时，就表示安装完成。

![](./images/Pasted%20image%2020260305171011.png)

---

## 第二部分：VS Code 界面导览

首次打开 VS Code 时，你通常会看到下面这个界面：

![](./images/Pasted%20image%2020260305171659.png)

### 左侧边栏（活动栏）

**为什么重要**：这里就是你的项目“控制台”。

左侧是**活动栏**，点击左上角按钮可展开/收起，常用入口如下：

| 图标 | 工具 | 主要用途 |
|------|------|------|
| 📁 | **文件** | 浏览与管理文件（类似 Finder） |
| 🔍 | **搜索** | 在整个项目中检索内容 |
| 🔀 | **版本管理** | 查看改动并管理历史 |
| 🧩 | **扩展** | 安装插件增强能力 |

---

### 打开你的第一个文件夹

依次点击顶部菜单 **File → Open Folder**，选择目标目录。

![](./images/Pasted%20image%2020260305172317.png)

打开后，你可以在资源管理器中：

- ✅ 点击文件夹展开或收起
- ✅ 使用工具栏新建文件、新建文件夹、刷新视图

![](./images/Pasted%20image%2020260305173132.png)

>[!TIP]
>
> VS Code 更适合处理纯文本文件（如 `.txt`、`.md`、`.html`）；Word、Excel、PPT 等格式通常需要插件或外部应用配合。

---

### 搜索面板

**搜索**栏会在整个项目（含子文件夹）中检索匹配文本；结果会高亮显示，点击左侧文件名即可快速跳转。

![](./images/Pasted%20image%2020260305173548.png)

---

### 版本管理（Git）

>[!TIP]
>
> 如果你对 Git 还不太熟悉，建议先花 10 分钟阅读 [Git 入门实战教程](../../../Basic-tools/06-git-basis)。那篇更系统，这里上手会更轻松。

**版本管理**视图提供了图形化界面，让你更直观地管理改动，不必一开始就记住大量命令。

点击 **Initialize Repository**，即可把当前文件夹初始化为可追踪版本的仓库。

>[!NOTE]
>
> 只有完成初始化后，Git 才会开始记录该文件夹的改动历史。

![](./images/Pasted%20image%2020260305173743.png)
#### 基本流程（3 步）

| 阶段 | 含义 | 你要做什么 |
|------|-----------|----------|
| **有改动** | 文件已修改，但尚未纳入提交 | 先正常编辑文件 |
| **准备提交** | 选择本次要保存的改动 | 点击文件旁的 **+** |
| **已保存** | 改动已写入版本历史 | 点击蓝色 **Commit** 按钮 |

![](./images/Pasted%20image%2020260305175821.png)

---

### 扩展市场

**扩展**视图就是插件市场，你可以在这里为 VS Code 添加新能力。

![](./images/Pasted%20image%2020260305182927.png)

>[!TIP]
>
> 安装 **Markdown All in One**、**Md Editor** 等插件后，可以直接预览 Markdown 效果，排版所见即所得。

![](./images/Pasted%20image%2020260305183558.png)

![](./images/Pasted%20image%2020260305184231.png)

---

### 内置终端

点击右上角**终端**图标，即可在 VS Code 内打开终端，并自动定位到当前项目目录。

![](./images/Pasted%20image%2020260305184535.png)

点击终端面板中的 **+** 可新建多个终端；右下角下拉菜单可用于切换与管理已打开终端。

![](./images/Pasted%20image%2020260305184747.png)

---

### AI 助手

点击右上角 **Copilot / Agent** 图标可打开 AI 助手（默认是 GitHub Copilot）。在输入框输入指令后，Agent 会在当前目录执行相关工作。

![](./images/Pasted%20image%2020260305190648.png)

---

### 命令面板

**命令面板**可用于检索命令、设置、扩展等功能。很多不在主界面直接显示的功能，都可以在这里快速找到。

![](./images/Pasted%20image%2020260305191241.png)

---

## 第三部分：文档管理

### 基本文件管理规范

很多初学者在刚开始使用 VS Code 时，最大的问题不是不会操作，而是**文件容易变乱、找不到、甚至放错地方**。下面这些简单规则，可以帮你避免大部分混乱：

**1. 一个项目，一个文件夹**  
每一个任务或项目，都单独放在一个文件夹里。不要把不同项目的文件混在一起，否则后期会很难整理。

**2. 文件和文件夹命名要清晰**  
尽量使用有意义的名字，例如 `report.md`、`data_analysis.docx`，避免使用 `test1`、`aaa` 这类随意命名。  

**3. 不要混放不同类型内容**  
例如：
- 文档放在一个地方
- 图片或数据单独放文件夹

这样后续查找和维护会更容易。

**4. 建立一个简单的目录结构**  
可以参考下面这种基础结构：

```
your-project/  
├── data/        （数据文件）  
├── docs/        （文档说明）  
├── src/         （代码）  
└── README.md    （项目说明）
```

不需要一开始就很复杂，但**有结构一定比没有结构好**。

> [!TIP]
> 
> 记住：VS Code 只是帮你“操作文件”的工具，真正的文件始终在你的电脑文件夹中。一个清晰的文件结构，会让你以后节省大量时间。

---
### 打开工作区

打开 VS Code 后，依次点击 **File → Open Folder**，切换到你要处理文件的目录。

![](./images/Pasted%20image%2020260309111111.png)

![](images/Pasted%20image%2020260317181317.png)

---

### 创建文件夹和文件

#### 创建新文件夹

可使用文件夹右侧工具栏按钮新建文件夹。

![](images/Pasted%20image%2020260317181528.png)

输入文件夹名并按 Enter。

![](images/Pasted%20image%2020260317181612.png)

#### 创建子文件夹

若需在某个文件夹内创建子文件夹，先选中该文件夹，再点击 **New Folder**。

![](images/Pasted%20image%2020260317181655.png)

#### 创建新文件

同样可通过工具栏直接在文件夹内新建文件。

![](images/Pasted%20image%2020260317181733.png)

新文件默认为空，需要你手动输入后缀名，例如 `test.md`。

![](images/Pasted%20image%2020260317181755.png)

创建完成后，点击侧栏文件即可查看或编辑内容。

![](images/Pasted%20image%2020260317181848.png)

>[!TIP]
>
> VS Code 可直接创建 `.txt`、`.md`、`.json` 等纯文本文件；Word、Excel、PPT 这类文件通常建议在对应应用中创建。

---

### 重命名和删除

#### 重命名文件

右键文件并选择 **Rename**，输入新文件名即可。

>[!TIP]
>
> 在 Mac 上，也可以先选中文件，再按 Enter 快速重命名。

![](images/Pasted%20image%2020260317181926.png)

![](images/Pasted%20image%2020260317181938.png)

#### 重命名文件夹

文件夹操作同理：右键重命名，或选中后按 Enter。

![](images/Pasted%20image%2020260317182048.png)

#### 删除文件或文件夹

右键文件或文件夹，选择 **Delete** 即可删除。

![](images/Pasted%20image%2020260317182150.png)

![](images/Pasted%20image%2020260317182210.png)

---

### 快速查找文件

当项目文件较多时，可通过**搜索**按关键词快速定位内容。

![](./images/Pasted%20image%2020260306115131.png)

文件路径会显示在编辑器上方。

![](./images/Pasted%20image%2020260306115255.png)

点击路径中的任一级目录，即可快速浏览该目录下的文件。

![](./images/Pasted%20image%2020260306115349.png)

>[!TIP]
>
> 安装 PDF、Office 等格式插件后，可在 VS Code 内直接查看或编辑更多文件类型，减少应用切换。

![](./images/Pasted%20image%2020260306115638.png)

在扩展搜索栏输入「claude」，即可找到并安装 Claude Code for VS Code 插件。

![](images/Pasted%20image%2020260317182540.png)

点击右上角图标可打开 Claude Code 对话窗口，使用更便捷。

![](images/Pasted%20image%2020260317182749.png)


---

## 第四部分：Skills 和 MCP 实战

> [!TIP]
> 
> 建议先阅读 [Skills 介绍](../../../Extensions/01-skills) 和 [MCP 介绍](../../../Extensions/02-mcp)（选读），再继续本章。

### 为什么需要 Skills 和 MCP？

Agent 基于通用大模型，本身知识库和工具能力有限，对图片、音频等多媒体任务支持也相对有限。因此，我们通常通过 Skills 和 MCP 来“扩展能力”。

| 扩展类型 | 是什么 | 如何使用 |
|------|------|------|
| **Skills** | 基于文本的提示文件 | 告诉 Agent 某类任务该怎么做 |
| **MCP** | 现成的工具/接口 | 让 Agent 直接调用，无需从零写代码 |

如果你已在前文按 [GLM 配置教程](../../../Agents/01-GLM-configuration#方法一-可视化配置工具推荐-) 或 [KIMI 配置教程](../../../Agents/02-KIMI-configuration#方法一-可视化配置工具推荐-) 安装了 **Agent Manager**（通过 `agent_manager-main.zip`），它也可以用于安装 Skills 和 MCP。本节主要讲清：它们是什么、在 VS Code 中怎么用。无论你通过应用安装还是命令行安装，使用方式都类似。

---

### Skills：你的任务向导

打开 VS Code，依次点击 **File → Open Folder**，切换到目标文件夹。

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309111611.png)

点击右上角快捷按钮，打开 Claude Code 插件对话窗口。

![](images/Pasted%20image%2020260317183955.png)

输入 **`/file-conversion`**（即该 Skill 的文件夹名）即可调用它。

![](images/Pasted%20image%2020260317184133.png)

例如输入 **please convert this pdf file to md and place this md file in the current folder**，拖入 PDF 后按 Enter。

>[!WARNING]
>
> `file-conversion` 需要阿里云付费服务与 API Key。建议先用其他 Skill 做演示测试。

![](images/Pasted%20image%2020260317184235.png)

任务完成后，就能在工作区看到转换后的 Markdown 文件。

![](images/Pasted%20image%2020260317185208.png)

---

### MCP：你的预构建工具箱

和主要依靠文本提示的 Skill 不同，**MCP** 通常是独立程序或服务。Agent 可直接调用，减少从零写代码的工作量。

你只需按 MCP 提供方说明完成安装与配置，就能在 Claude Code 中查看并使用。

#### 在 VSCode 中使用 MCP

打开 VS Code，依次点击 **File → Open Folder**，切换到目标文件夹。

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309115212.png)

点击右上角 Claude Code 图标，打开插件面板。

![](images/Pasted%20image%2020260317194356.png)

输入 **`/mcp`**，查看当前可用 MCP 服务。

![](images/Pasted%20image%2020260317194423.png)

![](images/Pasted%20image%2020260317194437.png)

点击任一 MCP 可查看详细信息。

![](images/Pasted%20image%2020260317194559.png)

点击 **View tools** 可查看该 MCP 提供的全部工具。

例如 **qwen-ai** MCP 支持文本输出、翻译、图片文字识别、图片理解、联网搜图、网页抓取、音频转文字、视频理解等能力，可显著扩展 Agent 的工作范围。

![](images/Pasted%20image%2020260317194620.png)

![](images/Pasted%20image%2020260317194714.png)

例如在 Claude Code 中输入 **please convert this audio file to txt and save it to output folder**，再拖入音频文件。

![](images/Pasted%20image%2020260317195139.png)

稍等片刻，音频内容就会转换为文字。

![](images/Pasted%20image%2020260317195424.png)

---

*遇到问题也别着急：VS Code 社区资料非常丰富；当然，你也可以直接问你的 AI 助手，它一直都在。*
