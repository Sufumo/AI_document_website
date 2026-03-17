---
title: Skills Introduction
draft: false
prev: Basic-tools/05-homebrew-install
next: Extensions/02-mcp
---

# Skills Introduction

## What Is a Skill? How Does It Work?

Agents (such as Claude Code, referred to as Agent below) are built on general-purpose large language models with limited knowledge and tools. Skills extend what they can do. A Skill is like a preset workflow that guides the Agent through fixed steps to complete a task.

![](images/Pasted%20image%2020260317115400.png)

A Skill is essentially a prompt file. When the Agent uses a Skill, it combines your instructions with that Skill's description and sends both to the "brain" (the large language model) to figure out how to complete the task. Once the brain understands, it directs the local Agent to work — opening files, running programs, and so on.

For example, typing `\find-skill please help me find a Skill to summarize the article` in the Agent is like sending both the `find-skill` description and your instruction to the brain for processing.

That's the case when you call a Skill yourself. The Agent also automatically searches your computer for installed Skills in each conversation and picks suitable ones to complete tasks.

There's a catch: scanning all Skills on your computer every time uses a lot of "quota" (tokens). If Skills overlap or conflict, the Agent can get confused and perform worse. To use Skills efficiently, configure them per project or folder so the Agent doesn't see too many at once.

## Finding Your Skills

### Method 1: Ask Claude Code Directly (Works for All Launch Methods)

Open Claude Code in your project directory and send: `Which skills can be used? Please classify them to user and project skills.`

![](images/Pasted%20image%2020260317160551.png)

When Claude Code responds, you'll see two types: **User skills** (available everywhere, any folder) and **Project skills** (only in the current project).

![](images/Pasted%20image%2020260317160940.png)

### Method 2: Use the Built-in Command (Some Plugins Like VS Code Don't Support This)

Type `/skills` in Claude Code to see all available Skills in the current folder.

![](images/Pasted%20image%2020260317161647.png)

As shown: **Project skills** are for the current project only; **User skills** are global.

![](images/Pasted%20image%2020260317161948.png)

## Installing New Skills

Many creators share Skills online, and several repositories collect them for easy download. This section uses [skills.sh](https://skills.sh/) as an example to show how to install a new Skill.

Open the site and you'll see a list of Skills. Take **find-skills** — it's the command name, with 580.7k downloads, the highest on the site.

![](images/Pasted%20image%2020260317163055.png)

Open the find-skills page to see the install command (click the copy icon on the right) and a description — it's a Skill that helps you quickly find other Skills.

![](images/Pasted%20image%2020260317163547.png)

### Method 1: Let Claude Code Install It (Recommended)

Back in Claude Code, type `please help me install this skill globally`, paste the install command you copied into the input box, and it will install globally.

![](images/Pasted%20image%2020260317164410.png)

Once installed, find-skill is ready. It helps you find the best Skill for your needs on [skills.sh](https://skills.sh/).

![](images/Pasted%20image%2020260317165023.png)

For example, type `\find-skill please help me find a skill to summarize the article` to use this Skill to find new Skills.

![](images/Pasted%20image%2020260317170041.png)

Claude Code will list several Skills to choose from; pick one with high downloads and a description that fits your needs.

![](images/Pasted%20image%2020260317165826.png)

When you decide to install a Skill, copy its info into the input box and ask Claude Code to install it. For example, type `please help me install this skill just in this project`, paste the Skill info, and it will install only for the current project.

![](images/Pasted%20image%2020260317170416.png)

The Skill is now installed in the current project.

![](images/Pasted%20image%2020260317170534.png)

Ask Claude Code what Skills are available in the project.

![](images/Pasted%20image%2020260317170733.png)

The Skills you installed are now loaded correctly.

![](images/Pasted%20image%2020260317171018.png)

### Method 2: Install via Command Line

### How Skills Really Work

Claude Code's global Skills live in **~/.claude/skills** (or ~/.agent/skills — this guide uses .claude). Click **Go → Home** to open your home directory.

![](./images/Pasted%20image%2020260303192106.png)

Press `Command + Shift + .` to show hidden files, then open the **.claude** directory.

![](./images/Pasted%20image%2020260306002212.png)

If you've installed Skills before, **.claude** will have a **skills** folder.

![](./images/Pasted%20image%2020260306002332.png)

Open that folder to see your installed Skills.

![](./images/Pasted%20image%2020260306002359.png)

Each Skill folder usually contains a **SKILL.md** file — the Skill's prompt file.

![](images/Pasted%20image%2020260317171849.png)

Open **SKILL.md** to read the description. Below is the content of find-skills' md file.

![](images/Pasted%20image%2020260317171625.png)

Project-level Skills go in `.claude/skills` at the project root. As shown below, summarization is a project-level Skill.

![](images/Pasted%20image%2020260317172353.png)

### The Actual Install Flow

In short: global install = put the Skill folder in ~/.claude/skills; project-only = put it in `.claude/skills` at the project root. Most install commands do one thing: **download → put in the right place**.

This command uses `npx skills` (a Skill management tool) to run `add`, downloading from `https://github.com/vercel-labs/skills` and installing `find-skills`.

```sh
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

Open the project's Terminal.

![](images/Pasted%20image%2020260317175358.png)

Run these commands to install the skills tool first, then download find-skills.

```sh
npm install -g skills@1.4.3
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

![](images/Pasted%20image%2020260317175729.png)

You'll be prompted to choose an install directory — **.claude/skills** or **.agent/skills** both work. Here we choose Claude Code format, i.e., .claude/skills.

![](images/Pasted%20image%2020260317175754.png)

You'll be asked whether to install for the current project only (Project) or globally (Global). Choose as needed.

![](images/Pasted%20image%2020260317175936.png)

You'll be asked for the install method; choose the recommended Symlink.

![](images/Pasted%20image%2020260317180233.png)

Confirm the install and wait for it to finish.

![](images/Pasted%20image%2020260317180313.png)

When the terminal is responsive again and shows Done!, installation is complete.

![](images/Pasted%20image%2020260317180421.png)
