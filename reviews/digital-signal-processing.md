# Series review: Digital Signal Processing for Engineers

- Series: `digital-signal-processing` (5 articles, status published, 0 planned entries)
- Reviewed commit: db16bd5 (reviewed on branch `review/digital-signal-processing` after merging `master` 047af87, which adds the last two Foundations of Control Systems entries that this series links to; the merge does not touch this series' files)
- Date: 2026-10-13
- Content hash: sha256:7780ea2f2e1e0c22eb612bccf5174e5b841549ed5e90c0a28e1ce2f954885120

## Summary

The series is technically strong. All 13 Python blocks were rerun with Python 3.13.16 and NumPy 2.5.3, and each printed output matches the article byte for byte. Every other worked number was also recomputed with numpy: the window tables of entries 3 and 4, the Kaiser formulas, the Butterworth biquad, the noise gains, the leakage levels, the stability limits and every exercise answer. All are correct. All thirteen references are real works, and their authors, titles, editions, publishers, years and volume and page details are correct. The build, the KaTeX output and the link check are clean.

The problems are small. One statement in entry 1 is wrong: it says that at $a = 1$ the smoother "degenerates into a scaled accumulator" and that its sum diverges, but its gain $1 - a$ is then zero. The should-fix findings are:
- mixed British and American spelling across the series ("analyse" and "normalised" next to "quantization" and "analog");
- a link whose text says "series" but which points to one article;
- a mis-summary of the moving-average trick in entry 2;
- a promise in entry 2 that entry 4 explains why IIR filters cannot have linear phase, which entry 4 never does;
- an exercise that asks for the "nearest" power of 2 when the answer gives the next one up;
- an uncomputed claim that an elliptic design "would need far fewer sections";
- a wrong table-column reference and an ambiguous delay sentence in entry 5.

The series is ready once F1 is fixed. All findings have now been fixed (see Resolution).

Findings: 1 blocking, 8 should fix, 7 optional.

## Resolution

Corrections were applied on 2026-10-13 on branch `review/digital-signal-processing`, in one commit together with this report. Line numbers in the findings refer to the reviewed commit db16bd5, not to the corrected files. None of the five articles has a Vietnamese translation. The only translated file touched is `src/content/series/vi/digital-signal-processing.md`, which received the new objective of F16.

All 16 findings were applied:
- **F1, F3, F4, F6, F8, F9, F11–F13:** applied as recommended. F13 was worded "such as the running example" because §2.2 comes before the example design.
- **F2:** every "analog", "quantization" and "quantize(d)" in the five articles became "analogue", "quantisation" and "quantise(d)", including the heading "6.2 Coefficient quantisation" (no link targets its anchor) and the `quantise` function in entry 4's script. The titles "Sampling, Quantization and Data Conversion" and "Feedback and System Behavior" in link text, and their URLs and anchors, are unchanged because they name other articles.
- **F5:** the explanation was added in entry 4 §2.1, as two shorter sentences than recommended. Exactly linear phase requires a real impulse response that is symmetric or antisymmetric about some centre. A response that continues forever after $n = 0$ can be mirrored only if it also extends to negative $n$.
- **F7:** applied as recommended.
- **F10:** applied. The explanation of the exact coefficients says what they do, after a check: with $25/46$ and $21/46$ the transform is −76 dB at 2.5 bins, so they put a zero in the middle of the first side lobe. That replaces "would cancel it exactly". The note on Harris's 1.78 dB follows the window table.
- **F14:** applied as recommended.
- **F15:** §2.1 now gives the higher-order equivalent $x[n+1] = A_d\,x[n] + B_d\,u[n]$, $A_d = e^{AT}$, written with $n$ because $k$ is the proportional gain in this entry. It links [Stability and Eigenvalues](/blog/stability-and-eigenvalues#stability-in-discrete-time), noting that it uses $k$ as the sample index. Deviation from the recommendation: §3.1 links the [Foundations of Control Systems](/series/foundations-of-control-systems) series instead of the state-feedback entry. A static state-feedback gain $u = -Kx$ is not a transfer function $C(s)$ to be emulated, so citing it there was inaccurate (second pass). [Designing a State-Feedback Controller](/blog/state-feedback-controller-design#the-controller-runs-in-continuous-time) is linked instead at the end of §5. That is where its advice matches this entry: when the sampling period is not small compared with the fastest closed-loop time constant, place the poles on the discrete-time model.
- **F16:** the objective was added to the series file and, in Vietnamese, to `src/content/series/vi/digital-signal-processing.md`. That translation follows the glossary of `docs/translation-vi.md` ("đối tượng điều khiển" for plant) and uses "thời gian trễ (delay)", because the glossary assigns "độ trễ" to hysteresis.

Second pass. After the corrections, all five articles were reread for defects introduced by the corrections and for anything missed. Three defects were found and fixed:
- the first wording of F1 used "pole", a term that entry 1 does not introduce (it is defined in entry 2), and said "whatever its input gain" next to the zero-gain special case; it now reads "A feedback coefficient with $|a| \ge 1$ makes the recursion unstable for any nonzero input gain";
- the first wording of F15 in §3.1 cited state-feedback pole placement as an example of emulating $C(s)$ (see the F15 deviation above);
- the first wording of F10 said the exact coefficients "cancel" the side lobe; it now says they put a zero in its middle.

A further full pass found no blocking or should-fix issues.

Re-run results after the corrections:
- All 13 Python blocks were rerun with Python 3.13.16 and NumPy 2.5.3; every output still matches the article byte for byte.
- `npm run build:local`: 0 errors, 0 warnings, 83 pages indexed.
- `npm run check:links`: 224 pages and 6438 internal references checked; all resolve, including the new anchors `#stability-in-discrete-time` and `#the-controller-runs-in-continuous-time`.
- Dist checks: Mermaid min-widths unchanged (393–473 px), no `katex-error`, and no text glued to inline elements.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Describe discrete-time signals and linear time-invariant systems by difference equations, impulse responses and convolution. | Entry 1 §1–5 | Met: sequences, discrete-time frequency, the five system properties, difference equations, impulse response, the convolution sum with its derivation, and stability from $\sum\lvert h[n]\rvert$. |
| Use the z-transform to analyse stability and frequency response. | Entry 2 §1–5 | Met: ROC, transforms table, transfer function, partial fractions, the pole condition with the stability triangle, the $s$-to-$z$ map, and the geometric reading of the frequency response, with a notch-filter design. |
| Compute and interpret spectra with the DFT and FFT, including leakage and windowing. | Entry 3 §1–5 | Met: the DFT definition and conventions, bins, conjugate symmetry, zero padding, circular convolution, the radix-2 FFT with code, leakage, the window table, a dynamic-range example, amplitude and noise scaling. |
| Design FIR and IIR filters to a specification and implement them within hardware limits. | Entry 4 §1–6 | Met: tolerance scheme, linear phase, the window and Kaiser methods, decimation, the bilinear transform with prewarping, Butterworth order, structures, coefficient quantisation, round-off noise, overflow and limit cycles. |
| (Not an objective) The step from signal processing to digital control promised in the description | Entry 5 | Covered, but the series file has no objective for it (F16). |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `src/content/blog/signals-and-systems-in-discrete-time.mdx` | §5 (line 299) | Technical accuracy | At $a = 1$ the smoother's gain $1 - a$ is zero, so it is not "a scaled accumulator", and its sum does not diverge. |
| F2 | Should fix | All five articles | many lines | Terminology | British and American spellings are mixed: "analyse", "normalised", "centred", "discretising" next to "quantization", "quantize(d)" and "analog". |
| F3 | Should fix | `src/content/blog/z-transform-poles-and-stability.mdx` | §4.3 (line 212) | Cross-article references | Link text "control systems series" points to a single article. |
| F4 | Should fix | `src/content/blog/z-transform-poles-and-stability.mdx` | §5.3 (line 268) | Factual consistency | "needed $f_s$ to be a multiple of 150 Hz" misstates entry 1: the three-point average needs $f_s$ = 150 Hz exactly. |
| F5 | Should fix | `src/content/blog/z-transform-poles-and-stability.mdx` → `designing-fir-and-iir-filters.mdx` | line 264 → §2.1 (line 53) | Cross-article references | Promise "the fourth entry shows ... why recursive filters cannot [have linear phase]" is not fulfilled; entry 4 only asserts it. |
| F6 | Should fix | `src/content/blog/dft-and-fft.mdx` | Exercise 1 (lines 315, 320) | Technical accuracy | Asks for the "nearest power of 2" to 48 000, which is 32 768, but the answer gives 65 536. |
| F7 | Should fix | `src/content/blog/designing-fir-and-iir-filters.mdx` | §4.5 (line 299), §4.1 (line 188) | Fit with site rules | "an elliptic prototype would need far fewer sections" reads as a result but was not computed. |
| F8 | Should fix | `src/content/blog/from-signal-processing-to-digital-control.mdx` | §3.4 (line 216) | Cross-article references | "the third column of the table" should be the last column (the image of a stable pole). |
| F9 | Should fix | `src/content/blog/from-signal-processing-to-digital-control.mdx` | §4.2 (line 243) | Technical accuracy | "adds $T$ to the delay, three times the hold's own lag": $T$ is twice the hold's lag; the total is three times. |
| F10 | Optional | `src/content/blog/dft-and-fft.mdx` | §5.1 (lines 242–251) | Technical accuracy | Hamming "cancel[s] the first side lobe" only nearly; the 1.75 dB scalloping loss differs from the 1.78 dB of Harris's table without explanation. |
| F11 | Optional | `src/content/blog/dft-and-fft.mdx` | §3.1 (line 111) | Technical accuracy | The 1965 Cooley–Tukey paper gives a general factorisation; radix-2 is its best-known case, not its only content. |
| F12 | Optional | `src/content/blog/designing-fir-and-iir-filters.mdx` | §3.4 (line 162) | Writing quality | The Parks–McClellan coefficient claim can be stated as the general property it is. |
| F13 | Optional | `src/content/blog/designing-fir-and-iir-filters.mdx` | §2.2 (line 63) | Technical accuracy | "which happens only in the stopband" holds for low-pass designs such as this one, not for every symmetric filter. |
| F14 | Optional | `src/content/blog/from-signal-processing-to-digital-control.mdx` | §1.3 (line 59), §4.2 (line 243) | Technical accuracy | The feedback moves the PI loop's poles inside the circle only for suitable gains; "a typical phase margin" can be stated as a design target. |
| F15 | Optional | `src/content/blog/from-signal-processing-to-digital-control.mdx` | §2.1 (line 77), §3.1 (line 141) | Cross-article references | The Foundations entries now on master derive the discrete-time state model and discuss sampled state feedback; entry 5 does not link them. |
| F16 | Optional | `src/content/series/digital-signal-processing.md` | objectives (lines 6–10) | Completeness | No objective covers entry 5, although the description and body promise it. |

### F1. The exponential smoother at $a = 1$
- **Where:** `src/content/blog/signals-and-systems-in-discrete-time.mdx:299`, section "5. Reading Properties from the Impulse Response"
- **Text:** "With $|a| \ge 1$ the geometric series diverges and the system is unstable; with $a = 1$ the smoother degenerates into a scaled accumulator."
- **Problem:** The smoother is $y[n] = a\,y[n-1] + (1 - a)\,x[n]$ with $h[n] = (1 - a)a^n u[n]$. At $a = 1$ the input gain $1 - a$ is zero, so $h[n] = 0$, $S = 0$, and the output stays at zero from rest. The sum does not diverge, and the system is not an accumulator in any useful sense (it is one scaled by zero). The statement is right for $|a| > 1$ and for $a = -1$, where $|h[n]| = 2$ for all $n \ge 0$.
- **Recommended correction:** "A pole with $|a| \ge 1$ makes the system unstable whatever its input gain: with $|a| > 1$ the terms grow, and with $|a| = 1$ they never decay, so the sum diverges. (At $a = 1$ the smoother's own gain $1 - a$ is zero and the output stays at zero; with any other input gain $b_0 \ne 0$, the recursion $y[n] = y[n-1] + b_0\,x[n]$ is a scaled accumulator.)"

### F2. Mixed British and American spelling
- **Where:** for example `src/content/blog/signals-and-systems-in-discrete-time.mdx:15` ("analog-to-digital converter") and `:48` ("quantized"); `designing-fir-and-iir-filters.mdx:166, 176, 182, 192, 198, 204, 208, 226, 247, 249, 299, 414` ("analog"), `:326` ("Coefficient quantization"), `:339–351` (`quantize`), `:368` ("quantization noise"); `from-signal-processing-to-digital-control.mdx:23, 34, 216, 247, 264`.
- **Text:** "analog" (25 times), "quantization" (9), "quantize"/"quantized" (4), against "analyse", "analysed", "normalised", "normalisation", "centred", "discretising", "discretisation", "generalises", "minimises", "optimised", "destabilises", "favour", "behaviour", "artefact", "defences".
- **Problem:** The series file uses British spelling ("analyse", "analyses"), as do most words in the articles. The -ize and "analog" forms are inconsistent with it, contrary to the terminology dimension.
- **Recommended correction:** Use British spelling throughout the series: "analogue", "quantisation", "quantise(d)" (also the `quantize` function in entry 4's script, which does not change the output). Keep the exact titles of other articles in link text ("Sampling, Quantization and Data Conversion", "Feedback and System Behavior") and their URLs and anchors unchanged, because link text must match the target.

### F3. Link text "control systems series" points to one article
- **Where:** `src/content/blog/z-transform-poles-and-stability.mdx:212`, section "4.3 The mapping from the s-plane"
- **Text:** "The Laplace-transform description of continuous systems, used in the [control systems series](/blog/introduction-to-control-systems), ..."
- **Problem:** The text names a series, but the link goes to the first article of that series. The series is called "Foundations of Control Systems" and has its own page.
- **Recommended correction:** "..., used in the [Foundations of Control Systems](/series/foundations-of-control-systems) series and introduced in its [first entry](/blog/introduction-to-control-systems), ..."

### F4. The moving-average trick misstated
- **Where:** `src/content/blog/z-transform-poles-and-stability.mdx:268`, section "5.3 Worked example: a notch filter for mains interference"
- **Text:** "The moving-average trick of the first entry needed $f_s$ to be a multiple of 150 Hz and attenuated the signal band noticeably"
- **Problem:** The three-point average has its zeros at $\omega = \pm 2\pi/3$, that is, at $f_s/3$. It removes 50 Hz only when $f_s = 150$ Hz. At $f_s = 300$ Hz, a multiple of 150 Hz, its zero is at 100 Hz and 50 Hz passes with gain $|1 + 2\cos(\pi/3)|/3 = 0.67$. Entry 1 says the trick needs "$f_s$ as a multiple of the interference frequency" (with an average of matching length).
- **Recommended correction:** "The moving-average trick of the first entry needed $f_s$ to be exactly three times the interference frequency (a longer average needs another fixed multiple) and attenuated the signal band noticeably"

### F5. Unfulfilled promise about linear phase in IIR filters
- **Where:** `src/content/blog/z-transform-poles-and-stability.mdx:264` (promise); `src/content/blog/designing-fir-and-iir-filters.mdx:53` (where it should be fulfilled)
- **Text:** entry 2: "The fourth entry shows how FIR filters achieve linear phase exactly and why recursive filters cannot." Entry 4: "And it can have exactly linear phase, which no causal IIR filter can."
- **Problem:** Entry 4 shows how symmetric FIR filters get linear phase (§2.2), but only asserts the IIR half.
- **Recommended correction:** In entry 4 §2.1, replace the sentence with: "And it can have exactly linear phase, which no causal IIR filter can: as Section 2.2 shows, a real impulse response has linear phase when it is symmetric (or antisymmetric) about its centre, and an impulse response that continues forever after $n = 0$ has no centre about which it could be mirrored without extending to negative $n$, that is, without becoming non-causal."

### F6. "Nearest power of 2" in DFT Exercise 1
- **Where:** `src/content/blog/dft-and-fft.mdx:315` and `:320`, section "6. Exercises"
- **Text:** "How many samples are needed for bins 1 Hz apart, and what is the nearest power of 2?" / "The nearest power of 2 above is $2^{16} = 65\,536$"
- **Problem:** The nearest power of 2 to 48 000 is $2^{15} = 32\,768$ (15 232 away, against 17 536 for $2^{16}$). Its bins would be 1.46 Hz apart, which does not meet the requirement. The exercise means the next power of 2 above.
- **Recommended correction:** Question: "... and what is the smallest power of 2 that is at least that long?" Answer: "The smallest power of 2 at least that long is $2^{16} = 65\,536$, ..."

### F7. Uncomputed claims about elliptic and Chebyshev orders
- **Where:** `src/content/blog/designing-fir-and-iir-filters.mdx:299` (and `:188`), sections "4.5 FIR or IIR?" and "4.1 Why IIR, and where to start"
- **Text:** "A narrow transition band with a tight passband tolerance is the case where Butterworth filters are least efficient; an elliptic prototype would need far fewer sections." Also "Chebyshev and elliptic prototypes ... reach a given specification with a lower order".
- **Problem:** No elliptic or Chebyshev design is computed in the series. "Far fewer sections" for this specification therefore reads as a measured result that the text does not support. The general property (equiripple prototypes need a lower order than a Butterworth prototype for the same specification) is well established and can be stated as such.
- **Recommended correction:** Line 299: "... least efficient; a Chebyshev or, especially, an elliptic prototype generally needs a much lower order for such a specification (this entry does not design one)." Line 188: "... in exchange for a steeper transition, and as a general property need a lower order than a Butterworth filter for the same specification; the bilinear-transform procedure below applies to them unchanged."

### F8. Wrong table column cited
- **Where:** `src/content/blog/from-signal-processing-to-digital-control.mdx:216`, section "3.4 Derivative action needs a filter"
- **Text:** "The discretisation method then matters for a reason the third column of the table already hints at."
- **Problem:** The table of §3.1 has four columns: method, integration rule, substitution for $s$, image of a stable continuous pole. The hint (where a stable pole lands) is in the fourth, last column.
- **Recommended correction:** "... for a reason the last column of the table already hints at: a fast pole, with $|s|T$ large, lands near $z = 0$ under backward Euler but near $z = -1$ under Tustin."

### F9. Computation delay compared with the hold's lag
- **Where:** `src/content/blog/from-signal-processing-to-digital-control.mdx:243`, section "4.2 Phase lag at the crossover frequency"
- **Text:** "The second row assumes the command is written at the next tick (Section 1.2), which adds $T$ to the delay, three times the hold's own lag."
- **Problem:** The hold's delay is $T/2$, so the added $T$ is twice the hold's lag. The table row (108°, 54°, ...) is the total, $3T/2$, which is three times the hold's lag. The sentence reads as if $T$ itself were three times.
- **Recommended correction:** "The last row assumes the command is written at the next tick (Section 1.2), which adds $T$ to the hold's $T/2$ and so triples the lag." (The table's rows are a header row and two data rows, so "last row" is also clearer than "second row".)

### F10. Hamming window: side-lobe cancellation and scalloping loss
- **Where:** `src/content/blog/dft-and-fft.mdx:242` and `:244–251`
- **Text:** "The **Hamming window**, $0.54 - 0.46\cos(2\pi n/N)$, adjusts the coefficients to cancel the first side lobe"; table row "Hamming | 2 | −42.7 dB | 1.75 dB | ...".
- **Problem:** The coefficients that place a zero on the first side lobe are $25/46$ and $21/46$; 0.54 and 0.46 are their rounded values, which nearly cancel it. Recomputed here: the rounded coefficients give a 1.751 dB scalloping loss and the exact ones 1.778 dB. Harris (1978), cited by the entry, lists 1.78 dB. The table's stated method ("computed numerically for $N = 1024$ from the periodic forms above") is correct but does not explain the difference a reader will see.
- **Recommended correction:** "adjusts the coefficients to nearly cancel the first side lobe ($25/46$ and $21/46$ would cancel it exactly; 0.54 and 0.46 are their rounded values)". After the table: "Published tables can differ in the last digit. Harris (1978) gives 1.78 dB for the Hamming scalloping loss, which is the value the unrounded coefficients $25/46$ and $21/46$ give; the rounded 0.54 and 0.46 used here give 1.75 dB."

### F11. What Cooley and Tukey published
- **Where:** `src/content/blog/dft-and-fft.mdx:111`
- **Text:** "The version described here, the radix-2 decimation-in-time algorithm, was published by Cooley and Tukey in 1965"
- **Problem:** The 1965 paper describes the factorisation of the DFT for composite $N$ in general. Radix-2 is its main worked case, not the whole of it.
- **Recommended correction:** "The version described here, the radix-2 decimation-in-time algorithm, is the best-known case of the algorithm Cooley and Tukey published in 1965 for any composite $N$; ..."

### F12. Parks–McClellan coefficient count
- **Where:** `src/content/blog/designing-fir-and-iir-filters.mdx:162`
- **Text:** "and it typically meets a specification with fewer coefficients than any window design."
- **Problem:** No Parks–McClellan design is computed. The sentence is a general property, and it is stronger than "typically": a minimax design of a given order, weighted by the ratio of the two tolerances, meets any specification that a window design of that order meets.
- **Recommended correction:** "As a general property of this optimal design, it never needs more coefficients than a window design for the same band edges and tolerances, and usually needs fewer (this entry does not compute one)."

### F13. Where $A(\omega)$ changes sign
- **Where:** `src/content/blog/designing-fir-and-iir-filters.mdx:63`
- **Text:** "(plus a jump of $\pi$ wherever $A(\omega)$ changes sign, which happens only in the stopband)"
- **Problem:** This is true for a low-pass design like the running example, not for every symmetric filter.
- **Recommended correction:** "(plus a jump of $\pi$ wherever $A(\omega)$ changes sign, which in a low-pass design such as this one happens only in the stopband)"

### F14. Two general claims in entry 5
- **Where:** `src/content/blog/from-signal-processing-to-digital-control.mdx:59` and `:243`
- **Text:** "inside the loop the feedback moves the closed-loop poles inside the unit circle" and "A loop designed in continuous time with a typical phase margin of 45° to 60° survives the delay only if ..."
- **Problem:** The first holds only for suitable gains, as §2.2 of the same entry shows for the proportional loop. The second is a common design target, not a measured property of loops.
- **Recommended correction:** "inside the loop, with suitable gains, the feedback moves the closed-loop poles inside the unit circle" and "A loop designed in continuous time for a phase margin of 45° to 60°, a common design target, survives the delay only if ..."

### F15. Missing links to the completed Foundations of Control Systems series
- **Where:** `src/content/blog/from-signal-processing-to-digital-control.mdx:77` and `:141`
- **Text:** "For a plant of higher order, the same calculation done with the matrix exponential of the state-space model ([state-space primer](/blog/state-space-models-primer)) gives the equivalent" and "Controllers are often designed in continuous time, with the tools of the control series, and then converted into a difference equation."
- **Problem:** Master now contains [Stability and Eigenvalues](/blog/stability-and-eigenvalues). Its section "Stability in discrete time" derives exactly this model, $x[k+1] = A_d x[k] + B_d u[k]$ with $A_d = e^{AT}$, and the eigenvalue map $e^{\lambda T}$. Master also contains [Designing a State-Feedback Controller](/blog/state-feedback-controller-design), a continuous-time design whose section "The controller runs in continuous time" raises exactly the sample-and-hold question this entry answers. "The tools of the control series" is vague.
- **Recommended correction:** §2.1: "... the same calculation done with the matrix exponential of the state-space model ([state-space primer](/blog/state-space-models-primer)) gives the equivalent, $x[k+1] = A_d\,x[k] + B_d\,u[k]$ with $A_d = e^{AT}$, which [Stability and Eigenvalues](/blog/stability-and-eigenvalues#stability-in-discrete-time) derives; the poles always map as ...". §3.1: "Controllers are often designed in continuous time, for example by the pole placement of [Designing a State-Feedback Controller](/blog/state-feedback-controller-design), whose closing section notes that a sampled implementation adds delay, and then converted into a difference equation."

### F16. No objective for the final entry
- **Where:** `src/content/series/digital-signal-processing.md:6–10`
- **Text:** the four objectives end with "Design FIR and IIR filters to a specification and implement them within hardware limits."
- **Problem:** The description ("the step from signal processing to digital control") and the body ("ends by placing a digital filter inside a feedback loop as a digital controller") promise entry 5, but no objective states what it teaches.
- **Recommended correction:** Add "Treat a digital control loop as a signal-processing system: discretise a plant and a controller, and account for the delays that sampling, holding and filtering add when choosing the sampling rate." Add the equivalent objective to `src/content/series/vi/digital-signal-processing.md`.

## Concept introduction map

| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Discrete-time signal, sequence | `signals-and-systems-in-discrete-time.mdx:15` | `signals-and-systems-in-discrete-time.mdx:46` | Good. |
| Sampling, aliasing, Nyquist frequency | `signals-and-systems-in-discrete-time.mdx:17` | Prerequisite (sensor series entry, linked at :17); Nyquist frequency at :82 | Good. |
| Euler's formula, complex exponential | `signals-and-systems-in-discrete-time.mdx:17` | :17 (prerequisite stated), :60 | Good. |
| Normalised angular frequency $\omega$ | `signals-and-systems-in-discrete-time.mdx:37` | :37, §1.3 (:72) | Good. |
| LTI system, linearity, time invariance, causality, BIBO stability | `signals-and-systems-in-discrete-time.mdx:21` | §2.2 (:107–123) | Good. |
| Difference equation, coefficient convention | `signals-and-systems-in-discrete-time.mdx:21` | §3.1 (:136–150) | Good. |
| Impulse response, convolution, FIR/IIR | `signals-and-systems-in-discrete-time.mdx:24` | §4 (:194–219); forward reference at :24 | Good. |
| Frequency response | `signals-and-systems-in-discrete-time.mdx:60` | §6.1 (:316–322) | Good. |
| z-transform, ROC, DTFT | `z-transform-poles-and-stability.mdx:17` | §1.1–1.2 (:25–49) | Good. |
| Transfer function, poles, zeros | `z-transform-poles-and-stability.mdx:17` | §2.1–2.2 (:84, :117); poles used briefly at :49 with a pointer | Good. |
| Laplace transform, $s$-plane | `z-transform-poles-and-stability.mdx:37` | Prerequisite: Foundations entry 1 (linked at :212) | Acceptable; link text corrected (F3). |
| Group delay, linear phase | `z-transform-poles-and-stability.mdx:261` | :258–264 | Good. |
| DFT, bins, conjugate symmetry | `dft-and-fft.mdx:17` | §1.2–1.3 | Good. |
| FFT, butterfly, twiddle factor | `dft-and-fft.mdx:17` | §3.1–3.2 | Good. |
| Leakage, window, scalloping loss, coherent gain, ENBW | `dft-and-fft.mdx:17` | §4.1–5.1 | Good. |
| Welch's method | `dft-and-fft.mdx:300` | :300 | Good. |
| Tolerance scheme, passband, stopband | `designing-fir-and-iir-filters.mdx:33` | §1.2 | Good. |
| Window method, Gibbs phenomenon, Kaiser window, Parks–McClellan | `designing-fir-and-iir-filters.mdx:73` | §3.1–3.4 | Good. |
| Decimation | `designing-fir-and-iir-filters.mdx:166` | :166 and the linked sensor entry | Good. |
| Butterworth prototype, bilinear transform, prewarping | `designing-fir-and-iir-filters.mdx:176` | §4.1–4.2 | Good. |
| Direct forms, second-order sections | `designing-fir-and-iir-filters.mdx:305` | §5 | Good. |
| Fixed point (Q15), IEEE 754 floating point | `designing-fir-and-iir-filters.mdx:323` | §6.1 | Good. |
| Round-off noise, noise gain, limit cycle, dead band | `designing-fir-and-iir-filters.mdx:368` | §6.3–6.4 | Good. |
| Sampled-data system, ZOH, ADC, DAC | `from-signal-processing-to-digital-control.mdx:23` | §1.1 | Good. |
| Plant, controller, reference, error | `from-signal-processing-to-digital-control.mdx:17` | Prerequisite: Foundations entry 1 (linked at :17) | Good. |
| Damping ratio | `from-signal-processing-to-digital-control.mdx:159` | Foundations entry 1 (prerequisite linked at :17) | Acceptable. |
| PI controller, integrator windup, clamping | `from-signal-processing-to-digital-control.mdx:59` | §1.3, §3.2–3.3 | Good. |
| Crossover frequency, phase margin | `from-signal-processing-to-digital-control.mdx:149` | §4.2 (:232) | Used once in passing in §3.1 ("the crossover frequency of the loop") before §4.2 defines it; acceptable. |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| Python 3.13, NumPy 2.5 | Entry 1 :40; "Python 3 with NumPy" in entries 2–5 | Yes | Verified: Python 3.13.16 and NumPy 2.5.3 reproduce every output. |
| Difference-equation sign convention ($a_0 = 1$, $+a_k$ on the left) | Entry 1 :142 | Yes | Consistent in all entries and in the code. |
| DFT sign and $1/N$ placement (NumPy's) | Entry 3 :53 | Yes | Correct for `numpy.fft` default `norm="backward"`. |
| Periodic vs symmetric windows | Entry 3 :242, entry 4 :83 | Yes | Consistent. |
| Angles in radians, $\omega$ in rad/sample, decibels as $20\log_{10}$ | Entry 1 :40, entry 4 :17 | Yes | Consistent. |
| Systems start at rest; causal sequences | Entry 1 :150, entry 2 :19 | Yes | Consistent. |
| Python `round()` rounds halves to even | Entry 4 :381 | Yes | Correct; matters for the printed limit cycle. |
| Q15 / Q14 fixed-point formats, IEEE 754 single and double | Entry 4 :323–324 | Yes | Correct. |
| Command applied at $t = nT$ vs at the next tick | Entry 5 :55 | Yes | Consistent with §4.2. |
| $T_s$ written $T$ in entry 5 | Entry 5 :17 | Yes | Fine. |

## Series-level notes

- **Cross-references.** Every "first/second/third/fourth/fifth entry", "next entry" and "Section N" reference was checked against its target. Apart from F3, F4, F5 and F8, all are accurate. Examples: entry 1's promises that entry 4 shows cascade order mattering with finite word length (entry 4 §5, section ordering) and that entry 5 reuses $a = e^{-T_s/\tau}$ (entry 5 §2.1); entry 2's references to the moving average's zeros; entry 3's "filter design (in the next entry) uses the symmetric form" (entry 4 §3.1); entry 4's "as the next entry shows, it can be decisive" (entry 5 §4.3); entry 5's use of the Euler factor $-1.5$ for $\lambda = -50$, $h = 0.05$ (matches `numerical-integration-notes.mdx:88`). Links to other series also check out: the sensor series' oversampling section says what entry 4 §3.5 attributes to it, its §3.2 derives the $q/\sqrt{12}$ figure, the state-space primer gives the eigenvalues $-0.25 \pm 1.984j$, and *Feedback and System Behavior* has the plant, the offset 0.8 for $k = 4$, the delay warning and the integrator remark that entry 5 cites.
- **Terminology.** Terms are defined once and used consistently ("transfer function", "pole", "group delay", "order", "section"). Spelling is the exception (F2).
- **Structure and tone.** All five entries have the same structure: an introduction linking back, numbered sections, exercises with answers in `<details>`, a summary table, a closing paragraph that names the next entry, and references. The frontmatter is consistent: category "Mathematical Foundations", `seriesOrder` 1–5, the same date, and tags in the site's existing forms ("linear-systems" and "control-theory" match the Foundations series).
- **References.** The thirteen works are real and correctly cited: Oppenheim and Schafer (3rd ed., 2010); Oppenheim, Willsky and Nawab (2nd ed., 1997); Proakis and Manolakis (4th ed., 2007); Jury (Wiley, 1964); Cooley and Tukey (*Math. Comp.* 19(90):297–301, 1965); Heideman, Johnson and Burrus (*IEEE ASSP Magazine* 1(4):14–21, 1984); Harris (*Proc. IEEE* 66(1):51–83, 1978); Welch (*IEEE Trans. Audio Electroacoust.* 15(2):70–73, 1967); Parks and McClellan (*IEEE Trans. Circuit Theory* 19(2):189–194, 1972); IEEE Std 754-2019; Franklin, Powell and Workman (3rd ed., Addison-Wesley, 1998); Åström and Wittenmark (3rd ed., Prentice Hall, 1997); Åström and Murray (Princeton, 2008). No volume or page detail needed removing.

## Verification log

- `npm run build:local` (on db16bd5 merged with master): 0 errors, 0 warnings; 83 pages indexed in 2 languages.
- `npm run check:links`: 224 pages and 6435 internal references checked; all resolve, including the `#fragment` anchors of the series.
- Dist checks: Mermaid min-widths 431 px (entry 1), 399 px (entry 2), 440 px (entry 3), 473 px (entry 4), and 393 and 428 px (entry 5), all below 600 px. No `katex-error`. No text glued to inline elements (the only candidates were KaTeX's internal `log` spans).
- Recomputed (Python 3.13.16, NumPy 2.5.3):
  - **Python blocks.** All 13 were extracted and run with `python -I`; each printed output matches the article byte for byte (entry 1: 2 blocks, entry 2: 2, entry 3: 3, entry 4: 4, entry 5: 2).
  - **Entry 1.**
    - Step-response threshold: $\ln 0.05/\ln 0.9 = 28.43$, so $n = 28$.
    - Time constant: $\tau = 94.9$ ms.
    - Smoother response: $|H| = 0.319$ with phase $-62.6°$ at $0.1\pi$; gain at $\pi$ is $0.0526$ (a factor of 19).
    - Exercise 5: $59.9$ samples, so $n = 59$.
    - Exercises 1–4 checked by hand.
  - **Entry 2.**
    - Partial fractions: $A_1 = -5/3$, $A_2 = 8/3$; $H(1) = 10$.
    - Pole mapping: $e^{-0.01/0.0949} = 0.900$; $e^{-0.025} = 0.9753$ at angle $0.198$ rad.
    - Notch filter: $|a_1| = 1.8641$, $a_2 = 0.9604$; width estimate $6.37$ Hz; $-1/\ln 0.98 = 49.5$.
    - Exercises: 1 ($2/1.81 = 1.105$), 2 (pole radii $0.975$ and $1.025$, real poles $0.564$ and $-1.064$), 3 ($e^{-0.04} = 0.961$, 31.4 samples, 15.9 Hz) and 5 ($r = 0.99372$, $\tau \approx 158.7$ samples, about 480 samples to settle).
  - **Entry 3.**
    - Four-point DFT checked.
    - Window table (zero-padded by 64, $N = 1024$, periodic forms):
      - rectangular: −13.26 dB, 3.922 dB, 1.000, 1.0000;
      - Hann: −31.47 dB, 1.424 dB, 0.500, 1.5000;
      - Hamming: −42.67 dB, 1.751 dB, 0.540, 1.3628;
      - Blackman: −58.11 dB, 1.099 dB, 0.420, 1.7268;
      - first zeros at 1, 2, 2 and 3 bins.
      - All agree with the table. The Hamming scalloping loss with the exact coefficients $25/46$, $21/46$ is 1.778 dB.
    - Scalloping of a complex exponential halfway between bins ($N = 100$): $0.6366 = 2/\pi$, 3.92 dB.
    - Leakage of the 101.3 Hz tone alone into the 160.2 Hz bin: −47.9 dB with the rectangular window and −94.2 dB with Hann; Hann floor at 200–300 Hz: −108.8 dB.
    - Offset of the tone from the nearest bin: 0.067 bins.
    - Exercises 1–5 checked.
  - **Entry 4.**
    - FIR window table ($\omega_c = \pi/2$, $M = 200$, method as stated):
      - rectangular: $\delta$ = 0.0895, 21.0 dB, $1.84\pi/M$;
      - Hann: 0.0064, 43.9 dB, $6.25\pi/M$;
      - Hamming: 0.0020, 54.2 dB, $6.66\pi/M$;
      - Blackman: 0.0002, 75.3 dB, $11.17\pi/M$.
    - Kaiser's formulas checked against Kaiser's published form, as given in Oppenheim and Schafer: $\beta = 0.1102(A - 8.7)$ for $A > 50$, $0.5842(A - 21)^{0.4} + 0.07886(A - 21)$ for $21 \le A \le 50$, $0$ below, and $M = (A - 8)/(2.285\,\Delta\omega)$. Values: $\beta(50) = 4.534$ and $M = 58.5$; Exercise 1 gives $\beta = 6.755$ and $M = 207.3$.
    - Biquad: $K = 0.32492$, coefficients $[0.067455, 0.134911, 0.067455]$ and $[1, -1.142981, 0.412802]$.
    - Analog Butterworth gain at twice the cut-off: 12.3 dB.
    - Noise gains: 3.489 (5.43 dB) and 11 920.7 (40.76 dB, 6.77 bits); the 5 Hz coefficients and the pole radius 0.97803 also check.
    - Exercises 3 (178.6 Hz) and 4 (Q14 values $-18727/16384$, $6763/16384$, radius 0.642480) checked.
    - Limit-cycle sequence checked.
  - **Entry 5.**
    - $\coth(T/2)$ table: 200.0, 20.02, 10.03, 4.08, 2.16.
    - Exercise 1: $20.067$ by both formulas. Exercise 2: $9.508$.
    - Emulation maps for $sT = -2.5$: $-1.5$, $0.2857$, $-0.111$, $0.0821$.
    - Damping ratio: $\zeta = 0.791$; the PI zero is at $0.882$.
    - Phase-lag table and the sampling rates of Exercise 3 checked.
    - FIR delay at 2 Hz: 23.8°.
- Not verified: the historical claim that Gauss's FFT-like method was unpublished in his lifetime rests on the cited Heideman, Johnson and Burrus paper, which was not available here (it is consistent with that paper as generally summarised). The claim that transposed direct form II is popular in floating point because its states hold "partial sums of moderate size" is a common justification; it was not tested numerically.
