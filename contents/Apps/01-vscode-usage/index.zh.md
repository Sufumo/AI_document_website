---
title: VSCode 使用指南
draft: false
---

>[!TIP]
>
> 本教程假设你具备基本的终端和命令行知识。如果听起来有点慌，先花5分钟看看 [Terminal 基础](../../../Basic-tools/01-terminal-basics/zh) 和 [Homebrew 安装](../../../Basic-tools/05-homebrew-install/zh)，绝对物超所值。

![](./images/Pasted%20image%2020260310143657.png)

---

# VSCode 使用指南

## 为什么选 VS Code？

**VS Code 是你的全能代码编辑器和文档管理工具，相当于一个装备了超能力的文本编辑器：**

| 功能 | 你能得到什么 | 为什么重要 |
|------|-------------|-----------|
| **多语言支持** | 100+ 语言的语法高亮 | 用任何格式写代码或文档 |
| **集成终端** | 编辑器内置终端 | 不再需要切换窗口 |
| **扩展生态** | 数千个免费扩展 | 随心所欲地自定义 |
| **Git 集成** | 可视化版本控制 | 一眼看到所有变更 |
| **AI 助手** | Copilot 和 Agent 支持 | AI 驱动的编程伙伴 |

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
> - `brew`：Homebrew 的主命令，用于在 Mac 上安装软件
> - `install`：表示使用 brew 安装程序
> - `--cask`：表示安装带图形界面的应用程序，而非仅命令行工具
> - `visual-studio-code`：VS Code 的官方包名

⚠️ **注**：若尚未安装 Homebrew，请先安装 [Homebrew](../../../Basic-tools/05-homebrew-install/zh)。

等待终端恢复可输入状态即表示安装完成。

![](./images/Pasted%20image%2020260305171011.png)

---

## 第二部分：VS Code 界面导览

下面是你第一次打开 VS Code 时会看到的界面：

![](./images/Pasted%20image%2020260305171659.png)

### 左侧边栏（活动栏）

**为什么重要**：这是你项目导航的指挥中心。

左侧为**活动栏**，可通过左上角按钮打开或收起，包含：

| 图标 | 工具 | 作用 |
|------|------|------|
| 📁 | **文件资源管理器** | 浏览和管理文件（类似 Finder） |
| 🔍 | **搜索** | 在项目所有文件中查找文本 |
| 🔀 | **源代码管理（Git）** | 跟踪变更和管理版本 |
| 🧩 | **扩展** | 安装附加组件增强 VS Code |

---

### 打开你的第一个文件夹

依次点击顶部菜单 **File → Open Folder**，并选择要打开的目录。

![](./images/Pasted%20image%2020260305172317.png)

文件资源管理器中会显示已打开的文件夹，你可以：

- ✅ 点击文件夹展开或收起
- ✅ 使用工具栏新建文件、新建文件夹、刷新

![](./images/Pasted%20image%2020260305173132.png)

💡 **小贴士**：VS Code 默认更适合处理纯文本类文件（如 `.txt`、`.md`、`.html` 等）；`.docx`、`.xlsx`、`.ppt` 等格式通常仍需依赖专门扩展或外部应用。

---

### 搜索面板

**搜索**栏可根据输入内容，在当前文件夹及所有子文件夹中查找匹配的文本；匹配处会高亮显示，点击左侧文件名可快速跳转。

![](./images/Pasted%20image%2020260305173548.png)

---

### Git 源代码管理

**源代码管理**（Git）视图为 Git 命令提供图形界面，便于管理版本。

点击 **Initialize Repository** 可将当前文件夹初始化为 Git 仓库。

![](./images/Pasted%20image%2020260305173743.png)

⚠️ **注**：只有已初始化为 Git 的目录才会被 Git 跟踪和记录。

#### 理解 Git 工作流

| 阶段 | 发生了什么 | 如何操作 |
|------|-----------|----------|
| **更改** | 文件已修改但尚未暂存 | 编辑你的文件 |
| **暂存更改** | 文件准备好提交 | 点击文件旁的 **+** |
| **已提交** | 变更已保存到 Git 历史 | 点击蓝色 **Commit** 按钮 |

![](./images/Pasted%20image%2020260305175821.png)

---

### 扩展市场

**扩展**视图提供扩展市场，可在此安装扩展以增强 VS Code 功能。

![](./images/Pasted%20image%2020260305182927.png)

💡 **小贴士**：例如，安装 **Markdown All in One**、**Md Editor** 等 Markdown 扩展后，可以渲染 Markdown 语法并提供便捷预览。

![](./images/Pasted%20image%2020260305183558.png)

![](./images/Pasted%20image%2020260305184231.png)

---

### 集成终端

点击右上角**终端**图标，可在 VS Code 内打开集成终端；该终端会自动将工作目录设为当前项目目录。

![](./images/Pasted%20image%2020260305184535.png)

可通过终端面板中的 **+** 新建多个终端；右下角终端下拉菜单可管理所有已打开的终端。

![](./images/Pasted%20image%2020260305184747.png)

---

### AI 助手面板

点击右上角 **Copilot / Agent** 图标可打开 AI 助手面板，默认为 GitHub Copilot；在输入框中输入指令即可让 Agent 在当前目录下工作。

![](./images/Pasted%20image%2020260305190648.png)

---

### 命令面板

**命令面板** 可用于搜索命令、设置、扩展等内容，特别适合调用那些未直接显示在主界面上的功能。

![](./images/Pasted%20image%2020260305191241.png)

---

## 第三部分：文档管理

### 打开工作区

打开 VS Code，依次点击 **File → Open Folder**，切换到需要处理文件的文件夹。

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309120523.png)

---

### 创建文件夹和文件

#### 创建新文件夹

可使用文件夹右侧的工具栏新建文件夹。

![](./images/Pasted%20image%2020260309120646.png)

输入文件夹名并按下 Enter 即可。

![](./images/Pasted%20image%2020260309120817.png)

#### 创建子文件夹

如果想在某个文件夹下新建子文件夹，先选中该文件夹，再点击 **New Folder** 按钮即可。

![](./images/Pasted%20image%2020260309121009.png)

#### 创建新文件

也可通过同一工具栏在子文件夹中新建文件。

![](./images/Pasted%20image%2020260309121036.png)

新建的文件默认为空文件，因此需要自行填写后缀名，例如 `test.md`。

![](./images/Pasted%20image%2020260309121215.png)

此时空文件已成功创建。点击侧边栏中的文件即可查看或编辑其内容。

![](./images/Pasted%20image%2020260309121254.png)

💡 **小贴士**：VS Code 可直接新建 `.txt`、`.md`、`.json` 等纯文本文件；`.docx`、`.xlsx`、`.ppt` 等格式仍建议通过对应应用程序创建。

---

### 重命名和删除

#### 重命名文件

如果想重命名文件，可右键选择 **Rename**，然后输入新的文件名。

![](./images/Pasted%20image%2020260309121543.png)

![](./images/Pasted%20image%2020260309121646.png)

💡 **小贴士**：在 Mac 上，也可通过选中文件后按下 Enter 快速重命名文件。

![](./images/Pasted%20image%2020260309121736.png)

#### 重命名文件夹

文件夹同理，也可通过右键或选中后按下 Enter 进行重命名。

![](./images/Pasted%20image%2020260309121827.png)

#### 删除文件或文件夹

右键文件或文件夹并选择 **Delete** 即可删除对应内容。

![](./images/Pasted%20image%2020260309121920.png)

![](./images/Pasted%20image%2020260309122005.png)

---

### 快速查找文件

在文件较多的项目中，可通过**搜索**功能按关键词快速定位资料；在搜索界面输入关键词即可在项目内跳转到对应内容。

![](./images/Pasted%20image%2020260306115131.png)

文件所在路径会在编辑器上方显示。

![](./images/Pasted%20image%2020260306115255.png)

点击路径中的某一级目录即可快速浏览该文件夹下的文件。

![](./images/Pasted%20image%2020260306115349.png)

💡 **小贴士**：可安装各类文件格式对应的扩展（如 PDF、Office 等），在 VS Code 内阅读或编辑不同格式；善用扩展可将 VS Code 打造成多格式阅读与编辑环境。

![](./images/Pasted%20image%2020260306115638.png)

---

## 第四部分：Skills 和 MCP

### 为什么需要 Skills 和 MCP？

Agent 基于通用大语言模型设计，本身没有丰富的知识库与工具，对图片、音频等多媒体处理能力有限，因此需要 Skills 和 MCP 来扩展 Agent 的能力。

| 扩展类型 | 是什么 | 如何工作 |
|---------|--------|----------|
| **Skills** | 基于文本的提示文件 | 引导 Agent 完成特定任务 |
| **MCP** | 预构建的工具和 API | 为 Agent 提供直接的工具访问 |

如果你在前面的配置章节中已经按照 [GLM 配置教程](../../../Agents/01-GLM-configuration/zh/#方法一-可视化配置工具推荐-) 或 [KIMI 配置教程](../../../Agents/02-KIMI-configuration/zh/#方法一-可视化配置工具推荐-) 安装了可视化的 **Agent Manager** 应用（通过 `agent_manager-main.zip` 脚本安装的那个小程序），那么同一个应用也可以帮你用几次点击就安装和管理很多 Skills 与 MCP 集成。下面这一整部分主要讲的是 Skills 和 MCP 各自是什么、在 VS Code 中是怎样呈现的 —— 无论你是通过这个应用安装，还是直接用命令行手动配置，它们的使用方式都是类似的。

---

### Skills：你的任务专属向导

一般而言，Skill 由一个或多个提词文件组成，对特定任务进行说明。用户描述需求后，Agent 会主动匹配并调用合适的 Skill；也可通过 **`/skill-name`** 主动调用指定 Skill。

#### 找到你的 Skills

Claude Code 的 Skills 存放在 **.claude/skills** 目录。依次点击 **Go → Home** 打开 Home 目录。

![](./images/Pasted%20image%2020260303192106.png)

按下 `Command + Shift + .` 显示隐藏文件，并打开 **.claude** 目录。

![](./images/Pasted%20image%2020260306002212.png)

若此前已安装过 Skills，**.claude** 下会有 **skills** 文件夹。

![](./images/Pasted%20image%2020260306002332.png)

打开该文件夹即可看到已安装的各个 Skill。

![](./images/Pasted%20image%2020260306002359.png)

每个 Skill 目录下通常有一个 **SKILL.md** 文件，即该 Skill 的提词文件。

![](./images/Pasted%20image%2020260306002437.png)

打开 **SKILL.md** 可查看说明。下例为使用 docmind MCP 与 pandoc 进行文件格式转换的 Skill。

![](./images/Pasted%20image%2020260306002959.png)

#### 使用 Skill

打开 VS Code，依次点击 **File → Open Folder**，切换到需要处理文件的文件夹。

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309111611.png)

点击右上角的快捷按钮打开一个新的终端。

![](./images/Pasted%20image%2020260309111728.png)

输入用于启动 Claude Code 的命令。

⚠️ **注**：本教程使用 `glm` 命令启动 Claude Code，你也可以根据自己的环境改用其他启动命令。

![](./images/Pasted%20image%2020260309111952.png)

![](./images/Pasted%20image%2020260309112012.png)

输入 **`/file-conversion`**（即该 Skill 的文件夹名）即可调用该 Skill。

![](./images/Pasted%20image%2020260306002745.png)

例如输入 **please convert this pdf file to md**，拖入 PDF 文件后按下 Enter。

![](./images/Pasted%20image%2020260309112124.png)

任务完成后，即可在工作区中看到转换得到的 Markdown 文件。

![](./images/Pasted%20image%2020260309114546.png)

![](./images/Pasted%20image%2020260309114609.png)

将生成的文件拖入当前目录。

![](./images/Pasted%20image%2020260309114711.png)

此时可以看到 `test.md` 已显示在工作区中。

![](./images/Pasted%20image%2020260309114736.png)

---

### 查找与安装新 Skill

可通过 **find-skills** 这一 Skill，让 Claude Code 协助搜索并安装新的 Skill。

新建一个终端，并执行以下命令安装 **find-skills**：

```bash
npm install -g skills@1.4.3
skills add https://github.com/vercel-labs/skills --skill find-skills -y
```

![](./images/Pasted%20image%2020260309112648.png)

![](./images/Pasted%20image%2020260309112756.png)

等待命令执行完成即表示 **find-skills** 安装成功。

![](./images/Pasted%20image%2020260306101931.png)

回到 Claude Code，输入 **`/find-skills`** 即可搜索 Skill。例如输入：**find a skill that extracts the most crucial information structure and key sentences from a speech.**

![](./images/Pasted%20image%2020260309112909.png)

![](./images/Pasted%20image%2020260306102616.png)

运行结束后，Claude Code 会返回多个可选 Skill。

![](./images/Pasted%20image%2020260306102519.png)

选择其中一个（如下载量最高的），并请 Claude Code 安装，例如：**please install this skill: jwynia/agent-skills@summarization**

![](./images/Pasted%20image%2020260306102840.png)

💡 **小贴士**：新安装的 Skill 可能需重启 Claude Code 后才会出现在列表中。

安装完成后，可新建一个终端会话，必要时关闭原有终端，并在新终端中重新打开 Claude Code。

![](./images/Pasted%20image%2020260309113352.png)

输入 `/skills`，即可看到 `summarization` 这个 Skill 已成功安装。

![](./images/Pasted%20image%2020260309113605.png)

按 **ESC** 回到对话界面，输入 **please extract the most crucial information structure and key sentences from this speech** 并拖入文件。

![](./images/Pasted%20image%2020260309114300.png)

运行完成后即可看到提取出的信息结构和关键句子。

![](./images/Pasted%20image%2020260306104112.png)

---

### MCP：你的预构建工具

与主要由文字提词组成的 Skill 不同，**MCP**（Model Context Protocol）通过预置工具供 Agent 调用，减少从零编写代码的 token 消耗，并降低不确定性。

对用户而言，只需按 MCP 提供方的说明完成安装，即可在 Claude Code 中查看并调用。

#### 在 Claude Code 中使用 MCP

打开 VS Code，依次点击 **File → Open Folder**，切换到需要处理文件的文件夹。

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309115212.png)

点击右上角的快捷按钮打开一个新的终端。

![](./images/Pasted%20image%2020260309115227.png)

输入用于启动 Claude Code 的命令。

⚠️ **注**：本教程使用 `glm` 命令启动 Claude Code，你也可以根据自己的环境改用其他启动命令。

![](./images/Pasted%20image%2020260309115250.png)

![](./images/Pasted%20image%2020260309115308.png)

输入 **`/mcp`** 可查看当前可用的 MCP 服务。

![](./images/Pasted%20image%2020260306004713.png)

按 **Enter** 进入某个 MCP（如 **docmind**）可查看其详细信息。

![](./images/Pasted%20image%2020260306004748.png)

点击 **View tools** 可查看该 MCP 提供的全部工具。

![](./images/Pasted%20image%2020260306004911.png)

打开第一个 **convert** 工具可知，其功能为将 PDF 转为 Markdown。

![](./images/Pasted%20image%2020260306005027.png)

MCP 安装正确后，其工具会被 Claude Code 自动识别；Claude Code 会根据任务自动选用合适工具，也可在对话中指定使用某一工具。

以下以 **qwen-ai** 的 MCP 为例，其提供多类工具：文本输出、翻译、图片文字识别、图片内容理解、联网文搜图、联网图搜图、网页抓取、音频转录、视频理解等，用于扩展原生 Agent 能力。

![](./images/Pasted%20image%2020260306005358.png)

![](./images/Pasted%20image%2020260306005704.png)

例如在 Claude Code 中输入 **please convert this audio file to txt** 并拖入音频文件。

![](./images/Pasted%20image%2020260309115436.png)

等待片刻即可看到音频内容已被转写为文本。

![](./images/Pasted%20image%2020260309115655.png)

---

*有问题？卡住了？VS Code 社区很大。或者直接问你的 AI 助手 —— 它就在那。*
