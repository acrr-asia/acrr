# Series audit: Industrial Automation

- Series: `industrial-automation`, 5 entries, status published, no planned entries; previous series review `reviews/industrial-automation.md` (resolved 2026-10-13; its corrections F1-F16 and S1-S3 are present in the files and are kept).
- Audited at commit `e21dcc8`, 2026-10-13.

## Structural consistency across entries (before revision)

| Entry | Words (`eos status`) | Numbered sections | Opening: builds-on / conventions | Exercises | Summary | Closing transition | References |
|---|---|---|---|---|---|---|---|
| 1 Logic and Sequential Control | 3,967 | Yes, incl. `## 6. Exercises`, `## 7. Summary` | Yes / Python 3, IEC edition | 5 with answers | Table | To entry 2 | 6, "5th edition" form, unordered |
| 2 Programmable Logic Controllers | 4,420 | Yes | Yes / Python 3, IEC 61131-3:2013 + 2025 note | 5 | Table | To entry 3 | 7, unordered |
| 3 Fieldbuses and Industrial Ethernet | 4,316 | Yes | Yes / Python 3 | 5 | Table | To entry 4 | 8 lines bundling ~13 works |
| 4 PID Control of Process Variables | 3,719 | Yes | Yes / % of span, s, $e = r - y$, Python 3 | 5 | Table | To entry 5 | 5, journal articles without pages |
| 5 Networked Automation and Digital Twins | 4,466 | Yes | Yes / Python 3 | 5 | Table | Closes the series (layers) | 7 |

The structure is uniform and already meets standards 6.2: every entry numbers its sections (Exercises and Summary numbered, References as `### References` under the Summary), opens with what it builds on (linked), ends with a summary table and a transition naming the next entry. No structural change is needed. The systemic problems are metadata and house style:

1. **Descriptions** of 263-392 characters in all five entries and 219 in the overview; each is a list of the entry's sections rather than one sentence of what the reader learns.
2. **Title-case level-2 headings** in every entry (27 headings); the level-3 headings are already sentence case.
3. **References** not in the simplified IEEE house format: "5th edition" instead of "5th ed.", journal articles without volume/issue/pages, several works in one bullet, entries not alphabetical, IEC titles title-cased instead of as published.
4. Scattered intensifiers ("very", "simply", "actually", "quite", "clearly") and a few 50-77-word sentences.

## Notation and terminology

- Consistent across entries: `stop_ok`, seal-in, TON/TOF/TP, scan cycle, input/output image, $T_c$ (entry 1) and $T_\text{scan}$ (entry 2) for the evaluation period (entry 2 introduces its own symbol for the PLC case; acceptable), $e = r - y$, percent of span, "setpoint" (closed compound), "data sets" (entry 5, house form), "Ethernet" capitalized, American spelling.
- The deterministic audit's "datasets vs data set" item does not occur in this series: `grep -i dataset` finds nothing; entry 5 already writes "data sets".
- "Don't-care" (entry 1) is the established term from digital design, not a prose contraction; kept (see the entry's audit).
- Abbreviations are expanded at first use, with two exceptions in entry 3 (CAN in the introduction, CRC in the layer table, both expanded later) and two in entry 4 (PI, OPC UA).

## Overlap and gaps

- No harmful overlap remains after the previous review's F10 cuts. Entry 1, Section 1.4 repeats the series list as a table; it orients a reader arriving at the first entry and is kept.
- **Gap between the overview and the entries:** the overview's four objectives cover entries 1-4; entry 5 (ISA-95, OPC UA, IEC 62443 zones and conduits, digital twins) has none (overview finding D1). The previous review's objective map shows the same four rows.
- Topology is treated briefly in entry 3 (Section 2.2) against an objective that names it; noted by the previous review as adequate; unchanged.

## Overview page against standards 6.5

| Requirement | Before |
|---|---|
| What the series covers and why in that order | Covered by one 86-word list sentence; the dependency of each entry on the previous one is not stated |
| Intended reader and prerequisites | Yes |
| What each entry contributes and how they connect | Listed, not connected |
| Shared conventions | Not stated (IEC 61131-3 edition, % of span, Python 3) |
| 3-6 checkable objectives, each covered | 4 verb-first objectives, all covered, but entry 5 has none |
| Description 70-165 characters | 219 |

## Cross-references

- Within the series (checked): entry 2 → entry 1 Section 2.1, 5.2 (anchor `#52-a-worked-example-a-mixing-tank`), 5.3; entry 4 → entry 2 Section 3.3; entry 5 → entry 3 Section 3.1 and anchor `#9-time-sensitive-networking`, entry 2 Section 3.3; entry 3 → entry 2 Section 2.2 ("Section 6.2" internal). All resolve. Changing heading case does not change the generated anchors (slugs are lowercase).
- No file outside the series links to an entry of this series with a fragment (grep of `src/content`, `src/views`, `src/components`).
- Out of the series: entry 2 → `sampling-quantization-and-data-conversion`; entry 4 → `introduction-to-control-systems`, `feedback-and-system-behavior`, `/series/foundations-of-control-systems` (all accurate; see the entry 4 audit); entry 5 → `numerical-integration-notes`, `sensing-and-state-estimation`.
