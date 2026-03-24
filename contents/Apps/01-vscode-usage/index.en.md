---
title: A Gentle Introduction to VSCode
draft: false
prev: Extensions/02-mcp
next: Apps/03-obsidian-notes
---
# Introduction to VSCode

## What is VSCode? Why is VSCode recommended?

Visual Studio Code is essentially a workspace for viewing, editing, and managing files on your computer—not where the files are actually stored. Think of your computer as a room where all your files are neatly stored in a filing cabinet; VS Code is more like a desk. When you open it, you simply take out the files you need and lay them out on the desk to work on them. Any changes you make on the desk—such as editing, saving, or deleting—directly affect the original files in the filing cabinet.

From this perspective, VS Code can be understood as a tool that integrates file browsing, searching, and text editing, allowing you to search for, view, and modify files all within the same interface. At the same time, its capabilities can be continuously expanded by installing extensions. For example, tools like Claude Code can be used directly within VS Code, enabling you to perform development and AI-assisted tasks within the same environment.

![](images/01-vscode-usage-20260310143657.jpg)

---

## Part 1: Installing VS Code

### Quick Installation (Recommended ✨)

>[!TIP]
>
> This section assumes you already have basic terminal and command-line skills. If you’re not familiar with these, we recommend spending 5 minutes reading [Terminal Basics](../../../Basic-tools/01-terminal-basics) and [Homebrew Installation](../../../Basic-tools/05-homebrew-install) first—it will make the rest of the process much easier.


Press `Option + Space` to open the search bar, type **Terminal**, and then press Enter.

![](images/01-vscode-usage-20260303190946.jpg)

Copy the following “magic spell” into the terminal and press Enter:

```bash
brew install --cask visual-studio-code
```

![](images/01-vscode-usage-20260305170644.jpg)

> **Command Explanation:**
>
> - `brew`: Homebrew, the standard package manager for macOS
> - `install`: Executes the installation
> - `--cask`: Installs applications with a graphical user interface
> - `visual-studio-code`: The package name for VS Code

>[!NOTE]
>
> If you haven’t installed Homebrew yet, please complete the [Homebrew installation](../../../Basic-tools/05-homebrew-install) first.

When the terminal returns to a state where you can type, the installation is complete.

![](images/01-vscode-usage-20260305171011.jpg)

---

## Part 2: VS Code Interface Overview

When you open VS Code for the first time, you will typically see the following interface:

![](images/01-vscode-usage-20260305171659.jpg)

### Left Sidebar (Activity Panel)

**Why it matters**: This is your project’s “control center.”

On the left is the **Activity Panel**. Click the button in the top-left corner to expand or collapse it. Common shortcuts are as follows:

| Icon | Tool | Main Purpose |
|------|------|------|
| 📁 | **Files** | Browse and manage files (similar to Finder) |
| 🔍 | **Search** | Search for content across the entire project |
| 🔀 | **Version Control** | View changes and manage history |
| 🧩 | **Extensions** | Install plugins to enhance functionality |

---

### Open Your First Folder

Click **File → Open Folder** in the top menu, then select the target directory.

![](images/01-vscode-usage-20260305172317.jpg)

Once opened, you can do the following in the Explorer:

- ✅ Click a folder to expand or collapse it
- ✅ Use the toolbar to create new files, create new folders, or refresh the view

![](images/01-vscode-usage-20260305173132.jpg)

>[!TIP]
>
> VS Code is better suited for handling plain text files (such as `.txt`, `.md`, `.html`); formats like Word, Excel, and PPT typically require plugins or external applications.

---

### Search Panel

The **Search** bar searches for matching text throughout the entire project (including subfolders); results are highlighted, and you can quickly navigate to them by clicking the filename on the left.

![](images/01-vscode-usage-20260305173548.jpg)

---

### Version Control (Git)

>[!TIP]
>
> If you're not yet familiar with Git, we recommend spending 10 minutes reading the [Git Practical Getting Started Guide](../../../Basic-tools/06-git-basis). That guide is more systematic, making it easier to get started here.

The **Version Control** view provides a graphical interface that lets you manage changes more intuitively, so you don’t have to memorize a bunch of commands right away.

Click **Initialize Repository** to initialize the current folder as a version-controlled repository.

>[!NOTE]
>
> Git will only start tracking the change history of this folder after initialization is complete.

![](images/01-vscode-usage-20260305173743.jpg)
#### Basic Workflow (3 Steps)

| Stage | Meaning | What You Do |
|------|---------- -|----------|
| **Changes** | File has been modified but not yet committed | Edit the file as usual |
| **Ready to Commit** | Select the changes to save | Click the **+** next to the file |
| **Saved** | Changes have been written to version history | Click the blue **Commit** button |

![](images/01-vscode-usage-20260305175821.jpg)

---

### Extensions Market

The **Extensions** view is the plugin marketplace, where you can add new capabilities to VS Code.

![](images/01-vscode-usage-20260305182927.jpg)

>[!TIP]
>
> After installing plugins like **Markdown All in One** or **Md Editor**, you can preview Markdown formatting directly with WYSIWYG layout.

![](images/01-vscode-usage-20260305183558.jpg)

![](images/01-vscode-usage-20260305184231.jpg)

---

### Built-in Terminal

Click the **Terminal** icon in the top-right corner to open a terminal within VS Code, which will automatically navigate to the current project directory.

![](images/01-vscode-usage-20260305184535.jpg)

Click the **+** in the terminal panel to create multiple terminals; use the dropdown menu in the bottom-right corner to switch between and manage open terminals.

![](images/01-vscode-usage-20260305184747.jpg)

---

### AI Assistant

Click the **Copilot / Agent** icon in the top-right corner to open the AI Assistant (GitHub Copilot by default). After entering a command in the input field, the Agent will perform the relevant task in the current directory.

![](images/01-vscode-usage-20260305190648.jpg)

---

### Command Panel

The **Command Palette** can be used to access commands, settings, extensions, and other features. Many functions not directly displayed on the main interface can be quickly found here.

![](images/01-vscode-usage-20260305191241.jpg)

---

## Part 3: File Management

### Basic File Management Guidelines

For many beginners, the biggest challenge when starting with VS Code isn’t learning how to use it, but rather **files becoming disorganized, hard to find, or even placed in the wrong locations**. The following simple rules can help you avoid most of this confusion:

**1. One project, one folder**  
Place each task or project in its own separate folder. Do not mix files from different projects together, as this will make it difficult to organize them later.

**2. Use Clear File and Folder Names**  
Try to use meaningful names, such as `report.md` or `data_analysis.docx`, and avoid arbitrary names like `test1` or `aaa`.  

**3. Don’t Mix Different Types of Content**  
For example:
- Keep documents in one place
- Store images or data in separate folders

This will make searching and maintenance much easier later on.

**4. Establish a simple directory structure**  
You can use the following basic structure as a reference:

```
your-project/  
├── data/        (Data files)  
├── docs/        (Documentation)  
├── src/         (Code)  
└── README.md    (Project description)
```

It doesn’t need to be complicated from the start, but **having a structure is definitely better than having none**.

> [!TIP]
> 
> Remember: VS Code is just a tool to help you “manage files”; the actual files are always in your computer’s folders. A clear file structure will save you a lot of time in the future.

---
### Open the Workspace

After opening VS Code, click **File → Open Folder** to navigate to the directory containing the files you want to work on.

![](images/01-vscode-usage-20260309111111.jpg)

![](images/01-vscode-usage-20260317181317.jpg)

---

### Creating Folders and Files

#### Creating a New Folder

You can create a new folder using the button in the toolbar to the right of the folder.

![](images/01-vscode-usage-20260317181528.jpg)

Enter a folder name and press Enter.

![](images/01-vscode-usage-20260317181612.jpg)

#### Creating a Subfolder

To create a subfolder within an existing folder, first select that folder, then click **New Folder**.

![](images/01-vscode-usage-20260317181655.jpg)

#### Creating a New File

You can also create a new file directly within a folder using the toolbar.

![](images/01-vscode-usage-20260317181733.jpg)

The new file is empty by default; you must manually enter a file extension, such as `test.md`.

![](images/01-vscode-usage-20260317181755.jpg)

Once created, click the file in the sidebar to view or edit its contents.

![](images/01-vscode-usage-20260317181848.jpg)

>[!TIP]
>
> VS Code can directly create plain text files such as `.txt`, `.md`, and `.json`; for files like Word, Excel, and PPT, it is generally recommended to create them in their respective applications.

---

### Renaming and Deleting

#### Renaming a File

Right-click the file and select **Rename**, then enter the new filename.

>[!TIP]
>
> On Mac, you can also select the file first and then press Enter to rename it quickly.

![](images/01-vscode-usage-20260317181926.jpg)

![](images/01-vscode-usage-20260317181938.jpg)

#### Renaming Folders

The process for folders is the same: right-click to rename, or select the folder and press Enter.

![](images/01-vscode-usage-20260317182048.jpg)

#### Deleting Files or Folders

Right-click the file or folder and select **Delete** to remove it.

![](images/01-vscode-usage-20260317182150.jpg)

![](images/01-vscode-usage-20260317182210.jpg)

---

### Quickly Find Files

When there are many project files, you can use **Search** to quickly locate content by keyword.

![](images/01-vscode-usage-20260306115131.jpg)

The file path is displayed above the editor.

![](images/01-vscode-usage-20260306115255.jpg)

Click any directory level in the path to quickly browse the files within that directory.

![](images/01-vscode-usage-20260306115349.jpg)

>[!TIP]
>
> After installing plugins for formats like PDF and Office, you can view or edit more file types directly within VS Code, reducing the need to switch between applications.

![](images/01-vscode-usage-20260306115638.jpg)

Type “claude” in the extension search bar to find and install the Claude Code for VS Code plugin.

![](images/01-vscode-usage-20260317182540.jpg)

Click the icon in the top-right corner to open the Claude Code dialog window for more convenient use.

![](images/01-vscode-usage-20260317182749.jpg)


---

## Part 4: Hands-On with Skills and MCP

> [!TIP]
> 
> We recommend reading the [Skills Introduction](../../../Extensions/01-skills) and [MCP Introduction](../../../Extensions/02-mcp) (optional) before continuing with this chapter.

### Why Do We Need Skills and MCP?

Agents are based on general-purpose large language models, which have limited knowledge bases and tool capabilities, and offer relatively limited support for multimedia tasks such as images and audio. Therefore, we typically use Skills and MCP to “extend their capabilities.”

| Extension Type | What It Is | How to Use |
|------|------|------|
| **Skills** | Text-based prompt files | Tell the Agent how to perform a specific type of task |
| **MCP** | Off-the-shelf tools/APIs | Allow the Agent to call them directly without writing code from scratch |

If you have already followed the [GLM Configuration Tutorial](../../../Agents/01-GLM-configuration#Method-1-Recommended-Visual-Configuration-Tools-) or the [KIMI Configuration Tutorial](../../../Agents/02-KIMI-configuration# Method 1 - Recommended Visual Configuration Tools-) and installed **Agent Manager** (via `agent_manager-main.zip`), you can also use it to install Skills and MCPs. This section explains what they are and how to use them in VS Code. The usage is similar whether you install via the application or the command line.

---

### Skills: Your Task Wizard

Open VS Code, click **File → Open Folder**, and navigate to the target folder.

![](images/01-vscode-usage-20260309111111.jpg)

![](images/01-vscode-usage-20260309111611.jpg)

Click the shortcut button in the top-right corner to open the Claude Code plugin dialog.

![](images/01-vscode-usage-20260317183955.jpg)

Enter **`/file-conversion`** (the folder name for this Skill) to invoke it.

![](images/01-vscode-usage-20260317184133.jpg)

For example, enter **please convert this PDF file to MD and place this MD file in the current folder**, then drag and drop the PDF and press Enter.

>[!WARNING]
>
> `file-conversion` requires a paid Alibaba Cloud service and an API key. We recommend testing with other Skills first.

![](images/01-vscode-usage-20260317184235.jpg)

Once the task is complete, you will see the converted Markdown file in your workspace.

![](images/01-vscode-usage-20260317185208.jpg)

---

### MCP: Your Pre-built Toolkit

Unlike Skills, which primarily rely on text prompts, **MCPs** are typically standalone programs or services. Agents can call them directly, reducing the workload of writing code from scratch.

Simply follow the MCP provider’s instructions to complete installation and configuration, and you’ll be able to view and use it in Claude Code.

#### Using MCP in VS Code

Open VS Code, click **File → Open Folder**, and navigate to the target folder.

![](images/01-vscode-usage-20260309111111.jpg)

![](images/01-vscode-usage-20260309115212.jpg)

Click the Claude Code icon in the top-right corner to open the extensions panel.

![](images/01-vscode-usage-20260317194356.jpg)

Type **`/mcp`** to view the currently available MCP services.

![](images/01-vscode-usage-20260317194423.jpg)

![](images/01-vscode-usage-20260317194437.jpg)

Click any MCP to view detailed information.

![](images/01-vscode-usage-20260317194559.jpg)

Click **View tools** to see all tools provided by that MCP.

For example, the **qwen-ai** MCP supports text output, translation, OCR, image understanding, web image search, web scraping, audio-to-text conversion, video understanding, and other capabilities, significantly expanding the Agent’s scope of work.

![](images/01-vscode-usage-20260317194620.jpg)

![](images/01-vscode-usage-20260317194714.jpg)

For example, in Claude Code, enter **please convert this audio file to txt and save it to output folder**, then drag and drop the audio file.

![](images/01-vscode-usage-20260317195139.jpg)

Wait a moment, and the audio content will be converted to text.

![](images/01-vscode-usage-20260317195424.jpg)

---

*Don’t worry if you run into issues: the VS Code community has plenty of resources; of course, you can also ask your AI assistant directly—it’s always there.*