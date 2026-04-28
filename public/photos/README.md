# Author Photos

Place author headshots and personal photos here. Files in `public/` are served
from the URL root, so a file at `public/photos/pages/about/portrait.jpg` is
reachable at `/photos/pages/about/portrait.jpg`.

For decorative website imagery (heroes, backgrounds, illustrations, OG cards),
use `public/images/` instead.

## Directory Structure

- **`author-headshot.jpg`** — Professional headshot for book covers (AI-enhanced from real photo recommended)
- **`bios/`** — Author bio photos and portrait source images
- **`pages/`** — Photos of the author used on specific website pages. One
  subfolder per route:
  - `pages/home/` — used on `/`
  - `pages/about/` — used on a future `/about` route
  - `pages/book/` — used on `/book`
  - `pages/courses/` — used on `/courses`
  - `pages/essence/` — used on `/essence`
  - `pages/library/` — used on `/library`
  - `pages/schedule/` — used on `/schedule`

  Add more page folders as needed. Use lowercase, hyphenated filenames
  (e.g. `pages/about/portrait-warm.webp`).

## Using a page photo in a component

```tsx
import Image from "next/image";

<Image
  src="/photos/pages/about/portrait.webp"
  alt="..."
  width={800}
  height={1000}
/>
```

## Photos

### `bios/`

Source photos for author bio and marketing use:

- `IMG_1020.jpeg`
- `IMG_1482.jpeg`
- `IMG_1483.jpeg`
- `IMG_3996.jpeg`

## Technical Requirements

- High resolution (minimum 300 DPI at print size)
- Clean background, uncluttered
- JPEG or PNG format
- Minimum 600 x 800 px (will be scaled for back cover use)
- Same photo used across all 8 volumes for series consistency

## Photo Style Guide

Given the subject matter (healing from narcissistic abuse, personal sovereignty) and the audience (emotionally sensitive adults seeking recovery), the photo should communicate **trust, warmth, and lived experience** — not corporate polish.

### Framing

- Head-and-shoulders crop (not full body)
- Slightly off-center composition — more natural and inviting than centered/corporate
- Shot from chest up, allowing breathing room around the head

### Expression & Energy

- Soft, genuine smile — approachable but grounded (not performative)
- Direct eye contact with the camera — builds trust, critical for readers who've experienced betrayal
- Relaxed posture — conveys someone who's done the work, not someone posing

### Background

- Clean and uncluttered
- Natural/warm tones — soft greenery, warm neutrals, or a slightly blurred natural setting (Costa Rica connection is a differentiator)
- Avoid pure white studio backgrounds — they feel clinical for this genre

### Lighting

- Natural light or soft diffused light
- Golden hour or open shade produces the warmest, most flattering results
- Avoid harsh shadows or overhead lighting

### Wardrobe

- Solid, warm colors (earth tones, soft blues, muted greens)
- Avoid busy patterns — they distract at small print sizes on the back cover
- Simple neckline — the reader's eye should go to the face

### What to Avoid

- Overly glamorous or filtered shots — readers in this genre value authenticity
- Sunglasses, hats, or anything hiding the eyes — eye contact = trust
- Group photos cropped down — they always look awkward
- Low-resolution phone selfies — even with AI enhancement, the source needs decent quality

## Back Cover Placement

The back cover layout places the author photo and bio side by side in the lower section:

```
[Author Photo]  [Author Bio]
 (headshot)     (50-75 words)
 Left-aligned   bio wraps right
```

This is the standard nonfiction convention — readers' eyes scan left-to-right, so the photo anchors the section and the bio flows naturally. See `book/release/15-designer-brief.md` for full back cover specifications.

## AI Enhancement Notes

AI enhancement works well as long as the base photo has good lighting and composition. AI can clean up background, adjust color balance, and sharpen — but it can't fix a bad angle or forced expression. Start with the best natural photo possible.

## Usage

Referenced by `book/release/15-designer-brief.md` for the back cover layout of all 8 volumes of The Sovereignty Series.
