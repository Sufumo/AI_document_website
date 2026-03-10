---
layout: doc
title: KIMI 配置教程
---

## 阅前说明
> Pre-reading Note
>
> Before using this KIMI configuration guide, it is recommended to:
>
> - Be familiar with opening a terminal and running simple commands (you can review [Basic-tools/01-terminal-basics](/contents/Basic-tools/01-terminal-basics.html) if needed).
>
> This will make it easier to follow the steps for obtaining an API key, setting environment variables, and launching Claude Code with KIMI.
>

> 阅前说明
>
> 在阅读本篇 KIMI 配置教程前，建议您：
>
> - 熟悉如何打开终端并运行简单命令（如有需要，可先阅读 [Basic-tools/01-terminal-basics](/contents/Basic-tools/01-terminal-basics.html)）。
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

In the left sidebar, go to **Financial** → **Account Top-up** (财务管理 → 账户充值). Choose an amount and complete the payment to add balance to your API key.
在左侧栏进入 **财务管理** → **账户充值**，选择对应金额并完成支付，即可为 API Key 充值余额。

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