<!-- audit: {"slug":"planar-arm-kinematics","type":"article","series":"introduction-to-robotics","priority":"P2","before":{"purpose":4,"structure":3,"accuracy":4,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":7,"optional":2}} -->
# Audit: Forward and Inverse Kinematics of a Planar Arm

- Path: `src/content/blog/planar-arm-kinematics.mdx` · Route: `/blog/planar-arm-kinematics` · Type: article · Series `introduction-to-robotics`, entry 3 of 4 · Words: 2028
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4: purpose, prerequisite (previous entry) and the radians convention are stated (the last only in Section 2.2).
- structure 3: clear progression; no exercises for the most computational entry of the series; the "previous entry" and "first entry" mentions are not linked.
- accuracy 4: recomputed (below). One qualification could be sharper (A1).
- evidence 2: "Craig's textbook" is named in the text (line 77) but not in the References; Denavit–Hartenberg lacks volume, issue and pages; not in house format.
- language 3: title-case headings; "popularised", "centre" (British); "very large"; a 52-word sentence (line 212); "A third joint lets the gripper reach points inside the ring at any orientation only in a smaller interior region" (line 89) is hard to parse.
- consistency 3: British forms.
- publishing 2: description 389 characters.

Accuracy spot-check (python3, numpy): forward kinematics $(1.0472, 1.1761)$; $c_2 = 0.7071$; inverse solutions $(30^\circ, 45^\circ)$ and $(66.64^\circ, -45^\circ)$; $\det J = 0.4950$; Newton errors from $(0^\circ, 90^\circ)$: 0.478, 0.113, 0.0116, $1.8 \times 10^{-4}$, $6.4 \times 10^{-8}$ (text "$6 \times 10^{-8}$", correct to one figure); first Newton step from $(0^\circ, 1^\circ)$ to $(1.75, 0.05)$: $(166.6^\circ, -401.6^\circ)$; first damped step $\lambda = 0.1$: $(1.80^\circ, -1.33^\circ)$; damped iteration ends at radius 1.7000, 0.0507 from the target. All correct.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 389 characters. |
| P2 | Should fix | H2 headings | language | Title case (lines 21, 39, 91, 176, 216 and others). |
| A1 | Optional | `:221` | accuracy | Pieper's sufficient condition is stated as only "three consecutive joint axes intersect at a point"; Pieper's thesis also covers three consecutive parallel axes. Flag for technical review; the sentence is not wrong as a sufficient condition. |
| A2 | Should fix | `:77`, References | evidence | Craig's textbook cited in text, absent from References. |
| A3 | Should fix | `:245` | evidence | Denavit and Hartenberg 1955 lacks vol. 22, no. 2, pp. 215–221. |
| D1 | Should fix | `:17, 25` | consistency | "previous entry", "first entry" not linked (standards 8.1). |
| D2 | Should fix | before Summary | structure | No exercises. |
| C1 | Should fix | lines 77, 221 | language | "popularised", "centre". |
| C2 | Should fix | `:89` | language | Garbled sentence on the dexterous workspace. |
| C3 | Optional | lines 169, 212 | language | "very large"; 52-word sentence. |

### C2. Dexterous workspace sentence
- **Text:** "A third joint lets the gripper reach points inside the ring at any orientation only in a smaller interior region, the **dexterous workspace**; near the boundary, the arm must be stretched, and the gripper's orientation is forced."
- **Correction:** "With a third joint, the gripper can reach a point at any orientation only within a smaller interior region, the **dexterous workspace**. Near the outer boundary the arm must be stretched to reach at all, so the gripper's orientation is forced."

### P1. Description
- **Correction:** "Learn to compute a two-link arm's gripper position from its joint angles and back, and why inverse kinematics has several solutions and singularities." (148)

## Revision log (wave 1)
- Structure: new Section 9 "Exercises" (both inverse solutions for $(1.2, 0.5)$, an unreachable target, $\det J$ near the stretched configuration; recomputed with python3: $(-9.6^\circ, 81.8^\circ)$ and $(54.8^\circ, -81.8^\circ)$, forward check $(1.20, 0.50)$; $c_2 = 1.79$; $\det J = 0.122$). Summary renumbered 9 → 10.
- Prose: dexterous-workspace sentence rewritten (C2); 52-word sentence in Section 7 split; "very large" → "large".
- Terminology/style: headings in sentence case; "popularised" → "popularized"; "centre" → "center".
- Metadata: description rewritten (148 characters).
- References: Craig added (cited in Section 2.3 as "Craig's textbook"; same entry as in the second entry); Denavit and Hartenberg completed with vol. 22, no. 2, pp. 215–221 (Wikipedia article on J. Denavit, consistent with DOI 10.1115/1.4011045; crossref was not reachable from this environment); house format, alphabetical.
- Cross-references: links to the previous, first and final entries.
- Technical corrections: none.
- Remaining warnings: none.
- Flags for independent review: A1 (Pieper's condition stated only for intersecting axes); exercises; Denavit–Hartenberg details verified against a secondary source only.
- Vietnamese translation affected: yes: dexterous-workspace sentence (meaning clarified, not changed), new Section 9 Exercises, Summary renumbered 10, Craig added to References, description. No `updatedAt` (published 2026-10-13).
