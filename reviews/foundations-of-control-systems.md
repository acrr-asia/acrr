# Series review: Foundations of Control Systems

- Series: `foundations-of-control-systems` (5 articles, status published, 0 planned entries)
- Reviewed commit: 9232ed9
- Date: 2026-10-13
- Review type: independent review (wave 2), fact-check, technical review and series review of the wave-1 revision (changes since `e21dcc8`)
- Content hash: sha256:cd15a21f2681dd409d75977b17a7a7374490b68b75a7fd0c3d427cf616ee1e65

## Summary

The wave-1 revision turned entries 1-3 into complete series entries: numbered sections, stated conventions, derivations of the step-response formulas, a worked first-order transfer function, a worked stabilization case, the loop-gain factor $1/(1 + L_0)$, the state concept, coordinate invariance of eigenvalues and the two forms of the mass-spring-damper side by side. Every new derivation was checked step by step and every number, table and code block in the five entries was recomputed or re-run with Python 3.13.16 and NumPy 2.5; all agree with the text. The ten references exist and support what they are cited for. The build output is clean (no KaTeX errors, links resolve, no glued inline text), and `eos lint` and `eos syntax` report nothing. The remaining problems are wording: one sentence in the second entry that contradicts its own Section 2.3, an overview sentence that says a single equation cannot describe a mass on a spring, an imprecise statement about how many state-space models a transfer function has, and an opening of the fourth entry that no longer matches what the primer now does. None of them is a technical error in a derivation or a number. The series is ready once the four should-fix items are resolved.
Findings: 0 blocking, 4 should fix, 3 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Explain how feedback changes the stability and speed of a system's response, and how sensitive that response is to model errors and disturbances. | Entry 2, Sections 2.2, 2.4, 4.1-4.2; entry 5, Sections 1-3, 5.2 | Met. Speed, stabilization and sensitivity each have a derivation and a worked number; the general factor $1/(1 + L_0)$ is new and correct. |
| Describe a linear time-invariant system in both input-output form and state-space form. | Entry 1, Sections 3.1-3.4; entry 3, Sections 2-5; entry 4, Section 6 | Met. Entry 3, Section 5 now shows the same system in both forms; entry 4 derives $C(sI - A)^{-1}B + D$. |
| Relate the eigenvalues of a system matrix to stability and transient behavior. | Entry 3, Section 4; entry 4, Sections 2-7 | Met. |
| Recognize the assumptions and limits of a model before designing a controller around it. | Entry 1, Section 5; entry 2, Section 5; entry 3, Section 6; entry 4, Sections 5, 8; entry 5, Section 6 | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| T1 | Should fix | `src/content/blog/feedback-and-system-behavior.mdx` | Section 5 (line 167) | Technical accuracy | "larger gains better in every respect except the offset" contradicts Section 2.3, where a larger gain reduces the offset |
| S1 | Should fix | `src/content/series/foundations-of-control-systems.md` | Body (line 15) | Technical accuracy | "A single equation cannot describe a mass on a spring" is false; the third entry describes it by one second-order equation |
| T2 | Should fix | `src/content/blog/state-space-models-primer.mdx` | Section 5 (line 138) | Technical accuracy | "infinitely many answers, one for every choice of coordinates" omits realizations with extra (hidden) states, which the next bullet itself describes |
| S2 | Should fix | `src/content/blog/stability-and-eigenvalues.mdx` | Opening (line 15) | Cross-article references | Says the primer "ended with a single claim"; the revised primer states the test, proves one direction and promises the rest |
| T3 | Optional | `src/content/blog/state-space-models-primer.mdx` | Section 4.2 (line 103) | Technical accuracy | Negative damping gives a growing oscillation only when $c^2 < 4mk$ |
| T4 | Optional | `src/content/blog/state-space-models-primer.mdx` | Section 4.1 (line 87) | Technical accuracy | Eigenvector argument uses a complex $v$ for a real system; and "a sum of such terms" does not cover the repeated-eigenvalue case that entry 4 handles with $t^p e^{\lambda t}$ |
| F1 | Optional | `src/content/blog/state-feedback-controller-design.mdx` | References (line 288) | Factual consistency | Journal title spelled "Prozessdatenverarbeitung"; catalogues give "Prozess-Datenverarbeitung" |

### T1. "Better in every respect except the offset"
- **Where:** `src/content/blog/feedback-and-system-behavior.mdx:167`, section "5. What this model hides"
- **Text:** "For a stable plant ($a > 0$) this model makes every positive gain stable, and larger gains better in every respect except the offset."
- **Problem:** Section 2.3 (line 73) shows the offset $a\,r/(a + bk)$ "shrinks as $k$ grows", and the table at lines 77-82 shows it falling from 0.50 to 0.10. In this model a larger gain is better with respect to the offset too; what it cannot do is remove it. The sentence was added in wave 1 (`git diff e21dcc8`).
- **Recommended correction:** "For a stable plant ($a > 0$) this model makes every positive gain stable, and every increase of the gain an improvement: faster, less sensitive and with a smaller offset, although the offset never reaches zero."

### S1. "A single equation cannot describe a mass on a spring"
- **Where:** `src/content/series/foundations-of-control-systems.md:15`, body paragraph 2
- **Text:** "A single equation cannot describe a mass on a spring or a robot joint, so the third entry introduces state-space models and relates them to the transfer function."
- **Problem:** The third entry describes the mass-spring-damper by exactly one equation, $m\ddot{q} + c\dot{q} + kq = u$ (`state-space-models-primer.mdx:38`), and the first entry gives its transfer function. The second entry's closing says it correctly: "a single first-order equation cannot describe a mass on a spring" (`feedback-and-system-behavior.mdx:186`). The overview dropped "first-order".
- **Recommended correction:** "A single first-order equation cannot describe a mass on a spring or a robot joint, so the third entry introduces state-space models, which collect several first-order equations into one matrix equation, and relates them to the transfer function." Apply the same change to `src/content/series/vi/foundations-of-control-systems.md` when its body is retranslated.

### T2. How many state-space models a transfer function has
- **Where:** `src/content/blog/state-space-models-primer.mdx:138`, section "5. Input-output and state-space forms of the same system"
- **Text:** "**From transfer function to state space** there are infinitely many answers, one for every choice of coordinates in Section 3."
- **Problem:** Coordinate changes $z = Tx$ generate all models *with the smallest number of states* (minimal realizations are related by a similarity transformation; Chen, Ch. 7). Models with more states, containing a mode the input does not move or the output does not show, have the same transfer function and are not obtained by a coordinate change; the very next bullet (line 139) describes them. As written, the reader is told that coordinate choice accounts for every answer.
- **Recommended correction:** "**From transfer function to state space** there are infinitely many answers. Every choice of coordinates in Section 3 gives one, and adding states that the input does not move or the output does not show gives more, as the next point explains."

### S2. Opening of the fourth entry no longer matches the primer
- **Where:** `src/content/blog/stability-and-eigenvalues.mdx:15`, opening paragraph
- **Text:** "The [primer on state-space models](/blog/state-space-models-primer) ended with a single claim: the free response of $\dot{x} = Ax$ decays for every initial condition if and only if every eigenvalue of $A$ has a negative real part. This entry explains why that is true, ..."
- **Problem:** After wave 1 the primer does not end with this claim: it states it in Section 4.1, proves one direction there (line 87, "One direction of the reason fits in a line"), and its closing says "This entry stated the eigenvalue test and proved half of it. The next entry proves the rest" (line 162). The fourth entry's opening should pick up that thread.
- **Recommended correction:** "The [primer on state-space models](/blog/state-space-models-primer) stated that the free response of $\dot{x} = Ax$ decays for every initial condition if and only if every eigenvalue of $A$ has a negative real part, and proved that an eigenvalue with zero or positive real part prevents decay. This entry proves the other direction, explains what else the eigenvalues say about the response, and shows where they stop being enough."

### T3. Negative damping and oscillation
- **Where:** `src/content/blog/state-space-models-primer.mdx:103`, section "4.2 The characteristic polynomial"
- **Text:** "With negative damping ($c < 0$, a mechanism that feeds energy in rather than removing it), the real part becomes positive and the oscillation grows."
- **Problem:** True for $-2\sqrt{mk} < c < 0$; for $c \le -2\sqrt{mk}$ the roots are real and positive and the response grows without oscillating. Minor, since the sentence follows the complex-pair case.
- **Recommended correction:** "... the real part becomes positive and the response grows, as an oscillation of increasing amplitude while $c^2 < 4mk$."

### T4. Eigenvector argument for a real system
- **Where:** `src/content/blog/state-space-models-primer.mdx:87`, section "4.1 The free response"
- **Text:** "If $v$ is an eigenvector of $A$ with eigenvalue $\lambda$, ... then $x(t) = e^{\lambda t}v$ satisfies $\dot{x} = Ax$ ... The fourth entry proves the other direction by writing every free response as a sum of such terms."
- **Problem:** For a complex $\lambda$, $v$ is complex and $e^{\lambda t}v$ is not a physical state; the real initial condition $\operatorname{Re} v$ gives $\operatorname{Re}(e^{\lambda t}v)$, which also fails to decay, so the conclusion holds. Separately, entry 4 writes the free response as a sum of $e^{\lambda t}v$ terms only for diagonalizable $A$ (Section 2) and handles repeated eigenvalues with $t^p e^{\lambda t}$ terms (Section 4). Both are polish.
- **Recommended correction:** append to the eigenvector sentence "(for a complex $\lambda$, the real part of this solution, which starts at the real vector $\operatorname{Re} v$, does not decay either)", and change the last sentence to "The fourth entry proves the other direction by writing every free response as a sum of modes."

### F1. Ackermann journal title
- **Where:** `src/content/blog/state-feedback-controller-design.mdx:288`, References
- **Text:** "*Regelungstechnik und Prozessdatenverarbeitung*, vol. 20, pp. 297–300, 1972."
- **Problem:** Library catalogues list the journal as *Regelungstechnik und Prozess-Datenverarbeitung* (e.g. the EKT ESKEP and IBICT CCN serial records). Standards 7.3: titles keep the spelling of the original. The article exists (De Gruyter lists "Der Entwurf linearer Regelungssysteme im Zustandsraum", 1 December 1972, in volume 20 of the journal now titled *at – Automatisierungstechnik*); volume 20 and pages 297–300 agree with the Wikipedia reference list, which gives DOI 10.1524/auto.1972.20.112.297 (doi.org not fetched, so the DOI is not added here).
- **Recommended correction:** "*Regelungstechnik und Prozess-Datenverarbeitung*, vol. 20, pp. 297–300, 1972."

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| Open-loop and closed-loop control | `introduction-to-control-systems.mdx:26` | Same line, defined in bold | OK |
| Negative feedback, reference, error, disturbance, noise | `introduction-to-control-systems.mdx:36-39` | Same lines | OK |
| Linearity, superposition, time invariance, LTI | `introduction-to-control-systems.mdx:60` | Same line | OK (new in wave 1; was missing although entry 3 used "LTI") |
| Laplace transform | `introduction-to-control-systems.mdx:64` | Same line, with the derivative rule | OK |
| Transfer function, poles, zeros | `introduction-to-control-systems.mdx:78, 104` | Same lines; worked first-order example at :82-100 | OK |
| Time constant, steady-state (DC) gain | `introduction-to-control-systems.mdx:100` | Same line | OK |
| Step response, overshoot, 2% settling time | `introduction-to-control-systems.mdx:110-114` | Same lines | OK |
| Natural frequency, damping ratio, damped frequency, peak time | `introduction-to-control-systems.mdx:126-162` | Same lines | OK |
| Proportional feedback, integrator | `feedback-and-system-behavior.mdx:49, 73` | Same lines | OK |
| Explicit Euler method | `feedback-and-system-behavior.mdx:102` | Same line | OK |
| Loop gain $L_0$ | `feedback-and-system-behavior.mdx:155` | Same line | OK |
| State | `state-space-models-primer.mdx:27` | Same line, motivated at :25 | OK |
| $(A, B, C, D)$ form | `state-space-models-primer.mdx:55-69` | Same lines, with sizes | OK |
| Matrix exponential | `state-space-models-primer.mdx:85` | Same line (power series) | OK |
| Characteristic polynomial | `state-space-models-primer.mdx:91` | Same line | OK |
| Linearization | `state-space-models-primer.mdx:147` | Same line; Jacobian in `stability-and-eigenvalues.mdx:256-262` | OK |
| Mode, diagonalizable, Jordan form | `stability-and-eigenvalues.mdx:43-55, 151` | Same lines | OK |
| Asymptotic, marginal, BIBO stability | `stability-and-eigenvalues.mdx:25-29` | Same lines | OK |
| Controllability, observability | `stability-and-eigenvalues.mdx:223-224` | Same lines; test in `state-feedback-controller-design.mdx:67-73` | OK |
| Pole placement, Ackermann's formula, observer, separation principle, LQR | `state-feedback-controller-design.mdx:15, 107, 212, 218, 228` | Same lines | OK |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| SI units, time in s, frequencies and eigenvalues in rad/s | All entries | Overview :17; each opening | OK |
| 2% settling criterion | Entries 1, 4, 5 | Overview :17; entry 1 :20, :114 | OK |
| $j$ for the imaginary unit | Entries 1, 3, 4 | Overview :17; entry 1 :104; entry 4 :99 | OK |
| Python 3 standard library (entries 1-2), NumPy (3-5), "run with NumPy 2.5" (4-5) | Code blocks | Openings | OK; re-run with Python 3.13.16, NumPy 2.5 |
| Column vectors | Entry 3 onward | Entry 3 :21 | OK |
| Negative-feedback sign convention; $u = -Kx$ sign | Entries 1, 2, 5 | Entry 1 :39; entry 5 :35 | OK |
| Arbitrary consistent units for $x$, $u$, $r$ in entry 2 | Entry 2 | :21 | OK |
| Symbol reuse ($k$ stiffness/gain/sample index, $m$ mass/input count) | Entries 2-5 | Disambiguated locally (entry 3 :55, entry 4 :232) | OK |
| Zero-order hold in the sampled-gain figure | Entry 2 :169 | "holds $u$ constant between samples" | OK |

## Series design

**Purpose, audience and scope.** The overview (lines 13-17) now states the reader (calculus, basic linear algebra with eigenvalues, Python), the extra prerequisites (complex numbers, constant-coefficient linear ODEs), and what is introduced in the entries (Laplace transform, matrix exponential). Each entry's opening matches this. The four objectives begin with assessable verbs and each is met by named entries (table above).

**Sequence and rationale.** The overview gives the rationale explicitly (input-output first for the performance measures, state space for several variables and design). The order is right for the stated reader: each entry uses only what earlier entries established. One sentence of the rationale is technically wrong as worded (S1).

**Prerequisites and dependencies.** Nothing depends on a later entry. Forward references are promises that are kept: entry 1 :104 and entry 3 :137-139 (fourth entry, Section 6, derives $C(sI - A)^{-1}B + D$ and the hidden-mode example), entry 3 :85 and :87 (fourth entry, Section 2), entry 3 :147 (pendulum linearization, fourth entry Section 8), entry 3 :133 (fourth entry Section 3 reads $\omega_n$ and $\zeta$ from the eigenvalues). The one external dependency, the sampled-loop gain limit in entry 2 :169, matches `from-signal-processing-to-digital-control.mdx:98-105` ($\coth 0.05 = 20.02$).

**Notation and depth.** Symbols agree across entries ($s$, $G(s)$, $\omega_n$, $\zeta$, $\omega_d$, $(A, B, C, D)$, $T$); the mass-spring-damper values ($m = 1$, $c = 0.5$, $k = 4$) are the same in entries 3-5. Depth is now comparable: entries 1-3 have derivations and worked examples, entries 4-5 also have exercises. Entries 1-3 have no exercises; the standards make them optional for non-computational topics, and entry 1's Section 4.4 and entry 2's Section 3 carry the computation, so this is acceptable.

**Overview completeness.** Every entry is accounted for in the overview and nothing is promised that the entries do not deliver; shared conventions are stated once. The description (line 3) is unchanged and within limits.

## Series-level notes

- Cross-reference map (all checked against the target text): entry 2 → entry 1 Sections 1, 3, 3.3; entry 3 → entry 1 Section 3, entry 2 plant, entry 4 Sections 2, 6, 8; entry 4 → primer Section 5, entry 1 Section 4.2, Sections 6 and 9 internally; entry 5 → entry 1 Section 4.3, entry 4 Sections 4 and 5, Section 5.1 internally. All exist and say what is claimed, except the stale framing in S2.
- Fragment ids changed by numbering are already updated in the DSP article: the built `/tmp/claude-0/b2/blog/from-signal-processing-to-digital-control.html` links `#7-stability-in-discrete-time` and `#64-the-controller-runs-in-continuous-time`, and both ids exist.
- Structure is now uniform: numbered sections, numbered Summary with table and closing transition, `### References` in house format and alphabetical order in every entry.
- Vietnamese translations (`src/content/blog/vi/introduction-to-control-systems.mdx`, `feedback-and-system-behavior.mdx`, `state-space-models-primer.mdx`, `src/content/series/vi/foundations-of-control-systems.md`) still carry the pre-wave-1 bodies (only `updatedAt` changed since `e21dcc8`). Translations are outside this review; the item audits already mark them for update.

## Verification log

- `npm run build:local`: not run (brief: parallel reviewers). Used the post-wave-1 build `/tmp/claude-0/b2` (SITE_URL=https://acrr.asia), confirmed current by grepping new wave-1 sentences in the HTML.
- `node scripts/check-links.mjs /tmp/claude-0/b2`: "Checked 314 pages and 9667 internal references ... All internal links resolve."
- Rendering: `grep -c katex-error` = 0 in all five pages; one Mermaid diagram (entry 5) with `min-width:423px` (fits the column); no letter or punctuation glued to `<a `, `<strong>` or `<code` (KaTeX spans excluded).
- `npm run -s eos -- lint foundations-of-control-systems`: 6 files, 0 errors, 0 warnings, 0 suggestions.
- `npm run -s eos -- syntax <series file and five entries>`: "All files compile."
- Code: all eight Python blocks extracted and run with `python3 -I` (Python 3.13.16, NumPy 2.5). Output identical to the text: entry 1 (`overshoot: 16.3%, peak 1.1630 at 1.81 s` / `settling time: estimate 4.0 s, from the response 4.04 s`), entry 2 (`0.8`; `nominal 1.0 0.8`, `a = 1.2 0.833 0.769`, `d = 0.2 1.2 0.84`), entry 3 (`[-0.25+1.98431348j -0.25-1.98431348j]`), entry 4 (modal vs RK4 `[-0.223098 -1.43759169]` both; `2.513 0.683`; pendulum `[-0.25+3.12209865j ...]`, `[ 2.89205347+0.j -3.39205347+0.j]`), entry 5 (`[[12. 5.1]]`, `[-2.8+2.85657137j -2.8-2.85657137j]`).
- Recomputed, entry 1 (new): step response formula satisfies $\ddot{y} + 2\zeta\omega_n\dot{y} + \omega_n^2 y = \omega_n^2$ (residual 1e-12) with $y(0) = 0$; derivative formula matches central differences at three times; peak via $\sin(\pi + \varphi) = -\sqrt{1 - \zeta^2}$ derived by hand; $\ln 50 = 3.912$; $e^{-4} = 0.0183$; table by scanning the analytic response at 1e-4 s: $\zeta$ = 0.3/0.5/0.7/1.0 give overshoot 37.2/16.3/4.6/0%, settling 5.62/4.04/2.99/2.92 s, estimates 6.67/4.00/2.86/2.00 s; minimum settling 1.80 s at $\zeta = 0.78$, where the overshoot is 1.99%; poles $-1 \pm 1.732j$, $t_p = 1.814$ s; 4.0 vs 4.04 s differs by 0.99%.
- Recomputed, entry 2 (new): unstable case $a = -1$, $b = 1$, $k = 4$: Euler simulation settles at 1.3333 = 4/3, pole $-3$; relative sensitivity $(a/x_{ss})\,\partial x_{ss}/\partial a = -a/(a + bk)$ derived by hand; simulated shifts $-16.7\%$, $-3.9\%$ vs predicted $-20\%$, $-4\%$; disturbance $0.2/5 = 0.04$; sampled-loop limit $\coth 0.05 = 20.017$ (matches the DSP article's table); $u(0) = kr = 9r$.
- Recomputed, entry 3 (new): $\det(sI - TAT^{-1}) = \det(sI - A)$ and invariance of $C(sI - A)^{-1}B$ under $z = Tx$ checked by hand; $G(s) = 1/(s^2 + 0.5s + 4)$, $G(0) = 0.25$ m/N; imaginary part $\sqrt{15.75}/2 = 1.984$; series check of $e^{At}$ by hand.
- Recomputed, entry 4: $\zeta = 0.125$, overshoot 67.3%, estimate 16 s; $e^{\lambda T}$ at $T = 0.1$ s $= 0.956 \pm 0.192j$, magnitude 0.975; Euler magnitudes 0.995 ($T = 0.1$) and 1.323 ($T = 0.5$), bound 0.125 s; e-folding $1/2.892 = 0.346$ s; Exercise answers (8 s, $\omega_n = 5$, $\zeta = 0.6$; $c = 2.8$, $-1.4 \pm 1.428j$; $x_1 \to x_1(0) + x_2(0)$; $T < 0.59$ s).
- Recomputed, entry 5 (explicit Euler, 0.1 ms step): open loop overshoot 67.3%, settling 14.66 s; reference-gain design 4.6%, 1.49 s, peak force 16 N; integral design final 1.000 m, peaks 1.015 m (k = 4) and 1.006 m (k = 5), reaches 0.9 m at 1.00 s vs 0.66 s, settles 1.20 s; stiffness 5 N/m with $k_r = 16$ gives 0.941 m; $\omega_n = 8$ design settles 0.75 s, 0.90 s when limited to 10 N; table gains $[0, 2.3]$, $[12, 5.1]$, $[60, 10.7]$, estimates 2.86/1.43/0.71 s; augmented characteristic polynomial expanded by hand ($s^3 + (0.5 + k_2)s^2 + (4 + k_1)s + k_I$); observer $L = [19.5, 86.25]^\top$ by matching $s^2 + 20s + 100$; Exercise 1 ($K = [11, 7.5]$, $k_r = 15$), Exercise 3 (1.067 m).
- Wave-1 flags resolved: entry 1 Section 1.1 open-loop claim (correct: an open-loop controller does not change the plant's poles); Section 5 "a zero can add overshoot" (correct as stated); entry 2 Section 4.2 condition $a > 0$ (needed: $L_0$ and the factor require it); Section 2.4 "no constant open-loop input can hold" an unstable plant (correct: the equilibrium exists but is unstable); entry 3 time delay with infinitely many states (correct: $e^{-sT}$ is not rational).
- References verified (publisher pages and library catalogues via web search): Åström and Murray, 2nd ed., Princeton UP, 2021 (ISBN 9780691193984); Franklin, Powell and Emami-Naeini, 8th ed., Pearson, 2019 (Pearson catalogue, British Library record 2019); Ogata, 5th ed., Prentice Hall, 2010 (ISBN 9780136156734); Chen, 4th ed., Oxford UP, 2013 (ISBN 9780199959570); Khalil, 3rd ed., Prentice Hall, 2002 (ISBN 0130673897; author's MSU page); Trefethen and Embree, Princeton UP, 2005 (ISBN 9780691119465); Ackermann 1972 (De Gruyter volume 20 listing; see F1). Each supports the textbook material it is cited for (step-response specifications, state-space theory, Lyapunov's indirect method, non-normal transient growth, Ackermann's formula).
- Not verified: the issue designation and DOI of Ackermann (1972) (doi.org and the De Gruyter article page not reachable without authentication; the text cites neither, so nothing is asserted); the exact chapter/page in each textbook for each claim (books not accessible; the claims are standard textbook content).

## Resolution

- T1 (Should fix): fixed - sentence replaced with the reviewer's correction ("every increase of the gain an improvement: faster, less sensitive and with a smaller offset, although the offset never reaches zero"), `src/content/blog/feedback-and-system-behavior.mdx:167`.
- S1 (Should fix): fixed - "A single first-order equation cannot describe ..., which collect several first-order equations into one matrix equation", `src/content/series/foundations-of-control-systems.md:15`; the paragraph is also split before "The input-output view comes first" (new line 17). The Vietnamese overview needs the same change when its body is retranslated.
- T2 (Should fix): fixed - reviewer's wording: coordinate choices give one answer each, and adding states the input does not move or the output does not show gives more, `src/content/blog/state-space-models-primer.mdx:138`.
- S2 (Should fix): fixed - the opening now says the primer stated the test and proved that an eigenvalue with zero or positive real part prevents decay, and that this entry proves the other direction, `src/content/blog/stability-and-eigenvalues.mdx:15`.
- Optional applied: T3 (growing oscillation only while $c^2 < 4mk$, primer:103); T4 (added a sentence on complex $v$ and $\operatorname{Re} v$, and changed "a sum of such terms" to "a sum of modes", primer:87); F1 (journal title "Regelungstechnik und Prozess-Datenverarbeitung", state-feedback-controller-design:288). Optional not applied: none.

Resolved by the wave-1 author on 2026-10-14; awaiting the reviewer's resolution check.

## Resolution check

QA editor (final gate), 2026-10-15, against the working tree at `0d10069` and the build `/tmp/claude-0/b6` (confirmed current: the resolved sentences of T1, S1 and S2 are present in the built HTML).

- T1: confirmed. `feedback-and-system-behavior.mdx:167` now reads "every increase of the gain an improvement: faster, less sensitive and with a smaller offset, although the offset never reaches zero", consistent with Section 2.3 and the table at lines 77-82 (offset 0.50, 0.20, 0.10).
- S1: confirmed. `foundations-of-control-systems.md:15` reads "A single first-order equation cannot describe a mass on a spring or a robot joint, ... which collect several first-order equations into one matrix equation"; consistent with `state-space-models-primer.mdx:38` and `feedback-and-system-behavior.mdx:186`. The paragraph split (new line 17) changes no content. The Vietnamese overview is out of scope.
- T2: confirmed. `state-space-models-primer.mdx:138` now names both sources of non-uniqueness (coordinate changes and added hidden states) and leads into the next bullet.
- S2: confirmed. `stability-and-eigenvalues.mdx:15` now matches the primer: test stated, one direction proved (primer:87), the other proved here (Section 2 for diagonalizable $A$, Section 4 for repeated eigenvalues via the Jordan form).
- Optional T3, T4, F1: applied as described (primer:103, primer:87, state-feedback-controller-design:288). T4's added sentence precedes the sentence it qualifies ("does not decay either" comes before "that response does not decay"), so the paragraph reads slightly out of order; polish only, not reopened.

Independent checks: `eos lint foundations-of-control-systems` 6 files, 0 errors, 0 warnings; `eos syntax` "All files compile."; `check-links /tmp/claude-0/b6` 314 pages, all internal links resolve; `eos validate-site /tmp/claude-0/b6` reports no issue on the six English pages of this scope (all 29 issues are `/vi/` pages, out of scope); 0 `katex-error` in the five article pages. Recomputed with `python3 -I` (NumPy 2.5): every Python block in entries 2, 4 and 5 re-run with identical output; entry 1 table (37.2/16.3/4.6/0%, 5.62/4.04/2.99/2.92 s) and minimum settling 1.80 s at $\zeta = 0.78$ with 1.99% overshoot; entry 4 Euler magnitudes 0.995 and 1.323, $e^{\lambda T} = 0.956 \pm 0.192j$, bound 0.125 s; entry 5 open loop 67.3%/14.66 s, reference-gain design 1.49 s and 0.66 s to 0.9 m, integral design peaks 1.015/1.006 m, settles 1.20 s, 1.00 s to 0.9 m, stiffness 5 N/m gives 0.941 m, $\omega_n = 8$ design 0.75 s and 0.90 s with a 10 N limit; observer $L = [19.5, 86.25]^\top$ by hand. Cross-site claims checked against their targets: RK4 in `numerical-integration-notes`, Kalman filter in `sensing-and-state-estimation`, $k_{\max} = 20.02$ at $T = 0.1$ s in `from-signal-processing-to-digital-control`.
