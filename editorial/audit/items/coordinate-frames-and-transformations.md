<!-- audit: {"slug":"coordinate-frames-and-transformations","type":"article","series":"introduction-to-robotics","priority":"P2","before":{"purpose":3,"structure":3,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":2}} -->
# Audit: Coordinate Frames and Rigid-Body Transformations

- Path: `src/content/blog/coordinate-frames-and-transformations.mdx` · Route: `/blog/coordinate-frames-and-transformations` · Type: article · Series `introduction-to-robotics`, entry 2 of 4 · Words: 2267
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: opening links the first entry only implicitly ("The first entry of this series", unlinked) and ends with a prose outline ("frames and notation first, then rotations, then ...").
- structure 3: concepts before mechanics throughout; no exercises although the worked example is computational.
- accuracy 4: recomputed (below).
- evidence 3: three standard textbooks, existence certain; format "3rd edition" instead of "3rd ed."; not alphabetical (Lynch, Siciliano, Craig).
- language 3: title-case headings; "re-orthonormalised", "renormalisation", "orthonormalise" (British); "towards"; "we describe it" (standards 2.3 reserve "we" for derivation steps).
- consistency 3: British forms against the American house variant.
- publishing 2: description 305 characters.

Accuracy spot-check (python3, numpy): $R_x(90^\circ)R_z(90^\circ)$ and $R_z(90^\circ)R_x(90^\circ)$ as printed; ${}^{W}T_{R}(3,0,1) = (2,4,1)$; ${}^{R}T_{W}$ as printed; camera chain $(1.8, 2.5)$; gimbal-lock pair $(30^\circ,10^\circ)$, $(50^\circ,30^\circ)$ equal at $\theta = 90^\circ$. All correct.

## Priority

P2: metadata and style problems a reader would notice; foundational content correct.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 305 characters. |
| P2 | Should fix | H2 headings | language | Title case (lines 19, 55, 75, 132, 174, 204, 213, 237). |
| C1 | Should fix | lines 23, 107, 130, 246 | language | British spellings ("towards", "re-orthonormalised", "renormalisation", "Re-orthonormalise"). |
| D1 | Should fix | `:15-17` | purpose | First entry not linked; prose outline at the end of the opening; conventions (right-handed frames, radians internally) scattered. |
| D2 | Should fix | before Summary | structure | No exercises for a computational entry. |
| P3 | Should fix | References | evidence | Not house format ("3rd edition"), not alphabetical. |
| C2 | Optional | `:208` | language | "we describe it in a different frame". |
| C3 | Optional | `:99` | language | "This single fact is behind most of the difficulty" (overstated; "much" is defensible). |

### P1. Description
- **Correction:** "Learn how a robot describes position and orientation with coordinate frames, rotation matrices, quaternions and homogeneous transformations." (141)

### D1. Opening
- **Text:** "The entry builds that machinery from the general to the specific: frames and notation first, then rotations, ..."
- **Correction:** link [the first entry](/blog/what-is-a-robot); replace the outline with the conventions used (right-handed frames, column vectors, angles in radians in computation, degrees in examples).

## Revision log (wave 1)
- Structure: prose outline at the end of the opening replaced by a conventions paragraph (column vectors, matrices from the left, radians in computation, degrees in examples). New Section 9 "Exercises" (pose transform, transform inversion, angle wrapping; recomputed with python3: $(-1, 1)$; ${}^{B}T_{A}$ with translation $(0, 3)$; $+20^\circ$). Summary renumbered 9 → 10.
- Prose: "we describe it" → "is described"; "This single fact is behind most of the difficulty" → "Much of the difficulty ... follows from this one fact".
- Terminology/style: headings in sentence case; "towards", "re-orthonormalised", "renormalisation", "Re-orthonormalise" → American forms.
- Metadata: description rewritten (141 characters).
- References: house format ("3rd ed."), alphabetical.
- Cross-references: links to the first, next and last entries added.
- Technical corrections: none.
- Remaining warnings: none.
- Flags for independent review: exercises (new content).
- Vietnamese translation affected: yes: conventions paragraph replaces the outline sentence; new Section 9 Exercises; Summary renumbered 10; reference order; description. No `updatedAt` (published 2026-10-13).

## Independent review (wave 2)
- Fact-check: pass.
- Technical: pass (Exercises 1-3 recomputed: (-1, 1); B_T_A and its check on (3, 0); +20°; gimbal-lock and product examples re-run).
- Findings: none.
- Not verified: textbook reference details (Craig, Lynch and Park, Siciliano et al.) not re-fetched.
