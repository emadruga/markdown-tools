#!/usr/bin/env python3
"""
Markdown to PDF Converter (Chrome-based with full emoji support)

Uses Playwright (Chromium) for perfect emoji and Unicode rendering.

This script automatically fixes common markdown formatting inconsistencies:
- Corrects table of contents links that don't match heading anchors
- Handles headings with periods (e.g., "1. Introduction")
- Fixes double-dashes in links (e.g., #section--name -> #section-name)
- Adds explicit anchor IDs to ensure links work in the final PDF

The original markdown file is never modified - all corrections are done
in a temporary file that is automatically cleaned up after conversion.

Requires: pip install markdown playwright
Then run: playwright install chromium
"""

import argparse
import sys
from pathlib import Path
import asyncio
import re
import tempfile

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Error: playwright is not installed.", file=sys.stderr)
    print("Install with: pip install playwright", file=sys.stderr)
    print("Then run: playwright install chromium", file=sys.stderr)
    sys.exit(1)

try:
    import pypandoc
except ImportError:
    print("Error: pypandoc is not installed.", file=sys.stderr)
    print("Install with: pip install pypandoc", file=sys.stderr)
    sys.exit(1)


def generate_pandoc_anchor(heading_text: str) -> str:
    """
    Generate an anchor ID exactly as pandoc does.

    Pandoc's rules:
    1. Convert to lowercase
    2. Remove punctuation (except hyphens and underscores)
    3. Replace spaces with hyphens
    4. Remove leading/trailing hyphens

    Args:
        heading_text: The heading text

    Returns:
        The anchor ID that pandoc will generate
    """
    anchor = heading_text.lower()

    # Remove backticks and their content (code spans)
    anchor = re.sub(r'`[^`]*`', '', anchor)

    # Remove all punctuation except spaces, hyphens, and underscores
    # Keep alphanumeric, spaces, hyphens, and underscores
    anchor = re.sub(r'[^\w\s-]', '', anchor)

    # Replace one or more spaces with a single hyphen
    anchor = re.sub(r'\s+', '-', anchor)

    # Collapse multiple hyphens into one
    anchor = re.sub(r'-+', '-', anchor)

    # Remove leading and trailing hyphens
    anchor = anchor.strip('-')

    return anchor


def normalize_heading_anchors(content: str) -> str:
    """
    Normalize heading anchors in markdown content to match the actual headings.

    This function:
    1. Adds explicit anchor IDs to headings using pandoc's {#id} syntax
    2. Fixes TOC links to match those explicit IDs

    Args:
        content: The markdown file content as a string

    Returns:
        The normalized markdown content with explicit anchors and corrected TOC links
    """
    # Extract all headings from the content
    heading_pattern = re.compile(r'^(#{1,6})\s+(.+?)(?:\s*\{#[^}]+\})?\s*$', re.MULTILINE)
    headings = {}
    heading_positions = []

    for match in heading_pattern.finditer(content):
        level = match.group(1)
        heading_text = match.group(2).strip()

        # Generate the anchor exactly as pandoc would
        anchor = generate_pandoc_anchor(heading_text)

        headings[heading_text] = anchor
        heading_positions.append((match.start(), match.end(), level, heading_text, anchor))

    # First pass: Add explicit anchor IDs to headings
    # Process in reverse order to maintain string positions
    modified_content = content
    for start, end, level, heading_text, anchor in reversed(heading_positions):
        original_heading = modified_content[start:end]

        # Check if heading already has an explicit ID
        if not re.search(r'\{#[^}]+\}', original_heading):
            # Add explicit anchor ID
            new_heading = f"{level} {heading_text} {{#{anchor}}}"
            modified_content = modified_content[:start] + new_heading + modified_content[end:]
            print(f"  Adding anchor to heading: {heading_text} -> {{#{anchor}}}")

    # Second pass: Fix TOC links
    # Pattern to match markdown links like [text](#anchor)
    link_pattern = re.compile(r'\[([^\]]+)\]\(#([^\)]+)\)')

    def replace_link(match):
        link_text = match.group(1)
        old_anchor = match.group(2)

        # Try to find a heading that matches this link text
        # Remove leading numbering from link text for comparison
        clean_link_text = re.sub(r'^\d+[\.\)]\s*', '', link_text)

        # Look for a heading that starts with similar numbering or exact text match
        best_match = None
        for heading_text, correct_anchor in headings.items():
            # Try exact match after removing numbers from both
            heading_clean = re.sub(r'^\d+[\.\)]\s*', '', heading_text)

            # Check for exact match (case-insensitive)
            if clean_link_text.lower() == heading_clean.lower():
                best_match = (heading_text, correct_anchor)
                break

            # Fallback: check if heading contains the link text
            if clean_link_text.lower() in heading_text.lower():
                if best_match is None:
                    best_match = (heading_text, correct_anchor)

        if best_match:
            heading_text, correct_anchor = best_match
            if old_anchor != correct_anchor:
                print(f"  Fixing TOC link: #{old_anchor} -> #{correct_anchor}")
            return f'[{link_text}](#{correct_anchor})'

        # If no match found, keep original
        print(f"  Warning: No heading found for TOC link: [{link_text}](#{old_anchor})")
        return match.group(0)

    normalized_content = link_pattern.sub(replace_link, modified_content)
    return normalized_content


async def convert_markdown_to_pdf_async(input_path: str) -> None:
    """
    Convert markdown to PDF using Chrome rendering.

    This function automatically fixes inconsistencies in TOC links by creating
    a temporary normalized markdown file, without modifying the original.
    """
    input_file = Path(input_path).resolve()

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    if input_file.suffix.lower() not in ['.md', '.markdown']:
        raise ValueError(f"Input file must be a markdown file (.md or .markdown): {input_file}")

    output_file = input_file.with_suffix('.pdf')

    print(f"Reading markdown file: {input_file}")
    original_content = input_file.read_text(encoding='utf-8')

    # Normalize the markdown content to fix TOC links
    print(f"Normalizing TOC links...")
    markdown_text = normalize_heading_anchors(original_content)

    # Preprocess: ensure blank lines before lists for proper parsing
    import re
    # Add blank line before lines starting with '- ' if not already preceded by blank line
    lines = markdown_text.split('\n')
    processed_lines = []
    for i, line in enumerate(lines):
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            # Check if previous line is not blank and not a list item
            if i > 0 and lines[i-1].strip() and not (lines[i-1].strip().startswith('- ') or lines[i-1].strip().startswith('* ')):
                processed_lines.append('')  # Add blank line
        processed_lines.append(line)

    markdown_text = '\n'.join(processed_lines)

    print("Converting markdown to HTML...")
    # Use pypandoc to convert markdown to HTML (preserves list structure better)
    html_content = pypandoc.convert_text(
        markdown_text,
        'html',
        format='markdown'
    )

    # Create styled HTML with emoji support
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            h1, h2, h3, h4, h5, h6 {{
                margin-top: 24px;
                margin-bottom: 16px;
                font-weight: 600;
                line-height: 1.25;
            }}
            h1 {{
                font-size: 2em;
                border-bottom: 1px solid #eaecef;
                padding-bottom: 0.3em;
            }}
            h2 {{
                font-size: 1.5em;
                border-bottom: 1px solid #eaecef;
                padding-bottom: 0.3em;
            }}
            code {{
                background-color: #f6f8fa;
                padding: 0.2em 0.4em;
                border-radius: 3px;
                font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
                font-size: 0.9em;
            }}
            pre {{
                background-color: #f6f8fa;
                padding: 16px;
                border-radius: 3px;
                overflow-x: auto;
                white-space: pre;
            }}
            pre code {{
                background-color: transparent;
                padding: 0;
                font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 16px 0;
                table-layout: auto;
            }}
            table th, table td {{
                border: 1px solid #dfe2e5;
                padding: 6px 13px;
                word-wrap: break-word;
                overflow-wrap: break-word;
            }}
            table th {{
                background-color: #f6f8fa;
                font-weight: 600;
            }}
            /* First column should be narrow and not wrap unless necessary */
            table td:first-child, table th:first-child {{
                white-space: nowrap;
                width: 1%;
            }}
            /* Description/content columns should wrap and take available space */
            table td:not(:first-child), table th:not(:first-child) {{
                width: auto;
            }}
            blockquote {{
                margin: 0;
                padding: 0 1em;
                color: #6a737d;
                border-left: 0.25em solid #dfe2e5;
            }}
            img {{
                max-width: 100%;
            }}
            ul, ol {{
                margin: 16px 0;
                padding-left: 2em;
            }}
            li {{
                margin: 4px 0;
                display: list-item;
            }}
            ul li {{
                list-style-type: disc;
            }}
            ol li {{
                list-style-type: decimal;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    print(f"Generating PDF: {output_file}")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(styled_html)

        await page.pdf(
            path=str(output_file),
            format='Letter',
            margin={
                'top': '1in',
                'right': '1in',
                'bottom': '1in',
                'left': '1in'
            },
            print_background=True,
            display_header_footer=True,
            header_template='<div></div>',
            footer_template='<div style="font-size: 10pt; text-align: center; width: 100%; color: #666; margin-top: 20px;"><span class="pageNumber"></span></div>'
        )

        await browser.close()

    print(f"Successfully converted to PDF: {output_file}")


def convert_markdown_to_pdf(input_path: str) -> None:
    """Synchronous wrapper for async conversion."""
    asyncio.run(convert_markdown_to_pdf_async(input_path))


def main():
    parser = argparse.ArgumentParser(
        description='Convert markdown files to PDF with full emoji support (Chrome-based).',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s /path/to/document.md
  %(prog)s ~/Documents/README.md

Requirements:
  pip install playwright markdown
  playwright install chromium
        """
    )

    parser.add_argument(
        'input_file',
        type=str,
        help='Full path to the input markdown file'
    )

    args = parser.parse_args()

    try:
        convert_markdown_to_pdf(args.input_file)
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
