<!-- audit: {"slug":"stability-and-eigenvalues","type":"article","series":"foundations-of-control-systems","priority":"P2","before":{"purpose":4,"structure":3,"accuracy":3,"evidence":3,"language":3,"consistency":2,"publishing":2},"findings":{"blocking":1,"shouldFix":4,"optional":2}} -->
# Audit: Stability and Eigenvalues

- Path: `src/content/blog/stability-and-eigenvalues.mdx` · Route: `/blog/stability-and-eigenvalues` · Type: article (series entry) · Series `foundations-of-control-systems`, entry 4 of 5 · Words: 2,810 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 3: complete progression; sections unnumbered; the Summary ends with a transition but cites no section numbers.
- accuracy 3: all worked numbers recomputed (modal vs RK4, 2.513 at 0.683, pendulum eigenvalues, Euler bounds); but the printed output of the pendulum script does not match what numpy 2.5.3 prints (see A1).
- evidence 3: five verified textbooks; reference format not house style ("2nd edition" instead of "2nd ed.").
- language 3: "simply" twice; the description is 297 characters.
- consistency 2: unnumbered sections unlike the house standard; structure now differs from entries 1-3 (to be aligned).
- publishing 2: description 297 characters (lint warning).

## Priority

P2: no critical condition other than one code-output mismatch, but metadata and structural inconsistency.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| A1 | Blocking | `:284` | accuracy | Comment shows `[ 2.89205347 -3.39205347]`; numpy 2.5.3 prints `[ 2.89205347+0.j -3.39205347+0.j]` |
| D1 | Should fix | headings | structure | Sections unnumbered |
| C1 | Should fix | `:3` | publishing | Description 297 characters, a topic list |
| C2 | Should fix | `:354-358` | evidence | References not in house format ("2nd edition" for "2nd ed.") |
| P1 | Should fix | `:29` | consistency | "the section on hidden modes below" should cite the section number once sections are numbered |
| C3 | Optional | `:17`, `:143` | language | "simply" twice (intensifier) |
| D2 | Optional | `:205-211` | consistency | Transfer function of the example re-derived without noting that the primer obtained it from the differential equation |

### A1. Code output mismatch
- **Where:** `:284`
- **Text:** `print(np.linalg.eigvals([[0, 1], [ g / L, -d]]))   # [ 2.89205347 -3.39205347]`
- **Problem:** ran the block with Python 3.13.16 and numpy 2.5.3 (the entry says "run with numpy 2.5"): the output is `[ 2.89205347+0.j -3.39205347+0.j]`. Standards 6.2 item 3 requires the real output.
- **Correction:** replace the comment by the actual output.

### D1. Number sections (1-8, Exercises 9, Summary 10).
### C1. Description: one sentence within 165 characters.
### C2. References: "2nd ed.", "4th ed.", "8th ed.", "3rd ed."; already alphabetical.
### P1. "the section on hidden modes below" → "Section 6 shows when they differ".
### C3. Remove "simply" where it adds nothing ("written rad/s, or 1/s"; "has the eigenvalue $0$ and holds its initial value").
### D2. After numbering, say "which agrees with the transfer function the primer obtained from the differential equation" once the primer derives it.

## Revision log (wave 1)

- **Structure:** sections numbered 1-10 (Exercises 9, Summary 10); no content moved.
- **Technical correction:** pendulum script comment changed to the real output `[ 2.89205347+0.j -3.39205347+0.j]` (evidence: ran the block with Python 3.13.16 and numpy 2.5.3).
- **Cross-references:** "the section on hidden modes below" → "Section 6"; Exercise 5 names Section 6; step-response formulas cited as "the first entry, Section 4.2"; the transfer function of the example is now noted as the one the primer obtained (third entry, Section 5); Section 6's opening sentence updated because the first entry and the primer now give transfer functions (first-order plant, mass-spring-damper) but not from a state-space model.
- **Prose / style:** "simply" removed twice; "Runge-Kutta" → "Runge–Kutta" (glossary term, via `eos fix --rules terminology`, at the coordinator's request).
- **Metadata:** description shortened to one sentence (146 characters). No `updatedAt` (published 2026-10-13).
- **References:** "2nd edition" etc. → "2nd ed." (house format); order already alphabetical; contents unchanged.
- Remaining warnings: none.
- **Flags:** fragment ids changed (e.g. `#stability-in-discrete-time` → `#7-stability-in-discrete-time`); `src/content/blog/from-signal-processing-to-digital-control.mdx:77` links the old id and must be updated by the orchestrator (outside scope).
- **Vietnamese translation affected:** no translation exists.
- **Style (follow-up):** "numpy" in prose changed to "NumPy" (glossary term added by the coordinator); code and code spans unchanged.
