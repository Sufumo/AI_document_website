---
title: 将 Claude Code 接到 GLM / KIMI 等备选 API（macOS 版）
draft: false
prev: gsi/02-claude-code-vscode
---
# 将 Claude Code 接到 GLM / KIMI 等备选 API（macOS 版）

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

配置好密钥与接口后，上述流程与使用官方默认后端时一致。

---

已有稳定官方账号的读者可将本文当作选读；需要配置智谱或月之暗面线路的读者可直接进入下文「GLM 配置教程」「KIMI 配置教程」。

---


## GLM 配置教程
### 步骤一：获取你的「入场券」

一切从一个 API Key 开始。获取方式如下：

打开 [https://bigmodel.cn/usercenter/proj-mgmt/apikeys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)

![](images/01-GLM-configuration-20260303185459.jpg)

点击 **Create a new API Key**。

![](images/01-GLM-configuration-20260303185651.jpg)

起个能记住的名字（比如「claude-code-key」——未来的你会感谢现在的你），然后点击 **Yes**。

![](images/01-GLM-configuration-20260303185744.jpg)

点击 **Copy**，找个安全的地方存起来。**重要提示**：这是你唯一一次能看到它的机会！

![](images/01-GLM-configuration-20260303185954.jpg)

---

### 步骤二：订阅还是不订阅？这是个问题

不办付费套餐时，通常仍有一定免费额度，并可用到偏基础档的模型版本，适合先摸清自己的调用量。若你每天大量使用、需要更高配额或更新的旗舰档模型，可以再考虑官方的 **GLM Coding Plan** 付费方案。建议先用免费额度判断用量，再决定是否升级；订阅界面说明见下文「GLM Coding Plan 订阅详情」。

---

### 步骤三：实际配置

配置方式大致可分两类：一类通过可视化工具写入多套配置，日后在智谱与其他后端之间切换较省事，但需要多跑一小段安装流程；另一类使用智谱提供的一键脚本，首次更快，但以后改服务商时往往要多改环境或配置文件。若你预期会换模型或换平台，优先考虑前者。

#### 方法一：可视化配置工具

可视化工具适合需要「多套后端来回试」的场景：同一台 Mac 上可以为 GLM、KIMI 等分别落盘配置，再用不同命令启动。

找个文件夹，右键 → **Terminal**。

![](images/01-GLM-configuration-20260311005958.jpg)

将下面整段命令粘贴到终端后按 **Enter** 执行（需已安装 `wget`/`unzip` 等，若缺失可用 Homebrew 补齐）：

```
wget "https://cm.maku.press/editor4/agent_manager/-/archive/main/agent_manager-main.zip?ref_type=heads" -O agent_manager-main.zip && \
unzip agent_manager-main.zip && \
cd agent_manager-main && \
chmod +x install.sh && \
./install.sh
```

![](images/01-GLM-configuration-20260311010117.jpg)

安装完成后，找到 **AGENT_MANAGER.command** 文件，双击运行。

![](images/01-GLM-configuration-20260306111847.jpg)

在图形界面中粘贴 API Key，选好模型，再点击 **Install & configure** 完成写入。

> [!WARNING]
>
> 没订阅千万别选 `glm-5`！选了会出问题，到时候别说我没提醒你。

![](images/01-GLM-configuration-20260306113120.jpg)

成功长这样：

![](images/01-GLM-configuration-20260306113321.jpg)

之后在终端输入 `glm` 即可按当前 GLM 配置启动客户端。

![](images/01-GLM-configuration-20260303152714.jpg)

重启客户端后输入 `/model`，应能看到与当前配置一致的模型名称（是否出现 **GLM-5** 取决于你是否已订阅并选用该档）。

![](images/01-GLM-configuration-20260303193201.jpg)

![](images/01-GLM-configuration-20260303193234.jpg)

> [!TIP]
>
> GLM-5 能力更强、往往也更耗额度，复杂任务可优先；日常轻量任务可用 GLM-4.7 等档位控制成本。工作日午后时段有时会出现排队或延迟，属常见现象。

也可在对话里直接询问当前所用模型，辅助确认是否切到你期望的后端：

![](images/01-GLM-configuration-20260310101707.jpg)

---

#### 方法二：官方一键脚本

若你确定较长一段时间内只使用 GLM，一条官方脚本即可完成环境写入；若日后要改别家 API，一般需要手动改回环境变量或配置文件。

按 `Option + Space` → 输入 **Terminal** → 回车。

![](images/01-GLM-configuration-20260303190946.jpg)

复制运行：

```sh
curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh
```

上述命令先用 `curl -O` 拉取安装脚本，再交给 `bash` 执行；含义与官方文档保持一致。

![](images/01-GLM-configuration-20260303191656.jpg)

提示时粘贴 API Key，按回车。

> [!NOTE]
>
> 粘贴时终端可能什么都不显示，这是正常的，别重复粘贴。

![](images/01-GLM-configuration-20260303191343.jpg)

终端恢复可输入状态就完成了。输入 `claude` 启动。

![](images/01-GLM-configuration-20260303191816.jpg)

![](images/01-GLM-configuration-20260303191919.jpg)

---

#### GLM-5 解锁教程（仅订阅用户）

若已订阅 GLM Coding Plan，可按下列步骤在配置中启用 GLM-5 等高档模型（具体以控制台当前可用模型名为准）：

**访达** → **前往** → **个人**

![](images/01-GLM-configuration-20260303192106.jpg)

按 `Command + Shift + .` 显示隐藏文件，打开 **.claude** 文件夹。

![](images/01-GLM-configuration-20260303192303.jpg)

用你喜欢的编辑器打开 **settings.json**。

![](images/01-GLM-configuration-20260303192828.jpg)

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

> [!WARNING]
>
> 把 `"your api key"` 换成你真正的 API Key！

保存，重启客户端，运行 `/model` 验证。

![](images/01-GLM-configuration-20260303192957.jpg)

---

### 进阶：创建 `glm` 和 `glm5` 命令

若希望用固定命令（如 `glm` 或 `glm5`）启动带 GLM 配置的会话，可按下面步骤建立专用 `settings` 文件并在 shell 里加别名。

复制 **settings.json** → 重命名为 **glm-settings.json**。

![](images/01-GLM-configuration-20260310232459.jpg)

返回 Home 目录，打开 **.zshrc**。

![](images/01-GLM-configuration-20260310234055.jpg)

在文件末尾添加：

```bash
alias glm="claude --settings ~/.claude/glm-settings.json"
```

或者用 `glm5`：

```bash
alias glm5="claude --settings ~/.claude/glm-settings.json"
```

![](images/01-GLM-configuration-20260310232746.jpg)

打开新终端，运行：

```bash
source .zshrc
```

![](images/01-GLM-configuration-20260310233106.jpg)

![](images/01-GLM-configuration-20260310233154.jpg)

现在输入 `glm`（或 `glm5`）就能用 GLM 线路启动客户端了。

![](images/01-GLM-configuration-20260310233233.jpg)

![](images/01-GLM-configuration-20260310233250.jpg)

---

### 小结

先到 [bigmodel.cn](https://bigmodel.cn/usercenter/proj-mgmt/apikeys) 取得密钥，再按用量在免费档与 GLM Coding Plan 之间做选择；接着用可视化工具（得到 `glm` 等启动方式）或官方脚本（常用 `claude` 启动）写入环境；最后在客户端内用 `/model` 或直接提问确认当前模型是否如预期。

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

点击 **复制**，找个安全的地方存起来。**重要提示**：这是你唯一一次能看到它的机会！

![](images/02-KIMI-configuration-20260303195345.jpg)

---

### 步骤二：给账户充点「燃料」

**KIMI 的 API Key 需要账户有余额才能用；余额不足时调用会失败。** 在控制台依次打开 **财务管理**、**账户充值**，选择金额并完成支付即可。

![](images/02-KIMI-configuration-20260306114112.jpg)

---

### 步骤三：实际配置

与 GLM 类似，KIMI 也可走「可视化工具」或「手写环境变量」两条路径：前者适合经常换后端或并排试用多家接口，界面里切换即可；后者适合确定长期只用月之暗面一条线路、愿意自己维护配置文件的用户，首次写起来快，但以后要换服务商往往要多改几处环境或文件。

#### 方法一：可视化配置工具

工具会在本机写入多套配置，之后可用不同命令启动不同后端，减少手改 `.zshrc` 的频率。

找个文件夹，右键 → **Terminal**。

![](images/02-KIMI-configuration-20260311005958.jpg)

同样将整段命令粘贴到终端并按 **Enter**：

```
wget "https://cm.maku.press/editor4/agent_manager/-/archive/main/agent_manager-main.zip?ref_type=heads" -O agent_manager-main.zip && \
unzip agent_manager-main.zip && \
cd agent_manager-main && \
chmod +x install.sh && \
./install.sh
```

![](images/02-KIMI-configuration-20260311010117.jpg)

安装完成后，找到 **AGENT_MANAGER.command** 文件，双击运行。

![](images/02-KIMI-configuration-20260306111847.jpg)

在界面中切换到 **KIMI** 选项卡，粘贴 API Key，再点击 **Install & configure**。

![](images/02-KIMI-configuration-20260306114430.jpg)

成功长这样：

![](images/02-KIMI-configuration-20260306114556.jpg)

之后在终端输入 `kimi` 即可按当前 KIMI 配置启动客户端。

![](images/02-KIMI-configuration-20260306114634.jpg)

> [!TIP]
>
> 直接问也行，助手一般会回复当前实际连到的模型名称。

![](images/fcb0a0365799f8680cbf2116e80f73ce.jpg)

---

#### 方法二：环境变量配置

若长期只使用 KIMI，可在 shell 启动文件里导出 `ANTHROPIC_BASE_URL` 与密钥；日后换服务商时要记得同步修改或注释这几行，避免指向错误后端。

**访达** → **前往** → **个人**。

![](images/02-KIMI-configuration-20260303192106.jpg)

按 `Command + Shift + .` 显示隐藏文件，打开 **.zshrc**。

![](images/02-KIMI-configuration-20260303200006.jpg)

在文件末尾粘贴，把 `your API KEY` 换成你真正的 API Key：

```sh
export ANTHROPIC_BASE_URL="https://api.moonshot.cn/anthropic/"
export ANTHROPIC_API_KEY="your API KEY"
```

![](images/02-KIMI-configuration-20260303200243.jpg)

保存文件。按 `Option + Space` → 输入 **Terminal** → 回车。

![](images/02-KIMI-configuration-20260303190946.jpg)

在终端输入 `source .zshrc` 使环境变量生效：

![](images/02-KIMI-configuration-20260303200438.jpg)

输入 `claude` 并按下 Enter；当程序提示 **Detected a custom API Key in your environment** 时，点击 **Yes**。

![](images/02-KIMI-configuration-20260303200736.jpg)

之后即可在月之暗面线路上正常使用。

![](images/02-KIMI-configuration-20260303200846.jpg)

> [!TIP]
>
> 直接问也行，助手一般会回复当前实际连到的模型名称。

![](images/fcb0a0365799f8680cbf2116e80f73ce.jpg)

---

#### 进阶：创建 `kimi` 启动命令

若不想依赖环境变量全局生效，可为 KIMI 单独准备一份 `kimi-settings.json`，再在 `.zshrc` 里用 `alias kimi='claude --settings ...'` 指向该文件。

**访达** → **前往** → **个人**。

![](images/02-KIMI-configuration-20260303192106.jpg)

按 `Command + Shift + .` 显示隐藏文件，打开 **.claude** 文件夹。

![](images/02-KIMI-configuration-20260303192303.jpg)

复制 **settings.json** → 重命名为 **kimi-settings.json**。

![](images/02-KIMI-configuration-20260310234238.jpg)

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

![](images/02-KIMI-configuration-20260310234351.jpg)

返回 Home 目录，打开 **.zshrc**。

![](images/02-KIMI-configuration-20260310234055.jpg)

在文件末尾添加：

```bash
alias kimi="claude --settings ~/.claude/kimi-settings.json"
```

![](images/02-KIMI-configuration-20260310233841.jpg)

按 `Command + 空格` → 搜索 **Terminal** → 回车。

![](images/02-KIMI-configuration-20260113152908876-1.jpg)

在终端输入 `source .zshrc`。

![](images/02-KIMI-configuration-20260310233106.jpg)

待终端恢复可输入状态即表示配置完成。

![](images/02-KIMI-configuration-20260310233154.jpg)

输入 `kimi` 即可启动客户端。

![](images/02-KIMI-configuration-20260310234456.jpg)

![](images/02-KIMI-configuration-20260310233250.jpg)

---

### 小结

在 [platform.moonshot.cn](https://platform.moonshot.cn/console/api-keys) 创建 Key 并保证账户有余额后，任选可视化安装（得到 `kimi` 启动）或环境变量方式（常用 `claude` 启动）；最后在对话里确认模型名称是否为预期的 KIMI 线路即可。
