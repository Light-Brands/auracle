# Website Images

Static image assets for the website. Files placed here are served from `/images/...`
at runtime (Next.js serves everything under `public/` at the URL root).

For author headshots and book-related photography, use `public/photos/` instead.

## Structure

- **`hero/`** — Hero / banner images at the top of pages.
- **`backgrounds/`** — Section or page background imagery and textures.
- **`illustrations/`** — Decorative graphics, spot illustrations, diagrams.
- **`icons/`** — Custom inline icons and SVG glyphs (site favicons live in `public/`).
- **`og/`** — Open Graph and social share cards (1200x630 recommended).

Add subfolders as needed (e.g. `images/about/`, `images/landing/`) — keep
related images grouped and use lowercase, hyphenated filenames.

## Usage

```tsx
import Image from "next/image";

<Image
  src="/images/hero/home-banner.webp"
  alt="..."
  width={1600}
  height={900}
  priority
/>
```

Or with a plain `<img>` for simple cases:

```tsx
<img src="/images/illustrations/lotus.svg" alt="..." />
```

## Format guidelines

- **Photos:** WebP or AVIF preferred; JPEG acceptable for compatibility.
- **Illustrations / icons:** SVG when possible (scalable, small).
- **Transparency:** PNG or WebP.
- **OG cards:** PNG or JPEG, exactly 1200x630.

## Optimization

- Compress before committing (e.g. `squoosh`, `sharp`, ImageOptim).
- Aim for < 300 KB per hero image and < 100 KB per inline image.
- For remote images, allowlist the host in `next.config.js` under
  `images.remotePatterns`.

## Licensing

Only commit images you have rights to use. Note the source / license in a
sibling `CREDITS.md` if the provenance isn't obvious from the filename.
