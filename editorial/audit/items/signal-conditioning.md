<!-- audit: {"slug":"signal-conditioning","type":"article","series":"sensor-systems","priority":"P2","before":{"purpose":4,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":3}} -->
# Audit: Signal Conditioning: Bridges, Amplifiers and Analog Filters

- Path: `src/content/blog/signal-conditioning.mdx` · Route: `/blog/signal-conditioning` · Type: article · Series `sensor-systems`, entry 3 of 7 · Words: 4028
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- structure 3: §7.1 "Protection and isolation" is one 93-word sentence (lint); otherwise the order (excitation → bridge → op-amp → in-amp → current/charge → filters → complete channel) is exemplary.
- evidence 3: references not in house format.
- language 3: eight title-case H2s; ten "N %" spacings; "very" twice.
- consistency 3: "the previous entry", "the first entry", "the noise entry" unlinked at first mention; the lint `acronym-expansion` flag for CMRR (line 149) is a false positive, since the term is defined in bold at line 141; LVDT not re-expanded in this entry (line 202).
- publishing 2: description 274 characters.

Accuracy recomputed: quarter bridge 2.4975 mV; Butterworth at 50 Hz 14.15/27.97/55.92 dB and at 3 Hz 0.958/0.996/0.99997; $R_G = 50.05$ Ω; RC cut-off 9.95 Hz; 0.1% resistor CMRR $(1+G)/(4\varepsilon) = 500$ → 54 dB; transimpedance 159 kHz; charge-amplifier 0.159 Hz; gain 450 → 2.97 V. All correct.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 274 characters. |
| P2 | Should fix | H2 headings | language | Title case. |
| C1 | Should fix | lines 18, 39, 80, 127, 151–152, 251, 260 | language | Space before %. |
| P3 | Should fix | References | evidence | House format, alphabetical order. |
| D1 | Optional | line 268 | structure | 93-word sentence in §7.1. |
| D2 | Optional | lines 18, 37 | consistency | First mentions of the previous and first entries unlinked. |
| C2 | Optional | line 202 | language | LVDT not expanded in this entry. |

### P1. Description
- **Correction:** "Learn the analog electronics between sensor and converter: excitation, Wheatstone bridges, instrumentation amplifiers and filters, built into a load-cell channel." (164)

### D1. Long sentence
- **Text:** "**Galvanic isolation**, which carries the signal across a barrier through a transformer, capacitor or optical link with no conducting path, is needed when the sensor sits at a dangerous voltage, as in current measurement on a power line or in medical equipment connected to a patient, or when two grounds far apart differ by more than the amplifier's common-mode range."
- **Correction:** Split into a definition sentence and a sentence on when it is needed.

## Revision log (wave 1)
- Structure: §7.1 isolation sentence split into definition and use.
- Prose/style: eight H2s to sentence case; "%" spacing (10); "very high input resistance" → "high input resistance"; LVDT expanded at first use.
- Metadata: description 165 characters.
- References: house format, alphabetical.
- Cross-references: links to the previous, first, noise and next entries at first mention.
- Remaining warnings: none. Suggestions: PT100 (line 32, glossed in the same sentence), CMRR (false positive, defined in bold at line 141), "very large open-loop gain" (kept: the point is that it is too large to use directly), sentence length at 18, 39, 268 (each one idea with a list).
- Flags for independent review: none new.
- Vietnamese translation affected: yes, wording only (description, §7.1 sentence split, LVDT expansion).
