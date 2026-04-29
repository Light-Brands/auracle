# GitHub Issue: Morgan (Managing Editor) - Phase 1 Strategic Review

**Title:** `[Review Round 7 - Phase 1] Morgan (Managing Editor): 11 Coordination Questions - Vol. 1 (Book Edition)`

**Labels:** `review-round-7`, `phase-1-strategic`, `author-input-required`, `book-edition`

**Repository:** Light-Brands/auracle

---

## Overview

I'm Morgan, your managing editor. I don't redline prose. My job is to keep the round coherent — make sure reviewers don't trip over each other, decisions don't get lost, and the work that needs to happen first happens first.

Round 7 is a different shape than Rounds 1–5. Earlier rounds were framed against a video curriculum and ran phases against an evolving artifact. Round 7 reads Vol 1 as a finished book and produces a single coordinated pass before downstream production work (regenerated `.docx`, `.epub`, possible second-edition print). The integration plan and Round 6 closed; Round 7 inherits a manuscript that has settled.

That settling creates a coordination question I want to surface up front: **the book has stopped moving, but the implementation backlog from Round 5 hasn't fully closed.** The Round 5 `review-state.json` still has reviewer entries with `implementationComplete: false`. Either Round 7 absorbs those open items, or we explicitly defer them. We can't pretend they're not there.

My questions cluster into four categories: (A) Round 7 charter and what's in scope, (B) sequencing and dependencies between phases, (C) conflict pre-resolution between reviewers (Diana, Sage, Lyra all have potential to disagree), and (D) close criteria and risk register. I keep the questions answerable in one pass — multi-select with brief rationale, not "discuss further."

A note on Diana: she is also producing her review in parallel with mine. Her recommendations may include restructuring proposals (Part rebalancing, Ch 14 reframing, Ch 3 split). My questions assume her review is advisory; final decisions are yours. Some of my questions ask you to decide *how* her recommendations are routed — implemented in Round 7 or deferred to a Round 8 / second edition.

**Why this phase matters:** Coordination decisions made now prevent compounding rework in Phases 2–4. A reviewer in Phase 3 polishing prose that Phase 1 will restructure has wasted their pass. Order of operations matters more than the operations themselves.

---

## How to Respond

For each question:
1. Select your preferred option (or write your own under "Author Response").
2. Add brief reasoning where the choice isn't obvious.
3. Answer any clarifying questions.

**Response location:** `book/sovereignty-series/vol-1-see/review-07/phase-1-strategic/author-decisions.md`

---

## Section A: Round 7 Charter and Scope (Q1–Q3)

### Q1: Round 7 Scope — Full Pass vs. Selective

**Context:** A full top-to-bottom round invokes 8 reviewer agents across 4 phases:

| Phase | Reviewers |
|-------|-----------|
| 1. Strategic | Diana, Morgan |
| 2. Content & Experience | Bailey, Sage, Felix |
| 3. Prose Polish | Lyra, Cora |
| 4. Final | Penny |

Round 5 ran 7 reviewers and produced 160 author questions. Round 6 was a single-reviewer focused refresh.

**The Question:** What's the actual scope of Round 7?

**Options:**
- [ ] A) **Full 8-reviewer top-to-bottom pass.** All four phases, all reviewers, against the full manuscript.
- [ ] B) **Phase 1 + Phase 3 + Phase 4 only.** Skip Phase 2 (Bailey/Sage/Felix) — Round 6 just closed Sage; beta and fact-check defer to Round 8.
- [ ] C) **Phase 1 + Phase 2 + Phase 4.** Skip Phase 3 prose polish until Phase 1 restructuring decisions are implemented; have Penny do final-pass cleanup as a substitute.
- [ ] D) **Diana's review drives scope.** Hold scoping until Diana's review lands; if she recommends major restructuring (Q1, Q3, Q10 in her review), Round 7 becomes restructure-then-stop and Phase 3/4 defer to Round 8.
- [ ] E) **Selective: pick 3–5 highest-value questions across all phases.** Bound the round at ~30–40 author decisions instead of ~150.

**Editor Comments:**
Three external pressures shape this:

1. The author has been through six review rounds. Marginal value of a comprehensive eighth-reviewer pass is real but diminishing. The right question is: what does this round catch that Round 8 (after a real-world reader response cycle) wouldn't catch better?
2. Diana's review (running parallel to this one) may surface restructuring recommendations significant enough that Phase 3 prose polish would be wasted work. Locking Round 7's scope before her review lands is premature.
3. The integration plan implementation closed recently. There is meaningful "settling time" value in *not* immediately running another full pass — let the prose breathe, let early readers respond, then run Round 8 against real reader signal.

**Editor Reasoning:**
Full pass is defensible if the author's intent is to produce a final-camera-ready Round 7. Selective is defensible if the author's intent is to validate that the integrated manuscript holds up. Diana-driven (D) is the most efficient path if you trust her judgment on scope; it lets her audit set the scope rather than pre-committing.

**Clarifying Questions:**
- Is Round 7 the last pass before regenerating publication artifacts (`.docx`, `.epub`) and potentially printing, or is there a Round 8 already planned?
- Are there external commitments (review copy delivery, beta reader cohort, marketing date) that anchor a hard deadline for Round 7?

**Proposed Action (upon approval):**
- **If A:** I'll launch Phase 2 reviewers immediately after Phase 1 author decisions land.
- **If B:** I'll skip Phase 2; sequence Phase 3 to start as soon as Phase 1 implementation is mostly complete.
- **If C:** I'll skip Phase 3; brief Penny on a heavier-than-usual final pass.
- **If D:** I'll hold all Phase 2/3/4 scoping until Diana's review is read and her restructure recommendations triaged.
- **If E:** I'll triage all 8 reviewers' typical question banks down to a 30–40 question bounded set.

**Author Response:**
_[Space for author to respond]_

---

### Q2: Carry-Over from Round 5 — Open Implementation Items

**Context:** The current `book/sovereignty-series/vol-1-see/review-state.json` (still showing Round 5 status) has these reviewer entries flagged `implementationComplete: false`:

- Diana (Developmental Editor) — Phase 1 Strategic
- Morgan (Managing Editor) — Phase 1 Strategic
- *(Phase 2/3/4 entries also show varying implementation states)*

The state file has not been updated to reflect what was actually done in the implementation phase that followed Round 5's decisions. It may overstate or understate completeness.

**The Question:** How should Round 7 handle Round 5's open items?

**Options:**
- [ ] A) **Audit Round 5 first.** Before Phase 2 of Round 7 launches, audit which Round 5 author decisions have been implemented and which haven't. Close completed items in the state file; carry incomplete items into Round 7 as known issues.
- [ ] B) **Defer Round 5 closure.** Leave Round 5 state as-is; treat Round 7 as a fresh pass against the current manuscript regardless of unresolved Round 5 commitments.
- [ ] C) **Roll Round 5 + Round 6 + Round 7 into a single closure.** Update both prior round state files at the start of Round 7, mark them all closed-by-supersession.
- [ ] D) **Author triages.** Author lists which Round 5 items were intentionally not implemented vs. forgotten; Morgan acts on the list.

**Editor Comments:**
Stale state files are not just clerical. They affect how Phase 2 reviewers calibrate their work. If Sage thinks a Round 5 sensitivity decision was implemented but it wasn't, her Phase 2 pass may build on a foundation that doesn't exist. Felix the fact-checker may verify claims against a manuscript version that never shipped.

The Round 6 (Sage refresh) README was clear: "the author's decisions have been implemented." That's the cleanest closure. Round 5's broader implementation status is less clear.

**Editor Reasoning:**
Round 7 inherits whatever's in the manuscript today. State files exist to tell future reviewers (and future you) what the manuscript was supposed to be. When state files lie, every subsequent round wastes time discovering the truth from the prose. Cheap to fix now; expensive to fix later.

**Clarifying Questions:**
- Is there a known list of Round 5 items that were deliberately not implemented (maybe parked for second edition)?
- Should Round 5's `review-state.json` and Round 7's `review-state.json` cross-reference each other?

**Proposed Action (upon approval):**
- **If A:** I'll produce a Round 5 implementation audit before Phase 2 launches; flag any items that affect Round 7 reviewer scope.
- **If B:** I'll log the deferral and notify Phase 2/3/4 reviewers that they're working against the current manuscript with no obligation to verify Round 5 promises.
- **If C:** I'll consolidate prior round closures into a single supersession note in Round 7's state.
- **If D:** I'll request the author's triage list and act on it.

**Author Response:**
_[Space for author to respond]_

---

### Q3: Companion Website Coordination

**Context:** Per the integration plan's standing decision, appendices are migrated to a companion website. The manuscript currently has 19 in-body cross-references to "Appendix A" and 6 ToC entries for appendices that don't exist in the printed book (Diana's Q12 covers this in detail). These references should resolve to website locations.

The companion website's source-of-truth document is `book/sovereignty-series/vol-1-see/website-appendixes-and-resources.md`. I have not verified whether the live website matches that document.

**The Question:** Who owns website-coordination during Round 7?

**Options:**
- [ ] A) **Round 7 verifies website parity.** Before Phase 4 (Penny) closes, audit that every in-book reference resolves to live website content with the correct URL pattern. Add to Penny's scope.
- [ ] B) **Out of Round 7 scope.** Website parity is a separate workstream owned by the marketing/web team; Round 7 only verifies the master document (`website-appendixes-and-resources.md`) is internally consistent.
- [ ] C) **Felix (fact-checker) owns it in Phase 2.** URLs and resource accuracy fall under Felix's remit. Add to Felix's brief.
- [ ] D) **Author owns it as a side-task to Round 7.** Round 7 reviewers note discrepancies; author resolves with the web team out-of-band.

**Editor Comments:**
This is a coordination question, not a content question. Whoever owns it needs the web team's contact, current URL structure, and a way to test that referenced resources are live. Round 7 reviewers don't have that context unless we give it to them.

The risk of leaving it unowned is that the printed book ships with broken cross-references. The risk of putting it in Penny's lap is that Penny doesn't have web-team access. The risk of giving it to Felix is that he has 30 other things to fact-check and this might slip.

**Editor Reasoning:**
Ownership decisions like this look small until they aren't. A single broken in-book URL is a five-star Amazon review at risk. Naming the owner now is cheap. Discovering at print time that no one owned it is expensive.

**Clarifying Questions:**
- Is the companion website live now, or in development?
- Is there a web team contact who would be available during Round 7's window?

**Proposed Action (upon approval):**
- **If A:** I'll add a website-parity verification step to Penny's Phase 4 brief.
- **If B:** I'll scope Round 7 to manuscript-internal consistency only; document the exclusion.
- **If C:** I'll expand Felix's Phase 2 brief to include website parity.
- **If D:** I'll log discrepancies as they're discovered and forward to the author.

**Author Response:**
_[Space for author to respond]_

---

## Section B: Sequencing and Dependencies (Q4–Q6)

### Q4: Strict Phase Gating vs. Selective Parallelism

**Context:** The Round 7 README specifies strict phase gating: Phase 2 starts after Phase 1 author decisions are recorded; Phase 3 starts after Phase 2 content changes settle; etc. This is the safe sequence — it prevents Phase 3 polish work on prose that Phase 2 might restructure.

But strict gating creates idle time. Felix (fact-checker) can validate sources, citations, and named patterns against text that won't change in Phase 2 (e.g., bibliography references, case-study attributions). His Phase 2 work doesn't depend on Phase 1 implementation in chapters he's checking.

```
Strict gating:                  Selective parallelism:
P1 → wait → P2 → wait → P3      P1 ──→ P2 (Bailey, Sage)
                                P1 ──→ P2 (Felix, in chapters not affected)
                                       └──→ P3 (in chapters not affected)
```

**The Question:** Do we strictly gate, or allow selective parallelism?

**Options:**
- [ ] A) **Strict gating.** Each phase finishes (and author decisions are recorded) before the next starts. Maximally safe.
- [ ] B) **Allow Felix (fact-check) to start in parallel with Phase 1.** Bibliography, citations, named patterns, statistics don't depend on developmental restructuring.
- [ ] C) **Allow Phase 3 (line + copy) to start on chapters Diana flags as architecturally stable.** If Diana's review identifies chapters where she has no structural recommendations (e.g., Ch 5 Narcissist Types), Lyra can start there immediately.
- [ ] D) **Allow Bailey (beta reader) to read in parallel with Phase 1.** Reader response doesn't depend on author decisions; her perspective informs Phase 1 decisions retroactively.

**Editor Comments:**
The downside of strict gating is calendar time. With Phase 1 → Phase 2 → Phase 3 → Phase 4 in series, Round 7 takes ~8 weeks minimum (one week per reviewer + author response time). Selective parallelism can compress to ~5 weeks at the cost of some rework risk.

The downside of selective parallelism is exactly that rework. If Lyra polishes Ch 5 in Phase 3 while Diana is still considering whether Ch 5 should be split (Q1 in her review), Lyra's polish becomes invalid.

This is a calibration decision. There's no universally right answer.

**Editor Reasoning:**
Strict gating is appropriate when the manuscript is unstable. Selective parallelism is appropriate when the manuscript is stable enough that most reviewers won't surface restructuring requests. After six rounds, this manuscript is closer to stable than unstable. But Diana's review is genuinely an open question right now — and her recommendations may be aggressive.

**Clarifying Questions:**
- Is calendar pressure a factor for Round 7?
- Are you willing to accept ~10% rework risk in exchange for ~30% calendar compression?

**Proposed Action (upon approval):**
- **If A:** I'll sequence reviewers strictly, build slack between phases.
- **If B:** I'll launch Felix in parallel with Phase 1, brief him to focus on stable content (citations, bibliography).
- **If C:** I'll wait for Diana's recommendations, identify stable chapters, launch Phase 3 there in parallel with author decisions on the unstable chapters.
- **If D:** I'll launch Bailey in parallel with Phase 1; her notes inform decisions before they close.

**Author Response:**
_[Space for author to respond]_

---

### Q5: Re-merge Cadence into the Assembled Manuscript

**Context:** Recent commit history shows a clear pattern from earlier integration phases:

```
Phase 4.8: Ch 11 — Exit Phase Escalation voice activation
Phase 4.7: Ch 11 — The Damage You Bring Forward
Phase 4.6: Ch 11 — The Dinner Party Silence field note
Phase 4.5: Ch 11 — Public Scenes voice activation + Tier 1
```

Each integration step touched a chapter file under `chapters/` and (presumably) re-merged into `vol-1-complete-manuscript.md`. The CLAUDE.md / AGENTS.md note: "edit the chapter file first, then decide whether to re-merge into `vol-N-complete-manuscript.md` (check recent commits for the pattern)."

For Round 7 implementation, multiple reviewers may produce edits across multiple chapters. Re-merging after every edit produces a clean per-step audit trail at the cost of merge conflicts when edits overlap.

**The Question:** What's the re-merge cadence for Round 7?

**Options:**
- [ ] A) **Per-edit re-merge.** Every chapter edit is followed by a re-merge into the assembled manuscript. Per-commit auditability; high merge-conflict risk if Phase 3 reviewers work in parallel.
- [ ] B) **Per-chapter re-merge.** A reviewer finishes their pass on a chapter, then re-merges. Lower conflict surface; chapter-level audit trail.
- [ ] C) **Per-phase re-merge.** Phase 2 finishes entirely → re-merge → Phase 3 starts. Lowest conflict risk; phase-level audit trail; longest gap between chapter source of truth and assembled view.
- [ ] D) **Reverse the relationship.** Treat `vol-1-complete-manuscript.md` as the source of truth; reviewers edit *it* and chapters get regenerated. Simpler for reviewers; breaks the existing chapter-first workflow.

**Editor Comments:**
Right now the workflow has the chapters as source-of-truth and the assembled file as a downstream artifact. That's a sound choice for editorial work — chapters are the unit of editing — but it means every implementation step that touches a chapter requires a corresponding re-merge step or the assembled file goes stale.

The Round 6 commit pattern suggests per-step re-merging is the operational default. It produces a lot of small commits (which is fine), but Round 7 with multiple parallel reviewers would create commit storms.

**Editor Reasoning:**
The operational tradeoff is between merge-conflict risk (high cadence) and assembled-file staleness (low cadence). Choose deliberately. Set the convention before reviewers start submitting edits. If the convention isn't set, each reviewer will pick their own and the result is non-recoverable conflicts.

**Clarifying Questions:**
- Are there active concurrent sessions on `vol-1-complete-manuscript.md` from other Claude workers (per the QIE worktree note in CLAUDE.md)?
- Is there a build/automation step that depends on the assembled file being current?

**Proposed Action (upon approval):**
- **If A:** I'll instruct Round 7 reviewers to re-merge after every edit; budget extra time per chapter.
- **If B:** I'll instruct per-chapter re-merge; reviewers complete a chapter pass before re-merging.
- **If C:** I'll instruct phase-end re-merges; reviewers work entirely on chapter files until phase close.
- **If D:** I'll re-document the workflow with assembled-file as source of truth; coordinate one-time chapter regeneration.

**Author Response:**
_[Space for author to respond]_

---

### Q6: Style Sheet Handoff Between Lyra and Cora

**Context:** Phase 3 has two reviewers: **Lyra** (line editor) focuses on prose craft, voice, rhythm, transitions, word choice. **Cora** (copy editor) focuses on grammar, consistency, internal continuity, style sheet creation.

In a normal editorial workflow, Cora produces the style sheet *during* her pass. Lyra works either before the style sheet exists (and ratifies the author's existing instincts) or after Cora has produced an interim sheet (and works against established conventions).

**The Question:** Who goes first in Phase 3, and how does the style sheet flow?

**Options:**
- [ ] A) **Lyra first, then Cora.** Lyra polishes prose; Cora creates the style sheet from the polished prose and enforces consistency.
- [ ] B) **Cora first, then Lyra.** Cora creates an interim style sheet documenting the author's current conventions; Lyra polishes against the sheet.
- [ ] C) **Parallel.** Both work simultaneously; Cora's style sheet is iterative and Lyra adapts as it grows. Highest coordination overhead.
- [ ] D) **Combine into a single reviewer/pass.** One reviewer doing both line and copy work; produces a combined deliverable. Sacrifices the depth of separate passes.

**Editor Comments:**
The conventional wisdom (Lyra → Cora) optimizes for prose quality. Cora's checking is mechanical enough that having stable prose to check makes her more effective. Lyra working first allows the prose to settle into its final voice before grammar conventions get locked.

The reverse (Cora → Lyra) optimizes for consistency. The author's current conventions get codified; Lyra works against documented conventions; final prose is consistent with what the style sheet will say.

For this manuscript specifically: the author has a strong existing voice (six rounds of revision). Lyra's value-add is targeted (transitions between integrated content and original prose, especially); Cora's value-add is significant (the manuscript has accumulated stylistic drift across rounds).

**Editor Reasoning:**
The decision depends on whether Round 7's primary risk is voice inconsistency (Cora-first protects against this) or prose roughness (Lyra-first protects against this). My read: voice inconsistency is the bigger risk after six rounds of accumulated edits.

**Clarifying Questions:**
- Is there an existing style sheet from any prior round, or is this a from-scratch pass?
- Has the author flagged specific conventions she wants protected (e.g., capitalization of "Pause and Integrate," italic conventions for field notes)?

**Proposed Action (upon approval):**
- **If A:** Sequence Lyra → Cora.
- **If B:** Sequence Cora → Lyra; Cora's first deliverable is an interim style sheet.
- **If C:** Launch in parallel; build a coordination protocol between them.
- **If D:** Combine into one Phase 3 pass with one reviewer carrying both responsibilities.

**Author Response:**
_[Space for author to respond]_

---

## Section C: Conflict Pre-Resolution and Decision Authority (Q7–Q9)

### Q7: Diana × Sage Conflict — When Developmental and Sensitivity Diverge

**Context:** Diana (developmental editor) and Sage (sensitivity reader) can both make recommendations on the same passage. Diana might say: "Cut this field note — it's redundant with the one in Ch 8." Sage might say: "Add a field note here — there's no representation of [context]." Their recommendations could land on the same paragraph and disagree.

In Round 5, both reviewers worked in different phases (Diana in Phase 1, Sage in Phase 2), so conflicts surfaced sequentially. In Round 7, if selective parallelism is enabled (Q4 Option D), they could surface simultaneously.

**The Question:** When Diana and Sage disagree on a passage, who wins by default?

**Options:**
- [ ] A) **Diana wins on architecture; Sage wins on representation.** If the disagreement is about whether a passage exists, Diana decides. If the disagreement is about what the passage says or how it represents identity, Sage decides.
- [ ] B) **Sage wins by default.** Sensitivity is a higher-stakes domain; representation errors compound into harm; Sage's flag is presumptive unless the author explicitly overrides.
- [ ] C) **Diana wins by default.** Structure is the foundation; sensitivity edits can be made within Diana's structural decisions; Sage's recommendations are scoped to what survives Diana's pass.
- [ ] D) **Author resolves every conflict.** Surface every Diana × Sage disagreement to the author; no default precedence.
- [ ] E) **Morgan resolves with author escalation only on disagreement.** Default to a precedence rule (likely A); author overrides specific conflicts on flag.

**Editor Comments:**
The integration plan's standing language about sensitivity is clear: "the goal is catch rather than rework" (from Round 6). That suggests Sage's flags are meant to be high-signal — when she flags, she means it. But it also suggests her flags don't override the manuscript's existing structure unless the structure itself is the problem.

In practice, most Diana × Sage conflicts are minor and can be resolved by Morgan (me) without author input. The ones that escalate are usually about whether a particular cultural representation is structurally adequate or merely present. Those go to the author.

**Editor Reasoning:**
Default precedence rules are how editorial workflows scale. Without them, every micro-conflict goes to the author and the author burns out before Phase 4. With them, the author handles only the genuine disagreements.

**Clarifying Questions:**
- Has there been a Diana × Sage conflict in any prior round you remember, and how was it resolved?
- Are there any sensitivity domains where you want Sage to win unconditionally (e.g., trauma framing)?

**Proposed Action (upon approval):**
- **If A:** I'll codify the architecture/representation split in the round's coordination doc.
- **If B:** I'll set Sage-presumptive precedence; route author overrides on case-by-case basis.
- **If C:** I'll set Diana-presumptive precedence; Sage's recommendations apply within Diana's frame.
- **If D:** I'll route every conflict to author; budget for author response time.
- **If E:** I'll set default precedence (probably A) with explicit escalation triggers.

**Author Response:**
_[Space for author to respond]_

---

### Q8: Standing Decision Override — When Reviewers Want to Re-litigate

**Context:** The integration plan contains standing decisions:

1. All appendices and resources go to the website.
2. Author sibling references are anonymized as "a family member."
3. The Ch 8 Testimony stays in book in close third or second person, attributed to "a family member."

Round 7 reviewers may surface recommendations that contradict standing decisions. Examples:
- Sage might recommend re-introducing a sibling label as part of representation (relatability of family identity).
- Diana might recommend reintroducing a printed Appendix to make cross-references resolve cleanly (her Q12 Option C).
- Felix might recommend citing a specific resource that contradicts the website-only rule.

**The Question:** Can reviewers' recommendations override standing decisions?

**Options:**
- [ ] A) **Standing decisions are binding.** Reviewers may flag for author awareness but cannot recommend changes that violate standing decisions; the standing decision document is canonical.
- [ ] B) **Standing decisions are presumptive but not binding.** Reviewers may recommend overriding; author resolves explicitly per case.
- [ ] C) **Round 7 re-ratifies standing decisions before reviewers begin.** Author confirms each standing decision still holds; updated decisions get propagated to all reviewer briefs.
- [ ] D) **Standing decisions are advisory only.** Reviewers treat them as background context; author makes all decisions in real time.

**Editor Comments:**
This question is about how much governance the standing decision document has. If it has full governance (A), the document is the spec and Round 7 reviewers work within it. If it has partial governance (B/C), Round 7 may produce author-facing decisions that re-open closed questions.

The risk of A: a standing decision made under different assumptions (e.g., "appendices go to the website" assuming the website was ready) may now be wrong, but no one can flag it.

The risk of B: every reviewer feels permissioned to re-open every standing decision; the round's question count balloons.

The risk of C: re-ratification takes time and may surface that the author has changed her mind on items but never updated the document.

**Editor Reasoning:**
Without explicit governance, every reviewer makes their own assumption. Some treat the standing decisions as binding, others as advisory. The result is that the manuscript inherits inconsistent treatment.

**Clarifying Questions:**
- Has any standing decision been quietly revised since the integration plan was written?
- Are you willing to re-ratify the standing decisions in writing before Phase 2 launches (option C)?

**Proposed Action (upon approval):**
- **If A:** I'll codify the integration plan as binding spec for Round 7.
- **If B:** I'll permit reviewer overrides; each one becomes an author decision.
- **If C:** I'll request author re-ratification of each standing decision; brief reviewers on the ratified set.
- **If D:** I'll de-emphasize standing decisions in reviewer briefs; surface each decision case-by-case to the author.

**Author Response:**
_[Space for author to respond]_

---

### Q9: Decision Authority Matrix — Author-Only vs. Reviewer-Autonomous

**Context:** Editorial decisions split into three categories:

1. **Reviewer-autonomous:** Mechanical (typo fix, comma rule, dictionary spelling).
2. **Reviewer-recommends, author-decides:** Substantive (structural change, voice change, cut/keep, content addition).
3. **Author-only:** Identity/values (what the book says about the author's life, family, faith, stance on contested questions).

Round 7's coordination cost depends on how this split is drawn. If too much falls in (3), author decision fatigue kicks in by Phase 2. If too much falls in (1), reviewers may make changes the author doesn't sanction.

**The Question:** Where do you want the dividing lines?

**Options:**
- [ ] A) **Conventional split.** Mechanical → reviewer. Substantive → author decision. Identity/values → author-only with veto power.
- [ ] B) **Tighter author control.** Even mechanical changes require author confirmation per chapter; substantive changes require explicit author sign-off; identity changes only by author.
- [ ] C) **Looser author control.** Reviewers handle mechanical and substantive autonomously within their reviewer brief; author surfaces only identity/values; round-end review for blanket sign-off.
- [ ] D) **Per-reviewer customization.** Cora and Penny work autonomously on mechanical; Lyra works mostly autonomous with author check-ins; Diana, Sage, Bailey, Felix surface every recommendation.

**Editor Comments:**
The author has been through six rounds. There's data on what fatigue threshold she hits. If Round 5 produced 160 questions and the author responded to all of them, her bandwidth is high — but that doesn't mean Round 7 should target similar volume. Author capacity is finite per round.

If Round 7 targets a 30–40 question round (Q1 Option E), the reviewer-autonomous bucket needs to be larger — most mechanical work happens autonomously, only substantive recommendations surface.

**Editor Reasoning:**
The matrix should match the round's scope (Q1) and the author's calendar bandwidth. Naming it now prevents the round from drifting into "every change goes to the author" by default.

**Clarifying Questions:**
- How many author decisions can you respond to per week comfortably?
- Are there specific reviewers (e.g., Cora) you'd be comfortable trusting with autonomous changes within their domain?

**Proposed Action (upon approval):**
- **If A:** I'll publish the conventional matrix as the round's working agreement.
- **If B:** I'll publish a tight matrix; expect ~150–200 author decisions across the round.
- **If C:** I'll publish a loose matrix; expect ~30–50 author decisions; round-end review of all autonomous changes.
- **If D:** I'll publish a per-reviewer matrix with explicit autonomy boundaries.

**Author Response:**
_[Space for author to respond]_

---

## Section D: Close Criteria, Risk, and Vol 2 Handoff (Q10–Q11)

### Q10: Round 7 Close Criteria

**Context:** "Done" looks different to different stakeholders:

- **Editorial:** All Phase 4 reviewers have signed off; no open author decisions; style sheet committed.
- **Production:** Regenerated `.docx` and `.epub`; verified rendering; print-ready PDF if applicable.
- **Distribution:** Updated companion website; refreshed marketing assets; cross-volume continuity check vs. Vol 2.
- **Operational:** Tag/release in git; PR merged to `main`; state files closed.

Round 5 closed without a clear visible "done" event — implementation continued silently.

**The Question:** What constitutes Round 7 closure?

**Options:**
- [ ] A) **Editorial-only close.** All reviewers signed off, all author decisions recorded, all decisions implemented in chapter files and re-merged. Production/distribution are downstream workstreams.
- [ ] B) **Editorial + production.** Add: regenerated `.docx` + `.epub`, verified rendering of integrated content (cultural callouts, field notes, Pause interludes).
- [ ] C) **Full close.** Editorial + production + companion website parity verified + cross-volume note with Vol 2.
- [ ] D) **Tagged release.** Editorial close + git tag (`vol-1-see/round-7-complete`) + closed PR to `main`. Provides a recoverable snapshot.

**Editor Comments:**
The right answer depends on what comes after Round 7. If a real-world reader cohort or beta program is planned, B is probably the floor — they need readable artifacts. If Round 7 is purely internal, A may be enough.

Tagged release (D) is independent of A/B/C and is recommended regardless. A snapshot named after the round makes future archeology trivial.

**Editor Reasoning:**
Defining "done" prevents Round 7 from sliding into a long tail. Without a visible close event, work in progress feels like normal operations and the round never officially ends — that's how Round 5 closed.

**Clarifying Questions:**
- Are there external commitments (review copies, beta cohort, marketing date) anchored to a specific Round 7 close milestone?
- Should Round 7 close trigger an automated change-log entry or release note?

**Proposed Action (upon approval):**
- **If A:** I'll define editorial close criteria and run a closure checklist at round end.
- **If B:** I'll add `.docx` + `.epub` regeneration to Phase 4 deliverables.
- **If C:** I'll define a multi-stakeholder closure with explicit owners per criterion.
- **If D:** I'll plan a tagged release (independent or alongside A/B/C).

**Author Response:**
_[Space for author to respond]_

---

### Q11: Vol 2 (HEAL) Cross-Volume Continuity

**Context:** Diana's Q15 explores the Vol 2 promise from a developmental angle — should Vol 1 commit to specific Vol 2 content, or stay loose? My question is the coordination version: regardless of what Vol 1 says about Vol 2, who owns ensuring the two volumes remain coherent as Vol 2 is drafted?

Vol 2 (HEAL) does not exist in the manuscript repo yet. References to it in Vol 1 are forward-promises. If Vol 2 development surfaces a contradiction — say, Vol 2 names a recovery practice differently from how Vol 1 references it — there needs to be a process for resolving the contradiction.

**The Question:** How does Round 7 hand off to Vol 2 development?

**Options:**
- [ ] A) **Round 7 produces a "Vol 1 → Vol 2 handoff" document.** Lists every Vol 2 reference in Vol 1 prose, the implicit content commitment, and the deferral status. Vol 2 development must reconcile against this document.
- [ ] B) **Round 7 catalogs Vol 2 references; resolution deferred.** Just produce the catalog; Vol 2 development team resolves contradictions case-by-case as they arise.
- [ ] C) **Round 7 minimizes Vol 2 references.** Recommend cutting or weakening Vol 1 → Vol 2 cross-references; reduce coupling; avoid future contradictions.
- [ ] D) **Out of scope.** Vol 2 continuity is a separate concern owned by the Vol 2 author/editor; Round 7 doesn't address it.

**Editor Comments:**
This is structurally the same problem as the companion website (Q3): there's a downstream artifact whose state Round 7 doesn't fully control, but Round 7 makes commitments about. The cleanest resolution is a documented handoff that future work must reconcile against.

The risk of D is that Vol 2 launches with internal-vs-Vol-1 contradictions that readers catch and reviewers don't.

**Editor Reasoning:**
Cross-volume continuity is cheap to plan now and expensive to fix later. A handoff document (A) is light infrastructure that pays off across the rest of the series.

**Clarifying Questions:**
- Is Vol 2 outline locked, or in flux? (If locked, contradictions can be checked now. If in flux, the handoff doc is the way to surface the constraints.)
- Is the same author writing Vol 2, or a different author/voice?

**Proposed Action (upon approval):**
- **If A:** I'll produce the Vol 1 → Vol 2 handoff document at Round 7 close.
- **If B:** I'll produce just the catalog of references; defer resolution.
- **If C:** I'll work with Diana on minimizing forward-references in Vol 1.
- **If D:** I'll log the deferral.

**Author Response:**
_[Space for author to respond]_

---

## Summary

| Section | Questions | Focus |
|---------|-----------|-------|
| A: Round 7 Charter and Scope | Q1–Q3 | Full vs. selective scope, Round 5 carry-over, website coordination ownership |
| B: Sequencing and Dependencies | Q4–Q6 | Phase gating vs. parallelism, re-merge cadence, Lyra/Cora order |
| C: Conflict Pre-Resolution | Q7–Q9 | Diana × Sage precedence, standing decisions, author/reviewer authority matrix |
| D: Close, Risk, and Vol 2 | Q10–Q11 | Close criteria, Vol 2 handoff |

## Coordination Risk Register

**Top 3 risks to Round 7 finishing cleanly, with mitigations:**

1. **Risk: Diana's review surfaces aggressive restructuring (Part rebalancing, Ch 3 split, Ch 14 reframing) that invalidates Phase 3 work.**
   *Mitigation:* Q1 Option D (Diana-driven scoping) — hold Phase 3 launch until Diana's recommendations are triaged. Worst case, Phase 3 is deferred to Round 8 after restructuring lands.

2. **Risk: Round 5 implementation backlog (open `implementationComplete: false` items in prior state files) surfaces mid-round and contaminates Round 7 reviewer briefs.**
   *Mitigation:* Q2 Option A — audit Round 5 state at Round 7 start, before Phase 2 launches. Two days of work; prevents two weeks of confusion.

3. **Risk: Companion website not in parity with manuscript at Round 7 close — printed book ships referencing resources that don't exist online (or exist at different URLs).**
   *Mitigation:* Q3 ownership decision (probably Option A — Penny verifies in Phase 4). Hard-block Round 7 close on at least one round-trip verification.

**Secondary risks (logged for awareness, not blocking):**

- Parallel-session collisions: per CLAUDE.md, other Claude sessions may run concurrent editorial passes. If Round 7 implementation runs without `bin/qie worktree`, conflicts could surface mid-round. Mitigation: every Round 7 implementer uses the worktree pattern.
- Author decision fatigue: 6 rounds in, author has answered ~200+ questions. Round 7 should target ~30–50 author decisions, not ~150 (Q9 Option C). If the round generates more, surface a triage flag immediately.
- Vol 2 contradiction surface: Vol 2 doesn't exist yet. Vol 1 → Vol 2 references are uncontrolled commitments. Mitigation: Q11 Option A (handoff document).

---

*Morgan (Managing Editor)*
*Review Round 7 — Phase 1: Strategic Decisions*
*April 27, 2026*

