---
permalink: /contents/Apps/01-vscode-usage/en/
lang: en


layout: doc
title: VS Code Usage Guide
---

> **Before You Dive In**
>
> This guide assumes you basic terminal and command line knowledge. If that sounds intimidating, take a quick detour to [Terminal Basics](../../../Basic-tools/01-terminal-basics/en/) and [Homebrew Installation](../../../Basic-tools/05-homebrew-install/en/) first. Trust me, it's worth the 5-minute investment.

![](./images/Pasted%20image%2020260310143657.png)

---

# VS Code Usage Guide

## The Big Picture: Why VS Code?

Here's the deal: VS Code is your all-in-one code editor and document management tool. Think of it as a supercharged text editor with superpowers:

| Feature | What You Get | Why It Matters |
|---------|--------------|----------------|
| **Multi-language Support** | Syntax highlighting for 100+ languages | Write code or docs in any format |
| **Integrated Terminal** | Terminal inside the editor | No more window switching |
| **Extension Ecosystem** | Thousands of free extensions | Customize to your heart's content |
| **Git Integration** | Visual version control | See changes at a glance |
| **AI Assistant** | Copilot and agent support | AI-powered coding partner |

---

## Part 1: Installing VS Code

### The Quick Way (Recommended ✨)

Press `Option + Space` to open the search bar, type **Terminal**, and press Enter.

![](./images/Pasted%20image%2020260303190946.png)

Copy-paste this magic spell into Terminal and hit Enter:

```bash
brew install --cask visual-studio-code
```

![](./images/Pasted%20image%2020260305170644.png)

> **Command Explanation:**
>
> - `brew`: The main command for Homebrew, used to install software on Mac
> - `install`: Tells Homebrew to install a package
> - `--cask`: Tells Homebrew to install a graphical application (GUI), not a command-line-only tool
> - `visual-studio-code`: The official package name for VS Code

⚠️ **Note**: If Homebrew is not installed yet, please install [Homebrew](../../../Basic-tools/05-homebrew-install/en/) first.

Wait until the terminal prompt returns; the installation is then complete.

![](./images/Pasted%20image%2020260305171011.png)

---

## Part 2: VS Code Interface Tour

Here's what you're looking at when you first open VS Code:

![](./images/Pasted%20image%2020260305171659.png)

### The Left Sidebar (Activity Bar)

**Why it matters**: This is your command center for navigating projects.

The left sidebar is the **Activity Bar**. You can show or hide it with the top-left button. It includes:

| Icon | Tool | What It Does |
|------|------|--------------|
| 📁 | **File Explorer** | Browse and manage files (similar to Finder) |
| 🔍 | **Search** | Find text across all files in your project |
| 🔀 | **Source Control (Git)** | Track changes and manage versions |
| 🧩 | **Extensions** | Install add-ons to enhance VS Code |

---

### Opening Your First Folder

Click **File → Open Folder** in the top menu and select a folder to open.

![](./images/Pasted%20image%2020260305172317.png)

The File Explorer shows the opened folder. You can:

- ✅ Click folders to expand or collapse them
- ✅ Use the toolbar to create files, create folders, or refresh

![](./images/Pasted%20image%2020260305173132.png)

💡 **Pro Tip**: By default, VS Code is best suited for plain-text files (e.g. `.txt`, `.md`, `.html`). Formats such as `.docx`, `.xlsx`, and `.ppt` usually require dedicated extensions or external applications.

---

### The Search Panel

The **Search** panel finds text across all files in the opened folder and subfolders. Matches are highlighted; you can click a result to jump to that file.

![](./images/Pasted%20image%2020260305173548.png)

---

### Git Source Control

The **Source Control** (Git) view provides a graphical interface for Git commands and helps you track changes.

Click **Initialize Repository** to turn the current folder into a Git repository.

![](./images/Pasted%20image%2020260305173743.png)

⚠️ **Note**: Only folders that have been initialized as a Git repository will show Git status and history.

#### Understanding Git Workflow

| Stage | What Happens | How to Do It |
|-------|--------------|--------------|
| **Changes** | Files modified but not yet staged | Edit your files |
| **Staged Changes** | Files ready to be committed | Click the **+** next to a file |
| **Committed** | Changes saved to Git history | Click the blue **Commit** button |

![](./images/Pasted%20image%2020260305175821.png)

---

### Extensions Marketplace

The **Extensions** view gives access to the extension marketplace. You can install extensions here to add new features to VS Code.

![](./images/Pasted%20image%2020260305182927.png)

💡 **Pro Tip**: For example, Markdown extensions such as **Markdown All in One** or **Md Editor** can render Markdown and provide a convenient preview.

![](./images/Pasted%20image%2020260305183558.png)

![](./images/Pasted%20image%2020260305184231.png)

---

### Integrated Terminal

Click the **Terminal** icon (near the top-right) to open the integrated terminal. This terminal starts in the current workspace folder, unlike a standalone Terminal app.

![](./images/Pasted%20image%2020260305184535.png)

Use the **+** in the terminal panel to open additional terminal instances. The terminal dropdown at the bottom-right lets you switch between or manage running terminals.

![](./images/Pasted%20image%2020260305184747.png)

---

### AI Assistant Panel

Click the **Copilot / Agent** icon (right side of the top bar) to open the AI assistant panel. The default is GitHub Copilot; you can type instructions for the agent to work in the current folder.

![](./images/Pasted%20image%2020260305190648.png)

---

### Command Palette

The **Command Palette** lets you search for commands, settings, and extensions. It is especially useful for features that are not directly visible in the main UI.

![](./images/Pasted%20image%2020260305191241.png)

---

## Part 3: Managing Documents

### Opening a Workspace

Open VS Code, then click **File → Open Folder** to switch to the folder you want to work on.

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309120523.png)

---

### Creating Folders and Files

#### Create a New Folder

Use the toolbar on the right side of the folder name to create a new folder.

![](./images/Pasted%20image%2020260309120646.png)

Type the folder name and press Enter.

![](./images/Pasted%20image%2020260309120817.png)

#### Create a Subfolder

To create a subfolder inside an existing folder, select that folder first and then click the **New Folder** button.

![](./images/Pasted%20image%2020260309121009.png)

#### Create a New File

You can also create a new file from the same toolbar inside an existing folder.

![](./images/Pasted%20image%2020260309121036.png)

New files are empty by default, so you need to type the file extension yourself, such as `test.md`.

![](./images/Pasted%20image%2020260309121215.png)

The empty file is now created successfully. Click the file in the sidebar to view or edit its contents.

![](./images/Pasted%20image%2020260309121254.png)

💡 **Pro Tip**: VS Code can directly create plain-text files such as `.txt`, `.md`, and `.json`. Files like `.docx`, `.xlsx`, and `.ppt` should still be created with their corresponding applications.

---

### Renaming and Deleting

#### Rename a File

To rename a file, right-click it and choose **Rename**. VS Code will then let you enter a new file name.

![](./images/Pasted%20image%2020260309121543.png)

![](./images/Pasted%20image%2020260309121646.png)

💡 **Pro Tip**: On Mac, you can also select a file and press Enter to rename it quickly.

![](./images/Pasted%20image%2020260309121736.png)

#### Rename a Folder

Folders can be renamed in the same way, either by right-clicking or by pressing Enter after selecting them.

![](./images/Pasted%20image%2020260309121827.png)

#### Delete Files or Folders

Right-click a file or folder and choose **Delete** to remove it.

![](./images/Pasted%20image%2020260309121920.png)

![](./images/Pasted%20image%2020260309122005.png)

---

### Finding Files Quickly

For large projects, use the **Search** feature to quickly find files by keyword. Type a keyword in the Search panel to see matching results across the project.

![](./images/Pasted%20image%2020260306115131.png)

The path to the file is shown above the editor.

![](./images/Pasted%20image%2020260306115255.png)

Click a path segment to browse files in that folder.

![](./images/Pasted%20image%2020260306115349.png)

💡 **Pro Tip**: You can also install extensions for specific file types (e.g. PDF, Office) to view or edit them inside VS Code. With the right extensions, VS Code can act as a versatile document viewer.

![](./images/Pasted%20image%2020260306115638.png)

---

## Part 4: Skills and MCP

### The Big Picture: Why Skills and MCP?

Here's the deal: Agents are built on general-purpose language models and do not ship with large knowledge bases or many built-in tools; their ability to handle images, audio, and other multimedia is limited. **Skills** and **MCP** (Model Context Protocol) extend the agent's capabilities.

| Extension Type | What It Is | How It Works |
|----------------|------------|--------------|
| **Skills** | Text-based prompt files | Guide the agent through specific tasks |
| **MCP** | Pre-built tools and APIs | Provide direct tool access to the agent |

If you followed the [GLM Configuration Guide](../../../Agents/01-GLM-configuration/en/#method-1-visual-setup-tool-recommended-) or [KIMI Configuration Guide](../../../Agents/02-KIMI-configuration/en/#method-1-visual-setup-tool-recommended-) earlier and installed the visual **Agent Manager** app (the one set up via the `agent_manager-main.zip` script), that same app can also install and manage many Skills and MCP integrations for you with a few clicks. The rest of this section focuses on what Skills and MCP are and how they appear in VS Code, whether you install them through that app or by using the command line directly.

---

### Skills: Your Task-Specific Guides

In general, a **Skill** is made up of one or more prompt files that describe how to perform a specific task. After you describe what you need, the agent can find and use the right skill, or you can call a skill directly with **`/skill-name`**.

#### Finding Your Skills

Claude Code looks for skills in the **.claude/skills** folder. Go to **Go → Home** to open your Home directory.

![](./images/Pasted%20image%2020260303192106.png)

Press `Command + Shift + .` to show hidden files, then open the **.claude** folder.

![](./images/Pasted%20image%2020260306002212.png)

If you have installed skills before, you will see a **skills** folder inside **.claude**.

![](./images/Pasted%20image%2020260306002332.png)

Open the **skills** folder to see the list of installed skills.

![](./images/Pasted%20image%2020260306002359.png)

Each skill folder usually contains a **SKILL.md** file, which is the prompt file that guides the agent for that skill.

![](./images/Pasted%20image%2020260306002437.png)

Opening **SKILL.md** shows the instructions. The example below is a skill that uses the Docmind MCP and Pandoc for file conversion.

![](./images/Pasted%20image%2020260306002959.png)

#### Using a Skill

Open VS Code, then click **File → Open Folder** to switch to the folder you want to work on.

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309111611.png)

Click the shortcut button in the top-right corner to open a new terminal.

![](./images/Pasted%20image%2020260309111728.png)

Run the command that launches Claude Code.

⚠️ **Note**: This tutorial uses the `glm` command to launch Claude Code. You can replace it with the command that is available in your own environment.

![](./images/Pasted%20image%2020260309111952.png)

![](./images/Pasted%20image%2020260309112012.png)

Type **`/file-conversion`** (the skill folder name from above) to invoke that skill.

![](./images/Pasted%20image%2020260306002745.png)

For example, type **please convert this pdf file to md**, drag in a PDF file, and press Enter.

![](./images/Pasted%20image%2020260309112124.png)

When the task finishes, the converted Markdown file will appear in the workspace.

![](./images/Pasted%20image%2020260309114546.png)

![](./images/Pasted%20image%2020260309114609.png)

Drag the generated file into the current folder.

![](./images/Pasted%20image%2020260309114711.png)

You will then see that `test.md` appears in the workspace.

![](./images/Pasted%20image%2020260309114736.png)

---

### Finding and Installing New Skills

You can use the **find-skills** skill to search for and install new skills with Claude Code.

Open a new terminal and run the following commands to install **find-skills**:

```bash
npm install -g skills@1.4.3
skills add https://github.com/vercel-labs/skills --skill find-skills -y
```

![](./images/Pasted%20image%2020260309112648.png)

![](./images/Pasted%20image%2020260309112756.png)

Wait for the commands to finish; **find-skills** is then installed.

![](./images/Pasted%20image%2020260306101931.png)

Return to Claude Code and type **`/find-skills`** to search for skills. For example: **find a skill that extracts the most crucial information structure and key sentences from a speech.**

![](./images/Pasted%20image%2020260309112909.png)

![](./images/Pasted%20image%2020260306102616.png)

When the run finishes, Claude Code will list suggested skills.

![](./images/Pasted%20image%2020260306102519.png)

Choose one (e.g. the most downloaded) and ask Claude Code to install it, e.g.: **please install this skill: jwynia/agent-skills@summarization**

![](./images/Pasted%20image%2020260306102840.png)

💡 **Pro Tip**: Newly installed skills may not appear until you restart Claude Code.

After installation, open a new terminal session, close the old one if needed, and launch Claude Code again in the new terminal.

![](./images/Pasted%20image%2020260309113352.png)

Run `/skills`, and you should see that the `summarization` skill has been installed successfully.

![](./images/Pasted%20image%2020260309113605.png)

Press **ESC** to return to the chat. For example, type **please extract the most crucial information structure and key sentences from this speech** and drag in your file.

![](./images/Pasted%20image%2020260309114300.png)

When the run completes, you will see the extracted structure and key sentences.

![](./images/Pasted%20image%2020260306104112.png)

---

### MCP: Your Pre-Built Tools

Unlike Skills (which are mostly text prompts), **MCP** (Model Context Protocol) exposes pre-built tools that the agent can call. This reduces the need for the agent to write code from scratch and makes behavior more predictable.

As a user, you only need to install an MCP according to its developer's instructions, then use Claude Code to view and call it.

#### Using MCP in Claude Code

Open VS Code, then click **File → Open Folder** to switch to the folder you want to work on.

![](./images/Pasted%20image%2020260309111111.png)

![](./images/Pasted%20image%2020260309115212.png)

Click the shortcut button in the top-right corner to open a new terminal.

![](./images/Pasted%20image%2020260309115227.png)

Run the command that launches Claude Code.

⚠️ **Note**: This tutorial uses the `glm` command to launch Claude Code. You can replace it with the command that is available in your own environment.

![](./images/Pasted%20image%2020260309115250.png)

![](./images/Pasted%20image%2020260309115308.png)

Type **`/mcp`** to see the list of available MCP servers.

![](./images/Pasted%20image%2020260306004713.png)

Press **Enter** on an MCP (e.g. **docmind**) to see its details.

![](./images/Pasted%20image%2020260306004748.png)

Click **View tools** to see all tools provided by that MCP.

![](./images/Pasted%20image%2020260306004911.png)

Opening the first **convert** tool shows that it converts PDF to Markdown.

![](./images/Pasted%20image%2020260306005027.png)

Once an MCP is installed correctly, its tools are available to Claude Code. The agent will choose the right tool for the task; you can also ask it to use a specific tool.

The following example shows **qwen-ai** MCP, which provides several tools: text output, translation, image OCR, image understanding, web search for images, image search, web scraping, audio transcription, and video understanding, extending the default agent.

![](./images/Pasted%20image%2020260306005358.png)

![](./images/Pasted%20image%2020260306005704.png)

For example, in Claude Code type **please convert this audio file to txt** and drag in an audio file.

![](./images/Pasted%20image%2020260309115436.png)

After a short wait, the transcribed text will appear.

![](./images/Pasted%20image%2020260309115655.png)

---

*Questions? Stuck somewhere? The VS Code community is huge. Or just ask your favorite AI assistant — it's literally right there.*
