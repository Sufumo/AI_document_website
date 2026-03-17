---
title: VSCode 使用指南
draft: false
---
>[!TIP]
>
> 本教程假设你具备基本的终端和命令行知识。若对此不太熟悉，建议先花 5 分钟阅读 [Terminal 基础](../../../Basic-tools/01-terminal-basics) 和 [Homebrew 安装](../../../Basic-tools/05-homebrew-install)，绝对物超所值。

![](./images/Pasted%20image%2020260310143657.png)

---

# VSCode 使用指南

## 为什么选 VS Code？

**VS Code 是全能型代码编辑器和文档管理工具，就像一个「会魔法的记事本」：**

| 功能 | 你能得到什么 | 为什么重要 |
|------|-------------|-----------|
| **多语言支持** | 100+ 种语言的语法高亮 | 写代码、写文档都能用 |
| **内置终端** | 编辑器里直接开终端 | 不用来回切窗口 |
| **扩展市场** | 数千个免费插件 | 想装啥装啥 |
| **版本管理** | 图形化查看文件改动 | 改了什么一目了然 |
| **AI 助手** | Copilot 和 Agent | 让 AI 帮你写代码 |

---

## 第一部分：VS Code 安装

### 快速安装（推荐 ✨）

按 `Option + Space` 打开搜索界面，输入 **Terminal** 并按下 Enter。

![](./images/Pasted%20image%2020260303190946.png)

复制这段「魔法咒语」到终端，按下 Enter：

```bash
brew install --cask visual-studio-code
```

![](./images/Pasted%20image%2020260305170644.png)

> **命令解释：**
>
> - `brew`：Mac 上的软件安装工具 Homebrew
> - `install`：安装的意思
> - `--cask`：装带界面的应用（不是那种只能敲命令的）
> - `visual-studio-code`：VS Code 的包名

⚠️ **注**：若尚未安装 Homebrew，请先安装 [Homebrew](../../../Basic-tools/05-homebrew-install)。

等终端可以继续输入、不再卡住时，就说明装好了。

![](./images/Pasted%20image%2020260305171011.png)

---

## 第二部分：VS Code 界面导览

下面是你第一次打开 VS Code 时会看到的界面：

![](./images/Pasted%20image%2020260305171659.png)

### 左侧边栏（活动栏）

**为啥重要**：这是你管理项目的「控制台」。

左侧是**活动栏**，点左上角按钮可展开或收起，里面有这些工具：

| 图标 | 工具 | 干啥用的 |
|------|------|------|
| 📁 | **文件** | 浏览、管理文件（类似 Finder） |
| 🔍 | **搜索** | 在整个项目里找文字 |
| 🔀 | **版本管理** | 看文件改了什么、管理历史 |
| 🧩 | **扩展** | 装插件，给 VS Code 加功能 |

---

### 打开你的第一个文件夹

依次点击顶部菜单 **File → Open Folder**，并选择要打开的目录。

![](./images/Pasted%20image%2020260305172317.png)

文件资源管理器中会显示已打开的文件夹，你可以：

- ✅ 点击文件夹展开或收起
- ✅ 使用工具栏新建文件、新建文件夹、刷新

![](./images/Pasted%20image%2020260305173132.png)

💡 **小贴士**：VS Code 更适合处理纯文本（如 `.txt`、`.md`、`.html`）；Word、Excel、PPT 这类格式一般要装专门插件或用别的软件打开。

---

### 搜索面板

**搜索**栏能按你输入的内容，在整个项目（含子文件夹）里找匹配的文字；找到的地方会高亮，点左侧文件名就能跳过去。

![](./images/Pasted%20image%2020260305173548.png)

---

### 版本管理（Git）

**版本管理**视图用图形界面帮你管理文件改动，不用记命令。

点击 **Initialize Repository** 可以把当前文件夹变成「可追踪版本」的仓库。

![](./images/Pasted%20image%2020260305173743.png)

⚠️ **注**：只有初始化过的文件夹才会被记录改动。

#### 基本流程

| 阶段 | 啥意思 | 怎么操作 |
|------|-----------|----------|
| **有改动** | 文件改了但还没「登记」 | 直接编辑文件 |
| **准备提交** | 选好要保存的改动 | 点文件旁的 **+** |
| **已保存** | 改动已写入历史 | 点蓝色 **Commit** 按钮 |

![](./images/Pasted%20image%2020260305175821.png)

---

### 扩展市场

**扩展**视图就是插件商店，在这里装插件来给 VS Code 加功能。

![](./images/Pasted%20image%2020260305182927.png)

💡 **小贴士**：装 **Markdown All in One**、**Md Editor** 等插件后，就能直接预览 Markdown 效果，不用自己脑补排版。

![](./images/Pasted%20image%2020260305183558.png)

![](./images/Pasted%20image%2020260305184231.png)

---

### 内置终端

点右上角**终端**图标，就能在 VS Code 里开一个终端，而且会自动进到当前项目目录。

![](./images/Pasted%20image%2020260305184535.png)

点终端面板里的 **+** 可以多开几个终端；右下角的下拉菜单可以切换、管理已打开的终端。

![](./images/Pasted%20image%2020260305184747.png)

---

### AI 助手

点右上角 **Copilot / Agent** 图标打开 AI 助手，默认是 GitHub Copilot；在输入框里发指令，Agent 就会在当前目录下帮你干活。

![](./images/Pasted%20image%2020260305190648.png)

---

### 命令面板

**命令面板**可以搜命令、设置、扩展等，那些没摆在明面上的功能，多半都能从这里找到。

![](./images/Pasted%20image%2020260305191241.png)

---

## 第三部分：文档管理

### 打开工作区

打开 VS Code，依次点击 **File → Open Folder**，切换到需要处理文件的文件夹。

![](./images/Pasted%20image%2020260309111111.png)

![](images/Pasted%20image%2020260317181317.png)

---

### 创建文件夹和文件

#### 创建新文件夹

可使用文件夹右侧的工具栏按钮新建文件夹。

![](images/Pasted%20image%2020260317181528.png)

输入文件夹名并按下 Enter 即可。

![](images/Pasted%20image%2020260317181612.png)

#### 创建子文件夹

如果想在某个文件夹下新建子文件夹，先选中该文件夹，再点击 **New Folder** 按钮即可。

![](images/Pasted%20image%2020260317181655.png)

#### 创建新文件

也可通过同一工具栏在文件夹中新建文件。

![](images/Pasted%20image%2020260317181733.png)

新建的文件默认为空文件，需要自行输入后缀名，例如 `test.md`。

![](images/Pasted%20image%2020260317181755.png)

此时空文件已成功创建。点击侧边栏中的文件即可查看或编辑其内容。

![](images/Pasted%20image%2020260317181848.png)

💡 **小贴士**：VS Code 可以直接新建 `.txt`、`.md`、`.json` 等纯文本文件；Word、Excel、PPT 这类建议用对应软件创建。

---

### 重命名和删除

#### 重命名文件

若要重命名文件，可右键点击文件并选择 **Rename**，然后输入新的文件名。

💡 **小贴士**：在 Mac 上，也可选中文件后按下 Enter 键快速重命名。

![](images/Pasted%20image%2020260317181926.png)

![](images/Pasted%20image%2020260317181938.png)

#### 重命名文件夹

文件夹同理，可通过右键选择，或选中后按下 Enter 键进行重命名。

![](images/Pasted%20image%2020260317182048.png)

#### 删除文件或文件夹

右键文件或文件夹并选择 **Delete** 即可删除对应内容。

![](images/Pasted%20image%2020260317182150.png)

![](images/Pasted%20image%2020260317182210.png)

---

### 快速查找文件

在文件较多的项目中，可通过**搜索**功能按关键词快速定位文件；在搜索界面输入关键词即可在项目内跳转到对应内容。

![](./images/Pasted%20image%2020260306115131.png)

文件所在路径会在编辑器上方显示。

![](./images/Pasted%20image%2020260306115255.png)

点击路径中的某一级目录即可快速浏览该文件夹下的文件。

![](./images/Pasted%20image%2020260306115349.png)

💡 **小贴士**：装 PDF、Office 等格式对应的插件后，就能在 VS Code 里直接看、直接改这些文件，一个应用搞定多种格式。

![](./images/Pasted%20image%2020260306115638.png)

在扩展搜索栏输入「claude」，可搜索并安装 Claude Code for VS Code 插件。

![](images/Pasted%20image%2020260317182540.png)

点击右上角的图标可打开 Claude Code 的对话窗口，以便更方便地使用 Claude Code。

![](images/Pasted%20image%2020260317182749.png)


---

## 第四部分：Skills 和 MCP 实战

> [!TIP]
> 
> 本章节建议先阅读 [Skills 介绍](../../../Extensions/01-skills) 和 [MCP 介绍](../../../Extensions/02-mcp)（选读），再继续阅读。

### 为啥需要 Skills 和 MCP？

Agent 基于通用大模型，本身知识库和工具有限，对图片、音频等处理能力也一般，所以需要 Skills 和 MCP 来「加技能」。

| 扩展类型 | 是啥 | 咋用 |
|------|------|------|
| **Skills** | 基于文字的提示文件 | 告诉 Agent 该怎么做某件事 |
| **MCP** | 现成的工具/接口 | 让 Agent 直接调用，不用自己写代码 |

如果你在前面的配置章节里已经按 [GLM 配置教程](../../../Agents/01-GLM-configuration#方法一-可视化配置工具推荐-) 或 [KIMI 配置教程](../../../Agents/02-KIMI-configuration#方法一-可视化配置工具推荐-) 安装了 **Agent Manager** 小程序（通过 `agent_manager-main.zip`），那同一个应用也能帮你装 Skills 和 MCP。下面这一整块主要讲 Skills 和 MCP 是啥、在 VS Code 里长啥样 —— 不管你是用应用装的还是命令行装的，用起来都一样。

---

### Skills：你的任务专属向导

打开 VS Code，依次点击 **File → Open Folder**，切换到需要处理文件的文件夹。

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309111611.png)

点击右上角的快捷按钮打开 Claude Code 插件的对话窗口。

![](images/Pasted%20image%2020260317183955.png)

输入 **`/file-conversion`**（即该 Skill 的文件夹名）即可调用该 Skill。

![](images/Pasted%20image%2020260317184133.png)

比如输入 **please convert this pdf file to md and place this md file in the current folder**，拖入 PDF 文件后按 Enter。

>[!Warning]
> file-conversion 需要用到阿里云付费服务并填写 API Key，建议读者换用其他 Skill 来测试。

![](images/Pasted%20image%2020260317184235.png)

任务完成后，即可在工作区中看到转换得到的 Markdown 文件。

![](images/Pasted%20image%2020260317185208.png)

---

### MCP：你的预构建工具

和 Skill 主要由文字提示不同，**MCP** 大多是独立的程序或服务，Agent 直接调用就行，不用从零写代码，省时省力。

你只需要按 MCP 提供方的说明装好、配置好，就能在 Claude Code 里看到并用了。

#### 在 VSCode 中使用 MCP

打开 VS Code，依次点击 **File → Open Folder**，切换到需要处理文件的文件夹。

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309115212.png)

点击右上角的 Claude Code 标志打开 Claude Code 插件。

![](images/Pasted%20image%2020260317194356.png)

输入 **`/mcp`** 可查看当前可用的 MCP 服务。

![](images/Pasted%20image%2020260317194423.png)

![](images/Pasted%20image%2020260317194437.png)

点击进入某个 MCP 可查看其详细信息。

![](images/Pasted%20image%2020260317194559.png)

点击 **View tools** 可查看该 MCP 提供的全部工具。

比如 **qwen-ai** MCP 提供多种能力：文本输出、翻译、图片文字识别、图片内容理解、联网搜图、网页抓取、音频转文字、视频理解等，用来扩展 Agent 的能力。

![](images/Pasted%20image%2020260317194620.png)

![](images/Pasted%20image%2020260317194714.png)

比如在 Claude Code 里输入 **please convert this audio file to txt and save it to output folder**，再拖入音频文件。

![](images/Pasted%20image%2020260317195139.png)

稍等片刻，音频就会被转成文字。

![](images/Pasted%20image%2020260317195424.png)

---

*有问题？卡住了？VS Code 社区资源丰富。或者直接问问你的 AI 助手 —— 它就在那里。*
