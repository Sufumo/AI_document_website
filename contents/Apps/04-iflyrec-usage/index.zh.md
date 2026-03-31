---
title: 讯飞听见使用指南
draft: false
prev: Apps/01-vscode-usage
next: Agents/05-claude-code-workshop
---

>[!TIP]
>
> 本文聚焦 **Import File（文件转录）** 全流程；**Start Recording（实时录音）** 上手同样直观，可自行尝试。

# 讯飞听见：会议与字幕的「快转文字」方案

**为什么用它？** 多语种语音 → **准确、可导出**的文本，不必自己折腾脚本或大模型 API；图形界面清晰，适合会议纪要、复盘与字幕粗稿。

与「纯靠命令行/脚本调用语音识别」相比，讯飞听见把**语言选择、说话人、领域词**等选项放在界面上，往往**更少试错、更快出稿**。

## 安装

打开官网下载页：  
[https://www.iflyrec.com/zhuanwenzi.html](https://www.iflyrec.com/zhuanwenzi.html)  
点击 **下载**，获取讯飞听见 App。

![](images/Pasted%20image%2020260328000623.png)

双击安装包，按向导完成安装。

![](images/Pasted%20image%2020260328001242.png)

![](images/Pasted%20image%2020260328001349.png)

![](images/Pasted%20image%2020260328001416.png)

![](images/Pasted%20image%2020260328001437.png)

![](images/Pasted%20image%2020260328001458.png)

首次进入需同意用户协议并登录。

![](images/Pasted%20image%2020260328001805.png)

![](images/Pasted%20image%2020260328001824.png)

![](images/Pasted%20image%2020260328001847.png)

## 主界面速览

登录后，Home 上常用能力包括：

| 功能 | 适用场景 |
|------|----------|
| **Start Recording** | 边录边转，带一定润色，适合现场速记 |
| **Import File** | 音视频转文字，多语言、速度快，适合复盘与字幕 |
| **Floating Captions** | 悬浮实时字幕，切到其他应用时仍能看转写结果 |

下方 **Recent Files** 展示历史任务；文件保存在云端，便于手机与电脑同步，降低本地丢失风险。

下文以 **Import File** 为主。点击 **Import File** 进入文件转录。

![](images/Pasted%20image%2020260328002717.png)

## 上传与参数（决定质量的关键）

**源语言**务必选对：默认含仅英语、中英混合等；选对语言通常能**明显提升**识别质量。

![](images/Pasted%20image%2020260328011832.png)

点击 **More** 可展开更多语言（如西班牙语、日语、汉语等），以及 **英语 Pro / 中英混合 Pro** 等增强选项。

![](images/Pasted%20image%2020260328012651.png)

将音视频文件拖入 **Select or drag** 区域。

![](images/Pasted%20image%2020260328012830.png)

**Speaker**：选择说话人数量；不确定可选 **Auto**。示例为单人视频，故选 **1**。信息越准，稿面越干净。

![](images/Pasted%20image%2020260328013110.png)

**Professional Domains**：按内容选领域（法律、经济、医疗等），有助于专业术语识别与行文优化。

![](images/Pasted%20image%2020260328013338.png)

若列表中没有合适领域，可在 **Keyword Optimization** 中填写关键词，内置 AI 会结合关键词优化识别与表述。

![](images/Pasted%20image%2020260328013619.png)

确认后点击 **Submit** 上传；界面会显示上传进度。

![](images/Pasted%20image%2020260328013814.png)

![](images/Pasted%20image%2020260328013901.png)

上传结束后，**Uploading** 变为 **Open File**，点击即可开始转写。

![](images/Pasted%20image%2020260328014036.png)

## 任务与预览

转写进行中或完成后，左侧任务栏会出现对应条目；可点击话筒图标快速跳转。

![](images/Pasted%20image%2020260328014238.png)

点击文稿某段，音频进度条会跳到对应时间，便于**逐段核对**质量。

![](images/Pasted%20image%2020260328014511.png)

进度条旁的设置中可调整预览行为：

- **Display speaker**：像对话一样显示不同说话人名称  
- **Speaker filtering**：按说话人筛选播放，适合去噪或只听某些人  
- **Display timecode**：在文本上方显示段落起始时间  
- **Skip silent segments**：跳过静音段，稿面更紧凑  

![](images/Pasted%20image%2020260328020116.png)

设置旁的翻译按钮可翻译全文。

>[!TIP]
>
> 讯飞听见可将多种源语言译成**中文**；若目标语不是中文，请导出后用其他工具处理。

![](images/Pasted%20image%2020260328014750.png)

## 导出

点击 **Downloads** 进入导出。

![](images/Pasted%20image%2020260328014640.png)

可选择 **docx / srt / txt** 等格式，并决定是否附带说话人、时间码等元信息。

![](images/Pasted%20image%2020260328015351.png)

点击 **Download** 保存到本机。

![](images/Pasted%20image%2020260328015733.png)

![](images/Pasted%20image%2020260328015824.png)

一份可用的转写稿即完成。若要做视频字幕，**srt** 通常是首选。

![](images/Pasted%20image%2020260328015906.png)

---

**小结：** 讯飞听见适合**大量会议、演讲、课程**的快速成稿；应用内还有多种 AI 辅助功能，可按需自行探索。
