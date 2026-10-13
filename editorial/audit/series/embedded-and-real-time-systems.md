# Series audit: Embedded and Real-Time Systems

- Series file: `src/content/series/embedded-and-real-time-systems.md` · 5 entries, published, no planned entries
- Audited at commit `e21dcc8`, 2026-10-13, by the wave-1 Content Auditor; previous series review `reviews/embedded-and-real-time-systems.md` (resolved, all 13 findings plus S1, S2 applied; verified still in place).

## Structural consistency across entries

- **Numbering**: all five entries number every H2 and H3, and number Exercises and Summary as sections (`## 8. Exercises`, `## 9. Summary`); References is an unnumbered `### References` under the Summary in all five. Consistent.
- **Opening paragraphs**: every entry opens with what it builds on (linked), what it covers, and a **Conventions** paragraph. Consistent. Entry 1 also carries the series prerequisites.
- **Summary**: every entry has a question/answer summary table and a closing paragraph leading to the next entry; entry 5 closes the series against its objectives.
- **Exercises with answers**: present in all five (4–5 each), all recomputed.
- **Headings**: H3 headings are already sentence case; every H2 except "Timers", "Exercises", "Summary" is in title case in all five entries (systemic).
- **Descriptions**: all six descriptions exceed 165 characters (189–401) and list the sections instead of saying what the reader learns (systemic).
- **References**: no entry follows the house format of standards 7.3 ("3rd edition", "35(3)", missing pages, not alphabetical) (systemic).

## Notation and terminology

- $C_i, T_i, D_i, B_i, R_i, U$ consistent between entries 4 and 5; $L$ (loop period) in entry 2; $t_\text{bit}$ in entry 3.
- "utilization" is the technical quantity of scheduling theory throughout entries 4 and 5; kept despite the glossary's "utilize" rule.
- Spelling variant drift: "zero-initialised" (1), "resynchronising/-ise/-isation" (3), "analysable", "normalise", "utilisation" (4, code comment), "analysed" (5, diagram label). "start-up" (5) vs "startup" (1).
- Percent written with a space ("2.4 %") in prose across all entries; standards 5.5 asks for none.
- I2C written in ASCII throughout (glossary form).

## Overlap and gaps

- No harmful duplication: entry 2 refers back to entry 1 for read-modify-write; entry 4 refers back to entry 2 for race conditions and ISR rules; entry 5 refers back for timers, latency components and stack layout.
- The Davis et al. (2007) CAN analysis is described in entries 3 (§5.3) and 4 (§2.4); entry 4 was corrected by the series review (S2), entry 3's wording is slightly different and is aligned in this wave.
- No gaps against the objectives.

## Overview page against standards 6.5

- Reader and prerequisites: present.
- Sequence rationale and how entries connect: only implicit, in one 150-word paragraph.
- Conventions: partly stated.
- Objectives: four, each with an assessable verb; objective 4 promises verification "by measurement", contradicting entry 5's thesis.
- Description: too long and a fragment.

## Cross-references

`eos lint` reports no `series-crossref` or internal-link errors. All "Section x.y of the n-th entry" references were checked by hand against the headings; all correct. Renaming the two "The frame" headings in entry 3 changes their anchors; no link in `src/content` targets them.
