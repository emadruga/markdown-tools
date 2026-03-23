# Markdown to PDF/DOCX Converter

A command-line tool suite that converts Markdown files to professionally formatted PDF or Microsoft Word DOCX documents with full Unicode support, including emojis and special characters.

## Three Converters Available

This tool suite includes **three converters** to suit different needs:

### Version 1: `markdown2pdf.py` (LaTeX-based) - Best for Professional Documents
- ✅ **Professional typography** - LaTeX quality typesetting
- ✅ **Excellent code formatting** - Beautiful syntax highlighting and code blocks
- ✅ **Box-drawing characters** - Perfect for ASCII diagrams (├, │, ─, etc.)
- ⚠️ **Limited emoji support** - Some emojis may not render
- 📦 **Requirements**: Pandoc, BasicTeX/LaTeX

**Use when**: You need professional-quality documents with code and diagrams, and don't need full emoji support.

### Version 2: `markdown2pdf_chrome.py` (Chrome-based) - Best for Emoji Support
- ✅ **Full emoji support** - Renders all emojis including color emojis (✅, ❌, ✨)
- ✅ **Modern rendering** - Uses Chromium browser engine
- ✅ **Page numbers** - Automatic page numbering at the bottom
- ✅ **Box-drawing characters** - Supports ASCII diagrams
- ✅ **Smart table layout** - Optimized column widths (narrow first column, wider content columns)
- ⚠️ **Larger dependency** - Requires Chromium download (~300MB)
- 📦 **Requirements**: Pandoc, Playwright (with Chromium)

**Use when**: You need full emoji rendering, page numbers, well-formatted tables, and modern web-based PDF output.

### Version 3: `markdown2docx.py` - Best for Microsoft Word
- ✅ **Word 365 compatible** - Native DOCX format for Microsoft Word
- ✅ **Editable output** - Continue editing in Word after conversion
- ✅ **Professional formatting** - Tables, headings, lists, code blocks
- ✅ **Automatic TOC link fixing** - Same intelligent formatting fixes as PDF versions
- ✅ **No special dependencies** - Only requires Pandoc (no LaTeX or Chromium)
- 📦 **Requirements**: Pandoc only

**Use when**: You need an editable Word document that can be further modified in Microsoft Word or Word 365.

## What They Do

All three converters take a Markdown (`.md` or `.markdown`) file as input and generate an output file (PDF or DOCX) in the same directory with the same filename. They preserve all Markdown formatting including:

- Headers and text formatting (bold, italic, etc.)
- Code blocks with proper formatting
- Tables
- Lists (ordered and unordered)
- Links and images
- Blockquotes
- Unicode characters and box-drawing symbols (→, ├, │, etc.)

## Prerequisites

### System Requirements

This tool requires the following to be installed on your system:

1. **Python 3.6+** (with pip)
2. **Pandoc** - Document converter
3. **BasicTeX/LaTeX** - PDF generation engine (includes XeLaTeX)

### Installing Prerequisites

#### macOS

```bash
# Install Pandoc
brew install pandoc

# Install BasicTeX (includes XeLaTeX)
brew install basictex

# Update PATH - add this to your ~/.zshrc
eval "$(/usr/libexec/path_helper)"

# Reload your shell configuration
source ~/.zshrc

# Update LaTeX package manager and install required packages
sudo tlmgr update --self
sudo tlmgr install framed fancyvrb
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install pandoc texlive-xetex texlive-latex-base texlive-fonts-recommended
```

#### Windows

```bash
# Using Chocolatey
choco install pandoc miktex
```

## Installation

### 1. Set Up Python Environment

It's recommended to use a dedicated conda environment:

```bash
# Create a new conda environment
conda create -n MARKDOWN_TOOLS python=3.12

# Activate the environment
conda activate MARKDOWN_TOOLS
```

### 2. Install Python Dependencies

#### For Version 1 (LaTeX-based) and Version 3 (DOCX):
```bash
cd /path/to/markdown2pdf
pip install -r requirements.txt
```

#### For Version 2 (Chrome-based):
```bash
cd /path/to/markdown2pdf
pip install pypandoc playwright
playwright install chromium
```

**Note:** Version 3 (DOCX) uses the same dependencies as Version 1, just `pypandoc`.

## Usage

### Version 1: LaTeX-based (markdown2pdf.py)

**IMPORTANT:** Always activate the conda environment before using the tool:

```bash
# Activate the environment
conda activate MARKDOWN_TOOLS

# Convert a markdown file
python markdown2pdf.py /path/to/your/file.md
```

**Examples:**
```bash
conda activate MARKDOWN_TOOLS

# Convert a README file
python markdown2pdf.py ~/Documents/README.md
# Output: ~/Documents/README.pdf

# Convert with relative path
python markdown2pdf.py ../metris/docs/WORKFLOW.md
# Output: ../metris/docs/WORKFLOW.pdf
```

### Version 2: Chrome-based (markdown2pdf_chrome.py)

**IMPORTANT:** Always activate the conda environment before using the tool:

```bash
# Activate the environment
conda activate MARKDOWN_TOOLS

# Convert a markdown file (with full emoji support and page numbers)
python markdown2pdf_chrome.py /path/to/your/file.md
```

**Examples:**
```bash
conda activate MARKDOWN_TOOLS

# Convert a file with emojis
python markdown2pdf_chrome.py ~/Documents/README.md
# Output: ~/Documents/README.pdf (with emojis and page numbers)

# Convert with relative path
python markdown2pdf_chrome.py ../metris/docs/WORKFLOW.md
# Output: ../metris/docs/WORKFLOW.pdf
```

### Version 3: DOCX (markdown2docx.py)

**IMPORTANT:** Always activate the conda environment before using the tool:

```bash
# Activate the environment
conda activate MARKDOWN_TOOLS

# Convert a markdown file to Word DOCX
python markdown2docx.py /path/to/your/file.md
```

**Examples:**
```bash
conda activate MARKDOWN_TOOLS

# Convert to editable Word document
python markdown2docx.py ~/Documents/README.md
# Output: ~/Documents/README.docx

# Convert with relative path
python markdown2docx.py ../metris/docs/WORKFLOW.md
# Output: ../metris/docs/WORKFLOW.docx
```

### Command-Line Options

```bash
# View help
python markdown2pdf.py --help

# Usage format
python markdown2pdf.py <input_file>
```

**Arguments:**
- `input_file` - Full or relative path to the markdown file (required)

## Features

### Automatic Markdown Formatting Fixes

**NEW:** Both `markdown2pdf.py` and `markdown2pdf_chrome.py` scripts now automatically detect and fix common markdown formatting inconsistencies **without modifying your original file**:

- **Table of Contents Link Correction**: Automatically fixes TOC links that don't match their target headings
- **Heading Format Normalization**: Handles headings with periods, numbers, and special characters (e.g., "1. Introduction", "Section / Subsection")
- **Double-Dash Correction**: Fixes incorrect double-dashes in anchor links (e.g., `#section--name` → `#section-name`)
- **Explicit Anchor IDs**: Adds pandoc-compatible `{#id}` attributes to ensure all internal links work correctly
- **Non-Destructive Processing**: All corrections happen in a temporary file that's automatically cleaned up

**How it works:**
1. Reads your original markdown file
2. Creates a temporary file with corrected formatting
3. Generates the PDF from the corrected version
4. Cleans up the temporary file
5. Your original markdown file remains **completely untouched**

**Example output:**
```
Reading markdown file: document.md
Normalizing TOC links...
  Adding anchor to heading: 1. Introduction -> {#1-introduction}
  Fixing TOC link: #section--name -> #section-name
  Fixing TOC link: #features--benefits -> #features-benefits
Converting to PDF: document.pdf
Successfully converted to PDF: document.pdf
Cleaned up temporary file
```

This feature is especially useful when working with markdown files generated by AI assistants or automated tools that may produce inconsistent heading and link formats.

### Supported Markdown Elements

- **Text Formatting**: Bold, italic, strikethrough, inline code
- **Headers**: H1 through H6
- **Lists**: Unordered (bullets) and ordered (numbered)
- **Code Blocks**: With language-specific syntax formatting
- **Tables**: Full table support with headers
- **Links**: Both inline and reference-style (now with automatic TOC link fixing!)
- **Images**: Embedded images (local or URLs)
- **Blockquotes**: Nested blockquotes supported
- **Horizontal Rules**: Section dividers
- **Unicode & Emojis**: Full support for ✅, ❌, →, ✨, etc.

### PDF Formatting

- **Margins**: 1 inch on all sides
- **Font Size**: 11pt body text
- **Font**: System default fonts with Unicode support
- **Page Size**: Letter (8.5" x 11")

### Table Formatting (Chrome Version)

The Chrome-based version (`markdown2pdf_chrome.py`) includes intelligent table layout optimization:

- **First column auto-sizing**: The first column is kept as narrow as possible without wrapping, ideal for labels, codes, or short identifiers
- **Content columns expand**: Remaining columns automatically use available space and wrap text naturally
- **No unnecessary wrapping**: Short text in narrow columns (like "E0X-avg") won't wrap unless absolutely necessary
- **Responsive layout**: Tables adapt to content while maintaining readability

**Example:**
```markdown
| Column    | Description                                    |
|-----------|------------------------------------------------|
| E0X       | Number of brand new flashcards added           |
| E0X-avg   | New flashcards per day available              |
```

Result: "E0X-avg" stays on one line, while the description column wraps if needed.

## Common Markdown Formatting Issues (Automatically Fixed!)

The script automatically handles these common markdown formatting problems:

### Issue 1: TOC Links Don't Match Headings

**Problem:**
```markdown
## Table of Contents
1. [Introduction](#1-introduction)
2. [Main Section](#2-main-section)

## 1. Introduction    ← Heading has a period after the number
...
## 2. Main Section    ← But the link doesn't account for it
```

**Solution:** The script automatically detects the heading format and corrects the anchor links to match.

### Issue 2: Double-Dashes in Anchor Links

**Problem:**
```markdown
## Table of Contents
1. [Features & Benefits](#1-features--benefits)  ← Double dash

## 1. Features & Benefits    ← Ampersand becomes single dash in anchor
```

**Solution:** The script normalizes the anchor generation to match pandoc's rules exactly.

### Issue 3: Special Characters in Headings

**Problem:**
```markdown
## Table of Contents
1. [Anki `revlog` Table](#anki-revlog-table)  ← Missing backticks in anchor

## Anki `revlog` Table    ← Heading has backticks
```

**Solution:** The script strips backticks and special characters when generating anchors, just like pandoc does.

### Issue 4: Slashes and Other Punctuation

**Problem:**
```markdown
[Section / Subsection](#section--subsection)  ← Slash becomes double-dash

## Section / Subsection    ← Original has slash
```

**Solution:** The script converts slashes and punctuation to single dashes in anchors.

### Why This Matters

When TOC links don't match their target headings, the links in the PDF won't work - they'll be dead links that don't navigate anywhere. This script ensures all your internal document links work perfectly, even if the markdown was generated by AI tools or other automated processes that may not follow consistent formatting rules.

**Remember:** Your original markdown file is never modified. All fixes happen in a temporary file during PDF generation.

## Troubleshooting

### Environment Issues

**Problem:** Command not found or import errors

**Solution:** Make sure you've activated the conda environment:
```bash
conda activate MARKDOWN_TOOLS
```

### "pandoc is not installed" Error

**Problem:** Script reports pandoc is missing

**Solution:** Install pandoc:
```bash
# macOS
brew install pandoc

# Linux
sudo apt-get install pandoc
```

### "xelatex not found" Error

**Problem:** LaTeX engine is missing or not in PATH

**Solution:**
```bash
# macOS - Install BasicTeX
brew install basictex

# Add to PATH (add to ~/.zshrc for persistence)
eval "$(/usr/libexec/path_helper)"
source ~/.zshrc

# Verify installation
which xelatex
```

### Unicode/Emoji Rendering Issues

**Problem:** Emojis or special characters don't appear in PDF

**Solution:** The script uses XeLaTeX which supports Unicode. If you still have issues:
1. Ensure you're using the latest version of the script (it should use `--pdf-engine=xelatex`)
2. Install additional fonts:
```bash
sudo tlmgr install collection-fontsrecommended
```

### Missing LaTeX Packages

**Problem:** Error about missing `.sty` files (like `framed.sty`)

**Solution:** Install the missing packages:
```bash
sudo tlmgr update --self
sudo tlmgr install framed fancyvrb
```

### Permission Errors

**Problem:** Can't write output PDF

**Solution:** Ensure you have write permissions in the target directory:
```bash
# Check permissions
ls -la /path/to/target/directory

# Fix permissions if needed
chmod 755 /path/to/target/directory
```

## Quick Start Guide

For first-time users, follow these steps:

```bash
# 1. Install system prerequisites
brew install pandoc basictex

# 2. Update PATH
echo 'eval "$(/usr/libexec/path_helper)"' >> ~/.zshrc
source ~/.zshrc

# 3. Install LaTeX packages
sudo tlmgr update --self
sudo tlmgr install framed fancyvrb

# 4. Create and activate conda environment
conda create -n MARKDOWN_TOOLS python=3.12
conda activate MARKDOWN_TOOLS

# 5. Install Python dependencies
cd /path/to/markdown2pdf
pip install -r requirements.txt

# 6. Test the tool
python markdown2pdf.py test.md

# 7. Verify the PDF was created
ls -lh test.pdf
```

## File Structure

```
markdown2pdf/
├── markdown2pdf.py           # Version 1: LaTeX-based converter (professional documents)
├── markdown2pdf_chrome.py    # Version 2: Chrome-based converter (emoji support + page numbers)
├── requirements.txt          # Python dependencies for Version 1
├── README.md                 # This file
└── test.md                   # Sample markdown file for testing
```

## Technical Notes

### Why These Technologies?

- **Pandoc**: Industry-standard document converter with excellent Markdown support
- **XeLaTeX**: Modern LaTeX engine with native Unicode support
- **pypandoc**: Simplifies Python-Pandoc integration

### Limitations

- Large files (>100MB) may take longer to process
- Some advanced LaTeX features may not be available
- Images must be accessible at conversion time (local files or URLs)

## License

MIT
