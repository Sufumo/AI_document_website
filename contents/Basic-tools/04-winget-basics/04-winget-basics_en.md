---
permalink: /contents/Basic-tools/04-winget-basics/en/
lang: en


layout: doc
title: winget Basics
---

# winget Basics

## The Big Picture: Why Use a Package Manager?

Remember how you used to install software? Go to a website, find the download button, run the installer, click "Next" seventeen times, uncheck some toolbar you didn't ask for, and hope nothing breaks. Fun times.

**Package managers** are here to save you from that nightmare. Think of them as an "App Store" for your terminal. One command, and software installs automatically — no clicking, no toolbars, no drama.

| Traditional Way | Package Manager Way |
|-----------------|---------------------|
| Download installer | `winget install python` |
| Run installer | Done. |
| Click through wizard | |
| Uncheck bloatware | |
| Reboot sometimes | |

---

## What is winget?

**winget** (Windows Package Manager) is Microsoft's official package manager for Windows. It's like Homebrew for Mac, but built right into Windows. The software ecosystem is surprisingly rich — most popular programs are available.

💡 **Pro Tip**: winget comes pre-installed on Windows 10 (version 1809+) and Windows 11. If you're on an older version, you might need to install it from the Microsoft Store first.

⚠️ **Note**: All programs installed via winget go to the default system location. If you need to install something to a specific drive (like D:), you'll need to use the traditional installer method for that program.

---

## Step 1: Find What You Want (Search)

Before installing, let's find the exact package name. Why? Because one program might have multiple versions, and you want the right one.

In your terminal, type:

```powershell
winget search python
```

> **What this does**:
> - Searches the winget repository for anything matching "python"
> - Returns a list with names, IDs, versions, and sources

![](./images/Windows/file-20260109161753557.png)

💡 **Pro Tip**: Use the **ID** column for installation instead of the name. It's more precise and avoids confusion when multiple versions exist.

---

## Step 2: Install It (One Command)

Found what you need? Now install it with the ID you got from the search:

```powershell
winget install Python.Python.3.12
```

> **What this does**:
> - Downloads the installer automatically
> - Runs the installation silently (no clicking through wizards)
> - Handles dependencies if needed

![](./images/Windows/file-20260109162641973.png)

That's it. Python is now installed on your system.

---

## Common winget Commands Cheat Sheet

| Command | What It Does | Example |
|---------|--------------|---------|
| `winget search <name>` | Find a package | `winget search node` |
| `winget install <id>` | Install a package | `winget install OpenJS.NodeJS.LTS` |
| `winget list` | Show installed packages | `winget list` |
| `winget upgrade <id>` | Update a package | `winget upgrade Python.Python.3.12` |
| `winget upgrade --all` | Update everything | `winget upgrade --all` |
| `winget uninstall <id>` | Remove a package | `winget uninstall Python.Python.3.12` |

---

## Summary

1. **Package managers** = terminal-based app stores (no clicking, no bloatware)
2. **winget** = Microsoft's official package manager for Windows
3. **Search first**: `winget search <name>` → find the ID
4. **Install with ID**: `winget install <id>` → done!
5. **Upgrade easily**: `winget upgrade --all` keeps everything current

---

*Welcome to the future of software installation. Your mouse-clicking finger will thank you.*
