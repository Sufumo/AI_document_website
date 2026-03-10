---
layout: doc
title: GLM 配置教程
---

## 阅前说明
> Pre-reading Note
>
> Before using this GLM configuration guide, it is recommended to understand a few basic concepts and tools:
>
> - Know how to open a terminal on your system and run simple commands (you can review [Basic-tools/01-terminal-basics](/contents/Basic-tools/01-terminal-basics.html) if needed).
>
> With this background, following the steps to fetch API keys and edit configuration files in this guide will be much easier and less error-prone.
>

> 阅前说明
>
> 在阅读本篇 GLM 配置教程前，建议先了解以下基础内容：
>
> - 知道如何在自己的系统上打开终端并运行简单命令（如有需要，可先阅读 [Basic-tools/01-terminal-basics](/contents/Basic-tools/01-terminal-basics.html)）。
>
> 具备以上基础后，按照本教程获取 API Key 并修改配置文件会更顺畅，也更不容易出错。


# GLM Configuration Guide
# GLM 配置教程

![](./images/Pasted%20image%2020260310154428.png)

## Step 1: Get Your GLM API Key
## 步骤一：获取 GLM 的通行密钥

Go to [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys) and log in or sign up.
访问 [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)，并登录或注册。

![](./images/Pasted%20image%2020260303185459.png)

Click **Create a new API Key** to create a new API key.
点击 **Create a new API Key** 创建一个新的 API Key。

![](./images/Pasted%20image%2020260303185651.png)

Enter a name for the API key, then click **Yes**.
输入 API Key 的名称后点击 **Yes**。

![](./images/Pasted%20image%2020260303185744.png)

Click **Copy** to copy the API key.
点击 **Copy** 即可复制 API Key。

![](./images/Pasted%20image%2020260303185954.png)

## Step 2: Subscribe to GLM (Optional)
## 步骤二：订阅 GLM（可选）

Subscribing to GLM increases your Claude Code usage quota and gives you access to GLM’s latest model, **GLM-5**. However, GLM currently limits the number of available subscriptions, so getting one may be difficult. You can still try other GLM models using the free quota (as of March 9, 2026). Detailed subscription steps have been moved to the appendix **GLM Coding Plan**, so you can skip this section for now and continue with API key setup.
订阅 GLM 可以增加 Claude Code 的可用额度，并可使用 GLM 的最新模型 **GLM-5**。不过，由于 GLM 当前限制了订阅名额，申请订阅可能会有一定难度。即便如此，你仍可使用免费额度体验其他 GLM 模型（截至 2026 年 3 月 9 日）。详细的订阅步骤已移至附录 **GLM Coding Plan**，因此你也可以先跳过本节，直接继续使用 API Key 配置 GLM。

## Step 3: Configure Claude Code with GLM
## 步骤三：配置 Claude Code（GLM）

### Method 1: Configure via the visual app
### 方法一：通过可视化 APP 配置

After installing the app, double-click **AGENT_MANAGER.command** to open it.
安装完成后，双击打开 **AGENT_MANAGER.command**。

![](./images/Pasted%20image%2020260306111847.png)

Enter your API Key, select the **Model**, and then click **Install & configure**. Please refer to Step 1 if you still need to create an API key.
输入 API Key，选择 **Model**，然后点击 **Install & configure**。如果尚未获取 API Key，请先参照步骤一。

**Note**: If you have not subscribed to GLM, do **not** select the **glm-5** model, or Claude Code may not work correctly.
**注**：若未订阅 GLM，请勿选择 **glm-5** 模型，否则 Claude Code 可能无法正常使用。

![](./images/Pasted%20image%2020260306113120.png)

When the interface shows that GLM is configured successfully, the setup is complete.
当界面显示 GLM 已配置成功即表示完成。

![](./images/Pasted%20image%2020260306113321.png)

After configuration, you can run the `glm` command in the terminal to launch Claude Code with GLM.
配置完成后，在终端输入 `glm` 即可使用 GLM 进入 Claude Code。

![](./images/Pasted%20image%2020260303152714.png)

Restart Claude Code and run `/model` to confirm that **GLM-5** is available.
重新打开 Claude Code，输入 `/model`。

![](./images/Pasted%20image%2020260303193201.png)

You should see that the **GLM-5** model is now enabled.
此时即可看到 **GLM-5** 模型已被启用。

**Note**: **GLM-5** is a larger model, comparable to Claude Opus. Use it for complex tasks; for routine tasks, **GLM-4.7** can save quota. “Peak hours” are 14:00–18:00 (UTC+8) and may affect availability or rate limits.
**注**：GLM-5 参数量更大，对标 Claude Opus，建议在复杂任务时切换至 GLM-5，日常任务可继续使用 GLM-4.7 以节省额度。「高峰期」为每日 14:00～18:00（UTC+8）。

![](./images/Pasted%20image%2020260303193234.png)

You can also directly ask the agent which model it is using. As shown below, it is the **GLM-5** model.
你也可以直接询问 agent 使用的是什么模型。如下所示，为 glm-5 模型。

![](./images/Pasted%20image%2020260310101707.png)

### Method 2: Install via the official GLM script
### 方法二：通过 GLM 官方脚本安装

GLM provides a one-click install script. This method modifies Claude Code’s config directly, so switching to another API provider later is less convenient, and you may need to add or switch models manually. The advantage is a quick one-step setup, and usage is similar to the default Claude Code.
GLM 官方提供一键安装脚本。该方法会直接修改 Claude Code 的配置文件，后续如需切换其他 API 供应商会较不便，且需手动添加或切换模型；优点是一键安装，使用方式与原生 Claude Code 类似。

Press `Option + Space` to open search, type **Terminal**, and press Enter to open Terminal.
使用 `Option + Space` 打开搜索，输入 **Terminal** 并按下 Enter 打开终端。

![](./images/Pasted%20image%2020260303190946.png)

Copy the following command into the terminal and press Enter.
将下面的命令复制到终端并按下 Enter。

```sh
curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh
```

> Command explanation:
>
> `curl -O`: Downloads a file from the given URL.
>
> `bash`: Runs a shell script. This command downloads the script and then runs it.

> 命令解释：
>
> `curl -O`：从指定链接下载文件。
>
> `bash`：执行脚本。该命令表示从远程下载脚本并执行。

![](./images/Pasted%20image%2020260303191656.png)

When prompted, paste your GLM API key and press Enter. Please refer to Step 1 if you still need to create an API key.
按提示将已复制的 API Key 粘贴到终端并按下 Enter。如果尚未获取 API Key，请先参照步骤一。

**Note**: Pasted input may not be visible in the terminal; avoid pasting multiple times.
**注**：在终端粘贴内容时可能不会显示，请勿反复粘贴。

![](./images/Pasted%20image%2020260303191343.png)

When the terminal prompt returns, the script has finished.
当终端恢复可输入状态时，表示脚本安装完成。

![](./images/Pasted%20image%2020260303191816.png)

Run `claude` in the terminal to start Claude Code with GLM.
在终端输入 `claude` 即可正常使用 Claude Code（GLM）。

![](./images/Pasted%20image%2020260303191919.png)

### Using the GLM-5 model (optional)
### 使用 GLM-5 模型（可选）

If you have subscribed to GLM, you can use the **GLM-5** model by editing the config. Go to **Go → Home** to open your Home directory.
若已订阅智谱 GLM，可使用 **GLM-5** 模型，需修改配置文件。依次点击 **Go → Home** 打开 Home 目录。

![](./images/Pasted%20image%2020260303192106.png)

Press `Command + Shift + .` to show hidden files, then open the **.claude** folder.
使用 `Command + Shift + .` 显示隐藏文件，并打开 **.claude** 文件夹。

![](./images/Pasted%20image%2020260303192303.png)

Open **settings.json** and edit it.
打开 **settings.json** 并进行修改。

![](./images/Pasted%20image%2020260303192828.png)

Claude Code’s internal model variables map to GLM models. The default mapping is:
Claude Code 内部模型环境变量与 GLM 模型对应关系如下，默认配置为：

- `ANTHROPIC_DEFAULT_OPUS_MODEL`: `GLM-4.7`
- `ANTHROPIC_DEFAULT_SONNET_MODEL`: `GLM-4.7`
- `ANTHROPIC_DEFAULT_HAIKU_MODEL`: `GLM-4.5-Air`

Replace the contents of **settings.json** with the configuration below (use your real API key and ensure **glm-5** is only used if you have a GLM-5 subscription).
将 **settings.json** 中的内容替换为下面配置（将 `your api key` 改为你的 API Key；仅订阅 GLM-5 后再使用 `glm-5`）。

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "your api key",
    "ANTHROPIC_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5"
  },
  "hasCompletedOnboarding": true
}
```

Save the file.
保存文件。

![](./images/Pasted%20image%2020260303192957.png)

Restart Claude Code and run `/model` to confirm that **GLM-5** is available.
重新打开 Claude Code，输入 `/model`。

![](./images/Pasted%20image%2020260303193201.png)

You should see that the **GLM-5** model is now enabled.
此时即可看到 **GLM-5** 模型已被启用。

**Note**: **GLM-5** is a larger model, comparable to Claude Opus. Use it for complex tasks; for routine tasks, **GLM-4.7** can save quota. “Peak hours” are 14:00–18:00 (UTC+8) and may affect availability or rate limits.
**注**：GLM-5 参数量更大，对标 Claude Opus，建议在复杂任务时切换至 GLM-5，日常任务可继续使用 GLM-4.7 以节省额度。「高峰期」为每日 14:00～18:00（UTC+8）。

![](./images/Pasted%20image%2020260303193234.png)

You can also directly ask the agent which model it is using. As shown below, it is the glm-5 model.
你也可以直接询问 agent 使用的是什么模型。如下所示，为 glm-5 模型。

![](./images/Pasted%20image%2020260310101707.png)

## Appendix
## 附录

### GLM Coding Plan
### GLM Coding Plan 订阅说明

Click **My Plan** (我的套餐) to open the subscription page.
点击 **My Plan** 进入「我的套餐」。

![](./images/Pasted%20image%2020260306112528.png)

Click **GLM Coding plan** to open the subscription options.
点击 **GLM Coding plan** 进入订阅界面。

![](./images/Pasted%20image%2020260306112619.png)

You can subscribe to a GLM plan on this page. Without a subscription, a limited free quota is available, but the **GLM-5** model cannot be used.
可在该页面订阅 GLM 计划。如不订阅，有一定免费额度可用，但无法使用 **GLM-5** 模型。

![](./images/Pasted%20image%2020260306112719.png)
