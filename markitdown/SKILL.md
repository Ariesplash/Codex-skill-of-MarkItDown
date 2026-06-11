---
name: markitdown
description: Convert various file formats (PDF, DOCX, PPTX, XLSX, HTML, images, ZIP, EPUB) to Markdown using Microsoft MarkItDown. Use when user needs to extract text from documents or convert files to markdown.
---

# MarkItDown - File to Markdown Converter

> Microsoft MarkItDown: Convert PDF, Office documents, images, HTML and more to Markdown format.

## Installation

```bash
pip install markitdown
```

## Basic CLI Usage

### Convert single file

```bash
markitdown input.pdf
markitdown input.docx -o output.md
markitdown input.pptx > output.md
cat input.html | markitdown
```

### Supported Formats

| Format | Extension |
|--------|-----------|
| PDF | .pdf |
| Word | .docx |
| PowerPoint | .pptx |
| Excel | .xlsx |
| HTML | .html, .htm |
| Images | .jpg, .png, .bmp, .gif, .tiff |
| CSV | .csv |
| JSON | .json |
| XML | .xml |
| ZIP | .zip |
| EPUB | .epub |
| Markdown | .md |
| Text | .txt |
| RTF | .rtf |

### Using the wrapper script

```bash
python scripts/markitdown_convert.py input.pdf
python scripts/markitdown_convert.py input.docx -o output.md
python scripts/markitdown_convert.py input.pdf --clip
python scripts/markitdown_convert.py . --all
```

## Python API

```python
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert_local("input.pdf")
print(result.text_content)
```
