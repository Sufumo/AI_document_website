---
title: Claude Code 实践任务
draft: false
---

>[!TIP]
>
> 为了顺利完成本 Claude Code 工作坊中的所有练习，建议您：
>
> - 阅读 [Terminal 基础](../../../Basic-tools/01-terminal-basics/zh)，熟悉在 macOS/Windows 中通过终端切换目录、运行命令。
> - 确保已按安装/配置文档提前安装并配置好 Claude Code。
>
> 完成以上准备后，您就可以把精力集中在练习任务本身，而不是基础环境问题上。


# Claude Code 实践任务

## 前置要求

在开始之前，请确保您已具备：

- ✅ Claude Code 已安装（安装说明请参见 [Claude Code 使用教程](../../../Agents/04-claude-codel/zh)）
- ✅ 基本了解如何使用 Claude Code（只需用自然语言描述您想要完成的任务即可）

---

## 小贴士与最佳实践

### 复制路径

**Windows**

右键复制文件路径。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919865.png)

**Mac**

右键并按住 Option 键以复制路径。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919864.png)

---

### 在终端打开

**Windows**

通过右键在 Terminal 中打开工作文件夹。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919867.png)

**Mac**

通过右键路径栏在 Terminal 中打开工作文件夹。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919866.png)

---

### 使用规范

⚠️ **重要警告**：我们强烈建议不要在源文件位置直接进行修改，以防 Claude Code 出错；应新建一个文件夹（如 `Output`）保存结果。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919850.png)

💡 **小贴士**：应仔细人工审核 Claude Code 输出的结果，而非完全接受 Claude Code 输出或修改的内容。

---

## 练习1：批量重命名

### 目标

将文件夹从中文名称重命名为标准化格式：`DOC-NSE-XXXX-中文名称`，其中 XXXX 是补零的4位数字。

### 输入结构

| 项目 | 详情 |
|------|------|
| **位置** | `01_Batch_Renaming/sample_pdfs/` |
| **内容** | 包含多个中文命名的文件夹 |

### 预期输出

| 项目 | 详情 |
|------|------|
| **位置** | `01_Batch_Renaming/expected_results/` |
| **格式** | `DOC-NSE-0001-从70年发展看经济学理论创新/`, `DOC-NSE-0002-中国70年发展是理论创新的"金矿"...` |

### 解题步骤

#### 步骤1：打开 Claude Code 并导航到目录

打开 Claude Code 并告诉它您要在哪里工作。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919894.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919893.png)

#### 步骤2：提词

用简单的语言告诉 Claude Code 您想要做什么。

**提词：**

```
我有一个名为 `sample_pdfs` 的文件夹，里面包含许多中文名称的文件夹。我想将所有文件夹重命名为新格式。新名称应该是：DOC-NSE 后跟4位数字（如 0001、0002、0003...），然后是短横线，然后是原来的中文名称。例如，如果原来的文件夹叫"新结构经济学"，新名称应该是"DOC-NSE-0001-新结构经济学"。请将所有文件夹从 `sample_pdfs` 复制到名为 `expected_results` 的新文件夹中，使用新名称，按原来的中文名称字母顺序排序。
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919892.png)

#### 步骤3：让 Claude Code 完成任务

Claude Code 会自动创建脚本并执行。您只需等待。

💡 **小贴士**：如果 Claude Code 请求确认，只需说"yes"或"继续"即可。

#### 步骤4：验证结果

请 Claude Code 显示结果，以确保一切正常工作。

**提词：**

```
请向我展示 `expected_results` 文件夹中的前5个文件夹，以验证重命名是否正确。
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919890%201.png)

---

## 练习2：提取PDF数据

### 目标

从 PDF 文件中提取文本内容并保存为 Markdown 文件。

### 输入结构

| 项目 | 详情 |
|------|------|
| **位置** | `02_Extract_PDF_Data/sample_pdf/` |
| **文件** | `0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf` |

### 预期输出

| 项目 | 详情 |
|------|------|
| **位置** | `02_Extract_PDF_Data/expected_result/` |
| **文件** | `0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.md` |

### 解题步骤

#### 步骤1：导航到目录

![](./images/5.Claude%20Code%20Workshop/file-20260113152919890.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919889.png)

#### 步骤2：提词

告诉 Claude Code 您想对 PDF 文件做什么。

**提词：**

```
我在 `sample_pdf` 文件夹中有一个 PDF 文件。文件名是"0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf"。我想从这个 PDF 文件中提取所有文本内容，并将其保存为 Markdown 文件（扩展名为 .md）。新文件应与 PDF 同名，但扩展名是 .md 而不是 .pdf。请将其保存在名为 `expected_result` 的文件夹中。从 PDF 的所有页面中提取所有文本。
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919888.png)

#### 步骤3：等待完成

Claude Code 会自动安装任何必要的工具并从 PDF 中提取文本。只需等待它完成。

---

## 练习3：格式转换

### 目标

将 PDF 转换为 Markdown，然后将 Markdown 转换为 DOCX 格式。

### 输入结构

| 项目 | 详情 |
|------|------|
| **位置** | `03_Format_Conversion/sample_pdfs/` |
| **文件** | `0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf` |

### 预期输出

| 项目 | 详情 |
|------|------|
| **位置** | `03_Format_Conversion/expected_result/` |
| **文件** | `.md` 和 `.docx` 两个版本 |

### 解题步骤

#### 步骤1：导航到目录

![](./images/5.Claude%20Code%20Workshop/file-20260113152919887.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919886%201.png)

#### 步骤2：提词

告诉 Claude Code 您想将 PDF 转换为 Markdown 和 DOCX 两种格式。

**提词：**

```
我在 `sample_pdfs` 文件夹中有一个 PDF 文件。文件名是"0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf"。我想要：
1. 首先，将这个 PDF 文件转换为 Markdown 文件（.md 格式）
2. 然后，将该 Markdown 文件转换为 DOCX 文件（.docx 格式）
3. 将两个文件都保存在名为 `expected_result` 的文件夹中
两个文件应与原始 PDF 同名，但扩展名不同（.md 和 .docx）。
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919886.png)

#### 步骤3：等待完成

Claude Code 会自动处理所有转换。只需等待它完成。

---

## 练习4：网页抓取

### 目标

从 HTML 文件中提取内容并转换为 Markdown 格式。

### 输入结构

| 项目 | 详情 |
|------|------|
| **位置** | `04_Web_Scraping/` |
| **文件** | 多个 HTML 文件（例如 `01_Protests_erupt_in_Tanzania...html`） |

### 预期输出

| 项目 | 详情 |
|------|------|
| **位置** | `04_Web_Scraping/` |
| **文件** | 每个 HTML 文件对应的 `.md` 文件 |

### 解题步骤

#### 步骤1：导航到目录

![](./images/5.Claude%20Code%20Workshop/file-20260113152919885.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919884.png)

#### 步骤2：提词

告诉 Claude Code 您想将 HTML 文件转换为 Markdown 文件。

**提词：**

```
这个文件夹中有几个 HTML 文件（以 .html 结尾的文件）。我想将每个 HTML 文件转换为 Markdown 文件（.md 格式）。对于每个 HTML 文件，创建一个新的 Markdown 文件，名称相同，但扩展名是 .md 而不是 .html。从每个 HTML 文件中提取主要内容并转换为 Markdown 格式。将 Markdown 文件保存在与 HTML 文件相同的文件夹中。
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919879.png)

#### 步骤3：等待完成

Claude Code 会自动处理所有 HTML 文件并将它们转换为 Markdown。

---

## 练习5：分割文件

### 目标

将大型 PDF 文件分割为多个较小的 PDF 文件，每个文件包含指定页数。

### 输入结构

| 项目 | 详情 |
|------|------|
| **位置** | `05_Split_Files/sample_pdfs/` |
| **文件** | `DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy.pdf` |

### 预期输出

| 项目 | 详情 |
|------|------|
| **位置** | `05_Split_Files/expected_result/` |
| **文件** | `DOC-NSE-0827-..._part1.pdf`, `DOC-NSE-0827-..._part2.pdf` 等 |

### 解题步骤

#### 步骤1：导航到目录

![](./images/5.Claude%20Code%20Workshop/file-20260113152919883.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919881.png)

#### 步骤2：提词

告诉 Claude Code 您想将 PDF 分割为较小的文件。

**提词：**

```
我在 `sample_pdfs` 文件夹中有一个大型 PDF 文件。文件名是"DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy.pdf"。我想将这个 PDF 文件分割为多个较小的 PDF 文件。每个较小的文件应包含 50 页。通过在原文件名（.pdf 扩展名之前）添加"_part1"、"_part2"、"_part3"等来命名分割的文件。例如，第一部分应命名为"DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy_part1.pdf"。将所有分割的文件保存在名为 `expected_result` 的文件夹中。
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919874.png)

#### 步骤3：等待完成

Claude Code 会自动分割 PDF 文件。只需等待它完成。

#### 步骤4：验证结果

请 Claude Code 显示分割的文件，以确保一切正常工作。

**提词：**

```
请向我展示 `expected_result` 文件夹中的所有分割 PDF 文件，以验证分割是否正确。
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919871.png)

---

## 总结

这5道练习展示了如何使用简单的自然语言提词来使用 Claude Code：

| 练习 | 你会学到什么 |
|------|-------------|
| **1. 批量重命名** | 描述您想要重命名的内容，Claude Code 会处理它 |
| **2. 数据提取** | 描述您想要提取的内容，Claude Code 会完成它 |
| **3. 格式转换** | 描述您需要的转换，Claude Code 会转换它 |
| **4. 网页抓取** | 描述您想要的内容，Claude Code 会提取它 |
| **5. 文件操作** | 描述您想要如何分割文件，Claude Code 会分割它们 |

💡 **核心要点**：通过完成这些练习，您将了解到您不需要自己编写代码——只需用自然语言描述您想要的内容，Claude Code 就会为您完成工作。

---

*有问题？卡住了？查阅官方文档。或者直接问 Claude —— 它就在那。*
