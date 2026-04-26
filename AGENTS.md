# AGENTS.md — auracle

Canonical rules for any AI agent working in this repo. Read this first, every session.

## What this is

Two things in one repo:

1. **`auracle-platform`** — Next.js 14 App Router site for The Auracle (aura reading,
   Rose Meditation courses, Sovereignty Series book reader, admin/CMS, gated content,
   membership/payments). Author: Jae Lawless. Domain: jaelawless.com.
2. **`book/`** — the editorial workspace for the **Sovereignty Series**, a 9-volume
   non-fiction work on narcissism / sovereignty / spiritual recovery. Vol 1 ("The
   Narcissism Decoder" / "See") is the active manuscript and is what 95% of recent
   commits touch. Other vols are scaffolded. This is a *publishing project that ships
   to KDP/Amazon* — markdown is the source of truth, `.docx` and `.epub` are exports.

These two things share a repo because the website surfaces the book content through
`/reader` and the courses through `/courses`. Treat them as one product.

## Stack

- **Next.js 14.0.4 App Router**, React 18, TypeScript (strict: false), Tailwind CSS.
- **No backend, no database.** State lives in `localStorage` (`auracle_user_session`,
  `auracle_user`). Auth is mock — `UserContext` reads/writes localStorage, no real
  identity provider. Payments are mock modals.
- **react-markdown** renders chapter content; chapter MD lives under
  `book/sovereignty-series/vol-N-*/chapters/` and is loaded by the reader routes.
- framer-motion for animation, lucide-react for icons, @headlessui/react for primitives.
- Jest + RTL for tests (mostly absent — `npm run test:ci` is `continue-on-error` in CI).
- Husky pre-commit runs lint-staged + `tsc --noEmit`. Commit-msg hook enforces format.
- CI: `.github/workflows/ci.yml` (lint, type-check, build, audit). No deploy step in
  the workflow file — deployment is presumably manual or external (see `docs/DEPLOYMENT.md`).

## Where things live

```
app/                              # Next.js App Router
  page.tsx                        # Marketing home (Hero/About/Services/Testimonials/CTA)
  layout.tsx                      # Root layout, wraps everything in UserProvider
  globals.css
  components/                     # APP-scoped components (NOT the root /components dir)
    Header.tsx Footer.tsx
    HeroSection.tsx AboutSection.tsx ServicesSection.tsx ...
    auth/AuthModal.tsx            # Mock auth UI
    courses/                      # Course catalog, lesson view, AI lesson chat, etc
    membership/MembershipUpsellModal.tsx
    payment/PaymentModal.tsx      # Mock payment
    AdminProtection.tsx           # Gate around /admin
  contexts/UserContext.tsx        # Mock user/session/membership/purchases
  reader/                         # Sovereignty Series book reader
    page.tsx                      # Volume index
    chapters.ts                   # Volume + chapter manifest (slug -> filename)
    [volume]/[slug]/page.tsx      # Reads MD from book/sovereignty-series/...
    components/ChapterContent.tsx ChapterSidebar.tsx
  courses/                        # Course pages
    page.tsx
    [courseId]/page.tsx
    [courseId]/dashboard/page.tsx
  admin/                          # Admin/CMS UI (gated by AdminProtection)
    page.tsx                      # Dashboard with dummy analytics
    ai/  analytics/  community/  courses/  media/  services/  settings/  users/
  book/page.tsx essence/page.tsx library/page.tsx schedule/page.tsx

components/admin/SacredUI.tsx     # Reusable admin primitives (SacredCard/Stat/Button)
                                  # NOTE: this is the root /components dir; app/components/ is separate
hooks/                            # useCourseProgress, useLessonProgression, usePerformance
data/
  lessons/rm1-*.ts                # Rose Meditation Level 1 lesson data (typed Lesson)
  admin/dummyData.ts              # Dummy analytics for admin dashboard
  sample-lessons.ts
types/course.ts                   # Lesson, Course types
context/                          # Project-wide design docs (NOT React context)

book/                             # Editorial workspace — non-code
  sovereignty-series/
    vol-1-see/                    # ACTIVE. The Narcissism Decoder.
      chapters/01-opening-manifesto.md ... 17-moving-forward.md
      00-front-matter.md back-matter-about-author.md
      companion-workbook/         # Workbook companion (parts + appendices)
      vignettes/  appendices/  drafts/  marketing/  course/  epub/
      review-01..05/              # Editorial review iteration outputs
      review-state.json           # Tracks which reviews have run
      vol-1-complete-manuscript.md          # ~16k lines, the merged manuscript
      vol-1-complete-manuscript.md.backup   # Pre-edit safety copy
      vol-1-see.docx vol-1-see.epub         # Exports for KDP
      hispanic-cultural-integration-proposal.md
      lgbtq-woven-integration-proposal.md
      unified-woven-integration-plan.md     # Active integration program
      legal-review-vol-1.md
      convert_to_docx.py
    vol-2-heal/ ... vol-9-insight-control/  # Scaffolds, varying maturity
  agents/                         # Editorial agent personas (developmental, line,
                                  # copy, proofreader, sensitivity, fact-checker,
                                  # beta-reader, managing-editor, legal-review-advisor)
  release/                        # KDP/marketing/launch assets, decoder cards giveaway,
                                  # cover specs, content calendar, social templates
  integration-materials/          # Per-volume "additions" decks
  energy-series/                  # Future series plan
  raw/                            # Author's raw transcripts/notes (input material)
  reference-guides/  reviews/  deprecated/

docs/                             # Brand identity, deployment, course/admin guides
context/design-principles.md      # Design doctrine
scripts/                          # md_to_docx.py, review-github-integration.sh
public/                           # Static assets
content/                          # GITIGNORED — large video files (e.g. About-The-Roses.mp4)
.claude/                          # .claude/agents/publishing-attorney.md +
                                  # .claude/commands/* (project slash commands)
.cursor/                          # Cursor rules (referenced from old AGENTS via @-imports)
```

## Current focus (per recent commits — read before assuming anything)

The active work stream is **Vol 1 cultural & structural integration**:
- Cultural-coverage adaptation (LGBTQ+, Hispanic, six underserved communities) being
  woven into the existing Vol 1 manuscript via the "unified woven integration plan."
- Phased structural passes (Phases 2-5) adding field notes, vignettes, subsections to
  specific chapters (Ch 3, 5, 7, 8, 9, 10, 11).
- Recent terminology pass: `queer` → `LGBTQ+` in taxonomic voice only (see PR #419).
- Author branding: 3-layer identity (Jae Lawless / Auracle / Jennifer); KDP Amazon is
  publisher (Auracle is NOT publisher — see commit 918832a).
- Migrating appendix references to companion website (Phase 5).

The pattern: open a `claude/<short-slug>` branch, do one focused editorial pass, merge
PR. Commits use a leading emoji (✨ feature, 🐛 fix, 📝 docs, 🎨 style, 🔄 revert,
🗑️ remove, 🧹 cleanup, 📚 content, 📦 build/release, 🔧 chore, 📸 asset).

App-code work has been quiet for weeks — the platform is in maintenance while content
is the focus. Don't refactor app/ speculatively.

## Conventions

- **Commit format:** `{emoji} {imperative verb} {concise description}`. Look at
  `git log` before writing one. Examples:
  - `✨ Phase 4.5: Ch 11 — Public Scenes voice activation + Tier 1`
  - `🐛 Remove Auracle-as-publisher references`
  - `📝 Move appendixes to website, anonymize sibling references in Vol 1 plan`
- **Branch naming:** `claude/<kebab-slug>-<rand>` (matches the auto-generated worktree
  branches; harmless if you create your own). Open a PR back to `main`.
- **Pre-commit will fail your commit if `tsc --noEmit` errors or eslint can't fix.**
  Don't pass `--no-verify` — fix the type/lint issue.
- **Quality check in CI greps for `console.log`** in `app/` and `components/`. Strip
  them before committing or your PR's quality job will warn.
- **Volume manifest is hand-curated** in `app/reader/chapters.ts` — when chapters are
  added/renamed in `book/sovereignty-series/vol-N/chapters/`, update `chapters.ts` so
  the reader route can find them.
- **Manuscript edits go to chapter files first, then re-merge into
  `vol-N-complete-manuscript.md`.** The complete-manuscript file is a build artifact
  in spirit but committed in practice. If you edit it directly, also update the
  source chapter file or the next merge will overwrite you.
- **Volume IDs are inconsistent between code and book/.** `app/reader/chapters.ts`
  uses `vol-1-decoder`, `vol-2-bridge`, etc. The folder names use `vol-1-see`,
  `vol-2-heal`, etc. Both are intentional (reader-facing vs editorial). Don't
  "fix" the mismatch without checking both places.

## Gotchas

- **Two `components/` directories.** `/components/admin/` (root) holds shared admin UI
  primitives (`SacredUI.tsx`). `/app/components/` holds App-Router-scoped components.
  Imports from admin pages use `../../components/admin/SacredUI`. Don't merge them.
- **`UserContext` is purely client-side.** All "auth," "purchases," "membership" state
  is in `localStorage`. `hasPurchasedCourse` / `hasActiveMembership` are boolean
  fictions. Anything that looks like a real user system isn't.
- **Chapter content is server-side fs-read at request time** (see
  `app/reader/[volume]/[slug]/page.tsx`) from `book/sovereignty-series/...`. This
  works in dev and in `next build` only because everything ships in the repo. Do not
  delete or reorganize `book/sovereignty-series/<vol>/chapters/` filenames without
  also updating `app/reader/chapters.ts`.
- **`content/` is gitignored.** Large video files (e.g. `About-The-Roses.mp4`
  referenced from lesson data) are not in the repo. Lesson playback won't work
  locally without populating `content/`.
- **TypeScript is `strict: false`.** Type errors are loose. CI runs `tsc --noEmit`
  but only catches hard errors, not soft inference holes.
- **Branch `claude/doctrine-bootstrap` is far ahead of `main` (~937 commits).** It is
  a long-lived integration branch. **Branch from `main` for normal work**, not from it.
- **Local `main` lags origin/main heavily.** Always `git fetch && git checkout
  origin/main` (or rebase) before branching. The local clone is rarely current.
- **Cover images, designer briefs, and KDP assets are in `book/release/`** — when
  asked about marketing/launch, look there before grepping the codebase.
- **Editorial review iterations live as numbered folders** (`review-01/` through
  `review-05/`, plus phased subdirs `review-03-phase-1..4/`). `review-state.json`
  tracks what's been done. Don't rerun a review pass without checking that file.
- **`dummyData.ts` is real-looking but fake.** Admin dashboard analytics are dummy
  values; do not surface them to users as real metrics.

## Don'ts

- **Don't rename volume folders or chapter filenames** without grepping
  `app/reader/chapters.ts` and updating it. Reader routes will 404.
- **Don't touch `vol-1-complete-manuscript.md.backup`.** It's the safety copy.
- **Don't add `console.log` to `app/` or `components/`.** CI quality job greps for it.
- **Don't refer to Auracle as the book's publisher.** KDP/Amazon is publisher,
  Auracle is the author's brand. (See commits 918832a, 670ca43.)
- **Don't push to `main` directly. Don't merge to main without explicit approval.**
- **Don't commit `.docx`/`.epub` regenerations as a side effect** of unrelated edits —
  they're large binaries. Regenerate explicitly when shipping.
- **Don't run `npm run dev` or `npm run build` from the root checkout** if other
  Claude sessions might be active in this repo — use a worktree (see CLAUDE.md).
- **Don't introduce a real auth/payment provider** without an explicit task. The mock
  flows are intentional placeholders.

## Secrets

- `.env*` is gitignored. There are currently no documented runtime secrets — the app
  runs fully client-side with mock auth and mock payments. If you add a real provider,
  put keys in `.env.local`, never inline, never in tests.
- Don't commit author personal data, reader testimonials with real names, or PII from
  raw transcripts in `book/raw/` to anywhere public-facing without checking the
  legal-review and sensitivity-reader passes (see `book/agents/legal-review-advisor.md`,
  `book/sovereignty-series/vol-1-see/legal-review-vol-1.md`).
