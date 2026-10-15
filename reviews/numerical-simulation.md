# Series review: Numerical Simulation for Engineers

- Series: `numerical-simulation` (5 articles, status published, 0 planned entries)
- Reviewed commit: 9232ed9
- Date: 2026-10-13
- Review type: independent review (wave 2) of the wave-1 revision (`dfb4316`, audit logs in `editorial/audit/series/numerical-simulation.md` and `editorial/audit/items/`), combining fact-check (F), technical review (T) and series review (S). The reviewer did not write or revise any of the text.
- Content hash: sha256:e7297a51aac5170a355c6cbb645c4030088126c0ce2e2ac00b22be0f888c8eb6

## Summary

The series is accurate, well ordered and consistent, and the wave-1 revision left its substance intact. It was mostly copy and metadata work, plus one technical correction: the answer to Exercise 5 of entry 2. All 18 Python blocks reproduce their printed output byte for byte. Every worked number in the prose and the exercises was recomputed and is correct, including the new Exercise 5 wording. Every journal reference that was checked exists, with the stated venue, volume and pages. The build, links and rendering of the five pages are clean, and `eos lint` reports no errors or warnings.

One should-fix finding remains, a notation clash between entries. Entry 2 uses $T$ for $\text{tridiag}(1, -2, 1)$. Entry 3 uses $T$ for its negative, $\text{tridiag}(-1, 2, -1)$, and calls it "the tridiagonal matrix of the first entry", although entry 1 names that matrix $A = T/h^2$. Four optional points of polish follow. Once S1 is resolved, the series is ready.

Findings: 0 blocking, 1 should fix, 4 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Discretize a partial differential equation with its boundary and initial conditions into a finite algebraic problem, and state the order of accuracy of the result. | Entry 1 §2–7 (model equations, conditions, finite differences, the complete problem in §6, order and its measurement in §4.2, §6.1–6.2) | Met. |
| Analyze explicit and implicit finite-difference schemes for accuracy and stability, and choose a time step accordingly. | Entry 2 (whole): truncation error §2.1, von Neumann analysis §2.2, §3.2, §4.1, CFL §6.2, the scheme table §7, Exercises 1 and 3 | Met. |
| Choose a direct or an iterative method for the large sparse linear systems that discretization produces, and predict its cost. | Entry 3 (whole): operation counts §2, iteration counts §4.2, §5.2, measurements §6, decision guide §7, Exercises 1–2 | Met. |
| Derive the finite element method from the weak form of a boundary value problem, and explain how its error depends on mesh size and element degree. | Entry 4 §1–4 (weak form, Galerkin method, a priori estimates, measured rates for degrees 1 and 2) | Met. |
| Verify a simulation code and result by measuring the observed order and estimating the numerical error, and validate a model against measurements with stated uncertainties. | Entry 5 §2 (code verification with manufactured solutions), §3 (Richardson extrapolation, GCI, other numerical errors), §4 (validation with $E$ and $u_{\text{val}}$) | Met. This confirms the wave-1 flag on the new objective 5. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| S1 | Should fix | `src/content/blog/solving-large-linear-systems.mdx` (and `finite-differences-for-heat-and-waves.mdx`) | §1.1 (line 43), §3.1 (line 138), Exercise 3 (line 377); entry 2 §1.2 (lines 42–49) | Notation and depth / consistency | $T$ is $\text{tridiag}(1,-2,1)$ in entry 2 and $\text{tridiag}(-1,2,-1)$ in entry 3, and entry 3 calls it "the tridiagonal matrix of the first entry", where it is $h^2 A$. |
| S2 | Optional | `src/content/blog/verifying-and-validating-a-simulation.mdx` | §1.2 (line 50), §5 (line 313) | Terminology | "the insight note" survives twice; wave 1 changed the other mentions to "the insight". |
| T1 | Optional | `src/content/blog/solving-large-linear-systems.mdx` | §6 (line 329) | Technical accuracy / language | "to reduce the energy-norm error by $10^{-8}$" means a factor of $10^8$; the earlier F13 fix was made only in the §4.2 table. |
| T2 | Optional | `src/content/blog/solving-large-linear-systems.mdx` | §5.1 (line 230) | Technical accuracy | CG minimizes over $\mathbf{U}^{(0)} + \mathcal{K}_m$, not over the Krylov subspace itself, unless $\mathbf{U}^{(0)} = \mathbf{0}$. |
| T3 | Optional | `src/content/blog/finite-element-method.mdx` | §5.2 (line 292) | Notation | $\lvert T\rvert$ for a triangle's area adds a further meaning of $T$ in the series. |

### S1. The symbol $T$ has opposite signs in entries 2 and 3

- **Where:** `src/content/blog/solving-large-linear-systems.mdx:38–43`, section "1.1 The five-point matrix"; also `:138` (§3.1) and `:377` (Exercise 3). It conflicts with `src/content/blog/finite-differences-for-heat-and-waves.mdx:42–49` (§1.2).
- **Text:** Entry 3: "$T = \begin{bmatrix} 2 & -1 & & \\ -1 & 2 & \ddots & \\ \dots \end{bmatrix}$, where $T$ is the $(N-1)\times(N-1)$ tridiagonal matrix of the first entry"; "For the one-dimensional matrix $T/h^2$, the eigenvalues found in the second entry give $\kappa = \cot^2(\pi h/2)$"; Exercise 3: "Show that the first entry's tridiagonal matrix $T/h^2$". Entry 2: "$\frac{d\mathbf{U}}{dt} = \frac{\alpha}{\Delta x^2}\,T\,\mathbf{U}$, $T = \begin{bmatrix} -2 & 1 & & \\ 1 & -2 & \ddots & \\ \dots \end{bmatrix}$".
- **Problem:** Two consecutive entries define the same symbol for the same object with opposite signs, and neither says so. The overview promises shared conventions (`src/content/series/numerical-simulation.md:18`). Entry 1 never names a matrix $T$: its matrix is $A = \tfrac{1}{h^2}\,\text{tridiag}(-1, 2, -1)$ (`from-differential-equations-to-discrete-problems.mdx:238`). Entry 3's $T$ is therefore $h^2 A$, and entry 2's $T$ is $-h^2 A$. This matches entry 1 §4.3, $d\mathbf{U}/dt = -\alpha A\mathbf{U}$. In entry 3, "the eigenvalues found in the second entry" are the negative eigenvalues of entry 2's system matrix, so a reader who carries entry 2's $T$ into entry 3 gets the wrong sign for every eigenvalue and for the claim that $A$ is SPD. The magnitudes, and hence $\kappa$, are right.
- **Recommended correction (entry 3 only; entry 2 can stay as it is):**
  - Line 43: replace "where $T$ is the $(N-1)\times(N-1)$ tridiagonal matrix of the first entry" with "where $T$ is the $(N-1)\times(N-1)$ matrix $\text{tridiag}(-1, 2, -1)$, so that $T/h^2$ is the matrix $A$ of the first entry (Section 6.1); it is the negative of the matrix called $T$ in the second entry".
  - Line 138: replace "the eigenvalues found in the second entry give" with "the eigenvalues found in the second entry, with their sign reversed, give".
  - Line 377: replace "the first entry's tridiagonal matrix $T/h^2$" with "the tridiagonal matrix $T/h^2$ (the first entry's $A$)".

### S2. "The insight note"

- **Where:** `src/content/blog/verifying-and-validating-a-simulation.mdx:50` and `:313`
- **Text:** "and the insight note makes the same point"; "The open questions in the insight note on [trustworthy simulations]"
- **Problem:** Wave 1 replaced "The ACRR note" with "The insight" in all five entries. These two mentions keep "note", so the same kind of page is named in two ways within one entry. This is polish only.
- **Recommended correction:** "and the insight makes the same point"; "The open questions in the insight on [trustworthy simulations]".

### T1. "Reduce ... by $10^{-8}$"

- **Where:** `src/content/blog/solving-large-linear-systems.mdx:329`, section "6. Measuring the iteration counts"
- **Text:** "Its bound from Section 5.2 promises at most about 97, 194 and 389 iterations to reduce the energy-norm error by $10^{-8}$"
- **Problem:** Read literally, the error is reduced by a factor of $10^8$, not by $10^{-8}$. The §4.2 table was corrected to "by a factor of $10^8$" in the earlier review (its F13), but this sentence was not. The numbers are right: the smallest $m$ with $2q^m \le 10^{-8}$, where $q = (\sqrt\kappa - 1)/(\sqrt\kappa + 1)$, is 96.7, 194.4 and 389.2 (recomputed).
- **Recommended correction:** "... iterations to reduce the energy-norm error by a factor of $10^8$; the actual counts, measured with the residual criterion, are about a third of that."

### T2. The affine Krylov space

- **Where:** `src/content/blog/solving-large-linear-systems.mdx:230`, section "5.1 Solving by minimizing"
- **Text:** "$\mathbf{U}^{(m)}$ minimizes the error in the **energy norm** ... over all vectors in the **Krylov subspace** $\text{span}\{\mathbf{r}^{(0)}, \dots, A^{m-1}\mathbf{r}^{(0)}\}$, the best that any method built from $m$ matrix-vector products and that starting guess can do"
- **Problem:** With a nonzero starting guess, the iterate lies in $\mathbf{U}^{(0)} + \mathcal{K}_m$ and not in $\mathcal{K}_m$ (the standard statement of the CG optimality property, as in the entry's own references Saad 2003 and Trefethen and Bau 1997). The entry's examples all start from zero, and "that starting guess" hints at the shift, so this is a precision point only.
- **Recommended correction:** "... over all vectors $\mathbf{U}^{(0)} + \mathbf{w}$ with $\mathbf{w}$ in the **Krylov subspace** $\text{span}\{\dots\}$ ..."

### T3. $\lvert T\rvert$ for the triangle area

- **Where:** `src/content/blog/finite-element-method.mdx:292–295`
- **Text:** "$K^{e}_{ij} = k\,|T|\,\nabla N_i\cdot\nabla N_j$, where $|T|$ is the triangle's area."
- **Problem:** $T$ is already the tridiagonal matrix in entries 2 and 3 (see S1) and the true value in entry 5. The definition is local and correct, so this is optional.
- **Recommended correction:** Write $|e|$ for the area of element $e$: "$K^{e}_{ij} = k\,|e|\,\nabla N_i\cdot\nabla N_j$, where $|e|$ is the area of triangle $e$".

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| PDE, numerical simulation, discretization | from-differential-equations-to-discrete-problems.mdx:15–17 | Same lines, in bold | Good |
| Model, discretization, round-off and iteration errors | from-...:34–36 | §1.1 with a diagram | Good |
| Heat, wave and Poisson equations | from-...:56–91 | Derived from physics in §2.1–2.3 | Good |
| Elliptic, parabolic, hyperbolic | from-...:93–107 | §2.4 with the discriminant | Good |
| Dirichlet, Neumann, Robin; domain, boundary | from-...:115–119 | §3.1 | Good |
| Well-posedness | from-...:129 | §3.3 | Good |
| Grid, mesh, node, degrees of freedom, $h$ | from-...:135–143 | §4.1 | Good |
| Order of accuracy | from-...:147 | §4.2 | Good |
| Method of lines | from-...:151–157 | §4.3 | Good |
| Truncation error, stencil, $O(\cdot)$ | from-...:177–183 | §5.1 | Good |
| Unit roundoff $u_r$ | from-...:217 | Same line, linked to the insight | Good |
| Tridiagonal, symmetric, positive definite | from-...:248 | §6.1 | Good |
| Observed order | from-...:340 | §6.2 | Good |
| Consistency, stability, convergence | from-...:346–352 | §7 | Good |
| Stiffness | finite-differences-for-heat-and-waves.mdx:58 | Same line | Good |
| FTCS, BTCS, mesh ratio $\mu$ | finite-differences-...:74–81, :139 | At definition | Good |
| von Neumann analysis, amplification factor | finite-differences-...:94 | §2.2 | Good |
| Maximum principle | finite-differences-...:108 | §2.2 | Good |
| θ-scheme, Crank–Nicolson | finite-differences-...:165–173 | §4.1 | Good |
| A- and L-stability | finite-differences-...:258 | Defined inline; notes cited only for the stability regions | Good |
| Lax equivalence theorem | finite-differences-...:262 | §5 | Good |
| Courant number, CFL condition, domain of dependence | finite-differences-...:281, :297 | §6.1–6.2 (CFL also expanded in the opening, line 17) | Good |
| Numerical dispersion | finite-differences-...:342–348 | §6.4 | Good |
| Five-point stencil, Kronecker product | solving-large-linear-systems.mdx:35–43 | §1.1 | Good; the sign of $T$ is S1 |
| Sparse, banded, half-bandwidth, SPD | solving-...:45–47 | §1.1 | Good |
| Flops | solving-...:55 | §1.2 | Good |
| LU, pivoting, Thomas algorithm, Cholesky, fill-in, nested dissection | solving-...:61–130 | §2 | Good |
| Condition number, backward stability | solving-...:136 | §3.1 | Good |
| Iterative method, residual, iteration error | solving-...:190–192 | §4.1 | Good |
| Jacobi, Gauss–Seidel, SOR, red-black ordering, spectral radius | solving-...:196–202 | §4.2 | Good |
| Smoother, multigrid | solving-...:216–218 | §4.3 | Good |
| CG, $A$-conjugacy, energy norm, Krylov subspace | solving-...:230 | §5.1 | Good (T2 is precision only) |
| Preconditioner; GMRES and BiCGSTAB (named and expanded, then declared out of scope) | solving-...:255–257 | §5.3 | Good |
| Strong form, weak form, test function | finite-element-method.mdx:31–55 | §1.1–1.2 | Good |
| Sobolev space $H^1$, admissible functions | finite-element-...:59 | §1.2 | Good |
| Essential and natural conditions | finite-element-...:60 | §1.2 | Good |
| Energy functional, Rayleigh–Ritz | finite-element-...:67–73 | §1.3 | Good |
| Galerkin method, stiffness matrix, load vector | finite-element-...:85–93 | §2.1 | Good |
| Galerkin orthogonality, Céa's lemma | finite-element-...:97–109 | §2.2 | Good |
| Elements, hat and shape functions, assembly, Gauss–Legendre quadrature | finite-element-...:115–128 | §3.1–3.2 | Good |
| $L^2$ norm, $H^1$ seminorm | finite-element-...:136–137 | §3.3 | Good |
| A priori estimates, Aubin–Nitsche | finite-element-...:211–217 | §4.2 | Good |
| Isoparametric elements, mass matrix | finite-element-...:370 | §5.4 | Good |
| Verification, validation, code and solution verification | from-...:38 (first mention); verifying-and-validating-a-simulation.mdx:25–36 | Entry 1 §1.1 (one line), entry 5 §1.1 | Good |
| Calibration, prediction | verifying-...:38 | §1.1 | Good |
| Observed order, asymptotic range | verifying-...:56–62 | §2.1 | Good |
| Manufactured solutions | from-...:229 (named); verifying-...:66 | Entry 5 §2.2 | Good |
| Richardson extrapolation, GCI, factor of safety | verifying-...:129–153 | §3.1–3.2 | Good |
| Comparison error, validation uncertainty, standard uncertainty, coverage factor | verifying-...:221–239 | §4.2, linked to the measurement entry §5.2 | Good |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| Python 3 (run with 3.13), NumPy (run with 2.5), IEEE 754 binary64 | from-...:19; each entry's opening; series file line 18 | Yes | Reproduced with Python 3.13.16 and NumPy 2.5.3 |
| Sign convention $-\nabla^2 u = f$ | from-...:91; series file line 18 | Yes | Consistent in all entries |
| Capital $U$ discrete, lowercase $u$ exact; superscript $n$ an index | from-...:141; series file line 18 | Yes | Consistent |
| $h$ mesh size; $\Delta t$ is the notes' $h$ | from-...:141–143; finite-differences-...:258 | Yes | Consistent with the notes, which use $h$ for the time step |
| Name and sign of the 1D second-difference matrix | from-...:238 ($A$); finite-differences-...:44 ($T$, negative); solving-...:40 ($T$, positive) | Partly | Inconsistent between entries 2 and 3: S1 |
| SI units (m, s, K, W); °C in the validation example | from-...:54–61; verifying-...:247 | Yes | Consistent (°C is an SI derived unit; differences are in K) |
| Unit roundoff $u_r = 2^{-53}$ (binary64), $2^{-24}$ (binary32) | from-...:217; solving-...:136, :386 | Yes | Matches the floating-point insight |
| Red-black ordering for Gauss–Seidel and SOR | solving-...:199, :285 | Yes | Good |
| Unknowns numbered row by row; half-bandwidth $N - 1$ | solving-...:35, :46 | Yes | Good |
| GUM coverage factor 2 (about 95% if normal) | verifying-...:239 | Yes | Consistent with the measurement entry §5.2 |
| GCI used directly as $u_{\text{num}}$ | verifying-...:253, :268 | Yes, called conservative | Acceptable; see Not verified |
| Hypothetical validation data | verifying-...:17, :245–262 | Yes (heading, prose, code comment) | Labeled as required |

## Series design

**Purpose, audience and scope.** The overview names its reader: engineers and students who use simulation results. It names the prerequisites (calculus, basic linear algebra, ODEs at the level of the Foundations of Control Systems series), each linked, and points to the numerical integration notes as background. It says what the series covers, from the equations to a defensible result. Entry 1 §1.2 states the one deliberate exclusion, finite volumes ("Not covered in this series"). The five objectives each start with an assessable verb (Discretize, Analyze, Choose, Derive, Verify), and each is met by a named entry (table above). The reader's end state is stated implicitly through the objectives, which is enough.

**Sequence and rationale.** The overview's second paragraph says why the entries come in this order: each supplies what the next needs (equations and error vocabulary, then time stepping, the linear systems both produce, a second route to the same systems, and finally trust in the whole chain). The order is the right one for the stated reader. Entry 4 depends on entry 3 only for the SPD solver and the CG energy link, and entry 5 draws on all four. No move, split or merge would help.

**Prerequisites and dependencies.** Everything an entry relies on is either a stated prerequisite or introduced in an earlier entry that is cited by number and, where useful, by a section fragment. No entry depends on a later one. Forward pointers are promises that are kept: entry 1 points to entry 3 (rounding at $N = 10^6$) and to entry 5 (manufactured solutions), and entry 2 points to entry 5 (the measurement-time trap).

**Notation and depth.** The notation is consistent ($U/u$, $h$, $\Delta t$, $u_r$, $U_{\!f}$, $\xi$, $\mu$, $\nu$), with one exception: the sign and name of the tridiagonal matrix between entries 1–3 (S1). The depth is comparable across the entries: each has derivations, recomputed worked examples, runnable code with real output, five exercises with answers, a summary table and references.

**Overview completeness.** The description (165 characters) and the body match what the entries deliver. The conventions paragraph states the sign convention, the $U/u$ notation, SI units and the Python/NumPy setup once. The claim about experiments was qualified in the earlier review ("the main convergence rates and stability limits") and is accurate. The conventions paragraph could also fix the name of the second-difference matrix, which would resolve S1 at the series level. The entry-level correction proposed in S1 is sufficient.

## Series-level notes

- **Cross-references.** Every "first/second/.../fifth entry" and "next entry" mention matches its target. Every section citation was checked against the target's heading: entry 2 cites entry 1 Sections 5.1 and 6.2; entry 3 cites entry 1 Section 5.2; entry 4 cites entry 3 Sections 1.1 and 5.1; entry 5 cites entry 3 Section 4.1. All of them, and all the fragment links, resolve. They are `#43-the-method-of-lines`, `#22-banded-and-tridiagonal-systems`, `#52-checking-the-orders-and-where-rounding-takes-over`, `#51-solving-by-minimizing`, `#11-the-five-point-matrix`, `#41-why-iterate` and, in the sensor series, `#52-evaluating-uncertainty`.
- **Links outside the series.** The [numerical integration notes](/blog/numerical-integration-notes) were revised after the series (commit 9232ed9). They still support every claim the series makes about them. §4 shows the explicit Euler limit $|1 + h\lambda| \le 1$ for $\lambda = -50$ (entry 1 §7 and entry 2 §1.2). They present stability regions in the complex $h\lambda$-plane (entry 2 §4.3), and they use $h$ for the time step. They now also link forward to entries 2 and 5, and their description of entry 2 matches it. The insight *What Makes a Simulation Trustworthy?* contains the "perfectly solved wrong model" point and the two open questions that entry 5 §1.2 and §5 attribute to it. *Floating-Point Rounding in Long Simulations* writes the unit roundoff $u$ (as entry 1 says) and suggests comparing runs that differ only in rounding (entry 3 §3.2, entry 5 §3.4).
- **Terminology.** These terms are used consistently: "entry"; "time step" (open as a noun); "Crank–Nicolson", "Gauss–Seidel" and "Courant–Friedrichs–Lewy" with en dashes; "NumPy" in prose; American spelling; no space before %. The one leftover is "insight note" (S2).
- **Structure and front matter.** All five entries share the same structure: opening without a heading, numbered sections, numbered Exercises with answers, a numbered Summary with a table and a closing paragraph, and `### References`. The front matter is uniform: category "Mathematical Foundations", `publishedAt` 2026-10-13, `seriesOrder` 1–5 with no gaps, no `draft` or `example` flag. The descriptions are single sentences of 144–165 characters.
- **Content integrity.** Nothing is fabricated. The validation numbers in entry 5 §4.4 are labeled hypothetical in the heading, the prose and the code. The V&V definitions are paraphrases with attribution. No entry has a Vietnamese translation. The Vietnamese series file needs updating to match the wave-1 English overview, as recorded in the wave-1 audit; that is outside this review.

## Verification log

- Build: not run, by instruction (other reviewers run in parallel). The current full-site build in `/tmp/claude-0/b2` (built after wave 1 with `SITE_URL=https://acrr.asia`) was inspected instead. Its pages contain the wave-1 text (for example "Time discretization error" in entry 5 and "about 1.87 on the two finer" in entry 2).
- `node scripts/check-links.mjs /tmp/claude-0/b2`: checked 314 pages and 9,667 internal references; all internal links resolve.
- Rendering in `/tmp/claude-0/b2/blog/<slug>.html` and `/tmp/claude-0/b2/series/numerical-simulation.html`:
  - `katex-error` count is 0 on all six pages.
  - Mermaid min-widths are 500 px (entry 1), 315 px (entry 3), 579 px (entry 4) and 390 px (entry 5); entry 2 has no diagram. All are ≤ 600 px.
  - No letter or punctuation mark is glued to `<a `, `<strong>`, `<code>` or `<span class`.
- `npm run -s eos -- lint numerical-simulation`: 6 files, 0 errors, 0 warnings, 13 suggestions. These are `sentence-length` (46–65 words), `acronym-expansion` for "SIAM" and "JCGM" in reference lists, and `intensifiers` for "actually" at entry 1 line 36. All were justified in the wave-1 logs and are not re-reported.
- `npm run -s eos -- syntax <the six files>`: "All files compile."
- Code: all 18 Python blocks (3 + 4 + 5, counting the `thomas` definition, + 3 + 3) were extracted and run with `python3 -I` (Python 3.13.16, NumPy 2.5.3), each file's blocks in order in one namespace. All five outputs are identical to the printed `text` blocks (checked with `diff`).
- Recomputed (all correct):
  - **Entry 1:**
    - $\tfrac12\sin 1 = 0.42074$ and $\tfrac16\cos 1 = 0.090050$;
    - $\sqrt{u_r} = 1.05\times10^{-8}$ and $u_r^{1/3} = 4.8\times10^{-6}$;
    - $h^2\pi^2/12 = 8.2247\times10^{-3}$ ($h = 0.1$) and $8.2247\times10^{-7}$ ($h = 10^{-3}$);
    - the error ratio $1.69\times10^{-2}/5.78\times10^{-5} = 292$;
    - Exercise 1 ($-h^2/3$, by hand), Exercise 2 (discriminants 12 and 0), Exercise 3 ($3.214\times10^{-5}$, $8.227\times10^{-7}$), Exercise 4 (4000 s) and Exercise 5 (the flux balance $g - g_0 = -\int f$, re-derived);
    - the truncation and error relation $|e_j| \approx \tfrac{h^2\pi^2}{12}\sin\pi x_j$, re-derived.
  - **Entry 2:**
    - $\cot^2(\pi/200) = 4052$; $L^2/(\alpha\pi^2) = 101.3$ s; $\tfrac{4}{\pi^2}e^{-\pi^2/2} = 2.915\times10^{-3}$;
    - the FTCS shortest-mode factor $-1.02744$ over 392 steps, with growth $4.06\times10^4$; the tent's discrete mode-19 coefficient $2.52\times10^{-3}$ gives an amplitude of 102.2, against the printed $1.022\times10^2$;
    - the Crank–Nicolson factor $-0.96075$, with tenth power 0.670;
    - Exercise 1 (0.0182 s, 0.0045 s), Exercise 3 ($1.67\times10^{-5}$ s), Exercise 4 (112.8 and 115.0 steps; BTCS 0.00991);
    - the θ-scheme limit $\mu \le 1/(2 - 4\theta)$ and the dispersion relation, re-derived;
    - leapfrog at $t = 1$: $2.936\times10^{-6}$, $1.834\times10^{-7}$, $1.146\times10^{-8}$ (matching the text);
    - **new wave-1 Exercise 5:** root moduli 1.8391, 1.8678 and 1.8750 for $\xi = (N-1)\pi/N$; 48, 95 and 190 steps; estimates $5.03\times10^{-4}$, $5.98\times10^{9}$ and $7.38\times10^{35}$, whose ratios to the observed values are 13.2 and 9.7. The corrected wording ("1.84 ... about 1.87", "about $6\times10^9$ and $7\times10^{35}$", "within a factor of about 15") is correct.
  - **Entry 3:**
    - $99^3 = 970{,}299$; 7.53 TB; 54.3 MB;
    - the lower band of 30,256 positions (98.4% filled); the fill ratio 10.5;
    - $nb^2 = 9.6\times10^7$ and 7.84 MB in 2D; $9.32\times10^{13}$ and 76.1 GB in 3D;
    - $u_r^{1/4} = 1.03\times10^{-4}$, $\kappa u_r = 4.50\times10^{-5}$ and $8.22\times10^{-11}$ at $N = 10^5$;
    - the Jacobi predictions 949, 3,816 and 15,283; SOR 46.6, 93.7 and 187.6 (printed 47, 94, 188); the CG bound 96.7, 194.4 and 389.2; the coefficients 3.73, 1.87 and 2.93;
    - the ratio 128.2; the extrapolations $3.69\times10^6$ and 1,844;
    - Exercise 1 (768.5, 7.84 and 0.39 MB), Exercise 2 (61,152; 236) and Exercise 3 (re-derived);
    - Exercise 4 re-run in `float32` on $N = 16, \dots, 2048$: minimum $1.71\times10^{-5}$ at $N = 256$, and $3.62\times10^{-4}$ at $N = 1024$.
  - **Entry 4:**
    - the quadratic element matrix $\tfrac{1}{3h}[7, -8, 1; -8, 16, -8; 1, -8, 7]$ by Gauss quadrature;
    - the Exercise 2 triangle matrix $\tfrac12[2, -1, -1; -1, 1, 0; -1, 0, 1]$;
    - Exercise 3 ($7.9\times10^{-3}$; $N = 2526$);
    - six triangles of total area $3h^2$ per node; Exercises 1 and 4, re-derived.
  - **Entry 5:**
    - the manufactured source, checked by numerical differentiation (difference $3\times10^{-9}$);
    - the Fourier-series sums to 4001 and 2001, which differ by $1.4\times10^{-11}$;
    - $p$ from the rounded values: 1.991;
    - the temperature rise 39.284 K; the terms 1.179 K, 0.786 K and 0.0095 K; $u_{\text{input}} = 1.430$ K, $u_{\text{val}} = 1.515$ K and the interval $[-4.75, 1.31]$ K;
    - Exercise 1 (1.9985), Exercise 2 ($5.77\times10^{-4}$, 0.058% against an actual 0.0193%), Exercise 3 ($-2$) and Exercise 4 (0.393 K, 0.901 K, 1.030 K, $[-3.78, 0.34]$ K).
- Fact-check (web search, 2026-10-13):
  - Crank and Nicolson 1947, *Proc. Cambridge Philos. Soc.* 43(1) 50–67, confirmed. The journal was renamed *Mathematical Proceedings* only in 1975, so the cited name is the 1947 one.
  - Hestenes and Stiefel, *J. Res. NBS* 49(6) 409–436, 1952, confirmed (NIST record jresv49n6p409).
  - Courant, Friedrichs and Lewy, *Math. Ann.* 100, 32–74, 1928, confirmed (Encyclopedia of Mathematics).
  - Lax and Richtmyer, *CPAM* 9(2) 267–293, 1956, confirmed, and the stated theorem matches.
  - George, *SIAM J. Numer. Anal.* 10(2) 345–363, 1973, confirmed (epubs.siam.org, doi 10.1137/0710032).
  - Courant, *Bull. AMS* 49(1) 1–23, 1943, confirmed (ams.org and projecteuclid listings).
  - Richardson, *Phil. Trans. R. Soc. A* 210, 307–357: confirmed with year 1911 (Great Russian Encyclopedia bibliographic record); some sources give 1910.
  - Roache 1994, *J. Fluids Eng.*: title and journal confirmed.
  - ASME V&V 20-2009 and V&V 10-2006: titles confirmed (ASME and ANSI web store).
  - Strauss, 2nd ed., Wiley (ISBN 978-0-470-05456-7): confirmed.
  - Zienkiewicz, Taylor and Zhu, 7th ed., Butterworth-Heinemann, 2013: confirmed (British Library catalogue).
  - Trefethen and Bau III, SIAM 1997: confirmed in wave 1 by catalogue record.
  - The attributions match the sources: the V&V 20 comparison error $E = S - D$ and the RSS $u_{\text{val}}$, the GCI and Roache's $F_s$ of 1.25 and 3, the AIAA validation tiers, and GUM Supplement 1 = JCGM 101:2008. These agree with the earlier review's findings, and no contrary evidence was found.
- Not verified:
  - The issue number and pages of Roache 1994 (116(3), 405–413). The search confirmed the title and journal only; no record with pages was fetched.
  - The exact final word of Richardson's title ("stresses" in the article; "stress" in two secondary records). The original title page was not available.
  - The year printed in the books' imprints for these entries, which were not fetched in this pass (the earlier review recorded them as standard records): LeVeque 2007, Morton and Mayers 2005, Strikwerda 2004, Higham 2002, Golub and Van Loan 2013, Saad 2003, Davis 2006, Briggs–Henson–McCormick 2000, Brenner and Scott 2008, Hughes 1987/2000, Johnson 1987, Strang and Fix 1973, Oberkampf and Roy 2010, Roache 1998, AIAA G-077-1998, JCGM 100/101:2008, IEEE 754-2019. None is doubtful, but each is unverified in this pass.
  - Whether V&V 20 divides the GCI by a factor to obtain $u_{\text{num}}$. No copy of the standard was available. The text calls its choice conservative, which holds under either reading.
  - The exact wording of the ASME and AIAA definitions; the entry paraphrases them and does not quote.

## Resolution

- S1 (Should fix): fixed. Entry 3 §1.1 (`solving-large-linear-systems.mdx:43`) now defines $T = \text{tridiag}(-1, 2, -1)$, says that $T/h^2$ is the matrix $A$ of the first entry (linked to its §6.1, `#61-poisson-in-one-dimension`), and says that it is the negative of entry 2's $T$. The sentence was reordered so that the Kronecker product is defined first, and the reference is a link instead of "Section 6.1", which `section-reference` would read as a section of entry 3. §3.1 (`:138`) now reads "the eigenvalues found in the second entry, with their sign reversed, give", and Exercise 3 (`:377`) reads "the tridiagonal matrix $T/h^2$ (the first entry's $A$)". Entry 2 is unchanged, as recommended.
- Optional findings applied: S2 (`verifying-and-validating-a-simulation.mdx:50, :313`, "insight note" → "insight"), T1 (`solving-large-linear-systems.mdx:329`, "by a factor of $10^8$; the actual counts, measured with the residual criterion, ..."), T2 (`solving-large-linear-systems.mdx:230`, "over all vectors $\mathbf{U}^{(0)} + \mathbf{w}$ with $\mathbf{w}$ in the Krylov subspace") and T3 (`finite-element-method.mdx:292–295`, $|e|$ for the area of triangle $e$). Optional findings not applied: none.

Resolved by the wave-1 author on 2026-10-14; awaiting the reviewer's resolution check.

## Resolution check

QA editor (final gate), 2026-10-15, against the working tree at HEAD 0d10069 (the six files of this series have no uncommitted changes) and the build in `/tmp/claude-0/b6`.

- S1 (Should fix): confirmed. `solving-large-linear-systems.mdx:43` defines $T$ as $\text{tridiag}(-1, 2, -1)$, identifies $T/h^2$ with the first entry's $A$ (link to `#61-poisson-in-one-dimension`, which resolves) and says that $T$ is the negative of entry 2's $T$; `:138` reads "with their sign reversed"; `:377` reads "the tridiagonal matrix $T/h^2$ (the first entry's $A$)". Entry 2's $T$ (`finite-differences-for-heat-and-waves.mdx:44-49`) is $\text{tridiag}(1, -2, 1)$, so the statement is correct; entry 1's $A$ (`from-differential-equations-to-discrete-problems.mdx:238`) is $\tfrac{1}{h^2}\text{tridiag}(-1, 2, -1)$. The code of §3.1 and Exercise 3's value 2,593.2 are unchanged and re-run.
- S2 (Optional): confirmed applied (`verifying-and-validating-a-simulation.mdx:50, :313`).
- T1 (Optional): confirmed applied (`solving-large-linear-systems.mdx:329`, "by a factor of $10^8$"); the bound counts 96.7, 194.4, 389.2 hold.
- T2 (Optional): confirmed applied (`solving-large-linear-systems.mdx:230`, "$\mathbf{U}^{(0)} + \mathbf{w}$ with $\mathbf{w}$ in the Krylov subspace").
- T3 (Optional): confirmed applied (`finite-element-method.mdx:292-295`, $|e|$).

Checks: `eos lint numerical-simulation` 0 errors, 0 warnings, 13 suggestions (each justified in the wave-1 logs); `eos syntax` on the six files: all compile; `check-links /tmp/claude-0/b6`: 314 pages, 9,693 internal references, all resolve; `eos validate-site /tmp/claude-0/b6`: no issue on any English page; `katex-error` count 0 on all six pages; the build contains the S1 and T3 text. Code: all 18 Python blocks re-run independently with `python3 -I` (NumPy 2.5), each file's blocks in one namespace; the output of all five files matches the printed `text` blocks. Spot-checks: entry 2 Exercise 5 (moduli 1.8391, 1.8678, 1.8750; 48, 95, 190 steps; $5.0\times10^{-4}$, $6.0\times10^{9}$, $7.4\times10^{35}$), Exercise 4 (112.8 steps; BTCS 0.0099), the FTCS factor $-1.0274$ over 392 steps; entry 4 Exercise 3 ($N \approx 2{,}526$); entry 5 Exercise 4 ($[-3.78, 0.34]$ K). All agree with the text.

QA observations (optional, not blocking, recorded in the scores):

- Q1 (Optional, language): `solving-large-linear-systems.mdx:377` now has two parentheticals in a row, "$T/h^2$ (the first entry's $A$) (with $N - 1$ unknowns)", a side effect of the S1 fix. Suggest "the tridiagonal matrix $T/h^2$ with $N - 1$ unknowns (the first entry's $A$)".
- Q2 (Optional, language): `from-differential-equations-to-discrete-problems.mdx:19` "the time-stepping in the second entry" hyphenates the noun; the series uses "time stepping" as a noun (overview line 14).
- Q3 (Optional, structure): the closing paragraph of `verifying-and-validating-a-simulation.mdx:374` summarizes the chain but does not lead back to the series objectives or link the series page, as standards 6.2 item 6 asks of a last entry.

Verdict: no finding reopened. All six items pass the QA gate.

Build re-check: `/tmp/claude-0/b6` was deleted after the checks above, so they were run again on `/tmp/claude-0/b9`. That build has the same text for this series, plus later commits to other series (HEAD 3dd5a22; this series' files are unchanged). `check-links`: 314 pages, 9,695 internal references, all resolve. `eos validate-site`: no issue on any English page. `katex-error` count is 0 on every page of this series. The corrected text is present.
