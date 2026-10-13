<!-- audit: {"slug":"sensing-principles","type":"article","series":"sensor-systems","priority":"P2","before":{"purpose":3,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":3}} -->
# Audit: Sensing Principles: How Physical Effects Become Electrical Signals

- Path: `src/content/blog/sensing-principles.mdx` · Route: `/blog/sensing-principles` · Type: article · Series `sensor-systems`, entry 2 of 7 · Words: 2532
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: the opening refers to "the previous entry" without linking it, and the second paragraph is a prose outline.
- structure 3: §9 ends "That last question leads to the next entry", and the Summary ends with the same transition.
- evidence 3: reference list not in house format ("5th edition", "(eds.)" placement, not alphabetical). Material constants (quartz 2.3 pC/N, type K 41 µV/K) are uncited typical values; the previous series review checked them for plausibility only.
- language 3: ten title-case H2 headings; "well-standardised" (British); "−4.4 %", "0.39 %", "0.005 %" spacing; three "very" (lint).
- consistency 3: "the robotics series" (line 166) not linked; NTC expanded after the abbreviation ("The common **NTC** (negative temperature coefficient)") rather than term first.
- publishing 2: description 288 characters.

Accuracy recomputed: NTC 33.62 / 3.588 / 0.698 kΩ, −4.44%/K; 8.854 pF and +0.0089 pF per µm (text "about 0.09 pF" for 1 µm of 100 µm gap: recomputed $C(99\,\mu m) - C(100\,\mu m) = 0.089$ pF, correct); responsivity 0.548 A/W; Nernst 59.16 and 61.54 mV; strain gauge 0.7 Ω. All correct.

## Priority

P2: should-fix metadata and style problems a reader would notice; no accuracy problem.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 288 characters. |
| P2 | Should fix | H2 headings | language | Title case. |
| C1 | Should fix | lines 55, 63, 73, 128 | language | "standardised"; space before %. |
| P3 | Should fix | References | evidence | Not in house format or alphabetical. |
| D1 | Should fix | lines 14, 166 | consistency | Entries and the robotics series mentioned without links (standards 8.1: link the first mention). |
| D2 | Optional | line 16 | structure | Prose outline in opening. |
| D3 | Optional | line 196 | structure | Duplicate transition ("That last question leads to the next entry"). |
| C2 | Optional | lines 128, 146, 190 | language | "very" (lint intensifiers). |

### P1. Description
- **Text:** "The physical effects behind almost every sensor, organized by how they produce a signal: resistive, capacitive, ... each with its governing equation, a worked number, and its strengths and weaknesses."
- **Correction:** "Learn the physical effects behind most sensors, from resistive and capacitive to piezoelectric, thermoelectric, optical and electrochemical, with worked numbers." (160)

### D1. Unlinked references
- **Text:** "The previous entry treated the sensing element as the first box ..."; "(the encoders of the robotics series)".
- **Correction:** Link the previous entry; "(the joint encoders of the [robotics series](/blog/what-is-a-robot))" pointing to the entry that introduces encoders.

### D3. Duplicate transition
- **Text:** "That last question leads to the next entry." (line 196) and the Summary's closing paragraph.
- **Correction:** Cut the sentence in §9.

## Revision log (wave 1)
- Structure: opening paragraph 2 condensed; it now states that worked numbers use typical material constants; the duplicate transition at the end of §9 removed.
- Prose/style: ten H2s to sentence case; "standardised" → "standardized"; "%" spacing (also inside KaTeX: `-4.4\%`, `0.005\%`); NTC now term-first; three "very" reviewed: two removed ("self-generating and stiff", "wide ranges"), one kept in the table ("very high temperatures" contrasts with the other rows).
- Metadata: description 161 characters.
- References: house format, alphabetical; "(eds.)" → ", Eds.,".
- Cross-references: links to the previous entry, the signal-conditioning entry, the next entry, and the robotics entry that introduces joint encoders (`/blog/what-is-a-robot`).
- Remaining warnings: none. Suggestions: PT100 at line 55 (explained in entry 1, used here with its value), CRC (publisher name), one 56-word sentence on Hall-sensor uses (a list).
- Flags for independent review: fact-check typical constants (quartz 2.3 pC/N, type K ≈ 41 µV/K) against a cited source (Fraden or Webster/Eren); not verified in this wave.
- Vietnamese translation affected: yes, wording only (description, opening paragraph 2, removed sentence in §9, "Special charge amplifiers" → "Charge amplifiers").
