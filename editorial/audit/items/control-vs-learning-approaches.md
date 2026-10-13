<!-- audit: {"slug":"control-vs-learning-approaches","type":"insight","series":null,"priority":"P2","before":{"purpose":2,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":2,"publishing":3},"findings":{"blocking":1,"shouldFix":4,"optional":1}} -->
# Audit: Model-Based Control and Learned Policies

- Path: `src/content/insights/control-vs-learning-approaches.md` · Route: `/insights/control-vs-learning-approaches` · Type: insight (Comparison) · Words: 336
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: no framing paragraph (standards 6.4).
- structure 3: the Established paragraph on learning (line 16) ends by defining the sim-to-real gap, which is the subject of a separate insight; a link would replace the repetition.
- accuracy 4: LQR, MPC and RL statements are standard and qualified.
- evidence 3: no links; the site treats state feedback and mentions LQR (`state-feedback-controller-design`, "Placing poles is not the only choice"), feedback robustness (`feedback-and-system-behavior`) and learning from data (Machine Learning Fundamentals series).
- language 3: "These approaches read better as two ends of a spectrum than as rivals. The deciding factors appear to be ..."; "likely depends" hedges are stacked in Interpretation.
- consistency 2: two complete series on exactly the two families compared, none linked.
- publishing 3: description 157 characters but a noun phrase ("A short comparison of ...").

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Blocking | line 12 | structure | No framing paragraph (standards 6.4, C7). |
| D2 | Should fix | whole file | consistency | No links to the Foundations of Control Systems or Machine Learning Fundamentals entries. |
| D3 | Should fix | line 16 | structure | Re-defines the sim-to-real gap instead of linking the insight that treats it. |
| P1 | Should fix | `:3` | publishing | Description not a sentence. |
| C1 | Should fix | lines 20–22 | language | Stacked hedges ("appear to be", "likely depends"). |
| C2 | Optional | line 14 | language | "certain closed loops" is vague; the margins apply to single-loop (single-input single-output) designs. Left as is: the qualification is correct; flagged for the technical reviewer. |

## Revision log (wave 1)

- Structure: added the framing paragraph; the sim-to-real definition now links the insight that treats it instead of re-defining it.
- Cross-references: added `/series/foundations-of-control-systems`, `/blog/state-feedback-controller-design` (which mentions LQR), `/insights/closing-the-sim-to-real-gap`, `/series/machine-learning-fundamentals`.
- Prose: Interpretation rewritten to label the reading once ("One reading is ...") instead of stacking "appear to be" and "likely"; added "no general answer is evident" to keep the hybrid claim an interpretation; serial comma removed ("data, design effort and robustness"); "an MPC" → "an MPC controller".
- Metadata: description rewritten as one sentence (138 characters).
- Remaining warnings: none.
- Flags for independent review: (technical) "Classical tools such as gain and phase margins describe how much model error certain closed loops can tolerate": correct but vague; margins apply to single-input single-output loops. Left unchanged.
- Vietnamese translation affected: yes: framing paragraph, link sentences to both series, reworded Interpretation, new description.
