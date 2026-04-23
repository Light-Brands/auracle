# Review Round 6 — Vol. 1: See

**Status:** Scaffolded (awaiting Phase 1 kickoff)
**Date Prepared:** April 23, 2026
**Scope:** Full manuscript (~120K words, 17 chapters + 7 appendices) after Round 5 integration

---

## Overview

Review Round 6 is a full-manuscript editorial pass performed on top of a Round 5 that completed all 160 author decisions across four phases. With the heavy structural, representation, fact-check, and polish work landed, Round 6 narrows the roster to three agents — developmental, line, and coherence — and asks each to evaluate the manuscript as a whole rather than chapter-by-chapter.

Unlike Round 5, Round 6 is **not** a split four-phase process. It is a sequential three-phase pass: a top-down developmental pass (Diana) precedes a bottom-up line pass (Lydia), with Coherence Analysis performing a final consistency check across the whole.

---

## Prerequisites

Before starting Review Round 6:

- [x] Review Round 5 Phases 1–4 decisions complete (160/160)
- [x] Round 5 implementation complete (all nine reviewers' flags flipped)
- [x] `vol-1-complete-manuscript.md` re-bundled from current chapters after Round 5 integration
- [x] `review-state.json` reconciled (paths, repo, `roundStatus: complete`)
- [ ] `reviewRound` bumped to 6 and new `phases` tree populated (Phase B2)

---

## Phase Structure

### Phase 1: Developmental Pass (Do First)

| Agent                        | Focus                                                             | Issue Template                                          |
| ---------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| Diana (Developmental Editor) | Structure, arc, pacing, reader journey across the full manuscript | `phase-1-strategic/diana-developmental-editor-issue.md` |

**Why first:** Developmental issues cascade downstream. Any structural or arc-level changes Diana recommends must land before Lydia starts — line-level polish on text that may be moved or rewritten is wasted effort.

**Exit criterion:** Diana's author-decisions file signed off. No open Phase 1 items before Phase 2 begins.

### Phase 2: Line Pass (After Phase 1 Signoff)

| Agent               | Focus                                                      | Issue Template                              |
| ------------------- | ---------------------------------------------------------- | ------------------------------------------- |
| Lydia (Line Editor) | Voice, rhythm, sentence-level craft, emotional calibration | `phase-2-polish/lydia-line-editor-issue.md` |

**Why after Phase 1:** Line editing locks wording. Do it after any structural changes have settled.

**Exit criterion:** Lydia's author-decisions file signed off.

### Phase 3: Final Coherence Check (After Phase 2 Signoff)

| Agent              | Focus                                                                                | Issue Template                              |
| ------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------- |
| Coherence Analysis | Cross-chapter consistency, terminology, cross-references, bibliography/appendix sync | `phase-3-final/coherence-analysis-issue.md` |

**Why last:** Coherence can only be judged on the final text. Any cross-reference drift introduced by Phases 1 and 2 gets caught here.

**Exit criterion:** Zero coherence defects, or all defects acknowledged with a disposition.

---

## Context Handoff to Agents

Each agent should be briefed with:

1. **The current manuscript** — `vol-1-complete-manuscript.md` (re-bundled April 23, 2026)
2. **Round 5 decisions** — `../review-05/phase-{1,2,3,4}-*/author-decisions*.md` (nine files)
3. **Round 5 implementation checklist** — `../review-05/master-implementation-checklist.md`
4. **Round 5 state snapshot** — `../review-state.json` prior to Round 6 bump (see git history)

Agents should **not** re-adjudicate Round 5 decisions. Round 6 evaluates how those decisions landed and what, if anything, remains for a future revision.

---

## Labels

| Label                   | Meaning                   |
| ----------------------- | ------------------------- |
| `review-round-6`        | All Round 6 issues        |
| `phase-1-developmental` | Diana                     |
| `phase-2-line`          | Lydia                     |
| `phase-3-coherence`     | Coherence Analysis        |
| `author-input-required` | Awaiting author decisions |

---

## Success Criteria

Round 6 is complete when:

- All three author-decisions files exist and are signed off.
- All recommended changes are either implemented or explicitly deferred to a future edition.
- `review-state.json` for Round 6 matches the pattern of Round 5's closeout (`roundStatus: complete`, all `implementationComplete: true`, `completedAt` set).
- Manuscript is declared ready for the next publication milestone.
