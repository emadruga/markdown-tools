#!/usr/bin/env python3
"""
Markdown to DOCX Converter

A CLI tool that converts markdown files to Microsoft Word 365 compatible DOCX format.
The DOCX file is saved in the same directory as the input file.

This script automatically fixes common markdown formatting inconsistencies:
- Corrects table of contents links that don't match heading anchors
- Handles headings with periods (e.g., "1. Introduction")
- Fixes double-dashes in links (e.g., #section--name -> #section-name)
- Adds explicit anchor IDs to ensure links work in the final DOCX

The original markdown file is never modified - all corrections are done
in a temporary file that is automatically cleaned up after conversion.

This script uses pypandoc which requires pandoc to be installed.
Install pandoc:
  - macOS: brew install pandoc
  - Linux: sudo apt-get install pandoc
  - Windows: choco install pandoc
"""

import argparse
import sys
import re
import tempfile
from pathlib import Path

try:
    import pypandoc
except ImportError:
    print("Error: pypandoc is not installed. Install it with: pip install pypandoc", file=sys.stderr)
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


def convert_markdown_to_docx(input_path: str) -> None:
    """
    Convert a markdown file to DOCX using pandoc.

    This function automatically fixes inconsistencies in TOC links by creating
    a temporary normalized markdown file, without modifying the original.

    Args:
        input_path: Full path to the input markdown file

    Raises:
        FileNotFoundError: If the input file doesn't exist
        ValueError: If the input file is not a markdown file
        RuntimeError: If pandoc is not installed
    """
    # Validate input file
    input_file = Path(input_path).resolve()

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    if input_file.suffix.lower() not in ['.md', '.markdown']:
        raise ValueError(f"Input file must be a markdown file (.md or .markdown): {input_file}")

    # Generate output DOCX path
    output_file = input_file.with_suffix('.docx')

    # Read markdown content
    print(f"Reading markdown file: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # Normalize the markdown content to fix TOC links
    print(f"Normalizing TOC links...")
    normalized_content = normalize_heading_anchors(original_content)

    # Create a temporary file with normalized content
    temp_fd, temp_path = tempfile.mkstemp(suffix='.md', text=True)
    temp_file = Path(temp_path)

    try:
        # Write normalized content to temporary file
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(normalized_content)

        # Convert markdown to DOCX using pandoc
        print(f"Converting to DOCX: {output_file}")

        try:
            pypandoc.convert_file(
                str(temp_file),
                'docx',
                outputfile=str(output_file),
                extra_args=[
                    '--from=markdown+hard_line_breaks',  # Preserve line breaks and list formatting
                    '--to=docx',
                ]
            )
            print(f"Successfully converted to DOCX: {output_file}")
        except RuntimeError as e:
            if "pandoc" in str(e).lower():
                raise RuntimeError(
                    "pandoc is not installed or not found in PATH.\n"
                    "Install pandoc:\n"
                    "  - macOS: brew install pandoc\n"
                    "  - Linux: sudo apt-get install pandoc\n"
                    "  - Windows: choco install pandoc\n"
                    f"Original error: {e}"
                )
            raise
    finally:
        # Clean up temporary file
        import os
        try:
            os.close(temp_fd)
        except:
            pass
        if temp_file.exists():
            temp_file.unlink()
            print(f"Cleaned up temporary file")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Convert markdown files to Microsoft Word DOCX format.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s /path/to/document.md
  %(prog)s ~/Documents/README.md
        """
    )

    parser.add_argument(
        'input_file',
        type=str,
        help='Full path to the input markdown file'
    )

    args = parser.parse_args()

    try:
        convert_markdown_to_docx(args.input_file)
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
