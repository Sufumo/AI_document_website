---
title: Claude Code Plugins
draft: false
prev: Extensions/01-skills
next: Apps/01-vscode-usage
---

>[!TIP]
>
> If Agent extensions are new to you, skim [Skills Introduction](../01-skills) and [MCP Introduction](../02-mcp) first—you’ll install plugins faster with that context.

# Claude Code Plugins: A Pro Toolkit for Your AI

**In one sentence:** A plugin is not “more chat”—it’s a **reusable capability pack** for Claude Code: parse files, run workflows, talk to external systems, all following preset steps.

Think of Claude as a sharp collaborator who still needs the right gear. Plugins bundle tools and playbooks so it doesn’t just answer questions—it **gets work done**.

| What you gain | Why it matters |
|---------------|----------------|
| **Domain boost** | Ready-made workflows for finance, law, programming, and more |
| **External connections** | Hook up Discord, Telegram, and more—drive desktop tasks from your phone |
| **Repeatable flows** | Turn complex ops into commands and guided steps |

Official plugin directory: [https://claude.com/plugins#plugins](https://claude.com/plugins#plugins)

---

## Installing a Plugin (Skill Creator Example)

Open the marketplace and browse; each listing usually includes full usage notes and ecosystem context.

![](images/Pasted%20image%2020260329005815.png)

Open **Skill Creator** (the official plugin for building Skills). Click the copy button next to **Install in Claude Code** to copy the install command.

![](images/Pasted%20image%2020260329011248.png)

In your Agent tool, paste the command into the chat and run it to install.

![](images/Pasted%20image%2020260329011702.png)

When installation succeeds, **skill-creator** appears in your list.

![](images/Pasted%20image%2020260329012523.png)

On the plugin page you’ll see how to invoke it—typically with `/skill-creator`.

![](images/Pasted%20image%2020260329012620.png)

Restart Claude Code to refresh the plugin list, then try something like:

`/skill-creator Create a new skill that reviews PRs for security issues`

![](images/Pasted%20image%2020260329013003.png)

The plugin walks you through options and helps you build your own Skill. Submit the answers to Claude Code when you’re done.

![](images/Pasted%20image%2020260329013135.png)

![](images/Pasted%20image%2020260329013256.png)

Follow the guided flow and you’ll end up with a generated Skill—for example **security-pr-review**.

![](images/Pasted%20image%2020260330100339.png)
