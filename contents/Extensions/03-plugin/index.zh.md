---
title: Claude Code 插件
draft: false
prev: Extensions/01-skills
next: Apps/01-vscode-usage
---

>[!TIP]
>
> 如果你还不熟悉 Agent 与扩展的关系，可先扫一眼 [Skills 介绍](../01-skills) 与 [MCP 介绍](../02-mcp)，再回来装插件会更快上手。

# Claude Code 插件：给 AI 装上「专业工具箱」

**一句话说清楚：** Plugin 不是多聊几句天，而是把**可复用的能力包**装进 Claude Code——解析文件、跑工作流、连外部系统，都能按预设步骤执行。

如果把 Claude 想成「很聪明但缺装备」的协作者，插件就是成套工具与方法：装好后，它不只是回答问题，更能**真正帮你把事情做完**。

| 你得到什么 | 为什么重要 |
|-----------|-----------|
| **领域增强** | 金融、法律、编程等场景有现成工作流 |
| **连接外部** | 可与 Discord、Telegram 等打通，手机也能驱动电脑侧任务 |
| **流程固化** | 复杂操作变成可重复的命令与引导 |

官方插件市场：[https://claude.com/plugins#plugins](https://claude.com/plugins#plugins)

---

## 如何安装一个 Plugin（以 Skill Creator 为例）

打开插件市场，浏览各类插件；每个插件通常包含完整的使用说明与生态说明。

![](images/Pasted%20image%2020260329005815.png)

打开 **Skill Creator**（官方用于制作 Skill 的插件）。点击 **Install in Claude Code** 旁的复制按钮，复制安装命令。

![](images/Pasted%20image%2020260329011248.png)

在 Agent 工具中，将命令粘贴到对话框并执行，完成安装。

![](images/Pasted%20image%2020260329011702.png)

安装成功后，列表中会出现 **skill-creator**。

![](images/Pasted%20image%2020260329012523.png)

回到插件介绍页可查看用法：通过 `/skill-creator` 触发。

![](images/Pasted%20image%2020260329012620.png)

重启 Claude Code 以刷新插件列表，然后输入例如：

`/skill-creator Create a new skill that reviews PRs for security issues`

测试插件是否正常工作。

![](images/Pasted%20image%2020260329013003.png)

插件会逐步引导你填写选项，帮你生成属于自己的 Skill。全部完成后提交给 Claude Code 即可。

![](images/Pasted%20image%2020260329013135.png)

![](images/Pasted%20image%2020260329013256.png)

按插件预设流程走完后，例如 **security-pr-review** 的 Skill 即可成功生成。

![](images/Pasted%20image%2020260330100339.png)
