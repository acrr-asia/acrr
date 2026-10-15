<!-- audit: {"slug":"smart-sensors-and-mems","type":"article","series":"sensor-systems","priority":"P2","before":{"purpose":4,"structure":3,"accuracy":4,"evidence":3,"language":2,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":2}} -->
# Audit: Smart Sensors and MEMS

- Path: `src/content/blog/smart-sensors-and-mems.mdx` · Route: `/blog/smart-sensors-and-mems` · Type: article · Series `sensor-systems`, entry 6 of 7 · Words: 2589
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- structure 3: prose outline in the opening (line 24); otherwise the progression (material → fabrication → scaling → sensors → electronics → costs) is sound.
- evidence 3: references not in house format; Gabrielson's title has the comma outside the quotes and no month (house format does not require it). The "130 to 190 GPa" range for silicon and "gauge factors of the order of 100" are typical values, uncited; flagged as in the previous review.
- language 2: British "micrometre(s)" five times and "picometres" once survived the spelling standardization (lines 21, 38, 39, 82, 90, 175) while "millimeter" and "centimeters" are American in the same sentences; six title-case H2s; "very" three times; 64-word sentence on self-test (line 143).
- consistency 3: "the robotics series" (line 96) unlinked; "the noise entry", "the signal-conditioning entry", "the data-conversion entry" unlinked at first mention; SPI and FIFO not expanded (FIFO expanded only in entry 7).
- publishing 2: description 359 characters (the longest in the series).

Accuracy recomputed: 9.94 nm per g; 0.994 fF per g; $a_n = 7.22 \times 10^{-4}$ m/s²/√Hz = 73.6 µg/√Hz, 0.736 mg in 100 Hz; drive velocity 1.257 m/s; Coriolis 0.0440 m/s² = 4.48 mg; $\Delta V_\text{BE}$ 53.8 mV and 0.179 mV/K. All correct.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 359 characters. |
| C1 | Should fix | lines 21, 38, 39, 82, 90, 175 | language | "micrometre", "picometres" (British; standards 5.1). |
| P2 | Should fix | H2 headings | language | Title case. |
| P3 | Should fix | References | evidence | House format, alphabetical. |
| D1 | Should fix | lines 17, 32, 96, 121 | consistency | Earlier entries and the robotics series unlinked; SPI, FIFO unexpanded. |
| C2 | Optional | line 143 | language | 64-word sentence. |
| D2 | Optional | line 24 | structure | Prose outline. |

### C1. British spellings
- **Text:** "with dimensions from about a micrometre to a millimeter"; "a mass displacement of 7 picometres".
- **Correction:** micrometer, micrometers, picometers.

### P1. Description
- **Correction:** "Learn what changes when sensor and electronics share a package: MEMS fabrication and scaling, accelerometers and gyroscopes, on-chip compensation and its costs." (161)

## Revision log (wave 1)
- Prose/style: British "micrometre(s)" and "picometres" → American (six places); six H2s to sentence case; "very different rates" → "rates that differ by orders of magnitude" (anisotropic KOH etch selectivity between crystal planes is of that order; flagged below); "very often" → "often"; self-test sentence split; I2C, SPI and FIFO expanded.
- Structure: opening outline condensed; states that worked numbers describe a representative design, not a product.
- Metadata: description 162 characters.
- References: house format (comma inside the Gabrielson title quotes), alphabetical.
- Cross-references: links added to the sensing-principles (§2.2), signal-conditioning (§2.2), noise (§2.1) and data-conversion (§5.2) entries and to the robotics state-estimation entry.
- Remaining warnings: none. Suggestions: RMS (line 90, expanded in earlier entries; common in the series), FIFO flagged after expansion (lint matches the bolded form), sentence length at 96, 143, 151.
- Flags for independent review: technical reviewer to confirm "rates that differ by orders of magnitude" for KOH on (100)/(111) planes (replacing "very different rates"); typical constants (silicon 130–190 GPa, gauge factor ≈ 100) still uncited.
- Vietnamese translation affected: yes, wording only (description, opening, KOH phrase, self-test sentence, bus expansions).

## Revision log (wave 2 resolution)

Date: 2026-10-15. Resolves `reviews/sensor-systems.md`.

- S1: "on the same chip" -> "in the same package" (line 82), and the preceding "needs its electronics on the chip" -> "in the same package" (line 77). Heading "4. The electronics on the chip" kept for anchor stability.
- Vietnamese follow-up: lines 77 and 82 wording.
- Lint: 0 errors, 0 warnings; syntax: compiles.
