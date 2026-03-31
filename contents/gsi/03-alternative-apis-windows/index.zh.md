---
title: 将 Claude Code 接到 GLM / KIMI 等备选 API（Windows 版）
draft: false
prev: gsi/02-claude-code-vscode
---
# 将 Claude Code 接到 GLM / KIMI 等备选 API（Windows 版）

## 为什么要给客户端接 GLM / KIMI 备选线路？

不少人在装好编程助手客户端之后才发现，要稳定使用往往离不开官方模型的订阅或按量账单，对支付方式和账号环境也有一定要求。若你暂时不便走官方主路径，或希望多一条国内可用的「模型后端」，智谱与月之暗面等厂商提供了与官方客户端约定相近的接口，可以把同一套界面接到另一套推理服务上，降低上手门槛。

### 先搞清楚一件事：客户端 ≠ 模型

可以粗略理解成两层：一层是在本机替你改文件、跑命令的「执行端」；另一层是在云端理解你的话、决定改哪些内容的「推理服务」。执行端不会凭空知道该写什么，必须把句子发给某个推理服务并得到回复；只要把服务地址和密钥配对正确，执行端可以连着不同的推理服务使用。因此承担思考角色的可以是官方模型，也可以换成智谱或月之暗面等兼容线路，视你的配置而定。

![](images/01-GLM-configuration-20260316125916.jpg)

### 为什么选 GLM 和 KIMI？

在支付与账号环境上，对不少国内用户相对省心：常见银行卡或国内支付链路往往就能完成充值，不必反复折腾海外卡。若你担心高频调用触发平台风控，各家国内服务商的合规与限额规则以官方说明为准，与直接使用海外主站不是同一套体系。至于能力是否够用，公开排行榜里智谱、月之暗面的多款模型时常出现在靠前区间，日常写代码、改文档多数场景可以胜任，但仍建议用你自己的真实任务试几轮再下结论。

若你已有稳定的官方订阅，可继续沿用原线路；若没有或想并行试用，可把智谱与月之暗面当作可选的备用线路。

### GLM 和 KIMI 实力如何？

在一份对外公开的、偏复杂决策场景的第三方评测里（详见 [Vending-Bench 2](https://andonlabs.com/evals/vending-bench-2)），智谱与月之暗面旗下多款模型曾处于开源梯队靠前位置。排行会随时间与任务类型变化，是否满足你的工作仍建议亲自试跑后再定。

![](images/01-GLM-configuration-20260316120220.jpg)
### AI 工作流长这样

```
你提需求 → 大脑思考 → 手写代码 → 搞定
```

流程本身不随平台而变：配置好密钥与服务地址后，客户端仍按同样方式驱动本地文件与终端。

---

已有稳定官方账号的读者可将本文当作选读；需要配置智谱或月之暗面线路的读者可直接进入下文对应章节。

---


## GLM 配置教程
### 步骤一：获取你的「入场券」

一切从一个 API Key 开始。获取方式如下：

打开 [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)

![](images/01-GLM-configuration-20260303185459.jpg)

点击 **Create a new API Key**。

![](images/01-GLM-configuration-20260303185651.jpg)

起个能记住的名字（例如 `claude-code-key`），然后点击 **Yes**。

![](images/01-GLM-configuration-20260303185744.jpg)

点击 **Copy**，将密钥保存到安全位置。**重要提示**：这是你唯一一次能完整查看该密钥的机会。

![](images/01-GLM-configuration-20260303185954.jpg)

---

### 步骤二：订阅还是不订阅？这是个问题

不办付费套餐时，通常仍有一定免费额度，并可用到偏基础档的模型版本，适合先摸清自己的调用量。若你每天大量使用、需要更高配额或更新的旗舰档模型，可以再考虑官方的 **GLM Coding Plan** 付费方案。建议先用免费额度判断用量，再决定是否升级；订阅界面说明见下文「GLM Coding Plan 订阅详情」。

---

### 步骤三：实际配置

打开 `C:\Users\你的用户名\.claude`（将「你的用户名」换成当前 Windows 登录名），编辑或新建 **settings.json**。

![](images/Pasted%20image%2020260331132037.png)

将下面示例中的 `your_zhipu_api_key` 换成上一步复制的 Key，整段合并进 `settings.json` 后保存（若文件里已有其他键，请手工合并 `env` 字段，避免覆盖 unrelated 配置）。

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

在 **PowerShell** 或终端中执行 `claude`，应能启动已指向智谱后端的客户端（若命令未找到，请确认安装路径已加入 `PATH`）。

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

### 进阶：创建 `glm` 命令

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

### GLM Coding Plan 订阅详情

点击 **My Plan** 进入「我的套餐」。

![](images/01-GLM-configuration-20260306112528.jpg)

点击 **GLM Coding plan** 进入订阅界面。

![](images/01-GLM-configuration-20260306112619.jpg)

滑动到下方订阅界面，可看到不同的选项，可根据实际的需求进行选择。

![697](images/01-GLM-configuration-20260316113743.jpg)

## KIMI 配置教程


### 步骤一：获取你的「入场券」

一切从一个 API Key 开始。获取方式如下：

打开 [https://platform.moonshot.cn/console/api-keys](https://platform.moonshot.cn/console/api-keys) 并登录。

![](images/02-KIMI-configuration-20260303194555.jpg)

点击 **新建 API Key**。

![](images/02-KIMI-configuration-20260303194920.jpg)

起个能记住的名字，项目选择 **default**，然后点击 **确定**。

![](images/02-KIMI-configuration-20260303195050.jpg)

点击 **复制**，将密钥保存到安全位置。**重要提示**：这是你唯一一次能完整查看该密钥的机会。

![](images/02-KIMI-configuration-20260303195345.jpg)

---

### 步骤二：给账户充点「燃料」

KIMI 的 API Key 需要账户有足够余额才能调用。在控制台依次打开 **财务管理**、**账户充值**，选择金额并完成支付即可。

![](images/02-KIMI-configuration-20260306114112.jpg)

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
