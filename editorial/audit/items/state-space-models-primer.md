<!-- audit: {"slug":"state-space-models-primer","type":"article","series":"foundations-of-control-systems","priority":"P1","before":{"purpose":2,"structure":2,"accuracy":3,"evidence":1,"language":3,"consistency":2,"publishing":2},"findings":{"blocking":1,"shouldFix":6,"optional":2}} -->
# Audit: A Primer on State-Space Models

- Path: `src/content/blog/state-space-models-primer.mdx` · Route: `/blog/state-space-models-primer` · Type: article (series entry) · Series `foundations-of-control-systems`, entry 3 of 5 · Words: 470 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: "This primer builds a state-space model from a familiar example and shows what its main matrix tells you" says little; no prerequisites or conventions; "you" voice.
- structure 2: three unnumbered sections, no Summary or References; objective 2 (input-output and state-space form of the same system) is not shown in either direction here; the state concept is defined inside the derivation paragraph; the eigenvalue test is stated without any reason; the limits are mixed into a section titled "Why it is worth the extra notation".
- accuracy 3: equations and the numerical example are right (eigenvalues −0.25 ± 1.98431j recomputed). "For positive $m$, $c$ and $k$ both roots have negative real part" is correct.
- evidence 1: no references.
- language 3: clear; second person ("tells you").
- consistency 2: does not connect the first-order plant of entry 2 to the state-space form; non-uniqueness of the state (used implicitly by entry 4's change of variables $z = V^{-1}x$) is not mentioned.
- publishing 2: `series-sections` warnings; description lacks "what the reader will learn" form but is within length.

## Priority

P1: entry that introduces the notation $(A, B, C, D)$ used by entries 4-5 and by articles in the numerical and robotics series; required sections missing.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Blocking | whole file | publishing | Summary and References missing |
| D1 | Should fix | headings | structure | Sections unnumbered |
| D2 | Should fix | `:18` | purpose | Opening: no prerequisites, conventions or tools; vague statement of purpose |
| D3 | Should fix | `:32` | structure | The concept of state is introduced in the middle of a derivation; why a state is needed (initial conditions, internal variables, several inputs) is not motivated |
| D4 | Should fix | whole file | structure | Objective 2: the entry never shows the same system in input-output and state-space form (no transfer function of the example, no link from entry 2's first-order plant) |
| D5 | Should fix | `:62` | evidence | The eigenvalue test is stated without even the scalar argument; non-uniqueness of the state and invariance of eigenvalues not stated |
| D6 | Should fix | `:94-96` | structure | Limits (linearity, time invariance, lumped parameters) compressed into two sentences under a benefits heading |
| C1 | Optional | `:18` | language | "shows what its main matrix tells you" (second person, vague) |
| C2 | Optional | `:3` | publishing | Description is a fragment ("Writing a mechanical system ...") |

### P1. Summary and References missing
- `eos lint` `series-sections` ×2. Add Summary (table, closing to the fourth entry) and `### References` (Åström and Murray; Chen; Franklin et al.).

### D1. Unnumbered sections
- `:20`, `:60`, `:94`. Number them.

### D2. Opening
- **Text:** "A transfer function, introduced in the first entry, describes how one input affects one output. ... This primer builds a state-space model from a familiar example and shows what its main matrix tells you."
- **Correction:** state what it builds on (both earlier entries), what it covers, and conventions (SI units, column vectors, Python 3 and numpy).

### D3. State concept placement
- **Text:** "This is a second-order equation. The **state** of a system is a set of variables ..."
- **Correction:** a first section that motivates and defines the state, then shows entry 2's plant as a one-state model.

### D4. Objective 2 not demonstrated
- **Problem:** the series overview promises "Describe a linear time-invariant system in both input-output form and state-space form"; this entry is where both forms meet. Derivable in two lines: transforming $m\ddot q + c\dot q + kq = u$ at rest gives $G(s) = 1/(ms^2 + cs + k)$, whose denominator divided by $m$ is the characteristic polynomial found at `:66`.
- **Correction:** add a section relating the two forms, with the forward direction derived and the general formula $C(sI - A)^{-1}B + D$ deferred to the fourth entry, Section 6.

### D5. Eigenvalue test unsupported
- **Text:** "The solution decays to zero for every initial condition if and only if every eigenvalue of $A$ has a negative real part."
- **Correction:** give the reason in one step (eigenvector initial condition gives $e^{\lambda t}v$), state that the full proof is in the fourth entry; add the coordinate-change invariance $\det(sI - TAT^{-1}) = \det(sI - A)$.

### D6. Limits
- **Text:** "The model above is linear, so a real spring that stiffens or a damper that saturates needs linearization ..."
- **Correction:** separate section on assumptions: linear, time-invariant, lumped, finite-dimensional; what breaks each.

### C1, C2
- Impersonal voice; description as a sentence saying what the reader learns.

## Revision log (wave 1)

- **Structure:** sections numbered 1-7. New opening (what it builds on, what it covers, conventions: column vectors, SI units, Python 3 and numpy). New Section 1 motivating and defining the state (definition kept verbatim) and showing the second entry's plant as a one-state model; Section 2 keeps the derivation with a note on what each row means and what $y$ measures; Section 3 adds the second entry's plant as the $n = m = p = 1$ case and non-uniqueness of the state with the proof that eigenvalues are invariant ($\det(sI - TAT^{-1}) = \det(sI - A)$). Section 4 split into 4.1 (matrix exponential, with a one-line check that it solves the equation, and the eigenvector argument for one direction of the test), 4.2 (characteristic polynomial; negative-damping case added: eigenvalues $0.25 \pm 1.984j$, recomputed), 4.3 (numerical example). New Section 5 (objective 2): transfer function $1/(ms^2 + cs + k)$ derived from the ODE, poles = eigenvalues, $G(0) = 1/k = 0.25$ m/N, uniqueness one way and not the other, hidden modes (pointing to the fourth entry). New Section 6 (assumptions: linearity, time invariance, finite number of states). Summary with table and transition; References.
- **Prose:** second person removed; "primer" self-reference replaced by "entry".
- **Metadata:** description rewritten as a sentence (149 characters); `updatedAt: 2026-10-13` added here and in the Vietnamese file.
- **References:** Åström and Murray; Chen (state-space theory); Franklin et al.
- **Code:** unchanged; re-run, output matches.
- Remaining warnings: none.
- **Flags for independent review:** (technical) Section 3 invariance proof; Section 6 statement that a pure time delay has infinitely many states (standard: $e^{-sT}$ is not rational).
- **Vietnamese translation affected: yes.** Meaning changes: description; opening extended (scope sentence replaced, conventions paragraph added); Section 1 new (motivation, state as memory, first-order plant as one state, $n$ states for $n$-th order); Section 2 adds "displacement from the relaxed position", the meaning of the two rows and of $y$; Section 3 adds the one-state case and the coordinate-change paragraph; 4.1 adds the series check and the eigenvector argument; 4.2 now refers to "Section 5" instead of "the next entry" for why $s$ is used, adds the negative-damping sentence; 4.3 units moved to its own sentence (Python note moved to the opening), "(in 1/s)" added; Sections 5, 6 (limits rewritten from the former last section, which merged benefits and limits) and 7 (Summary, References) new; closing transition rewritten; all headings numbered.
- **Style (follow-up):** "numpy" in prose changed to "NumPy" (glossary term added by the coordinator); code and code spans unchanged.

## Independent review (wave 2)

- Reviewer: independent reviewer (fact-check, technical, series), commit `9232ed9`, 2026-10-13. Report: `reviews/foundations-of-control-systems.md`.
- Fact-check verdict: pass.
- Technical verdict: fail until T2 is resolved.
- Findings concerning this item: T2, T3 (optional), T4 (optional).
- Not verified: none.

## Revision log (wave 2 resolution)

- T2: Section 5 bullet "From transfer function to state space" now says coordinate changes give one answer each and realizations with extra hidden states give more (`:138`).
- T3: Section 4.2 negative-damping sentence now says the response grows, as an oscillation of increasing amplitude while $c^2 < 4mk$ (`:103`).
- T4: Section 4.1 adds a sentence on complex eigenvectors (the real initial condition $\operatorname{Re} v$ does not decay either) and says "a sum of modes" instead of "a sum of such terms" (`:87`).
- Lint 0/0/0; syntax passes. No front matter changed.
- Vietnamese translation affected: yes, for the three points above (4.1, 4.2 and the Section 5 bullet).
