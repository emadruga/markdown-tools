# Markdown Tools — Quick Start

## Table of Contents

1. [Prerequisites & Installation](#1-prerequisites--installation)
   - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
   - [macOS](#macos)
   - [Python environment (all platforms)](#python-environment-all-platforms)
2. [Font Selection](#2-font-selection)
   - [Linux fonts](#linux-fonts)
   - [macOS fonts](#macos-fonts)
   - [How to change the font](#how-to-change-the-font)
3. [Usage Examples](#3-usage-examples)
   - [Version 1 — LaTeX PDF](#version-1--latex-pdf-markdown2pdfpy)
   - [Version 2 — Chrome PDF](#version-2--chrome-pdf-markdown2pdf_chromepy)
   - [Version 3 — DOCX](#version-3--docx-markdown2docxpy)
4. [Controlling Log Verbosity](#4-controlling-log-verbosity)

---

## 1. Prerequisites & Installation

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install pandoc \
    texlive-xetex \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-fonts-recommended
```

### macOS

```bash
# Install Pandoc and BasicTeX (includes xelatex)
brew install pandoc basictex

# Make the TeX binaries available in your shell
echo 'eval "$(/usr/libexec/path_helper)"' >> ~/.zshrc
source ~/.zshrc

# Install required LaTeX packages
sudo tlmgr update --self
sudo tlmgr install framed fancyvrb booktabs caption xcolor geometry
```

### Python environment (all platforms)

```bash
conda create -n MARKDOWN_TOOLS python=3.12
conda activate MARKDOWN_TOOLS

# Version 1 (LaTeX PDF) and Version 3 (DOCX)
pip install -r requirements.txt

# Version 2 (Chrome PDF) — adds Playwright on top
pip install pypandoc playwright
playwright install chromium
```

---

## 2. Font Selection

`markdown2pdf.py` passes font names directly to XeLaTeX via `--variable mainfont` and
`--variable monofont`. The font must be installed on the system and known to `fc-list`.

### Linux fonts

| Purpose   | Font name (pass to `--variable`) | Package to install |
|-----------|----------------------------------|--------------------|
| Serif (default) | `Latin Modern Roman` | included with `texlive-fonts-recommended` |
| Monospace (default) | `Latin Modern Mono` | included with `texlive-fonts-recommended` |
| Sans-serif body | `DejaVu Sans` | `fonts-dejavu` |
| Serif body | `DejaVu Serif` | `fonts-dejavu` |
| Monospace | `DejaVu Sans Mono` | `fonts-dejavu` |
| Liberation (MS-compatible) | `Liberation Serif` / `Liberation Mono` | `fonts-liberation` |
| Wide Unicode coverage | `Noto Sans` / `Noto Mono` | `fonts-noto` |

Install extra font packages:
```bash
sudo apt-get install fonts-dejavu fonts-liberation fonts-noto
```

### macOS fonts

| Purpose   | Font name (pass to `--variable`) | Notes |
|-----------|----------------------------------|-------|
| Serif (default) | `Latin Modern Roman` | Ships with BasicTeX |
| Monospace (default) | `Latin Modern Mono` | Ships with BasicTeX |
| System serif | `Georgia` | Built into macOS |
| System sans-serif | `Helvetica Neue` | Built into macOS |
| System monospace | `Menlo` | Built into macOS |
| System monospace (newer) | `SF Mono` | Built into macOS 10.12+ |
| Classic serif | `Times New Roman` | Built into macOS |
| Classic monospace | `Courier New` | Built into macOS |

### How to change the font

Edit the `extra_args` list in `markdown2pdf.py`:

```python
extra_args=[
    '--pdf-engine=xelatex',
    '--variable', 'geometry:margin=1in',
    '--variable', 'fontsize=11pt',
    '--variable', 'mainfont=DejaVu Serif',      # ← change body font here
    '--variable', 'monofont=DejaVu Sans Mono',  # ← change code font here
    ...
]
```

Verify a font name before using it:
```bash
fc-list | grep -i "dejavu serif"
```

---

## 3. Usage Examples

Always activate the environment first:
```bash
conda activate MARKDOWN_TOOLS
```

### Version 1 — LaTeX PDF (`markdown2pdf.py`)

Best for: professional documents, code blocks, ASCII diagrams.

```bash
# Basic conversion — output written next to the input file
python markdown2pdf.py README.md

# Absolute path
python markdown2pdf.py ~/Documents/report.md
# → ~/Documents/report.pdf

# Relative path from another directory
python markdown2pdf.py ../project/docs/WORKFLOW.md
# → ../project/docs/WORKFLOW.pdf

# Override font at runtime (Linux)
MAINFONT="DejaVu Serif" python markdown2pdf.py README.md

# Show every heading anchor being processed (DEBUG)
LOGLEVEL=DEBUG python markdown2pdf.py README.md

# Quiet run — only warnings appear (e.g. broken TOC links)
LOGLEVEL=WARNING python markdown2pdf.py README.md
```

### Version 2 — Chrome PDF (`markdown2pdf_chrome.py`)

Best for: full emoji support, page numbers, modern web-style layout.

```bash
# Basic conversion
python markdown2pdf_chrome.py README.md

# Absolute path
python markdown2pdf_chrome.py ~/Documents/notes.md
# → ~/Documents/notes.pdf

# Relative path
python markdown2pdf_chrome.py ../project/docs/WORKFLOW.md
# → ../project/docs/WORKFLOW.pdf

# Suppress INFO, show only TOC-fix warnings
LOGLEVEL=WARNING python markdown2pdf_chrome.py README.md

# Full debug output
LOGLEVEL=DEBUG python markdown2pdf_chrome.py README.md
```

> **Note:** First run downloads Chromium (~300 MB) if not already installed.
> Run `playwright install chromium` once to pre-download it.

### Version 3 — DOCX (`markdown2docx.py`)

Best for: editable Word documents; no LaTeX required.

```bash
# Basic conversion
python markdown2docx.py README.md
# → README.docx

# Absolute path
python markdown2docx.py ~/Documents/report.md
# → ~/Documents/report.docx

# Relative path
python markdown2docx.py ../project/docs/WORKFLOW.md
# → ../project/docs/WORKFLOW.docx

# Quiet (only TOC warnings)
LOGLEVEL=WARNING python markdown2docx.py README.md
```

---

## 4. Controlling Log Verbosity

All three scripts read the `LOGLEVEL` environment variable (default: `INFO`).

| `LOGLEVEL` | What you see |
|------------|-------------|
| `WARNING`  | Only markdown adjustments — TOC link fixes, unresolved anchors |
| `INFO`     | + one start line and one done line per run (default) |
| `DEBUG`    | + every heading anchor added to the document |

```bash
# Default
python markdown2pdf.py file.md
# INFO: Converting /abs/path/file.md -> /abs/path/file.pdf
# WARNING: Fixing TOC link: #features--benefits -> #features-benefits
# INFO: Done: /abs/path/file.pdf

# Silent unless something needs fixing
LOGLEVEL=WARNING python markdown2pdf.py file.md
# WARNING: Fixing TOC link: #features--benefits -> #features-benefits

# Verbose
LOGLEVEL=DEBUG python markdown2pdf.py file.md
# INFO: Converting ...
# DEBUG: Adding anchor to heading: Introduction -> {#introduction}
# DEBUG: Adding anchor to heading: Features & Benefits -> {#features-benefits}
# WARNING: Fixing TOC link: #features--benefits -> #features-benefits
# ...
# INFO: Done: ...
```
