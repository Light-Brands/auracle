# Petra (Proofreader) — Round 1, Phase 4

**Volume:** Vol 1 Companion Workbook — *SEE: Recognizing Narcissistic Manipulation in Relationships, Family, and Work*

**Role:** Final proofread — mechanical errors only. The book is locked. I am the last eyes.

---

## 1. Overview

I reviewed every file in `/home/user/auracle/book/sovereignty-series/vol-1-see/companion-workbook/`:

- `README.md`
- `00-welcome.md`
- `DESIGNER-BRIEF-WORKBOOK.md`
- `part-1-recognition.md`
- `part-2-understanding.md`
- `part-3-origins.md`
- `part-4-application.md`
- `part-5-recovery.md`
- `appendix-a-decoder-patterns.md`
- `appendix-b-body-vocabulary.md`
- `appendix-c-grounding-techniques.md`
- `appendix-d-safety-planning.md`
- `appendix-e-recommended-reading.md`
- `appendix-f-printable-cards.md`

**Good news first:** I found no traditional typos, homophone errors (its/it's, their/there, then/than, principle/principal, etc.), doubled words, misspellings, unmatched quotation marks, or placeholder leftovers ([TBD], [draft], [TODO], FIXME). No broken internal file links — every `[text](./file.md)` resolves to an existing file in the directory. No empty sections.

**Where the issues live:** The mechanical problems are almost entirely about **cross-reference fidelity** and **dash/punctuation consistency** across the manuscript. Two cross-reference errors are blocking. One is a factual error (wrong Card number for a life-safety topic). The dash inconsistencies are copy-editing-level, not typos — I flag them because Part I diverges strongly from every other file.

---

## 2. Error Log

Columns: **File | Line (approx) | Issue | Suggested fix**

### Cross-reference and factual errors (highest priority)

| File | Line | Issue | Suggested fix |
|---|---|---|---|
| `appendix-d-safety-planning.md` | 183 | "described in the book (Card 21: Emotional Hostage-Taking)" — in the current canonical chapter 3, **Card 21 is "Weaponized Humor"** and the suicide-threats card is **Card 29** (named "Suicide Threats," not "Emotional Hostage-Taking"). Confirmed against `chapters/03-decoder-playbook.md` lines 949 and 1291, and against this workbook's own `appendix-a-decoder-patterns.md` line 73. | Change to "Card 29: Suicide Threats" |
| `appendix-e-recommended-reading.md` | 142 | "workbook exercises in Sections 3 (Pattern Naming), 5C (Role Identification), and 5D (Type Identification)" — **there is no Exercise 5D.** Type Identification is "Part D" inside Exercise 5C (see `part-2-understanding.md` line 559). | Change "5D (Type Identification)" to "5C, Part D (Type Identification)" — or "within 5C" |
| `part-4-application.md` | 721 | "Continue to **Part V: Integration**" — Part V is titled "Recovery, Response, and Moving Forward" in its own H1 (line 1), and "Part V — Recovery & Rewiring" in README line 118. No file calls it "Integration." | Change to "Part V: Recovery" (to match README short form) or the full actual title |
| `part-4-application.md` | 721 | Link text "Table of Contents" points to `00-welcome.md`, but the TOC lives in `README.md`. `00-welcome.md` has a Progress Tracker, not a TOC. | Change link to `README.md` |
| `README.md` vs `part-5-recovery.md` | README 118 vs file 1 | Part V name mismatch. README: "Part V — Recovery & Rewiring". File H1: "Part V: Recovery, Response, and Moving Forward." Progress Tracker in `00-welcome.md` lines 175-177 uses "Part V — Recovery". | Pick one canonical name and standardize across all three locations |

### Em-dash / en-dash / hyphen consistency

| File | Lines | Issue | Suggested fix |
|---|---|---|---|
| `part-1-recognition.md` | throughout (29 instances) | Uses ASCII double-hyphen `--` for em-dashes (e.g. line 36 "write 'unsure' -- that is data too", line 84 "Gradual Dimming -- how control"). Every other Part (II-V) and every other appendix uses proper em-dash `—`. | Global replace `--` with `—` in part-1 (29 occurrences). Verify word-spacing matches neighbors (other files use spaced em-dash: ` — `) |
| `part-4-application.md` | 3, 721 | Uses double-hyphen for chapter ranges: "Chapters 11--14", "Chapters 15--17" | Change to en-dash: "Chapters 11–14" and "Chapters 15–17" to match README (which uses en-dash throughout) |
| `part-1-recognition.md` | 3 | "Chapters 1-3" (plain hyphen) | Change to en-dash "Chapters 1–3" to match README (Chapters 1–3, 4–6, 7–10, 11–14, 15–17) |
| `part-1-recognition.md` | 830 | "aligned with Chapters 4-6" (plain hyphen) | Change to en-dash "Chapters 4–6" |
| `part-5-recovery.md` | 3, 5 | "Sections 14-16", "Chapters 15-17" (plain hyphens) | Change to en-dashes to match README style |
| `README.md` | 173 | "Chapters 5-6" (plain hyphen) in the Chapter-Section mapping table — inconsistent with lines 28, 49, 66, 92, 120 which use en-dash `–` | Change to "Chapters 5–6" |
| `appendix-e-recommended-reading.md` | 60, 93, 94, 95, 96 | Plain hyphens in "Chapters 7-10", "Sections 1-3", "Sections 4-5", "Sections 6-9", "Sections 10-11" | Change to en-dashes for consistency |

### Section-subtitle formatting inconsistency

| File | Lines | Issue | Suggested fix |
|---|---|---|---|
| `part-4-application.md` | 20, 198, 347, 488 | Uses `**Aligned with Chapter X — ...**` (bold) under Section headers | Decide on one style; Parts 1-3 use italic. Parts 4 and 5 use bold. |
| `part-5-recovery.md` | 30, 306, 708 | Same — uses bold "**Aligned with Chapter X**" under Section headers | Parts 1, 2, 3 use italic for the same construct (e.g. `*Aligned with Chapter 1: The Opening Manifesto*`). Pick one and standardize. |

### Heading-hierarchy anomalies

| File | Lines | Issue | Suggested fix |
|---|---|---|---|
| `part-5-recovery.md` | 1-5 | H1 "Part V: Recovery, Response, and Moving Forward" is immediately followed by two H3s ("### Companion Workbook Sections 14-16" and "### Aligned with Chapters 15-17") — skips H2. Every other Part opens H1 then an H3 subtitle (single line). | Collapse into a single H3 subtitle: `### Companion Workbook Sections 14–16 (Aligned with Chapters 15–17)` |
| `part-3-origins.md` | 3 | Uses H2 (`## Chapters 7–10: Family Systems & Childhood Patterns`) directly under H1, whereas Parts 1, 2, 4, 5 use H3 for the subtitle | Downgrade to H3 to match siblings, or standardize all Parts to H2 |
| `README.md` | 1-7 | Opens with H1 `# SEE:` then `## By Jennifer...` then `## A Free Resource...` then `### Volume 1`. `00-welcome.md` opens H1 then H3 then H3. Author byline appears at H2 in README but H3 in 00-welcome. | Align byline level between README and 00-welcome |

### Minor punctuation / spacing

| File | Line | Issue | Suggested fix |
|---|---|---|---|
| `00-welcome.md` | 153-154 | Two consecutive horizontal-rule lines `---` with only a blank line between them. Renders as a doubled rule in some processors. | Remove one of the two `---` lines |
| `part-4-application.md` | 176-177 | Two consecutive `---` horizontal rules | Remove one |
| `part-2-understanding.md` | 9 | "**How activated are you right now, on a scale of 1–10?**" — uses en-dash for numeric range; consistent with file but worth flagging only because `part-1-recognition.md` uses spaced double-hyphens for the analogous construct | Style-sheet decision only |
| `appendix-a-decoder-patterns.md` | 20 | Opening blockquote mixes `>` continuation lines with inline text — line 20 is one long paragraph inside a blockquote. Renders fine, but breaks visual rhythm. Mechanical only if the style guide mandates short block-quote lines. | No change required; flag for Q-section |
| `part-2-understanding.md` | 291 | Subtitle reads "*Aligned with Chapters 5–6 — Narcissist Types and the 12 Identity Roles*" — and Section 5 H2 says "Section 5: Seeing Behind the Mask" — the "12 Identity Roles" phrasing appears only in this italic line, while README line 173 calls them "Masks" and Chapter 6's file is `06-narcissist-roles.md`. No error, but terminology "Roles" vs. "Masks" vs. "12 Identity Roles" is used interchangeably. | Decide on one term; Petra-only flag for Lydia |

### Ambiguous / query-only (not mechanical fixes)

| File | Line | Observation |
|---|---|---|
| `part-1-recognition.md` | 530-537 | A blockquote `> **Grounding pause.**` starts immediately after a horizontal rule, and the following section "Exercise 3B" opens without a horizontal rule above it — inconsistent with other exercise separations in this file. |
| `part-3-origins.md` | 786-795 | The closing "If this section brought up more than you expected" blockquote appears *after* the final grounding-closing blockquote. Two sequential blockquotes at the end of the Part. Intentional, but visually unusual. |

---

## 3. Broken-Link Report

Every internal markdown link was traced to a file in the same directory.

| Link | Source | Target exists? |
|---|---|---|
| `./00-welcome.md` | README | YES |
| `./part-1-recognition.md` through `./part-5-recovery.md` | README | ALL YES |
| `./appendix-a-decoder-patterns.md` through `./appendix-f-printable-cards.md` | README | ALL YES |
| `appendix-f-printable-cards.md` | part-4 line 494 | YES |
| `appendix-c-grounding-techniques.md` | part-4 line 494 | YES |
| `00-welcome.md` (as "Table of Contents") | part-4 line 721 | **FILE EXISTS but link text is wrong** — 00-welcome does not contain a TOC; README does. See error log above. |

**External links** (hotpeachpages.net, psychologytoday.com, openpathcollective.org, findtreatment.gov, outofthefog.website): not verified — that is outside proofread scope and hotline numbers are policy content.

**No 404 file links.** Every markdown `[text](path.md)` resolves.

---

## 4. Cross-Reference Report

Every "Section X," "Chapter Y," "Card Z," "Exercise NX" reference was tested.

### Chapter → Section mapping (README lines 167-184)

| Book Chapter | Workbook Section | Verified |
|---|---|---|
| Chapter 1 → Section 1 | YES (part-1 line 19) |
| Chapter 2 → Section 2 | YES (part-1 line 210) |
| Chapter 3 → Section 3 | YES (part-1 line 408) |
| Chapter 4 → Section 4 | YES (part-2 line 19) |
| Chapters 5–6 → Section 5 | YES (part-2 line 291) |
| Chapter 7 → Section 6 | YES (part-3 line 45) |
| Chapter 8 → Section 7 | YES (part-3 line 202) |
| Chapter 9 → Section 8 | YES (part-3 line 438) |
| Chapter 10 → Section 9 | YES (part-3 line 552) |
| Chapter 11 → Section 10 | YES (part-4 line 20) |
| Chapter 12 → Section 11 | YES (part-4 line 198) |
| Chapter 13 → Section 12 | YES (part-4 line 347) |
| Chapter 14 → Section 13 | YES (part-4 line 488) |
| Chapter 15 → Section 14 | YES (part-5 line 30) |
| Chapter 16 → Section 15 | YES (part-5 line 307) |
| Chapter 17 → Section 16 | YES (part-5 line 709) |

All 16 chapter-to-section mappings are internally consistent with the file contents.

### Card-number references (cross-workbook)

| Ref | Location | Verified against Appendix A + book ch. 3 |
|---|---|---|
| Card 0: Wolf in Sheep's Clothing | appendix-a line 24, app-f Card 8 line 234 | YES |
| Card 12: "When You Want to Go Back" | part-5 line 702 | YES (appendix-f line 363) |
| Card 21: "Emotional Hostage-Taking" | appendix-d line 183 | **NO — see error log.** Card 21 is "Weaponized Humor"; Suicide Threats is Card 29. |

### Exercise references

| Ref | Source | Target exists? |
|---|---|---|
| Exercise 10B | part-5 line 637 | YES (part-4 line 108) |
| Exercise 14C | part-5 lines 639, 1133 | YES (part-5 line 166) |
| Exercise 14D | part-5 line 638 | YES (part-5 line 219) |
| Exercise 16D | part-5 line 687 | YES (part-5 line 980) |
| Exercise 5C (Role Identification) | appendix-e line 142 | YES |
| Exercise 5D (Type Identification) | appendix-e line 142 | **NO — does not exist; it is Part D of 5C.** |

### Appendix references

| Ref | Source | Verified |
|---|---|---|
| Appendix C (Grounding) | 00-welcome 71, part-4 494, app-d 159 | YES (file exists) |
| Appendix D | 00-welcome 150 | YES |
| Appendix F Card 12 | part-5 702 | YES |
| Appendix G (book, not workbook) | part-1 717, part-2 563, appendix-e 138 | YES — book's `appendices/appendix-g-pop-culture-references.md` exists |

### Safety-level numbering

GREEN / YELLOW / RED levels referenced consistently across `00-welcome.md` (84-116), `part-4-application.md` (374-378), `appendix-d-safety-planning.md` (25-48). Color names and meanings match.

### Book-internal chapter chrono

Book chapters 1-17 and their topical titles match the chapter list in `/chapters/` (`01-opening-manifesto.md` through `17-moving-forward.md`). No phantom chapters referenced.

---

## 5. Placeholder / TODO Report

Grep against `TBD|TODO|FIXME|[draft]|[fill|[placeholder]|XXX` returned **no matches** across all 14 files.

**Intentional fill-in blanks** (writing prompts using underscores or blank fields like `_______________` or `_____`) are present in every Part file — these are workbook features, not placeholders. Not flagged.

**No unfinished sections.** Every Section header has content; every Exercise label has instructions; every table has column headers.

---

## 6. Numbered Judgment-Call Questions

These are genuine questions where editorial judgment — not mechanical correction — is needed. I'd like a ruling before implementing fixes that have style implications.

**Q1 — Part V canonical name.** Three different names are in play: "Recovery & Rewiring" (README line 118), "Recovery, Response, and Moving Forward" (part-5 H1), "Recovery" (00-welcome Progress Tracker). Which is canonical? I recommend "Recovery" (short) or "Recovery & Rewiring" (README's form) and aligning the file H1 + part-4's forward reference.

**Q2 — Em-dash style for Part I.** Part I uses ASCII `--` 29 times; every other file uses `—`. Is Part I intentionally authored in ASCII (maybe for a specific distribution format) or is this an artifact from an older draft? I recommend global replace to `—` to match the rest. Confirming before I touch 29 lines.

**Q3 — Range separator (hyphen vs. en-dash).** "Chapters 1-3" vs. "Chapters 1–3" vs. "Chapters 11--14" — three different conventions appear. README uses en-dash consistently (1–3, 4–6, 7–10, 11–14, 15–17). Should I normalize all subtitle / list "Chapters X–Y" references to match README?

**Q4 — Section-subtitle formatting.** Parts 1-3 use italic `*Aligned with Chapter X*`; Parts 4-5 use bold `**Aligned with Chapter X**`. Which wins? (Italic reads calmer; bold reads structural. Readability suggests italic.)

**Q5 — `part-4` line 721 "Table of Contents" link target.** Currently links to `00-welcome.md` but the TOC is in `README.md`. Should I repoint to README, or should 00-welcome become the TOC landing page? (README is currently the TOC per its own header.)

**Q6 — Card 21 vs. Card 29 correction in Appendix D.** This is a factual mismatch with a life-safety topic (suicide threats). I'd ordinarily fix it silently, but the cross-reference also renames the card ("Emotional Hostage-Taking" vs. "Suicide Threats"). Recommend: change to "Card 29: Suicide Threats." Approve before I touch the number?

**Q7 — Appendix E's "Exercise 5D".** Should I repoint the citation to "Exercise 5C, Part D" (accurate) or promote the Type Identification sub-exercise to its own Exercise 5D in part-2 (bigger structural change)? The smaller fix is the citation; the bigger fix is consistency with how Exercise 5C is currently split into Parts A-D.

**Q8 — `00-welcome.md` lines 153-154 double horizontal rule.** Same in part-4 lines 176-177. These render as a single thicker rule in some markdown engines and as two rules in others. Remove one? (Almost certainly artifact.)

**Q9 — Heading hierarchy in `part-3-origins.md`.** Uses H2 for the subtitle ("## Chapters 7–10: Family Systems & Childhood Patterns") while Parts 1, 2, 4, 5 use H3. Downgrade to H3 to match sibling files, or promote others to H2? Recommend downgrading part-3 to H3.

**Q10 — Part V opening uses two consecutive H3 lines (file lines 3 and 5).** Recommend merging into a single subtitle: `### Companion Workbook Sections 14–16 (Aligned with Chapters 15–17)`. Approve?

---

## 7. Fix Count by Type

| Category | Count |
|---|---|
| Broken cross-references (factual errors) | **2** (Card 21/29; Exercise 5D) |
| Incorrect link-target pairings | **1** (part-4 "Table of Contents" → 00-welcome vs. README) |
| Title/name mismatches across files | **1** (Part V — three different names) |
| ASCII double-hyphen `--` where em-dash `—` is standard | **~31 instances** (29 in part-1, 2 in part-4) |
| Hyphen used where en-dash is the book standard | **~10 instances** (part-1 line 3 & 830, part-5 lines 3 & 5, README line 173, appendix-e lines 60, 93, 94, 95, 96) |
| Section subtitle formatting (bold vs. italic) | **~6 headers** (Parts 4 & 5 vs. Parts 1-3) |
| Heading-hierarchy inconsistencies | **2** (part-3 H2 subtitle; part-5 double H3 opener) |
| Double horizontal rules | **2** (00-welcome 153-154; part-4 176-177) |
| Spelling errors / typos | **0** |
| Homophone errors | **0** |
| Doubled words | **0** |
| Punctuation errors (unmatched quotes/brackets/parens) | **0** |
| Placeholders / [TBD] / draft markers | **0** |
| Broken file links | **0** |
| Missing required files (from README TOC) | **0** |

**Total mechanical corrections:** ~55, concentrated in dash normalization and subtitle formatting. The high-priority factual fixes number just 4 (Card 21→29, Exercise 5D→5C Part D, part-4 "Integration"→"Recovery", TOC link target).

---

## 8. Proofread Verdict

**Publication-ready after the four cross-reference corrections in Section 2 are applied.** The manuscript is remarkably clean — no typos, no homophones, no doubled words, no broken links, no placeholders, no empty sections. The errors that remain are either factual cross-reference slips (four) or stylistic/format-consistency items that reflect multiple authoring passes (dashes, subtitle formatting, one heading level).

The **Card 21 / Card 29** error in Appendix D is the single most important fix in this pass. It involves suicide-threat content and a reader may search the decoder patterns by the number given. Getting this right matters more than all the dash normalizations combined.

Once Q1-Q10 are resolved and the corrections implemented, I am prepared to mark the manuscript **PUBLICATION READY**.

— Petra
