---
title: MCP Introduction
draft: false
prev: Extensions/01-skills
---

# MCP Introduction

## What's the Difference Between MCP and Skills?

MCP and Skills are both Agent extensions. They feel similar to use, but they fit different scenarios.

**Skills** are easy to write — you describe the workflow in plain language so the AI knows what to do and what to watch for. In short, Skills are preset prompts that the Agent still has to interpret and run; results can vary.

**MCP** is different: inputs and outputs are usually well-defined. The Agent only sees the "instructions" the MCP provides; it has no idea how the work is actually done. For example, with Google's email MCP, the Agent only knows "this tool can send and read email" — it doesn't handle login or the steps behind it.

So Skills and MCP complement each other. For email: a Skill can tell the Agent how to write a certain style of email, then have the Agent use Google's MCP to send it. For the Skill and Agent, how MCP sends the email doesn't matter — they just need to know "use MCP for sending."

![](images/Pasted%20image%2020260317192920.png)

## Viewing Available MCP Services

Open Claude Code and type `/mcp` to see available MCP services.

![](./images/Pasted%20image%2020260306004713.png)

Press **Enter** on an MCP (e.g., **docmind**) to view its details.

![](./images/Pasted%20image%2020260306004748.png)

Click **View tools** to see all tools provided by that MCP.

![](./images/Pasted%20image%2020260306004911.png)

Open the first **convert** tool to see its function: convert PDF to Markdown.

![](./images/Pasted%20image%2020260306005027.png)

## Using MCP Services

Once MCP is installed, Claude Code automatically detects its tools. It picks suitable ones based on the task, and you can also specify which to use in the conversation.

Below we use **qwen-ai** MCP as an example. It offers: text output, translation, image OCR, image understanding, web search, web scraping, audio transcription, video understanding, and more — extending the Agent's capabilities.

![](./images/Pasted%20image%2020260306005358.png)

![](./images/Pasted%20image%2020260306005704.png)

For example, type **please convert this audio file to txt and save it to output folder** in Claude Code, then drag in an audio file.

>[!NOTE]
> You can also type **please convert this audio file to txt and save it to output folder by qwen-ai MCP's audio_transcribe tools** to explicitly use a specific MCP tool.

![](./images/Pasted%20image%2020260309115436.png)

After a moment, the audio will be transcribed to text.

![](images/Pasted%20image%2020260317195357.png)
