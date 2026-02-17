# Website Designer Guide — LightField Institute

## A Multi-Series Author Platform for Jennifer Brooke Lawless

**Site:** LightField.institute
**Author:** Jennifer Brooke Lawless
**Current State:** Sessions-focused single-page site (dark theme, healing sessions, aura reading)
**Goal:** Full redesign from scratch as a multi-series author platform that integrates books, sessions, courses, and community — with a kingfisher-inspired palette (cream, electric blue, dark indigo, orange-red, black text) that is vivid, precise, and alive

---

## 1. Site Identity & Naming Recommendation

### Why Keep LightField.institute

The name "Light Field" naturally bridges every pillar of this platform:

| Pillar | How "Light Field" Connects |
|--------|---------------------------|
| **The Sovereignty Series** | Your field of personal power, agency, and self-authority |
| **The Energy Series** | Your literal biofield — the human energy field you learn to read, clear, and protect |
| **Sessions** | Aura reading and energy work — observing and healing the light field |
| **Future Series** | The "field" metaphor scales to any domain of consciousness |

**Recommendation:** Keep **LightField.institute** as the permanent home. "Institute" conveys authority, research-backed credibility, and a container larger than any single book. It positions Jennifer not as an author selling books, but as the founder of a body of work.

### Brand Architecture

```
LightField Institute (umbrella)
├── The Sovereignty Series (book series 1)
├── The Energy Series (book series 2)
├── Future Series (book series 3+)
├── The Auracle (sessions page — /the-auracle)
│   Jennifer's practitioner identity; word-of-mouth booking destination
│   Connect-first flow (WhatsApp / email), not calendar widget
├── Courses (structured learning)
└── Community (newsletter, circles, resources)
```

### Alternative Names Considered

If a fresh start feels right, these alternatives were evaluated:

| Name | Pros | Cons |
|------|------|------|
| **LightField.institute** (keep) | Already established, SEO equity, bridges all series | May carry associations from V1 that need resetting |
| **JaeLawless.com** | Author-centric, personal, memorable | Doesn't scale if brand outgrows one person |
| **TheFieldInstitute.com** | Clean, academic, ties to Energy Series | Loses "Light" which carries spiritual weight |
| **SovereignField.com** | Powerful, bridges both series | Too niche if future series diverge |
| **LightFieldPress.com** | Clearly a publishing/book brand | Loses sessions and healing work |

**Verdict:** LightField.institute is the strongest option. It's already live, the domain is premium (.institute), and "light field" is a concept that grows with the work.

---

## 2. What to Keep from the Current Site

The current LightField.institute has a strong foundation. Preserve these elements:

### Keep
- **The Auracle page** — the core session offering (thematic, couples, business, and group readings + the Chakra Journey package), rebranded from generic "Sessions" to leverage The Auracle's word-of-mouth recognition
- **The "Where Seen and Unseen Meet" positioning** — this tagline is powerful and bridges the clinical and the spiritual
- **Medical disclaimer** — sessions don't replace medical care; this stays in the footer
- **The sparkle/star logo element** — refine, consider rendering in electric blue or indigo
- **The three-pillar messaging** — intuitive wisdom, consciousness education, biofield research

### Evolve
- **Color palette** — move from the all-dark theme to a **kingfisher-inspired palette**: cream backgrounds, black text, electric blue and indigo accents, orange-red CTAs. Dark indigo is used for immersive sections (hero, footer, series banners), not as the default page background
- **Navigation** — currently Sessions/Learn/Research/Resources/Community/About; needs to add Books prominently
- **Hero section** — shift from sessions-first to a broader "author + body of work" introduction
- **Visual depth** — the current site is functional; the redesign should feel more immersive and editorial
- **Typography** — the current Inter + Cormorant Garamond pairing is good but could be elevated (see typography section below)

### Remove
- **The all-dark default** — the new palette leads with cream (warmth, openness) and reserves dark indigo for impact sections
- **Any "coming soon" or placeholder content** — only ship what's real
- **Overly generic stock imagery** — replace with custom art direction

---

## 3. Information Architecture

### Primary Navigation

```
Logo (Home)  |  Books  |  The Auracle  |  Learn  |  About  |  [Connect with Jennifer]
```

**Mobile:** Hamburger menu with the same items; "Connect with Jennifer" remains visible as a floating CTA.

### Sitemap

```
/                           Home (hero + overview)
│
├── /books                  All Series overview
│   ├── /sovereignty        The Sovereignty Series landing page
│   │   ├── /see            Volume 1 detail page
│   │   ├── /heal           Volume 2 detail page
│   │   ├── /stand          Volume 3 detail page
│   │   ├── /live           Volume 4 detail page
│   │   ├── /give           Volume 5 detail page
│   │   ├── /serve          Volume 6 detail page
│   │   ├── /thrive         Volume 7 detail page
│   │   └── /become         Volume 8 detail page
│   │
│   └── /energy             The Energy Series landing page
│       ├── /the-field      Volume 1 detail page
│       ├── /the-centers    Volume 2 detail page
│       ├── /the-cleanse    Volume 3 detail page
│       ├── /the-fuel       Volume 4 detail page
│       ├── /the-frequency  Volume 5 detail page
│       ├── /the-circle     Volume 6 detail page
│       ├── /the-space      Volume 7 detail page
│       └── /the-flow       Volume 8 detail page
│
├── /the-auracle            The Auracle — all session types & booking
│   ├── #thematic           Thematic Reading (anchor sections)
│   ├── #couples            Couples Reading
│   ├── #business           Business Reading
│   ├── #group              Group Reading
│   └── #chakra-journey     Chakra Journey (12-session package)
│
├── /learn                  Courses and education (Coming Soon)
│   ├── /aura-reading-1     Aura Reading Level 1 (Coming Soon)
│   └── /rose-meditation    Rose Meditation Training (Coming Soon)
│
├── /about                  Jennifer's story + credentials
├── /newsletter             Substack integration / signup
├── /free                   Lead magnets (Decoder Cards, etc.)
└── /contact                Contact + booking
```

### URL Strategy

- **Series pages** use the series name: `/books/sovereignty`, `/books/energy`
- **Volume pages** use the arc word (short, memorable): `/books/sovereignty/see`, `/books/energy/the-field`
- **No dates in URLs** — these are evergreen
- **Lowercase, hyphenated** — standard web convention

### What the Site Does NOT Include

- **No built-in digital reader.** Books are purchased on Amazon (Kindle/paperback) and Gumroad (PDF/ebook). The site offers a chapter preview (Chapter 1 of each volume) as a lead magnet / taste, not a full reading experience. Chapter 1 can also be offered as a free download in exchange for an email address.
- **No course enrollment at launch.** The course infrastructure (Rose Meditation Level 1 with 10 lessons, AI learning assistant) exists in the codebase and will launch in Phase 4. For now, courses show as "Coming Soon" with an email waitlist.
- **No fabricated social proof.** No "500+ readings" or "1200+ students" counters. Real testimonials only — currently ~4 video and ~3 written. Design should accommodate a small but growing collection.

---

## 4. Page Templates

### 4A. Home Page

The home page introduces the full scope of LightField Institute. It is NOT a book landing page or a session booking page — it's the front door to the entire body of work.

```
┌─────────────────────────────────────────────────────────┐
│  HERO                                                   │
│                                                         │
│  "Where Seen and Unseen Meet"                          │
│                                                         │
│  A brief author introduction (2-3 sentences):           │
│  Jennifer Brooke Lawless is a therapist, writer,        │
│  and energy practitioner. Through books, sessions,      │
│  and courses, she helps sensitive adults decode          │
│  patterns, heal their nervous systems, and reclaim      │
│  their energy fields.                                   │
│                                                         │
│  [Explore the Books]  [Meet The Auracle]                │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  THE BOOKS — Two series cards side by side              │
│                                                         │
│  ┌──────────────────┐  ┌──────────────────┐            │
│  │ The Sovereignty  │  │ The Energy       │            │
│  │ Series           │  │ Series           │            │
│  │                  │  │                  │            │
│  │ 8 volumes on     │  │ 8 volumes on     │            │
│  │ healing from     │  │ reading, clearing │            │
│  │ narcissistic     │  │ and protecting    │            │
│  │ abuse & building │  │ your energy      │            │
│  │ sovereignty      │  │ field            │            │
│  │                  │  │                  │            │
│  │ SEE → BECOME     │  │ SENSE → RADIATE  │            │
│  │                  │  │                  │            │
│  │ [Explore Series] │  │ [Coming Soon]    │            │
│  └──────────────────┘  └──────────────────┘            │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  THE AURACLE — Sessions overview                        │
│                                                         │
│  "Your field speaks. I help you listen."                │
│                                                         │
│  Brief intro: Jennifer Brooke Lawless, The Auracle —    │
│  therapist, energy practitioner, and the person your    │
│  friend told you to go see.                             │
│                                                         │
│  Session type cards:                                    │
│  - Thematic Reading                                     │
│  - Couples Reading                                      │
│  - Business Reading                                     │
│  - Group Reading                                        │
│  - Chakra Journey (12-session signature package)        │
│                                                         │
│  [Meet The Auracle]  [Connect with Jennifer]            │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  FEATURED VOLUME — Spotlight on the latest release      │
│                                                         │
│  Large cover image + excerpt + buy links                │
│  (Amazon, Gumroad) + "Read Chapter 1" preview           │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  TESTIMONIALS — Highlighted real testimonials            │
│                                                         │
│  Space for 2-3 featured testimonials (video embed       │
│  or written quote with attribution). Only real           │
│  testimonials — no fabricated stats. Currently ~4        │
│  video and ~3 written testimonials available.            │
│                                                         │
│  Layout: Featured video testimonial (large) +           │
│  2 written quotes beside or below. Rotates or           │
│  curated selection.                                      │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  COURSES — Coming Soon teaser                           │
│                                                         │
│  "Learn the practices."                                 │
│  Brief description of Rose Meditation and Aura          │
│  Reading courses. Infrastructure exists — content is    │
│  coming. Email capture: "Be the first to know when      │
│  courses launch."                                       │
│                                                         │
│  [Join the Waitlist]                                    │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  NEWSLETTER SIGNUP — Substack integration               │
│                                                         │
│  "Join the field. Get early access, free resources,     │
│  and the decoder cards."                                │
│                                                         │
│  [Email input]  [Subscribe]                             │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  ABOUT (brief) — Photo + 2-sentence bio + link          │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  FOOTER                                                 │
└─────────────────────────────────────────────────────────┘
```

### 4B. Series Landing Page (`/books/sovereignty` or `/books/energy`)

Each series gets its own immersive landing page. This is where readers understand the arc, browse volumes, and decide where to start.

```
┌─────────────────────────────────────────────────────────┐
│  SERIES HERO                                            │
│                                                         │
│  "The Sovereignty Series"                               │
│  Tagline: "You were never broken. You were decoded."    │
│                                                         │
│  The full arc mantra (subtle, typographic):             │
│  SEE · HEAL · STAND · LIVE · GIVE · SERVE · THRIVE     │
│  · BECOME                                               │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  SERIES OVERVIEW — 2-3 paragraphs on what the series    │
│  covers, who it's for, and what transformation awaits   │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  THE VOLUMES — Visual grid of all 8 books               │
│                                                         │
│  Each volume card shows:                                │
│  - Cover image                                          │
│  - Arc word (SEE, HEAL, etc.)                           │
│  - Subtitle                                             │
│  - One-sentence description                             │
│  - Status badge (Available / Coming Soon)               │
│  - [Read More] link to volume detail page               │
│                                                         │
│  Layout: 2 columns on desktop, 1 column on mobile       │
│  Volumes should visually flow left-to-right, top-to-    │
│  bottom in reading order                                │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  THE POEM — The subtitles read together as a poem       │
│                                                         │
│  "The truth that was hidden in plain sight...           │
│   The body that remembers the way home...               │
│   The ground that was always yours..."                  │
│                                                         │
│  (Typographic moment — large, elegant, centered)        │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  BUNDLE OPTIONS — Buy individual or bundled              │
│                                                         │
│  - Single volumes (Kindle, Paperback, Gumroad)          │
│  - Vol 1-2 Bundle                                       │
│  - Vol 1-4 Bundle                                       │
│  - Complete Series Bundle                               │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  CROSS-SERIES CALLOUT                                   │
│  "Continue the journey → The Energy Series"             │
└─────────────────────────────────────────────────────────┘
```

### 4C. Volume Detail Page (`/books/sovereignty/see`)

Each individual volume gets a page that serves as both a reading guide and a sales page.

```
┌─────────────────────────────────────────────────────────┐
│  VOLUME HERO                                            │
│                                                         │
│  The Sovereignty Series · Volume 1                      │
│                                                         │
│  SEE                                                    │
│  The Truth That Was Hidden in Plain Sight               │
│                                                         │
│  [Cover image — large, high-quality]                    │
│                                                         │
│  [Buy on Amazon]  [Buy on Gumroad]  [Read Chapter 1]   │
│                                                         │
│  Note: "Read Chapter 1" opens a chapter preview on-     │
│  site (not a full reader). Books are purchased via       │
│  Amazon (Kindle/paperback) or Gumroad (PDF/ebook).      │
│  No built-in digital reader — external platforms only.   │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  BOOK DESCRIPTION — Back cover blurb (100-150 words)    │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  WHAT'S INSIDE — Chapter overview or key topics          │
│  (Not full TOC — just the promise of what the reader    │
│  will learn)                                            │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  TESTIMONIALS — Real reader testimonials (when avail.)  │
│  Space for video testimonials (embedded) and written     │
│  quotes. Only show if real testimonials exist for this   │
│  volume. No fabricated stats or placeholder reviews.     │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  NEXT IN THE SERIES — Card linking to Volume 2           │
│  "You've named the patterns. Now heal the body that     │
│  remembers → HEAL"                                      │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  FREE RESOURCE — Chapter 1 download for email, or       │
│  Decoder Cards download (lead magnet)                   │
└─────────────────────────────────────────────────────────┘
```

### 4D. The Auracle Page (`/the-auracle`)

The dedicated sessions page. This is where word-of-mouth traffic lands — when someone's friend says "go see The Auracle," this is the door they walk through. From here they discover LightField's entire ecosystem (books, courses, community).

The page uses LightField's visual identity throughout — kingfisher palette, same typography, same component system. No separate branding.

**Booking flow:** Connect-first, not transactional. No calendar widget. Visitors read about session types, then reach out via WhatsApp or email to connect with Jennifer personally before booking. This filters for readiness, builds the relationship before the session starts, and positions the work as premium and personal.

```
┌─────────────────────────────────────────────────────────┐
│  THE AURACLE — HERO                                     │
│                                                         │
│  "Your field speaks. I help you listen."                │
│                                                         │
│  Jennifer Brooke Lawless, The Auracle                   │
│                                                         │
│  Brief intro (2-3 sentences): Who The Auracle is,       │
│  what she does, who this is for. Direct, warm,          │
│  grounded — not "gentle sacred" or rose-toned.          │
│                                                         │
│  [Connect with Jennifer]                                │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  SESSION TYPES — Card grid (anchor sections)            │
│                                                         │
│  Each card:                                             │
│  - Session name                                         │
│  - Duration                                             │
│  - Price                                                │
│  - Brief description (what happens, who it's for)       │
│  - [Connect to Book] → WhatsApp or email                │
│                                                         │
│  Individual Sessions — 60 min, $200 each:               │
│  1. Thematic Reading                                    │
│  2. Couples Reading                                     │
│  3. Business Reading                                    │
│  4. Group Reading                                       │
│                                                         │
│  Signature Package:                                     │
│  5. Chakra Journey — 12 sessions, $2,100                │
│     Flexible pacing: 1x/week over 3 months or           │
│     1x/month over a year. This is the signature         │
│     deep-work offering — give it visual prominence.     │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  HOW IT WORKS — 3-step visual                           │
│  (Reach Out → We Connect → We Meet)                     │
│                                                         │
│  1. Reach out via WhatsApp or email                     │
│  2. Jennifer connects with you personally to            │
│     understand what you need                            │
│  3. She books your session and you meet                 │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  TESTIMONIALS — Real session testimonials                │
│                                                         │
│  Video testimonials (embedded, 1-2 featured) and/or     │
│  written quotes with attribution. Only real — no         │
│  fabricated numbers or inflated stats.                   │
│                                                         │
│  Currently available: ~4 video, ~3 written.             │
│  Design should accommodate growing collection over      │
│  time without looking empty at launch.                  │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  ABOUT JENNIFER — Brief practitioner bio                │
│  BS Psychology (Boston University), MS Mental Health     │
│  Counseling (Nova Southeastern). Clinical experience    │
│  in psychiatric care, family systems, couples work.     │
│  100+ readings completed. Not a flashy stat — a quiet   │
│  credential in the bio, not a homepage banner.          │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  CONNECT — WhatsApp link + email                        │
│  "Ready to start? Reach out and let's talk."            │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  DISCLAIMER — Sessions are not a substitute for         │
│  medical or psychological care                          │
└─────────────────────────────────────────────────────────┘
```

### 4E. About Page (`/about`)

```
┌─────────────────────────────────────────────────────────┐
│  ABOUT HERO                                             │
│                                                         │
│  Professional headshot (large, centered or left)         │
│  Jennifer Brooke Lawless                                 │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  THE STORY — Medium bio (150 words), personal tone       │
│                                                         │
│  Credentials: BS Psychology (Boston University),         │
│  MS Mental Health Counseling (Nova Southeastern),        │
│  Clinical experience in psychiatric care, family         │
│  systems, couples work                                   │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  THE WORK — Brief on Light Field Institute's mission     │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  CONNECT — Instagram (@jae.lawless), email, newsletter   │
└─────────────────────────────────────────────────────────┘
```

---

## 5. Visual Design System

### 5A. Color Palette — Inspired by the Kingfisher

The entire site palette is drawn from the common kingfisher (*Alcedo atthis*) — a bird whose plumage is electric blue along the back and rump, deep indigo on the wings and crown, fiery orange-red on the breast, and soft cream at the throat. The colors are not produced by pigment but by structural refraction of light — fitting for a site called **Light Field**.

The palette moves between these poles: **deep indigo** grounds the site, **electric blue** energizes it, **cream** gives breathing room, and **orange-red** draws the eye to action.

#### Kingfisher Reference Colors

| Plumage Area | Color | Hex | Source |
|--------------|-------|-----|--------|
| Back & rump | Electric Blue | `#0EA5C3` | Structural blue (Tyndall effect) |
| Wings & crown | Dark Indigo | `#13417C` | Deep blue, almost navy |
| Breast & belly | Orange-Red | `#E0522D` | Warm, fiery, unmistakable |
| Throat & collar | Cream | `#F5F0E1` | Soft warm white |
| Eye & bill | Black | `#1A1A1A` | Sharp, defining |

#### Core Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg-primary` | `#F5F0E1` | Page background — the cream of the kingfisher's throat. Warm, natural, not sterile white |
| `--bg-secondary` | `#FFFDF7` | Cards, elevated surfaces — slightly lighter cream |
| `--bg-tertiary` | `#EDE8D9` | Subtle contrast areas, hover states |
| `--bg-dark` | `#0C1A2E` | Dark sections (hero, footer) — derived from the indigo deepened |
| `--bg-dark-secondary` | `#13417C` | Dark section cards, nav overlay — the indigo itself |
| `--border-subtle` | `#D4CDBD` | Card borders, dividers on light backgrounds |
| `--border-dark` | `#1E3A5F` | Borders on dark sections |
| `--text-primary` | `#1A1A1A` | Headlines, primary text — black, like the kingfisher's bill |
| `--text-secondary` | `#3A3A3A` | Body text, descriptions |
| `--text-tertiary` | `#6B6B6B` | Captions, metadata, timestamps |
| `--text-on-dark` | `#F5F0E1` | Text on indigo/dark backgrounds — cream |
| `--text-on-dark-secondary` | `#B8C8D8` | Secondary text on dark backgrounds |

#### Accent Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `--accent-blue` | `#0EA5C3` | Primary accent — links, interactive elements, the electric blue flash |
| `--accent-blue-deep` | `#0889A3` | Hover state for blue elements |
| `--accent-blue-soft` | `#0EA5C320` | Blue at 12% opacity — subtle tag backgrounds on cream |
| `--accent-indigo` | `#13417C` | Secondary accent — depth, authority, section backgrounds |
| `--accent-indigo-light` | `#1E5A9E` | Lighter indigo for hover/active states |
| `--accent-red` | `#E0522D` | CTA accent — buttons, urgency, "Buy Now", the fiery breast |
| `--accent-red-deep` | `#C4421F` | Hover state for red CTAs |
| `--accent-red-soft` | `#E0522D15` | Red at 8% opacity — subtle warmth, badges |
| `--accent-orange` | `#FB9543` | Warm midtone — between the red and cream, highlights and accents |

#### Series-Specific Accent Colors

Each series uses a color drawn from the kingfisher palette. This prevents visual monotony as the site grows.

| Series | Accent | Hex | Rationale |
|--------|--------|-----|-----------|
| **The Sovereignty Series** | Orange-Red | `#E0522D` | Fire, truth, the courage to see and stand |
| **The Energy Series** | Electric Blue | `#0EA5C3` | The biofield, light, energetic clarity |
| **Future Series** | TBD | TBD | Drawn from remaining palette tones |

#### Semantic Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `--success` | `#3A8A5C` | Available, in stock, confirmed |
| `--warning` | `#FB9543` | Coming soon, limited |
| `--info` | `#0EA5C3` | Informational badges, tips |
| `--error` | `#C4421F` | Error states, validation failures |

#### Dark Sections

The site is primarily cream-on-black-text, but key sections use the kingfisher's indigo as an immersive backdrop:

- **Hero sections** — deep indigo (`#0C1A2E`) with electric blue typographic accents
- **Footer** — dark indigo background, cream text
- **Series hero banners** — indigo base with series-specific accent color wash
- **Newsletter signup strip** — indigo background, cream input, orange-red submit button

This creates a rhythm: **cream (breathe) → indigo (immerse) → cream (breathe)** — like the kingfisher diving into water and emerging again.

### 5B. Typography

#### Font Pairing

| Role | Font | Weight | Fallback |
|------|------|--------|----------|
| **Headings** | Cormorant Garamond | 400, 500 | Georgia, serif |
| **Body** | Inter | 300, 400, 500 | system-ui, sans-serif |
| **Arc Words** | Cormorant Garamond (uppercase, tracked) | 500, 600 | Georgia, serif |
| **Monospace** | JetBrains Mono | 400 | monospace |

**Why this pairing:** Cormorant Garamond brings editorial elegance and spiritual warmth to headings. Inter provides clean, modern readability for body text. The contrast between serif headings and sans-serif body creates a magazine-like editorial feel that positions the site above typical self-help aesthetics.

#### Type Scale

| Level | Size (Desktop) | Size (Mobile) | Line Height | Use |
|-------|----------------|---------------|-------------|-----|
| **Display** | 64px | 40px | 1.1 | Hero headlines |
| **H1** | 48px | 32px | 1.2 | Page titles |
| **H2** | 36px | 28px | 1.25 | Section headings |
| **H3** | 28px | 22px | 1.3 | Card titles |
| **H4** | 22px | 18px | 1.35 | Subsection headings |
| **Body** | 17px | 16px | 1.7 | Paragraphs |
| **Small** | 14px | 13px | 1.5 | Captions, metadata |
| **Micro** | 12px | 12px | 1.4 | Labels, badges |

#### Arc Word Treatment

The single-word titles (SEE, HEAL, STAND, etc.) are the brand. They receive special typographic treatment:

```css
.arc-word {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.25em;
  color: var(--text-primary); /* Black on cream, cream on indigo */
  /* Size varies by context — hero: 96px, card: 36px, inline: 18px */
}

/* On indigo backgrounds */
.arc-word--on-dark {
  color: var(--text-on-dark); /* Cream */
}

/* Series-specific accent coloring (optional) */
.arc-word--sovereignty { color: #E0522D; } /* Orange-red */
.arc-word--energy { color: #0EA5C3; } /* Electric blue */
```

### 5C. Spacing & Layout

- **Base unit:** 8px
- **Spacing scale:** 8, 16, 24, 32, 48, 64, 96, 128px
- **Max content width:** 1200px (centered)
- **Prose max-width:** 680px (for readability on book description text)
- **Card padding:** 32px desktop, 24px mobile
- **Section spacing:** 96px desktop, 64px mobile
- **Grid:** 12-column on desktop, 4-column on mobile

### 5D. Imagery & Art Direction

| Element | Direction |
|---------|-----------|
| **Hero backgrounds** | Deep indigo (`#0C1A2E`) with abstract light effects — think light refracting through water, the kingfisher's dive. Electric blue and orange-red light streaks on dark indigo. No stock photos of people. |
| **Book covers** | Display as high-quality 3D mockups with shadows on the cream background. Show books at a slight angle, not flat. Use the mockup files from the cover design package. |
| **Series backgrounds** | Each series landing hero uses indigo + its accent color. Sovereignty: indigo with orange-red warmth. Energy: indigo with electric blue luminescence. |
| **Session images** | Abstract or environmental — water, light through prisms, nature. Never photos of people in sessions. The kingfisher is a river bird — water imagery is natural. |
| **Author photo** | The AI-enhanced professional headshot from `public/photos/author-headshot.jpg`. Warm, approachable, not overly staged. |
| **Kingfisher motif** | The kingfisher bird itself should NOT appear literally on the site. The palette IS the bird. If a subtle nod is desired, a single abstract feather illustration or light-refraction pattern can echo the source. |

#### Gradient System

```css
/* Primary gradient — electric blue flash */
--gradient-primary: linear-gradient(135deg, #0EA5C3, #13417C);

/* Hero overlay — deep indigo immersion */
--gradient-hero: linear-gradient(180deg, #0C1A2E 0%, #13417C 50%, #0C1A2E 100%);

/* CTA gradient — the fiery breast */
--gradient-cta: linear-gradient(135deg, #E0522D, #FB9543);

/* Sovereignty Series accent wash */
--gradient-sovereignty: linear-gradient(135deg, #E0522D12, #FB954312);

/* Energy Series accent wash */
--gradient-energy: linear-gradient(135deg, #0EA5C312, #13417C12);

/* Cream-to-white page transition */
--gradient-page: linear-gradient(180deg, #F5F0E1, #FFFDF7);
```

### 5E. Component Patterns

#### Buttons

| Type | Style | Use |
|------|-------|-----|
| **Primary** | Solid orange-red background (`#E0522D`), cream text (`#F5F0E1`) | "Connect with Jennifer", "Buy Now" |
| **Secondary** | Electric blue border (`#0EA5C3`), transparent background, blue text | "Explore Series", "Learn More" |
| **Dark Primary** | Solid orange-red on indigo sections, cream text | CTAs inside dark hero/footer sections |
| **Ghost** | No border, electric blue text with subtle hover underline | "Read more", navigation links |

All buttons: `border-radius: 4px` (subtly rounded, not pill-shaped), `height: 48px` for primary, `40px` for secondary. On hover, primary buttons darken to `#C4421F`.

#### Cards

```
┌─────────────────────────────────────────┐
│                                         │  border: 1px solid var(--border-subtle)
│   [Image or Cover Art]                  │  background: var(--bg-secondary) (#FFFDF7)
│                                         │  border-radius: 8px
│   Card Title (black text)               │  padding: 32px
│   Description text (dark gray)          │
│                                         │  On hover:
│   [CTA Link in electric blue]           │  border-color: var(--accent-blue)
│                                         │  subtle upward translate (2px)
│                                         │  soft warm box-shadow
└─────────────────────────────────────────┘
```

On dark (indigo) backgrounds, cards invert: `background: #1E3A5F`, `border: #2A4A6F`, text in cream.

#### Navigation Bar

- Fixed to top, cream background (`#F5F0E1`) with subtle bottom border and backdrop-blur
- Logo left (black text or mark), nav items center (black text), CTA button right (orange-red, "Connect with Jennifer")
- Mobile: hamburger menu, full-screen indigo overlay with cream text
- Active page indicated by electric blue underline or text color
- On scroll: slight shadow appears beneath nav bar
- Height: 72px desktop, 64px mobile

#### Footer

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Logo]                                                 │
│                                                         │
│  Books          The Auracle    Institute     Connect    │
│  Sovereignty    Thematic       About         Instagram  │
│  Energy         Couples        Newsletter    YouTube    │
│  Free Resources Business       Research       Email     │
│                 Group          WhatsApp                  │
│                 Chakra Journey                           │
│                                                         │
│  ─────────────────────────────────────────────────────  │
│                                                         │
│  © 2026 LightField Institute. All rights reserved.      │
│  Sessions do not replace medical or psychological care. │
│                                                         │
│  Privacy  ·  Terms  ·  Disclaimer  ·  Accessibility     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 6. Multi-Series Design System

The site must scale to support multiple book series without redesigning. Here's the pattern:

### Series Identity Pattern

Each series registers:

| Property | Sovereignty Series | Energy Series | Future Series |
|----------|--------------------|---------------|---------------|
| **Name** | The Sovereignty Series | The Energy Series | TBD |
| **Accent Color** | Orange-Red `#E0522D` | Electric Blue `#0EA5C3` | TBD |
| **Tagline** | "You were never broken. You were decoded." | "You are not just in a body — you are a field." | TBD |
| **Arc Words** | SEE, HEAL, STAND, LIVE, GIVE, SERVE, THRIVE, BECOME | SENSE, UNDERSTAND, CLEAR, NOURISH, ATTUNE, PROTECT, SANCTIFY, RADIATE | TBD |
| **Volume Count** | 8 | 8 | TBD |
| **Audience** | Adults healing from narcissistic abuse | Adults learning energy mastery | TBD |
| **Hero Texture** | Warm indigo with orange-red light / shattered glass motif | Deep indigo with electric blue luminescence / biofield waves | TBD |

### Volume Card Component

Every volume across every series uses the same card component with series-specific theming:

```
┌─────────────────────────────────┐
│                                 │
│  [Cover Image]                  │  ← Same aspect ratio, all series
│                                 │
│  VOLUME 1                       │  ← Micro text, --text-tertiary (#6B6B6B)
│  SEE                            │  ← Arc word, series accent (orange-red or blue)
│  The Truth That Was Hidden      │  ← Subtitle, --text-secondary (#3A3A3A)
│  in Plain Sight                 │
│                                 │
│  [Available Now]                │  ← Status badge (green on cream)
│  [Read More →]                  │  ← Link in electric blue (#0EA5C3)
│                                 │
└─────────────────────────────────┘
```

### Cross-Series Navigation

At the bottom of every series page:

```
──── More from Jennifer Brooke Lawless ────

[The Sovereignty Series]     [The Energy Series]
 SEE · HEAL · STAND ...      SENSE · UNDERSTAND · CLEAR ...

──────────────────────────────────────────────
```

### Adding a New Series (Designer Instructions)

When a new series is announced:

1. Choose a new accent color that complements existing palette
2. Create a hero texture/gradient for the series landing page
3. Register the series in the navigation dropdown under "Books"
4. Build the series landing page from the existing template
5. Build volume detail pages from the existing template
6. Add the series card to the home page Books section
7. Add cross-series links to all existing series pages

No structural redesign should be needed. The system is additive.

---

## 7. Responsive Breakpoints

| Breakpoint | Width | Layout |
|------------|-------|--------|
| **Mobile** | < 640px | Single column, stacked cards, hamburger nav |
| **Tablet** | 640px – 1024px | 2-column grids, condensed nav |
| **Desktop** | 1024px – 1440px | Full layout, 3-column grids |
| **Wide** | > 1440px | Centered content, max-width 1200px |

### Key Responsive Behaviors

- **Book grids:** 4-across on desktop, 2-across on tablet, 1-across (with horizontal scroll option) on mobile
- **Navigation:** Full horizontal on desktop, hamburger on mobile/tablet
- **Hero text:** Scale down from Display (64px) to 40px on mobile
- **Section spacing:** 96px → 64px → 48px as viewport narrows
- **Cards:** Full width on mobile, side margins collapse to 16px

---

## 8. Performance & Technical Standards

| Metric | Target |
|--------|--------|
| **Lighthouse Performance** | > 90 |
| **First Contentful Paint** | < 1.5s |
| **Largest Contentful Paint** | < 2.5s |
| **Cumulative Layout Shift** | < 0.1 |
| **Time to Interactive** | < 3s |

### Technical Requirements

- **Framework:** Next.js (already in codebase) with App Router
- **Styling:** Tailwind CSS (already configured)
- **Images:** Next.js `<Image>` with WebP/AVIF, lazy-loaded
- **Fonts:** Self-hosted (not Google Fonts CDN) for performance and privacy
- **Animations:** CSS-only for micro-interactions; respect `prefers-reduced-motion`
- **Dark mode:** Cream is default; the indigo sections provide natural contrast. A full dark mode toggle is not required for launch but the color system should support it if added later

---

## 9. Accessibility

- WCAG AA compliance minimum
- All interactive elements keyboard-accessible
- Skip-to-content link on every page
- Alt text on all images (book covers, headshot, decorative marked as `aria-hidden`)
- Color contrast: black text (`#1A1A1A`) on cream (`#F5F0E1`) = 14.2:1 — excellent. Cream text on indigo (`#13417C`) = 8.1:1 — excellent. All combinations must meet 4.5:1 minimum
- Focus indicators: electric blue outline (`#0EA5C3`) visible on all focusable elements
- Screen reader-friendly navigation with proper ARIA landmarks

---

## 10. Content Strategy for Growth

### Phase 1 — Launch (Sovereignty Series Vol 1-3)
- Home page with series overview
- Sovereignty Series landing + volume pages for published volumes
- Volume detail pages with chapter preview, buy links (Amazon/Gumroad), and free Chapter 1 download for email
- The Auracle page (sessions, migrated and rebranded from current site)
- About page
- Newsletter signup
- Free Decoder Cards download
- Real testimonials placed where available (~4 video, ~3 written)
- Courses section as "Coming Soon" with email waitlist capture

### Phase 2 — Expansion (Sovereignty Series Vol 4-8)
- Add volume pages as published
- Add testimonials and reviews as they come in
- Add "Start Here" quiz ("Which volume should I read first?")
- Blog/articles integration (optional — could link to Substack)

### Phase 3 — Multi-Series (Energy Series)
- Energy Series landing page
- Volume pages as published
- Cross-series navigation
- Updated home page with both series featured equally
- Potential "Reading Path" feature — guided journey across both series

### Phase 4 — Platform (Courses Go Live)
- Course enrollment and delivery (Rose Meditation Level 1 first, infrastructure already built)
- AI learning assistant integrated into course experience (already prototyped as "The Auracle AI")
- Community features
- Reading groups / circles
- The Auracle page refinement (more testimonials, session outcomes, connect-first flow optimization)

---

## 11. Designer Deliverables

### What We Need

| Deliverable | Format | Description |
|-------------|--------|-------------|
| **Design system file** | Figma | All colors, typography, components, spacing |
| **Home page** | Figma (desktop + mobile) | Complete layout with real content |
| **Series landing page** | Figma (desktop + mobile) | Template that works for any series |
| **Volume detail page** | Figma (desktop + mobile) | Template that works for any volume |
| **Sessions page** | Figma (desktop + mobile) | All session types |
| **About page** | Figma (desktop + mobile) | Author story + credentials |
| **Navigation & Footer** | Figma | All states (desktop, mobile, expanded) |
| **Component library** | Figma | Buttons, cards, badges, forms, nav items |
| **Interaction specs** | Figma (prototyped) | Hover states, transitions, mobile menu |

### What the Designer Will Receive

1. This guide (complete specifications and creative direction)
2. Book cover art files (when available from cover designer)
3. Author headshot (`public/photos/author-headshot.jpg`)
4. Series content (titles, subtitles, descriptions, arc words)
5. Current site URL for reference (lightfield.institute)
6. Access to the Next.js codebase for technical context

### Creative Freedom

The designer has full creative freedom on:
- Exact color values (the palette above is a starting point, not a constraint)
- Decorative elements, textures, and atmospheric effects
- Animation choices and micro-interactions
- Icon style and illustration approach
- Layout refinements within the page templates
- Font alternatives (if the pairing above doesn't feel right, propose alternatives)

The designer must preserve:
- The kingfisher palette: cream backgrounds, black text, electric blue + indigo + orange-red accents
- Indigo used for immersive sections (hero, footer, series banners) — not as default page background
- The arc words as dominant typographic elements
- Series-agnostic component architecture (scales to N series)
- The overall tone: vivid yet grounded, editorial yet warm, premium yet accessible
- Mobile-first responsive approach

---

## 12. Reference & Inspiration

### Tone References
- **Nature meets authority:** The kingfisher palette — vivid, precise, alive, not muted or corporate
- **Editorial quality:** Monocle, Cereal Magazine — clean, spacious, intentional
- **Book publishing:** Penguin Random House author pages — series browsing done well
- **Premium wellness:** Goop editorial (not product-heavy) — elevated without being clinical
- **Color palette reference:** Study the common kingfisher (*Alcedo atthis*) — the way electric blue sits next to deep indigo, the pop of orange-red against cream. That contrast IS the brand

### What We Are NOT
- A clinical therapy website (no stock photos of couches or handshakes)
- A "woo" crystal shop (no rainbows, no Comic Sans, no clip art)
- A basic WordPress blog with a book sidebar
- An Amazon listing page dressed up as a website

### What We ARE
- An institute — a body of research, practice, and published work
- A sanctuary — a warm, luminous space to explore difficult truths (cream and light, not darkness)
- A bookshelf — a growing library organized by series and journey
- A practitioner's home — where you come to work with Jennifer directly
- A kingfisher — precise, vivid, alive. Dives deep, emerges with clarity

---

*This document is the single source of truth for the website redesign. It should be shared with the web designer alongside the cover designer brief (`15-designer-brief.md`) so both visual systems align.*
