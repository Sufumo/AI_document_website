---
title: Git Beginner Hands-on Guide
draft: false
prev: Basic-tools/01-terminal-basics
next: Agents/01-GLM-configuration
---
# Git Beginner Hands-on Guide

## What problem does Git actually solve?

Imagine this: you and a teammate are writing a book together. Your teammate drafts the outline first, then you add and revise content. If every update is shared by manually sending files back and forth, your computers quickly fill up with copies like "final-v2-real-final". Even worse, if your teammate updates something without telling you, and you edit the same part, you'll have to manually compare and decide whose version to keep.

To solve this, you decide to use a "middleman" to manage all versions in one place: always fetch the latest version before editing, submit changes after editing, and roll back whenever needed. Git plays exactly that "version middleman" role.

## Install Git

### Method 1: Install Git with an Agent (Recommended)

Open your Agent tool (such as Claude Code), enter `please help me install and config git, my name is "Your Name", my email is "email@example.com"`, and wait for the task to finish.

>[!NOTE]
>
> Git does not strictly require a real username or email. It will still work with `Your Name` and `email@example.com`.  
> But once you push to the cloud, others can see your commit identity, so it's better to use your real nickname and email.

![](images/Pasted%20image%2020260319163137.png)
### Method 2: Install Git on macOS

>[!TIP]
>
> This section assumes basic terminal and command-line knowledge. If you're not comfortable yet, spend 5 minutes reading [Terminal Basics](../../../Basic-tools/01-terminal-basics) and [Homebrew Installation](../../../Basic-tools/05-homebrew-install) first.

After confirming Homebrew is installed, press `Option + Space`, search for Terminal, and open it.

![](images/Pasted%20image%2020260319135151.png)

Copy the following command into Terminal to install Git with Homebrew.

```plain
brew install git
```

![](images/Pasted%20image%2020260319135330.png)

When the command line becomes available again, Git installation is complete.

![](images/Pasted%20image%2020260319135506.png)

After installing Git, there is one final setup step. Run the following commands in Terminal:

```
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```

> [!NOTE]
> 
> Git does not strictly require a real username or email. It can still work with `Your Name` and `email@example.com`.  
> But when you push to the cloud, others will see your commit identity, so it's better to use your own nickname and email.

![](images/Pasted%20image%2020260319163330.png)

When the command line becomes available again, Git configuration is done.

![](images/Pasted%20image%2020260319163303.png)

## Basic Git Operations

>[!TIP]
>
> VS Code makes Git management very convenient. If you haven't installed VS Code yet, spend 3 minutes reading [VSCode Usage Guide](../../../Apps/01-vscode-usage) first.

Open VS Code, choose a working folder, then click the branch-like **Source Control** icon in the left sidebar.

At first, there is no version history yet. Only projects tracked by Git will record file history, so it's best to initialize your repository early. Click **Initialize Repository** to turn the current folder into a tracked repository.

![](images/Pasted%20image%2020260319140656.png)

This is the main Git workspace. The **CHANGES** area at the top is for reviewing and handling edits (such as staging or undoing). The **GRAPH** area below shows commit history. You can think of each commit as a "reviewable and shareable" snapshot.

![](images/Pasted%20image%2020260319142054.png)

After creating a test file in the folder, you'll see `U` next to the file name. That means the file is **untracked**. Git doesn't know what baseline to compare against yet, so you need to add it to tracking first.

![](images/Pasted%20image%2020260319143208.png)

Click the `+` button shown below to add the file to the staging area (**Staged Changes**).

![](images/Pasted%20image%2020260319143524.png)

Now the file moves into **Staged Changes**, and the left-side symbol becomes `A`, meaning this is a newly added file (**Added**).

![](images/Pasted%20image%2020260319143828.png)

Now change the text to `hello, this is a new text`.

![](images/Pasted%20image%2020260319144414.png)

Back in the Git panel, the file changes to `M`, meaning it has been modified. The diff editor on the right shows changes: red = deleted content, green = added content. In this case, `hello, this is the original text` is removed and `hello, this is a new text` is added.

Git tracks changes line by line. Even if you change just one word, Git may show it as deleting the old line and adding a new one.

>[!NOTE]
>
> The `test-tutorial.md` file in `Staged Changes` may also display `M`.  
> That does not mean "history was modified"; it simply means there is a difference between the working directory and staging area for this file.  
> If you stage the latest edits from `Changes` again, the status updates to the latest state.

![](images/Pasted%20image%2020260319144805.png)

If you're not happy with the file and delete it, you'll see a file with `D` in `Changes`, meaning it has been deleted.

![](images/Pasted%20image%2020260319150004.png)

To undo this action, click the undo button highlighted below to restore the file.

![](images/Pasted%20image%2020260319150123.png)

You can also click **Unstage Changes** to move staged content back to the `Changes` area.

![](images/Pasted%20image%2020260319150334.png)

When you're happy with content in `Staged Changes`, write a commit message and click **Commit** to save a new version.

![](images/Pasted%20image%2020260319150900.png)

You can see this new commit in the GRAPH view.

> [!NOTE]
> 
> This version is currently saved only on your local machine.  
> To share it with others, connect a remote repository and push it.

![](images/Pasted%20image%2020260319151009.png)

## Git Authentication

To securely connect local Git to a remote repository, Git typically uses **SSH keys** for identity verification. You generate a key pair locally, add the public key to platforms like GitLab/GitHub, and then those platforms can verify that pushes and pulls are really from you. Below we use GitLab as an example.

## Configure Git Identity (SSH)

### Method 1: Get an SSH key with Agent

Open your Agent tool and enter: `please generate a ssh key for me and show me the public key to configure on gitlab`.

![](images/Pasted%20image%2020260319174529.png)

Once the task finishes, you'll see the public key content ready to copy.

![](images/Pasted%20image%2020260319174701.png)

### Method 2: Get an SSH key with Terminal

Open Terminal and run the following commands. Replace `"you@example.com"` with your email (keep the quotes).

```
ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub
```

![](images/Pasted%20image%2020260319173628.png)

If prompted with `Enter file in which to save the key...`, just press Enter.

![](images/Pasted%20image%2020260319173725.png)

Then you'll see one line starting with `ssh-ed25519` — that's your public key.

![](images/Pasted%20image%2020260319173812.png)

## Add your SSH public key to GitLab

Click avatar -> **Preferences** -> **SSH Keys** to enter the key configuration page.

![](images/Pasted%20image%2020260319172911.png)

At this point, you'll see no SSH keys configured yet.

![](images/Pasted%20image%2020260319173151.png)

Click **Add new key** to create a new key entry.

![](images/Pasted%20image%2020260319173930.png)

Paste the public key you copied into the `Key` input box, then click **Add key**.

![](images/Pasted%20image%2020260319174033.png)

After this, the key is active.

![](images/Pasted%20image%2020260319174158.png)

## Create a new remote repository

Open your Git hosting platform, then click **Projects -> New project**.

![](images/Pasted%20image%2020260319154451.png)

Click **Create blank project**.

![](images/Pasted%20image%2020260319154618.png)

Fill in the following:
- Set **Project Name**, preferably the same as your local project folder.
- Choose your username under **Project URL**.
- **Visibility Level** controls who can see the repo: `Private` (invite only), `Internal` (visible to users in the same organization), `Public` (visible to everyone).
- In **Project Configuration**, it's recommended to uncheck **Initialize repository with a README**. Otherwise, the remote repo starts with a README and your first push may fail due to mismatched histories.

After filling in everything, click **Create project**.

![](images/Pasted%20image%2020260319155130.png)

## Connect local repository to remote repository

### Method 1: Connect with Agent

Inside the repository page, click **Code -> Copy URL**, and copy the URL on the right side of **Clone with HTTPS**.

![](images/Pasted%20image%2020260319171744.png)

Open Agent, enter `Please help me push this folder to this Git repository.`, paste the copied URL, and wait for completion.

![](images/Pasted%20image%2020260319171852.png)

### Method 2: Connect with Terminal

Inside the repository page, click **Code -> Copy URL**, and copy the URL on the right side of **Clone with HTTPS**.

![](images/Pasted%20image%2020260319171744.png)

Open Terminal in your working directory, replace `YOUR_REPOSITORY_URL` with your repo URL, then run:

```
git remote add origin YOUR_REPOSITORY_URL
git push origin main
```

After execution, check the repository page and you'll see your local version uploaded to the cloud.

![](images/Pasted%20image%2020260319172053.png)

![](images/Pasted%20image%2020260319170746.png)

## Connect an existing Git repository

### Method 1: Clone with Agent

Inside the repository page, click **Code -> Copy URL**, and copy the URL on the right side of **Clone with HTTPS**.

![](images/Pasted%20image%2020260319171744.png)

Choose a working directory and open Agent. Enter `please clone this project for me`, then paste the copied URL into the chat box.

![](images/Pasted%20image%2020260319175956.png)

After the task completes, the project will be cloned locally.

>[!NOTE]
>
> A cloned project usually needs no extra setup. As long as you have repository permission, you can push to and pull from the remote repository.

![](images/Pasted%20image%2020260319180634.png)

### Method 2: Clone with Terminal

Inside the repository page, click **Code -> Copy URL**, and copy the URL on the right side of **Clone with HTTPS**.

![](images/Pasted%20image%2020260319171744.png)

Open Terminal in your working directory, replace `YOUR_REPOSITORY_URL` with your repository URL, then run:

```
git clone YOUR_REPOSITORY_URL
```

![](images/Pasted%20image%2020260319181844.png)

When Terminal becomes available again, the project has been cloned to your local machine.

![](images/Pasted%20image%2020260319181926.png)
