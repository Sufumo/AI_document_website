---

layout: doc

title: Claude Code Workshop · Claude Code 实践任务

---

## 阅前说明
> Pre-reading Note
>
> To complete all exercises in this Claude Code workshop smoothly, it is recommended that you:
>
> - Read [Terminal Basics](/contents/Basic-tools/01-terminal-basics.html) so you are comfortable changing directories and running commands in a terminal on macOS/Windows.
> - Make sure Claude Code has already been installed and configured according to the installation guides.
>
> With these preparations, you can focus on the practice tasks themselves instead of basic environment issues.
>

> 阅前说明
>
> 为了顺利完成本 Claude Code 工作坊中的所有练习，建议您：
>
> - 阅读 [Terminal 基础](/contents/Basic-tools/01-terminal-basics.html)，熟悉在 macOS/Windows 中通过终端切换目录、运行命令。
> - 确保已按安装/配置文档提前安装并配置好 Claude Code。
>
> 完成以上准备后，您就可以把精力集中在练习任务本身，而不是基础环境问题上。


# Claude Code Workshop Solutions (Claude Code 工作坊参考答案)

## Prerequisites (前置要求)

Before starting, ensure you have:
在开始之前，请确保您已具备：

- Claude Code installed (see [4.Claude code.md](4.Claude%20code.md) for installation instructions)
- Claude Code 已安装（安装说明请参见 [4.Claude code.md](4.Claude%20code.md)）
- Basic understanding of how to use Claude Code (you can simply describe what you want in natural language)
- 基本了解如何使用 Claude Code（只需用自然语言描述您想要完成的任务即可）

---

## Tips (小贴士)

### Copy as path
### 复制路径

**Windows**

Right-click to copy the path.
右键复制文件路径。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919865.png)

**Mac**

Right-click the file, then press and hold the Option key to copy the path.
右键并按住 Option 键以复制路径。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919864.png)
### Open in Terminal
### 在终端打开

**Windows**

Open the work folder in Terminal through right click.
通过右键在 Terminal 中打开工作文件夹。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919867.png)

**Mac**

Open the work folder in Terminal through right click the path bar.
通过右键路径栏在 Terminal 中打开工作文件夹。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919866.png)

### Usage Specifications
### 使用规范

We strongly recommend not making modifications directly in the source file location to prevent Claude Code errors. Instead, create a new folder (such as `Output`) to save the results.
我们强烈建议不要在源文件位置直接进行修改，以防 Claude Code 出错；应新建一个文件夹（如 `Output`）保存结果。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919850.png)

In addition, the results produced by Claude Code should be carefully reviewed manually, rather than fully accepting everything it outputs or modifies.
除此之外，应仔细人工审核 Claude Code 输出的结果，而非完全接受 Claude Code 输出或修改的内容。

## Exercise 1: Batch Renaming (练习1：批量重命名)

### Objective (目标)

Rename folders from Chinese names to a standardized format: `DOC-NSE-XXXX-ChineseName`, where XXXX is a zero-padded 4-digit number.
将文件夹从中文名称重命名为标准化格式：`DOC-NSE-XXXX-中文名称`，其中 XXXX 是补零的4位数字。

### Input Structure (输入结构)

- **Location**: `01_Batch_Renaming/sample_pdfs/`
- **Content**: Multiple folders with Chinese names
- **位置**：`01_Batch_Renaming/sample_pdfs/`
- **内容**：包含多个中文命名的文件夹

### Expected Output (预期输出)

- **Location**: `01_Batch_Renaming/expected_results/`
- **Format**: `DOC-NSE-0001-从70年发展看经济学理论创新/`, `DOC-NSE-0002-中国70年发展是理论创新的"金矿"...`
- **位置**：`01_Batch_Renaming/expected_results/`
- **格式**：`DOC-NSE-0001-从70年发展看经济学理论创新/`, `DOC-NSE-0002-中国70年发展是理论创新的"金矿"...`

### Solution Steps (解题步骤)

#### Step 1: Open Claude Code and Navigate to the Directory (步骤1：打开 Claude Code 并导航到目录)

Open Claude Code and tell it where you want to work.
打开 Claude Code 并告诉它您要在哪里工作。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919894.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919893.png)

#### Step 2: Prompt (步骤2：提词)

Tell Claude Code what you want to do in simple language.
用简单的语言告诉 Claude Code 您想要做什么。

**Prompt (提词):**
I have a folder called `sample_pdfs` that contains many folders with Chinese names. I want to rename all these folders to a new format. The new name should be: DOC-NSE followed by a 4-digit number (like 0001, 0002, 0003...), then a dash, then the original Chinese name. For example, if the original folder is called "新结构经济学", the new name should be "DOC-NSE-0001-新结构经济学". Please copy all folders from `sample_pdfs` to a new folder called `expected_results` with the new names, sorted alphabetically by the original Chinese names.
我有一个名为 `sample_pdfs` 的文件夹，里面包含许多中文名称的文件夹。我想将所有文件夹重命名为新格式。新名称应该是：DOC-NSE 后跟4位数字（如 0001、0002、0003...），然后是短横线，然后是原来的中文名称。例如，如果原来的文件夹叫"新结构经济学"，新名称应该是"DOC-NSE-0001-新结构经济学"。请将所有文件夹从 `sample_pdfs` 复制到名为 `expected_results` 的新文件夹中，使用新名称，按原来的中文名称字母顺序排序。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919892.png)

#### Step 3: Let Claude Code Complete the Task (步骤3：让 Claude Code 完成任务)

Claude Code will create a script and execute it automatically. You just need to wait.
Claude Code 会自动创建脚本并执行。您只需等待。

If Claude Code asks for confirmation, simply say "yes" or "proceed".
如果 Claude Code 请求确认，只需说"yes"或"继续"即可。
#### Step 4: Verify the Results (步骤4：验证结果)

Ask Claude Code to show you the results to make sure everything worked correctly.
请 Claude Code 显示结果，以确保一切正常工作。

**Prompt (提词):**
Please show me the first 5 folders in the `expected_results` folder to verify that the renaming worked correctly.
请向我展示 `expected_results` 文件夹中的前5个文件夹，以验证重命名是否正确。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919890%201.png)

---

## Exercise 2: Extract PDF Data (练习2：提取PDF数据)

### Objective (目标)

Extract text content from a PDF file and save it as a Markdown file.
从 PDF 文件中提取文本内容并保存为 Markdown 文件。

### Input Structure (输入结构)

- **Location**: `02_Extract_PDF_Data/sample_pdf/`
- **File**: `0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf`
- **位置**：`02_Extract_PDF_Data/sample_pdf/`
- **文件**：`0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf`

### Expected Output (预期输出)

- **Location**: `02_Extract_PDF_Data/expected_result/`
- **File**: `0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.md`
- **位置**：`02_Extract_PDF_Data/expected_result/`
- **文件**：`0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.md`

### Solution Steps (解题步骤)

#### Step 1: Navigate to the Directory (步骤1：导航到目录)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919890.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919889.png)
#### Step 2: Prompt (步骤2：提词)

Tell Claude Code what you want to do with the PDF file.
告诉 Claude Code 您想对 PDF 文件做什么。

**Prompt (提词):**
I have a PDF file in the `sample_pdf` folder. The file name is "0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf". I want to extract all the text content from this PDF file and save it as a Markdown file (with .md extension). The new file should have the same name as the PDF but with .md extension instead of .pdf. Please save it in a folder called `expected_result`. Extract all the text from all pages of the PDF.
我在 `sample_pdf` 文件夹中有一个 PDF 文件。文件名是"0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf"。我想从这个 PDF 文件中提取所有文本内容，并将其保存为 Markdown 文件（扩展名为 .md）。新文件应与 PDF 同名，但扩展名是 .md 而不是 .pdf。请将其保存在名为 `expected_result` 的文件夹中。从 PDF 的所有页面中提取所有文本。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919888.png)

#### Step 3: Wait for Completion (步骤3：等待完成)

Claude Code will automatically install any necessary tools and extract the text from the PDF. Just wait for it to finish.
Claude Code 会自动安装任何必要的工具并从 PDF 中提取文本。只需等待它完成。

## Exercise 3: Format Conversion (练习3：格式转换)

### Objective (目标)

Convert PDF to Markdown, then convert Markdown to DOCX format.
将 PDF 转换为 Markdown，然后将 Markdown 转换为 DOCX 格式。

### Input Structure (输入结构)

- **Location**: `03_Format_Conversion/sample_pdfs/`
- **File**: `0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf`
- **位置**：`03_Format_Conversion/sample_pdfs/`
- **文件**：`0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf`

### Expected Output (预期输出)

- **Location**: `03_Format_Conversion/expected_result/`
- **Files**: Both `.md` and `.docx` versions
- **位置**：`03_Format_Conversion/expected_result/`
- **文件**：`.md` 和 `.docx` 两个版本

### Solution Steps (解题步骤)

#### Step 1: Navigate to the Directory (步骤1：导航到目录)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919887.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919886%201.png)
#### Step 2: Prompt (步骤2：提词)

Tell Claude Code you want to convert the PDF to both Markdown and DOCX formats.
告诉 Claude Code 您想将 PDF 转换为 Markdown 和 DOCX 两种格式。

**Prompt (提词):**
I have a PDF file in the `sample_pdfs` folder. The file name is "0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf". I want to:
1. First, convert this PDF file to a Markdown file (.md format)
2. Then, convert that Markdown file to a DOCX file (.docx format)
3. Save both files in a folder called `expected_result`
Both files should have the same name as the original PDF, but with different extensions (.md and .docx).
我在 `sample_pdfs` 文件夹中有一个 PDF 文件。文件名是"0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf"。我想要：
1. 首先，将这个 PDF 文件转换为 Markdown 文件（.md 格式）
2. 然后，将该 Markdown 文件转换为 DOCX 文件（.docx 格式）
3. 将两个文件都保存在名为 `expected_result` 的文件夹中
两个文件应与原始 PDF 同名，但扩展名不同（.md 和 .docx）。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919886.png)

#### Step 3: Wait for Completion (步骤3：等待完成)

Claude Code will handle all the conversions automatically. Just wait for it to finish.
Claude Code 会自动处理所有转换。只需等待它完成。

---

## Exercise 4: Web Scraping (练习4：网页抓取)

### Objective (目标)

Extract content from HTML files and convert to Markdown format.
从 HTML 文件中提取内容并转换为 Markdown 格式。

### Input Structure (输入结构)

- **Location**: `04_Web_Scraping/`
- **Files**: Multiple HTML files (e.g., `01_Protests_erupt_in_Tanzania...html`)
- **位置**：`04_Web_Scraping/`
- **文件**：多个 HTML 文件（例如 `01_Protests_erupt_in_Tanzania...html`）

### Expected Output (预期输出)

- **Location**: `04_Web_Scraping/`
- **Files**: Corresponding `.md` files for each HTML file
- **位置**：`04_Web_Scraping/`
- **文件**：每个 HTML 文件对应的 `.md` 文件

### Solution Steps (解题步骤)

#### Step 1: Navigate to the Directory (步骤1：导航到目录)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919885.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919884.png)
#### Step 2: Prompt (步骤2：提词)

Tell Claude Code you want to convert HTML files to Markdown files.
告诉 Claude Code 您想将 HTML 文件转换为 Markdown 文件。

**Prompt (提词):**
I have several HTML files in this folder (files ending with .html). I want to convert each HTML file to a Markdown file (.md format). For each HTML file, create a new Markdown file with the same name but with .md extension instead of .html. Extract the main content from each HTML file and convert it to Markdown format. Save the Markdown files in the same folder as the HTML files.
这个文件夹中有几个 HTML 文件（以 .html 结尾的文件）。我想将每个 HTML 文件转换为 Markdown 文件（.md 格式）。对于每个 HTML 文件，创建一个新的 Markdown 文件，名称相同，但扩展名是 .md 而不是 .html。从每个 HTML 文件中提取主要内容并转换为 Markdown 格式。将 Markdown 文件保存在与 HTML 文件相同的文件夹中。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919879.png)

#### Step 3: Wait for Completion (步骤3：等待完成)

Claude Code will process all HTML files and convert them to Markdown automatically.
Claude Code 会自动处理所有 HTML 文件并将它们转换为 Markdown。

---

## Exercise 5: Split Files (练习5：分割文件)

### Objective (目标)

Split a large PDF file into multiple smaller PDF files with a specified number of pages per file.
将大型 PDF 文件分割为多个较小的 PDF 文件，每个文件包含指定页数。

### Input Structure (输入结构)

- **Location**: `05_Split_Files/sample_pdfs/`
- **File**: `DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy.pdf`
- **位置**：`05_Split_Files/sample_pdfs/`
- **文件**：`DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy.pdf`

### Expected Output (预期输出)

- **Location**: `05_Split_Files/expected_result/`
- **Files**: `DOC-NSE-0827-..._part1.pdf`, `DOC-NSE-0827-..._part2.pdf`, etc.
- **位置**：`05_Split_Files/expected_result/`
- **文件**：`DOC-NSE-0827-..._part1.pdf`, `DOC-NSE-0827-..._part2.pdf` 等

### Solution Steps (解题步骤)

#### Step 1: Navigate to the Directory (步骤1：导航到目录)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919883.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919881.png)
#### Step 2: Prompt (步骤2：提词)

Tell Claude Code you want to split the PDF into smaller files.
告诉 Claude Code 您想将 PDF 分割为较小的文件。

**Prompt (提词):**
I have a large PDF file in the `sample_pdfs` folder. The file name is "DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy.pdf". I want to split this PDF file into multiple smaller PDF files. Each smaller file should contain 50 pages. Name the split files by adding "_part1", "_part2", "_part3", etc. to the original file name (before the .pdf extension). For example, the first part should be named "DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy_part1.pdf". Save all the split files in a folder called `expected_result`.
我在 `sample_pdfs` 文件夹中有一个大型 PDF 文件。文件名是"DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy.pdf"。我想将这个 PDF 文件分割为多个较小的 PDF 文件。每个较小的文件应包含 50 页。通过在原文件名（.pdf 扩展名之前）添加"_part1"、"_part2"、"_part3"等来命名分割的文件。例如，第一部分应命名为"DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy_part1.pdf"。将所有分割的文件保存在名为 `expected_result` 的文件夹中。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919874.png)

#### Step 3: Wait for Completion (步骤3：等待完成)

Claude Code will split the PDF file automatically. Just wait for it to finish.
Claude Code 会自动分割 PDF 文件。只需等待它完成。

#### Step 4: Verify the Results (步骤4：验证结果)

Ask Claude Code to show you the split files to make sure everything worked correctly.
请 Claude Code 显示分割的文件，以确保一切正常工作。

**Prompt (提词):**
Please show me all the split PDF files in the `expected_result` folder to verify that the splitting worked correctly.
请向我展示 `expected_result` 文件夹中的所有分割 PDF 文件，以验证分割是否正确。

![](./images/5.Claude%20Code%20Workshop/file-20260113152919871.png)

---

## Summary (总结)

These 5 exercises demonstrate how to use Claude Code with simple natural language prompts:
这5道练习展示了如何使用简单的自然语言提词来使用 Claude Code：

1. **Batch Operations**: Describe what you want to rename, and Claude Code will handle it
   **批量操作**：描述您想要重命名的内容，Claude Code 会处理它
2. **Data Extraction**: Describe what you want to extract, and Claude Code will do it
   **数据提取**：描述您想要提取的内容，Claude Code 会完成它
3. **Format Conversion**: Describe the conversion you need, and Claude Code will convert it
   **格式转换**：描述您需要的转换，Claude Code 会转换它
4. **Web Scraping**: Describe what content you want, and Claude Code will extract it
   **网页抓取**：描述您想要的内容，Claude Code 会提取它
5. **File Manipulation**: Describe how you want to split files, and Claude Code will split them
   **文件操作**：描述您想要如何分割文件，Claude Code 会分割它们

By completing these exercises, you'll learn that you don't need to write code yourself—you can simply describe what you want in natural language, and Claude Code will do the work for you.
通过完成这些练习，您将了解到您不需要自己编写代码——只需用自然语言描述您想要的内容，Claude Code 就会为您完成工作。

