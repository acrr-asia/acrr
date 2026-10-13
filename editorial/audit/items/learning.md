<!-- audit: {"slug":"learning","type":"learning","series":null,"priority":"P3","before":{"purpose":3,"structure":4,"accuracy":3,"evidence":4,"language":3,"consistency":3,"publishing":4},"findings":{"blocking":0,"shouldFix":2,"optional":1}} -->
# Audit: Learning entries (English fields)

- Path: `src/data/learning.json` · Route: `/learning` · Type: Learning entries (6) · English `title`, `description`, `topic` only
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: descriptions say what each resource will cover; none says for whom, but the related series fix the audience implicitly.
- accuracy 3: every entry is `"status": "planned"` with no `url`, and every description says "planned"; nothing claims a resource exists. One description no longer reflects the site: `introduction-to-robotics-learning-path` describes a reading order through kinematics and sensing without mentioning that the published Introduction to Robotics series now covers those two topics (motion planning is not covered on the site).
- language 3: `numerical-methods-external-references` has two sentences, the second an editorial policy rather than a description (standards 6.6: one sentence on what the resource covers and for whom).
- consistency 3: series names are correct ("Foundations of Control Systems", "Machine Learning Fundamentals"); the numerical-methods entry does not name the published Numerical Simulation for Engineers series it would serve.

## Priority

P3: no false claim; descriptions slightly behind the content.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `introduction-to-robotics-learning-path` | consistency | Does not relate the planned path to the published Introduction to Robotics series. |
| C1 | Should fix | `numerical-methods-external-references` | language | Two sentences; second is policy, not description. |
| C2 | Optional | all | purpose | Audience not stated; not added, because the related series state it. |

### D1
- **Text:** "A planned reading order through the basics of robot kinematics, sensing and motion planning, with the mathematics each step relies on."
- **Correction:** "A planned reading order through robot kinematics, sensing and motion planning, with the mathematics each step relies on, to accompany the Introduction to Robotics series."

### C1
- **Text:** "A planned list of public references on numerical methods and simulation. Each item will be added only after it has been checked and a real link is available."
- **Correction:** "A planned list of checked public references on numerical methods and simulation, to accompany the Numerical Simulation for Engineers series."

Entries left unchanged: `control-systems-study-notes`, `mathematical-methods-study-notes`, `machine-learning-learning-path`, `computing-systems-study-notes` (accurate, planned, one sentence). No URL added anywhere; all statuses stay `planned`.

## Revision log (wave 1)

- `introduction-to-robotics-learning-path`: description now relates the planned path to the published Introduction to Robotics series ("..., to accompany the Introduction to Robotics series").
- `numerical-methods-external-references`: two sentences merged into one ("A planned list of checked public references on numerical methods and simulation, to accompany the Numerical Simulation for Engineers series.").
- Unchanged: titles, topics, types, statuses (all `planned`), no `url` anywhere, all `vi` fields.
- Flags for independent review: none.
- Vietnamese fields affected: yes, `vi.description` of `introduction-to-robotics-learning-path` (add the relation to the series) and of `numerical-methods-external-references` (one sentence, naming the series). Not edited here.
