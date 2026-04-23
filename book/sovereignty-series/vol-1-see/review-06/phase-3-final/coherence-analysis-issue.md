# Coherence Analysis — Round 6 Phase 3

**Title:** `[Review Round 6 - Phase 3] Coherence Analysis: Cross-Manuscript Consistency Audit — Vol. 1`

**Labels:** `review-round-6`, `phase-3-coherence`, `author-input-required`

**Repository:** light-brands/auracle

**Depends on:** Phase 1 (Diana) and Phase 2 (Lydia) signoff. Coherence can only be evaluated on the final, post-edit text.

---

## Overview

This is Coherence Analysis — the Phase 3 audit of Round 6. Unlike Diana (architecture) and Lydia (voice), my job is mechanical and complete: verify that every cross-reference resolves, every term is used consistently, every number agrees with every other number, and the bibliography lists every work cited.

**Why last:** Coherence defects can only be audited against a frozen text. Any structural or line-level change introduced by Phases 1 and 2 can introduce drift. I catch that drift.

---

## Scope

### Terminology Consistency

- **"Trauma bond"** (noun) vs. **"trauma bonding"** (process) — Round 5 Clara Q4 standardized this. Audit every instance across 17 chapters and 7 appendices.
- **"Decoder Protocol"** — 4 steps (Notice → Pause → Decode → Respond). No 5-step or 6-step residues.
- **"Modules"** — 6 of them. No references to "5 modules" or "six core modules + one advanced" or similar variants.
- **Card counts** — 52 base cards (28 Core + 24 Advanced); 60 total patterns (52 base + 4 digital + 4 substance). Both counts are valid depending on context. Audit that each appearance uses the right count for its context.
- **Lesson numbering** — 3.1a / 3.1b / 5.4 / 5.5 / 6.1–6.4 — all cross-references match.

### Cross-Reference Accuracy

- Every "(see Chapter X)" / "(Chapter Y)" / "as we covered in Ch. Z" resolves to the right chapter. Chapter numbers changed in the 9/10 reorder and 14–17 renumbering — audit thoroughly.
- Every "(see Lesson X.Y)" resolves to an existing lesson file.
- Every "Card N" reference resolves to the card now at position N in Ch 3.
- Every appendix reference ("see Appendix A: Resources", etc.) matches the current appendix letter.

### Bibliography Completeness

- Every cited author in the running text (Walker 1979, Carnes 1997, LeDoux 1996, Strutzenberg 2017, Balban/Stanford 2023, Dunbar 1992) has an entry in Appendix C.
- No Appendix C entry lacks at least one in-text citation (or is clearly framed as "further reading").

### Numerical Consistency

- Duration claims (~11 hours, Module durations in curriculum) add up.
- "50–150 people" (Dunbar): stated consistently.
- Percentages and statistics quoted verbatim across contexts.

### Resource Consistency

- **Crisis hotline:** 1-800-799-7233, 741741 (Crisis Text Line), thehotline.org, and TTY 1-800-787-3224 listed consistently. No stale versions of any number.
- In-book safety boxes use the same resource list as Appendix A.

### Appendix Sync

- Appendix A (Resources), Appendix E (Index), and running text in agreement on names and spellings.
- Appendix G (Pop-Culture References) exists in both chapters.ts and the manuscript bundle.
- Appendix F (Substance Patterns) cross-references: S-1..S-4 cards match the chapter-3 listings.

---

## Inputs

- `vol-1-complete-manuscript.md` (re-bundled April 23, 2026; should match post-Phase-2 state)
- `chapters/*.md`, `appendices/*.md` (source of truth)
- `app/reader/chapters.ts` (for URL-slug consistency cross-check)
- Round 5 decisions for context on what _should_ be consistent after integration

---

## Deliverable

A single `author-decisions-coherence.md` file containing:

- A defects list (severity, location, proposed fix)
- A sign-off section confirming every item is resolved or acknowledged
- A diff summary of any terminology or numbering changes I recommend applying

Document responses in:
`review-06/phase-3-final/author-decisions-coherence.md`

---

## Out of Scope

- Anything subjective (voice, rhythm, arc) — that was Diana and Lydia
- Factual accuracy of claims — that was Felix in Round 5
- Spanish translation
- Course lessons (except where book-to-course cross-references need sync)

---

_Template prepared: April 23, 2026. To be run after Phases 1 and 2 are signed off._
