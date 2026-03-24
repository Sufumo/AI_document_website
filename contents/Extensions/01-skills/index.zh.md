---
title: Skills 介绍
draft: false
prev: Agents/04-claude-codel
next: Extensions/02-mcp
---

# Skills 介绍

## Skill 是什么？怎么工作的？

Agent（如 Claude Code，下文统称为 Agent）基于通用大语言模型设计，本身没有丰富的知识库与工具，因此可以通过 Skill 来扩展能力。Skill 就像一条预设好的工作流程，引导 Agent 按固定步骤完成任务。

![](images/01-skills-20260317115400.jpg)

Skill 本质上是一个提示词文件。Agent 在使用这个 Skill 完成任务时，会把你的指令和该 Skill 的说明文本结合，一起发给背后的「大脑」（大语言模型）去思考如何完成任务。大脑理解后，会指挥本地的 Agent 干活，比如打开文件编辑、运行程序等。

举个例子，在 Agent 中输入 `\find-skill 请帮我寻找总结的 Skill`，相当于把 `find-skill` 的说明文件和你的指令一起发给「大脑」去处理。

以上是主动调用 Skill 的情况。其实 Agent 也会在每次对话中自动查找你电脑里安装的 Skill，并选用合适的来完成任务。

但有个问题：如果每次对话都要把电脑里的 Skill 全扫一遍，会消耗大量「额度」（token）。如果 Skill 之间互相重复或冲突，Agent 还可能搞混，执行效果变差。所以想高效用 Skill，建议按项目或文件夹分开配置，别让 Agent 一次接触太多。

## 找到你的 Skills

### 方法1：直接问 Claude Code（适合所有打开方式）

在项目目录下打开 Claude Code，输入并发送：`Which skills can be used? Please classify them to user and project skills.`

![](images/01-skills-20260317160551.jpg)

等 Claude Code 返回结果后，就能看到两类 Skill：**User skills**（全局可用，任何文件夹都能用）和 **Project skills**（仅当前项目可用）。

![](images/01-skills-20260317160940.jpg)

### 方法2：用内置命令查看（部分插件如 VS Code 不支持）

在 Claude Code 中输入 `/skills`，可查看当前文件夹下所有可用的 Skill。

![](images/01-skills-20260317161647.jpg)

如图所示：**Project skills** 是当前项目才有的，**User skills** 是全局都能用的。

![](images/01-skills-20260317161948.jpg)

## 安装新的 Skill

网上有很多创作者分享自己的 Skill，也有不少仓库专门收集这些 Skill 方便大家下载。本节以 [skills.sh](https://skills.sh/) 为例，教你如何安装新 Skill。

打开网站，下方列表里有很多 Skill。以 **find-skills** 为例，它是指令名，右侧下载量 580.7k，是全站最高的。

![](images/01-skills-20260317163055.jpg)

点进 find-skills 的页面，能看到安装指令（点右侧复制图标即可复制）和功能介绍——它本身就是一个帮你快速找其他 Skill 的 Skill。

![](images/01-skills-20260317163547.jpg)

### 方法1：让 Claude Code 帮你装（推荐）

回到 Claude Code，输入 `please help me install this skill globally`，把刚才复制的安装命令粘贴到输入框，即可全局安装。

![](images/01-skills-20260317164410.jpg)

安装成功后，find-skill 就能用了。它的作用是帮你在 [skills.sh](https://skills.sh/) 上找最符合需求的 Skill。

![](images/01-skills-20260317165023.jpg)

比如输入 `\find-skill please help me find a skill to summarize the article`，就能调用这个 Skill 去帮你找新的 Skill。

![](images/01-skills-20260317170041.jpg)

Claude Code 会列出多个 Skill 供你选，挑下载量高、介绍符合需求的即可。

![](images/01-skills-20260317165826.jpg)

决定安装某个 Skill 后，把它的信息复制到输入框，让 Claude Code 帮你装。比如输入 `please help me install this skill just in this project`，再粘贴 Skill 信息，即可只装到当前项目。

![](images/01-skills-20260317170416.jpg)

这个 Skill 已成功装到当前项目。

![](images/01-skills-20260317170534.jpg)

问问 Claude Code 项目里有哪些可用的 Skill。

![](images/01-skills-20260317170733.jpg)

之前装的 Skill 已经正确加载了。

![](images/01-skills-20260317171018.jpg)

### 方法2：使用命令行进行安装

### Skills 的真相

Claude Code 的全局 Skill 都放在 **~/.claude/skills** 目录里（放 ~/.agent/skills 也行，本文以 .claude 为例）。依次点击 **Go → Home** 打开主目录。

![](images/01-skills-20260303192106.jpg)

按下 `Command + Shift + .` 显示隐藏文件，并打开 **.claude** 目录。

![](images/01-skills-20260306002212.jpg)

若此前已安装过 Skills，**.claude** 下会有 **skills** 文件夹。

![](images/01-skills-20260306002332.jpg)

打开该文件夹即可看到已安装的各个 Skill。

![](images/01-skills-20260306002359.jpg)

每个 Skill 目录下通常有一个 **SKILL.md** 文件，即该 Skill 的提示词文件。

![](images/01-skills-20260317171849.jpg)

打开 **SKILL.md** 可查看说明。下例为 find-skills 的 md 文件内容。

![](images/01-skills-20260317171625.jpg)

项目级的 Skill 则放在项目根目录下的 `.claude/skills` 里。如下图所示，summarization 就是一个项目级 Skill。

![](images/01-skills-20260317172353.jpg)

### 实际安装流程

总结一下：全局安装就是把 Skill 文件夹放到 ~/.claude/skills；只装给当前项目，就放到项目根目录的 `.claude/skills` 里。绝大多数安装命令做的事就是：**下载 → 放到对应位置**。

这串命令的意思是：用 `npx skills`（一个管理 Skill 的工具）的 `add` 命令，从 `https://github.com/vercel-labs/skills` 这个地址下载，并安装 `find-skills`。

```sh
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

打开项目的 Terminal 。

![](images/01-skills-20260317175358.jpg)

输入以下命令，先安装 skills 管理工具，再下载 find-skills。

```sh
npm install -g skills@1.4.3
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

![](images/01-skills-20260317175729.jpg)

会提示你选择安装目录，选 **.claude/skills** 或 **.agent/skills** 都可以，这里选 Claude Code 格式，即 .claude/skills。

![](images/01-skills-20260317175754.jpg)

会问你是只装到当前项目（Project）还是全局装（Global），按需选择即可。

![](images/01-skills-20260317175936.jpg)

会问安装方式，选推荐的 Symlink（符号链接）即可。

![](images/01-skills-20260317180233.jpg)

最后确认安装，等待完成即可。

![](images/01-skills-20260317180313.jpg)

等终端恢复可输入状态并显示 Done!，就表示装好了。

![](images/01-skills-20260317180421.jpg)
