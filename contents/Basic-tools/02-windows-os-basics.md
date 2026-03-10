---

layout: doc

title: Windows 操作系统基础

---

# Windows 操作系统基础

## Quick Search (快速搜索)

### Windows: Everything

Because Windows' built-in search function is too slow and may consume a lot of cache, it is basically only suitable for searching applications. Everything is an important extension of Windows' search functionality, capable of quickly matching file names and file content based on search terms.
因 Windows 本身的检索功能过慢且可能消耗大量缓存，基本上只能用于检索应用程序，Everything 是 Windows 检索功能的重要扩展，能够根据检索词快速匹配文件名和文件内容。

You can download Everything by typing `winget install voidtools.Everything` in PowerShell and pressing Enter.
可通过在 Powershell 输入 `winget install voidtools.Everything` 并按下 Enter 下载 Everything。

   > [!TIP]
   >
   > 
   > `winget` is Windows' native package manager, `install` means download, and `voidtools.Everything` is the download Id for the Everything program. You can search for it using `winget search everything`.
   > `winget` 为 Windows 的原生包管理器，`install` 代表下载，`voidtools.Everything` 为 Everything 程序的下载 Id 。可通过 `winget search everything` 搜索得到。
   
![](./images/Windows/file-20260111122150310.png)

After downloading, you can see the Everything shortcut on the desktop. Double-click to open the graphical interface.
下载完成后可在桌面看到 Everything 的快捷方式，双击可打开图形化界面。

![](./images/Windows/file-20260111122844126.png)

Enter the file name or file content you want to search in the input box to quickly search for files.
在输入框输入想要搜索的文件名或文件内容，即可快速搜索文件。

![](./images/Windows/file-20260111123112848.png)

## System Language Settings (系统语言设置)

Press `win` to search for settings and open it.
按下 `win` 搜索 settings 并打开，

![](./images/1.OS/file-20260113152828153.png)

Click Time & language -> Language & region in sequence.
依次点击 Time & language -> Language & region 。

![](./images/1.OS/file-20260113152828152.png)

You can add and modify the default language here.
可在此处添加和修改默认语言。

![](./images/1.OS/file-20260113152828151.png)

## File Management (文件管理)

### File Explorer

Windows uses File Explorer for file management. You can access it by pressing `Win + E` or clicking the folder icon in the taskbar.
Windows 使用文件资源管理器进行文件管理。您可以按 `Win + E` 或点击任务栏中的文件夹图标来访问它。

### Show File Extensions and hidden files (显示文件扩展名和隐藏文件)

It is critical for developers to see the exact file type (e.g., `.md`, `.sh`, `.json`).
对于开发者来说，看到确切的文件类型（如 `.md`, `.sh`, `.json`）至关重要。

Open File Explorer, click the ... icon in the upper right corner, and select Options.
打开文件资源管理器，点击右上方 ... 的图标，并选择 Options。

![](./images/1.OS/file-20260113152828149.png)

Switch to the View interface, and in the Hidden files and folders section, select Show hidden files, folders, and drives. Also uncheck Hide extensions for known file types.
切换到 View 的界面，并在 Hidden files and folders 栏选择 Show hidden files, folders, and drives。并取消 Hide extensions for known file types 的选择。

![](./images/1.OS/file-20260113152828148.png)

Finally, click Apply -> OK in sequence to complete the settings.
最后依次点击 Apply -> OK 完成设置。

![](./images/1.OS/file-20260113152828147.png)

### File Path Bar (文件路径栏)

The file path bar is located at the top of File Explorer. You can click the folder buttons to quickly switch between folders.
文件路径栏位于文件资源管理器的正上方，可点击文件夹的按钮快速切换文件夹。

![](./images/1.OS/file-20260113152828144.png)

Right-click a folder and select Open in Terminal to open the folder in the terminal.
右键文件夹并选择 Open in Terminal 即可在终端打开文件夹。

![](./images/1.OS/file-20260113152828146.png)

## Application Organization (应用程序组织)

If you want to keep your desktop tidy, you can organize applications in Windows' Start page. Press `win` and search for Everything, then click Pin to Start to pin it to Windows' Start page. Click Pin to taskbar can pin it to Taskbar on the bottom.
如果想保持桌面的整洁性，可将应用程序收纳在 Windows 的启动页面中。按下  `win` 并搜索 Everything，点击 Pin to Start，将其固定在 Windows 的启动页面中。点击 Pin to taskbar 能将其固定到下方任务栏。

![](./images/1.OS/file-20260113152828142.png)

Press the `win` key again to see that Everything has been pinned to Windows' Start page.
再次按下 `win` 键即可看到 Everything 已被固定在 Windows 的启动页面中。

![](./images/Windows/file-20260111123743239.png)
