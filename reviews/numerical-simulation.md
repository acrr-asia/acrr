# Series review: Numerical Simulation for Engineers

- Series: `numerical-simulation` (5 articles, status published, 0 planned entries)
- Reviewed commit: 4520df1
- Date: 2026-10-13

## Summary

The five entries form a coherent, well-ordered course from the model equations to verification and validation. The mathematics is correct, and all 17 Python blocks reproduce their printed output byte for byte (Python 3.13.16, numpy 2.5.3). Every worked number in the prose and the exercises was recomputed and is right, with two exceptions: an amplification factor in entry 2 and a band count in entry 3. The build, the type check and the link check pass, and the rendered pages are clean.

One finding is blocking. Entry 2 says that A-stability and L-stability are "the language of the numerical integration notes", but those notes never use these terms and leave implicit methods out of scope.

Seven findings are should-fix:
- Entry 3 explains the slow optimal-ω SOR iteration count with an inaccurate statement about its eigenvalues.
- Entry 2 quotes the FTCS factor for ξ = π instead of the shortest grid mode.
- Entry 5's definitions of verification and validation follow the standard wording too closely to count as paraphrases.
- Entry 5 uses $T$ for both the true value and the temperature.
- The series and entry 2 claim that every rate and stability limit is checked by experiment.
- Entry 3 writes $A = LU$ where it means $L U_{\!f}$.
- Entry 3 compares the fill-in count with the wrong band size.

The eight bibliographic records the author flagged are correct. The V&V 10/20 and AIAA attributions are accurate (E = S − D, the root-sum-square $u_{\text{val}}$, the GCI with factors of safety 1.25 and 3, and the four-tier hierarchy). The explanation of the leapfrog "fourth order at t = 1" result is exactly right: δ²/2 reproduces the measured errors to three digits. The hypothetical example is clearly labeled. Once the findings are corrected, the series is ready.

Findings: 1 blocking, 7 should fix, 8 optional.

## Resolution

The corrections were applied on 2026-10-13, at the owner's request. Line numbers in the findings below refer to the reviewed commit (4520df1), not to the corrected files.

- **F1 (blocking):** The A-/L-stability sentence in entry 2 §4.3 now reads "In terms of the stability regions of the numerical integration notes, the trapezoidal rule is **A-stable** (its stability region contains the whole left half of the complex $h\lambda$-plane, where the notes' $h$ is the time step $\Delta t$, so no decaying mode can grow) but not **L-stable** ...". The notes are now cited only for the concept they actually present.
- **F2:** The SOR sentence was replaced as recommended. Every eigenvalue has modulus $\omega - 1$, and $\omega - 1$ itself is a double, defective eigenvalue, so the error decays like $m\rho^m$. This was checked numerically (see F2).
- **F3:** The text now gives the factor of the shortest grid mode, $1 - 4(0.51)\sin^2(19\pi/40) \approx -1.027$, over 392 steps, with a growth of about $4\times10^4$ from $2.5\times10^{-3}$. This recomputes to the printed amplitude of 102.
- **F4:** The definitions in entry 5 §1.1 are introduced as "Paraphrased, their definitions are:" and rewritten in original wording, as recommended.
- **F5:** Entry 5 §4.4 now writes $-k\nabla^2 u = Q$ "for the temperature $u$", so $T$ is used only for the true value.
- **F6:** Changed as recommended in the series file, in entry 2's description and in entry 2's introduction. The Vietnamese series file was changed to match ("Loạt bài kiểm tra các tốc độ hội tụ và giới hạn ổn định chính của mình bằng các thí nghiệm Python ngắn."). None of the series' articles has a Vietnamese translation, so no other translation needed changes.
- **F7:** Entry 3 §2.1 now writes $A = LU_{\!f}$ and $PA = LU_{\!f}$.
- **F8:** Entry 3 §2.4 now says the 29,757 nonzeros fill 98 % of the 30,256 positions in the lower band.
- **Optional findings applied:** F9 (the parentheticals merged), F10 (the stability limit of explicit Euler for a fast-decaying mode), F11 (a zero or negative number under a square root), F12 (grids $N = 16, 32, \dots, 2048$), F13 ("by a factor of $10^8$"), F14 (George 1973 named at nested dissection; one sentence on Courant 1943 in entry 4 §5.2) and F15 (the note that $f$ is no longer the source term).
- **Not applied:** F16. The borderline case ν = 1 at ξ = π concerns a mode that a grid with fixed ends does not contain, so the text is not misleading as written.
- **Second pass.** All five entries were re-read in full after the corrections. Two further should-fix issues were found and corrected:
  - **F17 (second pass, should fix).** Entry 1 §4.3 wrote the method-of-lines system as $d\mathbf{U}/dt = A\mathbf{U}$. In §6.1 of the same entry, $A$ is the positive definite second-difference matrix, so the two $A$s have opposite signs. The text now reads "$d\mathbf{U}/dt = -\alpha A\mathbf{U}$ (plus boundary terms), where $A$ is the second-difference matrix written out in Section 6.1 (with $h = \Delta x$): a linear system of exactly the form treated in the state-space primer, with system matrix $-\alpha A$." The relation $\alpha\,\delta^2 U = -\alpha A U$ was checked from the definition of $A$.
  - **F18 (second pass, should fix).** Three more sentences overstated the experimental coverage in the same way as F6:
    - entry 4 line 17, "Each convergence rate stated is checked by a computation", is now "The main convergence rates are checked by computations";
    - entry 4 line 444, "Every convergence rate in this series so far was measured against a known exact solution", is now "Every discretization error in this series so far was measured against a known exact solution";
    - entry 5 line 15, "every claim about accuracy was checked against an exact solution", is now "the main claims about accuracy were checked against exact solutions".

  No defects introduced by the corrections were found. A final check of the changed passages found no blocking or should-fix issue.
- **Re-run results after all corrections:**
  - `npm run build:local` exited 0, with 0 errors, 0 warnings and 0 hints from `astro check`, and 81 pages indexed.
  - `npm run check:links` checked 214 pages and 6,081 internal references, all of which resolve.
  - On the five pages there are no `katex-error`s, no text glued to inline elements, and the Mermaid min-widths are 500, 315, 579 and 390 px.
  - All 17 Python blocks were re-run, and every output still matches byte for byte (no code was changed).

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Turn partial differential equations with boundary conditions into finite-dimensional problems. | Entry 1 §2–6; entry 4 §1–3 | Met. |
| Analyze explicit and implicit finite-difference schemes for accuracy and stability. | Entry 2 (whole) | Met: truncation error, von Neumann analysis, Lax equivalence and CFL, all measured. |
| Choose direct or iterative methods for the large linear systems that discretization produces. | Entry 3 (whole), especially §7 | Met. |
| Explain the finite element method from its variational form, and verify and validate a simulation. | Entry 4 (whole); entry 5 (whole) | Met. |

The English series file was respelled from British to American spelling ("discretising" to "discretizing", "Analyse" to "Analyze", "discretisation" to "discretization"). The meaning of the description and the objectives is unchanged. The Vietnamese objective now says "hiển (explicit)", which matches the glossary entry in `docs/translation-vi.md:215`. The new body sentence "Every convergence rate the series states is checked by a short Python experiment." overstates the coverage (F6).

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `src/content/blog/finite-differences-for-heat-and-waves.mdx` | §4.3 (line 258) | Cross-article references | A-stable and L-stable are attributed to "the language of the numerical integration notes", which never use them. |
| F2 | Should fix | `src/content/blog/solving-large-linear-systems.mdx` | §6 (line 324) | Technical accuracy | The SOR explanation "its eigenvalues coincide in pairs" is inaccurate. |
| F3 | Should fix | `src/content/blog/finite-differences-for-heat-and-waves.mdx` | §2.2 (line 133) | Technical accuracy | The shortest grid mode's factor is −1.027, not −1.04, and the run takes 392 steps. |
| F4 | Should fix | `src/content/blog/verifying-and-validating-a-simulation.mdx` | §1.1 (lines 23–26) | Fit with site rules | The V&V definitions are near-verbatim copies of the guides' wording, presented "in substance". |
| F5 | Should fix | `src/content/blog/verifying-and-validating-a-simulation.mdx` | §4.2 (line 227) vs §4.4 (line 247) | Terminology | $T$ is the true value in §4.2 and the temperature field in §4.4. |
| F6 | Should fix | `src/content/series/numerical-simulation.md`; `finite-differences-for-heat-and-waves.mdx` | line 13; lines 3, 17 | Factual consistency | The claims that every rate and every stability limit is checked by experiment are too strong. |
| F7 | Should fix | `src/content/blog/solving-large-linear-systems.mdx` | §2.1 (lines 61, 65) | Terminology | "$A = LU$" and "$PA = LU$" contradict the factor's own name, $U_{\!f}$. |
| F8 | Should fix | `src/content/blog/solving-large-linear-systems.mdx` | §2.4 (line 128) | Technical accuracy | The full lower band at $N = 32$ holds 30,256 entries, not $n(N-1) = 29{,}791$. |
| F9 | Optional | `finite-differences-for-heat-and-waves.mdx` | §2.2 (line 94) | Writing quality | The sentence defining ξ has two parentheticals in a row. |
| F10 | Optional | `finite-differences-for-heat-and-waves.mdx` | §1.2 (line 58) | Cross-article references | The notes do not discuss "what stiffness does" to Euler; they show the stability limit for a fast mode. |
| F11 | Optional | `solving-large-linear-systems.mdx` | §2.3 (line 96) | Technical accuracy | Cholesky can also fail on a zero, not only on a negative number. |
| F12 | Optional | `solving-large-linear-systems.mdx` | Exercise 4 (line 387) | Completeness | The grids behind "smallest error ... at N = 256" are not named. |
| F13 | Optional | `solving-large-linear-systems.mdx` | §4.2 table (line 204) | Writing quality | "reduce the error by $10^{-8}$" should be "by a factor of $10^8$". |
| F14 | Optional | `solving-large-linear-systems.mdx` line 423; `finite-element-method.mdx` line 453 | References | Writing quality | George (1973) and Courant (1943) are listed but never cited in the text. |
| F15 | Optional | `verifying-and-validating-a-simulation.mdx` | §3.1 (line 129) | Terminology | $f$ becomes the quantity of interest, right after serving as the source term in §2.3. |
| F16 | Optional | `finite-differences-for-heat-and-waves.mdx` | §6.2 (line 291) | Technical accuracy | At $\lvert b\rvert = 1$ the leapfrog quadratic has a double root, so ν = 1 is a borderline case. |

### F1. A-stable and L-stable attributed to the numerical integration notes
- **Where:** `src/content/blog/finite-differences-for-heat-and-waves.mdx:258`, section "4.3 What Crank–Nicolson does not damp"
- **Text:** "In the language of the [numerical integration notes](/blog/numerical-integration-notes), the trapezoidal rule is A-stable (stable for every decaying mode) but not **L-stable** (its factor does not tend to zero for infinitely fast decay), while backward Euler is both."
- **Problem:** `src/content/blog/numerical-integration-notes.mdx` treats only explicit Euler and RK4, introduces stability regions, and ends: "Stiff problems ... usually call for implicit methods, which are outside the scope of these notes." It never mentions the trapezoidal rule, backward Euler, A-stability or L-stability. The cross-reference is therefore false.
- **Recommended correction:** "In terms of the stability regions of the [numerical integration notes](/blog/numerical-integration-notes), the trapezoidal rule is **A-stable** (its stability region contains every decaying mode) but not **L-stable** (its factor does not tend to zero for infinitely fast decay), while backward Euler is both."

### F2. SOR at the optimal ω: the eigenvalue explanation
- **Where:** `src/content/blog/solving-large-linear-systems.mdx:324`, section "6. Measuring the Iteration Counts"
- **Text:** "at the optimal $\omega$ its iteration matrix is defective (its eigenvalues coincide in pairs without a full set of eigenvectors), so the error decays like $\rho^m$ multiplied by a factor that grows with $m$."
- **Problem:** The conclusion is right, but the stated mechanism is not. At $\omega_{\text{opt}}$ (Young's theory for consistently ordered matrices; red-black ordering is one), every eigenvalue of the SOR iteration matrix has modulus $\omega - 1$. Most of them are complex-conjugate pairs, which are distinct, not coinciding. Only the eigenvalue $\omega - 1$ itself, which comes from the extreme Jacobi eigenvalues $\pm\rho_J$, is a double eigenvalue with a single eigenvector (a 2×2 Jordan block). A numerical check on the red-black-ordered matrix with $N = 8$ confirms this: all eigenvalue moduli equal $\omega - 1 = 0.44646$; the eigenvalue $\omega - 1$ has algebraic multiplicity 2 and geometric multiplicity 1; and $\|M^k\|_2/\rho^k$ is 43, 87, 173 and 346 for k = 10, 20, 40, 80, that is, it grows linearly.
- **Recommended correction:** "...at the optimal $\omega$ every eigenvalue of its iteration matrix has the same modulus $\omega - 1$, and the eigenvalue $\omega - 1$ itself is double with only one eigenvector (the matrix is defective), so the error decays like $m\rho^m$ rather than $\rho^m$."

### F3. The FTCS factor of the shortest grid mode
- **Where:** `src/content/blog/finite-differences-for-heat-and-waves.mdx:133`, section "2.2 Stability by Fourier modes"
- **Text:** "the shortest mode is multiplied by $1 - 4(0.51) = -1.04$ at each of about 400 steps."
- **Problem:** With fixed ends and $N = 20$, the shortest grid mode is $k = 19$, $\xi = 19\pi/20$. Its factor is $1 - 4(0.51)\sin^2(19\pi/40) = -1.0274$; −1.04 is the bound at ξ = π, which is not a grid mode. The run takes 392 steps. The corrected figures explain the output exactly: the tent's discrete coefficient for mode 19 is $2.5\times10^{-3}$, and $1.0274^{392} = 4.06\times10^4$, so the amplitude is $2.5\times10^{-3} \times 4.06\times10^4 = 102$, matching the printed $1.022\times10^2$. With −1.04 the same estimate gives about $10^4$.
- **Recommended correction:** "...the shortest grid mode ($\xi = 19\pi/20$) is multiplied by $1 - 4(0.51)\sin^2(19\pi/40) \approx -1.027$ at each of 392 steps, a growth by a factor of about $4\times10^4$ from its initial amplitude of $2.5\times10^{-3}$."

### F4. The V&V definitions are near-verbatim
- **Where:** `src/content/blog/verifying-and-validating-a-simulation.mdx:23–26`, section "1.1 Verification and validation"
- **Text:** "**Verification** determines whether a computational model represents the underlying mathematical model and its solution accurately." / "**Validation** determines to what degree a model represents the real world accurately, from the perspective of its intended uses."
- **Problem:** Both sentences follow the published definitions in the AIAA guide and ASME V&V 10 almost word for word, with the clauses reordered. They are introduced with "In substance", so they are neither marked as quotations nor genuine paraphrases. The content-integrity rules require original writing, and the author asked for paraphrase. Quoting the exact text from memory would risk misquotation, so a real paraphrase with attribution is the safe fix.
- **Recommended correction:** Introduce the definitions as "Paraphrased, their definitions are:" and rewrite them as follows. Verification checks that the computational model (the code and the numbers it produces) reproduces the mathematical model it was built from, to a known accuracy. Validation estimates how closely the model reproduces the behavior of the real system, judged against the accuracy that its intended use requires.

### F5. $T$ means two things in Section 4
- **Where:** `src/content/blog/verifying-and-validating-a-simulation.mdx:227` and `:247`
- **Text:** "in terms of the true value $T$" (§4.2); "turns the steady heat equation $-k\nabla^2T = Q$" (§4.4)
- **Problem:** Two subsections apart, $T$ is first the true value of the compared quantity and then the temperature field. The rest of the series writes temperature as $u$ (entry 1 §2.1).
- **Recommended correction:** In §4.4, write "$-k\nabla^2 u = Q$ for the temperature $u$". Keep $T_s$ as the surface temperature.

### F6. "Every rate checked" overstates the coverage
- **Where:** `src/content/series/numerical-simulation.md:13`; `src/content/blog/finite-differences-for-heat-and-waves.mdx:3` and `:17`
- **Text:** "Every convergence rate the series states is checked by a short Python experiment."; "with every rate checked in Python"; "Every claimed order of accuracy and every stability limit is checked by a short experiment."
- **Problem:** Several stated results are not checked by any experiment: the two-dimensional limits ν ≤ 1/√2 and μ ≤ 1/4 (entry 2 §6.2), the θ-scheme limit μ ≤ 1/(2 − 4θ) (entry 2 §4.1), the $h$-independent multigrid and preconditioned-CG rates (entry 3 §4.3, §5.3), and the nested-dissection costs (entry 3 §2.4). The main rates are checked, but not every one.
- **Recommended correction:** Series file: "The series checks its main convergence rates and stability limits with short Python experiments." Apply the same change to `src/content/series/vi/numerical-simulation.md`. Entry 2 description: "with the main rates checked in Python". Entry 2 line 17: "The main orders of accuracy and stability limits are checked by short experiments."

### F7. $A = LU$ against $U_{\!f}$
- **Where:** `src/content/blog/solving-large-linear-systems.mdx:61`, `:65`
- **Text:** "turns this into a **factorization** $A = LU$, with $L$ lower triangular ... and $U_{\!f}$ upper triangular; the subscript distinguishes the factor from the solution vector"; "giving $PA = LU$"
- **Problem:** The sentence introduces $U_{\!f}$ to avoid a clash with the solution vector $\mathbf{U}$, but its own formula still writes $LU$.
- **Recommended correction:** Write $A = LU_{\!f}$ and $PA = LU_{\!f}$. "LU" as the name of the method can stay.

### F8. Comparison with the wrong band size
- **Where:** `src/content/blog/solving-large-linear-systems.mdx:128`, section "2.4 Fill-in"
- **Text:** "$29{,}757 \approx n(N - 1) = 29{,}791$: the band is essentially full."
- **Problem:** With half-bandwidth $b = 31$, the lower band including the diagonal holds $\sum_i (\min(i, b) + 1) = 30{,}256$ positions, not $n(N-1) = 961 \times 31$. The conclusion stands (98 % of the band is filled, and the 499 missing entries fell below the script's $10^{-14}$ relative threshold), but the comparison number is wrong.
- **Recommended correction:** "...and its 29,757 nonzeros fill 98 % of the 30,256 positions in the lower band: the band is essentially full."

### F9. Two parentheticals in a row
- **Where:** `finite-differences-for-heat-and-waves.mdx:94`
- **Text:** "$\xi$ is the mode's phase change per grid interval (for the $k$-th sine mode of Section 1.1, $\xi = k\pi\Delta x/L$) ($0 \le \xi \le \pi$ covers every mode the grid can represent)"
- **Recommended correction:** Merge them: "(for the $k$-th sine mode of Section 1.1, $\xi = k\pi\Delta x/L$; the range $0 \le \xi \le \pi$ covers every mode the grid can represent)".

### F10. "What stiffness does to explicit Euler"
- **Where:** `finite-differences-for-heat-and-waves.mdx:58`
- **Text:** "The [numerical integration notes](/blog/numerical-integration-notes) showed what stiffness does to explicit Euler: it is stable only if ..."
- **Recommended correction:** "The numerical integration notes showed the stability limit of explicit Euler for a fast-decaying mode: it is stable only if ..." (The notes mention stiffness only in their last sentence.)

### F11. Cholesky breakdown
- **Where:** `solving-large-linear-systems.mdx:96`
- **Text:** "(a square root of a negative number appears)"
- **Recommended correction:** "(a zero or negative number appears under a square root)", which also covers the semidefinite case.

### F12. Exercise 4 grids unspecified
- **Where:** `solving-large-linear-systems.mdx:387`
- **Text:** "gives its smallest error, $1.7\times10^{-5}$, at $N = 256$"
- **Recommended correction:** Name the grids: "on the grids $N = 16, 32, \dots, 2048$". The values were reproduced on those grids: 1.71e-5 at N = 256 and 3.62e-4 at N = 1024.

### F13. "Reduce the error by $10^{-8}$"
- **Where:** `solving-large-linear-systems.mdx:204`
- **Recommended correction:** "Iterations to reduce the error by a factor of $10^8$, for small $h$".

### F14. Uncited references
- **Where:** `solving-large-linear-systems.mdx:130`, `:423`; `finite-element-method.mdx:289`, `:453`
- **Problem:** The reference lists include George (1973) and Courant (1943), but the text never mentions either.
- **Recommended correction:** At "**Nested dissection**", add "(introduced by George in 1973 for regular meshes)". In §5.2 of the finite element entry, add one sentence: Courant's 1943 paper used piecewise-linear functions on a triangulation in this way, one of the mathematical precursors of the method.

### F15. $f$ reused
- **Where:** `verifying-and-validating-a-simulation.mdx:129`
- **Recommended correction:** "Let $f$ (no longer the source term of Section 2.3) be a scalar **quantity of interest** ...".

### F16. The ν = 1 borderline
- **Where:** `finite-differences-for-heat-and-waves.mdx:291`
- **Problem:** When the middle coefficient equals ±1, the two roots coincide, which would mean linear growth. This happens only at ν = 1 and ξ = π, and ξ = π is not a grid mode when both ends are fixed, so the experiments are unaffected.
- **Recommended correction:** None needed. A footnote-level remark could be added.

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| PDE | from-differential-equations-to-discrete-problems.mdx:15 | same line | Good |
| Discretization | from-...:17 | same line | Good |
| Heat, wave and Poisson equations | from-...:56–91 | derived from physics in §2 | Good |
| Elliptic/parabolic/hyperbolic | from-...:93 | §2.4 with the discriminant | Good |
| Dirichlet/Neumann/Robin | from-...:115 | §3.1 | Good |
| Well-posedness (Hadamard) | from-...:129 | §3.3 | Good |
| Order of accuracy | from-...:147 | §4.2 | Good |
| Method of lines | from-...:151 | §4.3 | Good |
| Truncation error, stencil | from-...:183 | §5.1 | Good |
| Unit roundoff | from-...:217 | same line, linked to the insight | Good |
| Consistency, stability, convergence | from-...:346–350 | §7 | Good |
| Stiffness | finite-differences-...:58 | same line | Good |
| von Neumann analysis, amplification factor | finite-differences-...:94 | §2.2 | Good |
| Mesh ratio μ, Courant number ν | finite-differences-...:81, :281 | at definition | Good |
| Lax equivalence theorem | finite-differences-...:262 | §5 | Good |
| CFL condition, domain of dependence | finite-differences-...:297 | §6.2 | Good |
| A-/L-stability | finite-differences-...:258 | defined inline (attribution wrong, F1) | See F1 |
| Sparse, banded, SPD | solving-...:45–47 | §1.1 | Good |
| Kronecker product | solving-...:43 | same line | Good |
| Flops | solving-...:55 | §1.2 | Good |
| LU, Cholesky, fill-in, nested dissection | solving-...:61–130 | §2 | Good |
| Condition number | solving-...:136 | §3.1 | Good |
| Spectral radius, stationary iteration | solving-...:202 | §4.2 | Good |
| Krylov subspace, energy norm | solving-...:226 | §5.1 | Good |
| Preconditioner | solving-...:251 | §5.3 | Good |
| Weak form, Sobolev space $H^1$ | finite-element-method.mdx:47–59 | §1.2 | Good |
| Essential/natural BCs | finite-element-...:60 | §1.2 | Good |
| Galerkin method, stiffness matrix | finite-element-...:85–93 | §2.1 | Good |
| $L^2$ norm, $H^1$ seminorm | finite-element-...:136–137 | §3.3 | Good |
| Code/solution verification, validation | verifying-...:25–36 | §1.1 | Good (wording F4) |
| MMS | from-...:229 (named), verifying-...:66 | §2.2 of entry 5 | Good |
| Richardson extrapolation, GCI | verifying-...:135–153 | §3.1–3.2 | Good |
| Standard uncertainty, coverage factor | verifying-...:233–239 | linked to the measurement entry §5.2 | Good |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| Python 3.13, numpy 2.5, binary64 | from-...:19; "Python 3 with numpy, double precision" in each entry | Yes | Reproduced with 3.13.16 / 2.5.3 |
| Sign convention $-\nabla^2 u = f$ | from-...:91 | Yes | Consistent across entries |
| SI units (m, s, K, W) | from-...:54, :58–61 | Yes | Consistent; °C and K in entry 5 §4.4 |
| Capital $U$ discrete, lowercase $u$ exact; superscript $n$ is an index | from-...:141 | Yes | Consistent |
| $h$ = mesh size; $\Delta t$ = the notes' $h$ | from-...:141–143 | Yes | Good |
| $h_c$, $h_e$, $q_L$, $Q$ | from-...:119; finite-element-...:23–29, :121 | Yes, locally | Good |
| $r$ = residual (entry 3), refinement ratio (entry 5) | solving-...:192; verifying-...:56, :129 | Yes, locally | Good |
| Red-black ordering for GS/SOR | solving-...:199, :283 | Yes | Good |
| GUM coverage factor 2 | verifying-...:239 | Yes | Consistent with the measurement entry §5.2 |
| Hypothetical validation data | verifying-...:17, :245–262 | Yes (heading, prose, code comment) | Good |

## Series-level notes

- **Cross-references.** Every "first/second/.../fifth entry" and "next entry" claim, every section anchor (`#43-the-method-of-lines`, `#22-banded-and-tridiagonal-systems`, `#52-checking-the-orders-and-where-rounding-takes-over`, `#51-solving-by-minimizing`, `#11-the-five-point-matrix`, `#41-why-iterate`, measurement `#52-evaluating-uncertainty`) and every forward promise was checked and is fulfilled. Examples: entry 1's "the third entry solves this problem on grids up to $N = 10^6$"; "the second entry computes the decay rate exactly for one mode"; and "the implicit scheme's 0.88" in entry 5. The one false claim is F1.
- **Consistency with the linked notes.** Numerical integration notes: $h$ as the time step, the Euler bound $|1 + h\lambda| \le 1$ and the meaning of order agree. The exceptions are F1 and F10. *What Makes a Simulation Trustworthy?*: the verification/validation distinction, the "perfectly solved wrong model" point and the two open questions quoted in entry 5 §5 all match. *Floating-Point Rounding in Long Simulations*: $u = 2^{-53}$, the single-precision $2^{-24}$ and the suggestion to compare runs that differ only in rounding all match.
- **Points flagged by the author.**
  - Spelling is American throughout, and the respelled series fields mean the same.
  - The V&V attributions are correct: $E = S - D$; $u_{\text{val}}$ as the root sum of squares of $u_{\text{num}}$, $u_{\text{input}}$ and $u_D$; the GCI in V&V 20; Roache's $F_s$ of 1.25 (three or more grids) and 3 (two grids); and the AIAA tiers (unit problems, benchmark cases, subsystems, complete system).
  - The definitions need real paraphrase (F4).
  - The SOR explanation is fixed in F2.
  - The leapfrog explanation is correct: the discrete solution is exactly $\cos(\tilde\omega t)\sin\pi x_j$, and $\delta^2/2$ with $\delta = (\tilde\omega - \pi)\cdot 1$ gives $2.94\times10^{-6}$, $1.83\times10^{-7}$ and $1.15\times10^{-8}$, the measured values.
  - Notation is defined locally (F5 and F15 are the exceptions).
  - The hypothetical example is labeled.
- **Structure.** The five entries are uniform: numbered sections, exercises with answers, a summary table and a reference list. The tags reuse existing site tags (`numerical-methods`, `simulation`, `linear algebra`). The frontmatter is consistent: one category, publishedAt 2026-10-13, and seriesOrder 1–5 with no gaps.

## Verification log

- `npm run build:local`: exit 0. `astro check` reported 0 errors, 0 warnings and 0 hints. Pagefind indexed 81 pages in 2 languages. The only warning is the expected localhost warning.
- `npm run check:links`: 214 pages, 6,081 internal references, all resolve.
- `dist/blog/<slug>.html` (all five pages): no `katex-error`. Mermaid min-widths are 500px, 315px, 579px and 390px, all ≤ 600px. No letter or punctuation mark is glued to `<a`, `<strong>`, `<code>` or `<em>`.
- Python blocks: all 17 blocks (3 + 4 + 5, counting the `thomas` definition, + 3 + 3) were re-run with `python3 -I`, Python 3.13.16 and numpy 2.5.3. Every printed output matches byte for byte. The entry 3 rounding block was run after the `thomas` definition, as the text says.
- Recomputed, all correct unless noted:
  - **Entry 1:**
    - 0.4207 and 0.09005;
    - √u_r = 1.05e-8 and u_r^{1/3} = 4.8e-6;
    - h²π²/12 = 0.00822 (h = 0.1) and 8.22e-7 (h = 10⁻³);
    - the error ratio of 292 ("about 300");
    - Exercises 1–5, including the coefficient −h²/3 and 3.21e-5 / 8.23e-7;
    - the discriminants and the 1000 s and 4000 s diffusion times.
  - **Entry 2:**
    - cot²(π/200) = 4,052;
    - the time constant L²/(απ²) = 101.3 s, the 0.05 s explicit limit, 20,000 steps and the eightfold cost;
    - the first-mode amplitude 2.915e-3;
    - FTCS shortest grid mode −1.0274 over 392 steps (F3);
    - CN factor −0.9607, with 0.9607¹⁰ = 0.670, 115 steps and BTCS 0.0099;
    - the θ-scheme limit;
    - leapfrog ν = 1.05: |G| = 1.839, 1.868 and 1.875; 48, 95 and 190 steps; the estimates 5.0e-4, 6e9 and 7e35;
    - the leapfrog t = 1 errors (above);
    - Exercises 1 and 3 (0.0182 s, 0.0045 s, 1.67e-5 s);
    - the dispersion relation, re-derived.
  - **Entry 3:**
    - 99³ = 970,299; 7.5 TB; 54 MB;
    - 2D nb² = 9.6e7 and 7.8 MB; 3D 9.3e13 and 76 GB;
    - κu_r = 4.5e-5 and u_r^{1/4} = 1.03e-4;
    - the Jacobi predictions 949, 3,816 and 15,283; SOR 47, 94 and 188; the CG bound 97, 194 and 389;
    - the table coefficients 3.73, 1.87 and 2.93;
    - the ratios 128 and 3.7e6 / 1,844;
    - Exercise 1 (768 MB, 7.8 MB, 0.39 MB) and Exercise 2 (61,152);
    - Exercise 4 in float32: 1.71e-5 at N = 256 and 3.62e-4 at N = 1024;
    - the full band of 30,256 positions (F8);
    - the SOR Jordan structure (F2).
  - **Entry 4:**
    - the quadratic element matrix [[7,−8,1],[−8,16,−8],[1,−8,7]]/(3h), recomputed with Gauss quadrature;
    - Exercise 2's element matrix and Exercise 3's numbers (7.9e-3, about 2,500 elements);
    - the six triangles of total area 3h² per interior node.
  - **Entry 5:**
    - the manufactured source f;
    - Fourier series truncation: the sums to 2,001 and to 4,001 differ by 1.4e-11;
    - the temperature rise of 39.28 K, with 1.18 K and 0.79 K from the conductivity and the heat generation;
    - u_input = 1.43 K, u_val = 1.52 K and the interval [−4.75, 1.31] K;
    - Exercises 1, 2 and 4 (2.00; 5.77e-4 = 0.058 %; 0.90 K, 1.03 K, [−3.78, 0.34] K) and Exercise 3 (ratio −2).
- References. Crossref could not be queried from this environment (proxy 403). A web search confirmed the title, journal and volume or issue of Roache 1994 (J. Fluids Eng.), George 1973 (SIAM J. Numer. Anal., doi 10.1137/0710032), Lax & Richtmyer 1956 (CPAM) and Courant 1943 (Bull. AMS 49, issue 1). The remaining details agree with the standard bibliographic records known to the reviewer:
  - Richardson 1911, Phil. Trans. A 210, 307–357;
  - Roache 1994, 116(3) 405–413;
  - George 1973, 10(2) 345–363;
  - Lax & Richtmyer, 9(2) 267–293;
  - CFL 1928, Math. Ann. 100, 32–74;
  - Crank & Nicolson 1947, 43(1) 50–67;
  - Hestenes & Stiefel 1952, J. Res. NBS 49(6) 409–436;
  - Courant 1943, 49(1) 1–23.

  The books and standards (LeVeque 2007; Morton & Mayers 2nd ed. 2005; Strikwerda 2nd ed. 2004; Strauss 2nd ed. 2008; Higham 2nd ed. 2002; Golub & Van Loan 4th ed. 2013; Trefethen & Bau 1997; Saad 2nd ed. 2003; Davis 2006; Briggs–Henson–McCormick 2nd ed. 2000; Strang & Fix 1973; Brenner & Scott 3rd ed. 2008; Johnson 1987; Hughes 1987/2000; Zienkiewicz–Taylor–Zhu 7th ed. 2013; ASME V&V 10-2006; V&V 20-2009; AIAA G-077-1998; Roache 1998; Oberkampf & Roy 2010; JCGM 100:2008; JCGM 101:2008; IEEE 754-2019) are real, with the titles, editions and publishers given. No reference was judged doubtful.
- Not verified:
  - The exact wording of the ASME and AIAA definitions. No copy of the guides was available, which is why F4 recommends a genuine paraphrase rather than a quotation.
  - Whether V&V 20 converts the GCI into $u_{\text{num}}$ with a divisor. The article treats GCI as $u_{\text{num}}$ "conservatively", which is safe under either reading.
