# Series audit: Digital Signal Processing for Engineers

- Series: `digital-signal-processing` · 5 entries, status published, no planned entries · Overview `src/content/series/digital-signal-processing.md`
- Audited at commit `e21dcc8`, 2026-10-13 (wave 1, content auditor). Previous series review: `reviews/digital-signal-processing.md` (resolved; its corrections F1–F16 are all present and were not undone).

## Structural consistency across entries

| Entry | Opening (builds on / covers / versions) | Numbered sections | Exercises with answers | Summary table + lead-on | References | Notes |
|---|---|---|---|---|---|---|
| 1 Signals and systems | Yes / yes / Python 3.13, NumPy 2.5 | 1–8 | §7 (5) | §8, leads to entry 2 | `### References` (3) | Conventions block under an orphan h3 (lint error) |
| 2 z-transform | Yes / yes / no versions | 1–7 | §6 (5) | §7, leads to entry 3 | `### References` (3) | |
| 3 DFT and FFT | Yes / yes / Python 3, NumPy | 1–7 | §6 (5) | §7, leads to entry 4 | `### References` (5) | |
| 4 Filters | Yes / yes / Python 3, NumPy | 1–8 | §7 (5) | §8, leads to entry 5 | `### References` (4) | |
| 5 Digital control | Yes / yes / Python 3, NumPy | 1–8 | §7 (5) | §8, closes the series | `### References` (4) | |

The five entries share one structure: unheaded opening paragraphs that link back, numbered sections with numbered subsections, five exercises with answers in `<details>`, a numbered Summary with a question/answer table, a closing paragraph that names the next entry, and an unnumbered `### References` under the Summary. Summary is numbered in every entry, which is consistent within the series (standards 5.4 allows either).

## Systemic problems (all entries)

1. **House style adopted after publication.** All headings are title case; the previous review moved the series to British spelling ("analogue", "quantisation", "centre"), and some American forms remained ("analog" in entry 4 §3.5–4.5), so entry 4 now mixes both. Standards 5.1 adopt American spelling. Every entry needs sentence-case headings and American spelling.
2. **Descriptions are section lists of 271–373 characters** (overview 211). None says in one sentence what the reader learns.
3. **Reference format.** "3rd edition" instead of "3rd ed."; journal-article commas outside the closing quotation mark; three lists not in alphabetical order; the IEEE 754 entry lacks the organization/year element.
4. **"95 %", "2 %"**: a space before the percent sign in entries 1, 4 and 5.
5. **Versions.** Entry 1 names Python 3.13 and NumPy 2.5; entries 3–5 say "Python 3 and NumPy"; entry 2 says nothing although it has two scripts.

## Notation and terminology

Consistent: $\omega$ (rad/sample), $T_s$/$f_s$ ($T$ in entry 5, stated), $a_0 = 1$ sign convention, $H(e^{j\omega})$, "pole", "zero", "order", "section", "group delay", "linear phase", "coherent gain", "noise gain". Abbreviations are expanded at first use in each entry (LTI, BIBO, FIR, IIR, DTFT, DFT, FFT, ADC, DAC, ZOH, PI), with three small gaps listed in the item audits (entry 2 closing paragraph DFT/FFT; entry 3 heading 1.1 DTFT).

## Overlap and gaps

- No redundant explanations: later entries refer back (entry 3 to entry 1's convolution example for circular convolution; entry 4 to entry 3's windows; entry 5 to entry 4's bilinear transform as Tustin's method) instead of repeating.
- The moving average (entry 1 §6.2) and the notch filter (entry 2 §5.3) treat the same 50 Hz problem deliberately, and entry 2 says why its method is better.
- No gaps against the objectives (see below).

## Overview page against standards 6.5

- Covers: what the series treats; reader and prerequisites; Python 3 with NumPy.
- Missing: sequence rationale (why this order), how the entries connect, the shared conventions (entry 1's table), and a named/linked prerequisite ("the sensor series" is not linked). British "analyses". Description 211 characters.
- Objectives: five, each covered: (1) entry 1 §1–5; (2) entry 2 §1–5; (3) entry 3 §1–5; (4) entry 4 §1–6; (5) entry 5 §1–5. No promise is unfulfilled.

## Cross-references

- Every "first/second/third/fourth/fifth entry", "next entry" and "Section N" reference in the five entries was checked against its target: all correct (the previous review fixed F3, F4, F5, F8).
- Internal fragments in scope: `#conventions-used-throughout-the-series` (from entries 2–5; target is the orphan h3 in entry 1), `#4-impulse-response-and-convolution`, `#6-response-to-sinusoids-a-first-look-at-frequency-response`, `#22-poles-and-zeros`, `#3-the-inverse-transform-by-partial-fractions`, `#5-frequency-response-from-poles-and-zeros`, `#42-phase-lag-at-the-crossover-frequency`. Sentence-casing keeps all these slugs.
- Outbound fragments to other series: `sampling-quantization-and-data-conversion#21-oversampling` and `#32-quantization-error-as-uncertainty` (entry 4), `stability-and-eigenvalues#stability-in-discrete-time` and `state-feedback-controller-design#the-controller-runs-in-continuous-time` (entry 5). If the editors of the sensor-systems or control series renumber or reword those headings, these links break.
- Inbound: `sampling-quantization-and-data-conversion.mdx:75` links `/series/digital-signal-processing` (no fragment). No other file outside the scope links to these entries.

## Code

All 13 Python blocks were extracted and run with `python3 -I` (Python 3.13.16, NumPy 2.5.3); every printed output matches the article byte for byte. SciPy is not installed, and no block uses it.
