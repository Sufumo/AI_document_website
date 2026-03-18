---
title: MCP 介绍
draft: false
prev: Extensions/01-skills
next: Apps/01-vscode-usage
---

# MCP 介绍

## MCP 和 Skills 有啥区别？

MCP 和 Skills 都是 Agent 的扩展工具，用起来差别不大，但适用的场景不太一样。

**Skills** 写起来简单，用大白话描述工作流程，让 AI 知道该怎么做、要注意啥。说白了，Skills 就是预设好的提示词，还得靠 Agent 自己理解和执行，结果可能因各种因素而不太稳定。

**MCP** 则不同：输入和输出往往很明确。Agent 只能看到 MCP 给的「使用说明」，具体怎么执行的，Agent 完全不知道。比如 Google 的邮箱 MCP，Agent 只知道「用这个工具能发邮件、看邮件」，至于登录、操作这些步骤，Agent 一概不管。

所以 Skills 和 MCP 其实是互补的。拿发邮件举例：Skills 可以指挥 Agent 写某种风格的邮件，写完后让 Agent 用 Google 的 MCP 发出去。对 Skills 和 Agent 来说，MCP 怎么发的不重要，只要知道「发邮件找 MCP」就够了。

![](images/Pasted%20image%2020260317192920.png)

## 查看可用的 MCP 服务

打开 Claude Code，输入 `/mcp` 可查看当前可用的 MCP 服务。

![](./images/Pasted%20image%2020260306004713.png)

按 **Enter** 进入某个 MCP（如 **docmind**），可查看其详细信息。

![](./images/Pasted%20image%2020260306004748.png)

点击 **View tools** 可查看该 MCP 提供的全部工具。

![](./images/Pasted%20image%2020260306004911.png)

点开第一个 **convert** 工具，能看到它的功能：把 PDF 转成 Markdown。

![](./images/Pasted%20image%2020260306005027.png)

## 使用 MCP 服务

MCP 装好后，Claude Code 会自动识别这些工具；它会根据任务自动选用合适的，你也可以在对话里指定用哪一个。

下面以 **qwen-ai** MCP 为例，它提供多种能力：文本输出、翻译、图片文字识别、图片内容理解、联网搜图、网页抓取、音频转文字、视频理解等，用来扩展 Agent 的能力。

![](./images/Pasted%20image%2020260306005358.png)

![](./images/Pasted%20image%2020260306005704.png)

比如在 Claude Code 中输入 **please convert this audio file to txt and save it to output folder**，再拖入音频文件。

>[!NOTE]
>
> 也可输入 **please convert this audio file to txt and save it to output folder by qwen-ai MCP's audio_transcribe tools** 来明确指定使用某个 MCP 工具完成任务。

![](./images/Pasted%20image%2020260309115436.png)

稍等片刻，音频内容就会被转成文字。

![](images/Pasted%20image%2020260317195357.png)