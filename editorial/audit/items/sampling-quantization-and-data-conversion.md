<!-- audit: {"slug":"sampling-quantization-and-data-conversion","type":"article","series":"sensor-systems","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":3,"optional":3}} -->
# Audit: Sampling, Quantization and Data Conversion

- Path: `src/content/blog/sampling-quantization-and-data-conversion.mdx` · Route: `/blog/sampling-quantization-and-data-conversion` · Type: article · Series `sensor-systems`, entry 4 of 7 · Words: 2861
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- evidence 3: references not in house format; IEEE Std 1241-2010 has no publisher or year field.
- language 3: seven title-case H2s; the SAR parenthetical is a 73-word sentence (line 175); "very" twice.
- consistency 3: "the previous entry" unlinked; OSR, RC used without expansion (lint).
- publishing 2: description 293 characters.

Note: Sections 2.1 and 3.2 are linked from outside the scope (`designing-fir-and-iir-filters.mdx:166`, `#21-oversampling`; `#32-quantization-error-as-uncertainty`); their heading words must not change.

Accuracy recomputed: 76.34 dB vs 72.25 dB; $q$ = 0.806 mV / 50.4 µV / 0.197 µV; SQNR 74.0 / 98.1 dB; jitter limits 38.9 ns and 0.121 ns; 3686 / 58 982 codes, 2.71 / 0.170 g; SAR 2.000/0.206 = 9.70 LSB → code 9 truncating, 10 rounding. All correct.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 293 characters. |
| P2 | Should fix | H2 headings | language | Title case ("Anti-Aliasing Filters", "From Numbers Back to Voltages"). |
| P3 | Should fix | References | evidence | House format, alphabetical. |
| C1 | Optional | line 175 | language | 73-word sentence in parentheses. |
| C2 | Optional | lines 181, 184 | language | OSR, RC not expanded. |
| D1 | Optional | line 24 | structure | Prose outline in opening ("This entry treats sampling first, then ..."). |

### P1. Description
- **Correction:** "Learn how a sensor voltage becomes numbers: the sampling theorem, aliasing and anti-aliasing filters, quantization error, converter errors and ADC architectures." (162)

### C1. SAR parenthetical
- **Text:** "The result, code 9, represents 1.856 V, the largest step value not exceeding the input. (A converter that rounds to the nearest code, as in Section 3.1, compares the input with thresholds half an LSB lower, ... for this input it would end at code 10.) SAR converters typically offer ..."
- **Correction:** Make the parenthesis its own sentences, keeping the corrected content of the previous review's F2 unchanged.

## Revision log (wave 1)
- Structure: opening outline sentence condensed; SAR parenthetical turned into two plain sentences (content of the previous review's F2 unchanged: thresholds $kq - q/2$, code 10).
- Prose/style: seven H2s to sentence case (incoming fragments `#21-oversampling` and `#32-quantization-error-as-uncertainty` unchanged); "very high rate" → "a high rate, many times the band of interest"; OSR defined (sampling rate divided by twice the signal bandwidth, the standard definition consistent with the $10\log_{10}$ OSR formula); RC expanded.
- Metadata: description 164 characters.
- References: house format, alphabetical; IEEE Std 1241-2010 given publisher and year (IEEE, published 2011-01-14, confirmed at standards.ieee.org/standard/1241-2010.html).
- Cross-references: previous and next entries linked.
- Remaining warnings: none. Suggestion: FSR (expanded in words before the abbreviation as "full-scale range"; lint false positive).
- Flags for independent review: **fact-check**: standards.ieee.org lists IEEE 1241-2010 as Inactive-Reserved (2021) and superseded by IEEE 1241-2023. The text says "defined in IEEE Std 1241" without a year, so it remains true; the reference should probably cite the 2023 edition after its title and content are checked.
- Vietnamese translation affected: yes, wording only (description, opening sentence, SAR sentences, OSR definition, RC expansion).
