<!-- audit: {"slug":"when-a-kalman-filter-is-enough","type":"insight","series":null,"priority":"P2","before":{"purpose":2,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":3},"findings":{"blocking":1,"shouldFix":3,"optional":1}} -->
# Audit: When Is a Kalman Filter Enough?

- Path: `src/content/insights/when-a-kalman-filter-is-enough.md` · Route: `/insights/when-a-kalman-filter-is-enough` · Type: insight (Comparison) · Words: 348
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: no framing paragraph (standards 6.4).
- structure 3: sound.
- accuracy 4: the optimality statement is correctly conditioned (Gaussian: MMSE among all estimators; same second moments without Gaussianity: best linear). The normalized innovation squared follows a chi-square distribution with $m$ degrees of freedom under the model; "a chi-square distribution" is correct as written.
- evidence 3: no links; `sensing-and-state-estimation` (Sections 5 and 6) treats all four estimators in depth, with references (Kalman 1960; Thrun, Burgard and Fox).
- language 3: "unmodelled" (British; house spelling is American, "unmodeled").
- consistency 3: the guide pairs the EKF and UKF for "mildly nonlinear" models; the in-depth entry's table (Section 6.4) places the UKF one step further ("More strongly nonlinear models"). Not a contradiction (both are single-Gaussian filters), but the insight should say the UKF usually tolerates stronger nonlinearity, as the entry does.
- publishing 3: description 158 characters, a noun phrase.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Blocking | line 12 | structure | No framing paragraph (standards 6.4, C7). |
| D2 | Should fix | whole file | consistency | No link to `sensing-and-state-estimation`. |
| C1 | Should fix | line 31 | language | "unmodelled" → "unmodeled". |
| D3 | Should fix | line 23 | consistency | EKF/UKF grouping vs the entry's table (Section 6.4). |
| P1 | Optional | `:3` | publishing | Description a noun phrase. |

## Revision log (wave 1)

- Structure: added the framing paragraph with a link to `/blog/sensing-and-state-estimation`.
- Consistency: the UKF sentence now says it usually captures nonlinear effects better than the EKF at a similar cost (as Section 6.2 of the entry says), and the guide's middle item distinguishes EKF (mild nonlinearity over the spread of the uncertainty) from UKF (stronger), matching the entry's table (Section 6.4).
- Language: "unmodelled" → "unmodeled".
- Metadata: description rewritten as one sentence (161 characters).
- Remaining warnings: none.
- Flags for independent review: (technical) the revised guide item on EKF vs UKF; (series) `sensing-and-state-estimation` line 168 states optimality without distinguishing "among all estimators" (Gaussian case) from "among linear estimators"; the insight is the more precise of the two.
- Vietnamese translation affected: yes: framing paragraph, UKF clause, middle guide item, spelling, new description.
