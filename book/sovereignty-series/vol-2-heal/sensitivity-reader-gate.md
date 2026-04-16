# Sensitivity-Reader Gate (Vol 2: HEAL)

## Purpose

This document is a **standing rule** for all cultural-coverage work in Vol 2. It codifies the line-816 requirement from `../vol-1-see/cultural-coverage-gaps-proposal.md` as a hard gate on a specific kind of writing, and names exactly what is permitted before a reader is in place versus what must wait.

The gate exists because the author does not hold first-person authority in the six communities this plan covers. Drafting community-internal voice without a reader from the community in the loop is exactly what the proposal warns against — and exactly where books like this one most often fail their readers.

## Scope

This gate applies to the six communities named in `cultural-coverage-integration-plan.md`:

1. Black / African American
2. Asian (East, South, Southeast)
3. Indigenous / Native
4. Middle Eastern / Arab / SWANA
5. Religious traditions (Evangelical, Mormon/LDS, JW, Catholic — depth)
6. Transgender-specific dynamics

It also applies, by extension, to any future community added to the coverage plan where the author does not hold direct first-person authority.

It does **not** apply to:

- Jewish (Ashkenazi) or Jewrican-by-marriage material — the author holds first-person authority here.
- Hispanic / Latino, LGBTQ+ (not trans-specific), immigrant, and male-survivor material already integrated in Vol 1 per `../vol-1-see/unified-woven-integration-plan.md`. That pass already went through its reader process.

## The Rule

**For the six communities in scope, the following content may not be drafted or committed without a named human sensitivity reader from that community signed off on the scope:**

- First-person field notes in a community member's voice (composite or verified)
- Scripts or dialogue containing community-internal phrasing, in-language idioms, or code-switching
- Direct claims about community-internal theology, ceremony, kinship rules, gender codes, or honor architecture
- Community-specific exit pathways (e.g., JW judicial-committee procedure, LDS temple-recommend mechanics, Catholic annulment specifics, tribal disenrollment)
- In-language terms used with emotional weight (not just glossed in passing)

**The following content *may* be drafted without a reader in place, because it is author-voice / structural / factual rather than community-voice:**

- Structural patterns named from the outside, without putting words in any community's mouth (the Ch 5, 6, 7, 11, 12, 13, 14, 15, 16, 18, 19, 22 landed passages are the template)
- Verified directory resources (organization names, hotlines, URLs) in Appendix C
- Author-voice pointer language directing readers to community-specific companion resources
- Cross-community framing that names the shape of a pattern without prescribing how it reads from inside

## The Workflow

1. **Reader recruitment.** The six per-community reader profiles are listed in the table in `cultural-coverage-integration-plan.md`. Recruitment is tracked there; this gate applies regardless of whether any given community's reader has been identified.
2. **Outline first, with the reader.** Before any community-voice drafting begins, the reader reviews the outline for that community's material — what will be named, where, in what voice, with what framing. The reader shapes the frame before any prose is committed.
3. **Drafting, one community at a time.** One community's deferred material is drafted per pass, with that community's reader in the loop from outline → draft → revision. No parallel community-voice drafts without reader signoff, because community-internal material for one community can read against another community's material, and that cross-read is the reader's job to catch.
4. **Sage (AI) as second-pass filter.** The existing `book/agents/sensitivity-reader.md` agent runs after the human reader has signed off. Sage is an additional safety net, not a replacement for the human reader. **Invoking Sage does not satisfy this gate.** A commit that passes Sage but has no human reader signoff on the community-voice material is still in violation.
5. **Integration pass.** Approved community material merges into the Vol 2 chapters mapped in the integration plan.
6. **Final cross-community reader pass.** Each community's reader reviews the integrated manuscript — not just their own contribution — to catch where their material reads against another community's material.
7. **Legal review** paralleling the Tier 1/2/3 structure used for author-identifying details in Vol 1.

## What Triggers This Gate

Any pull request or commit that touches:

- `book/sovereignty-series/vol-2-heal/chapters/*.md` with content that puts words in a community's mouth
- `book/sovereignty-series/vol-2-heal/appendices/*` with community-internal claims beyond directory facts
- Any new Vol 2 content referencing the six in-scope communities in a way that exceeds the "author-voice / structural / factual" list above

…must either (a) pass the workflow above with a named human reader signoff recorded, or (b) stay strictly inside the author-voice / structural / factual scope.

## What Violates This Gate

Illustrative examples of what **is** a violation, independent of how well-intentioned the writing is:

- A first-person paragraph in the voice of a Black survivor, written without a Black reader in the loop.
- A script in which a Korean mother speaks to her daughter about shame, written without a Korean-American reader in the loop.
- A passage describing the internal mechanics of a JW judicial committee with confidence, written without a former JW (or a JW survivor advocate) in the loop.
- A field note in the voice of a trans woman describing HRT-continuity-as-leverage inside a coercive relationship, written without a trans reader — ideally a trans survivor — in the loop.
- Using "aguanta," "sabr," "chī kǔ," "shalhevet," or similar in-language terms with emotional weight (not just a parenthetical gloss) in contexts where the surrounding paragraph is *about* that community — without a reader from that community reviewing the use.

Illustrative examples of what is **not** a violation:

- An author-voice paragraph naming that in many Asian, SWANA, and Latin family systems, emotional restraint was taught as maturity — without writing a scene inside any of those family systems.
- Listing verified organization names and URLs in Appendix C for Indigenous, SWANA, JW-exit, and trans-specific resources, without drafting survivor-voice testimony from any of them.
- A structural description (as in Ch 12's "When the Community Is the Relationship") of the shape of the cost, without composing community-internal voice.
- Quoting language the author's own communities use — Jewish, Jewrican-by-marriage — because the author holds authority there.

## Exceptions

The only exceptions to this gate are:

- **Published, attributable source material** (a quote from a memoir, an interview, a clinical paper) used with full citation and in the source's own voice. This is not "putting words in a community's mouth"; it is quoting a community member speaking for themselves. Fair-use and permissions rules still apply.
- **The author's own first-person material** in the communities the author holds authority in. These are not in scope of this gate in the first place.
- **Direct reader-contributed material** sent to the author for inclusion, used with documented consent, in the reader's own voice.

## Relationship to Other Documents

- `cultural-coverage-integration-plan.md` — the Vol 2 blueprint. This gate enforces the integration plan's "What Is Explicitly NOT Drafted Here" section.
- `../vol-1-see/cultural-coverage-gaps-proposal.md` — the master proposal, line 816 in particular, which originated this requirement.
- `../../../agents/sensitivity-reader.md` — the Sage AI agent spec. Sage is the second-pass filter. This document gates the first pass.
- `../vol-1-see/unified-woven-integration-plan.md` — the Vol 1 unified integration, which went through its own reader process; its output is not in scope of this gate.

## A Note on Why This Exists as a Rule, Not a Guideline

Most of this book's quality controls — line editing, copy editing, proofreading, the editorial workflow in `../../../agents/README.md` — are iterative. A mistake made at one stage gets caught at the next. This gate is different. Community-voice harm does not surface as a line-edit issue or a typo. It surfaces as a reader from that community closing the book. Once the book is in print, the harm is durable. The only place to catch it is before the words go in.

That is why this is a rule, not a guideline, and why Sage (AI) — which is excellent at the work Sage does — cannot replace a human reader from the community for the work that human reader does.

---

*The wolf wears different clothing in every community. The teeth don't change. Vol 1 named the disguise. Vol 2 is writing the way out — in language each community can use without having to translate. This document exists so that language is written by the people who hold it.*
