# Book Formatting Guide

## Preparing Your Manuscripts for Amazon KDP and Gumroad

---

## Overview

This guide covers formatting your markdown manuscripts for:
1. **Amazon KDP** - EPUB/MOBI for Kindle, PDF for paperback
2. **Gumroad** - PDF for direct download

---

## File Structure

### Volume 1: You Are Not Crazy

```
vol-1-not-crazy/
├── 00-front-matter.md
├── chapters/
│   ├── 01-opening-manifesto.md
│   ├── 02-energetic-signature.md
│   ├── 03-narcissist-playbook.md
│   ├── 04-trauma-bonds.md
│   ├── 05-narcissist-archetypes.md
│   ├── 06-family-systems.md
│   ├── 07-manipulation-in-relationships.md
│   ├── 08-decoder-cards.md
│   ├── 09-energetic-remapping.md
│   ├── 10-practical-responses.md
│   └── 11-moving-forward.md
└── appendices/
    ├── appendix-a-content-creation.md
    └── appendix-b-childhood-patterns.md
```

### Volume 2: You Are Not Stuck

```
vol-2-not-stuck/
├── 00-front-matter.md
├── chapters/
│   ├── 01-opening-manifesto.md
│   ├── 02-authors-note.md
│   ├── ... (chapters 03-22)
│   └── 22-relationships-reorganized.md
└── appendices/
    ├── appendix-a-grief-process.md
    ├── appendix-b-vignettes.md
    └── appendix-c-worksheets.md
```

---

## Formatting Tools: Recommendations

Choose based on your comfort level and budget. All produce professional results.

---

### Best for Most Authors: Atticus ($147 one-time)

**Why it's recommended:**
- Modern, intuitive interface designed for self-publishers
- Works on Mac, Windows, and web browser
- Beautiful pre-made templates
- Export to EPUB, PDF, and print-ready files
- One-time purchase, no subscription
- Excellent customer support and tutorials

**Best for:** Authors who want professional results without learning technical tools.

**Get it:** [atticus.io](https://www.atticus.io)

---

### Premium Option: Vellum ($250 one-time, Mac only)

**Why it's great:**
- Industry standard for indie publishers
- Stunning output with minimal effort
- Best-in-class ebook formatting
- One-click export to all formats
- Regular updates with new features

**Best for:** Mac users willing to invest in the best tool available.

**Limitation:** Mac-only (no Windows version).

**Get it:** [vellum.pub](https://vellum.pub)

---

### Free Option: Kindle Create (Free)

**Why consider it:**
- Free, made by Amazon
- Guaranteed KDP compatibility
- Theme templates included
- Easy chapter detection

**Limitations:**
- Amazon-focused (less ideal for Gumroad PDF)
- Fewer customization options
- Less polished than paid tools

**Best for:** Budget-conscious authors publishing primarily on Amazon.

**Get it:** [Amazon Kindle Create](https://www.amazon.com/Kindle-Create)

---

### Technical/Free Options

For authors comfortable with command-line tools or who need maximum flexibility:

## Conversion Tools (Free)

### Option 1: Pandoc (Recommended for technical users)

**Install:**
```bash
# macOS
brew install pandoc

# Or download from pandoc.org
```

**Convert Markdown to EPUB:**
```bash
# Single file
pandoc input.md -o output.epub --toc --toc-depth=2

# Multiple files (Vol 1)
pandoc \
  vol-1-not-crazy/00-front-matter.md \
  vol-1-not-crazy/chapters/*.md \
  vol-1-not-crazy/appendices/*.md \
  -o narcissism-decoder.epub \
  --toc \
  --toc-depth=2 \
  --metadata title="You Are Not Crazy" \
  --metadata author="Jennifer Brooke Lawless" \
  --epub-cover-image=cover.jpg
```

**Convert to PDF:**
```bash
pandoc input.md -o output.pdf --pdf-engine=wkhtmltopdf
```

### Option 2: Calibre (GUI-based, user-friendly)

1. Download from [calibre-ebook.com](https://calibre-ebook.com)
2. Import your markdown or Word document
3. Convert to EPUB, MOBI, or PDF
4. Edit metadata (title, author, description)
5. Add cover image

### Option 3: Google Docs → Word → KDP

1. Paste markdown into Google Docs
2. Format with Styles (Heading 1, Heading 2, etc.)
3. Download as .docx
4. Upload directly to KDP (they convert automatically)

### Option 4: Reedsy Book Editor (Free, online)

1. Go to [reedsy.com/write-a-book](https://reedsy.com/write-a-book)
2. Create account
3. Paste chapters
4. Export as EPUB or PDF
5. Professional formatting included

---

## Tool Comparison Summary

| Tool | Cost | Platforms | Best For |
|------|------|-----------|----------|
| **Atticus** | $147 | Mac, Windows, Web | Most authors (recommended) |
| **Vellum** | $250 | Mac only | Premium output, Mac users |
| **Kindle Create** | Free | Mac, Windows | Amazon-only publishing |
| **Pandoc** | Free | All (command line) | Technical users |
| **Calibre** | Free | All (GUI) | Format conversion |
| **Reedsy Editor** | Free | Web | Simple books, beginners |

**Jennifer's Recommendation:** Start with Atticus. The $147 investment pays for itself in time saved and professional output. If you're on Mac and want the absolute best, Vellum is worth it.

---

## Required Elements

### Front Matter (DO NOT SKIP — these pages sell the series)

1. **Title Page**
   - Book title
   - Subtitle
   - Author name

2. **Copyright Page**
   ```
   © [Year] Jennifer Brooke Lawless
   All rights reserved.

   No part of this publication may be reproduced, distributed, or
   transmitted in any form without the prior written permission
   of the author.

   This book is not intended as a substitute for professional
   mental health treatment. If you are in crisis, please contact
   a mental health professional or crisis hotline.

   Published by KDP Amazon
   ISBN: [Amazon free ISBN for paperback — leave blank for ebook]

   First Edition
   ```

3. **Series Page** (Critical — include in every volume)
   ```
   THE SOVEREIGNTY SERIES

   Volume 1: You Are Not Crazy — You Are Not Crazy
   Volume 2: You Are Not Stuck — Healing Through Secure Attachment
   Volume 3: You Are Not Small — Internal Authority and Self-Trust
   Volume 4: You Are Not Gone — Living from Full Presence
   Volume 5: You Are Not Repeating — Conscious Parenting
   Volume 6: You Are Not Too Much — Serving Others
   Volume 7: You Are Not Behind — Thriving Beyond Survival
   Volume 8: You Were Never Broken — Becoming Who You Always Were
   ```

4. **Dedication** (optional)

5. **Table of Contents** (auto-generated by most tools — must be clickable for ebook)

### Back Matter (DO NOT SKIP — this is where nonfiction series win)

1. **About the Author** (use bio from `07-author-bio-versions.md`)

2. **What's Coming in the Next Volume** (this sells read-through)
   ```
   COMING NEXT: THE BRIDGE (Volume 2)

   You can name the tactics. You see the patterns. And yet your
   nervous system still reacts.

   The Bridge closes the gap between insight and embodiment.
   Learn why awareness alone doesn't heal, how childhood roles
   shape adult attraction, and how to retrain your nervous system
   for secure attachment. Includes a 12-week training program.

   Stop surviving connection. Start feeling safe in it.
   ```

3. **Call-to-Action Block** (every volume)
   ```
   CONTINUE YOUR JOURNEY

   📧 Newsletter: [Substack URL]
   Weekly insights on recognizing manipulation, healing attachment,
   and building sovereignty.

   🎴 Free Decoder Cards: [Gumroad URL]
   Quick-reference guide for real-time pattern recognition.

   📚 Series Bundles: [Gumroad URL]
   Save 15-25% on multi-volume bundles.
   ```

4. **Review Request**
   ```
   DID THIS BOOK HELP?

   If this book gave you clarity, language, or courage, please
   consider leaving a review on Amazon. Reviews help other readers
   find this book — and every review helps someone else realize
   they're not crazy either.
   ```

5. **Resources**
   - Crisis hotlines (already in Appendix A)
   - Recommended reading
   - Author website/newsletter

---

## Paperback Formatting (6" x 9")

### Interior Specs

| Setting | Value |
|---------|-------|
| **Trim Size** | 6" x 9" (most common for nonfiction) |
| **Interior Color** | Black & white (unless visuals matter) |
| **Paper Type** | White paper (cream optional for literary feel) |
| **Bleed** | No bleed (text-only interior) |

### Margins (KDP Minimum Requirements for 6x9)

Use the [KDP Margin Calculator](https://kdp.amazon.com/en_US/help/topic/G201834180) for exact values based on page count. General guidelines:

| Margin | Minimum |
|--------|---------|
| **Outside (right on recto, left on verso)** | 0.25" |
| **Top** | 0.25" |
| **Bottom** | 0.25" |
| **Inside (gutter)** | Varies by page count — typically 0.375"–0.875" |

### Print-Ready PDF Export

- Export as PDF/X-1a (print standard) or high-quality print PDF
- Embed all fonts
- No crop marks or printer's marks
- Verify page count is even (add blank page at end if needed)

### Paperback Cover

- Use [KDP Cover Calculator](https://kdp.amazon.com/en_US/cover-calculator) — input trim size, page count, and paper type
- Calculator generates a template with exact spine width
- **Spine text:** Include book title + author name (required if spine width > 0.5")
- **Back cover:** Include description, barcode area (Amazon adds ISBN barcode automatically), and author bio
- **Format:** PDF, 300 DPI minimum

---

## Cover Requirements

### Amazon KDP Ebook

- **Dimensions:** 2560 x 1600 pixels (1.6:1 ratio)
- **Format:** JPEG or TIFF
- **Resolution:** 300 DPI minimum
- **File size:** Under 50MB

### Amazon KDP Paperback

- Depends on page count and trim size
- Use KDP Cover Calculator: [kdp.amazon.com/cover-calculator](https://kdp.amazon.com/en_US/cover-calculator)
- Include spine width based on page count

### Gumroad

- **Recommended:** 1280 x 720 pixels or larger
- **Format:** JPEG, PNG, or GIF
- **Aspect ratio:** 16:9 works well

### Cover Design Options (Budget-friendly)

1. **Canva** - Free templates, easy to use
2. **Book Brush** - Free book cover templates
3. **99designs** - $299+ for custom professional cover
4. **Fiverr** - $20-100 for decent covers
5. **Reedsy Marketplace** - Professional designers

**Cover Tips:**
- Simple, readable at thumbnail size
- High contrast text
- Genre-appropriate design
- Your name clearly visible

---

## ISBN Strategy

| Format | ISBN Needed? | Approach |
|--------|-------------|----------|
| **Kindle eBook** | No | Amazon assigns ASIN automatically |
| **Paperback (Vol 1)** | Yes | Use Amazon's free ISBN — fast, free, zero downside |
| **Paperback (Vol 2+)** | Yes | Continue with Amazon's free ISBN, or buy your own from Bowker ($295 for 10) if you want imprint control |
| **Gumroad (all)** | No | Direct download, not a catalogued publication |

**When to buy your own ISBNs:** When the series proves traction and you want to list yourself (or your imprint) as publisher instead of Amazon. You can re-issue earlier books with new ISBNs later. Most nonfiction series never need this step.

---

## Formatting Checklist

### Before Conversion

- [ ] All chapters in correct order
- [ ] Consistent heading hierarchy (# for chapters, ## for sections)
- [ ] All links working (or removed for print)
- [ ] Front matter complete
- [ ] Back matter complete with calls-to-action
- [ ] Crisis resources included
- [ ] Spelling and grammar checked

### After Conversion

- [ ] Table of contents links work
- [ ] Chapter breaks appear correctly
- [ ] Special characters display properly
- [ ] Cover image displays correctly
- [ ] Test on Kindle Previewer (free from Amazon)

---

## Upload Checklist

### Amazon KDP — Paperback (Publish This FIRST)

1. [ ] Log in to kdp.amazon.com
2. [ ] Click "Create New Title" → **"Paperback"**
3. [ ] Enter book details:
   - [ ] Title and subtitle (consistent format — see `01-platform-setup-guide.md`)
   - [ ] Series name: `You Are Not Smallty Series` + volume number
   - [ ] Author name
   - [ ] Description (from `03-book-descriptions.md`)
   - [ ] Keywords (7 boxes — see optimized strategy in `03-book-descriptions.md`)
   - [ ] Categories (2)
4. [ ] ISBN: Select "Get a free KDP ISBN"
5. [ ] Upload print-ready interior PDF (6x9, black & white)
6. [ ] Upload full cover PDF (with spine — use KDP Cover Calculator)
7. [ ] Use KDP Print Previewer to verify formatting
8. [ ] Set pricing:
   - [ ] Vol 1 Paperback: $14.99
   - [ ] Territory: All territories
9. [ ] Publish (takes 24-72 hours to go live)

### Amazon KDP — Kindle eBook (Publish AFTER Paperback)

1. [ ] Click "Create New Title" → **"Kindle eBook"**
2. [ ] Enter book details (same title, subtitle, series, description, keywords, categories)
3. [ ] Upload manuscript (EPUB or DOCX)
4. [ ] Upload ebook cover (2560 x 1600 pixels)
5. [ ] Preview in Kindle Previewer
6. [ ] Set pricing:
   - [ ] Vol 1 Ebook: $2.99–$4.99 (70% royalty — lower price hooks readers into series)
   - [ ] Territory: All territories
7. [ ] Publish — Amazon automatically links ebook + paperback formats
8. [ ] After both are live: Enable Series page, add A+ Content

### Gumroad

1. [ ] Log in to gumroad.com
2. [ ] Click "New Product"
3. [ ] Product type: Digital product
4. [ ] Upload PDF file
5. [ ] Add cover image
6. [ ] Write description
7. [ ] Set price
8. [ ] Enable email collection
9. [ ] Set custom URL
10. [ ] Publish

---

## Quality Assurance

### Test Your Ebook

1. **Kindle Previewer** (free)
   - Download from Amazon
   - Open your EPUB/MOBI
   - Check on different device simulations

2. **Send to Kindle App**
   - Email file to your Kindle email address
   - Test on actual device

3. **Calibre Viewer**
   - Open in Calibre
   - Check formatting

### Common Issues to Check

- [ ] Images display correctly
- [ ] Tables are readable
- [ ] Blockquotes formatted properly
- [ ] No orphaned headers (heading at bottom of page)
- [ ] Links are clickable
- [ ] Font size readable

---

## Recommended Workflow

### Week 1: Prepare Files

1. Combine all chapter files in order
2. Add front matter and back matter
3. Proofread entire manuscript
4. Design or commission cover

### Week 2: Convert and Test

1. Convert to EPUB using Pandoc or Calibre
2. Test in Kindle Previewer
3. Make corrections
4. Convert to PDF for Gumroad
5. Test PDF on different devices

### Week 3: Upload and Publish

1. Upload to Amazon KDP
2. Preview and approve
3. Upload to Gumroad
4. Test purchase flow on Gumroad
5. Set up Decoder Cards as free lead magnet

---

## Quick Commands Reference

### Combine Markdown Files (macOS/Linux)

```bash
# Volume 1
cat vol-1-not-crazy/00-front-matter.md \
    vol-1-not-crazy/chapters/*.md \
    vol-1-not-crazy/appendices/*.md \
    > narcissism-decoder-complete.md

# Volume 2
cat vol-2-not-stuck/00-front-matter.md \
    vol-2-not-stuck/chapters/*.md \
    vol-2-not-stuck/appendices/*.md \
    > the-bridge-complete.md
```

### Convert with Pandoc

```bash
# To EPUB
pandoc narcissism-decoder-complete.md \
  -o narcissism-decoder.epub \
  --toc \
  --metadata title="You Are Not Crazy" \
  --metadata subtitle="Control Disguised as Care" \
  --metadata author="Jennifer Brooke Lawless" \
  --epub-cover-image=cover-vol1.jpg

# To PDF
pandoc narcissism-decoder-complete.md \
  -o narcissism-decoder.pdf \
  --pdf-engine=wkhtmltopdf \
  --metadata title="You Are Not Crazy"
```

---

## Next Steps

After formatting and uploading:
1. → Request reviews from friends/family (see launch sequence)
2. → Create content calendar (see `05-content-calendar.md`)
3. → Begin pre-launch content on social media

