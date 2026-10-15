# Series audit: Foundations of Control Systems

- Series: `foundations-of-control-systems`, 5 entries, status published; previous series review `reviews/foundations-of-control-systems.md` (resolved 2026-10-13; its corrections are kept).
- Audited at commit `e21dcc8`, 2026-10-13.

## Structural consistency across entries (before revision)

| Entry | Words (`eos status`) | Numbered sections | Opening states builds-on / conventions | Exercises | Summary | Closing transition | References |
|---|---|---|---|---|---|---|---|
| 1 Introduction to Control Systems | 669 | No | Partly / no | No | No | Outlook section | No |
| 2 Feedback and System Behavior | 774 | No | No link / no | No | No | Inline in last section | No |
| 3 A Primer on State-Space Models | 470 | No | Link / no | No | No | One line | No |
| 4 Stability and Eigenvalues | 2,810 | No | Yes / yes | Yes | Yes (unnumbered) | Yes | Yes (5, "2nd edition" form) |
| 5 Designing a State-Feedback Controller | 2,276 | No | Yes / yes | Yes | Yes, but followed by "Where the series ends" | After Summary | Yes (5, not alphabetical) |

No entry numbers its sections, although standards 5.4 and 6.2 require it and the other control-related series (`industrial-automation`, `introduction-to-robotics`, `digital-signal-processing`) number theirs, including Exercises and Summary (`## 7. Exercises`, `## 8. Summary`, `### References`). Decision for this series: number every section, including Exercises and Summary; References as `### References` under the Summary.

Entries 1-3 lack the Summary and References that `eos lint` requires (`series-sections` warnings) and are a quarter of the length of entries 4-5. Their gaps are of substance, not length: no worked transfer-function example and no derivation of the step-response formulas (entry 1); no worked stabilization case and no general sensitivity result for objective 1 (entry 2); no demonstration of objective 2 (the same system in input-output and state-space form) and no reason for the eigenvalue test (entry 3).

## Notation and terminology

- Consistent: $s$, $G(s)$, $\omega_n$, $\zeta$, $j$, $(A, B, C, D)$, "damping ratio", "natural frequency", "closed loop", "reference", American spelling.
- Symbol reuse already handled by the previous review ($m$, $k$). Entry 2 uses $k$ for the proportional gain, entry 3 for stiffness, entry 5 $K$/$k_1$/$k_2$ for gains; each is defined locally. Acceptable.
- Entry 1 uses $y$ for the output; entry 2 uses $x$ as output and state. Acceptable (entry 2 says $x$ is the output); entry 3 now makes the link explicit.
- "linear time-invariant" used in entry 3 and the objectives but defined nowhere; to be defined in entry 1.

## Overlap and gaps

- Overlap: the first-order transfer function is derived in entry 2 although entry 1 is the entry that introduces transfer functions; entry 4 restates the Laplace transform (acceptable, with back-reference). After revision entry 1 owns the first-order example and entry 2 refers to it.
- Gap: objective 1 "how feedback changes the stability" has one sentence in entry 2 (previous review F8 added it); a worked case belongs there.
- Gap: objective 2 is never demonstrated on one system in both forms before entry 4.
- Gap: no entry explains where $T_s \approx 4/(\zeta\omega_n)$ comes from, although entries 4 and 5 use it repeatedly.

## Overview page (standards 6.5)

Thin: audience stated; no sequence rationale; no shared conventions; "Each entry introduces one idea" inaccurate for entries 4-5. Objectives are checkable and each is covered.

## Cross-references

- Internal links between entries resolve and ordinals are correct (`eos lint` series-crossref clean).
- External fragment links into this series that will change when sections are numbered: `src/content/blog/from-signal-processing-to-digital-control.mdx:77` (`/blog/stability-and-eigenvalues#stability-in-discrete-time`) and `:267` (`/blog/state-feedback-controller-design#the-controller-runs-in-continuous-time`). These are outside this scope and must be updated by the orchestrator.

## Revision log (wave 1, series level)

- All five entries now have numbered sections, an opening paragraph stating what they build on and their conventions, a numbered Summary ending with a transition (entry 5: closing against the four objectives), and `### References` in house format.
- Entries 1-3 expanded with the missing reasoning (see item audits); entry 2 now refers back to entry 1 for the first-order transfer function instead of deriving it independently.
- Overview rewritten to state sequence rationale, prerequisites and shared conventions.
- New fragment ids (for the orchestrator): `stability-and-eigenvalues#7-stability-in-discrete-time`, `state-feedback-controller-design#64-the-controller-runs-in-continuous-time` (github-slugger form of "7. Stability in discrete time" and "6.4 The controller runs in continuous time"; confirm against the build).
