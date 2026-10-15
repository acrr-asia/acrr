<!-- audit: {"slug":"calibration-and-multisensor-fusion","type":"article","series":"sensor-systems","priority":"P2","before":{"purpose":4,"structure":2,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":4}} -->
# Audit: Calibration and Multisensor Fusion

- Path: `src/content/blog/calibration-and-multisensor-fusion.mdx` · Route: `/blog/calibration-and-multisensor-fusion` · Type: article · Series `sensor-systems`, entry 7 of 7 · Words: 5703 (prose, from `eos status`; about 8,000 including the four Python listings and their output)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- structure 2: the entry ends with "## 9. Summary" (table only) followed by "## 10. The Series as a Whole", and the References sit under §10, not under the Summary (standards 6.2: the Summary ends with the closing paragraph, which for the last entry closes the series against its objectives; References under the Summary). The closing paragraph does not refer to the series objectives. The second opening paragraph is a prose table of contents ("Its first half is about ...: what ..., how ..., how ..., how ..., and how often. Its second half ...").
- evidence 3: references not in house format; standards titles in headline case rather than their original case; no years on the JCGM entries; not alphabetical.
- language 3: ten title-case H2s; "%" spacing (lines 54, 222, 296); "simply", "clearly", "truly" (lint); §7.4 is a 218-word paragraph with a 77-word sentence (line 454).
- consistency 3: ILAC, OIML expanded only after use in the same sentence (acceptable); "the robotics series" sometimes linked to an entry, sometimes not (line 296, "the robotics series used the same distribution", unlinked).
- publishing 2: description 366 characters, the longest in the series.

## Length

The entry is long (5,703 words of prose, within the 2,500–8,000 range of standards 2.1) because it carries two of the series' subjects: calibration (objective 5, "calibrate") and fusion ("fuse sensors"). Each section serves an objective, and the four code listings are the only place in the series where the uncertainty formulas of entry 1 are applied to data. Splitting it would require a new entry, which is a series-level decision outside this wave. Verdict: the length is earned by content; the only padding is the prose outline of the opening, the separate §10 (which restates the series description) and some wordy sentences. These are trimmed in the revision, not the substance.

## Accuracy

All four Python listings were run with Python 3.13.16 and NumPy 2.5.3; every printed line matches the text exactly. Recomputed in the prose: offset 10.56 g; sensitivity −0.066%; $s/b = 0.132$ g; reference-ratio penalties 3.08 / 11.8 / 0.50%; calibration interval 2.67 years; six-position offset 0.0745 m/s², scale factor 1.0012, gravity spread ±0.27%; fused shift 0.127 °C = 3.2 $u$; tilt rate 25.1 °/s, 0.25° per 10 ms. All correct.

## Priority

P2: should-fix structure and metadata; no accuracy problem.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | §9–§10, lines 516–548 | structure | Summary does not close the series; §10 separates References from the Summary; no reference to the objectives. |
| P1 | Should fix | `:3` | publishing | Description 366 characters. |
| P2 | Should fix | H2 headings | language | Title case, including "Complementary Sensors: Tilt from Accelerometer and Gyroscope". |
| P3 | Should fix | References | evidence | House format, original titles, years, alphabetical order. |
| C1 | Should fix | line 454 | language | 218-word paragraph, 77-word sentence. |
| D2 | Optional | line 18 | structure | Prose table of contents. |
| C2 | Optional | lines 54, 222, 296 | language | Space before %. |
| C3 | Optional | lines 268, 337, 222 | language | "simply", "clearly", "truly". |
| D3 | Optional | line 296 | consistency | "the robotics series" unlinked. |

### D1. Ending
- **Where:** lines 516–537
- **Text:** "## 10. The Series as a Whole / This entry completes the series. Together, the seven entries have followed a measurement ..."
- **Problem:** Standards 6.2 item 6 and the brief: the Summary must end with the closing paragraph; for the last entry it closes the series against its objectives. Here the series close is a separate section after the Summary, and References are under it.
- **Correction:** Remove §10; end §9 Summary with one paragraph that names what the series set out to do (its five objectives) and where each was met, then the pointer to the robotics state-estimation entry; keep `### References` under §9. No link points to `#10-the-series-as-a-whole` (grep of `src/`).

### C1. §7.4 paragraph
- **Text:** "A Kalman filter whose state is the angle alone, with the gyroscope rate as its input and the accelerometer tilt as its measurement (the gyroscope's noise entering as white process noise and the accelerometer's as white measurement noise), settles to a fixed gain ..." (77 words)
- **Correction:** Split into two paragraphs (what a Kalman filter adds; the steady-state equivalence) and split the long sentence, keeping the noise assumptions added for the previous review's F15.

### P1. Description
- **Correction:** "Learn to calibrate sensors with traceable uncertainty and to fuse several: least-squares curves, in-field checks, inverse-variance weighting and complementary filters." (165)

## Revision log (wave 1)
- Structure: §10 "The Series as a Whole" removed; the Summary (§9) now ends with a closing paragraph that names what each entry contributed to the series objectives and leads to the robotics state-estimation entry, followed by a second short paragraph (the common thread); `### References` now sits under §9. No link pointed to `#10-...`. Opening paragraph 2 rewritten to map Sections 1–5 (calibration) and 6–8 (fusion) instead of listing every topic. §7.4 split into two paragraphs, keeping the noise assumptions of the previous review's F15. The Laplace-domain sentence of §7.2 split into three.
- Length: judged earned (see Length above); prose went from 5,703 to 5,766 words because the closing paragraph links each entry; the padding removed was the prose outline and §10.
- Prose/style: ten H2s to sentence case; "%" spacing; "simply", "truly" removed; "flags the inconsistency clearly" → "far above the 1% threshold of 9.21, flags the inconsistency" (9.21 is the text's own χ²(2) 1% quantile); gravity sentence split; JCGM expanded.
- Metadata: description 162 characters.
- References: house format, original titles of the standards (ISO/TS 28037:2010 confirmed on iso.org; ILAC-G24/OIML D 10:2007 confirmed on oiml.org), years added, alphabetical.
- Cross-references: the unlinked "robotics series" at §6.3 now links the state-estimation entry §8; all internal section references (Sections 2, 3, 3.3–3.5, 4.2, 7.3) checked and unchanged.
- Code: all four listings re-run with Python 3.13.16 and NumPy 2.5.3; outputs identical to the text; no code changed.
- Remaining warnings: none. Suggestions: sentence length (19, mostly derivation steps with lists), ILAC/OIML (expanded in the same sentence), TS (part of the standard's designation), MIT (publisher name), PT100 (introduced in entry 1).
- Flags for independent review: series editor to confirm the closing paragraph matches the objectives as worded in the series file; fact-check of standard titles' dash punctuation.
- Vietnamese translation affected: no translation exists.

## Revision log (wave 2 resolution)

Date: 2026-10-15. Resolves `reviews/sensor-systems.md`.

- T2: replaced the claim that one-second averages "should be somewhat quieter" than the 0.1-10 Hz budget with the reviewer's 1/f-aware wording, split for length (line 145). Recomputed: 75.5 nV (1/f, 1/600-0.5 Hz) + 7.1 nV white -> 75.9 nV vs 74.8 nV.
- F1: ISO/TS 28037:2010 -> ISO 28037:2026 in the text (line 202) and references (line 544); verified on iso.org.
- F2: reference updated to ILAC-G24:2022 / OIML D 10:2022 with its new title (line 542); verified in the OIML PDF.
- S1, S7: closing paragraph now says "integrated in one package" and "Building on the uncertainty budget of the first entry, this entry has propagated and combined uncertainties ..." (line 535).
- Code: unchanged; no output re-run needed.
- Vietnamese: no translation exists.
- Lint: 0 errors, 0 warnings; syntax: compiles.
