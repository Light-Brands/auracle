# Sibling Anonymization Audit — Pre-Phase-2

**Round:** 7
**Decision driver:** Diana Q13 (Author Decisions, decision A — audit before Phase 2)
**Standing decisions audited (from `unified-woven-integration-plan.md`):**

> **#2 — Anonymize the author's sibling references.** Any relational detail about the author's sibling is anonymized throughout the manuscript as "a family member" — no sibling role, no named relationship.

> **#3 — The Testimony is anonymized.** The Ch 8 Testimony passage stays in the book in close third or second person, attributed only to "a family member." No sibling label, no named role, no identifying relational detail.

**Method:** Grep across `vol-1-complete-manuscript.md` for `brother`, `sister`, `sibling`, `my brother`, `my sister`, `family member`. Each match classified as:

- **A. Author first-person reference** — must be anonymized as "a family member"
- **B. Composite/client field note** — third-person about other people; sibling labels permitted
- **C. Reader-direct address** — second-person about reader's relationships; sibling labels permitted
- **D. Generic taxonomy** — lists of role types; not about specific persons
- **E. Mythology / external reference** — Ali Baba, swans/brothers, etc.; not about real people

---

## Verdict: MOSTLY PASS, ONE CONFIRMED VIOLATION + ONE CANDIDATE

### Confirmed violation: Ch 8 Testimony uses "her siblings" twice

**Location:** Lines 7140 and 7148 of `vol-1-complete-manuscript.md` (Ch 8 Field Note: The Testimony).

**Quoted prose:**

> "Her siblings depend on her. Her mother depends on her. The family depends on her saying what needs to be said." (line 7140)

> "She chose her mother. She betrayed her father. She protected her siblings, or so she told herself." (line 7148)

**Why this is a violation:** Standing decision #3 explicitly states "no sibling label, no named role." The Testimony is correctly in close-third, attribution is implicit (not named), but "her siblings" is a sibling-role label.

**Recommended fixes** (author selects one):
- Option A: `her siblings` → `her family`
- Option B: `her siblings` → `her family members`
- Option C: Cut the second-half clauses entirely. (E.g., "She chose her mother. She betrayed her father. She did what she had to do, or so she told herself.")

**Author note:** The Testimony's emotional weight depends on the protection-instinct beat. Option A is the lightest substitution that preserves the beat. Option C reframes the moral injury without changing the family-system architecture; cleanest if the protect-them-at-a-cost emotional logic carries equally without the named role.

---

### Candidate violation: Ch 8 "First sister / second sister" wedding passage

**Location:** Lines 7240–7242 (Ch 8, mother-wedding field note).

**Quoted prose:**

> "The first sister got married and her mother barely participated… The second sister got married years later. She thought — maybe this time."

**Why this is a candidate:** The phrasing "first sister … second sister" reads as *anonymized but role-named*. If this passage is about the author's actual family, it violates standing decision #2 (no sibling role permitted).

**Cannot resolve from manuscript alone — author triage required:**
- If this is the author's biography → must change to "the first daughter / the second daughter," "the older / the younger," "one woman / years later, another," or fold into one figure.
- If this is a composite client field note → CURRENT WORDING IS ACCEPTABLE per category B (sibling labels permitted in composite material).

---

## Pass: 27 other matches reviewed and clear

### Author first-person references (Category A) — all compliant

| Line | Quote | Status |
|------|-------|--------|
| 1066 | "A fifteen-minute phone call with a certain family member would knock her out for three hours" | ✅ Anonymized as "a certain family member"; no sibling role |
| 5767 | "I have a family member who made me feel intellectually small for years" | ✅ Anonymized as "a family member"; no sibling role |

### Composite/client field notes (Category B) — sibling labels permitted

| Line | Context | Status |
|------|---------|--------|
| 6322 | "his sister pulled me aside" | ✅ Partner's sister in client composite |
| 6625 | "Her older sibling got the attention for sports" | ✅ Third-person field note about a client/composite |
| 6674 | "her brother was the screwup… Then she came out" | ✅ LGBTQ+ rejection composite, third-person |
| 6701 | "she'd not spoken to her sister for three years" | ✅ Mother-triangulation composite |
| 6743 | "the older sister pulled the younger onto a phone call" | ✅ Composite client material, third-person |
| 6757–6759 | "the older sister made a mistake and somehow flipped the whole thing" | ✅ Composite, third-person; same family as 6743 |
| 6879 | "what you told her in vulnerability, she repeats to your sister" | ✅ Reader-direct (Category C) |
| 7072 | "Triangulates you with a sibling (especially the Golden Child)" | ✅ Reader-direct list item |

### Reader-direct address (Category C) — sibling labels permitted

| Line | Context | Status |
|------|---------|--------|
| 6246 | "You parent your partner/friend/sibling" | ✅ Direct-address taxonomy |
| 6689 | "They tell you what your sibling 'said' about you" | ✅ Direct-address list item |
| 6691 | "They compare you to another family member" | ✅ Direct-address list item |
| 6733 | "Unable to have direct, honest relationships with siblings or other family members" | ✅ Direct-address consequence list |
| 8392–8541 | Ch 10 §"Sibling Dynamics in Narcissistic Families" — entire section | ✅ Direct-address chapter content; "your sibling" throughout |
| 9758 | "Comparison to siblings or other family members" | ✅ Direct-address pattern |
| 10643 | "I was really harsh with my sister once, said things I regret" | ✅ Sample healthy-response dialogue, hypothetical voice |
| 12871 | "When mother leaks your confidence to sibling" | ✅ Ch 16 script header, direct-address |
| 12907, 12973, 12991 | Ch 16 sibling-script subsections | ✅ Direct-address scripts for reader |
| 13010 | "See also: Chapter 9, Two Modes: What Sibling Exchange Actually Looks Like" | ✅ Cross-reference |
| 13766–13767 | "What is your approach if a client is considering going no-contact with a family member?" | ✅ Therapist-vetting questions |

### Generic taxonomy (Category D)

| Line | Context | Status |
|------|---------|--------|
| 630 | "your boss, your friend, or your sibling specifically" | ✅ Generic role list |

### Mythology / external (Category E)

| Line | Context | Status |
|------|---------|--------|
| 3443 | Ali Baba and his brother | ✅ Mythological reference |
| 3838 | The youngest brother's shirt (swan tale) | ✅ Mythological reference |

---

## Summary

| Standing decision | Status |
|-------------------|--------|
| #2 (author's sibling references → "a family member") | **PASS** — both author first-person references are properly anonymized |
| #3 (Testimony → no sibling label, no named role) | **FAIL** — two "her siblings" instances at lines 7140 and 7148 |
| Candidate triage | One passage at lines 7240–7242 ("first sister / second sister") needs author triage; if biographical, requires rewording |

**Action items before Phase 2 launches:**

1. Author selects fix for Testimony violations (Options A/B/C above) — implement during Phase 1 implementation.
2. Author triages "first sister / second sister" passage — biographical or composite?
   - If biographical → reword in Phase 1 implementation.
   - If composite → log as compliant; no action.
3. Sage briefed in Phase 2 brief that sibling anonymization audit was run; she validates representation choices on cases that surface during her sensitivity pass, not the standing-decision compliance (already audited).

**Audit confidence:** High for first-person references and reader-direct address; depends on author triage for the wedding-passage candidate. No further automated audit can resolve that case.
