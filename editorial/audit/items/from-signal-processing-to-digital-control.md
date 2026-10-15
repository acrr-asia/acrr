<!-- audit: {"slug":"from-signal-processing-to-digital-control","type":"article","series":"digital-signal-processing","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":4}} -->
# Audit: From Signal Processing to Digital Control

- Path: `src/content/blog/from-signal-processing-to-digital-control.mdx` · Route: `/blog/from-signal-processing-to-digital-control` · Type: article (series entry) · Series `digital-signal-processing`, entry 5 of 5 · Words: 3139 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4
- structure 4
- accuracy 4: both Python blocks rerun, identical output; coth table, emulation maps, damping ratio, phase-lag table, FIR delay and exercises recomputed.
- evidence 3: four real references, "3rd edition" format, not alphabetical.
- language 3: one sentence of 91 words (`:267`); British "analogue", "destabilise(s)", "towards"; "really".
- consistency 3: title-case headings; spelling.
- publishing 2: description 364 characters; title-case headings.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 364 characters, a list of contents. |
| C1 | Should fix | `:19`, `:61`, `:137`, `:218`, `:269` | consistency | Title-case headings. |
| C2 | Should fix | `:23`, `:135`, `:222`, `:247`, `:263`, `:334` | language | "analogue-to-digital", "digital-to-analogue", "destabilises", "destabilise", "towards": house variant is American. |
| C3 | Should fix | `:267` | language | 91-word sentence: "A slower rate is possible when the controller is designed directly in discrete time, ... even though it was poor." |
| C4 | Should fix | `:344–347`, `:175`, `:201`, `:207–212`, `:335` | evidence / language | References: "3rd edition" → "3rd ed.", alphabetical order (Åström and Murray, Åström and Wittenmark, Franklin, Oppenheim); "2 %", "11.7 %", "31.0 %", "2.0 %": no space before %. |
| C5 | Optional | `:71` | language | "because the input really is constant between them". |
| C6 | Optional | `:222` | language | "The second section of this entry handled the hold exactly" → cite "Section 2". |
| C7 | Optional | `:135`, `:149`, `:212` | language | Sentences of 48–51 words. |
| C8 | Optional | `:340` | structure | Closing paragraph summarizes the series well; it could name the objective it closes (treating a control loop as a signal-processing system), but it already does so in substance. No change needed. |

### P1. Description
- **Correction:** one sentence, 70–165 characters, e.g. how a digital control loop behaves as a signal-processing system, from the zero-order-hold model to the choice of sampling rate.

### C1. Headings
- **Correction:** "1. The sampled-data loop", "2. The plant seen by the computer", "3. Discretizing a controller", "4. The delays in the loop", "6. A control loop is a signal-processing system". The internal anchor `#42-phase-lag-at-the-crossover-frequency` is unaffected.

### C3. 91-word sentence
- **Correction:** split into: slower rates are possible with direct discrete design; the reason (the zero-order-hold model accounts for the hold exactly); the evidence (the proportional example at $T = 0.5$ s was predicted exactly though it was poor).

### C4. References and percent signs
- As listed. The PI script prints "2 % settling": change the label to "2% settling" and rerun.

### Accuracy spot-checks (no defect found)
- Python blocks: identical output (Python 3.13.16, NumPy 2.5.3).
- $\coth(T/2)$: 200.0, 20.02, 10.03, 4.08, 2.16; emulation of $sT = -2.5$: $-1.5$, $0.286$, $-0.111$, $0.082$; $\zeta = 5/(2\sqrt{10}) = 0.79$; PI zero 0.882; FIR delay at 2 Hz $360° \times 2 \times 0.033 = 23.8°$; Exercise 1 $20.07$; Exercise 2 $9.51$; Exercise 3 1.8 kHz and 5.4 kHz.

## Revision log (wave 1)
- Structure: none needed.
- Prose: the 91-word sentence of §5 split into three sentences and the following link sentence given a subject ("The entry [Designing a State-Feedback Controller] gives ..."); §2.1 higher-order sentence split; §2.2 alternating-response sentence split; §3.3 result paragraph split; "really" removed; "The second section of this entry" → "Section 2"; closing paragraph's 54-word sentence rewritten as a parallel list without changing what it says.
- Terminology/style: "analogue" → "analog" (2), "destabilises/destabilise" → "destabilizes/destabilize", "towards" → "toward" (3); "2 %", "11.7 %", "31.0 %", "2.0 %" → no space; five headings to sentence case (case only; `#42-phase-lag-at-the-crossover-frequency` unaffected).
- Code: the PI script's printed label changed from "2 % settling" to "2% settling"; rerun with Python 3.13.16 and NumPy 2.5.3, output pasted (numbers unchanged).
- Metadata: description replaced (364 → 163 characters): "How a digital control loop works as a signal-processing system: zero-order-hold plant models, discretized controllers, loop delays and the choice of sampling rate."
- References: alphabetical order (Åström and Murray, Åström and Wittenmark, Franklin, Oppenheim); "ed.".
- Technical corrections: none.
- Remaining warnings: none. Suggestions kept: sentence-length at `:15` (46 words, the list of the four earlier entries) and `:149` (48 words, the Euler comparison, readable as written).
- Flags for independent review: none new.
- Vietnamese translation affected: no translation of this article exists.

## Independent review (wave 2)
- Report: `reviews/digital-signal-processing.md` (reviewed commit 49941d2, 2026-10-14).
- Fact-check: pass (cross-site attributions to Feedback and System Behavior, Stability and Eigenvalues, Designing a State-Feedback Controller and the numerical integration notes checked).
- Technical: pass. Findings: S2 (should fix: :249 heading "5. Choosing the Sampling Rate" still title case), S6 (optional: version wording :17), T3 (optional: :232 qualify the crossover-phase rule).
- Code: both blocks rerun, outputs identical; coth table, emulation images and exercises recomputed.
- Not verified: "45° to 60°, a common design target" (:243); Åström–Wittenmark, Franklin–Powell–Workman, Åström–Murray editions not re-checked in this pass.

## Revision log (wave 2 resolution)
- Date: 2026-10-15. Report: `reviews/digital-signal-processing.md`, section Resolution.
- Changes: S2 fixed at :249 (heading in sentence case; slug unchanged). T3 applied at :232 (rule qualified to loops whose gain crosses 1 once; sentence split). S6 applied at :17 (separate sentence). No code changed.
- `eos lint`: 0 errors; the only warning in the series is entry 1's justified `heading-numbering`. `eos syntax`: pass.
