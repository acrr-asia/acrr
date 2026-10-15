# Independent review (wave 2): standalone scope

- Scope: the six insights in `src/content/insights/*.md` (English), the standalone article `src/content/blog/numerical-integration-notes.mdx`, and the English fields of `src/data/learning.json`.
- Reviewed text: working tree after wave-1 commit `9232ed9` (diff against `e21dcc8` read for every file).
- Roles performed: fact-checker (F) and technical reviewer (T). The reviewer did not write or revise any of this text.
- Date: 2026-10-13.

## Summary

Findings: 0 blocking, 3 should fix, 3 optional.

All references exist and their bibliographic details are correct (verified below). Every number in scope was recomputed and the article's code block was re-run; all printed values match. The three should-fix findings are technical precision problems: one in the new Section 2 of the numerical integration notes (the error-accumulation argument conflates convergence with absolute stability), one in the new imaginary-axis paragraph of the same article ("slight" damping is false near the stability limit), and one wave-1 flag in the control/learning insight (gain and phase margins described too vaguely). The insights all have the framing paragraph and the three required sections in order, Established contains only verifiable claims, and Interpretation is labeled as such.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `src/content/blog/numerical-integration-notes.mdx:67`, Section 2 | accuracy | Order argument requires that the method "does not amplify earlier errors" and says Section 4 makes this precise; convergence needs only bounded amplification as $h \to 0$, and Section 4 treats a different property (absolute stability at fixed $h$). Contradicted by the article's own Euler-on-oscillator case. |
| T2 | Should fix | `src/content/blog/numerical-integration-notes.mdx:127`, Section 4 | accuracy | "with a slight artificial damping": recomputed $\lvert R(2j)\rvert = 0.745$ per step; damping is slight only for small $h\omega$. |
| T3 | Should fix | `src/content/insights/control-vs-learning-approaches.md:16`, Established | accuracy | "gain and phase margins describe how much model error certain closed loops can tolerate" is vague: margins measure tolerance to a pure gain change or a pure phase lag, one at a time, in a single-input single-output loop. |
| F1 | Optional | `src/content/insights/compute-bound-or-memory-bound.md:16`, Established | consistency | The quantity is attributed to Williams, Waterman and Patterson as "arithmetic intensity"; the paper deliberately calls it "operational intensity" (bytes of DRAM traffic). |
| T4 | Optional | `src/content/blog/numerical-integration-notes.mdx:117`, Section 4 | accuracy | "decays only if $\lvert 1 + h\lambda\rvert \le 1$": at equality the solution neither grows nor decays. True as a necessary condition, but loose. |
| T5 | Optional | `src/content/blog/numerical-integration-notes.mdx:139`, Section 5 | structure | "the fastest mode limits an explicit method's step long after that mode has decayed, as in the example of Section 4": Section 4's example has a single mode, so it shows the step limit but not the coexistence of slow and fast modes. |

### T1. Error accumulation conflated with absolute stability
- **Where:** `src/content/blog/numerical-integration-notes.mdx:67`, Section 2 "Local error, global error and order".
- **Text:** "If each step makes a local error of size $O(h^{p+1})$, and the method does not amplify earlier errors (Section 4 makes that condition precise), the errors add up to about $(T/h)\,O(h^{p+1}) = O(h^p)$."
- **Problem:** Order is a statement about $h \to 0$ at fixed $T$. The condition the counting argument needs is that errors committed earlier are carried to $T$ with at most a bounded amplification, not that they are not amplified at all. Section 4 defines absolute stability, $\lvert R(z)\rvert \le 1$ at a fixed $z = h\lambda$, which is a different property. The article contradicts its own premise: Section 4 (line 127) shows that explicit Euler amplifies an undamped mode at every step ($\lvert 1 + jh\omega\rvert > 1$ for every $h$), yet Euler is still first order on that problem, because the total amplification over $[0, T]$ is $(1 + h^2\omega^2)^{T/(2h)} \to 1$ as $h \to 0$. Likewise the test with $\lambda = -50$ is absolutely unstable at $h = 0.05$ but converges with order 1 as $h \to 0$. On the test equation, $\lvert R(z)\rvert \le 1 + \lvert z\rvert + \dots \le e^{\lvert z\rvert}$ for both methods (every coefficient of $R$ is at most that of $e^z$), so the amplification over $T/h$ steps is at most $e^{\lvert\lambda\rvert T}$, independent of $h$; that is the bounded factor the argument uses.
- **Correction:** replace the sentence and add one after it:
  "If each step makes a local error of size $O(h^{p+1})$, and the errors made earlier are amplified by at most a bounded factor on their way to $T$, the errors add up to about $(T/h)\,O(h^{p+1}) = O(h^p)$. On the test equation that factor is at most $e^{|\lambda| T}$ whatever $h$ is, because each step multiplies an earlier error by $|R(z)| \le e^{|z|}$. This is a statement about $h \to 0$ at fixed $T$; Section 4 asks a different question, whether errors stay bounded at a fixed $h$ over many steps."

### T2. "Slight" artificial damping
- **Where:** `src/content/blog/numerical-integration-notes.mdx:127`, Section 4.
- **Text:** "RK4 keeps such a mode bounded for $h\omega \le 2\sqrt{2}$, with a slight artificial damping."
- **Problem:** Recomputed (Python 3.13) $\lvert R(jy)\rvert$ for $y = h\omega$: 0.99989 at 0.5, 0.9939 at 1, 0.941 at 1.5, 0.745 at 2, 0.508 at 2.5, 1.000 at $2\sqrt{2}$. The damping is slight only for small $h\omega$; near the limit the amplitude loses a quarter to a half per step. The wave-1 derivation $\lvert R(jy)\rvert^2 = 1 - y^6/72 + y^8/576$ is correct (checked numerically to $10^{-15}$), which gives $\lvert R\rvert \approx 1 - y^6/144$ for small $y$.
- **Correction:** "RK4 keeps such a mode bounded for $h\omega \le 2\sqrt{2}$, but damps it artificially: the amplitude factor per step is about $1 - (h\omega)^6/144$ for small $h\omega$ (0.994 at $h\omega = 1$) and falls to 0.745 at $h\omega = 2$."

### T3. Gain and phase margins
- **Where:** `src/content/insights/control-vs-learning-approaches.md:16`, Established (wave-1 flag C2).
- **Text:** "Classical tools such as gain and phase margins describe how much model error certain closed loops can tolerate."
- **Problem:** "model error" and "certain closed loops" leave the reader unable to tell what the margins guarantee. The gain margin is the factor by which the loop gain can grow, and the phase margin the extra phase lag (for example from an unmodeled delay) the loop can absorb, before a single-input single-output loop becomes unstable; each covers one kind of perturbation at a time, so a loop with good margins can still be destabilized by a combined gain and phase change. The site already defines the phase margin this way (`src/content/blog/from-signal-processing-to-digital-control.mdx:232`: "the phase margin is how far that phase is from $-180°$, and every delay in the loop eats into it").
- **Correction:** "Classical gain and phase margins measure how much extra loop gain, or extra phase lag such as an unmodeled delay, a single-input single-output loop tolerates before it becomes unstable; each covers one kind of model error at a time."

### F1. "Arithmetic intensity" versus the paper's "operational intensity"
- **Where:** `src/content/insights/compute-bound-or-memory-bound.md:16`.
- **Text:** "$I$ is the **arithmetic intensity**, the number of operations performed per byte moved between main memory and the processor."
- **Problem:** The definition matches the paper's quantity, but Williams, Waterman and Patterson name it "operational intensity" ("operations per byte of DRAM traffic") and say they avoid "arithmetic intensity" because that term is often used for traffic between processor and cache (fetched from the paper's PDF). Later literature commonly uses "arithmetic intensity", so the text is not wrong; a reader who opens the cited paper will look for the other term.
- **Correction (optional):** "$I$ is the **arithmetic intensity** (the original paper calls it operational intensity), the number of operations performed per byte moved between main memory and the processor."

### T4. Decay condition
- **Where:** `src/content/blog/numerical-integration-notes.mdx:117`.
- **Text:** "the numerical solution decays only if $|1 + h\lambda| \le 1$, which means $h \le 2/|\lambda|$."
- **Correction (optional):** "the numerical solution does not grow if and only if $|1 + h\lambda| \le 1$, which means $h \le 2/|\lambda|$; it decays for $h < 2/|\lambda|$."

### T5. Stiffness example
- **Where:** `src/content/blog/numerical-integration-notes.mdx:139`.
- **Text:** "the fastest mode limits an explicit method's step long after that mode has decayed, as in the example of Section 4."
- **Correction (optional):** "as the decaying mode of Section 4 would if it were one component of a system with a slow mode as well."

## Verification table

| Claim | Location | Status | Source or check |
|---|---|---|---|
| Williams, Waterman and Patterson, *Communications of the ACM*, vol. 52, no. 4, pp. 65–76, 2009 | compute-bound:16 | Verified | Crossref record for DOI 10.1145/1498765.1498785 (fetched through WebFetch): vol. 52, no. 4, pp. 65–76, April 2009, title "Roofline: an insightful visual performance model for multicore architectures". |
| "ridge point" as the meeting point of the two roofs | compute-bound:18 | Verified | Paper PDF (cs.colostate.edu copy): "The x-coordinate of the ridge point is the minimum operational intensity required to achieve maximum performance." |
| Sparse matrices with few operations per entry are usually bandwidth-bound (wave-1 flag) | compute-bound:26 | Verified | Same paper: SpMV operational intensity 0.17–0.25 flop/byte, "below the ridge point of all four multicores"; memory is the limiting factor in all SpMV results. Qualified as "often" in the text. |
| Roofline arithmetic: $I^* = 10$, $I = 0.0833$, $B\,I = 8.33$ GFLOP/s, 1/120 of peak; 24 bytes per element | compute-bound:20, 24 | Verified | Recomputed: 10.0, 0.08333, 8.333, 120.0. Byte count: 3 × 8 bytes, correct under the stated no-reuse assumption ($y$ is read before written, so write-allocate adds no traffic). |
| Unit roundoff $2^{-24} \approx 6\times10^{-8}$, $2^{-53} \approx 1.1\times10^{-16}$ | floating-point:16, notes:140 | Verified | Recomputed: 5.96e-8, 1.11e-16. Correctly-rounded basic operations: IEEE 754 (standard knowledge). |
| $(10^{16}+1)+1 = 10^{16}$; $10^{16}+(1+1) = 10^{16}+2$ in binary64 | floating-point:18 | Verified | Python 3.13: both comparisons `True`. |
| Recursive summation bound about $n u \sum|x_i|$; Higham, 2nd ed., SIAM, 2002, chapter 4 (wave-1 flag) | floating-point:20 | Verified | Book PDF table of contents (fetched): chapter 4 "Summation"; Second Edition, © 2002 SIAM. Bound form $\gamma_{n-1}\sum|x_i|$ is the chapter's standard result. |
| $10^6 u$: 0.06 (single), $10^{-10}$ (double); float32 counter stalls at $2^{24} = 16777216$ | floating-point:20 | Verified | Recomputed: 0.0596, 1.11e-10; `float32(2**24)+1 == float32(2**24)` is `True`. |
| Fragments `#52-checking-the-orders-...`, `#32-where-rounding-...`, `#34-the-other-numerical-errors`, `#4-validation`, `#7-direct-or-iterative` and the content they are cited for | floating-point:22, 28; sim-to-real:24; compute-bound:26 | Verified | Headings exist (from-differential-equations… :185, solving-large-linear-systems :161 and :333, verifying-and-validating… :201 and :211); link checker passes. |
| Kalman filter: exact conditional mean and MMSE among all estimators under Gaussian assumptions; best linear estimator otherwise | kalman:16 | Verified | Standard result (Kalman 1960; derivation in any estimation text); conditions stated correctly, including a Gaussian initial state. |
| UKF "usually captures nonlinear effects better than the EKF at a similar cost"; EKF mild / UKF stronger (wave-1 flag) | kalman:18, 25 | Verified (consistency) | Agrees with `sensing-and-state-estimation.mdx:184` (Section 6.2) and its table, Section 6.4 (EKF "Mildly nonlinear", UKF "More strongly nonlinear"). The guide item is presented under Interpretation. |
| "Sensing and State Estimation, the last entry of the Introduction to Robotics series" | kalman:12 | Verified | `seriesOrder: 4` of four entries; series status published. |
| NIS follows a chi-square distribution when the model holds | kalman:32 | Verified | Standard result ($m$ degrees of freedom for an $m$-dimensional measurement). |
| State-feedback entry "ends" Foundations of Control Systems and mentions LQR | control-vs-learning:16 | Verified | `seriesOrder: 5`, the last of five; LQR named at `state-feedback-controller-design.mdx:228`. |
| LQR optimal for linear model and quadratic cost; MPC finite-horizon optimization with constraints | control-vs-learning:16 | Verified | Standard definitions. |
| Euler energy factor $1 + h^2\omega^2$ per step | trustworthy:20; notes:127 | Verified | $|1 + jh\omega|^2 = 1 + h^2\omega^2$ (derivation). |
| Halving factors 2 and 16 | trustworthy:18 | Verified | Measured ratios in the notes: 2.04/2.02 and 16.7/16.3 (recomputed). |
| Code block output (table at notes:103–107) | notes:75–107 | Verified | Extracted the block and ran `python3 -I` (3.13): 1.920e-2, 9.394e-3, 4.647e-3; 3.332e-7, 1.998e-8, 1.223e-9. Matches the table to three digits. |
| Observed orders 1.03, 1.02, 4.06, 4.03; equal-work ratio about $10^4$ | notes:109, 111 | Verified | Recomputed ratios 2.044, 2.021, 16.68, 16.34; $4.647\times10^{-3}/3.332\times10^{-7} = 1.39\times10^4$. |
| Amplification factors $1+z$ and the RK4 degree-4 Taylor polynomial; local error $O(h^2)$, $O(h^5)$ | notes:55–69 | Verified | Substitution of $f = \lambda y$ into the stages gives the stated $R(z)$; truncated Taylor series of $e^z$. |
| RK4 order 4 for general smooth nonlinear $f$ (wave-1 flag) | notes:69 | Verified | Classical result; covered by the cited Butcher and Hairer–Nørsett–Wanner texts (order conditions); text defers the derivation to them. |
| $1.5^{20} \approx 3.3\times10^3$; $e^{-50} \approx 2\times10^{-22}$ | notes:117 | Verified | 3325.3; 1.93e-22. |
| RK4 real-axis limit −2.79; $R(-2.5) = 0.648$; imaginary-axis limit $2\sqrt{2}$ | notes:121 | Verified | Bisection on $|R| = 1$: −2.78529; $R(-2.5) = 0.6484$; imaginary root 2.828427 = $2\sqrt{2}$. Diagram description in `scripts/generate-diagrams.py:254` agrees. |
| RK4 after 20 steps at $z = -2.5$: $1.7\times10^{-4}$; $e^{-2.5} = 0.082$ | notes:131 | Verified | $0.6484^{20} = 1.727\times10^{-4}$; 0.0821. |
| Embedded Runge–Kutta pairs estimate local error from the same evaluations (wave-1 flag) | notes:137 | Verified | Standard description (Hairer–Nørsett–Wanner, chapter II on step-size control). |
| Backward Euler and trapezoidal rule stable on the whole left half-plane | notes:139 | Verified | Amplification factors $1/(1-z)$ and $(1+z/2)/(1-z/2)$; consistent with `finite-differences-for-heat-and-waves.mdx:258`. |
| Second Numerical Simulation entry shows stiffness and compares explicit Euler, backward Euler, Crank–Nicolson | notes:139 | Verified | `finite-differences-for-heat-and-waves.mdx` Sections 1.2, 2–4. |
| Stability-and-eigenvalues entry compares $e^{\lambda T}$ with $1+\lambda T$ | notes:129 | Verified | `stability-and-eigenvalues.mdx:244`. |
| Butcher, *Numerical Methods for Ordinary Differential Equations*, 3rd ed., Wiley, 2016 | notes:156 | Verified | Wiley-VCH product page (fetched): 3rd edition, August 2016, ISBN 978-1-119-12150-3. |
| Hairer, Nørsett and Wanner, *Solving Ordinary Differential Equations I: Nonstiff Problems*, 2nd rev. ed., Springer, 1993 | notes:157 | Verified | Library catalogue (lmbp.uca.fr, fetched): second revised edition, Springer, 1993, Springer Series in Computational Mathematics 8. |
| LeVeque, *Finite Difference Methods for Ordinary and Partial Differential Equations: Steady-State and Time-Dependent Problems*, SIAM, 2007 | notes:158 | Verified | Author's book page (faculty.washington.edu/rjl/fdmbook, fetched). |
| Learning entries: all `planned`, no `url`; series named exist and are published | learning.json | Verified | Parsed the JSON: six entries, none with `url`; Introduction to Robotics, Numerical Simulation for Engineers, Foundations of Control Systems, Machine Learning Fundamentals exist. The robotics path mentions motion planning, which the site does not cover; the description says "planned" and "to accompany", which does not claim coverage. |

## Not verified

- `when-a-kalman-filter-is-enough.md:18`: "that number often has to grow quickly with the state dimension" (particle count). Standard in the literature but no source was fetched in this pass; the claim is qualified ("often") and matches `sensing-and-state-estimation.mdx:188`. No change recommended.
- `closing-the-sim-to-real-gap.md:16–20`: the descriptions of simulator simplifications, domain randomization and system identification are treated as common knowledge for the audience; no primary source (for example the paper that introduced domain randomization) was checked or is cited. No change required by the standards; optional to cite once a source has been verified.

## Verification log

- `git diff e21dcc8 -- <each file>` read; new text in the notes (Sections 2, 4 additions, 5, 6, references, opening) given line-by-line technical review.
- Code: article's Python block extracted and run with `python3 -I` (Python 3.13); output above. Numerical checks in a scratch script (bisection for the RK4 boundaries, $|R(jy)|$ table, roofline arithmetic, float32/float64 identities).
- Links: `node scripts/check-links.mjs /tmp/claude-0/b2`: "Checked 314 pages and 9667 internal references ... All internal links resolve."
- Rendering (`/tmp/claude-0/b2`, built after wave 1): `grep -c katex-error` is 0 for the notes, all six insight pages and `learning.html`. Glued-inline-text grep: one hit in the notes, inside KaTeX markup for `\log` (not prose); zero elsewhere. The build contains the wave-1 text (`updatedAt` 2026-10-13 rendered; new Learning descriptions present).
- `npm run -s eos -- lint <file>` for each file: 0 errors, 0 warnings in all seven; suggestions only (sentence-length splitter artifacts in sim-to-real:20 and trustworthy:16; `acronym-expansion` for ACM and SIAM in citations). `eos lint` does not accept `src/data/learning.json` ("No content item matches"), so Learning was reviewed by hand.
- `npm run -s eos -- syntax src/content/insights/*.md src/content/blog/numerical-integration-notes.mdx`: "All files compile."
- Insight structure: each of the six has one framing paragraph, then `## Established`, `## Interpretation`, `## Open questions` in that order; Interpretation sections are labeled ("One reading is ..."); open questions are questions.

## Item verdicts

| Item | Fact-check | Technical | Findings |
|---|---|---|---|
| closing-the-sim-to-real-gap | pass | pass | none |
| compute-bound-or-memory-bound | pass | pass | F1 (optional) |
| control-vs-learning-approaches | pass | fail | T3 |
| floating-point-in-long-simulations | pass | pass | none |
| what-makes-a-simulation-trustworthy | pass | pass | none |
| when-a-kalman-filter-is-enough | pass | pass | none |
| numerical-integration-notes | pass | fail | T1, T2; T4, T5 (optional) |
| learning (English fields) | pass | pass (n/a: no technical content) | none |

## Resolution

- T1 (Should fix): fixed - replaced the condition "does not amplify earlier errors (Section 4 makes that condition precise)" with the reviewer's bounded-amplification wording, added the $e^{|\lambda|T}$ bound with its reason, and said that Section 4 asks a different question (fixed $h$, many steps); `src/content/blog/numerical-integration-notes.mdx:67`.
- T2 (Should fix): fixed - "with a slight artificial damping" replaced by the amplitude factor $1 - (h\omega)^6/144$ for small $h\omega$, 0.994 at $h\omega = 1$ and 0.745 at $h\omega = 2$. Recomputed with Python 3.13: $|R(j)| = 0.99391$, $|R(2j)| = 0.74536$. `src/content/blog/numerical-integration-notes.mdx:127`.
- T3 (Should fix): fixed - replaced with the reviewer's sentence (gain margin is extra loop gain; phase margin is extra phase lag such as an unmodeled delay; both for a single-input single-output loop, one kind of error at a time); `src/content/insights/control-vs-learning-approaches.md:16`.
- Optional findings applied: F1 (the paper's term "operational intensity" noted, `compute-bound-or-memory-bound.md:16`), T4 (the condition now reads "does not grow if and only if", and "decays for $h < 2/|\lambda|$", notes:117), T5 (the stiffness example reworded to a slow-plus-fast system, notes:139). Not applied: none.

Resolved by the wave-1 author on 2026-10-13; awaiting the reviewer's resolution check.

## Resolution check

QA editor (final gate), 2026-10-15. Checked against the current working tree and the build in `/tmp/claude-0/b6` (which contains the resolved text: "unmodeled delay", "operational intensity" and "0.745" are present in the rendered pages).

- T1 (Should fix): confirmed. `numerical-integration-notes.mdx:67` now requires bounded amplification, gives the $e^{|\lambda|T}$ bound with its reason ($|R(z)| \le \sum |z|^k/k! \le e^{|z|}$, true for both factors), and separates the $h \to 0$ statement from the fixed-$h$ question of Section 4.
- T2 (Should fix): confirmed. `numerical-integration-notes.mdx:127`. Recomputed (Python 3.13): $|R(j)| = 0.99391$, $|R(2j)| = 0.74536$, $|R(2\sqrt{2}j)| = 1.0000$; small-$y$ form $1 - y^6/144$ follows from $|R(jy)|^2 = 1 - y^6/72 + y^8/576$.
- T3 (Should fix): confirmed. `control-vs-learning-approaches.md:16` carries the reviewer's sentence; consistent with `from-signal-processing-to-digital-control.mdx:232`.
- F1 (Optional): confirmed applied (`compute-bound-or-memory-bound.md:16`).
- T4 (Optional): confirmed applied (`numerical-integration-notes.mdx:117`; "does not grow if and only if ... decays for $h < 2/|\lambda|$" is correct for real $\lambda < 0$).
- T5 (Optional): confirmed applied (`numerical-integration-notes.mdx:139`).

Independent spot checks: article code block re-run with `python3 -I` (errors 1.920e-2, 9.394e-3, 4.647e-3; 3.332e-7, 1.998e-8, 1.223e-9, matching the table); RK4 real-axis boundary by bisection −2.78529; $R(-2.5) = 0.6484$, $0.6484^{20} = 1.73\times10^{-4}$; $1.5^{20} = 3325$; $e^{-50} = 1.93\times10^{-22}$; equal-work ratio $1.39\times10^4$; roofline $I = 0.0833$, $B\,I = 8.33$, ratio 120; binary64 $(10^{16}+1)+1 = 10^{16}$ and $10^{16}+2$; float32 counter stall at $2^{24}$; $10^6 u$ = 0.0596 and $1.11\times10^{-10}$. Cross-reference targets read: `state-space-models-primer` (eigenvalues, Section 4), `stability-and-eigenvalues.mdx:244`, `finite-differences-for-heat-and-waves` (Section 1.2 stiffness, Section 4 Crank–Nicolson), `from-differential-equations-to-discrete-problems` Section 5.2, `solving-large-linear-systems` Sections 3.2 and 7, `verifying-and-validating-a-simulation` Sections 3.4 and 4, `state-feedback-controller-design.mdx:228` (LQR), `sensing-and-state-estimation` (`seriesOrder: 4`, last of four). References checked against the verification table: Williams et al. 2009, Higham 2002, Butcher 2016, Hairer–Nørsett–Wanner 1993, LeVeque 2007.

Checks: `eos lint` on the seven files: 0 errors, 0 warnings, 5 suggestions (two sentence-splitter artifacts, ACM/SIAM in citations). `eos syntax`: all files compile. `check-links /tmp/claude-0/b6`: 314 pages, 9693 references, all resolve. `eos validate-site /tmp/claude-0/b6 --json`: no issue on any English page in scope or on `learning.html` (the only scope-related issues are the Vietnamese meta descriptions of `vi/insights/closing-the-sim-to-real-gap` (229 characters) and `vi/insights/compute-bound-or-memory-bound` (179), outside this verdict). `katex-error` count 0 on all seven pages.

Learning (`src/data/learning.json`, English fields; not recorded by eos): pass. Six entries, all `planned`, none with a `url`; the page renders "Coming soon" with no outbound link; descriptions say "planned" and name series that exist. Note for the translation pass: two Vietnamese descriptions do not match the English (`introduction-to-robotics-learning-path` omits "to accompany the Introduction to Robotics series"; `numerical-methods-external-references` adds a sentence about links).

No finding reopened.
