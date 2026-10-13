# Series review: Foundations of Control Systems

- Series: `foundations-of-control-systems` (5 articles, status published, 0 planned entries)
- Reviewed commit: 3a5ac0d
- Date: 2026-10-13

## Summary

Every worked number in the five entries was recomputed with Python and numpy and is correct. That covers overshoots, settling times, eigenvalues, the modal matrix exponential against RK4, the transient-growth peak, the discrete-time and Euler factors, the pendulum Jacobians, the controllability matrix, the Ackermann, reference, integral and observer gains, and every simulation table. The build, the KaTeX output and the link check are clean. The ten references are real works with correct authors, editions, publishers and years.

The main weakness is concept introduction in the three older, shorter entries. The series promises a treatment "from first principles", but entry 1 uses the Laplace variable $s$, the transfer function $G(s)$, poles and zeros without saying what they are. Entry 3 then relies on "a transfer function" and on the matrix exponential $e^{At}$. Both concepts are defined only in entry 4. The other problems are smaller:
- undefined performance measures in entry 1;
- "pole" and "integrator" used without explanation in entry 2;
- no definition of the state in entry 3;
- units not stated in entry 3;
- objective 1 (feedback changes stability) not shown where feedback is introduced;
- a 15 s vs 16 s settling-time mismatch;
- an "apply exactly" claim for an approximate formula;
- a code call in entry 5 that silently computes the wrong gain.

The series is not ready as published until the two blocking findings are fixed. All findings except F16 and F17 have now been fixed (see Resolution).

Findings: 2 blocking, 9 should fix, 6 optional.

## Resolution

Corrections were applied on 2026-10-13 on branch `review/foundations-of-control-systems`, in one commit together with this report. Line numbers in the findings refer to the reviewed commit 3a5ac0d, not to the corrected files.

- **F1** (blocking): applied in entry 1, the earliest sensible place. A new paragraph at the start of "Reading a step response" introduces the input-output view, the Laplace transform (definition, and differentiation becoming multiplication by $s$), $Y(s) = G(s)U(s)$ and the transfer function, poles and zeros, and how a pole's position shapes the response. It points to entry 4 for the derivation from a state-space model. The second-order model is now called a "benchmark" rather than a "reference model", because "reference" is the setpoint in this entry. The entry now says what that model describes, what $\omega_n$ (in rad/s) and $\zeta$ do, that $G(0) = 1$, and that the poles are a complex pair for $0 < \zeta < 1$. Entry 4's Laplace and transfer-function sentences now refer back to entry 1 ("as the first entry outlined", "As in the first entry", "the first entry introduced without deriving it").
- **F2** (blocking): entry 3 now defines $e^{At}$ by its power series and points to entry 4 for computing it. It also says that the eigenvalues are the roots of the characteristic polynomial $\det(sI - A)$. Entry 4 line 61 now reads "the matrix exponential the primer defined by its power series, here computed from the eigenvalues".
- **F3–F11** (should fix): applied as recommended. F3 adds definitions of step response, unit-step response, overshoot and 2% settling time, plus glosses for steady-state error and gain. F4 adds the transfer function $b/(s + a)$ and the pole shift. F5 explains why proportional action leaves an offset and what an integrator is. F6 defines the state. F7 states the SI units. F8 adds the $a < 0$ sentence. F9 gives both settling-time figures (14.7 s simulated, 16 s estimated). F10 rewords "apply exactly". F11 gives the explicit `np.roots([1, 9.6, 38.4, 64])` call.
- **F12–F15** (optional): applied. F12 notes that $m$ (count of inputs vs mass) and $k$ (sample index vs stiffness) have different meanings. F13 adds links to entries 2 and 3 in entry 1's outlook. F14 quantifies the slower rise of the integral design (0.9 m reached at about 1.0 s instead of 0.66 s) and its earlier 2% settling (about 1.2 s instead of 1.49 s); both are recomputed by simulation. F15 replaces entry 1's description and changes "This note" to "This entry" and "the state decays" to "$x$ decays" in entry 2.
- **Not applied:** F16 (entry 1's `publishedAt` is later than entries 2 and 3). Publication dates are part of the record, and changing them is the owner's decision, so they were left as they are. F17 (no Python version stated in entries 1 and 2) was also left: their code uses only the standard library and runs unchanged on any Python 3. Entry 3 now says that its code uses Python 3 and numpy.
- **Vietnamese translations:** every changed English sentence in entries 1–3 has a counterpart in `src/content/blog/vi/`, and each one received the equivalent change, following `docs/translation-vi.md` (Vietnamese term plus English term on first use, *bài* for entry, links to `/vi/blog/...` where a translation exists). The changes include entry 1's description, and the "Pole" table header in entry 2, which no longer repeats "(pole)" because the term is now introduced in the prose. Entries 4 and 5 have no translation. The series file and its translation were not changed.
- **Second pass:** a full re-read of all five entries after the corrections found two problems, both fixed. (a) The new F2 sentence said the eigenvalues "determine" $e^{At}$. That is not true for a matrix without a full set of eigenvectors, so it now says that entry 4 "shows how to compute it from the eigenvalues and eigenvectors of $A$". (b) The new F4 sentence stated $b/(s + a)$ without showing where it comes from, so a one-line derivation was added ($sX(s) = -aX(s) + bU(s)$ with $x(0) = 0$). The same two changes were made in the Vietnamese translations. A further pass over the changed passages found no blocking or should-fix problems.
- **Re-run results:**
  - `npm run build:local`: exit 0, with 0 errors, 0 warnings and 0 hints from `astro check`, and Pagefind indexing 78 pages in 2 languages. The only warning was the expected localhost warning for sitemap and RSS.
  - `npm run check:links`: 201 pages and 5622 internal references checked, all resolve.
  - `dist/` checks: no `katex-error` in the five English or three Vietnamese pages, no text glued to inline elements or to KaTeX spans, and the only Mermaid diagram (entry 5) has a min-width of 423px.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Explain how feedback changes the stability and speed of a system's response, and how sensitive that response is to model errors and disturbances. | Entry 2 (speed, sensitivity); entry 5 (moving eigenvalues); entry 4 (stability) | Speed and sensitivity are fully met in entry 2. That feedback changes *stability* appears only implicitly, through pole placement in entry 5, whose example is already stable. Entry 2 never shows feedback stabilizing an unstable plant (F8). |
| Describe a linear time-invariant system in both input-output form and state-space form. | Entry 1 (uses $G(s)$), entry 3 (state space), entry 4 §"Internal stability and input-output stability" (derives $G(s)$) | Met in substance, but the input-output form is used in entries 1 and 3 before it is introduced (F1). |
| Relate the eigenvalues of a system matrix to stability and transient behavior. | Entries 3 and 4 | Met, thoroughly (modes, damping, marginal and repeated cases, transient growth, discrete time, linearization). |
| Recognize the assumptions and limits of a model before designing a controller around it. | Entry 2 §"What this model hides", entry 3 §3, entry 4 §§ on marginal stability, transient growth and linearization, entry 5 §"What the design assumes" | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `src/content/blog/introduction-to-control-systems.mdx` | "Reading a step response" (lines 47–69) | Concept introduction | $s$, the transfer function $G(s)$, poles and zeros are used without being introduced; the definition comes only in entry 4 |
| F2 | Blocking | `src/content/blog/state-space-models-primer.mdx` | §2 (line 62) | Concept introduction / Logical flow | The matrix exponential $e^{At}$ is used without being defined; entry 4 is the first to say what it is |
| F3 | Should fix | `src/content/blog/introduction-to-control-systems.mdx` | §2–3 (lines 39, 43, 53, 59) | Concept introduction | Step response, overshoot, 2% settling time, steady-state error and gain are named but not defined in the entry that "sets out ... the performance measures" |
| F4 | Should fix | `src/content/blog/feedback-and-system-behavior.mdx` | §2 table (line 60) | Concept introduction | A "Pole" column appears without saying what a pole is or how it relates to the decay rate |
| F5 | Should fix | `src/content/blog/feedback-and-system-behavior.mdx` | §2 (line 56) | Concept introduction | "no integrator to hold the input at the required value" relies on a term not explained |
| F6 | Should fix | `src/content/blog/state-space-models-primer.mdx` | §1 (lines 18, 32) | Concept introduction | The entry introducing state-space models never says what the state of a system is |
| F7 | Should fix | `src/content/blog/state-space-models-primer.mdx` | §2 (line 79) | Stated versions and defaults | The numerical example ($m = 1$, $c = 0.5$, $k = 4$) gives no units, although the result is quoted in rad/s |
| F8 | Should fix | `src/content/blog/feedback-and-system-behavior.mdx` | §2 (line 50) | Completeness | Objective 1 promises that feedback changes stability; the entry on feedback only shows changes of speed |
| F9 | Should fix | `src/content/blog/state-feedback-controller-design.mdx` | intro (line 25) | Factual consistency | "takes about 15 s to settle" vs entry 4's "about $4/(\zeta\omega_n) = 16$ s to settle" |
| F10 | Should fix | `src/content/blog/state-feedback-controller-design.mdx` | §3 (line 103) | Technical accuracy | Claims the first entry's formulas "apply exactly", but $T_s \approx 4/(\zeta\omega_n)$ is an approximation (1.49 s simulated vs 1.43 s) |
| F11 | Should fix | `src/content/blog/state-feedback-controller-design.mdx` | §5.2 (line 186) | Technical accuracy | `acker(A_a, B_a, poles)` reuses the two-element `poles` and silently returns a wrong gain |
| F12 | Optional | `src/content/blog/state-space-models-primer.mdx`, `src/content/blog/stability-and-eigenvalues.mdx` | entry 3 line 48; entry 4 line 232 | Terminology | $m$ is the mass and the number of inputs; $k$ is the stiffness and the sample index |
| F13 | Optional | `src/content/blog/introduction-to-control-systems.mdx` | §4 (line 83) | Cross-article references | The outlook links the fourth and fifth entries but not the second and third |
| F14 | Optional | `src/content/blog/state-feedback-controller-design.mdx` | §5.2 (line 186) | Technical accuracy | "a slightly slower approach" is unquantified, and the integral design actually settles within 2% sooner |
| F15 | Optional | `src/content/blog/introduction-to-control-systems.mdx`, `src/content/blog/feedback-and-system-behavior.mdx` | entry 1 line 3; entry 2 lines 18, 28 | Writing quality | Entry 1's description repeats entry 2's title; entry 2 calls itself a "note" and speaks of "the state" before states are introduced |
| F16 | Optional | `src/content/blog/introduction-to-control-systems.mdx` | frontmatter (line 4) | Fit with site rules | `publishedAt: 2026-10-11` is later than entries 2 (2026-09-20) and 3 (2026-09-27), so date-ordered navigation shows the introduction as newer than what follows it |
| F17 | Optional | `src/content/blog/introduction-to-control-systems.mdx`, `src/content/blog/feedback-and-system-behavior.mdx`, `src/content/blog/state-space-models-primer.mdx` | code blocks | Stated versions and defaults | Entries 4 and 5 state "Python 3 and numpy (run with numpy 2.5)"; entries 1–3 state nothing |

### F1. Laplace variable, transfer function, poles and zeros used before they are introduced
- **Where:** `src/content/blog/introduction-to-control-systems.mdx:47-69`, section "Reading a step response"
- **Text:** "A standard reference model is the second-order system $G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$, with natural frequency $\omega_n$ and damping ratio $\zeta$." … "Real systems often have additional poles and zeros"
- **Problem:** The series description promises a path "from first principles", and this is the foundational entry. It writes $G(s)$ without saying what $s$ is, what $G$ maps, or that $G(s)$ is a transfer function. The phrase "transfer function" never appears in the entry. "Poles and zeros" are used without definition. Entry 3 opens with "A transfer function describes how one input affects one output" (`state-space-models-primer.mdx:18`), relying on this. The first actual definition is in entry 4, "The **Laplace transform** turns a signal $f(t)$ …" and "$G(s)$ is the **transfer function**" (`stability-and-eigenvalues.mdx:199-211`). So entries 1–3 depend on material from a later entry. "Reference model" also clashes with "reference" (the setpoint) defined twenty lines earlier.
- **Recommended correction:** At the start of "Reading a step response", add a short paragraph that introduces the input-output description:
  - the Laplace transform $F(s) = \int_0^\infty f(t)e^{-st}\,dt$, and differentiation becoming multiplication by $s$;
  - $Y(s) = G(s)U(s)$ for a system starting at rest, with $G(s)$ named the transfer function;
  - poles and zeros as the roots of the denominator and numerator, each pole $p$ contributing a term $e^{pt}$;
  - a pointer to the fourth entry for the derivation.

  Then rename the model "a standard benchmark", say what it describes (for example a driven mass-spring-damper), and state that $G(0) = 1$ and that the poles are a complex pair for $0 < \zeta < 1$.

### F2. Matrix exponential used before it is defined
- **Where:** `src/content/blog/state-space-models-primer.mdx:62`, section "Stability from the eigenvalues of A"
- **Text:** "With $u = 0$ the solution is $x(t) = e^{At}x(0)$."
- **Problem:** The exponential of a matrix is not part of "calculus and basic linear algebra" (the stated prerequisites, series file line 13). The entry does not define it. Entry 4 defines it later via the modal decomposition: "which is the matrix exponential the primer quoted" (`stability-and-eigenvalues.mdx:61`). The central object of the stability claim is used before it is introduced, in a series that promises first principles. The characteristic polynomial $\det(sI - A)$ is likewise not linked to the eigenvalues.
- **Recommended correction:** "…the solution is $x(t) = e^{At}x(0)$, where $e^{At}$ is the **matrix exponential**, defined by the same power series as the scalar exponential, $e^{At} = I + At + (At)^2/2! + \cdots$, with $I$ the identity matrix; the next entry shows how to compute it from the eigenvalues and eigenvectors of $A$." Also add: "The eigenvalues of $A$ are the roots of its **characteristic polynomial** $\det(sI - A)$." In entry 4 line 61, change "quoted" to "defined by its power series".

### F3. Performance measures named but not defined
- **Where:** `src/content/blog/introduction-to-control-systems.mdx:39`, `:43`, `:53`, `:59`
- **Text:** "with small steady-state error"; "more than choosing a large gain"; "its unit-step response overshoots the final value by"; "a common approximation for the 2% settling time is"
- **Problem:** The entry says it "sets out the vocabulary and the performance measures that the rest of the series builds on" (line 17), but it never defines step response, overshoot, 2% settling time, steady-state error or gain. Entries 4 and 5 rely on these measures (for example `state-feedback-controller-design.mdx:86-89`).
- **Recommended correction:** Before the model, add definitions of the step response and the unit-step response, of overshoot (as a fraction of the final value) and of the 2% settling time. Add glosses for steady-state error ("the difference between reference and output once the response has settled") and gain ("the factor by which the controller multiplies the error").

### F4. "Pole" in entry 2 without explanation
- **Where:** `src/content/blog/feedback-and-system-behavior.mdx:60`, table header
- **Text:** "| Controller | Pole | Time constant | …"
- **Problem:** The table lists poles −1, −2, −5, −10, but the text never says what a pole is or why it equals $-(a + bk)$. Entry 1 mentions poles only in passing (F1).
- **Recommended correction:** Add: "In the language of the first entry, the plant's transfer function from $u$ to $x$ is $b/(s + a)$, with a single **pole** at $s = -a$. The closed loop from $r$ to $x$ has the transfer function $bk/(s + a + bk)$, so feedback moves the pole to $s = -(a + bk)$, further to the left, where its term decays faster."

### F5. "Integrator" without explanation
- **Where:** `src/content/blog/feedback-and-system-behavior.mdx:56`
- **Text:** "because this plant has no integrator to hold the input at the required value."
- **Problem:** The reasoning depends on what an integrator does, which is not said, and "this plant" places the missing element in the plant rather than in the loop. Entry 5 later builds integral action on this sentence (`state-feedback-controller-design.mdx:163`).
- **Recommended correction:** "To hold $x = r$ the plant needs the input $u = (a/b)\,r$, but $u = k(r - x)$ is zero whenever the error is zero. Supplying the required input with zero error takes an **integrator**: an element whose output is the time integral of the error, so it can stay at a nonzero value once the error has vanished. This loop has none."

### F6. The state is never defined
- **Where:** `src/content/blog/state-space-models-primer.mdx:18`, `:32`
- **Text:** "A state-space model keeps track of the internal variables as well"; "choose the state variables $x_1 = q$ and $x_2 = \dot{q}$"
- **Problem:** The concept the entry is about is described only as "internal variables". The text never says what makes a set of variables a state, so the choice of $q$ and $\dot q$ looks arbitrary.
- **Recommended correction:** "The **state** of a system is a set of variables whose present values, together with the input from now on, determine its entire future behavior. For the mass, position and velocity are enough…"

### F7. Units of the numerical example not stated
- **Where:** `src/content/blog/state-space-models-primer.mdx:79` (code) and line 90
- **Text:** "m, c, k = 1.0, 0.5, 4.0"; "sets the oscillation frequency in radians per second"
- **Problem:** The result is given in rad/s, which is valid only with consistent SI units. Entries 4 and 5 state "$m = 1$ kg, $c = 0.5$ N·s/m and $k = 4$ N/m" for the same example.
- **Recommended correction:** Before the code: "For a numerical example take $m = 1$ kg, $c = 0.5$ N·s/m and $k = 4$ N/m, with time in seconds (the code uses Python 3 and numpy):"

### F8. Objective 1: feedback changing stability is not shown
- **Where:** `src/content/blog/feedback-and-system-behavior.mdx:50`
- **Text:** "First, the decay rate changed from $a$ to $a + bk$ … A larger gain makes the system respond faster."
- **Problem:** The first objective is "Explain how feedback changes the stability and speed of a system's response". The entry on feedback assumes $a > 0$ throughout. The only treatment of stability under feedback is entry 5's pole placement on an already stable plant.
- **Recommended correction:** Add: "The same formula shows that feedback can change stability itself: if the plant were unstable ($a < 0$, so that $x$ grows without input), any gain with $a + bk > 0$ would make the closed loop decay."

### F9. Open-loop settling time: 15 s vs 16 s
- **Where:** `src/content/blog/state-feedback-controller-design.mdx:25`
- **Text:** "it overshoots by about 67% and takes about 15 s to settle."
- **Problem:** Entry 4 says the same system would "take about $4/(\zeta\omega_n) = 16$ s to settle within 2%" (`stability-and-eigenvalues.mdx:125`). Entry 5's table gives 14.7 s from simulation (recomputed: 14.66 s). Both numbers are right, but they are presented as the same fact with different values.
- **Recommended correction:** "…takes about 15 s to settle within 2% (a simulation below gives 14.7 s; the estimate $4/(\zeta\omega_n)$ of the previous entry gives 16 s)."

### F10. "The first entry's formulas apply exactly"
- **Where:** `src/content/blog/state-feedback-controller-design.mdx:103`
- **Text:** "Because the closed loop is exactly the standard second-order model with no zeros, the first entry's formulas apply exactly to it, not only as an approximation."
- **Problem:** The overshoot formula is exact for the standard model. The settling-time formula is itself an approximation even for that model (entry 1: "a common approximation for the 2% settling time"). The entry's own table shows 1.49 s simulated against the 1.43 s estimate (recomputed: 1.495 s).
- **Recommended correction:** "Because the closed loop is exactly the standard second-order model of the first entry, with no further poles and no zeros, the overshoot formula holds exactly (4.6%), and the settling-time estimate is as good as it is for that model: the simulation below gives 1.49 s against the estimate of 1.43 s."

### F11. `acker` called with the wrong pole list
- **Where:** `src/content/blog/state-feedback-controller-design.mdx:186`
- **Text:** "`acker(A_a, B_a, poles)` returns the same values."
- **Problem:** In the code above, `poles` holds the two roots of $s^2 + 5.6s + 16$. With the 3-state $A_a$, `np.poly(poles)` has only three coefficients, so $\varphi(A_a)$ omits the constant term and the function returns a wrong gain without any error. Exercise 4 gives the correct call.
- **Recommended correction:** "`acker(A_a, B_a, np.roots([1, 9.6, 38.4, 64]))` returns the same values (Exercise 4 builds $A_a$ and $B_a$)."

### F12. Symbol reuse: $m$ and $k$
- **Where:** `src/content/blog/state-space-models-primer.mdx:26`, `:48`; `src/content/blog/stability-and-eigenvalues.mdx:232`
- **Text:** "A mass $m$ on a spring with stiffness $k$"; "Size for $n$ states, $m$ inputs, $p$ outputs"; "sampling instants $t = kT$"
- **Problem:** In each entry the same letter has two meanings a few paragraphs apart. Both uses are conventional, but the clash is avoidable.
- **Recommended correction:** Say "(here $m$ is a count of inputs, not the mass)" before the table, and "the integer $k = 0, 1, 2, \dots$ counting samples (in this section $k$ is not the stiffness)" in entry 4.

### F13. Outlook links only two of four entries
- **Where:** `src/content/blog/introduction-to-control-systems.mdx:83`
- **Text:** "The next article closes the loop … The article after it introduces state-space models … The [fourth entry](…) … the [fifth](…)"
- **Problem:** The links are inconsistent. The described targets are correct (entries 2 and 3 are as described).
- **Recommended correction:** Link "next article" to `/blog/feedback-and-system-behavior` and "article after it" to `/blog/state-space-models-primer`.

### F14. Integral action: "a slightly slower approach"
- **Where:** `src/content/blog/state-feedback-controller-design.mdx:186`
- **Text:** "The price is a third state to implement and a slightly slower approach"
- **Problem:** Recomputed with the entry's own simulation setup (explicit Euler, 0.1 ms):
  - With the integral design, the output first reaches 0.9 m at 0.997 s; with the reference gain, at 0.658 s. So the rise is about 50% slower, not "slightly".
  - Because the integral design overshoots less (1.5% vs 4.6%), it settles within 2% sooner, at 1.20 s vs 1.49 s.

  As written, a reader would expect it to settle later.
- **Recommended correction:** "…a slower rise, because the integrator has to build up the force that the reference gain previously supplied at once: in the nominal simulation the output first reaches 0.9 m after about 1.0 s, against 0.66 s with the reference gain. Because it overshoots less, the integral design still settles within 2% sooner, after about 1.2 s."

### F15. Descriptions and wording in the older entries
- **Where:** `src/content/blog/introduction-to-control-systems.mdx:3`; `src/content/blog/feedback-and-system-behavior.mdx:18`, `:28`
- **Text:** "An introductory overview of feedback and system behavior."; "This note uses the smallest model"; "With no input the state decays as $e^{-at}$"
- **Problem:** Entry 1's description repeats the title of entry 2 and does not describe entry 1. Entry 2 calls itself a "note", while the series speaks of "entries". It also speaks of "the state" one entry before states are introduced.
- **Recommended correction:** New description: "The vocabulary of control: the feedback loop and its parts, the requirements a controller must meet, the transfer function, and how to read the step response of a second-order system." Change "This note" to "This entry" and "the state decays" to "$x$ decays".

### F16. Entry 1 is dated after entries 2 and 3
- **Where:** `src/content/blog/introduction-to-control-systems.mdx:4`
- **Text:** "publishedAt: 2026-10-11"
- **Problem:** Entries 2 and 3 are dated 2026-09-20 and 2026-09-27, and entries 4 and 5 2026-10-13. The article pager (older/newer by date) and date-sorted lists therefore place the introduction after the entries it introduces. The date reflects when the former draft was published, so this is a record rather than an error.
- **Recommended correction:** None required. If the owner prefers date order to match reading order, add an `updatedAt` rather than rewriting `publishedAt`, or accept the order as it is.

### F17. Python version not stated in entries 1–3
- **Where:** code blocks in entries 1–3
- **Problem:** Entries 4 and 5 state "Python 3 and numpy (run with numpy 2.5)"; the earlier entries state nothing. Entries 1 and 2 use only the standard library (f-strings, so Python 3.6+). Entry 3 uses numpy.
- **Recommended correction:** State "Python 3 and numpy" before entry 3's code. Entries 1 and 2 may stay as they are.

## Concept introduction map

| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Closed loop, plant, sensor, controller, actuator, reference, error | `introduction-to-control-systems.mdx:21` | Same place | Good |
| Stability (BIBO, informal) | `introduction-to-control-systems.mdx:38` | Same place; formalized in `stability-and-eigenvalues.mdx:19-31` | Good |
| Steady-state error, gain | `introduction-to-control-systems.mdx:39`, `:43` | Not introduced | F3 |
| Step response, overshoot, settling time | `introduction-to-control-systems.mdx:53`, `:59` | Not introduced (formula only) | F3 |
| Laplace variable $s$, Laplace transform | `introduction-to-control-systems.mdx:50` | `stability-and-eigenvalues.mdx:199` | F1 (used three entries early) |
| Transfer function | `introduction-to-control-systems.mdx:50` (as $G(s)$); named at `state-space-models-primer.mdx:18` | `stability-and-eigenvalues.mdx:205` | F1 |
| Poles and zeros | `introduction-to-control-systems.mdx:69`; `feedback-and-system-behavior.mdx:60` | `stability-and-eigenvalues.mdx:211` | F1, F4 |
| Natural frequency, damping ratio | `introduction-to-control-systems.mdx:53` | Named only; geometric meaning in `stability-and-eigenvalues.mdx:113-117` | Covered by F1's correction |
| Time constant | `feedback-and-system-behavior.mdx:28` | Same place | Good |
| Integrator | `feedback-and-system-behavior.mdx:56` | Not introduced (entry 4 line 134 uses "(an integrator)" for $\lambda = 0$) | F5 |
| Explicit Euler | `feedback-and-system-behavior.mdx:75` | Named; defined by the code; numerical-integration notes linked from entry 4 | Acceptable |
| State, state variables | `feedback-and-system-behavior.mdx:28`; `state-space-models-primer.mdx:18` | Not defined | F6, F15 |
| LTI form $(A, B, C, D)$ | `state-space-models-primer.mdx:42` | Same place, with table | Good |
| Matrix exponential $e^{At}$ | `state-space-models-primer.mdx:62` | `stability-and-eigenvalues.mdx:55-61` | F2 |
| Eigenvalue, eigenvector | `introduction-to-control-systems.mdx:83` | Prerequisite (basic linear algebra, series file line 13) | Good |
| Characteristic polynomial | `state-space-models-primer.mdx:62` | Not related to eigenvalues explicitly | Covered by F2's correction |
| Modes, diagonalization, Jordan form | `stability-and-eigenvalues.mdx:43-55`, `:151` | Same places | Good |
| Asymptotic / marginal stability, BIBO, equilibrium | `stability-and-eigenvalues.mdx:23-29` | Same place | Good |
| Normal / non-normal matrices | `stability-and-eigenvalues.mdx:191` | Same place | Good |
| Controllability, observability | `stability-and-eigenvalues.mdx:223-224` | Same place; test in `state-feedback-controller-design.mdx:67-73` | Good |
| Discrete-time model, unit circle | `stability-and-eigenvalues.mdx:232-240` | Same place | Good |
| Jacobian, Lyapunov's indirect method | `stability-and-eigenvalues.mdx:258-262` | Same place | Good |
| State feedback, pole placement, reference gain, integral action, Ackermann's formula | `state-feedback-controller-design.mdx:15-186` | Same places | Good |
| Observer, separation principle, LQR, Kalman filter | `state-feedback-controller-design.mdx:210-226` | Same place (Kalman filter by link to the robotics series, which introduces it) | Good |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| SI units (kg, N/m, N·s/m, s, rad/s) | Entries 3–5 | Entries 4 (line 17) and 5 (line 17); not entry 3 | F7 |
| 2% settling criterion | Entries 1, 4, 5 | Yes | Good |
| Eigenvalues in rad/s (1/s for real) | Entry 4 line 17 | Yes | Good |
| Imaginary unit $j$ (engineering convention) | Entries 3–5 | Defined in entry 4 line 99 | Good |
| Sign convention $u = -Kx$ | Entry 5 line 35 | Yes, explained | Good |
| Zero initial conditions for transfer functions | Entry 4 line 199 | Yes | Good; entry 1 now states it too (F1) |
| Continuous vs discrete time; zero-order hold | Entry 4 lines 232–238, entry 5 line 222 | Yes | Good |
| Pendulum angle measured from hanging down, in radians | Entry 4 line 264 | Yes | Good |
| Python 3, numpy version | Entries 4, 5 (numpy 2.5; 2.5.3 installed here) | Yes; not in entries 1–3 | F17 |
| Explicit Euler with 0.1 ms step for simulated tables | Entry 5 line 159 | Yes | Good |

## Series-level notes

- **Cross-reference map.**
  - Entry 1 promises entries 2–5 (line 83), and each description matches its entry.
  - Entry 2 promises "the fourth on stability, and the fifth on what a state-feedback design assumes about the actuator, the measurements and the model" (line 128). Both promises are fulfilled (entry 5 §"What the design assumes").
  - Entry 3 says "next entry" (stability-and-eigenvalues) correctly.
  - Entry 4:
    - its back-references to the first, second and third entries ("bounded inputs … bounded outputs", "$\dot{x} = \lambda x$", "$(A, B, C, D)$") are accurate;
    - "The next entry gives a test for controllability" is fulfilled (entry 5 §2);
    - the "next entry uses this system as its example" claim is fulfilled.
  - Entry 5's references to "the previous entry" (eigenvalues, controllability and observability definitions, discrete-time model) and to the second entry's $u = k(r - x)$ and integrator remark are accurate.
  - The closing summary (line 280) correctly characterizes each entry.
  - Every link's text matches its target, including the external-series links to `numerical-integration-notes` (Euler and RK4, stability regions) and `sensing-and-state-estimation` (Kalman filter).
- **Terminology.** Usage is consistent across entries: American spelling ("behavior", "linearization", "stabilizable"), "damping ratio", "natural frequency", "eigenvalue", "closed loop", "reference". "Pole" and "eigenvalue" are used interchangeably for closed-loop locations in entry 5, which entry 4 line 211 justifies.
- **Structure.** Entries 1–3 are short notes without exercises, summary tables or references. Entries 4 and 5 are long, with exercises, a summary table and references. This difference was a deliberate expansion, and it is not a defect in itself. The concept-introduction gaps it exposed are F1–F7.
- **References.** All ten citations were checked:
  - Åström and Murray, *Feedback Systems*, 2nd ed., Princeton University Press, 2021;
  - Chen, *Linear System Theory and Design*, 4th ed., Oxford University Press, 2013;
  - Franklin, Powell and Emami-Naeini, *Feedback Control of Dynamic Systems*, 8th ed., Pearson, 2019;
  - Khalil, *Nonlinear Systems*, 3rd ed., Prentice Hall, 2002;
  - Trefethen and Embree, *Spectra and Pseudospectra*, Princeton University Press, 2005;
  - Ogata, *Modern Control Engineering*, 5th ed., Prentice Hall, 2010;
  - Ackermann, "Der Entwurf linearer Regelungssysteme im Zustandsraum", *Regelungstechnik und Prozessdatenverarbeitung* (today *at – Automatisierungstechnik*), vol. 20, pp. 297–300, 1972 (DOI 10.1524/auto.1972.20.112.297).

  All are real works with the stated authors, editions, publishers, volumes, pages and years.

## Verification log

- `npm run build:local` (reviewed commit): exit 0; `astro check` 0 errors, 0 warnings; Pagefind indexed 2 languages; only the expected localhost sitemap/RSS warning.
- `npm run check:links` (reviewed commit): 201 pages, 5618 internal references, all resolve.
- `dist/blog/<slug>.html` for the five entries (and the three Vietnamese translations): no `katex-error`; no letter or punctuation glued to `<strong>`, `<a>`, `<code>`, `<em>` or a KaTeX span; one Mermaid diagram (entry 5) with min-width 423px (below 600px).
- Recomputed with Python 3 and numpy 2.5.3:
  - **Entry 1:**
    - overshoot for $\zeta = 0.5$ is 16.3%, and the analytic step-response peak is 1.1630;
    - $T_s$ estimate 4.0 s (exact 2% settling 4.04 s);
    - the code prints "overshoot: 16.3%, settling time: 4.0 s".
  - **Entry 2:**
    - the Euler loop prints 0.8;
    - the time-constant/error table is correct for $k = 1, 4, 9$;
    - perturbation table 1.000/0.800, 0.833/0.769, 1.200/0.840 (shifts −0.167/−0.031, +0.200/+0.040);
    - "opposite sign" claim: with $d = -0.2$, open loop 0.800 (error 0.20) and closed loop 0.760 (error 0.24), so it is correct.
  - **Entry 3:** eigenvalues $-0.25 \pm 1.98431j$; $\sqrt{4mk - c^2}/(2m) = 1.98431$.
  - **Entry 4:**
    - modal $e^{A}x_0$ and RK4 both give $[-0.223098, -1.43759169]$;
    - $\zeta = 0.125$, overshoot 67.31%, $4/(\zeta\omega_n) = 16$ s;
    - transient-growth peak norm 2.513 at $t = 0.683$; $x_1$ peak 2.5 at $\ln 2$; $v_2 \propto [-10, 1]$;
    - $\mu = 0.9562 \pm 0.1923j$, $|\mu| = 0.9753$;
    - Euler magnitudes 0.99499 ($T = 0.1$) and 1.3229 ($T = 0.5$); bound 0.125 s;
    - pendulum eigenvalues $-0.25 \pm 3.12210j$ and $2.89205, -3.39205$; $1/2.892 = 0.346$ s;
    - $G(j0.7)$ from $C(sI - A)^{-1}B$ equals $1/(s^2 + 0.5s + 4)$;
    - exercises: $-1.4 \pm 1.428j$, $T < 0.590$ s, limit $x_1(0) + x_2(0)$, all correct.
  - **Entry 5:**
    - $\det\mathcal{C} = -1$; overshoot for $\zeta = 0.7$ is 4.60%; $\omega_n = 3.81$; $T_s = 1.4286$; roots $-2.8 \pm 2.85657j$;
    - `acker` gives $K = [12, 5.1]$, $k_r = 16$;
    - integral gains $[34.4, 9.1, 64]$ (augmented controllability rank 3);
    - $\omega_n = 2, 4, 8$ table: $K = [0, 2.3], [12, 5.1], [60, 10.7]$, $k_r = 4, 16, 64$, estimates 2.86/1.43/0.71 s;
    - observer $L = [19.5, 86.25]$; exercises: $K = [11, 7.5]$, $k_r = 15$, $16/15 = 1.067$, $16/17 = 0.941$.
  - **Entry 5 simulations** (explicit Euler, 0.1 ms):
    - open loop: overshoot 67.3%, settling 14.66 s;
    - state feedback: 4.60%, 1.495 s, largest force 16 N;
    - integral design: peaks 1.0152 m (nominal) and 1.0057 m (stiffness 5 N/m), both settling at 1.000 m;
    - $\omega_n = 8$: settling 0.747 s, and 0.905 s with a 10 N limit.
  - **F14:** first reaching 0.9 m at 0.997 s (integral) vs 0.658 s (reference gain); 2% settling 1.198 s vs 1.495 s.
- Not verified: the rendered appearance of the generated SVG figures (unchanged by this review and generated from the articles' formulas by `scripts/generate-diagrams.py`); the exact page layout of the cited references beyond bibliographic data.
