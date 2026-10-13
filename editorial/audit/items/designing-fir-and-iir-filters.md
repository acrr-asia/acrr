<!-- audit: {"slug":"designing-fir-and-iir-filters","type":"article","series":"digital-signal-processing","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":2,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":4}} -->
# Audit: Designing FIR and IIR Filters

- Path: `src/content/blog/designing-fir-and-iir-filters.mdx` · Route: `/blog/designing-fir-and-iir-filters` · Type: article (series entry) · Series `digital-signal-processing`, entry 4 of 5 · Words: 3973 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4
- structure 4
- accuracy 4: four Python blocks rerun, identical output; biquad, Butterworth order, Kaiser formulas, noise gains and exercises recomputed.
- evidence 3: references real; IEEE 754 entry lacks organization and year in house form; "edition"; Parks–McClellan comma outside quotes; not alphabetical.
- language 3: "can't" (contraction), "very differently", "simply add", long sentences.
- consistency 2: the article mixes "analog" (§4.1–4.5, §3.5) with "analogue" (code comments `:247`, `:249`, prose `:368`), "center" (`:57`, `:144`) with "centre" (`:124`, output `:138`), and "quantization" with the function name `quantise`.
- publishing 2: description 373 characters; five title-case headings.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 373 characters, a list of contents. |
| C1 | Should fix | `:19`, `:49`, `:69`, `:170`, `:301`, `:317` | consistency | Title-case headings ("1. Specifying a Filter", "6. Finite Word Length"). |
| C2 | Should fix | `:124`, `:138`, `:148`, `:204`, `:226`, `:247`, `:249`, `:339–351`, `:368`, `:392` | consistency | Mixed spelling within one article: "centre", "analogue", `quantise`, "towards" next to "center", "analog", "quantization". House variant is American. Two of these are in code and its printed output, so the script must be rerun. |
| C3 | Should fix | `:445` | language | "Why can't an ideal filter be built?": contraction (lint warning). |
| C4 | Should fix | `:458–461` | evidence | House format: "3rd ed.", comma inside quotes, IEEE 754 entry without publisher/year element; order IEEE, Oppenheim, Parks, Proakis. |
| C5 | Should fix | `:81`, `:419` | language | "9 %", "11 %": no space before %. |
| C6 | Optional | `:303` | language | "which behave very differently". |
| C7 | Optional | `:368` | language | "In an FIR filter the errors simply add at the output". |
| C8 | Optional | `:236`, `:370`, `:374` | language | Sentences of 49–51 words. |
| C9 | Optional | `:15` | language | "IIR" flagged by lint at `:15` although it is expanded in the same sentence ("finite and infinite impulse response (FIR and IIR)"); no change needed. |

### P1. Description
- **Correction:** one sentence of 70–165 characters, e.g. turning a specification into FIR and IIR coefficients and what finite word length does to them.

### C1. Headings
- **Correction:** "1. Specifying a filter", "2. FIR filters and linear phase", "3. FIR design by the window method", "4. IIR design by the bilinear transform", "5. Implementation structures", "6. Finite word length". Case only; slugs unchanged; no inbound links.

### C2. Spelling
- **Correction:** "center tap" (code and output), "analog" in the two code comments and `:368`, `quantize` for the function, "toward". Rerun the two affected scripts and paste the real output.

### C3. Contraction
- **Correction:** "Why is an ideal filter impossible to build?"

### C4. References
- **Correction:** `IEEE Std 754-2019, *IEEE Standard for Floating-Point Arithmetic*, IEEE, 2019.` (the standard's designation carries the year; the publisher is the IEEE) and the other format fixes; alphabetical order.

### C5–C8
- As listed; split long sentences where it helps.

### Accuracy spot-checks (no defect found)
- Python blocks: identical output (Python 3.13.16, NumPy 2.5.3).
- Biquad $K = \tan(0.1\pi) = 0.32492$; Kaiser $\beta(50) = 4.534$, $M = 58.5$; Exercise 1 $\beta = 6.755$, $M = 207.3$; Exercise 3 178.6 Hz; noise gains 3.489 (5.43 dB) and 11 920.7 (40.76 dB, 6.77 bits), computed with unrounded coefficients (with the 6-decimal coefficients shown in the text the sum is 11 913.8, because the poles are close to the circle; the text says it used the 5 Hz design, so its number stands).
- Limit-cycle sequence and the dead-band bound $0.5/(1 - 0.9) = 5$ are correct.

## Revision log (wave 1)
- Structure: none needed.
- Prose: §4.4 introduction of the order script split (49 words); §6.3 noise-gain sentence split; §6.4 "Two defenses" sentence rewritten as three sentences, one per defense; "very differently" → "differently"; "simply add" → "add directly".
- Terminology/style: spelling made consistent within the article and with the house variant: "centre" → "center" (code and printed output), "analogue" → "analog" (two code comments, §6.3), `quantise` → `quantize` (function name, three places), "towards" → "toward" (5); "9 %", "11 %" → "9%", "11%"; contraction removed in the summary table ("Why is an ideal filter impossible to build?"); six headings to sentence case (case only; no inbound anchors).
- Code: the window-design script and the quantization script were changed (label and identifiers only) and rerun with Python 3.13.16 and NumPy 2.5.3; the shown output is the real output ("center tap" in the second line; the quantization output is unchanged).
- Metadata: description replaced (373 → 156 characters): "How to turn a filter specification into FIR and IIR coefficients with window and bilinear-transform designs, and what finite word length does to the result."
- References: alphabetical order (IEEE, Oppenheim, Parks, Proakis); "ed."; comma inside the quotation mark; the IEEE 754 entry completed as `IEEE Std 754-2019, *IEEE Standard for Floating-Point Arithmetic*, IEEE, 2019.` (organization and year taken from the standard's own designation).
- Technical corrections: none. Noise gain of the 5 Hz section rechecked: 11 920.7 with unrounded coefficients (40.76 dB); with the six-decimal coefficients printed in the text the sum is 11 913.8, which still rounds to the quoted 40.8 dB and "nearly 7 bits".
- Remaining warnings: none. Suggestions kept: `acronym-expansion` IIR at `:15` (expanded in the same phrase, "finite and infinite impulse response (FIR and IIR)"); sentence-length at `:162` and `:188` (wording set by the previous series review, F7/F12, to state carefully qualified general properties; splitting would separate the claim from its qualification), `:328`, `:374`, `:454` (47–48 words, readable as written).
- Flags for independent review: technical/fact-check: "transposed direct form II is popular in floating-point implementations because its state variables hold partial sums of moderate size" (§5) was recorded as untested by the earlier review; "Most signal-processing hardware offers saturation as an option" (§6.4) is a general claim without a source.
- Vietnamese translation affected: no translation of this article exists.
