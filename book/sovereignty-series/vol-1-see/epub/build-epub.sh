#!/usr/bin/env bash
#
# Build EPUB for Vol 1: See - The Truth That Was Hidden in Plain Sight
#
# Usage: bash build-epub.sh
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOOK_DIR="$(dirname "$SCRIPT_DIR")"
CHAPTERS_DIR="$BOOK_DIR/chapters"
APPENDICES_DIR="$BOOK_DIR/appendices"
OUTPUT_DIR="$SCRIPT_DIR"

METADATA="$SCRIPT_DIR/metadata.yaml"
CSS="$SCRIPT_DIR/epub-styles.css"
OUTPUT="$OUTPUT_DIR/see-vol-1.epub"

echo "=== Building EPUB: See ==="
echo "Book dir: $BOOK_DIR"
echo ""

# Define chapter order matching the Table of Contents
FILES=(
  # Front Matter
  "$BOOK_DIR/00-front-matter.md"

  # Part I: Recognition
  "$CHAPTERS_DIR/01-opening-manifesto.md"
  "$CHAPTERS_DIR/02-energetic-signature.md"
  "$CHAPTERS_DIR/03-decoder-playbook.md"
  "$CHAPTERS_DIR/pause-after-part-1.md"

  # Part II: Understanding Origins
  "$CHAPTERS_DIR/04-trauma-bonds.md"
  "$CHAPTERS_DIR/05-narcissist-types.md"
  "$CHAPTERS_DIR/06-narcissist-roles.md"
  "$CHAPTERS_DIR/07-family-roles-triangulation.md"
  "$CHAPTERS_DIR/08-parental-wounds.md"
  "$CHAPTERS_DIR/09-childhood-patterns.md"
  "$CHAPTERS_DIR/10-family-breaking-free.md"
  "$CHAPTERS_DIR/pause-after-part-2.md"

  # Part III: Patterns in Context
  "$CHAPTERS_DIR/11-romantic-manipulation.md"
  "$CHAPTERS_DIR/12-manipulation-across-contexts.md"
  "$CHAPTERS_DIR/13-exposure-questions.md"
  "$CHAPTERS_DIR/pause-after-part-3.md"

  # Part IV: Decoder Tools
  "$CHAPTERS_DIR/14-decoder-protocol.md"
  "$CHAPTERS_DIR/pause-after-part-4.md"

  # Part V: Recovery & Response
  "$CHAPTERS_DIR/15-energetic-remapping.md"
  "$CHAPTERS_DIR/16-practical-responses.md"
  "$CHAPTERS_DIR/17-moving-forward.md"

  # Appendices
  "$APPENDICES_DIR/appendix-a-resources.md"
  "$APPENDICES_DIR/appendix-b-glossary.md"
  "$APPENDICES_DIR/appendix-c-bibliography.md"
  "$APPENDICES_DIR/appendix-d-core-techniques.md"
  "$APPENDICES_DIR/appendix-e-index.md"
  "$APPENDICES_DIR/appendix-f-substance-patterns.md"

  # Back Matter
  "$BOOK_DIR/back-matter-about-author.md"
)

# Verify all files exist
echo "Verifying source files..."
MISSING=0
for f in "${FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "  MISSING: $f"
    MISSING=$((MISSING + 1))
  fi
done

if [[ $MISSING -gt 0 ]]; then
  echo "ERROR: $MISSING file(s) missing. Aborting."
  exit 1
fi
echo "  All ${#FILES[@]} source files found."
echo ""

# Build EPUB with pandoc
echo "Building EPUB..."
pandoc \
  --metadata-file="$METADATA" \
  --css="$CSS" \
  --toc \
  --toc-depth=2 \
  --split-level=1 \
  -f markdown+smart+pipe_tables+strikeout+yaml_metadata_block \
  -o "$OUTPUT" \
  "${FILES[@]}"

echo ""
echo "=== EPUB built successfully ==="
echo "Output: $OUTPUT"
echo "Size: $(du -h "$OUTPUT" | cut -f1)"
echo ""

# Validate basic structure
echo "Validating EPUB structure..."
if command -v python3 &>/dev/null; then
  python3 -c "
import zipfile, sys
try:
    z = zipfile.ZipFile('$OUTPUT')
    names = z.namelist()
    has_mimetype = 'mimetype' in names
    has_content = any('content.opf' in n for n in names)
    has_toc = any('toc' in n.lower() or 'nav' in n.lower() for n in names)
    html_count = sum(1 for n in names if n.endswith(('.xhtml', '.html')))
    print(f'  mimetype: {\"OK\" if has_mimetype else \"MISSING\"}')
    print(f'  content.opf: {\"OK\" if has_content else \"MISSING\"}')
    print(f'  navigation: {\"OK\" if has_toc else \"MISSING\"}')
    print(f'  HTML files: {html_count}')
    print(f'  Total files: {len(names)}')
    z.close()
    print('  Validation: PASSED')
except Exception as e:
    print(f'  Validation error: {e}', file=sys.stderr)
    sys.exit(1)
"
fi

echo ""
echo "Done! Your EPUB is ready at:"
echo "  $OUTPUT"
