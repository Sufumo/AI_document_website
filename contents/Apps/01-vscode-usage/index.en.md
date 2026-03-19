---
title: VS Code Getting Started Guide
draft: false
prev: Extensions/02-mcp
next: Apps/03-obsidian-notes
---
>[!TIP]
>
> This guide assumes you already have basic terminal and command-line skills. If not, we recommend spending 5 minutes on [Terminal Basics](../../../Basic-tools/01-terminal-basics) and [Homebrew Installation](../../../Basic-tools/05-homebrew-install); the rest will be much easier.

![](./images/Pasted%20image%2020260310143657.png)

---

# VS Code Getting Started Guide

## Why Choose VS Code?

**VS Code is an all-in-one tool for both coding and document management—like a “notebook with superpowers”:**

| Feature | What You Get | Why It Matters |
|---------|--------------|----------------|
| **Multi-language support** | Syntax highlighting for 100+ languages | Comfortable for code and docs |
| **Built-in terminal** | Open a terminal inside the editor | No need to switch windows constantly |
| **Extension marketplace** | A huge library of free extensions | Extend as you need |
| **Version control** | Visual view of file changes | See where changes come from |
| **AI assistant** | Copilot and Agent | Let AI help you get work done |

---

## Part 1: Installing VS Code

### Quick Install (Recommended ✨)

Press `Option + Space` to open Spotlight, type **Terminal**, then press Enter.

![](./images/Pasted%20image%2020260303190946.png)

Copy the following “magic spell” into the terminal and press Enter:

```bash
brew install --cask visual-studio-code
```

![](./images/Pasted%20image%2020260305170644.png)

> **What the command does:**
>
> - `brew`: Homebrew, the common package manager on macOS
> - `install`: Run the installation
> - `--cask`: Install a graphical application
> - `visual-studio-code`: The package name for VS Code

>[!NOTE]
>
> If you don’t have Homebrew yet, complete [Homebrew Installation](../../../Basic-tools/05-homebrew-install) first.

When the terminal is ready for input again, the installation is complete.

![](./images/Pasted%20image%2020260305171011.png)

---

## Part 2: VS Code Interface Tour

When you open VS Code for the first time, you’ll usually see this:

![](./images/Pasted%20image%2020260305171659.png)

### Left Sidebar (Activity Bar)

**Why it matters:** This is your project “control center.”

On the left is the **Activity Bar**. Use the icon at the top left to expand or collapse it. Main entries:

| Icon | Tool | What It’s For |
|------|------|----------------|
| 📁 | **Explorer** | Browse and manage files (like Finder) |
| 🔍 | **Search** | Search across the whole project |
| 🔀 | **Source Control** | View changes and manage history |
| 🧩 | **Extensions** | Install extensions to add features |

---

### Open Your First Folder

From the top menu, choose **File → Open Folder** and select your target folder.

![](./images/Pasted%20image%2020260305172317.png)

After opening, in the Explorer you can:

- ✅ Click folders to expand or collapse them
- ✅ Use the toolbar to create new files, new folders, or refresh the view

![](./images/Pasted%20image%2020260305173132.png)

>[!TIP]
>
> VS Code works best with plain text files (e.g. `.txt`, `.md`, `.html`). For Word, Excel, PowerPoint, and similar formats you’ll usually need extensions or other apps.

---

### Search Panel

The **Search** bar looks for matching text across the whole project (including subfolders). Results are highlighted; click a file name on the left to jump to it.

![](./images/Pasted%20image%2020260305173548.png)

---

### Source Control (Git)

>[!TIP]
>
> If you’re new to Git, we recommend spending about 10 minutes on the [Git Beginner Hands-on Guide](../../../Basic-tools/06-git-basis). That guide is more systematic; this section will then be easier to follow.

The **Source Control** view gives you a graphical way to manage changes so you don’t have to memorize many commands at once.

Click **Initialize Repository** to turn the current folder into a version-tracked repository.

>[!NOTE]
>
> Git only starts recording this folder’s history after initialization.

![](./images/Pasted%20image%2020260305173743.png)
#### Basic workflow (3 steps)

| Stage | Meaning | What You Do |
|-------|---------|-------------|
| **Changes** | Files are modified but not yet part of a commit | Edit files as usual |
| **Staged** | Choose which changes to include in this commit | Click the **+** next to the file |
| **Committed** | Changes are saved in version history | Click the blue **Commit** button |

![](./images/Pasted%20image%2020260305175821.png)

---

### Extensions Marketplace

The **Extensions** view is the marketplace for add-ons. Use it to give VS Code new capabilities.

![](./images/Pasted%20image%2020260305182927.png)

>[!TIP]
>
> After installing extensions like **Markdown All in One** or **Md Editor**, you can preview Markdown in the editor and see formatting as you type.

![](./images/Pasted%20image%2020260305183558.png)

![](./images/Pasted%20image%2020260305184231.png)

---

### Built-in Terminal

Click the **Terminal** icon in the top-right to open a terminal inside VS Code; it opens in your current project folder.

![](./images/Pasted%20image%2020260305184535.png)

Click **+** in the terminal panel to open more terminals. Use the dropdown in the bottom-right to switch or manage open terminals.

![](./images/Pasted%20image%2020260305184747.png)

---

### AI Assistant

Click the **Copilot / Agent** icon in the top-right to open the AI assistant (GitHub Copilot by default). Type instructions in the input box; the Agent will run tasks in the current directory.

![](./images/Pasted%20image%2020260305190648.png)

---

### Command Palette

Use the **Command Palette** to search for commands, settings, extensions, and more. Many features that aren’t on the main UI can be found quickly here.

![](./images/Pasted%20image%2020260305191241.png)

---

## Part 3: Document Management

### Open a Workspace

After opening VS Code, choose **File → Open Folder** and switch to the folder where you work with files.

![](./images/Pasted%20image%2020260309111111.png)

![](images/Pasted%20image%2020260317181317.png)

---

### Create Folders and Files

#### Create a New Folder

Use the toolbar next to a folder to create a new folder.

![](images/Pasted%20image%2020260317181528.png)

Type the folder name and press Enter.

![](images/Pasted%20image%2020260317181612.png)

#### Create a Subfolder

To create a subfolder inside a folder, select that folder first, then click **New Folder**.

![](images/Pasted%20image%2020260317181655.png)

#### Create a New File

You can also use the toolbar to create a new file directly inside a folder.

![](images/Pasted%20image%2020260317181733.png)

New files are empty by default; you need to type the extension yourself, e.g. `test.md`.

![](images/Pasted%20image%2020260317181755.png)

After creating, click the file in the sidebar to view or edit it.

![](images/Pasted%20image%2020260317181848.png)

>[!TIP]
>
> VS Code can create plain text files like `.txt`, `.md`, `.json` directly. For Word, Excel, PowerPoint, it’s usually better to create those in their own apps.

---

### Rename and Delete

#### Rename a File

Right-click the file and choose **Rename**, then enter the new name.

>[!TIP]
>
> On Mac, you can also select the file and press Enter to rename it quickly.

![](images/Pasted%20image%2020260317181926.png)

![](images/Pasted%20image%2020260317181938.png)

#### Rename a Folder

Same idea for folders: right-click to rename, or select and press Enter.

![](images/Pasted%20image%2020260317182048.png)

#### Delete a File or Folder

Right-click the file or folder and choose **Delete** to remove it.

![](images/Pasted%20image%2020260317182150.png)

![](images/Pasted%20image%2020260317182210.png)

---

### Find Files Quickly

When you have many files, use **Search** to find content by keyword.

![](./images/Pasted%20image%2020260306115131.png)

The file path appears at the top of the editor.

![](./images/Pasted%20image%2020260306115255.png)

Click any level in the path to browse files under that folder.

![](./images/Pasted%20image%2020260306115349.png)

>[!TIP]
>
> With extensions for PDF, Office, and other formats, you can view or edit more file types inside VS Code and switch apps less often.

![](./images/Pasted%20image%2020260306115638.png)

Search for “claude” in the Extensions search bar to find and install the Claude Code for VS Code extension.

![](images/Pasted%20image%2020260317182540.png)

Click the icon in the top-right to open the Claude Code chat window for easier use.

![](images/Pasted%20image%2020260317182749.png)


---

## Part 4: Skills and MCP in Practice

> [!TIP]
> 
> We recommend reading [Skills Introduction](../../../Extensions/01-skills) and [MCP Introduction](../../../Extensions/02-mcp) (optional) before this section.

### Why Skills and MCP?

Agents are built on general-purpose models with limited knowledge and tools; support for images, audio, and other media is also limited. So we usually extend them with **Skills** and **MCP**.

| Extension type | What it is | How to use it |
|----------------|------------|---------------|
| **Skills** | Text-based prompt files | Tell the Agent how to do a certain kind of task |
| **MCP** | Ready-made tools / APIs | Let the Agent call them directly, no need to write code from scratch |

If you’ve already installed **Agent Manager** (via `agent_manager-main.zip`) using the [GLM Configuration Guide](../../../Agents/01-GLM-configuration#method-1-visual-setup-tool-recommended-) or [KIMI Configuration Guide](../../../Agents/02-KIMI-configuration#method-1-visual-setup-tool-recommended-), you can use it to install Skills and MCP as well. This section explains what they are and how to use them in VS Code. Whether you install via the app or the command line, usage is similar.

---

### Skills: Your Task Guide

Open VS Code, choose **File → Open Folder**, and switch to your target folder.

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309111611.png)

Click the shortcut in the top-right to open the Claude Code extension chat window.

![](images/Pasted%20image%2020260317183955.png)

Type **`/file-conversion`** (the Skill’s folder name) to invoke it.

![](images/Pasted%20image%2020260317184133.png)

For example, type **please convert this pdf file to md and place this md file in the current folder**, drag in a PDF, and press Enter.

>[!WARNING]
>
> `file-conversion` requires a paid Alibaba Cloud service and API key. Try another Skill first for a demo.

![](images/Pasted%20image%2020260317184235.png)

When the task finishes, you’ll see the converted Markdown file in your workspace.

![](images/Pasted%20image%2020260317185208.png)

---

### MCP: Your Pre-built Toolbox

Unlike Skills, which rely mainly on text prompts, **MCP** is usually a separate program or service. The Agent can call it directly, so you do less coding from scratch.

Once you’ve installed and configured an MCP following its provider’s instructions, you can see and use it in Claude Code.

#### Using MCP in VS Code

Open VS Code, choose **File → Open Folder**, and switch to your target folder.

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309115212.png)

Click the Claude Code icon in the top-right to open the extension panel.

![](./images/Pasted%20image%2020260317194356.png)

Type **`/mcp`** to see the currently available MCP services.

![](./images/Pasted%20image%2020260317194423.png)

![](./images/Pasted%20image%2020260317194437.png)

Click any MCP to see its details.

![](./images/Pasted%20image%2020260317194559.png)

Click **View tools** to see all tools provided by that MCP.

For example, the **qwen-ai** MCP supports text output, translation, image text recognition, image understanding, web image search, web scraping, audio-to-text, and video understanding—greatly extending what the Agent can do.

![](./images/Pasted%20image%2020260317194620.png)

![](./images/Pasted%20image%2020260317194714.png)

For example, in Claude Code type **please convert this audio file to txt and save it to output folder**, then drag in an audio file.

![](./images/Pasted%20image%2020260317195139.png)

After a short wait, the audio is converted to text.

![](./images/Pasted%20image%2020260317195424.png)

---

*If you run into issues, don’t worry: the VS Code community has plenty of resources, and you can always ask your AI assistant—it’s there when you need it.*
