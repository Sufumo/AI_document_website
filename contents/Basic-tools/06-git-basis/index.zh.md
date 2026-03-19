---
title: Git 入门实战教程
draft: false
prev: Basic-tools/01-terminal-basics
next: Agents/01-GLM-configuration
---
# Git 入门实战教程

## Git 到底在解决什么问题？

想象这样一个场景：你和同事一起写一本书。同事先写好大纲，你再补充、修改内容。要是每次改完都靠“互传文件”，你们电脑里很快就会堆满一堆“最终版-v2-真的最终版”之类的副本。更麻烦的是，如果对方先改了但没告诉你，你又改了同一段，最后还得手动比对到底保留谁的版本。

为了解决这个问题，你们决定找一个“中介”来统一保管这本书：每次修改前先拿最新版本，改完再交回去；如果不满意，还能随时回到上一个版本。Git 扮演的就是这个“版本中介”角色。

## 安装 Git

### 方式一：通过 Agent 安装 Git（推荐）

打开你的 Agent 工具（如 Claude Code），输入 `please help me install and config git, my name is "Your Name", my email is "email@example.com"`，等待任务完成即可安装 Git。

>[!NOTE]
>
> Git 对用户名和邮箱没有严格要求，直接使用 `Your Name` 和 `email@example.com` 也能正常运行。  
> 但提交到云端后，其他人能看到你的提交身份信息，所以建议改成你常用的昵称和邮箱。

![](images/Pasted%20image%2020260319163137.png)
### 方式二：在 macOS 上安装 Git

>[!TIP]
>
> 本章节假设你具备基本的终端和命令行知识。若对此不太熟悉，建议先花 5 分钟阅读 [Terminal 基础](../../../Basic-tools/01-terminal-basics) 和 [Homebrew 安装](../../../Basic-tools/05-homebrew-install)，绝对物超所值。

确认已安装 Homebrew 后，按 `Option + Space` 搜索 Terminal 并打开。

![](images/Pasted%20image%2020260319135151.png)

将以下命令复制到 Terminal，使用 Homebrew 安装 Git。

```plain
brew install git
```

![](images/Pasted%20image%2020260319135330.png)

等待命令行重新可输入，就说明 Git 安装成功了。

![](images/Pasted%20image%2020260319135506.png)

安装 Git 后，还需要做最后一步初始化配置。在终端输入以下命令：

```
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```

> [!NOTE]
> 
> Git 对用户名和邮箱没有严格要求，直接用 `Your Name` 和 `email@example.com` 也能正常使用。  
> 但提交到云端后，其他人会看到你的提交身份信息，所以建议改成你的昵称和邮箱。

![](images/Pasted%20image%2020260319163330.png)

等待命令行重新变得可输入，Git 就配置完成了。

![](images/Pasted%20image%2020260319163303.png)

## Git 基础操作

>[!TIP]
>
> VS Code 管理 Git 十分方便。如果你还没安装 VS Code，建议先花 3 分钟阅读 [VSCode 使用指南](../../../Apps/01-vscode-usage)，绝对物超所值。

打开 VS Code，选择一个工作文件夹，然后点击左侧工具栏里带分叉图标的「源代码管理」按钮。

可以看到初始状态下还没有任何版本记录。只有被 Git 追踪的项目，才会记录文件历史，所以建议尽早初始化仓库。点击 **Initialize Repository**，即可把当前文件夹变成可追踪版本的仓库。

![](images/Pasted%20image%2020260319140656.png)

这就是 Git 的主工作区。上方的 **CHANGES** 用来查看和处理改动（如暂存、撤销）；下方的 **GRAPH** 用来展示提交历史。你可以把每条提交理解成一个“可回看、可共享”的历史快照。

![](images/Pasted%20image%2020260319142054.png)

在文件夹中新建一个测试文档后，你会看到文件右侧出现 `U`。这表示该文件是“未跟踪”状态。此时 Git 还不知道要从哪个版本开始对比，所以需要你先把它加入追踪。

![](images/Pasted%20image%2020260319143208.png)

点击下图标注的 `+` 按钮，把该文件加入暂存区（Staged Changes）。

![](images/Pasted%20image%2020260319143524.png)

可以看到文件被移入 **Staged Changes**，左侧符号变成 `A`，表示这是一个新增文件（Added）。

![](images/Pasted%20image%2020260319143828.png)

这时，把文本改成 `hello, this is a new text`。

![](images/Pasted%20image%2020260319144414.png)

回到 Git 面板后，文件右侧会变成 `M`，表示该文件已修改。右侧编辑区会显示差异：红色是删除内容，绿色是新增内容。也就是删掉 `hello, this is the original text`，新增 `hello, this is a new text`。

Git 以行为单位追踪，即使只修改一个词，也会显示删除整行文本并添加包含新词的新的一行文本。

>[!NOTE]
>
> `Staged Changes` 里的 `test-tutorial.md` 右侧也可能显示 `M`。  
> 这不表示“历史版本被改了”，只是说明当前文件在“工作区”和“暂存区”之间有差异。  
> 如果你把 `Changes` 里的修改再次暂存，状态会按最新内容更新。

![](images/Pasted%20image%2020260319144805.png)

如果对当前文件不满意并将其删除，`Changes` 中会出现带 `D` 标识的文件，表示该文件已被删除。

![](images/Pasted%20image%2020260319150004.png)

如果想撤销这个操作，点击下图标注的撤销按钮，即可恢复文件。

![](images/Pasted%20image%2020260319150123.png)

也可以通过 **Unstage Changes** 按钮，把已暂存内容退回到 `Changes` 区域。

![](images/Pasted%20image%2020260319150334.png)

如果对 `Staged Changes` 中的内容满意，就为这次修改写一条提交信息，然后点击 **Commit**，把它提交为一个新的版本。

![](images/Pasted%20image%2020260319150900.png)

可以在 GRAPH 界面看到这个新提交的版本。

> [!NOTE]
> 
> 这个版本目前只保存在本地。  
> 如果想和他人共享，需要连接远程仓库并推送。

![](images/Pasted%20image%2020260319151009.png)

## Git 认证

为了让本地 Git 安全连接远程仓库，通常会使用 **SSH 密钥** 进行身份验证。你在本地生成一对密钥，把公钥添加到 GitLab/GitHub 等平台后，后续推送和拉取时平台就能识别“是不是你本人在操作”。下面以 GitLab 为例说明配置流程。

## 配置 Git 身份认证（SSH）

### 方法1：使用 Agent 获取 SSH 密钥

打开 Agent 工具，输入：`please generate a ssh key for me and show me the public key to configure on gitlab`。

![](images/Pasted%20image%2020260319174529.png)

等待任务完成后，即可看到可复制的公钥内容。

![](images/Pasted%20image%2020260319174701.png)

### 方法2：使用 Terminal 获取 SSH 密钥

打开 Terminal 并输入以下命令，"you@example.com" 需要修改为你的邮箱（双引号需要保留）。

```
ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub
```

![](images/Pasted%20image%2020260319173628.png)

如果提示 Enter file in which to save the key... 直接按 Enter 即可。

![](images/Pasted%20image%2020260319173725.png)

然后你会看到一行以 `ssh-ed25519` 开头的公钥字符串。

![](images/Pasted%20image%2020260319173812.png)

## 把 SSH 公钥添加到 GitLab

依次点击头像 -> **Preferences** -> **SSH Keys**，进入密钥配置页面。

![](images/Pasted%20image%2020260319172911.png)

此时你会看到还没有配置任何 SSH 密钥。

![](images/Pasted%20image%2020260319173151.png)

点击 **Add new key** 创建一条新密钥。

![](images/Pasted%20image%2020260319173930.png)

把刚刚复制的公钥粘贴到 `Key` 输入框，然后点击 **Add key**。

![](images/Pasted%20image%2020260319174033.png)

配置完成后，密钥就生效了。

![](images/Pasted%20image%2020260319174158.png)

## 新建一个远程仓库

打开 Git 远程托管平台，依次点击 **Projects -> New project**。

![](images/Pasted%20image%2020260319154451.png)

点击 Create blank project 创建一个空项目。

![](images/Pasted%20image%2020260319154618.png)

依次完成以下内容的填写：
- 填写 **Project Name**，建议与项目文件夹同名。
- 在 **Project URL** 处选择你的用户名。
- **Visibility Level** 决定仓库可见范围：`Private` 仅邀请可见，`Internal` 对同组织账号可见，`Public` 对所有人可见。
- 在 **Project Configuration** 中，建议取消勾选 **Initialize repository with a README**。否则远程仓库会先生成一个 README，首次推送时可能出现“本地与远程历史不一致”。

完成填写后，点击 Create project 新建一个新仓库。

![](images/Pasted%20image%2020260319155130.png)

## 将本地仓库和云端仓库绑定

### 方法1：使用 Agent 进行关联

进入仓库，依次点击 **Code -> Copy URL**，复制 **Clone with HTTPS** 右侧的 URL。

![](images/Pasted%20image%2020260319171744.png)

打开 Agent，输入 `Please help me push this folder to this Git repository.`，并把复制的 URL 粘贴给 Agent。等待任务完成即可。

![](images/Pasted%20image%2020260319171852.png)

### 方法2：使用 Terminal 进行关联

进入仓库，依次点击 **Code -> Copy URL**，复制 **Clone with HTTPS** 右侧的 URL。

![](images/Pasted%20image%2020260319171744.png)

在工作目录打开 Terminal，将 `YOUR_REPOSITORY_URL` 替换为仓库链接，然后执行以下命令：

```
git remote add origin YOUR_REPOSITORY_URL
git push origin main
```

等待执行完毕，查看仓库可以发现本地的版本已被上传到云端。

![](images/Pasted%20image%2020260319172053.png)

![](images/Pasted%20image%2020260319170746.png)

## 关联一个已有的 Git 仓库

### 方法1：使用 Agent 关联仓库

进入仓库，依次点击 **Code -> Copy URL**，复制 **Clone with HTTPS** 右侧的 URL。

![](images/Pasted%20image%2020260319171744.png)

选择一个工作目录并打开 Agent，输入 `please clone this project for me`，再把复制的 URL 粘贴进对话框。

![](images/Pasted%20image%2020260319175956.png)

等待任务完成，即可看到项目已被克隆到本地。

>[!NOTE]
>
> 克隆到本地的项目不需要额外配置，只要拥有对仓库的权限，可以随意从远程仓库上传和下载数据。

![](images/Pasted%20image%2020260319180634.png)

### 方法2：使用 Terminal 关联仓库

进入仓库，依次点击 **Code -> Copy URL**，复制 **Clone with HTTPS** 右侧的 URL。

![](images/Pasted%20image%2020260319171744.png)

在工作目录打开 Terminal，将 `YOUR_REPOSITORY_URL` 替换为仓库链接，然后执行以下命令：

```
git clone YOUR_REPOSITORY_URL
```

![](images/Pasted%20image%2020260319181844.png)

等待 Terminal 重新可输入，即可看到项目已被克隆到本地。

![](images/Pasted%20image%2020260319181926.png)