---

layout: doc

title: Terminal 基础

---

# Terminal Introduction (终端介绍)

A terminal is a software interface that directly interacts with the operating system, complementing the graphical operating system. Through the terminal, users can precisely control system behavior in the form of commands and run many programs that do not provide independent graphical interfaces, such as command-line tools like Claude Code.
终端是一种直接与操作系统交互的软件界面，与图形化操作系统相互补充、互为表里。通过终端，用户可以以命令的形式精确控制系统行为，并运行许多不提供独立图形界面的程序，例如 Claude Code 等命令行工具。

## Title Bar (标题栏)

**Windows**

**Windows PowerShell Example**: The title bar shows "Windows PowerShell" or "Administrator: Windows PowerShell".
**Windows PowerShell 示例**：标题栏显示 "Windows PowerShell" 或 "Administrator: Windows PowerShell"。

![](./images/1.OS/file-20260113152828141.png)

**Mac**

**Mac Terminal Example**: **ruby -- 01-complete-macos-setup.sh**
**Mac 终端示例**：**ruby -- 01-complete-macos-setup.sh**

![](./images/Terminal/image3.png)

This title bar shows:
标题栏表示：

- **ruby**: the name of your current terminal session
- **ruby**：当前终端会话的名字
- **01-complete-macos-setup.sh**: the script file associated with the session
- **01-complete-macos-setup.sh**：当前关联的脚本文件名
- **.sh** indicates a shell script, meaning it can be executed in the terminal
- **.sh** 表示这是一个 shell 脚本，可在终端中执行

It does not mean the script is running --- it only tells you which file is currently open or associated.
它不代表一定在运行，只是显示会话名称。

## The Command Prompt (命令提示符)

**Windows**

This line is extremely important. It indicates that the system is ready to accept commands. Let's break it down:
这是最关键的一行，表示系统已准备好接受指令。逐项解释：

**PS**: Represents that the currently opened window is PowerShell.
**PS**： 代表目前打开的窗口为 PowerShell 。

**C:\Windows\System32**: Represents the path where the current folder is located.
**C:\Windows\System32**：代表当前文件夹所在的路径。

**>**: Represents that the previous program has completed and is ready to accept the next command input.
**>**：代表上一段程序已经完成，随时等待下一条指令的输入。

![](./images/1.OS/file-20260113152828140.png)

**Putting It All Together (组合起来理解)**

Readable explanation:
更易读的解释：

- Where are we working? → C:\Windows\System32
- 我们现在在哪？ → C:\Windows\System32
- Is the system ready? → >
- 系统准备好了吗？ → >
- Where will your typing appear? → blinking cursor
- 你输入的内容会出现在哪里？ → 闪烁的光标

**Mac**

This line is extremely important. It indicates that the system is ready to accept commands. Let's break it down:
这是最关键的一行，表示系统已准备好接受指令。逐项解释：

**Username**: Represents the account currently using the computer. Meaning: "User xxx is currently operating."
**Username** ：表示当前使用电脑的账号。含义："现在是用户 xxx 在操作。"

**~**: Represents the path where the current folder is located. The tilde ~ represents the home directory (Home directory), which is a shortcut notation for the home directory.
**~**：代表当前文件夹所在的路径，波浪号 ~ 表示 家目录（Home 目录），是家目录的快捷写法。

Other paths you might see:
其他你可能会看到：

- `~/Desktop` → you are in Desktop
    
- `~/Desktop` → 桌面
    
- `~/Documents` → you are in Documents
    
- `~/Documents` → 文档
    
- `/usr/local/bin` → system-level folder
    
- `/usr/local/bin` → 系统级目录

**%**：代表提示符符号，表示系统已经准备好执行命令。

- `%` → zsh shell (default on modern macOS)
- `%` → zsh（新版 macOS 默认）
- `$` → bash shell
- `$` → bash
- `#` → administrator (root) shell
- `#` → 超级管理员

If you ever see `#`, be careful --- it means full system access.
如果看到 `#`，说明你拥有最高权限，执行命令要格外谨慎。

**Blinking cursor**: Indicates "I am ready, please enter a command." Just like the blinking vertical line in a Word document.
**闪烁的光标**：表示"我已经准备好，请输入指令"。就像 Word 文档里的闪烁竖线。

![](./images/Terminal/image5.png)

**Putting It All Together (组合起来理解)**

![](./images/Terminal/image6.png)

Readable explanation:
更易读的解释：

- Who is operating? → selenagupSelena (current logged-in user)
- 是谁在操作？ → selenagupSelena（当前登录的用户）
- Where are we working? → ~ (home folder)
- 我们现在在哪？ → ~（家目录）
- Is the system ready? → %
- 系统准备好了吗？ → %
- Where will your typing appear? → blinking cursor
- 你输入的内容会出现在哪里？ → 闪烁的光标

![](./images/Terminal/image7.png)

## Opening Terminal (打开终端)

**Windows**

You can press `win` to search for PowerShell and open it.
可按 `win` 搜素 PowerShell 并打开。

**Note**: To avoid issues with insufficient permissions, it is recommended to select `Run as Administrator` to open PowerShell.
**注**：为避免权限不足的问题，建议选择 `Run as Administrator` 打开 PowerShell。

![](./images/Windows/file-20260109160736263.png)

Wait for the black window to pop up to enter PowerShell; the "Administrator" in the upper left corner represents administrator mode.
等待黑色窗口弹出即可进入 PowerShell，左上方的 Administrator 代表管理员模式。

![](./images/Windows/file-20260109161032035.png)

**Mac**

Press `Command + Space`, search for **Terminal**, and use it as the main command-line window.
**Mac**：按下 `Command + 空格键`，搜索 **Terminal**，并将其作为主要的命令行窗口使用。

![](./images/Toolkit/image260.png)

Then, you can enter the terminal environment (the text-based command window).
然后，就可以进入命令行环境（基于文本的命令窗口）。

![](./images/Toolkit/image270.png)
