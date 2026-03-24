---
title: Terminal Basics
draft: false
prev: Basic-tools/03-mac-os-basics
next: Basic-tools/05-homebrew-install
---

# Terminal Basics

**What exactly is a terminal?**

A terminal is your computer’s “direct line of communication.” You’re used to clicking icons and dragging windows, but the Terminal lets you type commands directly, and your computer executes them immediately. No clicks, no menus—just you and your computer, communicating directly.

Why is this important? Because tools like Claude Code live right inside the Terminal. If you want to use AI to help you write code, you’ll need to get comfortable with this black (or white) window first.

---

## How to Open the Terminal

### Mac: Summoning the Terminal

Press `Command + Space`, type “Terminal”, then hit Enter.

![](images/image260.jpg)

It’s that simple. You’re in.


>[!TIP]
>
> On a Mac, you can also right-click any folder and select “Open Terminal in This Folder.” This way, the terminal opens right where you are. Super convenient.


![](images/image270.jpg)


Now that you know what you’re looking at, let’s open a terminal.

### Windows: Open PowerShell

Press the `Windows key` (or `Win`), type “PowerShell”, then press Enter.

>[!WARNING]
>
> To avoid permission issues later on, I recommend selecting **Run as administrator**. Your future self will thank you for it.

![](images/01-terminal-basics-20260109160736263.jpg)

Wait for the window to appear. When you see “Administrator” in the title bar, you’ll know you’re in administrator mode.

![](images/01-terminal-basics-20260109161032035.jpg)
## Anatomy of a Terminal Window

Before you start typing commands, let’s figure out what you’re looking at. The terminal might seem a bit intimidating at first glance—it’s all text, no buttons—but once you understand the different parts, it actually makes a lot of sense.

### Title Bar: What Is This Window For?

#### Mac

**Mac Terminal Example**: **ruby -- 01-complete-macos-setup.sh**

The title bar tells you:

- **ruby**: The name of the current terminal session
- **01-complete-macos-setup.sh**: The name of the currently associated script file
- **.sh** indicates that this is a shell script, which the terminal can execute

>[!TIP]
>
> The title does not mean the script is running — it simply tells you what this window is associated with. Think of it as a file label.

![](images/image3.jpg)
#### Windows

**Windows PowerShell Example**: The title bar displays “Windows PowerShell” or “Administrator: Windows PowerShell”.

![](images/01-terminal-basics-20260113152828141.jpg)
### Command Prompt: Your “Ready, Set, Go” Signal

This line is **absolutely crucial**. It tells you the system is ready to receive your commands. Let’s break it down by operating system.

#### Mac Command Prompt

| Symbol | Meaning | Why It Matters |
|------|------|------------|
| **User** | Your username | Who is currently logged in |
| **~** | Home directory | Your personal folder |
| **%** | Ready for input | Go ahead! |

The tilde `~` is a shortcut to your home directory. Instead of typing `/Users/your-name`, you just see `~`. Clean and simple.
![](images/image5.jpg)

**Putting it all together:**

- Who’s in control? → `User` (that’s you!)
- Who’s doing this? → `~` (Home, sweet home)
- Is the system ready? → `%`
- Where do I type? → The blinking cursor—right here

![](images/image6.jpg)
#### Windows Command Prompt

| Symbol | Meaning | Why it matters |
|------|------|------------|
| **PS** | You are in PowerShell | Unlike the old-style CMD |
| **C:\Windows\System32** | The folder you are currently in | Commands will be executed here |
| **>** | The system is ready | Go ahead, type something |

**Putting it all together:**

- Where am I now? → `C:\Windows\System32`
- Is the system ready? → `>` (Yes!)
- Where will my input appear? → After `>`, at the blinking cursor

![](images/01-terminal-basics-20260113152828140.jpg)
**Summary**

1. **Terminal** = Text-based communication directly with your computer
2. **Mac**: `Command + Space` → “Terminal”
3. **Windows**: Open PowerShell as an administrator
4. **Command Prompt** = The signal that says “I'm ready” (look for `>`, `%`, or `$`)
5. **You're ready** to use command-line tools like Claude Code!

---

*Still nervous? Don’t worry. The best way to learn the terminal is to use it. Every time you run a command, you’ll feel a little more comfortable. You’ve got this.*
