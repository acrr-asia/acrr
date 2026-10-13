# Series audit: Introduction to Robotics

- Series: `introduction-to-robotics`, 4 entries, status published; audited at commit `e21dcc8`, 2026-10-13.
- Previous review: `reviews/introduction-to-robotics.md` (second pass, 8 findings, all applied). Its corrections (accelerometer and gravity, axis conventions, radians in entry 3, discrete-time $A$/$B$, notation $n_b$/$n_j$, lidar at the robot origin, wording of the DH sentence) are present and were preserved.

## Structural consistency across entries

| | Entry 1 | Entry 2 | Entry 3 | Entry 4 |
|---|---|---|---|---|
| Numbered sections | yes (1-7) | yes (1-9) | yes (1-9) | yes (1-10) |
| Opening without prose outline | no (outline, line 18) | no (outline, line 17) | yes | no (outline, line 21) |
| Earlier entries linked | n/a | no | no | no |
| Exercises | no | no | no | no |
| Summary table + closing transition | yes | yes | yes | Summary, then a separate §10 series close |
| References under Summary | yes | yes | yes | under §10 |
| Description ≤ 165 characters | 309 | 305 | 389 | 396 |
| Headings sentence case | no | no | no | no |

Systemic problems: every description is about twice the limit and lists sections; every entry uses title-case H2 headings; British spellings survive from the archive's earlier style (the previous review recorded "Spelling is British throughout"; the house variant is now American); references lack volume/issue/pages; cross-entry mentions ("the first entry", "the previous entry") are not linked; no entry carries exercises, though entries 2-4 are computational and most other series on the site have them.

## Notation and terminology

Consistent: frames ${}^{A}T_{B}$, $J$ for the Jacobian (entry 1's motor inertia is $J_m$, separated by subscript), $\mathbf q$/$\mathbf x$ for joint/task space, $P$, $Q$, $R$, $K$ in entry 4. Angles: degrees in examples, radians in computation, stated in entries 3 and 4 and in entry 2's mistakes table. "toward" (entry 1) vs "towards" (entries 2, 4): unify to "toward".

## Overlap and gaps

No duplicated explanations; later entries refer back (atan2, angle wrapping, gimbal lock, Jacobian). Gap against the objectives: none. Objective 4 ("Outline the sense, plan, and act structure") is covered by entry 1 §5 only, briefly but adequately.

## Overview page (standards 6.5)

Fails "sequence rationale", "what each entry contributes" and "shared conventions"; meets reader/prerequisites and objectives. See `editorial/audit/items/series-introduction-to-robotics.md`.

## Cross-references

All ordinal mentions ("first", "second", "previous", "next", "last", "final") name the right entry; all "Section x.y" references resolve. Inbound fragment links from `calibration-and-multisensor-fusion.mdx` to four section anchors of entry 4 depend on those headings' wording (kept). Inbound plain links from `state-feedback-controller-design.mdx` and `networked-automation-and-digital-twins.mdx` (no fragments).
