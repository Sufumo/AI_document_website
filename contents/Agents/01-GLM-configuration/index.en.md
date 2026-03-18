---
title: GLM Configuration Guide
draft: false
prev: Basic-tools/05-homebrew-install
next: Agents/04-claude-codel
---

>[!TIP]
>
> This guide assumes you know how to open a terminal and run basic commands. If that sounds intimidating, take a quick detour to [Terminal Basics](../../../Basic-tools/01-terminal-basics) first. Trust me, it's worth the 5-minute investment.


# GLM Configuration Guide

## Why GLM in Claude Code?

**Picture this:**

You download Claude Code, excited to have AI help you write code. You open it and discover — you need a Claude API to use it. You check the official site: subscription requires an international credit card, and there's the worry of account restrictions. Your enthusiasm takes a hit.

**Don't panic. This is exactly when GLM steps in.**

### First, Get One Thing Straight: Claude Code ≠ Claude

Here's the key idea:

**Claude Code is the "hands"; Claude/GLM is the "brain".**

| Role | Represents | What It Does |
|------|------------|--------------|
| **Brain** | Claude, GLM | Understands you, thinks through solutions, makes decisions |
| **Hands** | Claude Code | Writes code, edits files, runs commands |

Claude Code's "hands" are flexible, but they **don't think on their own**. They need a "brain" to tell them what to do.

**The key point: That brain can be Claude, or it can be GLM.**

![](./images/Pasted%20image%2020260316125916.png)

### Why Choose GLM?

Three words: **Easy, efficient, affordable.**

| Your Concern | Claude Option | GLM Option |
|--------------|---------------|------------|
| No international credit card | Subscription is hard | Multiple payment methods, top up directly |
| Worried about account bans | High-frequency use carries risk | Chinese provider, stable |
| Is performance enough? | Top-tier | Open-source #1, more than enough for daily dev |

**In a nutshell:** No Claude account? GLM is a solid Plan B.

### How Capable Is GLM?

GLM-5 ranks **#1 among open-source models** in the [Vending-Bench 2](https://andonlabs.com/evals/vending-bench-2) complex decision-making benchmark (March 2026). GLM-4.7 comes in second.

![](./images/Pasted%20image%2020260316120220.png)

Even compared to top closed-source models, GLM-5 ranks 6th globally — right behind Claude, GPT, Gemini, and Grok. As a "brain," its intelligence is fully up to the task.

![](./images/Pasted%20image%2020260316120041.png)

### The AI Workflow Looks Like This

```
You describe what you need → Brain thinks → Hands write code → Done
```

That simple.

---

**Quick decision guide:**
- ✅ Already have a stable Claude account → Keep using it, this guide is optional
- ✅ No Claude / Want to try GLM → Keep reading and start configuring

![](./images/Pasted%20image%2020260310154428.png)

---

## Step 1: Get Your Golden Ticket (API Key)

Every journey begins with a key. Here's how to get yours:

🔗 Head to [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)

![](./images/Pasted%20image%2020260303185459.png)

Click **Create a new API Key**.

![](./images/Pasted%20image%2020260303185651.png)

Give it a memorable name (like "claude-code-key" — future you will thank present you), then click **Yes**.

![](./images/Pasted%20image%2020260303185744.png)

Click **Copy** and save this somewhere safe. **Important**: You won't be able to see it again!

![](./images/Pasted%20image%2020260303185954.png)

---

## Step 2: To Subscribe or Not to Subscribe?

Here's where you make a choice:

| Option | What You Get | Who It's For |
|--------|--------------|--------------|
| **No Subscription** | Free quota + GLM-4.7 access | Casual users, testing the waters |
| **GLM Coding Plan** | GLM-5 access + higher quotas | Power users, heavy daily usage |

**My recommendation**: Start with the free tier. Upgrade later if you hit the limits. No pressure. [You can click here to subscribe](#-glm-coding-plan-subscription-details)

---

## Step 3: The Actual Setup (Pick Your Adventure)

You have two paths forward. Choose wisely:

| Method | Pros | Cons |
|--------|------|------|
| **Visual App** (Recommended) | Easy switching between providers, user-friendly | One extra setup step |
| **Official Script** | One command, done | Harder to switch providers later |

### Method 1: Visual setup tool (recommended ✨)

**Why I recommend this**: You can easily switch between GLM and other providers later. Flexibility = freedom.

Right-click in any folder → **Terminal**.

![](images/Pasted%20image%2020260311005958.png)

Copy-paste this magic spell into Terminal and hit Enter:

```
wget "https://cm.maku.press/editor4/agent_manager/-/archive/main/agent_manager-main.zip?ref_type=heads" -O agent_manager-main.zip && \
unzip agent_manager-main.zip && \
cd agent_manager-main && \
chmod +x install.sh && \
./install.sh
```

![](images/Pasted%20image%2020260311010117.png)

Once installed, find **AGENT_MANAGER.command** in the folder and double-click it.

![](./images/Pasted%20image%2020260306111847.png)

Now for the moment of truth:
1. Paste your API Key
2. Select your model
3. Click **Install & configure**

>[!WARNING]
>
> Don't select `glm-5` unless you've subscribed! Your code will break and you'll be confused.

![](./images/Pasted%20image%2020260306113120.png)

Success looks like this:

![](./images/Pasted%20image%2020260306113321.png)

Now just type `glm` in terminal to launch Claude Code with GLM. That's it. You're done.

![](./images/Pasted%20image%2020260303152714.png)

**Verification time**: Restart Claude Code, type `/model`. You should see **GLM-5** in the list.

![](./images/Pasted%20image%2020260303193201.png)

![](./images/Pasted%20image%2020260303193234.png)

>[!TIP]
>
> GLM-5 is like Claude Opus — powerful but expensive. Use it for complex tasks. For everyday stuff, GLM-4.7 is your friend. Also, peak hours (14:00-18:00 UTC+8) might feel slower.

You can also just ask the AI what model it's using:

![](./images/Pasted%20image%2020260310101707.png)

---

### Method 2: Official one-click script

**The tradeoff**: Faster setup, but harder to switch providers later. Choose this if you're committed to GLM.

Press `Option + Space` → type **Terminal** → Enter.

![](./images/Pasted%20image%2020260303190946.png)

Copy-paste and run:

```sh
curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh
```

> **What this does**:
> - `curl -O`: Downloads a file from the internet
> - `bash`: Runs the downloaded script

![](./images/Pasted%20image%2020260303191656.png)

When prompted, paste your API Key and press Enter.

>[!NOTE]
>
> The terminal might not show anything when you paste. That's normal. Don't paste twice.

![](./images/Pasted%20image%2020260303191343.png)

When the prompt returns, you're done. Type `claude` to start.

![](./images/Pasted%20image%2020260303191816.png)

![](./images/Pasted%20image%2020260303191919.png)

---

### Unlocking GLM-5 (Subscribers Only 🔓)

If you subscribed to GLM Coding Plan, here's how to unlock the big guns:

**Finder** → **Go** → **Home**

![](./images/Pasted%20image%2020260303192106.png)

Press `Command + Shift + .` to reveal hidden files, then open **.claude** folder.

![](./images/Pasted%20image%2020260303192303.png)

Open **settings.json** in your favorite text editor.

![](./images/Pasted%20image%2020260303192828.png)

**The default mapping looks like this:**

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

>[!WARNING]
>
> Replace `"your api key"` with your actual API key!

Save the file, restart Claude Code, run `/model` to verify.

![](./images/Pasted%20image%2020260303192957.png)

---

### Bonus: Create `glm` and `glm5` Commands

Want quick-launch commands? Here's how:

Copy **settings.json** → rename to **glm-settings.json**.

![](./images/Pasted%20image%2020260310232459.png)

Go back to Home, open **.zshrc**.

![](./images/Pasted%20image%2020260310234055.png)

Add this line at the end:

```bash
alias glm="claude --settings ~/.claude/glm-settings.json"
```

Or for `glm5`:

```bash
alias glm5="claude --settings ~/.claude/glm-settings.json"
```

![](./images/Pasted%20image%2020260310232746.png)

Open a fresh Terminal and run:

```bash
source .zshrc
```

![](./images/Pasted%20image%2020260310233106.png)

![](./images/Pasted%20image%2020260310233154.png)

Now type `glm` (or `glm5`) and boom — Claude Code launches with GLM.

![](./images/Pasted%20image%2020260310233233.png)

![](./images/Pasted%20image%2020260310233250.png)

---

## Conclusion

1. **Get API Key** from [bigmodel.cn](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)
2. **Choose**: Free tier (GLM-4.7) or subscribe (GLM-5)
3. **Setup**: Use visual app (`glm` command) or official script (`claude` command)
4. **Verify**: Run `/model` in Claude Code
5. **Done!** Start coding with your new AI pair programmer

---

*Questions? Stuck somewhere? The GLM community is pretty helpful. Or just ask Claude — it's literally right there.*

### 📖 GLM Coding Plan subscription details

Click **My Plan** to open the subscription page.

![](./images/Pasted%20image%2020260306112528.png)

Click **GLM Coding plan** to see your options.

![](./images/Pasted%20image%2020260306112619.png)

Subscribe here. Without subscription, you get free quota but **no GLM-5**.

![](./images/Pasted%20image%2020260306112719.png)
