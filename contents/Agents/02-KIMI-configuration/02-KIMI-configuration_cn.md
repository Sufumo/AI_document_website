---
permalink: /contents/Agents/02-KIMI-configuration/zh/
lang: zh


layout: doc
title: KIMI 配置教程
---

> **阅前说明**
>
> 本教程假设你知道怎么打开终端、运行基本命令。如果听起来有点慌，先花5分钟看看 [Terminal 基础](../../../Basic-tools/01-terminal-basics/zh)，绝对物超所值。


# KIMI 配置教程

## 大局观：为什么在 Claude Code 里用 KIMI？

**一张图看懂两种模式：**

| 模式 | 请求去哪 | 费用算谁头上 |
|------|----------|--------------|
| **Claude 账号登录** | Anthropic 官方服务器 | 你的 Claude 套餐 |
| **KIMI API Key** | Claude Code 只是「壳」，真正干活的是 KIMI | 你的 KIMI 账户 |

**快速决策：**
- 已有稳定 Claude 账号 → 继续用 Claude 即可，本篇选读
- 没有 Claude 账号 / 想使用 KIMI 的大模型 → 继续往下看

![](./images/Pasted%20image%2020260310143951.png)

---

## 步骤一：获取你的「入场券」

一切从一个 API Key 开始。获取方式如下：

🔗 打开 [https://platform.moonshot.cn/console/api-keys](https://platform.moonshot.cn/console/api-keys) 并登录。

![](./images/Pasted%20image%2020260303194555.png)

点击 **新建 API Key**。

![](./images/Pasted%20image%2020260303194920.png)

起个能记住的名字，项目选择 **default**，然后点击 **确定**。

![](./images/Pasted%20image%2020260303195050.png)

点击 **复制**，找个安全的地方存起来。**重要提示**：这是你唯一一次能看到它的机会！

![](./images/Pasted%20image%2020260303195345.png)

---

## 步骤二：给账户充点「燃料」

**KIMI 的 API Key 需要账户有余额才能用。没钱就没法干活。**

| 操作路径 | 要做什么 |
|---------|---------|
| **财务管理** → **账户充值** | 选择金额并完成支付，搞定 |

![](./images/Pasted%20image%2020260306114112.png)

---

## 步骤三：实际配置（选择你的路线）

你有两条路可以选，按你的需求来决定：

| 方法 | 优点 | 缺点 |
|------|------|------|
| **可视化配置工具**（推荐） | 方便切换服务商，易用 | 多一步配置 |
| **环境变量** | 一条命令搞定 | 后续切换服务商较麻烦 |

### 方法一：可视化配置工具（推荐 ✨）

**为什么推荐这一种**：后续可以在 KIMI 和其他服务商之间自由切换，灵活性最高。

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
1. 点击 **KIMI** 选项卡
2. 粘贴你的 API Key
3. 点击 **Install & configure**

![](./images/Pasted%20image%2020260306114430.png)

成功长这样：

![](./images/Pasted%20image%2020260306114556.png)

现在终端输入 `kimi` 就能用 KIMI 启动 Claude Code 了。搞定。

![](./images/Pasted%20image%2020260306114634.png)

💡 **小贴士**：直接问也行，AI 会告诉你它用的是 kimi-k2.5 模型。

![](./images/fcb0a0365799f8680cbf2116e80f73ce.png)

---

### 方法二：环境变量配置

**取舍**：配置更快，但后续切换服务商较麻烦。适合确定只用 KIMI 的用户。

**访达** → **前往** → **个人**。

![](./images/Pasted%20image%2020260303192106.png)

按 `Command + Shift + .` 显示隐藏文件，打开 **.zshrc**。

![](./images/Pasted%20image%2020260303200006.png)

在文件末尾粘贴，把 `your API KEY` 换成你真正的 API Key：

```sh
export ANTHROPIC_BASE_URL="https://api.moonshot.cn/anthropic/"
export ANTHROPIC_API_KEY="your API KEY"
```

![](./images/Pasted%20image%2020260303200243.png)

保存文件。按 `Option + Space` → 输入 **Terminal** → 回车。

![](./images/Pasted%20image%2020260303190946.png)

在终端输入 `source .zshrc` 使环境变量生效：

![](./images/Pasted%20image%2020260303200438.png)

输入 `claude` 并按下 Enter；当 Claude Code 提示 **Detected a custom API Key in your environment** 时，点击 **Yes**。

![](./images/Pasted%20image%2020260303200736.png)

之后即可正常使用 Claude Code（KIMI）。

![](./images/Pasted%20image%2020260303200846.png)

💡 **小贴士**：直接问也行，AI 会告诉你它用的是 kimi-k2.5 模型。

![](./images/fcb0a0365799f8680cbf2116e80f73ce.png)

---

### 进阶：创建 `kimi` 启动命令

想用 `kimi` 命令快速启动？操作如下：

**访达** → **前往** → **个人**。

![](./images/Pasted%20image%2020260303192106.png)

按 `Command + Shift + .` 显示隐藏文件，打开 **.claude** 文件夹。

![](./images/Pasted%20image%2020260303192303.png)

复制 **settings.json** → 重命名为 **kimi-settings.json**。

![](./images/Pasted%20image%2020260310234238.png)

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

返回 Home 目录，打开 **.zshrc**。

![](./images/Pasted%20image%2020260310234055.png)

在文件末尾添加：

```bash
alias kimi="claude --settings ~/.claude/kimi-settings.json"
```

![](./images/Pasted%20image%2020260310233841.png)

按 `Command + 空格` → 搜索 **Terminal** → 回车。

![](./images/4.Claude%20code/file-20260113152908876%201.png)

在终端输入 `source .zshrc`。

![](./images/Pasted%20image%2020260310233106.png)

待终端恢复可输入状态即表示配置完成。

![](./images/Pasted%20image%2020260310233154.png)

输入 `kimi` 即可启动 Claude Code。

![](./images/Pasted%20image%2020260310234456.png)

![](./images/Pasted%20image%2020260310233250.png)

---

## 总结

1. **获取 API Key**：去 [platform.moonshot.cn](https://platform.moonshot.cn/console/api-keys)
2. **充值**：账户需要有余额才能使用
3. **配置**：可视化工具（`kimi` 命令）或环境变量（`claude` 命令）
4. **验证**：直接问 AI 用的是什么模型
5. **完成！** 开始和你的 AI 结对编程吧

---

*有问题？卡住了？KIMI 社区挺活跃的。或者直接问 Claude —— 它就在那。*
