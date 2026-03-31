---
title: Docling 文档助手
draft: false
prev: Agents/04-claude-codel
next: Extensions/02-mcp
---

>[!TIP]
>
> 若你还没读过 Claude Code 与 MCP 的入门，理解会更快；**没读过也不碍事**——Docling 的安装与验证步骤本身很短，跟着做即可。

# Docling：让 Agent 真正「读懂」你的文档

**痛点很真实：** 很多 Agent 擅长对话，却对 PDF、扫描件、复杂版式束手无策。  
**Docling 的定位：** 帮 Agent **解析、理解、转换**各类文档，把「乱七八糟的文件」变成 Agent 能直接用的结构化信息——相当于给 Agent 配了一位**文档管家**。

## Docling 能做什么

- 快速处理文字、表格、图片混排的文档  
- 与 AI Agent 配合，扩展其可读格式与下游用法  
- 通过 MCP 接入后，在对话里完成「上传 → 转换 → 追问」闭环  

## 安装 Docling（以 VS Code 中的 Agent 为例）

首先打开 Agent 窗口。

![](images/Pasted%20image%2020260328174138.png)

能力较强的 Agent 通常能自行检索安装说明。你可以直接输入：

`Please help me install the Docling MCP service for use with an AI agent and configure the environment if necessary.`

同时附上官方文档链接效果更好：  
[https://docling-project.github.io/docling/usage/mcp/](https://docling-project.github.io/docling/usage/mcp/)

>[!TIP]
>
> 若 Agent 提示需要本机手动步骤，可继续让它**一步步协助配置**，直到 MCP 显示已连接、能完成一次测试转换为止。

![](images/Pasted%20image%2020260328204228.png)

配置完成后，Docling 即就绪。

![](images/Pasted%20image%2020260328204409.png)

在对话框输入 `/mcp`，查看已安装的服务。

![](images/Pasted%20image%2020260328204826.png)

当 **docling** 出现在 MCP 列表中且状态为 **Connected**，说明可以正式使用。

![](images/Pasted%20image%2020260328214453.png)

在 macOS 上，需要图像识别时，Docling 通常会使用系统自带能力，**一般不产生额外外部服务费用**。可上传示例 PDF，并输入：

`Please convert this PDF to Markdown.`

![](images/Pasted%20image%2020260328220635.png)

若转换成功，说明 Agent 已能稳定读取该 PDF 内容——对整理资料、快速抓重点、二次编辑都很有用。

![](images/Pasted%20image%2020260328221232.png)

据官方说明，Docling 支持多种格式，例如：PDF、Word（DOCX）、PPT、Excel（XLSX）、HTML、图片（PNG、JPEG、TIFF）、LaTeX、纯文本、音频（WAV、MP3）、字幕（WebVTT）等，能显著扩展 Agent 的文档能力。安装后若有具体格式需求，直接向 Agent 描述任务即可。
