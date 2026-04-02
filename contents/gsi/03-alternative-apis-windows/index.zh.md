---
title: 将 Claude Code 接到 GLM / KIMI 等备选 API（Windows 版）
draft: false
prev: gsi/02-claude-code-vscode
---
# 将 Claude Code 接到 GLM / KIMI 等备选 API（Windows 版）

## 为什么要给客户端接 GLM / KIMI 备选线路？

装好编程助手客户端之后，很多人会碰到同一件事：想长期稳定用下去，往往离不开官方模型的订阅或按量计费；而不同地区、不同团队对「哪条路更顺手」也不尽相同。若你在官方默认线路之外，还想多接一条兼容的推理服务，智谱 GLM、月之暗面 Kimi 等厂商提供了与常见客户端约定相近的接口，同一套界面可以指向另一套后端，换线路时不必从零换工具。

### 先搞清楚一件事：客户端 ≠ 模型

可以粗略理解成两层：一层是在本机替你改文件、跑命令的「执行端」；另一层是在云端理解你的话、决定改哪些内容的「推理服务」。执行端不会凭空知道该写什么，必须把提示发给某个推理服务并得到回复；只要把服务地址和密钥配对正确，执行端可以连着不同的推理服务使用。因此承担思考角色的可以是官方模型，也可以换成智谱或月之暗面等兼容线路，视你的配置而定。

![](images/01-GLM-configuration-20260316125916.jpg)

### 为什么选 GLM 和 KIMI？

选哪一家模型，往往会碰到延迟、价格、服务条款等现实因素，很难一句话定对错。从公开资料与社区实践看，不少中国大模型在「能力够用」与「账单压力」之间往往比较均衡，日常写代码、改文档的场景里也有不少可参考的案例。

### GLM 和 KIMI 实力如何？

在一份对外公开的、偏复杂决策场景的第三方评测里（详见 [Vending-Bench 2](https://andonlabs.com/evals/vending-bench-2)），智谱与月之暗面旗下多款模型曾处于开源梯队靠前位置。榜单会随时间与题型变化，这里只作参考：**是否真的适合你的工作，还请自己尝试一下。**

![](images/01-GLM-configuration-20260316120220.jpg)
### AI 工作流长这样

```
你提需求 → 大脑思考 → 手写代码 → 搞定
```

流程本身不随平台而变：配置好密钥与服务地址后，客户端仍按同样方式驱动本地文件与终端。

已有稳定官方账号的读者可将本文当作选读；需要跟练配置示例的读者可直接进入下文「GLM 配置教程」「KIMI 配置教程」。

---


## GLM 配置教程
### 步骤一：获取你的「入场券」

一切从一个 API Key 开始。获取方式如下：

打开 [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)

![](images/01-GLM-configuration-20260303185459.jpg)

点击 **Create a new API Key**。

![](images/Pasted%20image%2020260401172104.png)

起个能记住的名字（比如「AITraining」，未来的你会感谢现在的你），然后点击 **Yes**。

![](images/Pasted%20image%2020260401172158.png)

点击 **Copy**，找个安全的地方存起来。

![](images/Pasted%20image%2020260401172252.png)

---

### 步骤二：订阅还是不订阅？这是个问题

不办付费套餐时，仍有一定免费额度与偏基础的模型档，足以先摸清自己的用量。若你每天大量使用、需要更高限额或旗舰档模型，可考虑 **GLM Coding Plan**。

在控制台点击 **My Plan** 打开「My plan」。

![](images/01-GLM-configuration-20260306112528.jpg)

然后点击 **GLM Coding plan** 打开订阅界面。

![](images/01-GLM-configuration-20260306112619.jpg)

滑动到下方订阅区域，按需选择套餐。

![697](images/01-GLM-configuration-20260316113743.jpg)

---

### 步骤三：实际配置

打开 `C:\Users\你的用户名\.claude`（将「你的用户名」换成当前 Windows 登录名），编辑或新建 **settings.json**。

![](images/Pasted%20image%2020260331132037.png)

将下面示例中的 `your_zhipu_api_key` 换成上一步复制的 Key，整段合并进 `settings.json` 后保存（若文件里已有其他键，请手工合并 `env` 字段，避免覆盖其他无关配置）。

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

在 **PowerShell** 或终端中执行 `claude`，应能启动已指向智谱后端的客户端。

![](images/Pasted%20image%2020260331132529.png)


#### GLM-5 解锁教程（仅订阅用户）

若已订阅 GLM Coding Plan，可将 `settings.json` 中的 `env` 替换为下列结构（同样替换 `your_zhipu_api_key`），使默认模型指向 GLM-5；具体字段名以智谱当前文档为准。


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

#### 进阶：创建 `glm` 命令

若希望输入 `glm` 即加载专用配置，可将当前的 `settings.json` 复制一份为 **glm-settings.json**（仍放在同一 `.claude` 目录下）。

![](images/Pasted%20image%2020260331132855.png)

打开 **PowerShell**，执行下面两行以创建或打开 PowerShell 配置文件：

```
New-Item -Path $PROFILE -ItemType File -Force
notepad $PROFILE
```

![](images/Pasted%20image%2020260331133422.png)

在记事本末尾保存如下函数定义后关闭（路径中的 `$HOME` 在 PowerShell 中指向用户主目录）：

```
function glm {  
claude --settings $HOME/.claude/glm-settings.json $args  
}
```

![](images/Pasted%20image%2020260331133138.png)

回到 PowerShell，执行 `. $PROFILE` 使配置立即生效。

![](images/Pasted%20image%2020260331133254.png)

此后在新开的 PowerShell 中输入 `glm` 即可按 `glm-settings.json` 启动客户端。

![](images/Pasted%20image%2020260331133548.png)

---

## KIMI 配置教程


### 步骤一：获取你的「入场券」

一切从一个 API Key 开始。获取方式如下：

打开 [https://platform.kimi.ai/console/api-keys](https://platform.kimi.ai/console/api-keys) 并登录。

![](images/Pasted%20image%2020260401132502.png)

点击 **Create API Key**。

![](images/Pasted%20image%2020260401184807.png)

起个能记住的名字，项目选择 **default**，然后点击 **确定**。

![](images/Pasted%20image%2020260401132653.png)

点击下图所示的复制按钮复制你的 API Key，找个安全的地方存起来。

**重要提示**：这是你唯一一次能看到它的机会！

![](images/Pasted%20image%2020260401132817.png)

---

### 步骤二：给账户充点「燃料」

**KIMI 的 API Key 需要账户有余额才能用；余额不足时调用会失败。** 在控制台依次打开 **Billing**、**Recharge**，选择金额并完成支付即可。

![](images/Pasted%20image%2020260402102755.png)

---

### 步骤三：实际配置


打开 `C:\Users\你的用户名\.claude`，编辑 **settings.json**（用户名请替换为实际登录名）。

![](images/Pasted%20image%2020260331132037.png)

将 `your_kimi_api_key` 换成上一步复制的 Key，并写入下列 JSON。注意 `hasCompletedOnboarding` 与 `env` 同级，不要写进 `env` 对象内部，否则可能无法被客户端正确识别。

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

在 PowerShell 中执行 `claude` 启动客户端，按界面提示确认使用环境中的自定义密钥即可。

![](images/Pasted%20image%2020260331132529.png)

---

### 进阶：创建 `kimi` 命令

将当前用于 KIMI 的 `settings.json` 另存为 **kimi-settings.json**，与 GLM 做法相同，便于多条线路并存。

![](images/Pasted%20image%2020260331134051.png)

在 PowerShell 中执行：

```
New-Item -Path $PROFILE -ItemType File -Force
notepad $PROFILE
```

![](images/Pasted%20image%2020260331133422.png)

在配置文件中追加：

```
function kimi {  
claude --settings $HOME/.claude/kimi-settings.json $args  
}
```

![](images/Pasted%20image%2020260331134214.png)

执行 `. $PROFILE` 加载配置。

![](images/Pasted%20image%2020260331133254.png)

之后在 PowerShell 输入 `kimi` 即可启动指向月之暗面线路的客户端。

![](images/Pasted%20image%2020260331134300.png)
