---

layout: doc

title: winget Basics · winget 基础

---

# winget 基础

## Package Manager (包管理器)

A package manager can be understood as a "software app store" in the terminal. It can quickly download and automatically install various programs through commands, while handling dependency relationships and version management. Users do not need to manually download installation packages or launch installers one by one.
包管理器可以理解为终端中的"软件应用商店"。它能够通过命令快速下载并自动安装各种程序，同时负责处理依赖关系和版本管理，用户无需手动下载安装包或逐个启动安装器。

## Winget

Winget is the native package manager for Windows, equivalent to Mac's brew. Its software ecosystem is already quite rich, and most software can be installed here.
Winget 为 Windows 原生的包管理器，相当于 Mac 的 brew。其软件生态已经较为丰富，大多数软件都可在此安装。

**Note**: All programs installed by Winget will be installed in the default location; if you need to install to a data drive (such as D:), you will need to install the program manually.
**注**：Winget 安装的所有程序都会安装在默认的位置，如需安装到数据盘（如 D: ），需要手动安装程序。

### winget search

You can search for the program you want to install by typing `winget search xxx` in the command line and pressing Enter, where xxx can be the program's abbreviation. Since a program often has multiple versions, try to install using the Id obtained through the search command whenever possible.
可通过在命令行输入 `winget search xxx` 并按下回车搜索想要安装的程序，xxx 可为程序简称。因为往往一个程序有多个版本，所以尽可能通过 search 命令得到的 Id 进行安装。

![](./images/Windows/file-20260109161753557.png)

### winget install Id

For example, you can install the corresponding program by typing `winget install Python.Python.3.12` in the command line and pressing Enter, where `Python.Python.3.12` is the Id obtained from the `winget search` operation. As shown below, you can see that Python has been installed.
例如，可通过在命令行输入 `winget install Python.Python.3.12` 并按下回车安装对应的程序，其中，`Python.Python.3.12` 为 `winget search` 操作得到的 Id 。如下所示，可看到 Python 已经被安装。

![](./images/Windows/file-20260109162641973.png)
