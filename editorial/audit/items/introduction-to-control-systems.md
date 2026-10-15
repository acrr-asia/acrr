<!-- audit: {"slug":"introduction-to-control-systems","type":"article","series":"foundations-of-control-systems","priority":"P1","before":{"purpose":3,"structure":2,"accuracy":3,"evidence":1,"language":3,"consistency":2,"publishing":2},"findings":{"blocking":1,"shouldFix":7,"optional":2}} -->
# Audit: Introduction to Control Systems

- Path: `src/content/blog/introduction-to-control-systems.mdx` · Route: `/blog/introduction-to-control-systems` · Type: article (series entry) · Series `foundations-of-control-systems`, entry 1 of 5 · Words: 669 (`eos status`, prose only)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: the opening says what the entry does ("sets out the vocabulary and the performance measures") but not what it assumes or which conventions (units, 2% criterion, Python) its examples use.
- structure 2: four unnumbered sections, no Summary, no References; the transfer function, the pole-response link and the second-order benchmark are compressed into one 177-word paragraph; no worked example beyond a four-line script; limits are one sentence.
- accuracy 3: every number checked is right (overshoot 16.3%, estimate 4.0 s); the settling-time approximation and the overshoot formula are stated without derivation or conditions beyond "this specific model".
- evidence 1: no references at all, and the two formulas the rest of the series relies on are neither derived nor cited.
- language 3: clear; one overlong paragraph (line 49); "Engineers usually state requirements" is generic.
- consistency 2: structure differs from entries 4-5 (numbering, Summary, References); `linear time-invariant` is used by entry 3 and never defined here although objective 2 starts here.
- publishing 2: description 183 characters (lint warning) and a list of topics rather than a sentence about what the reader learns; `series-sections` warnings for Summary and References.

## Priority

P1: foundational first entry; entries 2-5 and three articles outside the series (`pid-control-of-process-variables`, `from-signal-processing-to-digital-control`, `what-is-a-robot`) depend on its definitions.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Blocking | whole file | publishing | Required series sections Summary and References are missing (standards 6.2, items 6-7; `series-sections`) |
| D1 | Should fix | whole file | structure | Sections are unnumbered while the series standard requires numbered sections |
| D2 | Should fix | `:17` opening | purpose | Opening does not state prerequisites, conventions (SI units, 2% criterion) or the Python version |
| D3 | Should fix | `:49` | structure | One 177-word paragraph introduces the Laplace transform, the transfer function, poles, zeros and the pole-response link; no worked example of a transfer function |
| D4 | Should fix | `:57-67` | evidence | The overshoot formula and the settling-time approximation are given without derivation, peak time or the reason for the "4" |
| D5 | Should fix | `:73` | structure | Limits are one sentence; no statement of what linearity and time invariance mean although entry 3 relies on "linear time-invariant" |
| D6 | Should fix | `:36-43` | structure | The trade-off between speed and robustness is asserted ("tends to reduce robustness") without the mechanism |
| C1 | Should fix | `:3` | publishing | Description is 183 characters and a topic list, not one sentence saying what the reader learns |
| C2 | Optional | `:36` | language | "Engineers usually state requirements in terms of a few properties." Generic opener for a list |
| D7 | Optional | `:85-87` | structure | "Where this series goes next" duplicates the role of a Summary closing paragraph; an outlook of all four later entries belongs there |

### P1. Summary and References missing
- **Where:** whole file
- **Text:** last section is "## Where this series goes next"
- **Problem:** standards 6.2 items 6-7 require a Summary ending with a transition and a References list; `eos lint` reports `series-sections` twice.
- **Correction:** add a numbered Summary with a results table and a closing paragraph leading to the second entry, and `### References` with Åström and Murray, Franklin et al., Ogata (already cited in the series and verified by the 2026-10-13 series review).

### D1. Unnumbered sections
- **Where:** headings at `:19`, `:34`, `:45`, `:85`
- **Problem:** standards 5.4 and 6.2 require numbered sections in series entries so that cross-references can cite them.
- **Correction:** number all sections, with Summary numbered too, and subsections for the Laplace transform, poles and the benchmark.

### D2. Opening lacks assumptions
- **Where:** `:17`
- **Text:** "A control system is an arrangement of components that makes a physical process behave in a desired way. This introduction sets out the vocabulary and the performance measures that the rest of the series builds on."
- **Problem:** standards 6.2 item 1: the opening must state what the entry builds on and the conventions and versions its examples assume.
- **Correction:** add prerequisites (calculus, complex numbers, linear differential equations with constant coefficients), units (seconds, rad/s), the 2% criterion and "Python 3, standard library only".

### D3. Overloaded paragraph, no transfer-function example
- **Where:** `:49` (177 words, `paragraph-length` suggestion)
- **Text:** "To compare systems in this way, a linear system is often described only by how its input ... derives the transfer function from a state-space model."
- **Problem:** five concepts in one paragraph; no example shows a transfer function being obtained, so the reader never sees $Y(s) = G(s)U(s)$ used. Entry 2 then derives $b/(s+a)$ on its own.
- **Correction:** split into subsections (linear time-invariant systems; Laplace transform and transfer function, with a first-order worked example $K/(\tau s + 1)$ and its step response; poles and the shape of the response).

### D4. Formulas without reasoning
- **Where:** `:57-67`
- **Text:** "the unit-step response overshoots the final value by $M_p = \exp(...)$ ... a common approximation for the 2% settling time is $T_s \approx 4/(\zeta\omega_n)$"
- **Problem:** standards 2.2 "show the reasoning, not only the result". The exact step response, the peak time $\pi/\omega_d$ and the envelope argument ($e^{-\zeta\omega_n t} = 0.02$ gives $3.91/(\zeta\omega_n)$) are short and explain both formulas. Recomputed: peak 1.1630 at 1.814 s; exact 2% settling 4.04 s for $\zeta = 0.5$, $\omega_n = 2$.
- **Correction:** add the step response formula, the peak-time derivation and the envelope derivation of the "4", and compare estimate and exact value in the worked example.

### D5. Linearity and limits
- **Where:** `:49`, `:73`
- **Text:** "a linear system is often described"; "These formulas apply to this specific model."
- **Problem:** "linear" and "time-invariant" are never defined although objective 2 is about linear time-invariant systems and entry 3 uses the term; limits (nonlinearity, saturation, extra poles and zeros, zeros causing overshoot) are compressed into one sentence.
- **Correction:** define linearity (superposition) and time invariance; give a limits section.

### D6. Trade-off asserted
- **Where:** `:43`
- **Text:** "Pushing for fast tracking tends to reduce robustness, which is why design is more than choosing a large gain"
- **Problem:** no mechanism; the reader cannot see why.
- **Correction:** name the mechanisms (larger gains amplify measurement noise, demand larger actuator effort and, with delay, bring the loop closer to instability), and point to the second entry, where they are shown.

### C1. Description
- **Where:** `:3`
- **Text:** "The vocabulary of control: the feedback loop and its parts, the requirements a controller must meet, the transfer function, and how to read the step response of a second-order system."
- **Problem:** 183 characters (> 165); not a complete sentence.
- **Correction:** "Learn the parts of a feedback loop, what a controller must achieve, what a transfer function is, and how to read a second-order step response." (sentence form, within limits)

### C2. Generic list opener
- **Where:** `:36`
- **Correction:** state the requirements directly ("A controller is judged against four requirements.").

### D7. Outlook section
- **Where:** `:85-87`
- **Correction:** fold into the Summary's closing paragraph.

## Revision log (wave 1)

- **Structure:** sections numbered 1-6 with subsections; new opening paragraph on prerequisites and conventions (seconds, rad/s, 2% criterion, Python 3 standard library). New 1.1 (open-loop vs closed-loop control, with a heater/thermostat illustration), 3.1 (linearity, superposition, time invariance, LTI), 3.3 (worked first-order example $\dot{y} = -ay + bu$: $G(s) = b/(s + a)$, step response, time constant, 63%/98%, steady-state gain $G(0)$), 4.3 (derivation of the exact step response, peak time $\pi/\omega_d$, exact overshoot, envelope origin of $4/(\zeta\omega_n)$, table for $\zeta$ = 0.3, 0.5, 0.7, 1.0), 4.4 worked example, 5 (limits: extra poles/zeros, nonlinearity, what a step does not show), 6 Summary with table and closing transition (the former "Where this series goes next" folded in), References.
- **Prose:** the 177-word paragraph split into 3.2-3.4; trade-off in Section 2 now gives its mechanisms (noise amplification, actuator demand, delay); "negative feedback", "reference", "error", "disturbance", "measurement noise" defined in bold; "Engineers usually state requirements" replaced.
- **Metadata:** description rewritten (141 characters, one sentence); `updatedAt: 2026-10-13` added (and in the Vietnamese file).
- **References:** added Åström and Murray (2021), Franklin, Powell and Emami-Naeini (2019), Ogata (2010), all already cited in the series, verified by the 2026-10-13 series review and re-confirmed by web search (publisher catalogues).
- **Technical (new material, all recomputed with Python 3.13 / standard library):** the code block was extended; it now prints `overshoot: 16.3%, peak 1.1630 at 1.81 s` and `settling time: estimate 4.0 s, from the response 4.04 s` (run, output pasted). Table values recomputed by scanning the analytic step response (step 1e-4 s): 5.62, 4.04, 2.99, 2.92 s. Minimum 2% settling over $\zeta$ found at $\zeta \approx 0.78$ (1.80 s for $\omega_n = 2$). Derivative of the step response checked numerically against finite differences.
- Remaining warnings: none (lint 0/0/0).
- **Flags for independent review:** (technical) Section 4.3 derivation and the $\zeta$ table; Section 3.4 statement "a zero can add overshoot that the formula does not predict" (true for a left-half-plane zero near the poles; deliberately not elaborated); Section 1.1 claim that open loop "cannot become unstable through the controller". (fact-check) the three references support the material (standard textbook content on step-response specifications).
- **Vietnamese translation affected: yes.** Changes of meaning: new second opening paragraph; Section 1.1 (open/closed loop) is new; negative feedback, disturbances and noise defined in 1.2; Section 2 trade-off now explains mechanisms; Sections 3.1 (LTI), 3.3 (first-order example), 4.3 (derivations and $\zeta$ table), 4.4 (new code and printed output), 5 (limits) are new; 4.1 adds "final value" as a measure and first-order settling $3.9\tau$; 4.2 adds pole formula and damped frequency; the former final section became the Summary (table + closing paragraph) with References; description changed; all headings numbered.

## Independent review (wave 2)

- Reviewer: independent reviewer (fact-check, technical, series), commit `9232ed9`, 2026-10-13. Report: `reviews/foundations-of-control-systems.md`.
- Fact-check verdict: pass.
- Technical verdict: pass.
- Findings concerning this item: none.
- Not verified: none (three textbook references verified; chapter/page not checked).
