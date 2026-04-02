---
title: Point Claude Code at GLM / KIMI and other alternate APIs (Windows)
draft: false
prev: gsi/02-claude-code-vscode
---
# Point Claude Code at GLM / KIMI and other alternate APIs (Windows)

## Why wire the client to GLM / KIMI?

After you install the coding-assistant client, a familiar pattern appears: staying on it long term usually means an official subscription or usage-based billing, and different regions or teams will find different routes more convenient. If you want a **second** inference backend that speaks the same client protocol as the usual defaults, vendors such as Zhipu (GLM) and Moonshot (Kimi) offer compatible endpoints, you keep the same UI and point it at another service without swapping your whole toolchain.

### Client ≠ model

Think in two layers: a **local execution** side that edits files and runs commands, and a **remote inference** service that understands your words and decides what to change. The execution side does not invent patches on its own, it must send prompts to an inference service and get answers back. Point the URL and credentials at the right service and the same client can use different backends. The “thinking” role can be the official model, GLM, KIMI, or another compatible route, depending on how you configure it.

![](images/01-GLM-configuration-20260316125916.jpg)

### Why GLM and KIMI?

Choosing a vendor is messy in practice: latency, pricing, and terms all matter, and there is no single “right” answer. From public write-ups and community practice, many Chinese LLMs sit in a workable band between capability and cost, with plenty of examples for everyday coding and documentation.

### How capable are they?

In one public, decision-heavy third-party benchmark ([Vending-Bench 2](https://andonlabs.com/evals/vending-bench-2)), several GLM and Moonshot models ranked strongly in the open-weight cohort. Leaderboards shift with time and task shape, treat this as background only: **whether it truly fits your work is something you’ll have to try for yourself.**

![](images/01-GLM-configuration-20260316120220.jpg)
### What the workflow looks like

```
You ask → model thinks → writes code → done
```

The flow is the same on every OS: after keys and service URL are set, the client still drives local files and the terminal the same way.

If you already rely on an official account, treat this page as optional; if you want to follow the walkthrough, jump to **GLM setup** and **KIMI setup** below.

---


## GLM setup
### Step 1: Get your API key

Everything starts with an API key.

Open [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)

![](images/01-GLM-configuration-20260303185459.jpg)

Click **Create a new API Key**.

![](images/Pasted%20image%2020260401172104.png)

Pick a memorable name (e.g. **AITraining**, your future self will thank you), then **Yes**.

![](images/Pasted%20image%2020260401172158.png)

Click **Copy** and store it somewhere safe. 

![](images/Pasted%20image%2020260401172252.png)

---

### Step 2: Subscribe or not?

Without a paid plan you still get free quota and a more basic model tier—enough to learn your usage. If you use it heavily every day and need higher limits or flagship models, consider the **GLM Coding Plan**.

In the console, click **My Plan** to open “My plan”.

![](images/01-GLM-configuration-20260306112528.jpg)

Then click **GLM Coding plan** to open the subscription screen.

![](images/01-GLM-configuration-20260306112619.jpg)

Scroll down to the plans and pick what fits.

![697](images/01-GLM-configuration-20260316113743.jpg)

---

### Step 3: Apply configuration

Open `C:\Users\<YourUsername>\.claude` (replace with your Windows user name), then edit or create **settings.json**.

![](images/Pasted%20image%2020260331132037.png)

Replace `your_zhipu_api_key` with your key, merge the JSON into `settings.json`, and save (if other keys exist, merge the `env` block carefully, do not wipe unrelated settings).

```
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "your_zhipu_api_key",
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
  }
}
```

![](images/Pasted%20image%2020260331132401.png)

In **PowerShell** or another terminal run `claude`; the client should start against the Zhipu backend.

![](images/Pasted%20image%2020260331132529.png)


#### Enabling GLM-5 (subscribers only)

If you subscribe to GLM Coding Plan, replace `env` in `settings.json` with the structure below (same key placeholder). That points default models at GLM-5; field names should match Zhipu’s current docs.

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "your_zhipu_api_key",
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
    "ANTHROPIC_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5"
  },
  "hasCompletedOnboarding": true
}
```

![](images/Pasted%20image%2020260331132753.png)

---

#### Advanced: `glm` command

To type `glm` and load a dedicated profile, copy `settings.json` to **glm-settings.json** in the same `.claude` folder.

![](images/Pasted%20image%2020260331132855.png)

In **PowerShell** run:

```
New-Item -Path $PROFILE -ItemType File -Force
notepad $PROFILE
```

![](images/Pasted%20image%2020260331133422.png)

Append this function (`$HOME` is your user profile in PowerShell):

```
function glm {  
claude --settings $HOME/.claude/glm-settings.json $args  
}
```

![](images/Pasted%20image%2020260331133138.png)

Back in PowerShell run `. $PROFILE` to load it.

![](images/Pasted%20image%2020260331133254.png)

In new PowerShell windows, `glm` starts the client with `glm-settings.json`.

![](images/Pasted%20image%2020260331133548.png)

---

## KIMI setup


### Step 1: Get your API key

Everything starts with an API key.

Open [https://platform.kimi.ai/console/api-keys](https://platform.kimi.ai/console/api-keys) and sign in.

![](images/Pasted%20image%2020260401132502.png)

Click **Create API Key**.

![](images/Pasted%20image%2020260401184816.png)

Choose a memorable name, select project **default**, then **OK**.

![](images/Pasted%20image%2020260401132653.png)

Use the copy button shown below to copy your API key and store it somewhere safe. 

**Important:** this is often the only time you see the full secret.

![](images/Pasted%20image%2020260401132817.png)

---

### Step 2: Top up balance

**A KIMI API key only works when the account has balance; calls fail if it is empty.** In the console open **Billing**, then **Recharge**, choose an amount, and complete payment.

![](images/Pasted%20image%2020260402102755.png)

---

### Step 3: Apply configuration


Open `C:\Users\<YourUsername>\.claude` and edit **settings.json** (use your real user name).

![](images/Pasted%20image%2020260331132037.png)

Replace `your_kimi_api_key` with your key. Keep `hasCompletedOnboarding` **sibling** to `env`, not inside `env`, or the client may ignore it.

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "your_kimi_api_key",
    "ANTHROPIC_BASE_URL": "https://api.moonshot.cn/anthropic/"
  },
  "hasCompletedOnboarding": true
}
```

![](images/Pasted%20image%2020260331134003.png)

Run `claude` in PowerShell and confirm you want to use the custom key from the environment when prompted.

![](images/Pasted%20image%2020260331132529.png)

---

### Advanced: `kimi` command

Save your KIMI `settings.json` as **kimi-settings.json** beside it, the same pattern as GLM for multiple routes.

![](images/Pasted%20image%2020260331134051.png)

In PowerShell:

```
New-Item -Path $PROFILE -ItemType File -Force
notepad $PROFILE
```

![](images/Pasted%20image%2020260331133422.png)

Append:

```
function kimi {  
claude --settings $HOME/.claude/kimi-settings.json $args  
}
```

![](images/Pasted%20image%2020260331134214.png)

Run `. $PROFILE` to load.

![](images/Pasted%20image%2020260331133254.png)

Then `kimi` starts the client on the Moonshot profile.

![](images/Pasted%20image%2020260331134300.png)
