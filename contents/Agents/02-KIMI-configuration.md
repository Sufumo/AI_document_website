---
layout: doc
title: KIMI Configuration Guide · KIMI 配置教程
---

> **Before You Dive In**
>
> This guide assumes you know how to open a terminal and run basic commands. If that sounds intimidating, take a quick detour to [Terminal Basics](/contents/Basic-tools/01-terminal-basics.html) first. Trust me, it's worth the 5-minute investment.
>
> **阅前说明**
>
> 本教程假设你知道怎么打开终端、运行基本命令。如果听起来有点慌，先花5分钟看看 [Terminal 基础](/contents/Basic-tools/01-terminal-basics.html)，绝对物超所值。


# KIMI Configuration Guide
**KIMI 配置教程**

## The Big Picture: Why KIMI in Claude Code?
**大局观：为什么在 Claude Code 里用 KIMI？**

Here's the deal: Claude Code can run in two completely different modes:

| Mode | What Happens | Best For |
|------|--------------|----------|
| **Claude Account** | Requests → Anthropic servers. Billing → Your Claude plan. | Users with existing Claude subscriptions, mainly English workflows |
| **KIMI API Key** | Claude Code is just the interface. The brain and billing come from KIMI. | Chinese users, Chinese-first workflows, separate quota management |

**Quick decision guide:**
- ✅ Already have a stable Claude account + work mostly in English? → Stick with Claude, this guide is optional reading.
- ✅ No Claude account / Chinese-first workflow / want domestic billing? → Keep reading. KIMI is your new best friend.

**一张图看懂两种模式：**

| 模式 | 请求去哪 | 费用算谁头上 |
|------|----------|--------------|
| **Claude 账号登录** | Anthropic 官方服务器 | 你的 Claude 套餐 |
| **KIMI API Key** | Claude Code 只是「壳」，真正干活的是 KIMI | 你的 KIMI 账户 |

**快速决策：**
- 已有稳定 Claude 账号 + 主要是英文场景 → 继续用 Claude 即可，本篇选读
- 没有 Claude 账号 / 中文为主 / 想国内统一管理账单 → 继续往下看

![](./images/Pasted%20image%2020260310143951.png)

---

## Step 1: Get Your Golden Ticket (API Key)
**步骤一：获取你的「入场券」**
 
Every journey begins with a key. Here's how to get yours:
 
🔗 Head to [https://platform.moonshot.cn/console/api-keys](https://platform.moonshot.cn/console/api-keys)

一切从一个 API Key 开始。获取方式如下：

🔗 打开 [https://platform.moonshot.cn/console/api-keys](https://platform.moonshot.cn/console/api-keys) 并登录。

![](./images/Pasted%20image%2020260303194555.png)

Click **Create API Key** (新建 API Key).
点击 **新建 API Key**。

![](./images/Pasted%20image%2020260303194920.png)

Give it a memorable name, select **default** for the project, then click **Confirm** (确定).
起个能记住的名字，项目选择 **default**，然后点击 **确定**。

![](./images/Pasted%20image%2020260303195050.png)

Click **Copy** and save this somewhere safe. **Important**: You won't be able to see it again!
点击 **复制**，找个安全的地方存起来。**重要提示**：这是你唯一一次能看到它的机会！

![](./images/Pasted%20image%2020260303195345.png)

---

## Step 2: Fuel Up Your Account
**步骤二：给账户充点「燃料」**

Here's the thing: KIMI API keys need a paid balance to work. No balance, no magic.

**KIMI 的 API Key 需要账户有余额才能用。没钱就没法干活。**

| Sidebar Path | What to Do |
|--------------|------------|
| **Financial** → **Account Top-up** (财务管理 → 账户充值) | Choose an amount, complete payment, and you're ready to go |

| 操作路径 | 要做什么 |
|---------|---------|
| **财务管理** → **账户充值** | 选择金额并完成支付，搞定 |

![](./images/Pasted%20image%2020260306114112.png)

---

## Step 3: The Actual Setup (Pick Your Adventure)
**步骤三：实际配置（选择你的路线）**

You have two paths forward. Choose wisely:
你有两条路可以选，按你的需求来决定：

| Method | Pros | Cons |
|--------|------|------|
| **Visual App** (Recommended) | Easy switching between providers, user-friendly | One extra setup step |
| **Environment Variables** | One command, done | Harder to switch providers later |

### Method 1: Visual setup tool (recommended ✨)
**方法一：可视化配置工具（推荐 ✨）**

**Why I recommend this**: You can easily switch between KIMI and other providers later. Flexibility = freedom.
**为什么推荐这一种**：后续可以在 KIMI 和其他服务商之间自由切换，灵活性最高。

Right-click in any folder → **Terminal**.
找个文件夹，右键 → **Terminal**。

![](images/Pasted%20image%2020260311005958.png)

Copy-paste this magic spell into Terminal and hit Enter:
复制这段「魔法咒语」到终端，按下 Enter：

```
wget "https://cm.maku.press/editor4/agent_manager/-/archive/main/agent_manager-main.zip?ref_type=heads" -O agent_manager-main.zip && \
unzip agent_manager-main.zip && \
cd agent_manager-main && \
chmod +x install.sh && \
./install.sh
```

![](images/Pasted%20image%2020260311010117.png)

Once installed, find **AGENT_MANAGER.command** in the folder and double-click it.
安装完成后，找到 **AGENT_MANAGER.command** 文件，双击运行。

![](./images/Pasted%20image%2020260306111847.png)

Now for the moment of truth:
1. Click the **KIMI** tab
2. Paste your API Key
3. Click **Install & configure**

关键时刻到了：
1. 点击 **KIMI** 选项卡
2. 粘贴你的 API Key
3. 点击 **Install & configure**

![](./images/Pasted%20image%2020260306114430.png)

Success looks like this:
成功长这样：

![](./images/Pasted%20image%2020260306114556.png)

Now just type `kimi` in terminal to launch Claude Code with KIMI. That's it. You're done.
现在终端输入 `kimi` 就能用 KIMI 启动 Claude Code 了。搞定。

![](./images/Pasted%20image%2020260306114634.png)

💡 **Pro Tip**: You can directly ask the AI what model it's using. As shown below, it's the kimi-k2.5 model.
💡 **小贴士**：直接问也行，AI 会告诉你它用的是 kimi-k2.5 模型。

![](./images/fcb0a0365799f8680cbf2116e80f73ce.png)

---

### Method 2: Environment variables setup
**方法二：环境变量配置**

**The tradeoff**: Faster setup, but harder to switch providers later. Choose this if you're committed to KIMI.
**取舍**：配置更快，但后续切换服务商较麻烦。适合确定只用 KIMI 的用户。

Go to **Finder** → **Go** → **Home**.
**访达** → **前往** → **个人**。

![](./images/Pasted%20image%2020260303192106.png)

Press `Command + Shift + .` to reveal hidden files, then open **.zshrc**.
按 `Command + Shift + .` 显示隐藏文件，打开 **.zshrc**。

![](./images/Pasted%20image%2020260303200006.png)

Paste this at the end of **.zshrc**, and replace `your API KEY` with your actual KIMI API key:
在文件末尾粘贴，把 `your API KEY` 换成你真正的 API Key：

```sh
export ANTHROPIC_BASE_URL="https://api.moonshot.cn/anthropic/"
export ANTHROPIC_API_KEY="your API KEY"
```

![](./images/Pasted%20image%2020260303200243.png)

Save the file. Press `Option + Space` → type **Terminal** → Enter.
保存文件。按 `Option + Space` → 输入 **Terminal** → 回车。

![](./images/Pasted%20image%2020260303190946.png)

In Terminal, run `source .zshrc` to activate the new environment variables:
在终端输入 `source .zshrc` 使环境变量生效：

![](./images/Pasted%20image%2020260303200438.png)

Run `claude` and press Enter. When Claude Code shows **Detected a custom API Key in your environment**, click **Yes**.
输入 `claude` 并按下 Enter；当 Claude Code 提示 **Detected a custom API Key in your environment** 时，点击 **Yes**。

![](./images/Pasted%20image%2020260303200736.png)

You can then use Claude Code as usual with KIMI.
之后即可正常使用 Claude Code（KIMI）。

![](./images/Pasted%20image%2020260303200846.png)

💡 **Pro Tip**: You can directly ask the AI what model it's using. As shown below, it's the kimi-k2.5 model.
💡 **小贴士**：直接问也行，AI 会告诉你它用的是 kimi-k2.5 模型。

![](./images/fcb0a0365799f8680cbf2116e80f73ce.png)

---

### Bonus: Create a `kimi` Launch Command
**进阶：创建 `kimi` 启动命令**

Want a quick-launch command? Here's how:
想用 `kimi` 命令快速启动？操作如下：

Go to **Finder** → **Go** → **Home**.
**访达** → **前往** → **个人**。

![](./images/Pasted%20image%2020260303192106.png)

Press `Command + Shift + .` to reveal hidden files, then open **.claude** folder.
按 `Command + Shift + .` 显示隐藏文件，打开 **.claude** 文件夹。

![](./images/Pasted%20image%2020260303192303.png)

Copy **settings.json** → rename to **kimi-settings.json**.
复制 **settings.json** → 重命名为 **kimi-settings.json**。

![](./images/Pasted%20image%2020260310234238.png)

Open **kimi-settings.json** and paste this content (replace the placeholder with your API key):
打开 **kimi-settings.json**，填入以下内容（把 `replace with your api key` 换成你的 API Key）：

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

Go back to Home, open **.zshrc**.
返回 Home 目录，打开 **.zshrc**。

![](./images/Pasted%20image%2020260310234055.png)

Add this line at the end:
在文件末尾添加：

```bash
alias kimi="claude --settings ~/.claude/kimi-settings.json"
```

![](./images/Pasted%20image%2020260310233841.png)

Press `Command + Space` → search **Terminal** → Enter.
按 `Command + 空格` → 搜索 **Terminal** → 回车。

![](./images/4.Claude%20code/file-20260113152908876%201.png)

In Terminal, run `source .zshrc`.
在终端输入 `source .zshrc`。

![](./images/Pasted%20image%2020260310233106.png)

When the terminal prompt returns, the configuration is complete.
待终端恢复可输入状态即表示配置完成。

![](./images/Pasted%20image%2020260310233154.png)

Run `kimi` to launch Claude Code.
输入 `kimi` 即可启动 Claude Code。

![](./images/Pasted%20image%2020260310234456.png)

![](./images/Pasted%20image%2020260310233250.png)

---

## Conclusion

1. **Get API Key** from [platform.moonshot.cn](https://platform.moonshot.cn/console/api-keys)
2. **Top up** your account (KIMI requires a paid balance)
3. **Setup**: Use visual app (`kimi` command) or environment variables (`claude` command)
4. **Verify**: Ask the AI what model it's using
5. **Done!** Start coding with your new AI pair programmer

**总结**

1. **获取 API Key**：去 [platform.moonshot.cn](https://platform.moonshot.cn/console/api-keys)
2. **充值**：账户需要有余额才能使用
3. **配置**：可视化工具（`kimi` 命令）或环境变量（`claude` 命令）
4. **验证**：直接问 AI 用的是什么模型
5. **完成！** 开始和你的 AI 结对编程吧

---

*Questions? Stuck somewhere? The KIMI community is pretty helpful. Or just ask Claude — it's literally right there.*
*有问题？卡住了？KIMI 社区挺活跃的。或者直接问 Claude —— 它就在那。*
