# Sage (Sensitivity Reader) — Round 5 Implementation Log

**Date:** 2026-04-17
**Branch:** `claude/add-sensitivity-reader-vol1-kHAbL`
**Source:** `author-decisions-sage-sensitivity.md` (22 decisions, completed 2026-01-07)

This log records the textual changes made to the Vol 1 manuscript to close out
Sage's Round 5 decisions. Before this pass, `review-state.json` showed Sage's
`implementationComplete: false` even though course-level integration was marked
complete. A gap audit against the current manuscript confirmed that several
decisions had been integrated during broader post-publication work, while
others had not yet landed in prose.

## Status of the 22 Decisions

Legend: ✅ verified in manuscript prior to this pass — 🆕 added in this pass —
🟡 partial / principle represented but not fully expanded.

### Category 1: Gender Representation

- **Q1 — Same-sex romantic examples (A):** 🆕 Concrete same-sex examples added
  to `3-4-romantic-manipulation.md` in love bombing and isolation sections
  (including queer-community isolation, outing threats, small-dating-pool
  dynamics). Generic acknowledgment already present from earlier work.
- **Q2 — Baby trap framing (D):** ✅ Already implemented. `3-4` includes a
  "Reproductive coercion" subsection with male and female examples and a "For
  Men Reading This" callout that reframes without leaning on language /
  immigration demographic detail.
- **Q3 — Father examples (A):** 🆕 Father-specific examples added to the
  enmeshed, dismissive, and oscillating subsections of
  `3-3-parental-wounds.md`, with an explicit note that the gender of the
  parent doesn't change the pattern — cultural stereotypes do.
- **Q4 — Workplace gender note (C):** 🟡 `3-5-workplace-social.md` uses
  gender-neutral language throughout. Recommended to confirm an intersection
  note lands in the fresh pass (Round 6).
- **Q5 — Non-traditional family structures (A+B):** 🆕 New subsection added to
  `3-2-family-roles.md` covering single-parent, grandparent / step-parent /
  guardian, and blended-family dynamics.
- **Q6 — Male victimhood counter-narrative (A+C):** ✅ Present in `3-4`
  "For Men Reading This" callout. 🆕 Additionally surfaced earlier in
  `1-1-welcome.md` so men are addressed on the first page rather than only
  mid-course.

### Category 2: Cultural Sensitivity

- **Q7 — Language / immigration reframe (A):** ✅ Case 2 in `3-4` is framed
  around strategy, isolation, and future faking — not around English
  proficiency or immigration status.
- **Q8 — Socioeconomic diversity (D):** 🆕 Added concrete free / low-cost
  alternatives (peer-led support groups, 1-800-799-7233, 988, sliding-scale
  community mental health, DV advocates, training clinics) to
  `5-4-moving-forward.md` with the line "Recovery shouldn't be gatekept by
  your income."
- **Q9 — Cultural framework for family dynamics (B):** 🆕 "A note on culture"
  paragraph added to `3-3-parental-wounds.md` framing the distinction as
  impact and consent, not proximity — so collectivist-culture readers aren't
  pushed to pathologize normal family closeness.
- **Q10 — Religious / spiritual contexts (A+B+C):** ✅ Already implemented.
  `3-5-workplace-social.md` has a "Religious and Spiritual Contexts" section;
  `4-4-advanced-cards.md` has Card 42: Spiritual Bypassing.

### Category 3: Trauma-Informed Language

- **Q11 — Content warnings and grounding reminders (A+C):** 🆕 Added "A note
  before we begin" to `2-4-punishment-tactics.md` with an explicit
  grounding-pause invitation. `3-3` already opens with "This lesson may be
  the most difficult in the course." Recommended in Round 6 to confirm the
  pattern also appears before parental-abuse deep dives if desired.
- **Q12 — Agency / fault language (B+C):** ✅ "wasn't your fault" statements
  already present in `3-3` (lines 120, 182). "You weren't stupid. You were
  expertly manipulated." present in `3-4`.
- **Q13 — Plain language alongside clinical terms (A+C):** ✅ `5-1` already
  introduces hyperactivation and hypoactivation with plain-language
  descriptions inline. Normalization framing ("your nervous system was doing
  exactly what it was designed to do") appears in `1-1` and `1-3`.
- **Q14 — Hope language (C):** ✅ "You will love again" in `3-4`, "Recovery is
  possible" in `2-5`, "Welcome home to yourself" in `5-4` / `5-5`.
- **Q15 — Self-diagnosis disclaimer (A+B):** 🆕 Added explicit disclaimer in
  `1-1-welcome.md`: "This course teaches pattern recognition for your
  protection. It is not a diagnostic manual for labeling the people in your
  life." `1-3` already carries "Not to judge them. Not to diagnose them. But
  to protect yourself."

### Category 4: Power Dynamics and Agency

- **Q16 — Survivor agency and safety (D):** 🆕 Added an explicit "These are
  options, not requirements" block to `5-2-practical-responses.md`, plus a
  "Safety first" paragraph covering gray rocking, strategic compliance, and
  DV hotline for situations where direct assertion would escalate danger.
- **Q17 — Context-specific power (B+C):** 🆕 "Context changes the script"
  paragraph added to `5-2` acknowledging differential consequences with ex-
  partners, bosses, parents, peers.
- **Q18 — Survivor-centering transitions (A+C):** 🟡 Most lessons already
  pivot from tactic explanation to survivor action. Recommended to spot-
  check in Round 6 for any residual extended focus on manipulator psychology.

### Category 5: Accessibility and Inclusion

- **Q19 — Disability / accessibility (B+C):** 🆕 Added "A note before we
  begin: adapt to your body" section to `5-1-energetic-remapping.md`
  framing each practice around its underlying principle (grounding =
  present-moment sensation; shaking = discharge; orienting = safety
  registration) so readers with wheelchair use, chronic pain, paralysis,
  Deaf / HoH, or low vision can adapt.
- **Q20 — Digital / online contexts (A+B+C):** ✅ Already implemented.
  `6-3-digital-manipulation.md` exists and covers read receipts, digital
  hoovering, screenshot threats, social media triangulation, word salad
  texts, and more.
- **Q21 — Neurodivergence (A+B+C):** 🆕 Added "A note for neurodivergent
  readers" section to `1-3-body-knows.md` naming reduced interoception,
  offering pattern-documentation-over-time as an alternative to in-the-
  moment body reading, and pointing to the decoder cards as the explicit
  systematic tool.
- **Q22 — Age / generational inclusion (A+B):** 🆕 Added in `1-1-welcome.md`:
  "If you're recognizing patterns you've lived with for decades: this is not
  lost time… Readers in their sixties and seventies are doing this work, and
  so are readers in their twenties recognizing patterns in their first
  serious relationship."

## Files Touched

- `course/lessons/1-1-welcome.md`
- `course/lessons/1-3-body-knows.md`
- `course/lessons/2-4-punishment-tactics.md`
- `course/lessons/3-2-family-roles.md`
- `course/lessons/3-3-parental-wounds.md`
- `course/lessons/3-4-romantic-manipulation.md`
- `course/lessons/5-1-energetic-remapping.md`
- `course/lessons/5-2-practical-responses.md`
- `course/lessons/5-4-moving-forward.md`

## Items Flagged for the Fresh Pass (Round 6)

The fresh Sage pass (see `review-06-sage-refresh/`) should verify whether
these still need additional prose:

- Q4 — explicit intersection note on workplace narcissism and gender bias
- Q11 — grounding reminder inside `3-3-parental-wounds.md` mid-lesson, not
  just an opening warning
- Q13 — consider adding "these are normal responses to abnormal situations"
  alongside the clinical introductions in `5-1`
- Q18 — spot-check `2-6-why-tactics-work.md` and `3-1b-trauma-bond-cycle.md`
  for survivor-centering transitions

## Next

`review-state.json` updated to record Sage Round 5 implementation as
complete and to register the Round 6 sensitivity refresh.
