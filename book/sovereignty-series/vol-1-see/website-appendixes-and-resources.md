# Vol 1: SEE — Library Section: Appendixes & Resources

> **Where appendixes live.** Every appendix to *Vol 1: SEE* is hosted here in the website library so it can be kept current. A subset is also bound into the print edition. Resources that age quickly (URLs, hotlines, apps, citations to specialized contexts) live online only — the canonical, evergreen reference matter is what gets printed.

This document is the master index for the library section that surfaces these appendixes on the site.

---

## Distribution at a glance

| Appendix | Title | In print book | On website |
| --- | --- | --- | --- |
| A | Resources | — | ✅ |
| B | Glossary of Terms | ✅ | ✅ |
| C | Bibliography & Further Reading | ✅ | ✅ |
| D | Core Techniques Reference | ✅ | ✅ |
| E | Index | ✅ | ✅ |
| F | Substance-Related Patterns | — | ✅ |
| G | Pop Culture References | — | ✅ |

**Print edition contains:** B, C, D, E.
**Website library contains:** A, B, C, D, E, F, G.

The print appendices retain their original letters (B, C, D, E) so cross-references between editions remain stable. A, F, and G are not renumbered — they simply do not appear in the printed book. A note in the print front matter directs readers here for the full set.

---

## Why some appendixes are web-only

**Appendix A — Resources.** Phone numbers, hotlines, app recommendations, Reddit communities, YouTube channels, therapist directories, and crisis URLs. This is the single most time-sensitive content in the book. Hotlines reorganize. Apps get discontinued. Communities get moved or banned. URLs break. Printing this content guarantees it begins degrading the day the book ships. Online, it can be maintained quarterly and expanded with region-, language-, and community-specific resources that would otherwise bloat the print edition.

**Appendix F — Substance-Related Patterns.** A specialized subset of decoder cards covering manipulation tactics involving alcohol, drugs, and other substances. Critically important for readers who encounter these dynamics, but not core to every reader's path. Hosting it online keeps the print edition focused while still making the material fully available to those who need it.

**Appendix G — Pop Culture References.** The largest of the appendixes (~55K), and the one most naturally suited to a browsable, searchable, link-rich format. The web version can hyperlink directly to the films, shows, and music being referenced — something print cannot do — and can be expanded as new cultural touchstones emerge.

---

## Why some appendixes are in both places

**Appendix B — Glossary of Terms.** Readers reach for it constantly while reading. It needs to live next to the chapters in print, and it needs to be searchable on the web.

**Appendix C — Bibliography & Further Reading.** A non-fiction book of this kind is expected to carry its bibliography in print — it signals the depth of the source material and lets a reader follow citations without a device. Online, it is also linkable and searchable.

**Appendix D — Core Techniques Reference.** The practical "do the work" quick-reference. Readers return to it under stress; it has to be in the print edition. It also needs to be one click away on the web.

**Appendix E — Index.** Print non-fiction is hard to navigate without an index. The web has search, but the index is also useful online as a curated map of key concepts.

---

## Library section: appendix entries

Each entry below is rendered as a page in the website's library section. Source content lives in `book/sovereignty-series/vol-1-see/appendices/` and is already wired into the reader via `app/reader/chapters.ts`.

### Appendix A: Resources *(web only)*

- **Source file:** `appendices/appendix-a-resources.md`
- **Subtitle:** Support, Information, and Next Steps
- **Description:** Living directory of crisis hotlines, culturally competent therapist networks, support communities, legal aid, financial assistance, and community-specific resources (LGBTQ+, BIPOC, immigrant, faith-tradition-specific, transgender, male survivors, indigenous, and more). Maintained on a quarterly review cadence.
- **Maintenance owner:** *(assign)*

### Appendix B: Glossary of Terms

- **Source file:** `appendices/appendix-b-glossary.md`
- **Subtitle:** Key Concepts and Definitions
- **Description:** Reference vocabulary used throughout the book — naming what was experienced is the first step toward reclaiming power over it.

### Appendix C: Bibliography & Further Reading

- **Source file:** `appendices/appendix-c-bibliography.md`
- **Subtitle:** Sources, Influences, and Recommended Reading
- **Description:** Works that informed the book and recommendations for continuing education and recovery. Online, citations are linkable.

### Appendix D: Core Techniques Reference

- **Source file:** `appendices/appendix-d-core-techniques.md`
- **Subtitle:** Quick Access Guide for Grounding, Response, and Protection
- **Description:** Consolidated, bookmarkable techniques pulled from across the chapters — grounding tools, response scripts, and protective practices for moments when you need them fast.

### Appendix E: Index

- **Source file:** `appendices/appendix-e-index.md`
- **Subtitle:** Quick Reference to Key Concepts and Terms
- **Description:** Concept and term index. On the web, also a curated entry point into the book's themes.

### Appendix F: Substance-Related Patterns *(web only)*

- **Source file:** `appendices/appendix-f-substance-patterns.md`
- **Subtitle:** Recognizing Narcissistic Dynamics in Addiction and Recovery
- **Description:** Decoder cards for manipulation tactics involving alcohol, drugs, and other substances. A specialized companion to the main pattern catalog.

### Appendix G: Pop Culture References *(web only)*

- **Source file:** `appendices/appendix-g-pop-culture-references.md`
- **Subtitle:** Films, Shows, and Music That Illustrate the Patterns
- **Description:** Browsable, link-rich catalog of cultural touchstones that illustrate the dynamics named in the book. Designed for the web — searchable, linkable, and expandable as new references emerge.

---

## Front matter note (for the print edition)

Insert in the front matter of the printed book:

> **A note on the appendices.** Four appendices are bound into this book — **B (Glossary), C (Bibliography), D (Core Techniques), and E (Index)**. Three additional appendices — **A (Resources), F (Substance-Related Patterns), and G (Pop Culture References)** — are hosted at the companion library on the author's website, where they can be kept current. The lettering is consistent across both editions: a reference to "Appendix A" in this book always points to the same Appendix A on the website.

---

## Implementation notes

1. **Reader routes.** The seven appendixes are already exposed via `app/reader/chapters.ts` for Vol 1. No changes needed there for the policy in this document — the reader serves all seven from the source MD files.
2. **Library landing page.** Build a `/library/vol-1` (or equivalent) page using this document as the source of truth. Render the table at the top, then the entries section, with each `Source file` linking to the rendered reader page for that appendix.
3. **Print build.** The print manuscript (`vol-1-complete-manuscript.md`) has been pruned to A, F, G removed; the front-matter note above should be added during the next print pass.
4. **Cross-references in the print body.** The body still contains in-text "See Appendix A" pointers that originally referenced the printed Appendix A. These should be replaced — either with the timeless crisis statement *("If you are in immediate danger, contact your local emergency services or a domestic violence hotline in your country.")* or with a single companion-URL pointer per relevant chapter — in a follow-on editorial pass. This is a separate task from the distribution decision documented here.
5. **Maintenance.** Assign an owner for quarterly review of Appendix A. Appendix G should be reviewed annually as cultural references age. Appendices B, C, D, E follow the normal book revision cadence.
