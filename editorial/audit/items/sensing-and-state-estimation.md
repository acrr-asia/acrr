<!-- audit: {"slug":"sensing-and-state-estimation","type":"article","series":"introduction-to-robotics","priority":"P2","before":{"purpose":3,"structure":2,"accuracy":4,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":8,"optional":3}} -->
# Audit: Sensing and State Estimation: An Overview

- Path: `src/content/blog/sensing-and-state-estimation.mdx` · Route: `/blog/sensing-and-state-estimation` · Type: article · Series `introduction-to-robotics`, entry 4 of 4 · Words: 2821
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: the opening restates the previous entries well but its second paragraph is a prose outline ("It starts with ..., then introduces ..., then ..."); earlier entries are not linked.
- structure 2: the series close ("## 10. The Series in One Picture") follows the Summary, so the References sit under Section 10 instead of under the Summary (standards 6.2 items 6-7); the closing does not go back to the series objectives; no exercises for a computational entry.
- accuracy 4: recomputed (below).
- evidence 2: Kalman 1960, Julier and Uhlmann 1997 and Durrant-Whyte and Bailey 2006 lack volume, issue and pages; not house format; not alphabetical.
- language 3: title-case headings; "towards" (three times), "coloured" (figure caption); "actually" twice; "Very low" in the table.
- consistency 3: "SLAM" in the 7.2 heading before its expansion in the body.
- publishing 2: description 396 characters.

Known issue checked: "Kalman Filter" capitalized in running text. Not present: the only occurrence (line 252) is the original title of Julier and Uhlmann's paper in the References, which keeps its original capitalization (standards 5.1). No change.

Accuracy spot-check (python3): $K = 0.7353$, $\hat x = 10.441$ m, $P = 0.0662$ m², $\sigma = 0.257$ m; prediction $P^- = 0.106$ m²; ten moves $\sqrt{0.066 + 0.4} = 0.683$ m; $d^2 = 0.36/0.34 = 1.06$; $4/0.34 = 11.8$; $\chi^2_{1, 0.99} = 6.63$. All correct.

Dependency: `calibration-and-multisensor-fusion.mdx` links to the fragments `#4-a-worked-example-in-one-dimension`, `#71-fusing-complementary-sensors`, `#5-the-kalman-filter`, `#8-engineering-details-that-decide-success`. Heading words of those four sections must be kept (case changes do not change the slug).

## Priority

P2 (other items link into its sections).

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 396 characters. |
| P2 | Should fix | H2 headings | language | Title case (lines 23, 48, 67, 107, 199, 214, 238). |
| D1 | Should fix | `:238-247` | structure | Series close after the Summary; References under it; no tie back to the objectives. |
| D2 | Should fix | `:21` | purpose | Prose outline; earlier entries not linked. |
| D3 | Should fix | before Summary | structure | No exercises. |
| A1 | Should fix | References | evidence | Kalman, Julier–Uhlmann, Durrant-Whyte–Bailey missing details. |
| C1 | Should fix | lines 103, 119, 129, 233 | language | "towards", "coloured". |
| C2 | Should fix | `:210` | consistency | "SLAM" in heading before expansion. |
| C3 | Optional | lines 103, 194, 222 | language | "actually" (x2), "Very low". |
| C4 | Optional | `:252-253` | language | "SPIE", "MIT" unexpanded (names; leave). |
| C5 | Optional | `:127` | language | "Combining two independent pieces of information always helps" restates the previous clause; fold into one statement. |

### A1. References
- Kalman: verified *Transactions of the ASME, Journal of Basic Engineering*, vol. 82 (Series D), pp. 35–45, 1960 (first page of the paper, Yale reading copy; UNC Welch–Bishop page). Issue number not printed on the first page: not added.
- Julier and Uhlmann: verified *Proceedings of SPIE*, vol. 3068, pp. 182–193, 1997 (SFB/TR 8 bibliography; ModelDB citation).
- Durrant-Whyte and Bailey: vol. 13, no. 2, 2006 verified (two bibliographies). Pages: the article PDF (Imperial College copy) runs 99–108; one bibliography gives 99–110. Used 99–108 from the article itself; flagged.

## Revision log (wave 1)
- Structure: opening second paragraph rewritten (no outline; states where the probability is introduced and the matrix conventions). Former Section 10 "The Series in One Picture" merged into the Summary as its closing paragraphs, now linked and tied to the series objectives; References now sit under the Summary. New Section 9 "Exercises" (update with a more precise prediction, growth of variance under dead reckoning, gating; recomputed with python3: $K = 0.308$, $\hat x = 5.09$ m, $\sigma = 0.17$ m; fifth move, $\sigma = 0.52$ m; $d^2 = 4.24$). Summary renumbered 9 → 10.
- Prose: Section 4's last two sentences merged into one statement of why fusion reduces the variance; "actually" (x2) removed; "Very low" → "Lowest" in the comparison table.
- Terminology/style: headings in sentence case (words of Sections 4, 5, 7.1 and 8 kept, so the fragment links from `calibration-and-multisensor-fusion.mdx` still resolve: slugs are lower-case); "towards" (x3) → "toward"; "coloured" → "colored"; 7.2 heading "Localization, mapping and SLAM" → "Localization and mapping" (abbreviation now first appears with its expansion in the body; no inbound link used the old anchor).
- Known issue "Kalman Filter in running text": not present; the only occurrence is the original title of Julier and Uhlmann's paper, kept.
- Metadata: description rewritten (156 characters).
- References: alphabetical, house format; Kalman: *Transactions of the ASME, Journal of Basic Engineering*, vol. 82, pp. 35–45 (first page of the paper); Julier and Uhlmann: *Proceedings of SPIE*, vol. 3068, pp. 182–193; Durrant-Whyte and Bailey: vol. 13, no. 2, pp. 99–108.
- Cross-references: links to all three earlier entries and the series page.
- Technical corrections: none.
- Remaining suggestions: "SPIE", "ASME", "MIT" unexpanded in References (organization names).
- Flags for independent review (fact-check): Kalman issue number (no. 1 commonly cited) not added because the first page does not print it; Durrant-Whyte and Bailey pages: the article PDF runs 99–108, one bibliography says 99–110; its title is "Simultaneous Localisation and Mapping (SLAM): Part I" on the PDF but "Simultaneous localization and mapping: part I" in IEEE metadata (left as before). Exercises (new content) for technical review.
- Vietnamese translation affected: yes: opening paragraph 2; the Section 4 fusion sentences; new Section 9 Exercises; Section 10 Summary now includes the former Section 10 series close (rewritten as a paragraph tied to the objectives); heading 7.2 renamed; references; description. No `updatedAt` (published 2026-10-13).

## Independent review (wave 2)
- Fact-check: fail (F1: the UKF is dated to 1997, but Julier, Uhlmann and Durrant-Whyte published it in 1995). Durrant-Whyte and Bailey pp. 99-108, Julier and Uhlmann pp. 182-193, Kalman vol. 82 pp. 35-45 verified.
- Technical: fail (T1: Exercise 3 says "two standard deviations from the prediction"; d = 2.06 is in innovation standard deviations). Exercise numbers all recomputed and correct.
- Findings: T1 (should fix), F1 (should fix), T2 (optional).
- Not verified: Kalman issue number (not in the text); Bar-Shalom et al. and Thrun et al. details not re-fetched.

## Revision log (wave 2 resolution)
- T1: Exercise 3 answer states the distance in innovation standard deviations ($\sqrt{4.24} = 2.06$, $\sqrt S = 0.58$ m), from the predicted measurement.
- F1: UKF dated to the mid-1990s, with the 1997 paper named as the usual reference.
- T2: Exercise 1 question asks why the estimate moves a smaller fraction of the way toward the measurement.
- Anchors of Sections 4, 5, 7.1 and 8 unchanged. Lint: 0 errors, 0 warnings, 3 suggestions (organization names in References). Syntax: compiles.
- Vietnamese translation affected: yes, meaning changes in §6.2 (UKF origin), Exercise 1 question and Exercise 3 answer (not yet present in the translation, which lacks the wave-1 exercises).
