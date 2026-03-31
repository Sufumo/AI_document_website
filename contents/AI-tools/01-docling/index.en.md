---
title: Docling Document Assistant
draft: false
prev: Agents/04-claude-codel
next: Extensions/02-mcp
---

>[!TIP]
>
> Reading the Claude Code and MCP primers first helps—but **you can skip them**: installing and smoke-testing Docling is short either way.

# Docling: Teach Your Agent to Actually Read Your Files

**The pain point:** Many agents chat well but stumble on PDFs, scans, and messy layouts.  
**What Docling does:** Helps your agent **parse, understand, and convert** documents—turning “unruly files” into structured input the agent can use. Think of it as a **document co-pilot** for your agent.

## What Docling Is For

- Handle text, tables, images, and mixed layouts quickly  
- Extend what formats your AI agent can read and reuse downstream  
- After MCP setup, run upload → convert → follow-up questions in one thread  

## Installing Docling (Agent in VS Code)

Open the Agent panel.

![](images/Pasted%20image%2020260328174138.png)

Capable agents can usually find install docs on their own. You can paste:

`Please help me install the Docling MCP service for use with an AI agent and configure the environment if necessary.`

Adding the official link helps:  
[https://docling-project.github.io/docling/usage/mcp/](https://docling-project.github.io/docling/usage/mcp/)

>[!TIP]
>
> If the agent asks for manual steps on your machine, keep asking it to **walk you through** until the MCP shows connected and a test conversion works.

![](images/Pasted%20image%2020260328204228.png)

When setup finishes, Docling is ready to use.

![](images/Pasted%20image%2020260328204409.png)

Type `/mcp` in the chat to list installed services.

![](images/Pasted%20image%2020260328204826.png)

When **docling** appears under MCP servers with **Connected**, you’re good to go.

![](images/Pasted%20image%2020260328214453.png)

On macOS, OCR-style tasks often use the built-in vision stack, so **extra paid vision APIs are usually unnecessary**. Upload a sample PDF and say:

`Please convert this PDF to Markdown.`

![](images/Pasted%20image%2020260328220635.png)

If that works, your agent can reliably read that PDF—handy for cleanup, summaries, and re-editing.

![](images/Pasted%20image%2020260328221232.png)

Per the project docs, Docling supports formats such as PDF, Word (DOCX), PowerPoint, Excel (XLSX), HTML, images (PNG, JPEG, TIFF), LaTeX, plain text, audio (WAV, MP3), subtitles (WebVTT), and more—substantially widening what your agent can handle. After install, describe your file and goal in natural language.
