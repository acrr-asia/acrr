<!-- audit: {"slug":"logic-and-sequential-control","type":"article","series":"industrial-automation","priority":"P1","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":4}} -->
# Audit: Logic and Sequential Control

- Path: `src/content/blog/logic-and-sequential-control.mdx` · Route: `/blog/logic-and-sequential-control` · Type: article (series entry) · Series `industrial-automation`, entry 1 of 5 · Words: 3,967 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4: context (1), concept and mechanism (2-5), worked examples with recomputed output, limits (2.5, 4.3, 5.4), exercises, summary, closing transition. Nothing out of order.
- accuracy 4: both Python programs re-run (`True`; the four transition lines match byte for byte); level-switch K-map, don't-care map, timer bounds (100-110 ms, 120-150 ms; Exercise 4: 60-80 ms and 40-60 ms), Exercise 1 ($\overline{B}\,\overline{D} + BD$), mixing-tank timings (37.5 s, 39.5 s, 87.0/87.5 s, 2-point overshoot) recomputed.
- evidence 3: references not in house format ("5th edition", no years on the standards, not alphabetical).
- language 3: intensifiers ("very", "actually", "simply"); two sentences over 50 words.
- consistency 3: reference format differs from the house style; otherwise consistent with entries 2-5.
- publishing 2: description 266 characters and a list of topics; five level-2 headings in title case.

## Priority

P1: first entry of the series; the vocabulary of entries 2-5 rests on it.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 266 characters, a list ("The foundation of the industrial automation series: ...") |
| P2 | Should fix | `:21, 62, 173, 227, 255` | publishing | Level-2 headings in title case (`heading-case`) |
| C1 | Should fix | `:426-431` | evidence | References not in house format: "5th edition", standards without years, not alphabetical, IEC titles not in their original capitalization |
| C2 | Should fix | `:231`, `:239` | language | Sentences of 52 and 54 words (the timer sentence carries a nested parenthetical on editions) |
| C3 | Optional | `:15`, `:19`, `:239` | language | Intensifiers: "look very different", "the languages that industrial controllers actually run", "is simply an on-delay" |
| C4 | Optional | `:158-171`, `:416` | language | `contractions` warnings on "don't-care" |
| C5 | Optional | `:74` | language | "why this algebra fits automation so naturally" |
| C6 | Optional | `:422` | consistency | Closing paragraph names "the five languages that IEC 61131-3:2013 defines" without signalling the 2025 edition, which entry 2 now discusses; acceptable because the edition is named |

### P1. Description
- **Text:** "The foundation of the industrial automation series: what automation systems control, Boolean algebra and Karnaugh maps for combinational logic, latches and edge detection for memory, timers and counters, and the description of sequential processes as state machines."
- **Correction:** "How Boolean algebra, Karnaugh maps, latches, timers and state machines describe the logic and sequential control of industrial machines and processes." (≤165)

### P2. Heading case
- **Text:** "## 1. What Industrial Automation Controls", "## 2. Boolean Algebra for Control", "## 3. Memory: Latches and Edges", "## 4. Time: Timers and Counters", "## 5. Sequential Control as State Machines".
- **Correction:** sentence case. The anchors are lowercase slugs, so `#52-a-worked-example-a-mixing-tank` (linked from entry 2) is unaffected.

### C1. References
- **Text:** "M. M. Mano and M. D. Ciletti, *Digital Design*, 5th edition, Pearson, 2013." ... "IEC 60848, *GRAFCET Specification Language for Sequential Function Charts*, International Electrotechnical Commission."
- **Correction:** "5th ed."; alphabetical (Bolton, Cassandras, IEC 60848, IEC 61131-3, Mano, Petruzella); IEC titles as published ("GRAFCET specification language for sequential function charts", edition 3.0, 2013, confirmed on IEC/VDE/SCC listings; "Programmable controllers – Part 3: Programming languages", 2013, confirmed on the IEC webstore listing).

### C2. Long sentences
- **Text (231):** "Three timer behaviors cover nearly all needs, and the international standard for controller languages, IEC 61131-3 (the second entry's subject; this series follows its third edition, IEC 61131-3:2013, which a fourth edition replaced in 2025), defines them as standard **function blocks**, ..."
- **Correction:** split; move the edition statement to its own sentence.

### C4. "Don't-care"
- **Where:** heading "2.5 Don't-care conditions", `:160`, `:162`, `:169`, `:171`, `:416`.
- **Problem:** the linter reads "don't" as a contraction. It is the established name of the concept in digital design (Mano and Ciletti, Chapter 3, "Don't-care conditions"), not prose contraction; none of the occurrences is in a quotation or code.
- **Correction:** keep the term (defined in bold at `:160`); record the warnings as justified. Rewriting it as "do-not-care" would be non-standard and would confuse readers who look it up.

## Revision log (wave 1)
- Structure: none needed (the entry already follows standards 6.2).
- Prose: the 52-word timer sentence split, with the edition statement as its own sentence ("This series follows the standard's third edition, IEC 61131-3:2013; a fourth edition replaced it in 2025."); the debounce sentence split; the mixing-tank check sentence split; "look very different" → "look nothing alike"; "actually run" → "run"; "is simply an on-delay" → "is an on-delay"; "fits automation so naturally" → "explains why this algebra suits automation". (C2, C3, C5)
- Headings: five level-2 headings to sentence case; numbering unchanged; anchors unchanged. (P2)
- Metadata: description 266 → 152 characters, one sentence of what the reader learns. (P1)
- References: house format ("5th ed."), alphabetical, IEC titles as published; IEC 60848 dated 2013 (edition 3.0, confirmed on IEC/VDE/SCC catalogue listings); IEC 61131-3:2013 given its year (IEC webstore listing). (C1)
- Technical content: unchanged. Both Python programs re-run; output identical to the text.
- Remaining warnings and why they stay: 6 `contractions` warnings on "don't-care" (heading 2.5 and lines 160, 162, 169, 171, 416). It is the established technical term for an unspecified truth-table entry (Mano and Ciletti, *Digital Design*, "don't-care conditions"), defined in bold at line 160, not a prose contraction; replacing it would make the term unrecognizable. One `intensifiers` suggestion ("described more clearly", line 259) is a comparison, not an intensifier. Acronym suggestions (TRUE, FALSE, ON, OFF, AND, OR, NOT, state names) are false positives.
- Flags for independent review: none on accuracy. Fact-check: the statement "a fourth edition replaced it in 2025" rests on the previous review's check of the IEC listing (IEC 61131-3:2025, ED4, 22 May 2025); not re-verified in this wave.
- Vietnamese translation affected: no translation of this article exists.

## Independent review (wave 2)
- Fact-check: pass (IEC 61131-3:2025 Ed. 4.0, 22 May 2025, verified; IEC 60848:2013 and IEC 61131-3:2013 references consistent).
- Technical: pass (both Python blocks re-run, output identical; Karnaugh maps, exercises, timer bounds and mixing-tank timings recomputed).
- Findings concerning this item: none. Report: `reviews/industrial-automation.md`.
- Not verified: book editions and years of Bolton, Cassandras and Lafortune, Mano and Ciletti (consistent with reviewer knowledge, not fetched); Petruzella 5th ed. 2016 verified.
