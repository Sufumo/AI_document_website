---
title: Point Claude Code at GLM / KIMI and other alternate APIs (macOS)
draft: false
prev: gsi/02-claude-code-vscode
---
# Point Claude Code at GLM / KIMI and other alternate APIs (macOS)

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

After keys and endpoints are set, the flow matches using the default official backend.

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

Click **Copy** and store it somewhere safe. **Important:** this is often the only time you see the full secret.

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

Two styles: a **visual config tool** writes multiple profiles so switching between GLM and other backends is easier (extra install step), or Zhipu’s **one-line installer script** is faster the first time but more annoying when you change vendors later. If you expect to swap models or providers, prefer the tool.

#### Method A: visual config tool

Best when you want several backends side by side on one Mac, separate on-disk profiles and different launch commands.

In any folder, right-click → **Terminal**.

![](images/Pasted%20image%2020260401172458.png)

Paste the whole block into the terminal and press **Enter** (needs `wget` / `unzip`; install via Homebrew if missing):

```
wget "https://cm.maku.press/editor4/agent_manager/-/archive/main/agent_manager-main.zip?ref_type=heads" -O agent_manager-main.zip && \
unzip agent_manager-main.zip && \
cd agent_manager-main && \
chmod +x install.sh && \
./install.sh
```

![](images/01-GLM-configuration-20260311010117.jpg)

When done, find **AGENT_MANAGER.command** and double-click it.

![](images/01-GLM-configuration-20260306111847.jpg)

Paste your API key, pick a model, then **Install & configure**.

> [!WARNING]
>
> If you are **not** subscribed, do **not** pick `glm-5`, that can break things. You have been warned.

![](images/01-GLM-configuration-20260306113120.jpg)

Success looks like this:

![](images/01-GLM-configuration-20260306113321.jpg)

In Terminal run `glm` to start the client with the current GLM profile.

![](images/01-GLM-configuration-20260303152714.jpg)

Restart the client, run `/model`, and you should see the configured model (whether **GLM-5** appears depends on subscription and selection).

![](images/01-GLM-configuration-20260303193201.jpg)

![](images/01-GLM-configuration-20260303193234.jpg)

> [!TIP]
>
> GLM-5 is stronger and often burns quota faster, good for hard tasks; lighter work can stay on GLM-4.7 to save cost. Queues or latency on weekday afternoons are common.

You can also ask in chat which model is active:

![](images/01-GLM-configuration-20260310101707.jpg)

---

#### Method B: official one-line script

If you expect to use only GLM for a long stretch, the official script writes the environment in one go; switching to another API later usually means editing env vars or config by hand.

`Option + Space` → type **Terminal** → Enter.

![](images/01-GLM-configuration-20260303190946.jpg)

Copy and run:

```sh
curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh
```

This downloads the installer with `curl -O` and runs it with `bash`, same idea as Zhipu’s docs.

![](images/01-GLM-configuration-20260303191656.jpg)

When prompted, paste the API key and press Enter.

> [!NOTE]
>
> The terminal may show nothing while pasting, that is normal. Do not paste twice.

![](images/01-GLM-configuration-20260303191343.jpg)

When you get a prompt again, installation is done. Run `claude` to start.

![](images/01-GLM-configuration-20260303191816.jpg)

![](images/01-GLM-configuration-20260303191919.jpg)

---

##### Enabling GLM-5 (subscribers only)

If you subscribe to GLM Coding Plan, follow these steps to point config at GLM-5-tier models (exact names depend on what the console lists):

**Finder** → **Go** → **Home**

![](images/01-GLM-configuration-20260303192106.jpg)

Press `Command + Shift + .` to show hidden items, open **.claude**.

![](images/01-GLM-configuration-20260303192303.jpg)

Open **settings.json** in your editor.

![](images/01-GLM-configuration-20260303192828.jpg)

**Default example:**

```json
{
  "env": {
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "GLM-4.7",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "GLM-4.7",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "GLM-4.5-Air"
  }
}
```

**To prefer GLM-5 everywhere**, replace with:

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

> [!WARNING]
>
> Replace `"your api key"` with your real API key.

Save, restart the client, run `/model` to verify.

![](images/01-GLM-configuration-20260303192957.jpg)

---

##### Advanced: `glm` and `glm5` commands

To always launch with a dedicated GLM settings file, copy the profile and add shell aliases.

Copy **settings.json** → rename to **glm-settings.json**.

![](images/Pasted%20image%2020260401153046.png)

Go to your home folder, open **.zshrc**.

![](images/Pasted%20image%2020260401152926.png)

Append:

```bash
alias glm="claude --settings ~/.claude/glm-settings.json"
```

Or `glm5`:

```bash
alias glm5="claude --settings ~/.claude/glm-settings.json"
```

![](images/01-GLM-configuration-20260310232746.jpg)

Open a new terminal:

```bash
source .zshrc
```

![](images/01-GLM-configuration-20260310233106.jpg)

![](images/01-GLM-configuration-20260310233154.jpg)

Now `glm` (or `glm5`) starts the client on the GLM profile.

![](images/01-GLM-configuration-20260310233233.jpg)

![](images/01-GLM-configuration-20260310233250.jpg)

---

### Recap

Get a key from [bigmodel.cn](https://bigmodel.cn/usercenter/proj-mgmt/apikeys), choose free tier vs GLM Coding Plan, then either the visual tool (for `glm`-style commands) or the official script (often `claude`). Confirm the active model with `/model` or by asking in chat.

---

## KIMI setup


### Step 1: Get your API key

Everything starts with an API key.

Open [https://platform.kimi.ai/console/api-keys](https://platform.kimi.ai/console/api-keys) and sign in.

![](images/Pasted%20image%2020260401132502.png)

Click **Create API Key**.

![](images/Pasted%20image%2020260401184707.png)

Choose a memorable name, select project **default**, then **OK**.

![](images/Pasted%20image%2020260401132653.png)

Use the copy button shown below to copy your API key and store it somewhere safe. **Important:** this is often the only time you see the full secret.

![](images/Pasted%20image%2020260401132817.png)

---

### Step 2: Top up balance

**A KIMI API key only works when the account has balance; calls fail if it is empty.** In the console open **Billing**, then **Recharge**, choose an amount, and complete payment.

![](images/Pasted%20image%2020260401132941.png)

---

### Step 3: Apply configuration

Like GLM, KIMI supports the **visual tool** or **hand-written env vars**. The tool suits hopping between backends; env vars suit “Moonshot only for the long term”, quick to set, more edits when you change provider.

#### Method A: visual config tool

Writes multiple local profiles so you can launch different backends without constantly editing `.zshrc`.

In any folder, right-click → **Terminal**.

![](images/Pasted%20image%2020260401152540.png)

Paste the same download/install block and press **Enter**:

```
wget "https://cm.maku.press/editor4/agent_manager/-/archive/main/agent_manager-main.zip?ref_type=heads" -O agent_manager-main.zip && \
unzip agent_manager-main.zip && \
cd agent_manager-main && \
chmod +x install.sh && \
./install.sh
```

![](images/02-KIMI-configuration-20260311010117.jpg)

Double-click **AGENT_MANAGER.command**.

![](images/02-KIMI-configuration-20260306111847.jpg)

Switch to the **KIMI** tab, paste the key, **Install & configure**.

![](images/02-KIMI-configuration-20260306114430.jpg)

Success:

![](images/02-KIMI-configuration-20260306114556.jpg)

Run `kimi` in Terminal for the current KIMI profile.

![](images/02-KIMI-configuration-20260306114634.jpg)

---

#### Method B: environment variables

If you will use only KIMI for a long time, export `ANTHROPIC_BASE_URL` and the key in your shell startup file; when you change vendors, update or comment those lines so you do not hit the wrong backend.

**Finder** → **Go** → **Home**

![](images/02-KIMI-configuration-20260303192106.jpg)

Show hidden files (`Command + Shift + .`), open **.zshrc**.

![](images/02-KIMI-configuration-20260303200006.jpg)

Append, replacing `your API KEY`:

```sh
export ANTHROPIC_BASE_URL="https://api.moonshot.cn/anthropic/"
export ANTHROPIC_API_KEY="your API KEY"
```

![](images/02-KIMI-configuration-20260303200243.jpg)

Save. `Option + Space` → **Terminal** → Enter.

![](images/02-KIMI-configuration-20260303190946.jpg)

Run `source .zshrc` to load variables.

![](images/02-KIMI-configuration-20260303200438.jpg)

Run `claude`; when you see **Detected a custom API Key in your environment**, click **Yes**.

![](images/02-KIMI-configuration-20260303200736.jpg)

You can then use the Kimi model normally.

![](images/02-KIMI-configuration-20260303200846.jpg)

---

#### Advanced: `kimi` launch command

To avoid global env vars, use a dedicated `kimi-settings.json` and `alias kimi='claude --settings …'` in `.zshrc`.

**Finder** → **Go** → **Home**

![](images/02-KIMI-configuration-20260303192106.jpg)

Show hidden items, open **.claude**.

![](images/02-KIMI-configuration-20260303192303.jpg)

Copy **settings.json** → **kimi-settings.json**.

![](images/Pasted%20image%2020260401152835.png)

Edit **kimi-settings.json** (replace `replace with your api key`):

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.moonshot.cn/anthropic/",
    "ANTHROPIC_AUTH_TOKEN": "replace with your api key"
  },
  "hasCompletedOnboarding": true
}
```

![](images/02-KIMI-configuration-20260310234351.jpg)

Back in home, open **.zshrc**.

![](images/Pasted%20image%2020260401152907.png)

Append:

```bash
alias kimi="claude --settings ~/.claude/kimi-settings.json"
```

![](images/02-KIMI-configuration-20260310233841.jpg)

`Command + Space` → **Terminal** → Enter.

![](images/02-KIMI-configuration-20260113152908876-1.jpg)

Run `source .zshrc`.

![](images/02-KIMI-configuration-20260310233106.jpg)

When the prompt returns, config is loaded.

![](images/02-KIMI-configuration-20260310233154.jpg)

Run `kimi` to start the client.

![](images/02-KIMI-configuration-20260310234456.jpg)

![](images/02-KIMI-configuration-20260310233250.jpg)

---

### Recap

Create a key on [platform.kimi.ai](https://platform.kimi.ai/console/api-keys), keep the account funded, then either the visual installer (`kimi`) or env vars (often `claude`). Confirm in chat that the model name matches the KIMI route you expect.
