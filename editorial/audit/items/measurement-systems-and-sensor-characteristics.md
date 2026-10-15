<!-- audit: {"slug":"measurement-systems-and-sensor-characteristics","type":"article","series":"sensor-systems","priority":"P1","before":{"purpose":4,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":3}} -->
# Audit: Measurement Systems and Sensor Characteristics

- Path: `src/content/blog/measurement-systems-and-sensor-characteristics.mdx` · Route: `/blog/measurement-systems-and-sensor-characteristics` · Type: article · Series `sensor-systems`, entry 1 of 7 · Words: 2595
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- structure 3: the second opening paragraph is a table of contents in prose ("The approach is from the outside in: first ..., then ..., then ..., and finally ...").
- evidence 3: references not in house format (Section 7.3): "5th edition" instead of "5th ed.", no years on the JCGM and IEC entries, standards titles in headline case rather than their original case, list not alphabetical.
- language 3: all eight H2 headings in title case ("What a Measurement Is", "Errors and Uncertainty"); space before % in seven places ("63.2 %", "0.375 %"); British "linearisation" survives in the Mermaid label (line 47), which is visible on the page.
- consistency 3: "endpoint line" (line 102) and "end points" (line 100) for the same thing; PT100 not explained as a designation at first use (lint `acronym-expansion`); JCGM not expanded.
- publishing 2: description 293 characters and a fragment.

Accuracy recomputed with python3: $R(100) = 138.506$ Ω; local slopes 0.3908 and 0.3793 Ω/°C; end-point nonlinearity 0.1444 Ω = 0.375 °C; $u_c = 0.0525$ °C, $U = 0.105 \to 0.11$ °C; $g = 1.01317$, 50.25 °C; $I^2R = 0.1385$ mW. All match the text.

## Priority

P1: foundational first entry; its vocabulary is used by every later entry.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 293 characters, a fragment. |
| P2 | Should fix | H2 headings lines 22–224 | language | Title-case headings. |
| C1 | Should fix | lines 32, 102, 135, 145–147, 177 | language | Space before % (standards 5.5). |
| C2 | Should fix | line 47 (Mermaid) | language | "linearisation" (British) in a visible diagram label. |
| P3 | Should fix | References, lines 241–246 | evidence | Not in house format; not alphabetical; no years on standards. |
| D1 | Optional | line 20 | structure | Prose table of contents. |
| C3 | Optional | lines 100–102 | consistency | "end points" / "endpoint line". |
| C4 | Optional | lines 34, 86 | language | JCGM and PT100 not explained at first use. |

### P1. Description
- **Text:** "What it means to measure something, and how to describe a sensor: the measurement chain from measurand to number, static characteristics such as sensitivity, ..."
- **Correction:** "Learn what a measurement is and how to describe a sensor: the measurement chain, static and dynamic characteristics, error, uncertainty and calibration." (153)

### P2. Headings
- **Text:** "## 1. What a Measurement Is", "## 2. The Measurement Chain", "## 3. Static Characteristics", ... "## 7. Choosing a Sensor".
- **Correction:** sentence case ("## 1. What a measurement is"). Slugs are lower case already, so fragment links (`#5-errors-and-uncertainty`, `#6-calibration`, used by entry 7) are unchanged.

### C1. Percent spacing
- **Text:** "at about 95 % confidence", "0.375 % of span", "63.2 % of the step", "(often 90 %)".
- **Correction:** "95%", "0.375%", etc.

### C2. British spelling in diagram
- **Text:** `P["Processing<br/>linearisation, calibration, filtering"]`
- **Correction:** "linearization".

### P3. References
- **Text:** "J. Fraden, *Handbook of Modern Sensors: Physics, Designs, and Applications*, 5th edition, Springer, 2016." / "IEC 60751, *Industrial Platinum Resistance Thermometers and Platinum Temperature Sensors*, International Electrotechnical Commission (2008 and 2022 editions, which give the same coefficients)."
- **Correction:** House format, alphabetical, years; standards titles in their original case (IEC 60751:2022 title confirmed at webstore.iec.ch/publication/63753).

### D1. Prose table of contents
- **Text:** "The approach is from the outside in: first the idea of measurement and its unavoidable uncertainty, then the chain of components ..., then the properties ..., and finally how errors are estimated ..."
- **Correction:** Shorten to one sentence that also states the conventions used (SI units, VIM/GUM vocabulary).

## Revision log (wave 1)
- Structure: second opening paragraph (prose outline) replaced by one sentence on the approach plus the conventions (prerequisites, SI, VIM/GUM vocabulary of Section 1.2).
- Prose: the VIM/GUM sentence split, with JCGM expanded; "PT100" designation explained at first use; "end points" made "**endpoint line**" (defined in bold, matching the glossary's closed compound `endpoint`).
- Terminology/style: eight H2 headings to sentence case (slugs unchanged); "%" spacing (9 places); Mermaid label "linearisation" → "linearization".
- Metadata: description rewritten, 146 characters.
- References: house format (`ed.`, years), standard titles in their original case (IEC 60751:2022 title confirmed on the IEC webstore; VIM and GUM titles as published by JCGM), alphabetical; IEC entry now cites the 2022 edition with the note on 2008.
- Cross-references: links added to the fourth entry (quantization), the signal-conditioning entry and the next entry at first mention.
- Technical corrections: none needed (recomputation in the audit section).
- Remaining warnings: none. Suggestions left: sentence length at lines 28, 51, 100 (lists of SI units and of chain stages; splitting would separate items from their list), `acronym-expansion` PT100 at line 86 (explained in the same sentence, after the symbol).
- Flags for independent review: fact-check that IEC 60751:2008 and :2022 give identical $A$, $B$ coefficients (carried over from the previous review, not re-verified); confirm VIM/GUM original title punctuation (en dash vs em dash in the JCGM PDFs).
- Vietnamese translation affected: yes, wording only: description; opening paragraph 2; PT100 gloss; "endpoint line" definition; VIM sentence split. No technical meaning changed. Headings in Vietnamese are already lower case by convention.

## Revision log (wave 2 resolution)

Date: 2026-10-15. Resolves `reviews/sensor-systems.md`.

- S5: figure caption now says "relative to the endpoint line" (line 104).
- F4: removed the unverified parenthetical "(The 2008 edition gives the same coefficients.)" from the IEC 60751:2022 reference (line 243).
- Vietnamese follow-up: caption wording (S5) and the reference parenthetical (F4).
- Lint: 0 errors, 0 warnings; syntax: compiles.
