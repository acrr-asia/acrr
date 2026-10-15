<!-- audit: {"slug":"numerical-integration-notes","type":"article","series":null,"priority":"P1","before":{"purpose":2,"structure":2,"accuracy":4,"evidence":1,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":1,"shouldFix":6,"optional":2}} -->
# Audit: Notes on Numerical Integration of ODEs

- Path: `src/content/blog/numerical-integration-notes.mdx` · Route: `/blog/numerical-integration-notes` · Type: article (standalone research note) · No series · Words: 286 (eos status, prose only; about 680 with code and math)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: the opening says what is compared ("These notes compare two standard methods on the simplest useful test problem") but not whom it is for, what it builds on, or the Python version and arithmetic of the code (standards 6.1, 6.3).
- structure 2: the order claims are asserted, not derived ("The error made in one step is of order $h^2$ ... the global error is of order $h$"; "Its global error is of order $h^4$"); there is no section on limits (the only limit is the last sentence on stiff problems) and no ending: the note stops after "outside the scope of these notes". Concepts of local error, global error and order are used without definition.
- accuracy 4: every number recomputed (below); all correct.
- evidence 1: no references at all, although the note states the convergence orders of both methods and the RK4 stability boundary without derivation (standards 6.3: a short note may omit exercises but "not ... references for any claim that is not derived in the text").
- language 3: clear but terse; "the simplest useful test problem", "is only half the job" are vague; "fast decaying" needs a hyphen as a compound modifier.
- consistency 3: "Runge-Kutta" with a hyphen (lines 3, 29), while the insight on trustworthy simulation and the series use the en dash for two-person names (Gauss–Seidel, Crank–Nicolson); no pointer to the Numerical Simulation series, although six series entries link here as background.
- publishing 2: description is a fragment, not a sentence; no `updatedAt` will be needed only if the revision is cosmetic (it will not be).

Accuracy recomputed with Python 3.13 (scratch script): Euler errors at $t = 1$: 1.920e-2, 9.394e-3, 4.647e-3; RK4: 3.332e-7, 1.998e-8, 1.223e-9 (all match the table). Error ratios: Euler 2.04, 2.02; RK4 16.7, 16.3 (observed orders 1.03, 1.02 and 4.06, 4.03). Euler factor at $h\lambda = -2.5$: $-1.5$. RK4 stability boundary on the negative real axis: $-2.7853$ (bisection on $|R(x)| = 1$); on the imaginary axis $2\sqrt{2} \approx 2.828$; $R(-2.5) = 0.6484$.

## Priority

P1: other items depend on it. Six series entries cite it as the site's treatment of ODE time stepping and its stability limit (`from-differential-equations-to-discrete-problems` lines 19 and 352, `finite-differences-for-heat-and-waves` lines 58 and 258, `stability-and-eigenvalues` lines 65 and 244, `z-transform-poles-and-stability` line 230, `networked-automation-and-digital-twins` line 180). It is also the item furthest below the standalone-article standard (no references, no limits, no ending).

## Decision on overlap with the Numerical Simulation series

The brief suspected overlap with `from-differential-equations-to-discrete-problems`. Reading the series shows the opposite relation: the series treats partial differential equations, and for ODE time stepping, explicit Euler's stability limit and the stability regions it **refers to these notes** instead of repeating them (first entry line 19: "useful background for the time-stepping in the second entry"; line 352; second entry lines 58 and 258, which reuse "the stability regions of the numerical integration notes"). The second entry applies explicit and implicit Euler to the method-of-lines system and treats stiffness, backward Euler and Crank–Nicolson; nothing in the notes duplicates that. Decision: keep the note as a standalone article, bring it to the standalone standard (opening, defined concepts, derivation of the orders, limits, ending, references), and point to the series for stiffness and implicit methods instead of adding them. Keep every element the inbound links rely on: the factor $1 + h\lambda$, the condition $|1 + h\lambda| \le 1$, the fast-decaying example, the stability-region figure.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Blocking | whole file | evidence | No references for the stated orders and the RK4 stability boundary (standards 6.3, C7). |
| D1 | Should fix | lines 15 | purpose | Opening lacks reader, prerequisites, code version and arithmetic. |
| D2 | Should fix | lines 27, 46 | structure | Local error, global error and order used without definition; orders asserted, not derived. |
| D3 | Should fix | lines 86–98 | structure | No limits section and no ending; note stops on "outside the scope of these notes". |
| D4 | Should fix | lines 92, 98 | consistency | No pointer to the series that builds on the note (stiffness, implicit schemes, code verification). |
| P2 | Should fix | `:3` | publishing | Description is a fragment. |
| C1 | Should fix | lines 3, 29 | consistency | "Runge-Kutta" hyphen; house practice uses an en dash for two-person names. |
| D5 | Optional | line 84 | structure | Cost per step not considered: RK4 uses four evaluations, so the fair comparison is at equal work. |
| C2 | Optional | lines 15, 90 | language | "simplest useful test problem", "only half the job", "fast decaying". |

### P1. No references
- **Where:** whole article.
- **Problem:** the orders ($h$, $h^4$) and the RK4 boundary "about $-2.79$" are stated without derivation or citation (standards 6.3, 7.1).
- **Correction:** derive the order on the test equation (the RK4 amplification factor is the Taylor polynomial of $e^{h\lambda}$ to degree 4), and add verified textbooks: Butcher (3rd ed., Wiley, 2016), Hairer, Nørsett and Wanner (2nd rev. ed., Springer, 1993), and LeVeque (SIAM, 2007, already cited by the series).

### D1. Opening
- **Text:** "These notes compare two standard methods on the simplest useful test problem."
- **Correction:** add a paragraph on the reader (calculus, ODE with initial condition), the code (Python 3 standard library, run with Python 3.13, binary64 arithmetic), and the relation to the Numerical Simulation series.

### D2. Order asserted
- **Text:** "The error made in one step is of order $h^2$, and accumulated over a fixed time interval the global error is of order $h$." / "Its global error is of order $h^4$."
- **Correction:** define **local error**, **global error** and **order**; give the counting argument ($T/h$ steps of local error $O(h^{p+1})$); show on the test equation that Euler's factor matches $e^{h\lambda}$ to first order and RK4's to fourth.

### D3. No limits, no ending
- **Text:** "Stiff problems, where fast and slow dynamics coexist, usually call for implicit methods, which are outside the scope of these notes."
- **Correction:** a limits section (fixed step versus adaptive step control; systems and eigenvalues; nonlinear problems and linearization; stability is not accuracy, shown with the RK4 numbers at $h\lambda = -2.5$; stiffness with a pointer to the second series entry; rounding) and a short Summary.

### D4. Missing pointers
- **Correction:** link the observed-order test to code verification in `verifying-and-validating-a-simulation` (Section 2) and stiffness and implicit schemes to `finite-differences-for-heat-and-waves` (Sections 1.2 and 3).

### P2. Description
- **Text:** "Explicit Euler versus fourth-order Runge-Kutta on a test equation, and why accuracy and stability are separate questions."
- **Correction:** a full sentence saying what the reader learns (see revision log).

### C1. Runge–Kutta
- **Text:** "fourth-order Runge-Kutta", "Classical Runge-Kutta (RK4)".
- **Correction:** "Runge–Kutta" (en dash), as `what-makes-a-simulation-trustworthy` and the series' Gauss–Seidel, Crank–Nicolson.

### D5. Cost per step
- **Correction:** at 40 slope evaluations, Euler ($h = 0.025$) errs by $4.65\times10^{-3}$ and RK4 ($h = 0.1$) by $3.33\times10^{-7}$ (recomputed), about $10^4$ times less.

## Revision log (wave 1)

- Structure: kept as a standalone article (see "Decision on overlap"); numbered sections 1–6. Added an opening paragraph on reader, prerequisites (Taylor series; eigenvalues for Section 4 via the state-space primer), code version (Python 3 standard library, run with Python 3.13, binary64) and the relation to the Numerical Simulation series. New Section 2 defines local error, global error and order and derives the orders on the test equation (amplification factors as truncated Taylor series of $e^z$); the counting argument from local to global error. Section 4 defines absolute stability and the stability region, adds the imaginary axis (undamped oscillations) and systems (every eigenvalue), and shows that stability is not accuracy. New Section 5 "Limits of these notes" (fixed step vs embedded pairs; linearization; stiffness with a pointer to the second series entry; rounding with a pointer to the floating-point insight). New Section 6 Summary with a comparison table and a closing paragraph. Every original equation, the code block, the table and the figure are unchanged.
- Technical additions, each recomputed (Python 3.13): observed orders 1.03/1.02 (Euler) and 4.06/4.03 (RK4); equal-work comparison at 40 evaluations, $4.65\times10^{-3}$ vs $3.33\times10^{-7}$ (ratio about $1.4\times10^4$); Euler after 20 steps at $h\lambda = -2.5$: $1.5^{20} = 3325$; $e^{-50} = 1.93\times10^{-22}$; $R(-2.5) = 0.6484$, RK4 after 20 steps $1.73\times10^{-4}$; RK4 imaginary-axis limit $2\sqrt{2} = 2.828$ (bisection; agrees with the diagram's description); Euler energy factor $|1 + jh\omega|^2 = 1 + h^2\omega^2$ (derived). RK4 on the imaginary axis: $|R(jy)|^2 = 1 - y^6/72 + y^8/576 < 1$ for $0 < y^2 < 8$ (derived), hence "slight artificial damping".
- Prose: "simplest useful test problem" replaced by the reasons the test equation is the model problem; blockquote reworded ("is only half the job" → "answers only one of the two questions"); "fast decaying" → "fast-decaying"; ODE expanded.
- Terminology/style: "Runge-Kutta" → "Runge–Kutta" (en dash).
- Metadata: new description (159 characters, one sentence); `updatedAt: "2026-10-13"` added (publishedAt 2026-10-04; structure and technical content changed) here and in `src/content/blog/vi/numerical-integration-notes.mdx` (only that line).
- References: added Butcher (3rd ed., Wiley, 2016; checked against the publisher's listing, ISBN 978-1-119-12150-3), Hairer, Nørsett and Wanner (2nd rev. ed., Springer, 1993; checked against Springer and library catalog listings), LeVeque (SIAM, 2007; as already cited in the series). No URLs added.
- Cross-references: new links to `/blog/state-space-models-primer`, `/series/numerical-simulation`, `/blog/verifying-and-validating-a-simulation`, `/blog/stability-and-eigenvalues`, `/blog/finite-differences-for-heat-and-waves`, `/insights/floating-point-in-long-simulations` (no fragments). Inbound links have no fragments; content they rely on is kept.
- Remaining suggestion: `acronym-expansion` "SIAM" in the reference list (publisher name, as in the series' references; not expanded).
- Flags for independent review: (technical) Section 2 states that the orders carry over to smooth nonlinear $f$ without derivation, citing the textbooks; Section 5 statement on embedded Runge–Kutta pairs; the claim "for smooth problems and moderate accuracy targets, a higher-order method usually wins" (Section 3). (fact-check) the three references' bibliographic details; the Springer page could not be fetched (rate-limited), details are from search-result listings. (consistency, outside scope) `stability-and-eigenvalues.mdx` line 65 writes "Runge-Kutta" with a hyphen.
- Vietnamese translation affected: yes. The English now has an opening on prerequisites and code version, new Sections 2, 5 and 6 (definitions and derivation of order, limits, summary table, references), the observed-order and equal-work paragraphs, the imaginary-axis and "stability is not accuracy" paragraphs, a new description, and numbered headings.

## Independent review (wave 2)

- Report: `editorial/audit/review/standalone.md`
- Fact-check: pass
- Technical: fail
- Findings: T1, T2 (should fix); T4, T5 (optional)
- Not verified: none (code re-run; all numbers recomputed; three references verified).

## Revision log (wave 2 resolution)

- T1: Section 2 (line 67): the error-accumulation argument now requires errors to be amplified by at most a bounded factor, not "not amplified". It gives the bound $e^{|\lambda|T}$ on the test equation from $|R(z)| \le e^{|z|}$, and separates order (as $h \to 0$) from absolute stability (Section 4).
- T2: Section 4 (line 127): "slight artificial damping" replaced by the amplitude factor per step, recomputed: 0.99391 at $h\omega = 1$, 0.74536 at $h\omega = 2$.
- T4 (optional): line 117 now reads "does not grow if and only if $|1 + h\lambda| \le 1$ ...; it decays for $h < 2/|\lambda|$".
- T5 (optional): line 139: the stiffness example is now a system with a slow mode as well as the fast mode of Section 4.
- Lint: 0 errors, 0 warnings; one suggestion ("SIAM" is a publisher name). Syntax: compiles. No anchors link into this page.
- Vietnamese translation affected: yes. The meaning changes are the four sentences above: the order argument and its bound, the RK4 damping figures, the decay condition and the stiffness example. No copied field changed.
