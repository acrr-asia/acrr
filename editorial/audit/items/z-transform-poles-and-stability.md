<!-- audit: {"slug":"z-transform-poles-and-stability","type":"article","series":"digital-signal-processing","priority":"P2","before":{"purpose":3,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":3}} -->
# Audit: The z-Transform, Poles and Stability

- Path: `src/content/blog/z-transform-poles-and-stability.mdx` · Route: `/blog/z-transform-poles-and-stability` · Type: article (series entry) · Series `digital-signal-processing`, entry 2 of 5 · Words: 3002 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: the opening states what the entry builds on and covers, but not the language versions its two scripts assume (they are stated only in entry 1).
- structure 4
- accuracy 4: both Python blocks rerun, identical output; partial fractions, pole mapping, notch width and exercise answers recomputed.
- evidence 3: references not in house format and not in alphabetical order.
- language 3: "counter-clockwise" (American: "counterclockwise"); three sentences of 47–51 words.
- consistency 3: title-case headings.
- publishing 2: description 325 characters; title-case headings.

Total before: 22 of 28.

## Priority

P2: should-fix problems a reader would notice (metadata, headings), no accuracy defect.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 325 characters, a list of sections. |
| C1 | Should fix | `:21`, `:74`, `:128`, `:183`, `:232` | consistency | Title-case section headings ("2. Transfer Functions", "5. Frequency Response from Poles and Zeros"). |
| C2 | Should fix | `:390–392` | evidence | "3rd edition"/"4th edition" instead of "ed."; list not alphabetical (Jury should come first). |
| D1 | Should fix | `:19` | purpose | Opening does not name the Python/NumPy versions used by the two scripts. |
| C3 | Should fix | `:242` | language | "counter-clockwise": American form is "counterclockwise". |
| C4 | Optional | `:15` | language | 51-word opening sentence. |
| C5 | Optional | `:324` | language | 47-word sentence on settling time inside a long paragraph. |
| C6 | Optional | `:386` | language | 49-word closing sentence; DFT/FFT not expanded in this article before use (expanded in the linked title context only). |

### P1. Description
- **Text:** "From difference equations to transfer functions: the z-transform and its region of convergence, poles and zeros, ... with a notch filter as the worked example."
- **Correction:** One sentence of 70–165 characters saying what the reader learns.

### C1. Headings
- **Correction:** "1. The z-transform", "2. Transfer functions", "3. The inverse transform by partial fractions", "4. Poles and stability", "5. Frequency response from poles and zeros". Case-only change: the internal anchors used at `:49`, `:99`, `:242` keep their slugs.

### C2. References
- **Correction:** Order Jury, Oppenheim and Schafer, Proakis and Manolakis; "3rd ed.", "4th ed.".

### D1. Versions
- **Where:** `:19`
- **Correction:** add "code uses Python 3 and NumPy, run with the versions stated in the first entry".

### C3–C6
- C3 `:242` "walks counter-clockwise" → "counterclockwise".
- C4 `:15` split into two sentences.
- C5 `:324` split the settling-time sentence.
- C6 `:386` split; expand DFT and FFT ("discrete Fourier transform (DFT)").

### Accuracy spot-checks (no defect found)
- Python blocks: identical output (Python 3.13.16, NumPy 2.5.3).
- $A_1 = -5/3$, $A_2 = 8/3$, $H(1) = 10$; $e^{-0.01/0.0949} = 0.900$; $e^{-0.025} = 0.975$; notch $|a_1| = 1.864$, $a_2 = 0.9604$, width estimate 6.37 Hz vs measured 6.19 Hz; $-1/\ln 0.98 = 49.5$; Exercise 1 peak $2/1.81 = 1.105$ at $z = j$; Exercise 5 $r = 0.9937$, about 159 samples.
- The stability statement "Apart from a finite number of initial samples (present when the numerator's degree in $z^{-1}$ is at least the denominator's)" is correct ($M \ge N$ gives a polynomial part of degree $M - N$).

## Revision log (wave 1)
- Structure: none needed.
- Prose: the 51-word opening sentence split; the settling-time sentence in §5.3 split; the closing paragraph split and now names the discrete Fourier transform before the link sentence ends.
- Purpose: the opening now states that the two scripts use Python 3 and NumPy at the versions given in the first entry (D1).
- Terminology/style: "counter-clockwise" → "counterclockwise"; five headings to sentence case (case only; the in-page anchors `#22-poles-and-zeros`, `#3-the-inverse-transform-by-partial-fractions` and `#5-frequency-response-from-poles-and-zeros` are unchanged).
- Metadata: description replaced (325 → 146 characters): "How the z-transform turns difference equations into transfer functions, and how poles and zeros decide stability and shape the frequency response."
- References: reordered (Jury, Oppenheim and Schafer, Proakis and Manolakis); "ed.".
- Technical corrections: none needed. Both Python blocks rerun: identical output.
- Remaining warnings: none. Suggestions kept: `acronym-expansion` DFT/FFT at `:386`, which occur in the linked title "Spectra: The DFT and the FFT"; the same sentence then names the discrete Fourier transform and the fast Fourier transform in full.
- Flags for independent review: none.
- Vietnamese translation affected: no translation of this article exists.

## Independent review (wave 2)
- Report: `reviews/digital-signal-processing.md` (reviewed commit 49941d2, 2026-10-14).
- Fact-check: pass (Jury, Wiley, 1964 confirmed in a library catalogue).
- Technical: pass. Findings: S3 (optional: :264 "recursive filters" → "causal IIR filters").
- Code: both blocks rerun, outputs identical; all exercise answers recomputed.
- Not verified: Oppenheim and Schafer and Proakis and Manolakis editions not re-checked in this pass.

## Revision log (wave 2 resolution)
- Date: 2026-10-15. Report: `reviews/digital-signal-processing.md`, section Resolution.
- Changes: S3 applied at :264 ("recursive filters" to "causal IIR filters"). No code changed.
- `eos lint`: 0 errors; the only warning in the series is entry 1's justified `heading-numbering`. `eos syntax`: pass.
