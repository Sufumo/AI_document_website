---
layout: doc
title: GLM Configuration Guide · GLM 配置教程
---

> **Before You Dive In**
>
> This guide assumes you know how to open a terminal and run basic commands. If that sounds intimidating, take a quick detour to [Terminal Basics](/contents/Basic-tools/01-terminal-basics.html) first. Trust me, it's worth the 5-minute investment.
>
> **阅前说明**
>
> 本教程假设你知道怎么打开终端、运行基本命令。如果听起来有点慌，先花5分钟看看 [Terminal 基础](/contents/Basic-tools/01-terminal-basics.html)，绝对物超所值。


# GLM Configuration Guide
**GLM 配置教程**

## The Big Picture: Why GLM in Claude Code?
**大局观：为什么在 Claude Code 里用 GLM？**

Here's the deal: Claude Code can run in two completely different modes:

| Mode | What Happens | Best For |
|------|--------------|----------|
| **Claude Account** | Requests → Anthropic servers. Billing → Your Claude plan. | Users with existing Claude subscriptions, mainly English workflows |
| **GLM API Key** | Claude Code is just the interface. The brain and billing come from GLM. | Chinese users, domestic billing, separate quota management |

**Quick decision guide:**
- ✅ Already have a stable Claude account + work mostly in English? → Stick with Claude, this guide is optional reading.
- ✅ No Claude account / Chinese-first workflow / want domestic billing? → Keep reading. GLM is your new best friend.

**一张图看懂两种模式：**

| 模式 | 请求去哪 | 费用算谁头上 |
|------|----------|--------------|
| **Claude 账号登录** | Anthropic 官方服务器 | 你的 Claude 套餐 |
| **GLM API Key** | Claude Code 只是「壳」，真正干活的是 GLM | 你的 GLM 账户 |

**快速决策：**
- 已有稳定 Claude 账号 + 主要是英文场景 → 继续用 Claude 即可，本篇选读
- 没有 Claude 账号 / 中文为主 / 想国内统一管理账单 → 继续往下看

![](./images/Pasted%20image%2020260310154428.png)

---

## Step 1: Get Your Golden Ticket (API Key)

Every journey begins with a key. Here's how to get yours:

🔗 Head to [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)

**步骤一：获取你的「入场券」**

一切从一个 API Key 开始。获取方式如下：

🔗 打开 [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)

![](./images/Pasted%20image%2020260303185459.png)

Click **Create a new API Key**.
点击 **Create a new API Key**。

![](./images/Pasted%20image%2020260303185651.png)

Give it a memorable name (like "claude-code-key" — future you will thank present you), then click **Yes**.
起个能记住的名字（比如「claude-code-key」——未来的你会感谢现在的你），然后点击 **Yes**。

![](./images/Pasted%20image%2020260303185744.png)

Click **Copy** and save this somewhere safe. **Important**: You won't be able to see it again!
点击 **Copy**，找个安全的地方存起来。**重要提示**：这是你唯一一次能看到它的机会！

![](./images/Pasted%20image%2020260303185954.png)

---

## Step 2: To Subscribe or Not to Subscribe?

Here's where you make a choice:

| Option | What You Get | Who It's For |
|--------|--------------|--------------|
| **No Subscription** | Free quota + GLM-4.7 access | Casual users, testing the waters |
| **GLM Coding Plan** | GLM-5 access + higher quotas | Power users, heavy daily usage |

**My recommendation**: Start with the free tier. Upgrade later if you hit the limits. No pressure. [You can click here to subscribe](/contents/Agents/01-GLM-configuration.html#-glm-coding-plan-subscription-details)

**步骤二：订阅还是不订阅？这是个问题**

| 选项 | 你能得到什么 | 适合谁 |
|------|--------------|--------|
| **不订阅** | 免费额度 + GLM-4.7 | 轻度用户、尝鲜党 |
| **GLM Coding Plan** | GLM-5 + 更高额度 | 重度用户、天天用 |

**我的建议**：先用免费版试试水，不够用了再升级。别有压力。[点这里订阅](/contents/Agents/01-GLM-configuration.html#-glm-coding-plan-subscription-details)

---

## Step 3: The Actual Setup (Pick Your Adventure)
**步骤三：实际配置（选择你的路线）**

You have two paths forward. Choose wisely:
你有两条路可以选，按你的需求来决定：

| Method | Pros | Cons |
|--------|------|------|
| **Visual App** (Recommended) | Easy switching between providers, user-friendly | One extra setup step |
| **Official Script** | One command, done | Harder to switch providers later |

### Method 1: Visual setup tool (recommended ✨)
**方法一：可视化配置工具（推荐 ✨）**

**Why I recommend this**: You can easily switch between GLM and other providers later. Flexibility = freedom.
**为什么推荐这一种**：后续可以在 GLM 和其他服务商之间自由切换，灵活性最高。

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
1. Paste your API Key
2. Select your model
3. Click **Install & configure**

关键时刻到了：
1. 粘贴你的 API Key
2. 选择模型
3. 点击 **Install & configure**

⚠️ **Critical Warning**: Don't select `glm-5` unless you've subscribed! Your code will break and you'll be confused.
⚠️ **重要警告**：没订阅千万别选 `glm-5`！选了会出问题，到时候别说我没提醒你。

![](./images/Pasted%20image%2020260306113120.png)

Success looks like this:
成功长这样：

![](./images/Pasted%20image%2020260306113321.png)

Now just type `glm` in terminal to launch Claude Code with GLM. That's it. You're done.
现在终端输入 `glm` 就能用 GLM 启动 Claude Code 了。搞定。

![](./images/Pasted%20image%2020260303152714.png)

**Verification time**: Restart Claude Code, type `/model`. You should see **GLM-5** in the list.
**验证一下**：重启 Claude Code，输入 `/model`。应该能看到 **GLM-5**。

![](./images/Pasted%20image%2020260303193201.png)

![](./images/Pasted%20image%2020260303193234.png)

💡 **Pro Tip**: GLM-5 is like Claude Opus — powerful but expensive. Use it for complex tasks. For everyday stuff, GLM-4.7 is your friend. Also, peak hours (14:00-18:00 UTC+8) might feel slower.
💡 **小贴士**：GLM-5 相当于 Claude Opus，强但费额度。复杂任务用它，日常任务用 GLM-4.7 省着点。另外高峰期（14:00-18:00 北京时间）可能会慢。

You can also just ask the AI what model it's using:
直接问也行：

![](./images/Pasted%20image%2020260310101707.png)

---

### Method 2: Official one-click script
**方法二：官方一键脚本**

**The tradeoff**: Faster setup, but harder to switch providers later. Choose this if you're committed to GLM.

Press `Option + Space` → type **Terminal** → Enter.
按 `Option + Space` → 输入 **Terminal** → 回车。

![](./images/Pasted%20image%2020260303190946.png)

Copy-paste and run:
复制运行：

```sh
curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh
```

> **What this does**:
> - `curl -O`: Downloads a file from the internet
> - `bash`: Runs the downloaded script
>
> **命令解释**：
> - `curl -O`：从网上下载文件
> - `bash`：执行下载的脚本

![](./images/Pasted%20image%2020260303191656.png)

When prompted, paste your API Key and press Enter.
提示时粘贴 API Key，按回车。

⚠️ **Note**: The terminal might not show anything when you paste. That's normal. Don't paste twice.
⚠️ **注意**：粘贴时终端可能什么都不显示，这是正常的，别重复粘贴。

![](./images/Pasted%20image%2020260303191343.png)

When the prompt returns, you're done. Type `claude` to start.
终端恢复可输入状态就完成了。输入 `claude` 启动。

![](./images/Pasted%20image%2020260303191816.png)

![](./images/Pasted%20image%2020260303191919.png)

---

### Unlocking GLM-5 (Subscribers Only 🔓)

**GLM-5 解锁教程（仅订阅用户）**

If you subscribed to GLM Coding Plan, here's how to unlock the big guns:
如果你已经订阅了 GLM Coding Plan，可以按下面步骤解锁「大杀器」：

**Finder** → **Go** → **Home**
**访达** → **前往** → **个人**

![](./images/Pasted%20image%2020260303192106.png)

Press `Command + Shift + .` to reveal hidden files, then open **.claude** folder.
按 `Command + Shift + .` 显示隐藏文件，打开 **.claude** 文件夹。

![](./images/Pasted%20image%2020260303192303.png)

Open **settings.json** in your favorite text editor.
用你喜欢的编辑器打开 **settings.json**。

![](./images/Pasted%20image%2020260303192828.png)

**The default mapping looks like this:**
**默认配置如下：**

```json
{
  "env": {
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "GLM-4.7",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "GLM-4.7",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "GLM-4.5-Air"
  }
}
```

**To use GLM-5 everywhere**, replace the contents with:
**想全面启用 GLM-5** ，替换为：

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

⚠️ Replace `"your api key"` with your actual API key!
⚠️ 把 `"your api key"` 换成你真正的 API Key！

Save the file, restart Claude Code, run `/model` to verify.
保存，重启 Claude Code，运行 `/model` 验证。

![](./images/Pasted%20image%2020260303192957.png)

---

### Bonus: Create `glm` and `glm5` Commands
**进阶：创建 `glm` 和 `glm5` 命令**

Want quick-launch commands? Here's how:
想用 `glm` 或 `glm5` 命令快速启动？操作如下：

Copy **settings.json** → rename to **glm-settings.json**.
复制 **settings.json** → 重命名为 **glm-settings.json**。

![](./images/Pasted%20image%2020260310232459.png)

Go back to Home, open **.zshrc**.
返回 Home 目录，打开 **.zshrc**。

![](./images/Pasted%20image%2020260310234055.png)

Add this line at the end:
在文件末尾添加：

```bash
alias glm="claude --settings ~/.claude/glm-settings.json"
```

Or for `glm5`:

或者用 `glm5`：

```bash
alias glm5="claude --settings ~/.claude/glm-settings.json"
```

![](./images/Pasted%20image%2020260310232746.png)

Open a fresh Terminal and run:
打开新终端，运行：

```bash
source .zshrc
```

![](./images/Pasted%20image%2020260310233106.png)

![](./images/Pasted%20image%2020260310233154.png)

Now type `glm` (or `glm5`) and boom — Claude Code launches with GLM.
现在输入 `glm`（或 `glm5`）就能用 GLM 启动 Claude Code 了。

![](./images/Pasted%20image%2020260310233233.png)

![](./images/Pasted%20image%2020260310233250.png)

---

## Conclusion

1. **Get API Key** from [bigmodel.cn](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)
2. **Choose**: Free tier (GLM-4.7) or subscribe (GLM-5)
3. **Setup**: Use visual app (`glm` command) or official script (`claude` command)
4. **Verify**: Run `/model` in Claude Code
5. **Done!** Start coding with your new AI pair programmer

**总结**

1. **获取 API Key**：去 [bigmodel.cn](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)
2. **选择**：免费版（GLM-4.7）或订阅（GLM-5）
3. **配置**：可视化工具（`glm` 命令）或官方脚本（`claude` 命令）
4. **验证**：在 Claude Code 里运行 `/model`
5. **完成！** 开始和你的 AI 结对编程吧

---

*Questions? Stuck somewhere? The GLM community is pretty helpful. Or just ask Claude — it's literally right there.*
*有问题？卡住了？GLM 社区挺活跃的。或者直接问 Claude —— 它就在那。*

### 📖 GLM Coding Plan subscription details

**📖 GLM Coding Plan 订阅详情**

Click **My Plan** (我的套餐) to open the subscription page.
点击 **My Plan** 进入「我的套餐」。

![](./images/Pasted%20image%2020260306112528.png)

Click **GLM Coding plan** to see your options.
点击 **GLM Coding plan** 进入订阅界面。

![](./images/Pasted%20image%2020260306112619.png)

Subscribe here. Without subscription, you get free quota but **no GLM-5**.
在此页面订阅。不订阅有一定免费额度，但**无法使用 GLM-5**。

![](./images/Pasted%20image%2020260306112719.png)
