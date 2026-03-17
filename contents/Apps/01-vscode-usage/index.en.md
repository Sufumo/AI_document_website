---
title: VS Code Usage Guide
draft: false
---
>[!TIP]
>
> This tutorial assumes basic terminal and command-line knowledge. If that sounds unfamiliar, we recommend spending 5 minutes on [Terminal Basics](../../../Basic-tools/01-terminal-basics) and [Homebrew Installation](../../../Basic-tools/05-homebrew-install) first — it's worth it.

![](./images/Pasted%20image%2020260310143657.png)

---

# VS Code Usage Guide

## Why VS Code?

**VS Code is an all-in-one code editor and document manager — like a "magic notepad" that does more:**

| Feature | What You Get | Why It Matters |
|------|-------------|-----------|
| **Multi-language support** | Syntax highlighting for 100+ languages | Write code and docs in any format |
| **Built-in terminal** | Open a terminal right inside the editor | No more switching windows |
| **Extension marketplace** | Thousands of free plugins | Install whatever you need |
| **Version control** | Visual view of file changes | See exactly what changed |
| **AI assistant** | Copilot and Agent | Let AI help you code |

---

## Part 1: Installing VS Code

### Quick Install (Recommended ✨)

Press `Option + Space` to open Spotlight, type **Terminal**, and press Enter.

![](./images/Pasted%20image%2020260303190946.png)

Copy this "magic spell" into the terminal and press Enter:

```bash
brew install --cask visual-studio-code
```

![](./images/Pasted%20image%2020260305170644.png)

> **What this does:**
>
> - `brew`: Homebrew, the package manager for Mac
> - `install`: The install command
> - `--cask`: Install a GUI app (not command-line only)
> - `visual-studio-code`: VS Code's package name

⚠️ **Note**: If you don't have Homebrew yet, install [Homebrew](../../../Basic-tools/05-homebrew-install) first.

When the terminal becomes responsive again and stops processing, installation is complete.

![](./images/Pasted%20image%2020260305171011.png)

---

## Part 2: VS Code Interface Tour

Here's what you'll see when you first open VS Code:

![](./images/Pasted%20image%2020260305171659.png)

### Left Sidebar (Activity Bar)

**Why it matters**: This is your project "control center."

The **Activity Bar** is on the left. Click the button in the top-left to expand or collapse it. It contains:

| Icon | Tool | What It Does |
|------|------|------|
| 📁 | **Explorer** | Browse and manage files (like Finder) |
| 🔍 | **Search** | Find text across your entire project |
| 🔀 | **Source Control** | View file changes and manage history |
| 🧩 | **Extensions** | Install plugins to extend VS Code |

---

### Open Your First Folder

Click **File → Open Folder** in the top menu, then select the folder you want to open.

![](./images/Pasted%20image%2020260305172317.png)

The Explorer will show the opened folder. You can:

- ✅ Click folders to expand or collapse them
- ✅ Use the toolbar to create files, create folders, or refresh

![](./images/Pasted%20image%2020260305173132.png)

💡 **Tip**: VS Code works best with plain text files (`.txt`, `.md`, `.html`); Word, Excel, and PowerPoint files usually need dedicated extensions or other apps.

---

### Search Panel

The **Search** bar finds matching text across your project (including subfolders). Matches are highlighted, and you can click a filename on the left to jump to it.

![](./images/Pasted%20image%2020260305173548.png)

---

### Source Control (Git)

The **Source Control** view gives you a graphical interface for managing file changes — no need to memorize Git commands.

Click **Initialize Repository** to turn the current folder into a version-tracked repository.

![](./images/Pasted%20image%2020260305173743.png)

⚠️ **Note**: Only initialized folders will have their changes tracked.

#### Basic Workflow

| Stage | Meaning | How to Do It |
|------|-----------|----------|
| **Modified** | File changed but not yet "staged" | Edit your file |
| **Staged** | Ready to save these changes | Click **+** next to the file |
| **Committed** | Changes saved to history | Click the blue **Commit** button |

![](./images/Pasted%20image%2020260305175821.png)

---

### Extensions Marketplace

The **Extensions** view is the plugin store — install extensions here to add features to VS Code.

![](./images/Pasted%20image%2020260305182927.png)

💡 **Tip**: Install **Markdown All in One**, **Md Editor**, or similar Markdown extensions to preview Markdown rendering without guessing the layout.

![](./images/Pasted%20image%2020260305183558.png)

![](./images/Pasted%20image%2020260305184231.png)

---

### Built-in Terminal

Click the **Terminal** icon in the top-right to open a terminal inside VS Code. It automatically starts in your current project directory.

![](./images/Pasted%20image%2020260305184535.png)

Click **+** in the terminal panel to open more terminals; use the dropdown in the bottom-right to switch between or manage open terminals.

![](./images/Pasted%20image%2020260305184747.png)

---

### AI Assistant

Click the **Copilot / Agent** icon in the top-right to open the AI assistant (default is GitHub Copilot). Type instructions in the input box, and the Agent will work in the current directory.

![](./images/Pasted%20image%2020260305190648.png)

---

### Command Palette

The **Command Palette** lets you search for commands, settings, extensions, and more. Features that aren't visible in the main UI are often found here.

![](./images/Pasted%20image%2020260305191241.png)

---

## Part 3: Document Management

### Open a Workspace

Open VS Code, click **File → Open Folder**, and switch to the folder where you want to work with files.

![](./images/Pasted%20image%2020260309111111.png)

![](images/Pasted%20image%2020260317181317.png)

---

### Create Folders and Files

#### Create a New Folder

Use the toolbar button next to a folder to create a new folder.

![](images/Pasted%20image%2020260317181528.png)

Type the folder name and press Enter.

![](images/Pasted%20image%2020260317181612.png)

#### Create a Subfolder

To create a subfolder inside another folder, select that folder first, then click the **New Folder** button.

![](images/Pasted%20image%2020260317181655.png)

#### Create a New File

You can also create files in a folder using the same toolbar.

![](images/Pasted%20image%2020260317181733.png)

New files are empty by default; you need to type the file extension yourself (e.g., `test.md`).

![](images/Pasted%20image%2020260317181755.png)

The empty file is now created. Click it in the sidebar to view or edit its content.

![](images/Pasted%20image%2020260317181848.png)

💡 **Tip**: VS Code can create plain text files like `.txt`, `.md`, `.json` directly; Word, Excel, and PowerPoint files are best created in their respective apps.

---

### Rename and Delete

#### Rename a File

To rename a file, right-click it and choose **Rename**, then enter the new name.

💡 **Tip**: On Mac, you can also select a file and press Enter to rename it quickly.

![](images/Pasted%20image%2020260317181926.png)

![](images/Pasted%20image%2020260317181938.png)

#### Rename a Folder

Same for folders — right-click and choose Rename, or select and press Enter.

![](images/Pasted%20image%2020260317182048.png)

#### Delete a File or Folder

Right-click the file or folder and choose **Delete** to remove it.

![](images/Pasted%20image%2020260317182150.png)

![](images/Pasted%20image%2020260317182210.png)

---

### Quick File Search

In projects with many files, use **Search** to find files by keyword. Type a keyword in the search panel to jump to matching content in the project.

![](./images/Pasted%20image%2020260306115131.png)

The file path appears at the top of the editor.

![](./images/Pasted%20image%2020260306115255.png)

Click any level in the path to quickly browse files in that folder.

![](./images/Pasted%20image%2020260306115349.png)

💡 **Tip**: Install extensions for PDF, Office, and other formats to view and edit them directly in VS Code — one app for many formats.

![](./images/Pasted%20image%2020260306115638.png)

Type "claude" in the extension search bar to find and install the Claude Code for VS Code extension.

![](images/Pasted%20image%2020260317182540.png)

Click the icon in the top-right to open Claude Code's chat window for easier use.

![](images/Pasted%20image%2020260317182749.png)


---

## Part 4: Skills and MCP in Action

> [!TIP]
> 
> We recommend reading [Skills Introduction](../../../Extensions/01-skills) and [MCP Introduction](../../../Extensions/02-mcp) (optional) before continuing.

### Why Skills and MCP?

Agents are built on general-purpose models with limited knowledge and tools, and modest support for images, audio, and other media. Skills and MCP extend what they can do.

| Extension Type | What It Is | How It Works |
|------|------|------|
| **Skills** | Text-based prompt files | Tell the Agent how to do a specific task |
| **MCP** | Ready-made tools and APIs | Let the Agent call them directly — no coding from scratch |

If you've already installed the **Agent Manager** app (via `agent_manager-main.zip`) from the [GLM Configuration](../../../Agents/01-GLM-configuration) or [KIMI Configuration](../../../Agents/02-KIMI-configuration) tutorials, that same app can install Skills and MCP too. This section covers what Skills and MCP are and how they appear in VS Code — whether you install via the app or the command line, usage is the same.

---

### Skills: Your Task Guide

Open VS Code, click **File → Open Folder**, and switch to the folder where you want to work with files.

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309111611.png)

Click the shortcut button in the top-right to open the Claude Code plugin's chat window.

![](images/Pasted%20image%2020260317183955.png)

Type **`/file-conversion`** (the Skill's folder name) to invoke that Skill.

![](images/Pasted%20image%2020260317184133.png)

For example, type **please convert this pdf file to md and place this md file in the current folder**, drag in a PDF file, and press Enter.

>[!Warning]
> file-conversion requires Alibaba Cloud paid services and an API Key. We recommend using another Skill for testing.

![](images/Pasted%20image%2020260317184235.png)

When the task completes, you'll see the converted Markdown file in your workspace.

![](images/Pasted%20image%2020260317185208.png)

---

### MCP: Your Pre-built Tools

Unlike Skills (which are mostly text prompts), **MCP** is usually a standalone program or service that the Agent calls directly — no need to write code from scratch.

Just install and configure according to the MCP provider's instructions, and you'll see and use it in Claude Code.

#### Using MCP in VS Code

Open VS Code, click **File → Open Folder**, and switch to the folder where you want to work.

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309115212.png)

Click the Claude Code icon in the top-right to open the Claude Code plugin.

![](images/Pasted%20image%2020260317194356.png)

Type **`/mcp`** to see available MCP services.

![](images/Pasted%20image%2020260317194423.png)

![](images/Pasted%20image%2020260317194437.png)

Click into an MCP to view its details.

![](images/Pasted%20image%2020260317194559.png)

Click **View tools** to see all tools provided by that MCP.

For example, **qwen-ai** MCP offers: text output, translation, image OCR, image understanding, web search, web scraping, audio transcription, video understanding, and more — extending the Agent's capabilities.

![](images/Pasted%20image%2020260317194620.png)

![](images/Pasted%20image%2020260317194714.png)

For example, type **please convert this audio file to txt and save it to output folder** in Claude Code, then drag in an audio file.

![](images/Pasted%20image%2020260317195139.png)

After a moment, the audio will be transcribed to text.

![](images/Pasted%20image%2020260317195424.png)

---

*Stuck? VS Code has a large community. Or just ask your AI assistant — it's right there.*
