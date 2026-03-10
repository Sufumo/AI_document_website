---
layout: doc
title: KIMI Configuration Guide · KIMI 配置教程
---
> Pre-reading Note
>
> Before using this KIMI configuration guide, it is recommended to:
>
> - Be familiar with opening a terminal and running simple commands (you can review [Terminal Basics](/contents/Basic-tools/01-terminal-basics.html) if needed).
>
> This will make it easier to follow the steps for obtaining an API key, setting environment variables, and launching Claude Code with KIMI.
>

> 阅前说明
>
> 在阅读本篇 KIMI 配置教程前，建议您：
>
> - 熟悉如何打开终端并运行简单命令（如有需要，可先阅读 [Terminal 基础](/contents/Basic-tools/01-terminal-basics.html)）。
>
> 具备这些基础后，按照本教程获取 API Key、配置环境变量并使用 KIMI 启动 Claude Code 会更加轻松。


# KIMI Configuration Guide
# KIMI 配置教程

![](./images/Pasted%20image%2020260310143951.png)
## Step 1: Get Your KIMI API Key
## 步骤一：获取 KIMI 的通行密钥

Open [https://platform.moonshot.cn/console/api-keys](https://platform.moonshot.cn/console/api-keys) and log in.
打开 [https://platform.moonshot.cn/console/api-keys](https://platform.moonshot.cn/console/api-keys) 并登录。

![](./images/Pasted%20image%2020260303194555.png)

Click **Create API Key** to create a new API key.
点击 **新建 API Key** 创建一个新的 API Key。

![](./images/Pasted%20image%2020260303194920.png)

Enter a name for the API key, select **default** for the project, then click **Confirm** (确定).
输入 API Key 的名称，项目选择 **default**，然后点击 **确定**。

![](./images/Pasted%20image%2020260303195050.png)

**Note**: The key is shown only once, so save it in a safe place immediately.
**注**：密钥只会显示一次，请及时妥善保存。

![](./images/Pasted%20image%2020260303195345.png)

## Step 2: Top Up Your KIMI Account
## 步骤二：KIMI 账户充值

**KIMI API keys require a paid balance; without top-up, the API cannot be used.**
**KIMI 的 API Key 需账户有余额方可使用，未充值则无法调用接口。**

- In the left sidebar: **Financial** → **Account Top-up** (财务管理 → 账户充值).
- 在左侧栏进入 **财务管理** → **账户充值**。
- Choose an amount, complete payment, and the balance will be available for your API key.
- 选择金额并完成支付后，即可为该 API Key 使用余额。

![](./images/Pasted%20image%2020260306114112.png)

## Step 3: Configure Claude Code with KIMI
## 步骤三：配置 Claude Code（KIMI）

### Method 1: Configure via the visual app
### 方法一：通过可视化 APP 配置

After installing the app, double-click **AGENT_MANAGER.command** to open it.
安装完成后，双击打开 **AGENT_MANAGER.command**。

![](./images/Pasted%20image%2020260306111847.png)

Open the **KIMI** tab, enter your API Key, and then click **Install & configure**. Please refer to Step 1 if you still need to create an API key.
点击 **KIMI** 选项卡，输入 API Key，然后点击 **Install & configure**。如果尚未获取 API Key，请先参照步骤一。

![](./images/Pasted%20image%2020260306114430.png)

When you see that KIMI is configured successfully, the setup is complete.
当界面显示 KIMI 已配置成功即表示完成。

![](./images/Pasted%20image%2020260306114556.png)

After configuration, you can run the `kimi` command in the terminal to launch Claude Code with KIMI.
配置完成后，在终端输入 `kimi` 即可使用 KIMI 进入 Claude Code。

![](./images/Pasted%20image%2020260306114634.png)

You can directly ask the agent which model it is using. As shown below, it is the kimi-k2.5 model.
你可以直接询问 agent 使用的是什么模型。如下所示，为 kimi-k2.5 模型。

![](./images/fcb0a0365799f8680cbf2116e80f73ce.png)

### Method 2: Configure via environment variables
### 方法二：使用环境变量配置

Go to **Go → Home** to open your Home directory.
依次点击 **Go → Home** 打开 Home 目录。

![](./images/Pasted%20image%2020260303192106.png)

Press `Command + Shift + .` to show hidden files, then open the **.zshrc** file.
使用 `Command + Shift + .` 显示隐藏文件，并打开 **.zshrc** 文件。

![](./images/Pasted%20image%2020260303200006.png)

Paste the following lines at the end of **.zshrc**, and replace `your API KEY` with your actual KIMI API key. Please refer to Step 1 if you still need to create an API key.
将下面两行复制到 **.zshrc** 文件末尾，并把 `your API KEY` 替换为你的实际 API Key。如果尚未获取 API Key，请先参照步骤一。

```sh
export ANTHROPIC_BASE_URL="https://api.moonshot.cn/anthropic/"
export ANTHROPIC_API_KEY="your API KEY"
```

![](./images/Pasted%20image%2020260303200243.png)

Save the file. Press `Option + Space` to open search, type **Terminal**, and press Enter to open Terminal.
保存文件后，使用 `Option + Space` 打开搜索，输入 **Terminal** 并按下 Enter 打开终端。

![](./images/Pasted%20image%2020260303190946.png)

In Terminal, run `source .zshrc` so the new environment variables take effect. When the prompt returns, the variables are active.
在终端输入 `source .zshrc` 使环境变量生效；当命令行恢复可输入状态即表示环境变量已生效。

![](./images/Pasted%20image%2020260303200438.png)

Run `claude` and press Enter. When Claude Code shows **Detected a custom API Key in your environment**, click **Yes** to use it.
在终端输入 `claude` 并按下 Enter；当 Claude Code 提示 **Detected a custom API Key in your environment** 时，点击 **Yes** 使 API Key 生效。

![](./images/Pasted%20image%2020260303200736.png)

You can then use Claude Code as usual with KIMI.
之后即可正常使用 Claude Code（KIMI）。

![](./images/Pasted%20image%2020260303200846.png)

You can directly ask the agent which model it is using. As shown below, it is the kimi-k2.5 model.
你可以直接询问 agent 使用的是什么模型。如下所示，为 kimi-k2.5 模型。

![](./images/fcb0a0365799f8680cbf2116e80f73ce.png)


### Launching Claude Code with `kimi`
### 使用 `kimi` 启动 Claude Code

If you want to launch Claude Code with the `kimi` command, follow the steps below. Go to **Go → Home** to open your Home directory.
若希望通过 `kimi` 命令启动 Claude Code，请按以下步骤操作。依次点击 **Go → Home** 打开 Home 目录。

![](./images/Pasted%20image%2020260303192106.png)

Press `Command + Shift + .` to show hidden files, then open the **.claude** folder.
使用 `Command + Shift + .` 显示隐藏文件，并打开 **.claude** 文件夹。

![](./images/Pasted%20image%2020260303192303.png)

Copy **settings.json** and rename the copy to **kimi-settings.json**.
将 **settings.json** 复制一份，并重命名为 **kimi-settings.json**。

![](./images/Pasted%20image%2020260310234238.png)

Open **kimi-settings.json** and paste the following content (replace the placeholder with your API key).
打开 **kimi-settings.json**，填入以下内容（将 `replace with your api key` 替换为你的 API Key）。

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.moonshot.cn/anthropic/",
    "ANTHROPIC_AUTH_TOKEN": "replace with your api key"
  },
  "hasCompletedOnboarding": true
}
```

![](./images/Pasted%20image%2020260310234351.png)

Go back to the Home directory and open the **.zshrc** file.
返回 Home 目录，打开 **.zshrc** 文件。

![](./images/Pasted%20image%2020260310234055.png)

Add the following line at the end of the file.
在文件末尾添加以下命令。

```bash
alias kimi="claude --settings ~/.claude/kimi-settings.json"
```

![](./images/Pasted%20image%2020260310233841.png)

Use `Command + Space` to search for **Terminal** and open it.
使用 `Command + 空格` 搜索 **Terminal** 并打开。

![](./images/4.Claude%20code/file-20260113152908876%201.png)

In Terminal, run `source .zshrc`.
在 Terminal 中输入 `source .zshrc`。

![](./images/Pasted%20image%2020260310233106.png)

When the terminal prompt returns, the configuration is complete.
待终端恢复可输入状态即表示配置完成。

![](./images/Pasted%20image%2020260310233154.png)

Run `kimi` to launch Claude Code.
输入 `kimi` 即可启动 Claude Code。

![](./images/Pasted%20image%2020260310234456.png)

![](./images/Pasted%20image%2020260310233250.png)
