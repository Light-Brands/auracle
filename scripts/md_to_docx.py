#!/usr/bin/env python3
"""
Convert a markdown manuscript to .docx for Atticus import.

Atticus works best with .docx files that use proper Word heading styles:
- Heading 1 → Chapter titles (Atticus auto-detects chapter breaks)
- Heading 2 → Section headings
- Heading 3 → Subsections
- Normal → Body text
- Block quotes, bold, italic preserved

Usage:
    python3 scripts/md_to_docx.py <input.md> [output.docx]
"""

import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH


def parse_markdown_to_blocks(md_text: str) -> list[dict]:
    """Parse markdown into structured blocks for docx generation."""
    blocks = []
    lines = md_text.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            i += 1
            continue

        # Horizontal rule (page/section break marker)
        if re.match(r"^---+$", stripped):
            blocks.append({"type": "hr"})
            i += 1
            continue

        # Headings
        heading_match = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            blocks.append({"type": "heading", "level": level, "text": text})
            i += 1
            continue

        # Blockquote (may span multiple lines)
        if stripped.startswith(">"):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_text = re.sub(r"^>\s*", "", lines[i].strip())
                quote_lines.append(quote_text)
                i += 1
            blocks.append({"type": "blockquote", "text": "\n".join(quote_lines)})
            continue

        # Unordered list item
        list_match = re.match(r"^[-*]\s+(.+)$", stripped)
        if list_match:
            list_items = []
            while i < len(lines):
                item_match = re.match(r"^[-*]\s+(.+)$", lines[i].strip())
                if item_match:
                    list_items.append(item_match.group(1))
                    i += 1
                elif lines[i].strip() == "":
                    i += 1
                    # Check if next non-empty line is also a list item
                    peek = i
                    while peek < len(lines) and lines[peek].strip() == "":
                        peek += 1
                    if peek < len(lines) and re.match(r"^[-*]\s+", lines[peek].strip()):
                        continue
                    else:
                        break
                else:
                    break
            blocks.append({"type": "list", "items": list_items})
            continue

        # Ordered list item
        olist_match = re.match(r"^\d+[.)]\s+(.+)$", stripped)
        if olist_match:
            list_items = []
            while i < len(lines):
                item_match = re.match(r"^\d+[.)]\s+(.+)$", lines[i].strip())
                if item_match:
                    list_items.append(item_match.group(1))
                    i += 1
                elif lines[i].strip() == "":
                    i += 1
                    peek = i
                    while peek < len(lines) and lines[peek].strip() == "":
                        peek += 1
                    if peek < len(lines) and re.match(r"^\d+[.)]\s+", lines[peek].strip()):
                        continue
                    else:
                        break
                else:
                    break
            blocks.append({"type": "ordered_list", "items": list_items})
            continue

        # Regular paragraph (collect consecutive non-empty lines)
        para_lines = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,6}\s|[-*]\s|>\s|---+$|\d+[.)]\s)", lines[i].strip()):
            para_lines.append(lines[i].strip())
            i += 1
        if para_lines:
            blocks.append({"type": "paragraph", "text": " ".join(para_lines)})
            continue

        # Fallback
        i += 1

    return blocks


def add_formatted_text(paragraph, text: str):
    """Add text with inline markdown formatting (bold, italic) to a paragraph."""
    # Process inline formatting: bold+italic, bold, italic
    # Pattern order matters: bold-italic first, then bold, then italic
    pattern = re.compile(
        r"(\*\*\*(.+?)\*\*\*)"   # bold+italic
        r"|(\*\*(.+?)\*\*)"      # bold
        r"|(\*(.+?)\*)"          # italic
        r"|(_(.+?)_)"            # italic with underscores
    )

    pos = 0
    for match in pattern.finditer(text):
        # Add text before the match as plain
        if match.start() > pos:
            plain = text[pos:match.start()]
            paragraph.add_run(plain)

        if match.group(2):  # bold+italic
            run = paragraph.add_run(match.group(2))
            run.bold = True
            run.italic = True
        elif match.group(4):  # bold
            run = paragraph.add_run(match.group(4))
            run.bold = True
        elif match.group(6):  # italic
            run = paragraph.add_run(match.group(6))
            run.italic = True
        elif match.group(8):  # italic underscore
            run = paragraph.add_run(match.group(8))
            run.italic = True

        pos = match.end()

    # Add remaining text
    if pos < len(text):
        paragraph.add_run(text[pos:])


def create_docx(blocks: list[dict], output_path: str, title: str, author: str):
    """Create a .docx from parsed blocks, optimized for Atticus import."""
    doc = Document()

    # Set default font
    style = doc.styles["Normal"]
    font = style.font
    font.name = "Times New Roman"
    font.size = Pt(12)

    # Configure heading styles for Atticus
    for level in range(1, 4):
        heading_style = doc.styles[f"Heading {level}"]
        heading_style.font.name = "Times New Roman"
        heading_style.font.color.rgb = RGBColor(0, 0, 0)
        if level == 1:
            heading_style.font.size = Pt(24)
            heading_style.font.bold = True
        elif level == 2:
            heading_style.font.size = Pt(18)
            heading_style.font.bold = True
        elif level == 3:
            heading_style.font.size = Pt(14)
            heading_style.font.bold = True

    for block in blocks:
        btype = block["type"]

        if btype == "heading":
            level = min(block["level"], 3)  # Atticus uses H1-H3
            text = block["text"]
            p = doc.add_heading(level=level)
            add_formatted_text(p, text)

        elif btype == "paragraph":
            p = doc.add_paragraph()
            add_formatted_text(p, block["text"])

        elif btype == "blockquote":
            p = doc.add_paragraph()
            p.style = doc.styles["Normal"]
            pf = p.paragraph_format
            pf.left_indent = Inches(0.5)
            pf.right_indent = Inches(0.5)
            add_formatted_text(p, block["text"])
            # Make blockquotes italic for visual distinction
            for run in p.runs:
                run.italic = True

        elif btype == "list":
            for item in block["items"]:
                p = doc.add_paragraph(style="List Bullet")
                add_formatted_text(p, item)

        elif btype == "ordered_list":
            for item in block["items"]:
                p = doc.add_paragraph(style="List Number")
                add_formatted_text(p, item)

        elif btype == "hr":
            # Atticus uses H1 headings as chapter breaks, so HRs can be
            # rendered as a subtle centered separator
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run("* * *")
            run.font.size = Pt(12)

    # Set document metadata
    doc.core_properties.title = title
    doc.core_properties.author = author

    doc.save(output_path)
    print(f"Created: {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_docx.py <input.md> [output.docx]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Error: {input_path} not found")
        sys.exit(1)

    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = str(input_path.with_suffix(".docx"))

    md_text = input_path.read_text(encoding="utf-8")

    # Extract title from first H1
    title_match = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    title = title_match.group(1) if title_match else "Manuscript"

    # Extract author from copyright line
    author_match = re.search(r"Copyright.*?by\s+(.+?)$", md_text, re.MULTILINE)
    author = author_match.group(1) if author_match else "Unknown"

    blocks = parse_markdown_to_blocks(md_text)
    create_docx(blocks, output_path, title, author)


if __name__ == "__main__":
    main()
