---
permalink: /contents/Agents/01-GLM-configuration/zh/
lang: zh


layout: doc
title: GLM 配置教程
---

> **阅前说明**
>
> 本教程假设你知道怎么打开终端、运行基本命令。如果听起来有点慌，先花5分钟看看 [Terminal 基础](../../../Basic-tools/01-terminal-basics/zh)，绝对物超所值。


# GLM 配置教程

## 大局观：为什么在 Claude Code 里用 GLM？

**想象一下这样的场景：**

你下载了 Claude Code，兴奋地准备让 AI 帮你写代码。结果打开后发现——需要 Claude API 才能用。去官网一看，订阅要国际信用卡，还得担心账号风控。一盆冷水浇下来，热情瞬间凉了半截。

**别慌，这正是 GLM 登场的时候。**

### 先搞清楚一件事：Claude Code ≠ Claude

这里有个关键概念：

**Claude Code 是「手」，Claude/GLM 是「大脑」。**

| 角色 | 代表 | 干什么 |
|------|------|--------|
| **大脑** | Claude、GLM | 理解你、思考方案、做决策 |
| **手** | Claude Code | 写代码、改文件、跑命令 |

Claude Code 这双「手」很灵活，但它**不会自己思考**。它需要一个「大脑」告诉它该干什么。

**重点来了：这个大脑，可以是 Claude，也可以是 GLM。**

![](images/Pasted%20image%2020260316125916.png)

### 为什么选 GLM？

三个字：**省心、省力、省钱**。

| 你的困扰 | Claude 方案 | GLM 方案 |
|----------|-------------|----------|
| 没国际信用卡 | 订阅困难 | 多种支付方式直接充 |
| 担心封号 | 高频调用有风险 | 中国服务商，稳得很 |
| 性能够不够用 | 顶级 | 开源第一，日常开发绰绰有余 |

**一句话总结：** 没有 Claude 账号？GLM 就是很能打的 Plan B。

### GLM 实力如何？

GLM-5 在 [Vending-Bench 2](https://andonlabs.com/evals/vending-bench-2) 复杂决策能力测试中（2026年3月），**开源模型排名第一**。GLM-4.7 紧随其后排第二。

![](images/Pasted%20image%2020260316120220.png)

即使和顶尖闭源模型比，GLM-5 也拿到了全球第6——仅次于 Claude、GPT、Gemini、Grok 这些巨头。作为「大脑」，智能完全在线。

![](images/Pasted%20image%2020260316120041.png)

### AI 工作流长这样

```
你提需求 → 大脑思考 → 手写代码 → 搞定
```

就是这么简单。

---

**快速决策：**
- ✅ 已有稳定 Claude 账号 → 继续用，本篇选读
- ✅ 没有 Claude / 想试试 GLM → 往下看，开始配置

![](./images/Pasted%20image%2020260310154428.png)

---

## 步骤一：获取你的「入场券」

一切从一个 API Key 开始。获取方式如下：

🔗 打开 [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)

![](./images/Pasted%20image%2020260303185459.png)

点击 **Create a new API Key**。

![](./images/Pasted%20image%2020260303185651.png)

起个能记住的名字（比如「claude-code-key」——未来的你会感谢现在的你），然后点击 **Yes**。

![](./images/Pasted%20image%2020260303185744.png)

点击 **Copy**，找个安全的地方存起来。**重要提示**：这是你唯一一次能看到它的机会！

![](./images/Pasted%20image%2020260303185954.png)

---

## 步骤二：订阅还是不订阅？这是个问题

| 选项 | 你能得到什么 | 适合谁 |
|------|--------------|--------|
| **不订阅** | 免费额度 + GLM-4.7 | 轻度用户、尝鲜党 |
| **GLM Coding Plan** | GLM-5 + 更高额度 | 重度用户、天天用 |

**我的建议**：先用免费版试试水，不够用了再升级。别有压力。[点这里订阅](#-glm-coding-plan-订阅详情)

---

## 步骤三：实际配置（选择你的路线）

你有两条路可以选，按你的需求来决定：

| 方法 | 优点 | 缺点 |
|------|------|------|
| **可视化配置工具**（推荐） | 方便切换服务商，易用 | 多一步配置 |
| **官方脚本** | 一条命令搞定 | 后续切换服务商较麻烦 |

### 方法一：可视化配置工具（推荐 ✨）

**为什么推荐这一种**：后续可以在 GLM 和其他服务商之间自由切换，灵活性最高。

找个文件夹，右键 → **Terminal**。

![](images/Pasted%20image%2020260311005958.png)

复制这段「魔法咒语」到终端，按下 Enter：

```
wget "https://cm.maku.press/editor4/agent_manager/-/archive/main/agent_manager-main.zip?ref_type=heads" -O agent_manager-main.zip && \
unzip agent_manager-main.zip && \
cd agent_manager-main && \
chmod +x install.sh && \
./install.sh
```

![](images/Pasted%20image%2020260311010117.png)

安装完成后，找到 **AGENT_MANAGER.command** 文件，双击运行。

![](./images/Pasted%20image%2020260306111847.png)

关键时刻到了：
1. 粘贴你的 API Key
2. 选择模型
3. 点击 **Install & configure**

⚠️ **重要警告**：没订阅千万别选 `glm-5`！选了会出问题，到时候别说我没提醒你。

![](./images/Pasted%20image%2020260306113120.png)

成功长这样：

![](./images/Pasted%20image%2020260306113321.png)

现在终端输入 `glm` 就能用 GLM 启动 Claude Code 了。搞定。

![](./images/Pasted%20image%2020260303152714.png)

**验证一下**：重启 Claude Code，输入 `/model`。应该能看到 **GLM-5**。

![](./images/Pasted%20image%2020260303193201.png)

![](./images/Pasted%20image%2020260303193234.png)

💡 **小贴士**：GLM-5 相当于 Claude Opus，强但费额度。复杂任务用它，日常任务用 GLM-4.7 省着点。另外高峰期（14:00-18:00 北京时间）可能会慢。

直接问也行：

![](./images/Pasted%20image%2020260310101707.png)

---

### 方法二：官方一键脚本

**取舍**：配置更快，但后续切换服务商较麻烦。确定只用 GLM 可以选这个。

按 `Option + Space` → 输入 **Terminal** → 回车。

![](./images/Pasted%20image%2020260303190946.png)

复制运行：

```sh
curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh
```

> **命令解释**：
> - `curl -O`：从网上下载文件
> - `bash`：执行下载的脚本

![](./images/Pasted%20image%2020260303191656.png)

提示时粘贴 API Key，按回车。

⚠️ **注意**：粘贴时终端可能什么都不显示，这是正常的，别重复粘贴。

![](./images/Pasted%20image%2020260303191343.png)

终端恢复可输入状态就完成了。输入 `claude` 启动。

![](./images/Pasted%20image%2020260303191816.png)

![](./images/Pasted%20image%2020260303191919.png)

---

### GLM-5 解锁教程（仅订阅用户 🔓）

如果你已经订阅了 GLM Coding Plan，可以按下面步骤解锁「大杀器」：

**访达** → **前往** → **个人**

![](./images/Pasted%20image%2020260303192106.png)

按 `Command + Shift + .` 显示隐藏文件，打开 **.claude** 文件夹。

![](./images/Pasted%20image%2020260303192303.png)

用你喜欢的编辑器打开 **settings.json**。

![](./images/Pasted%20image%2020260303192828.png)

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

⚠️ 把 `"your api key"` 换成你真正的 API Key！

保存，重启 Claude Code，运行 `/model` 验证。

![](./images/Pasted%20image%2020260303192957.png)

---

### 进阶：创建 `glm` 和 `glm5` 命令

想用 `glm` 或 `glm5` 命令快速启动？操作如下：

复制 **settings.json** → 重命名为 **glm-settings.json**。

![](./images/Pasted%20image%2020260310232459.png)

返回 Home 目录，打开 **.zshrc**。

![](./images/Pasted%20image%2020260310234055.png)

在文件末尾添加：

```bash
alias glm="claude --settings ~/.claude/glm-settings.json"
```

或者用 `glm5`：

```bash
alias glm5="claude --settings ~/.claude/glm-settings.json"
```

![](./images/Pasted%20image%2020260310232746.png)

打开新终端，运行：

```bash
source .zshrc
```

![](./images/Pasted%20image%2020260310233106.png)

![](./images/Pasted%20image%2020260310233154.png)

现在输入 `glm`（或 `glm5`）就能用 GLM 启动 Claude Code 了。

![](./images/Pasted%20image%2020260310233233.png)

![](./images/Pasted%20image%2020260310233250.png)

---

## 总结

1. **获取 API Key**：去 [bigmodel.cn](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)
2. **选择**：免费版（GLM-4.7）或订阅（GLM-5）
3. **配置**：可视化工具（`glm` 命令）或官方脚本（`claude` 命令）
4. **验证**：在 Claude Code 里运行 `/model`
5. **完成！** 开始和你的 AI 结对编程吧

---

*有问题？卡住了？GLM 社区挺活跃的。或者直接问 Claude —— 它就在那。*

### 📖 GLM Coding Plan 订阅详情

点击 **My Plan** 进入「我的套餐」。

![](./images/Pasted%20image%2020260306112528.png)

点击 **GLM Coding plan** 进入订阅界面。

![](./images/Pasted%20image%2020260306112619.png)

滑动到下方订阅界面，可看到不同的选项，可根据实际的需求进行选择。

![](images/Pasted%20image%2020260316113743.png)
