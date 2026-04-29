# Round 7 Phase 1 — Implementation Plan & Author Triage

**Status as of:** 2026-04-27
**Branch:** `claude/review-volume-one-nO2cx`
**Recent commits:** `a99df36` (pre-Phase-2 audits + Felix initial), `e021a14` (provisional resolutions), `3b9ceb6` (author decisions), `7712a0a` (Diana + Morgan reviews), `40e8e9f` (Round 7 skeleton)

This document is the working plan for the next batch of Round 7 work. It captures what's complete, what's blocked, and the proposed implementation sequence. Author review and triage requested before manuscript edits begin.

---

## What's complete

### Phase 1 strategic review (committed)
- `review-07/README.md` — Round 7 charter (book, not course)
- `review-07/review-state.json` — phase plan, reviewer roster
- `review-07/review-workflow.md` — phase checklist
- `review-07/phase-1-strategic/diana-developmental-editor-issue.md` — 15 questions, 5 sections
- `review-07/phase-1-strategic/morgan-managing-editor-issue.md` — 11 coordination questions, 4 sections, risk register
- `review-07/phase-1-strategic/author-decisions.md` — all 26 decisions, 5 PROVISIONAL flags resolved 2026-04-27 (Vol 2 = drafted, launch = open, fatigue = not a constraint)

### Pre-Phase-2 audits (committed)
- `review-07/pre-phase-2/sibling-anonymization-audit.md` — Diana Q13
- `review-07/pre-phase-2/website-parity-baseline.md` — Morgan Q3
- `review-07/pre-phase-2/round-5-implementation-audit.md` — Morgan Q2
- `review-07/pre-phase-2/standing-decisions-re-ratification.md` — Morgan Q8 (template; awaiting author marks)

### Phase 2 (parallel) initial deliverable (committed)
- `review-07/phase-2-content/felix-fact-checker-initial-issue.md` — 12 questions on stable content; full pass deferred until Phase 1 settles

---

## Audit findings that gate Phase 1 implementation

### Confirmed must-fix violations

| Finding | Source | Action |
|---------|--------|--------|
| **Ch 8 Testimony uses "her siblings" twice** (lines 7140, 7148) | Sibling audit | Violates SD-3. Author selects Option A / B / C below. |
| **Appendices A–F still in printed manuscript** (lines 13553–15703) — migration was planned, never executed | Website parity baseline | Author triages 6 questions (URL, web team, glossary/bib fates); then Batch 1 implements. |
| **R5 Q8 "baby-trap" male example never reached the manuscript** | R5 audit | Author chooses: implement now / defer to second edition / drop. |
| **Ch 14 ToC entry promises content that doesn't match Ch 14 body** | Diana Q3 audit | Already covered by Diana Q3 decision A (rewrite ToC entry). Mechanical fix in Batch 4. |

### Author triage requested before Batch 1 begins

Five blockers. Each is a brief author decision:

**TR-1. Ch 8 Testimony fix.** The Testimony violates standing decision #3 ("no sibling label, no named role").
- [ ] **A** — `her siblings` → `her family`
- [ ] **B** — `her siblings` → `her family members`
- [ ] **C** — Cut the protect-them clauses; reframe the moral injury without the named role

**TR-2. Ch 8 wedding passage** at lines 7240–7242 ("first sister got married… second sister got married years later"). Biographical or composite?
- [ ] **Biographical** — rewrite to remove sibling role (e.g., "the first daughter / the second daughter," "one woman / years later, another," or fold into one figure)
- [ ] **Composite** — no action; sibling labels permitted in composite material

**TR-3. Companion website URL** for Strategy 2 references (used ~2–3 times, once per relevant chapter at most). Examples: `jaelawless.com/see-resources`, `auracle.app/resources`, etc.
- Author specifies: _________________________________

**TR-4. Glossary / Bibliography / Techniques Reference fates.** Master plan migrates everything; trade-nonfiction convention often keeps these printed.
- [ ] **Glossary (Appendix B)** — migrate / keep printed
- [ ] **Bibliography (Appendix C)** — migrate / keep printed / hybrid (curated 5–10 printed, full list on website)
- [ ] **Techniques Reference (Appendix D)** — migrate / replace with cross-references to Ch 15–16 / keep printed

**TR-5. R5 Q8 baby-trap male example.** Two cases author had specified (loving man manipulated; man choosing partners with limited English proficiency).
- [ ] **Implement** in Phase 1 — author provides finalized prose; integrate into Ch 11 as field notes (pairs with Diana Q11 + Q14)
- [ ] **Defer** to second edition
- [ ] **Drop**

### Audit-stage author actions (no triage; just sign-off)

- **Standing decisions re-ratification** (`standing-decisions-re-ratification.md`) — author marks each SD as STILL HOLDS / REVISED / RETIRED. ~10 minutes. Required before Phase 2 main work launches.

---

## Worktree decision (CLAUDE.md compliance)

CLAUDE.md mandates `bin/qie worktree auto <slug>` before editing chapter MD files under `book/sovereignty-series/vol-N/chapters/` because other Claude sessions run editorial passes concurrently. Skipping the worktree risks mid-edit collisions.

**Proposed:** I run `bin/qie worktree auto round-7-phase-1` and proceed there. Idempotent if the worktree already exists.

**Author confirms:**
- [ ] Yes — proceed with worktree
- [ ] No — proceed on current branch (acknowledging collision risk)
- [ ] Pause — handle worktree manually first

---

## Phase 1 implementation sequence (9 batches)

Each batch is one work session minimum. Re-merge into `vol-1-complete-manuscript.md` happens per-chapter (Morgan Q5 decision B).

### Batch 1 — Mechanical, low-risk (highest public-trust impact)
**Goal:** Resolve the must-fix violations.
- Ch 8 Testimony fix (per TR-1)
- Ch 8 wedding passage (per TR-2 if biographical)
- Appendix A–E ToC entry removal (lines 122–130)
- 12 in-body "see Appendix A" cross-references rewired per `website-parity-baseline.md` (Strategy 1 = timeless statement, Strategy 2 = single companion URL)
- Appendix F (Substance-Related Patterns) retained; relocated header per Diana Q12 decision B
- Appendix bodies A–E either deleted from manuscript or kept until website confirms parity (depends on TR-3, TR-4)

**Estimated effort:** 1 work session.
**Dependencies:** TR-1, TR-2, TR-3, TR-4 resolved.

### Batch 2 — Part architecture (Diana Q1)
**Goal:** Six-Part book structure.
- Promote Ch 7–10 (Family Roles, Parental Wounds, Childhood Patterns, Breaking Free) into a new Part — proposed name "Part III: Family Systems" (or author specifies)
- Absorb current Part IV (Ch 14 standalone) into Part III "Patterns in Context"
- Renumber Parts: I Recognition / II Origins / III Family Systems / IV Patterns in Context / V Tools / VI Recovery & Response
- Update ToC, Pause interlude framing, Part header banners

**Estimated effort:** 1 work session.
**Dependencies:** Batch 1 complete (so Part-renumber doesn't conflict with appendix header changes).

### Batch 3 — Ch 3 split (Diana Q10)
**Goal:** Split Ch 3 into 3a (Core Patterns 0–27) and 3b (Advanced & Specialized 28–51 + D + P + S).
- Use the existing internal Part 1 / Part 2 / Part 3 sub-banners as natural split points
- Renumber subsequent chapters (Ch 4 → Ch 5, etc., propagating to Ch 17 → Ch 18)
- Cora flags every chapter cross-reference for update (Phase 3)
- ToC entries refreshed

**Estimated effort:** 1 work session, plus a renumber audit.
**Dependencies:** Batch 2 (Parts settled before chapter renumber).

### Batch 4 — Ch 14 reframe + Pause cadence (Diana Q2, Q3)
**Goal:** Ch 14 = Emergency Protocol only; Pauses cadence rebalanced.
- Update Ch 14 ToC entry (drop card sub-bullets; cards live in Ch 3a/3b)
- Move post-Ch-14 Pause to before Ch 15 (now between Part V Tools and Part VI Recovery)
- Verify the four-Pause cadence still hits Part boundaries

**Estimated effort:** 1 work session.
**Dependencies:** Batch 3 (chapter numbers stable).

### Batch 5 — Woven thesis as architecture (Diana Q5)
**Goal:** Promote the thesis from front-matter sidebar to load-bearing.
- Draft a thesis section in Ch 1 (~400–600 words) integrating without disturbing existing manifesto beats
- Draft Part-header beats — one per Part transition (6 beats post-restructure) — surfacing the thesis at hinge points
- Author reviews drafts; revisions before commit

**Estimated effort:** 1–2 work sessions (drafting + author revision cycle).
**Dependencies:** Batch 2 (Parts settled, so Part headers stable).

### Batch 6 — Cultural integration deepening (Diana Q6, Q7)
**Goal:** Eliminate cultural-content zero-instance chapters; extend the woven thesis through the recovery arc.
- 6–8 new field notes targeted at currently-zero chapters (Ch 4 Trauma Bonds, Ch 5 Narcissist Types, Ch 9 Childhood Patterns)
- 4–6 cultural-context field notes for Ch 15 Energetic Remapping and Ch 16 Practical Responses
- A "Recovery Across Contexts" section in Ch 17 (~600–900 words)

**Estimated effort:** 2–3 work sessions (extensive new prose; author voice required).
**Dependencies:** Batch 5 (Ch 1 thesis frame in place to anchor field-note voicing).

### Batch 7 — Field note rebalance + author voice (Diana Q8, Q11, Q14)
**Goal:** Ch 2 trim, Ch 11 build, voice beats in Ch 11 + Ch 16.
- Audit Ch 2's 17 field notes; consolidate or relocate 5–7 to other chapters
- Add 4–6 field notes to Ch 11 spanning integration plan contexts
- Add author first-person voice beats to Ch 11 (3–5 places); draft samples for Ch 16 (author keeps/vetoes per beat)
- If TR-5 = implement, integrate baby-trap example here

**Estimated effort:** 2–3 work sessions.
**Dependencies:** Batch 6 (cultural integration patterns established; voice consistent across new prose).

### Batch 8 — Closing + Vol 2 bridge + front matter (Diana Q4, Q15, Q9)
**Goal:** Ch 17 ending rewrite, Vol 2 bridge against actual Vol 2 chapters, front-matter Notes consolidation.
- Move bio paragraph from Ch 17 closing to About the Author section
- Draft three candidate closing lines (author selects); replace the third "superpower" repetition
- Draft "What Comes Next" Vol 2 bridge section (~400–600 words) referencing actual Vol 2 chapters: minimal contact (Ch 12), grief (Ch 15), reparenting (Ch 22), secure attachment training (Ch 21)
- Audit Vol 1's "Course 2" / forward-reference language (pairs with Felix Q12)
- Consolidate front-matter "A Note on…" sections (six → one) per Diana Q9

**Estimated effort:** 1–2 work sessions.
**Dependencies:** Batches 5–7 settled (consistent voice across closing).

### Batch 9 — Final implementation pass + reconciliation matrix
**Goal:** Cleanup before Phase 2 main work begins.
- Final audit of all chapter cross-references after renumber
- Vol 1 → Vol 2 reconciliation matrix produced (Morgan Q11 deliverable; consumed by Vol 2 future review work)
- `review-state.json` updated to reflect Phase 1 implementation complete
- Round 5 prior-state file marked superseded per R5 audit recommendations

**Estimated effort:** 1 work session.
**Dependencies:** All prior batches.

---

## Total estimated effort for Phase 1 implementation

**Lower bound:** 11 work sessions if author triages cleanly and revisions are light.
**Upper bound:** 14–16 work sessions if Batches 5–7 require multiple author revision cycles on new prose.

This is significantly more work than a single Claude session can complete in one turn. The proposed cadence is one batch per session, with author review at each batch boundary.

---

## After Phase 1 implementation closes

1. **Phase 2 main launch** (Bailey beta + Sage sensitivity validation + Felix full fact-check). Felix already has an initial pass committed; he expands once chapters are stable.
2. **Phase 3** (Lyra → Cora) per Morgan Q6 sequence.
3. **Phase 4** (Penny + companion website parity verification) per Morgan Q3 + Q10.
4. **Round 7 close:** editorial + production artifacts (`.docx`, `.epub` regenerated) + tagged release `vol-1-see/round-7-complete` per Morgan Q10 decision B+D.

---

## Author review checklist

Before I proceed with Batch 1, please confirm:

- [ ] Worktree decision (proceed / pause / handle manually)
- [ ] TR-1 Ch 8 Testimony fix (A / B / C)
- [ ] TR-2 Ch 8 wedding passage (biographical / composite)
- [ ] TR-3 companion URL
- [ ] TR-4 glossary / bibliography / techniques reference fates
- [ ] TR-5 baby-trap example (implement / defer / drop)
- [ ] Standing decisions re-ratified (template at `review-07/pre-phase-2/standing-decisions-re-ratification.md`)
- [ ] Implementation sequence — proceed batch-by-batch as proposed, or reorder?

When the above is signed off, I start Batch 1.

---

*Plan drafted by Claude on behalf of Round 7 coordination.*
*Last updated: 2026-04-27.*
