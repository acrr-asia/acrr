# Series review: Digital Signal Processing for Engineers

- Series: `digital-signal-processing` (5 articles, status published, 0 planned entries)
- Reviewed commit: 49941d2 (the wave-1 revision of this series is ab51b74; no file in scope changed after it). During the review the working tree gained an uncommitted, site-wide tag normalization that touches four entries' front matter only ("linear systems", "FFT", "control theory"); it changes no line number or text cited below.
- Date: 2026-10-14
- Review type: independent review (wave 2), fact-check, technical review and series review, of the text as revised in wave 1 (`git diff e21dcc8`).
- Content hash: sha256:1ffe91b624fa58a5768f3b1508ba0231ddb722331011d9e0e3d5a2c214a19840
## Summary

The series remains technically strong. All 13 Python blocks were rerun with Python 3.13.16 and NumPy 2.5.3 and every printed output matches the article byte for byte. Every other worked number was recomputed (window tables of entries 3 and 4, leakage levels, Kaiser formulas, Butterworth biquad, noise gains, stability limits, phase-lag table, all 25 exercise answers) and is correct. The wave-1 changes (sentence-case headings, American spelling, descriptions, reference format, sentence splits) introduced no technical error. All thirteen references exist and their bibliographic details are correct as far as could be checked.

One sentence in entry 1, present before wave 1, is wrong: it says the three-point average "would leave a 60 Hz component almost untouched" at $f_s = 150$ Hz (the gain is 0.21) and that the trick works whenever $f_s$ is "a multiple of the interference frequency" (at 100, 200 or 300 Hz it does not). The should-fix findings are an unsupported reason given for the popularity of transposed direct form II (flagged by wave 1 and not verifiable), a prerequisite list in the overview and entry 1 that omits the Laplace transform and feedback vocabulary that entries 2, 4 and 5 rely on, and one section heading in entry 5 that wave 1 left in title case. The series is ready once T1 is fixed and the should-fix findings are resolved.

Findings: 1 blocking, 3 should fix, 7 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Describe discrete-time signals and linear time-invariant systems by difference equations, impulse responses and convolution. | Entry 1 §1–5 | Met: sequences, discrete-time frequency, five system properties, difference equations, impulse response, convolution sum with derivation, stability from $\sum\lvert h[n]\rvert$. |
| Use the z-transform to analyze stability and frequency response. | Entry 2 §1–5 | Met: ROC, transform table, transfer function, partial fractions, pole condition and stability triangle, $s$-to-$z$ map, geometric frequency response, notch design. |
| Compute and interpret spectra with the DFT and FFT, including leakage and windowing. | Entry 3 §1–5 | Met: definition and conventions, bins, symmetry, zero padding, circular convolution, radix-2 FFT with code, leakage, window table, dynamic-range example, amplitude and noise scaling. |
| Design FIR and IIR filters to a specification and implement them within hardware limits. | Entry 4 §1–6 | Met: tolerance scheme, linear phase, window and Kaiser designs, decimation, bilinear transform with prewarping, Butterworth order, structures, coefficient quantization, round-off noise, overflow, limit cycles. |
| Treat a digital control loop as a signal-processing system: discretize a plant and a controller, and account for the delays that sampling, holding and filtering add when choosing the sampling rate. | Entry 5 §1–6 | Met: ZOH equivalent, proportional loop stability limit, emulation rules, digital PI with windup, derivative filter, hold and computation delay, filter delay, sampling-rate choice. |

The objectives begin with "Describe", "Use", "Compute", "Design" and "Treat"; "Use" and "Treat" are weaker than the verbs standards 6.5 suggests, but each objective is checkable and met (left as optional by wave 1; not re-raised).

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| T1 | Blocking | `src/content/blog/signals-and-systems-in-discrete-time.mdx` | §6.2 (line 377) | accuracy | The three-point average reduces a 60 Hz component at $f_s = 150$ Hz to 0.21 of its amplitude, not "almost untouched"; and choosing $f_s$ as a multiple of 50 Hz is not sufficient (at 100, 200, 300 Hz the gain at 50 Hz is 1/3, 1/3, 2/3). |
| F1 | Should fix | `src/content/blog/designing-fir-and-iir-filters.mdx` | §5 (line 307) | evidence | "transposed direct form II is popular in floating-point implementations because its state variables hold partial sums of moderate size": popularity and reason unsourced; the one authoritative account found gives a different reason. |
| S1 | Should fix | `src/content/series/digital-signal-processing.md`, `src/content/blog/signals-and-systems-in-discrete-time.mdx` | overview line 14; entry 1 line 17 | purpose | Prerequisites omit the Laplace transform and $s$-plane poles (entries 2 §4.3, 4 §4.1–4.2, 5) and basic feedback vocabulary (entry 5), which the series never introduces and which come from Foundations of Control Systems. |
| S2 | Should fix | `src/content/blog/from-signal-processing-to-digital-control.mdx` | line 249 | consistency | Heading "## 5. Choosing the Sampling Rate" is still title case; every other heading in the series is sentence case (standards 5.4). Missed by `heading-case` and by wave 1. |
| S3 | Optional | `src/content/blog/z-transform-poles-and-stability.mdx` | §5.2 (line 264) | accuracy | "why recursive filters cannot [have linear phase]": the property belongs to causal IIR filters (entry 4 :53 says so); a recursive realization of an FIR filter can have linear phase. |
| S4 | Optional | `src/content/blog/signals-and-systems-in-discrete-time.mdx` | §4.4 (line 276) | consistency | "the fourth entry shows that with finite word length it can [matter]": entry 4 :315 states the section-ordering practice but does not show it. |
| S5 | Optional | `src/content/series/digital-signal-processing.md` | line 18 | consistency | "the notation table of the first entry: ... a single sign convention for difference equations and the assumption that systems start at rest": those two conventions are in entry 1 §3.1, not in its table. |
| S6 | Optional | entries 3, 4, 5 | `dft-and-fft.mdx:19`, `designing-fir-and-iir-filters.mdx:17`, `from-signal-processing-to-digital-control.mdx:17` | consistency | Versions are stated three ways: entry 1 (3.13, 2.5), entry 2 ("run with the versions stated in the first entry"), entries 3–5 ("Python 3 and NumPy"). |
| T2 | Optional | `src/content/blog/dft-and-fft.mdx` | §5.3 (line 300) | language | "subject to up to the scalloping loss if it lies between bins" is ungrammatical. |
| T3 | Optional | `src/content/blog/from-signal-processing-to-digital-control.mdx` | §4.2 (line 232) | accuracy | "The stability of a feedback loop is governed by its phase at the crossover frequency" holds for the usual loop whose gain crosses 1 once; unqualified it overstates the rule. |
| F2 | Optional | `src/content/blog/designing-fir-and-iir-filters.mdx` | §6.4 (line 374) | evidence | "Most signal-processing hardware offers saturation as an option": a quantified generalization without a source. |

### T1. The 60 Hz remark and the "multiple" condition
- **Where:** `src/content/blog/signals-and-systems-in-discrete-time.mdx:377`, section "6.2 Example: a moving average that removes mains interference"
- **Text:** "The same filter would leave a 60 Hz component almost untouched at this sampling rate, so the trick depends on choosing $f_s$ as a multiple of the interference frequency."
- **Problem:** With the article's own gain formula $|1 + 2\cos\omega|/3$, 60 Hz at $f_s = 150$ Hz is $\omega = 0.8\pi$ and the gain is $|1 + 2\cos 0.8\pi|/3 = 0.618/3 = 0.206$ (recomputed with NumPy: 0.20601), an attenuation of about 13.7 dB, not "almost untouched". The conclusion is also too weak: $f_s$ a multiple of 50 Hz is not enough for this filter. At $f_s = 100$, 200 and 300 Hz the three-point average has gain 0.333, 0.333 and 0.667 at 50 Hz (recomputed). What the trick needs is that the averaging length spans exactly one interference cycle, $f_s = 3 \times 50$ Hz for three points. Entry 2 :268 already states it correctly ("needed $f_s$ to be exactly three times the interference frequency (a longer average needs another fixed multiple)"), so the two entries currently disagree. The sentence predates wave 1.
- **Correction:** "At the same sampling rate a 60 Hz component is only reduced, to 0.21 of its amplitude, not removed, so the trick depends on matching the average to the interference: an $N$-point average removes it when $f_s$ is exactly $N$ times the interference frequency, so that the $N$ samples span one cycle."

### F1. Transposed direct form II and floating point
- **Where:** `src/content/blog/designing-fir-and-iir-filters.mdx:307`, section "5. Implementation structures"
- **Text:** "transposed direct form II is popular in floating-point implementations because its state variables hold partial sums of moderate size."
- **Problem:** The claim is stated as fact without a source and was recorded as untested by the earlier review and flagged by wave 1. None of the entry's references supports it. J. O. Smith III, *Introduction to Digital Filters with Audio Applications*, section "Numerical Robustness of TDF-II" (CCRMA, fetched), gives a different reason for preferring TDF-II: "the zeros effectively precede the poles in series order", so the zeros' attenuation offsets the large gain that poles near the unit circle give at some frequencies; it does not say the structure is popular in floating point or that its states are partial sums of moderate size. Standards 7.2: an unverifiable claim is qualified or removed.
- **Correction:** Replace the bullet with "The **transposed** forms reverse every signal path and need the same number of delays; in transposed direct form II the zeros act before the poles." (or remove the second clause entirely). Do not keep the popularity claim unless a source that states it is added to the references.

### S1. Prerequisites that the series relies on but does not state
- **Where:** `src/content/series/digital-signal-processing.md:14`; `src/content/blog/signals-and-systems-in-discrete-time.mdx:17`
- **Text:** "It assumes calculus, complex numbers and basic linear algebra, and the idea of sampling that [Sampling, Quantization and Data Conversion](...) introduces"; entry 1: "The series assumes calculus, complex numbers ... and basic linear algebra. It also assumes the idea of sampling".
- **Problem:** Entry 2 §4.3 (:212) maps $s$-plane poles to the $z$-plane, entry 4 §4.1–4.2 (:176–204) designs from an analog prototype $H_a(s)$, and entry 5 uses transfer functions $C(s)$, the damping ratio, plant/controller vocabulary and continuous PI design. The series never introduces the Laplace transform; each entry links Foundations of Control Systems at the point of use, but the overview (standards 6.5, "the intended reader and the prerequisites") and entry 1's prerequisite paragraph say nothing, so a reader who meets only the stated prerequisites is surprised in entry 2. Foundations entry 1 §3.2 introduces the Laplace transform (`introduction-to-control-systems.mdx:62`).
- **Correction:** In the overview, after the sampling sentence, add: "Entries 2, 4 and 5 also use the Laplace transform and poles in the $s$-plane, and the fifth entry the vocabulary of feedback; [Introduction to Control Systems](/blog/introduction-to-control-systems) introduces both." Add the same sentence (with "The second, fourth and fifth entries") to entry 1's prerequisite paragraph at :17. Update `src/content/series/vi/digital-signal-processing.md` in the same commit.

### S2. Title-case heading in entry 5
- **Where:** `src/content/blog/from-signal-processing-to-digital-control.mdx:249`
- **Text:** "## 5. Choosing the Sampling Rate"
- **Problem:** Standards 5.4 require sentence case; wave 1 converted the other five headings of this entry ("five headings to sentence case") but not this one, and `eos lint` does not flag it. No link targets `#5-choosing-the-sampling-rate` (grep of `src/`), and a case change keeps the slug anyway.
- **Correction:** "## 5. Choosing the sampling rate".

### S3–S6, T2, T3, F2 (optional)
- **S3** `z-transform-poles-and-stability.mdx:264`: "The fourth entry shows how FIR filters achieve linear phase exactly and why causal IIR filters cannot." (entry 1 defines "recursive" by nonzero $a_k$; the recursive running sum $y[n] = y[n-1] + x[n] - x[n-N]$ is recursive, FIR and linear-phase).
- **S4** `signals-and-systems-in-discrete-time.mdx:276`: "the fourth entry notes that with finite word length it can".
- **S5** `digital-signal-processing.md:18`: "All entries share the conventions of the first entry: its notation table (frequency in radians per sample), its sign convention for difference equations and the assumption that systems start at rest." Keep the Vietnamese file in step.
- **S6** In entries 3–5, use entry 2's wording: "Code uses Python 3 and NumPy, run with the versions stated in the first entry."
- **T2** `dft-and-fft.mdx:300`: "... at its peak bin (which reduces to $2|X[k]|/N$ for the rectangular window); if it lies between bins, the reading is low by up to the scalloping loss."
- **T3** `from-signal-processing-to-digital-control.mdx:232`: "For the usual loop whose gain falls through 1 once, stability is governed by its phase at the **crossover frequency** ..."
- **F2** `designing-fir-and-iir-filters.mdx:374`: "Signal processors commonly offer saturation as an option, and it should be used." (or attribute to a named architecture with a source). Not verified as stated (see Verification log).

## Concept introduction map

| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Discrete-time signal, sequence | `signals-and-systems-in-discrete-time.mdx:15` | `:46` | Good. |
| Sampling, aliasing, Nyquist frequency | `signals-and-systems-in-discrete-time.mdx:17` | Prerequisite (sensor entry linked at :17); Nyquist at :82 | Good. |
| Euler's formula, complex exponential | `signals-and-systems-in-discrete-time.mdx:17` | :17 (stated prerequisite), :60 | Good. |
| Normalized angular frequency $\omega$ | `signals-and-systems-in-discrete-time.mdx:37` | :37, §1.3 (:72–86) | Good. |
| LTI, linearity, time invariance, causality, BIBO stability | `signals-and-systems-in-discrete-time.mdx:21` | §2.2 (:105–123) | Good. |
| Difference equation, coefficient convention, at rest | `signals-and-systems-in-discrete-time.mdx:21` | §3.1 (:136–150) | Good. |
| Impulse response, convolution, FIR/IIR | `signals-and-systems-in-discrete-time.mdx:24` | §4 (:194–219); forward pointer at :24 | Good. |
| Frequency response | `signals-and-systems-in-discrete-time.mdx:60` | §6.1 (:316–322) | Good. |
| z-transform, ROC, DTFT | `z-transform-poles-and-stability.mdx:17` | §1.1–1.2 (:25–49) | Good. |
| Transfer function, poles, zeros | `z-transform-poles-and-stability.mdx:17` | §2.1–2.2 (:84, :117); pointer at :49 | Good. |
| Laplace transform, $s$-plane | `z-transform-poles-and-stability.mdx:37` | Not introduced in the series; linked to Foundations entry 1 at :212 | Acceptable at point of use; missing from stated prerequisites (S1). |
| Group delay, linear phase | `z-transform-poles-and-stability.mdx:258` | :258–264 | Good. |
| DFT, bins, conjugate symmetry, zero padding | `dft-and-fft.mdx:17` | §1.2–1.4 | Good. |
| FFT, butterfly, twiddle factor | `dft-and-fft.mdx:17` | §3.1–3.2 | Good. |
| Leakage, window, scalloping loss, coherent gain, ENBW | `dft-and-fft.mdx:17` | §4.1–5.1 | Good. |
| Welch's method | `dft-and-fft.mdx:302` | :302 | Good. |
| Tolerance scheme | `designing-fir-and-iir-filters.mdx:33` | §1.2 | Good. |
| Window method, Gibbs phenomenon, Kaiser window, Parks–McClellan | `designing-fir-and-iir-filters.mdx:73` | §3.1–3.4 | Good. |
| Decimation | `designing-fir-and-iir-filters.mdx:166` | :166 and the linked sensor entry | Good. |
| Analog prototype $H_a(s)$, Butterworth, bilinear transform, prewarping | `designing-fir-and-iir-filters.mdx:176` | §4.1–4.2 (Laplace variable assumed, S1) | Good. |
| Direct forms, transposed forms, second-order sections | `designing-fir-and-iir-filters.mdx:305` | §5 | Good (F1 on one claim). |
| Q15, IEEE 754 | `designing-fir-and-iir-filters.mdx:323` | §6.1 | Good. |
| Round-off noise, noise gain, limit cycle, dead band | `designing-fir-and-iir-filters.mdx:368` | §6.3–6.4 | Good. |
| Sampled-data system, ZOH, ADC, DAC | `from-signal-processing-to-digital-control.mdx:23` | §1.1 | Good. |
| Plant, controller, reference, error | `from-signal-processing-to-digital-control.mdx:17` | Prerequisite linked at :17 | Good (overview silent, S1). |
| Damping ratio | `from-signal-processing-to-digital-control.mdx:159` | Foundations (linked at :17) | Acceptable. |
| PI controller, windup, clamping | `from-signal-processing-to-digital-control.mdx:59` | §1.3, §3.2–3.3 | Good. |
| Crossover frequency, phase margin | `from-signal-processing-to-digital-control.mdx:149` | §4.2 (:232) | Used once in passing at :149 before definition; acceptable (T3 optional). |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| Python 3.13, NumPy 2.5 | Entry 1 :40; entry 2 :19; entries 3–5 "Python 3 and NumPy" | Yes | Reproduced with 3.13.16 / 2.5.3. Wording differs (S6). |
| Difference-equation sign convention ($a_0 = 1$) | Entry 1 :142 | Yes | Consistent in all entries and all code. |
| DFT sign and $1/N$ placement | Entry 3 :53 | Yes | Matches `numpy.fft` default. |
| Periodic vs symmetric windows | Entry 3 :242; entry 4 :83 | Yes | Consistent. |
| Radians, rad/sample, decibels as $20\log_{10}$ | Entry 1 :40; entry 4 :17 | Yes | Consistent. |
| Systems at rest; causal sequences | Entry 1 :150; entry 2 :19 | Yes | Consistent. |
| Python `round()` half-to-even | Entry 4 :381 | Yes | Correct; determines the printed limit cycle. |
| Q15/Q14, IEEE 754 single/double | Entry 4 :323–324 | Yes | Correct (24- and 53-bit significands). |
| Command applied at $t = nT$ vs next tick | Entry 5 :55 | Yes | Consistent with §4.2. |
| $T_s$ written $T$ in entry 5 | Entry 5 :17 | Yes | Fine. |

## Series design

**Purpose, audience and scope.** The rewritten overview states the reader (engineers working with sampled signals), the aim, the order and the shared conventions, and the five objectives are checkable and each met by a named entry. Its prerequisite statement is incomplete (S1): the Laplace transform and feedback vocabulary are needed from entry 2 on.

**Sequence and rationale.** Time domain, then z-domain, then spectra, then design, then control is the right order for the stated reader, and the overview now says why. The wave-1 flag asked whether "each uses the tools of the one before" is fair for entry 3: it is. Entry 3 takes the DTFT from entry 2 (:25, "The second entry defined the DTFT ... as its z-transform on the unit circle") and invokes "the dual of the convolution property of the second entry" (:222), besides entry 1's convolution and frequency. Entry 5 uses entry 4's bilinear transform, FIR delay and word-length results. No entry would serve better moved, split or merged.

**Prerequisites and dependencies.** Nothing depends on a later entry. External dependencies (sensor entry, Foundations entries 1–5, numerical integration notes) are linked where used and say what is attributed to them (checked; see Series-level notes). Only the overview's statement lags (S1).

**Notation and depth.** Symbols agree across entries ($\omega$, $T_s$/$f_s$, $H(e^{j\omega})$, $b$/$a$ arrays; $T$ for $T_s$ in entry 5, stated). Depth is even: every entry has derivations, at least two runnable scripts, five exercises with answers, a summary table and references.

**Overview completeness.** The body matches what the entries deliver and promises nothing they do not. Two small inaccuracies: the prerequisite list (S1) and the description of the "notation table" (S5). The Vietnamese overview (`src/content/series/vi/digital-signal-processing.md`) has not yet been updated for the wave-1 rewrite of the English body; translations are outside this review, but it should be updated together with S1/S5.

## Series-level notes

- **Cross-references.** Every "first/second/third/fourth/fifth entry", "next entry" and "Section N" reference in the five entries was checked against its target and is accurate, except the two optional imprecisions S3 and S4. Promises are fulfilled: entry 2's linear-phase promise by entry 4 §2.1 (:53); entry 1's $a = e^{-T_s/\tau}$ reuse by entry 5 §2.1; entry 4's "as the next entry shows, it can be decisive" by entry 5 §4.3; entry 3's symmetric-window remark by entry 4 §3.1. Outbound links say what is attributed to them: `sampling-quantization-and-data-conversion.mdx:75` (oversampling, gentle analog plus steep digital filter, decimation) and §3.2 ($q^2/12$); `state-space-models-primer.mdx:116,123` ($-0.25 \pm 1.984j$); `stability-and-eigenvalues.mdx:230–242` (§7, $x[k+1] = A_d x[k] + B_d u[k]$, $k$ as index); `state-feedback-controller-design.mdx:222–224` (§6.4, design on the discrete model when $T$ is not small); `numerical-integration-notes.mdx:36,117` ($1 + h\lambda$, $-1.5$ for $\lambda = -50$, $h = 0.05$); `feedback-and-system-behavior.mdx:73,102,161,165–169` (plant $a = b = 1$, offset 0.8 at $k = 4$, integrator remark, delay warning, "unstable for $k$ above about 20" at $T = 0.1$ s, matching entry 5's 20.02). Entry 1's statement in T1 contradicts entry 2 :268; fixing T1 resolves it.
- **Terminology and spelling.** American spelling throughout after wave 1 (no "analogue", "centre", "quantis-", "towards" left in the five entries); terms defined once and used consistently.
- **Structure and tone.** Uniform across entries; frontmatter consistent (category, `seriesOrder` 1–5, dates).
- **References.** Thirteen distinct works; all exist (see Verification log). Format follows standards 7.3 after wave 1; lists are alphabetical.

## Verification log

- Build: not run (instruction for this wave). Used the current site build in `/tmp/claude-0/b2` (built after wave 1 with `SITE_URL=https://acrr.asia`).
- `node scripts/check-links.mjs /tmp/claude-0/b2`: 314 pages, 9667 internal references, all resolve (including `#conventions-used-throughout-the-series`, `#7-stability-in-discrete-time`, `#64-the-controller-runs-in-continuous-time`, `#21-oversampling`, `#32-quantization-error-as-uncertainty`).
- Rendered pages `/tmp/claude-0/b2/blog/<slug>.html`: `katex-error` count 0 in all five; Mermaid min-widths 431, 399, 440, 473, 393 and 428 px (all under 600 px); no text glued to inline elements (the only `letter<span` matches are KaTeX internals such as `lo<span` in "log" and an opening quote before inline math).
- `npm run -s eos -- lint digital-signal-processing`: 0 errors, 1 warning (`heading-numbering` at entry 1 :27, justified in wave 1: the unnumbered conventions section is the series-wide anchor), 17 suggestions (acronyms inside linked titles and journal names; sentences of 46–48 words). Not re-reported.
- `npm run -s eos -- syntax` on the six files: "All files compile."
- Code: all 13 Python blocks extracted and run with `python3 -I` (Python 3.13.16, NumPy 2.5.3); 13 of 13 outputs identical to the article.
- Recomputed (NumPy): entry 1 — 3-point gain at 60 Hz / 150 Hz = 0.2060 (T1); gains at 50 Hz for $f_s$ = 100, 200, 300 Hz = 0.333, 0.333, 0.667 (T1); $\ln 0.05/\ln 0.9 = 28.43$; $\tau = 94.9$ ms; smoother at $0.1\pi$: 0.319, −62.6°; $(1-a)/(1+a) = 0.0526$; Ex. 5 $e^{-0.05} = 0.9512$, 59.91. Entry 2 — $A_1 = -5/3$, $A_2 = 8/3$; notch width estimate 6.37 Hz; Ex. 1 maximum gain 1.105 at $\omega = \pi/2$ (derivative of the squared gain in $\cos 2\omega$ is negative everywhere, so the maximum is at $\cos 2\omega = -1$); Ex. 2 roots 0.564, −1.064; Ex. 5 $r = 0.99372$, 158.7 samples. Entry 3 — four-point DFT; window table for $N = 1024$ (rect 1/−13.26/3.92/1.00/1.00; Hann 2/−31.47/1.42/0.50/1.50; Hamming 2/−42.67/1.75/0.54/1.36; Blackman 3/−58.11/1.10/0.42/1.73); exact Hamming (25/46, 21/46) scalloping 1.778 dB and −76.1 dB at 2.5 bins; leakage without the weak tone −47.9 dB (rect) and −94.2 dB (Hann); 101.3 Hz is 0.067 bins from 101.56 Hz. Entry 4 — window-design table at $M = 200$, $\omega_c = \pi/2$ reproduced exactly (0.0895/21.0/1.84; 0.0064/43.9/6.25; 0.0020/54.2/6.66; 0.0002/75.3/11.17); Kaiser $\beta = 4.534$, $M = 58.5$; noise gains 3.489 (5.43 dB) and 11 920.7 (40.76 dB; 109.2 in amplitude, 6.77 bits) with $a = [1, -1.955578, 0.956544]$, radius 0.9780; analog Butterworth at $2\Omega_c$: 12.30 dB; Ex. 1 268.1, $\beta = 6.755$, 207.3; Ex. 3 178.6 Hz; Ex. 4 −18727, 6763, radius 0.64248. Entry 5 — $\coth(T/2)$ table 200.0, 20.02, 10.03, 4.08, 2.16; emulation images −1.5, 0.286, −0.111, 0.082; $\zeta = 0.791$; PI zero 0.882; 23.76°; Ex. 1 20.07; Ex. 2 9.51, 0.905.
- References verified: Cooley and Tukey, *Math. Comp.* 19(90):297–301, 1965 (Burrus's FFT notes at fftw.org; FFT reference listings); Heideman, Johnson and Burrus, *IEEE ASSP Magazine* vol. 1, pp. 14–21, Oct. 1984 (Burrus's FFT notes, fftw.org; October is no. 4 of the quarterly volume); the extended 1985 version (*Archive for History of Exact Sciences* 34:265–277) states that Gauss's treatise, written in 1805, "was not published in his lifetime" and appeared "posthumously in Volume 3 of his collected works in 1866", which supports entry 3 §3.1 (wave-1 flag resolved); Harris, *Proc. IEEE* 66(1):51–83, Jan. 1978 (scan of the paper); Welch, *IEEE Trans. Audio Electroacoust.* 15(2):70–73, 1967 (IBM Research publication page, DOI 10.1109/TAU.1967.1161901, and a journal reference record); Parks and McClellan, *IEEE Trans. Circuit Theory* 19(2):189–194, March 1972 (reference listing in arXiv:1608.03161); Jury, *Theory and Application of the z-Transform Method*, Wiley, New York, 1964 (library catalogue; later Krieger reprints exist).
- Not verified:
  - Harris's Hamming scalloping loss of 1.78 dB (`dft-and-fft.mdx:253`): the scan of Table I is illegible for that cell (reads about 1.8). The text's own explanation is consistent with computation (exact coefficients give 1.778 dB). Left as is.
  - Popularity of transposed direct form II in floating point and the stated reason (`designing-fir-and-iir-filters.mdx:307`): no supporting source found (F1).
  - "Most signal-processing hardware offers saturation" (`designing-fir-and-iir-filters.mdx:374`): saturating instructions exist in common DSP-oriented instruction sets (e.g. Arm), but the quantified "most" was not verified (F2).
  - Book editions not re-checked against a catalogue in this pass (accepted from the earlier series review, which verified them): Oppenheim and Schafer 3rd ed. 2010; Oppenheim, Willsky and Nawab 2nd ed. 1997; Proakis and Manolakis 4th ed. 2007; Åström and Wittenmark 3rd ed. 1997 (a search confirmed a third edition of this title exists); Franklin, Powell and Workman 3rd ed. 1998; Åström and Murray 2008; IEEE Std 754-2019.
  - "a phase margin of 45° to 60°, a common design target" (`from-signal-processing-to-digital-control.mdx:243`): stated as a design target, a convention rather than a fact; not checked against a source.

## Resolution

- T1 (Blocking): fixed - reviewer's correction applied, split into two sentences: the 60 Hz component at $f_s = 150$ Hz is "only reduced, to 0.21 of its amplitude, not removed", and an $N$-point average removes the interference when $f_s$ is exactly $N$ times its frequency (`signals-and-systems-in-discrete-time.mdx:377`). Recomputed with `python3 -I` (NumPy 2.5): gain 0.2060 (-13.7 dB); gain at 50 Hz 0.333, 0.333, 0.667 for $f_s$ = 100, 200, 300 Hz; $N$-point average at $f_s = 50N$ gives 0 (to 1e-16) for $N$ = 2 to 5. Now agrees with `z-transform-poles-and-stability.mdx:268`.
- F1 (Should fix): fixed - popularity claim and unsupported reason removed; bullet now reads "The **transposed** forms reverse every signal path and need the same number of delays; in transposed direct form II the zeros act before the poles." (`designing-fir-and-iir-filters.mdx:307`). The zeros-before-poles statement checked against J. O. Smith III, "Numerical Robustness of TDF-II" (ccrma.stanford.edu/~jos/fp/Numerical_Robustness_TDF_II.html: "the zeros effectively precede the poles in series order"); the equal delay count follows from flow-graph transposition. No reference added.
- S1 (Should fix): fixed - prerequisite sentence on the Laplace transform, $s$-plane poles and feedback vocabulary, linking Introduction to Control Systems (which introduces the Laplace transform in §3.2, poles in §3.4 and the loop vocabulary in §2), added to the overview (`src/content/series/digital-signal-processing.md:14`) and to entry 1 (`signals-and-systems-in-discrete-time.mdx:17`). The Vietnamese overview was not changed (no copied field changed; prose is left to the translation follow-up).
- S2 (Should fix): fixed - "## 5. Choosing the sampling rate" (`from-signal-processing-to-digital-control.mdx:249`); slug unchanged.
- Optional applied: S3 (`z-transform-poles-and-stability.mdx:264`, "causal IIR filters"), S4 (`signals-and-systems-in-discrete-time.mdx:276`, "notes"), S5 (overview :18), S6 (entries 3 :19, 4 :17, 5 :17: code run with the versions stated in the first entry; in entry 5 as a separate sentence to keep the sentence length down), T2 (`dft-and-fft.mdx:300`), T3 (`from-signal-processing-to-digital-control.mdx:232`, qualified and the sentence split at the semicolon), F2 (`designing-fir-and-iir-filters.mdx:374`, reworded instead of the reviewer's text, which kept an unverified generalization: "Instruction sets with signal-processing extensions often provide it (the signal-processing instructions of Arm processors include a saturating addition, for example), and where it is available it should be used."; Arm's saturating add `QADD` confirmed in the Arm DSP intrinsics documentation). Optional not applied: none.
- Checks: `eos lint` on the six files: 0 errors, 1 warning (`heading-numbering` at entry 1 :27, justified in wave 1: the series-wide anchor `#conventions-used-throughout-the-series`, linked from entries 2-5, is kept), 18 suggestions (pre-existing kinds: acronyms in titles, sentences of 46-48 words). `eos syntax`: all files compile. No code block or printed output changed. No build run (per brief).
- Vietnamese follow-up (meaning changes, translation not edited): overview :14 (new prerequisite sentence) and :18 (conventions sentence). No Vietnamese translation of the five articles exists.

Resolved by the wave-1 author on 2026-10-15; awaiting the reviewer's resolution check.

## Resolution check

QA editor (final gate), 2026-10-15, against the current working tree and the build in `/tmp/claude-0/b9`.

- T1 (Blocking): confirmed. `signals-and-systems-in-discrete-time.mdx:377` now says the 60 Hz component is "only reduced, to 0.21 of its amplitude, not removed" and states the $N$-point condition. Recomputed (`python3 -I`, NumPy): gain 0.20601 (−13.72 dB); 50 Hz gains 0.333, 0.333, 0.667 at $f_s$ = 100, 200, 300 Hz; $N$-point average at $f_s = 50N$ gives below 1.3e-16 for $N$ = 2 to 5; 10 Hz gain 0.9424. Agrees with `z-transform-poles-and-stability.mdx:268`.
- F1 (Should fix): confirmed. `designing-fir-and-iir-filters.mdx:307` no longer claims popularity or a reason; the remaining statements (equal delay count under transposition; zeros before poles in TDF-II) are correct.
- S1 (Should fix): confirmed. Prerequisite sentence present in the overview (:14) and entry 1 (:17); Introduction to Control Systems does introduce the Laplace transform (§3.2), poles (§3.4) and the loop vocabulary (§1.2; the Resolution's "§2" is a slip in the report only, the article text cites no section).
- S2 (Should fix): confirmed. `from-signal-processing-to-digital-control.mdx:249` reads "## 5. Choosing the sampling rate".
- Optional S3, S4, S5, S6, T2, T3, F2: applied as described (checked at each line).
- Q1 (Optional, new): the S3 change put "causal IIR filters" into entry 2 (`z-transform-poles-and-stability.mdx:264`), and entry 2 never expands IIR (standards 5.3; `acronym-expansion` suggestion). Minor; recorded in the item's notes, not blocking.
- Checks: `eos lint digital-signal-processing` 0 errors, 1 warning (entry 1 :27 `heading-numbering`, justified), 18 suggestions; `eos syntax` on the six files: all compile; `check-links /tmp/claude-0/b9`: 314 pages, all internal links resolve; `eos validate-site /tmp/claude-0/b9`: no issue on any page of this scope; KaTeX errors 0 on the five pages. All 13 Python blocks rerun independently: 13 of 13 outputs identical. Window table of entry 3 recomputed (−13.26/−31.47/−42.67/−58.11 dB; 3.92/1.42/1.75/1.10 dB; ENBW 1.00/1.50/1.36/1.73): matches.

Verdict: no finding reopened.
- Q2 (Optional, new): `designing-fir-and-iir-filters.mdx` has two serial commas against standards 5.1 (:17 "compares the two, and ends"; :63 "an electrocardiogram, or a data pulse"); the `serial-comma` lint suggestion at :324 is a false positive (clauses). Minor; reflected in the item's language score (3) and notes, not blocking.

## Live-review revision (2026-10-23)

The chief editor's live review of `/blog/dft-and-fft` (`editorial/live-reviews/article/dft-and-fft.md`) requested two presentation changes, made in an author pass independent of the live reviewer and checked by the QA editor:

- L1: the two display equations of Section 3.2 are now `aligned` blocks; the mathematics and the trailing punctuation are unchanged. Measured in a local build: both fit their box at 1280 px (640 of 640 px) and at 360 px (328 of 328 px); 0 KaTeX errors.
- L3: window-table header "Equivalent noise bandwidth (bins)" shortened to "ENBW (bins)"; the list after the table already introduces "Equivalent noise bandwidth (ENBW)". The table still scrolls by about 33 px at 1280 px because every cell has a 7rem minimum width (`prose.css`), a site-level matter left with the live finding.

No wording, number, code or reference changed; the series review above still covers the text. `eos lint`: 0 errors, 0 warnings, 2 suggestions (as before).
