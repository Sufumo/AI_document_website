---
title: Claude Code Workshop
draft: false
prev: Apps/03-obsidian-notes
---

>[!TIP]
>
> To complete all exercises in this Claude Code workshop smoothly, it is recommended that you:
>
> Read [Terminal Basics](../../../Basic-tools/01-terminal-basics) so you are comfortable changing directories and running commands in a terminal on macOS/Windows.
> Make sure Claude Code has already been installed and configured according to the installation guides.
>
> With these preparations, you can focus on the practice tasks themselves instead of basic environment issues.


# Claude Code Workshop

## Prerequisites

Before starting, ensure you have:

- ✅ Claude Code installed (see [Claude Code Usage Guide](../../../Agents/04-claude-codel) for installation instructions)
- ✅ Basic understanding of how to use Claude Code (you can simply describe what you want in natural language)

---

## Tips & Best Practices

### Copy as Path

**Windows**

Right-click to copy the path.

![](./images/5.Claude%20Code%20Workshop/file-20260113152919865.png)

**Mac**

Right-click the file, then press and hold the Option key to copy the path.

![](./images/5.Claude%20Code%20Workshop/file-20260113152919864.png)

---

### Open in Terminal

**Windows**

Open the work folder in Terminal through right click.

![](./images/5.Claude%20Code%20Workshop/file-20260113152919867.png)

**Mac**

Open the work folder in Terminal through right click the path bar.

![](./images/5.Claude%20Code%20Workshop/file-20260113152919866.png)

---

### Usage Specifications

>[!WARNING]
>
> We strongly recommend not making modifications directly in the source file location to prevent Claude Code errors. Instead, create a new folder (such as `Output`) to save the results.

![](./images/5.Claude%20Code%20Workshop/file-20260113152919850.png)

>[!TIP]
>
> Always carefully review the results produced by Claude Code manually, rather than fully accepting everything it outputs or modifies.

---

## Exercise 1: Batch Renaming

### Objective

Rename folders from Chinese names to a standardized format: `DOC-NSE-XXXX-ChineseName`, where XXXX is a zero-padded 4-digit number.

### Input Structure

| Item | Details |
|------|---------|
| **Location** | `01_Batch_Renaming/sample_pdfs/` |
| **Content** | Multiple folders with Chinese names |

### Expected Output

| Item | Details |
|------|---------|
| **Location** | `01_Batch_Renaming/expected_results/` |
| **Format** | `DOC-NSE-0001-从70年发展看经济学理论创新/`, `DOC-NSE-0002-中国70年发展是理论创新的"金矿"...` |

### Solution Steps

#### Step 1: Open Claude Code and Navigate to the Directory

Open Claude Code and tell it where you want to work.

![](./images/5.Claude%20Code%20Workshop/file-20260113152919894.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919893.png)

#### Step 2: Prompt

Tell Claude Code what you want to do in simple language.

**Prompt:**

```
I have a folder called `sample_pdfs` that contains many folders with Chinese names. I want to rename all these folders to a new format. The new name should be: DOC-NSE followed by a 4-digit number (like 0001, 0002, 0003...), then a dash, then the original Chinese name. For example, if the original folder is called "新结构经济学", the new name should be "DOC-NSE-0001-新结构经济学". Please copy all folders from `sample_pdfs` to a new folder called `expected_results` with the new names, sorted alphabetically by the original Chinese names.
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919892.png)

#### Step 3: Let Claude Code Complete the Task

Claude Code will create a script and execute it automatically. You just need to wait.

>[!TIP]
>
> If Claude Code asks for confirmation, simply say "yes" or "proceed".

#### Step 4: Verify the Results

Ask Claude Code to show you the results to make sure everything worked correctly.

**Prompt:**

```
Please show me the first 5 folders in the `expected_results` folder to verify that the renaming worked correctly.
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919890%201.png)

---

## Exercise 2: Extract PDF Data

### Objective

Extract text content from a PDF file and save it as a Markdown file.

### Input Structure

| Item | Details |
|------|---------|
| **Location** | `02_Extract_PDF_Data/sample_pdf/` |
| **File** | `0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf` |

### Expected Output

| Item | Details |
|------|---------|
| **Location** | `02_Extract_PDF_Data/expected_result/` |
| **File** | `0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.md` |

### Solution Steps

#### Step 1: Navigate to the Directory

![](./images/5.Claude%20Code%20Workshop/file-20260113152919890.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919889.png)

#### Step 2: Prompt

Tell Claude Code what you want to do with the PDF file.

**Prompt:**

```
I have a PDF file in the `sample_pdf` folder. The file name is "0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf". I want to extract all the text content from this PDF file and save it as a Markdown file (with .md extension). The new file should have the same name as the PDF but with .md extension instead of .pdf. Please save it in a folder called `expected_result`. Extract all the text from all pages of the PDF.
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919888.png)

#### Step 3: Wait for Completion

Claude Code will automatically install any necessary tools and extract the text from the PDF. Just wait for it to finish.

---

## Exercise 3: Format Conversion

### Objective

Convert PDF to Markdown, then convert Markdown to DOCX format.

### Input Structure

| Item | Details |
|------|---------|
| **Location** | `03_Format_Conversion/sample_pdfs/` |
| **File** | `0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf` |

### Expected Output

| Item | Details |
|------|---------|
| **Location** | `03_Format_Conversion/expected_result/` |
| **Files** | Both `.md` and `.docx` versions |

### Solution Steps

#### Step 1: Navigate to the Directory

![](./images/5.Claude%20Code%20Workshop/file-20260113152919887.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919886%201.png)

#### Step 2: Prompt

Tell Claude Code you want to convert the PDF to both Markdown and DOCX formats.

**Prompt:**

```
I have a PDF file in the `sample_pdfs` folder. The file name is "0007_Glantz and House - 2015 - X052 - When Titans Clashed - pp. 369_X052,X082.pdf". I want to:
1. First, convert this PDF file to a Markdown file (.md format)
2. Then, convert that Markdown file to a DOCX file (.docx format)
3. Save both files in a folder called `expected_result`
Both files should have the same name as the original PDF, but with different extensions (.md and .docx).
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919886.png)

#### Step 3: Wait for Completion

Claude Code will handle all the conversions automatically. Just wait for it to finish.

---

## Exercise 4: Web Scraping

### Objective

Extract content from HTML files and convert to Markdown format.

### Input Structure

| Item | Details |
|------|---------|
| **Location** | `04_Web_Scraping/` |
| **Files** | Multiple HTML files (e.g., `01_Protests_erupt_in_Tanzania...html`) |

### Expected Output

| Item | Details |
|------|---------|
| **Location** | `04_Web_Scraping/` |
| **Files** | Corresponding `.md` files for each HTML file |

### Solution Steps

#### Step 1: Navigate to the Directory

![](./images/5.Claude%20Code%20Workshop/file-20260113152919885.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919884.png)

#### Step 2: Prompt

Tell Claude Code you want to convert HTML files to Markdown files.

**Prompt:**

```
I have several HTML files in this folder (files ending with .html). I want to convert each HTML file to a Markdown file (.md format). For each HTML file, create a new Markdown file with the same name but with .md extension instead of .html. Extract the main content from each HTML file and convert it to Markdown format. Save the Markdown files in the same folder as the HTML files.
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919879.png)

#### Step 3: Wait for Completion

Claude Code will process all HTML files and convert them to Markdown automatically.

---

## Exercise 5: Split Files

### Objective

Split a large PDF file into multiple smaller PDF files with a specified number of pages per file.

### Input Structure

| Item | Details |
|------|---------|
| **Location** | `05_Split_Files/sample_pdfs/` |
| **File** | `DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy.pdf` |

### Expected Output

| Item | Details |
|------|---------|
| **Location** | `05_Split_Files/expected_result/` |
| **Files** | `DOC-NSE-0827-..._part1.pdf`, `DOC-NSE-0827-..._part2.pdf`, etc. |

### Solution Steps

#### Step 1: Navigate to the Directory

![](./images/5.Claude%20Code%20Workshop/file-20260113152919883.png)

![](./images/5.Claude%20Code%20Workshop/file-20260113152919881.png)

#### Step 2: Prompt

Tell Claude Code you want to split the PDF into smaller files.

**Prompt:**

```
I have a large PDF file in the `sample_pdfs` folder. The file name is "DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy.pdf". I want to split this PDF file into multiple smaller PDF files. Each smaller file should contain 50 pages. Name the split files by adding "_part1", "_part2", "_part3", etc. to the original file name (before the .pdf extension). For example, the first part should be named "DOC-NSE-0827-New Structural Economics： A Framework for Rethinking Development and Policy_part1.pdf". Save all the split files in a folder called `expected_result`.
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919874.png)

#### Step 3: Wait for Completion

Claude Code will split the PDF file automatically. Just wait for it to finish.

#### Step 4: Verify the Results

Ask Claude Code to show you the split files to make sure everything worked correctly.

**Prompt:**

```
Please show me all the split PDF files in the `expected_result` folder to verify that the splitting worked correctly.
```

![](./images/5.Claude%20Code%20Workshop/file-20260113152919871.png)

---

## Summary

Here's the deal: These 5 exercises demonstrate how to use Claude Code with simple natural language prompts:

| Exercise | What You'll Learn |
|----------|-------------------|
| **1. Batch Renaming** | Describe what you want to rename, and Claude Code will handle it |
| **2. Data Extraction** | Describe what you want to extract, and Claude Code will do it |
| **3. Format Conversion** | Describe the conversion you need, and Claude Code will convert it |
| **4. Web Scraping** | Describe what content you want, and Claude Code will extract it |
| **5. File Manipulation** | Describe how you want to split files, and Claude Code will split them |

>[!TIP]
>
> **Key Takeaway**: By completing these exercises, you'll learn that you don't need to write code yourself — you can simply describe what you want in natural language, and Claude Code will do the work for you.

---

*Questions? Stuck somewhere? Check out the official documentation. Or just ask Claude — it's literally right there.*
