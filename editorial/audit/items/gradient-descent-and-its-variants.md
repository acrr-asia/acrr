<!-- audit: {"slug":"gradient-descent-and-its-variants","type":"article","series":"machine-learning-fundamentals","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":4}} -->
# Audit: Gradient Descent and Its Variants

- Path: `src/content/blog/gradient-descent-and-its-variants.mdx` · Route: `/blog/gradient-descent-and-its-variants` · Type: article (series entry) · Series `machine-learning-fundamentals`, entry 2 of 4 · Words: 2931 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4
- structure 4
- accuracy 4: all three Python blocks rerun (Python 3.13.16, NumPy 2.5.3): identical output. Recomputed: Hessian $\begin{psmallmatrix}2.000&1.025\\1.025&0.732\end{psmallmatrix}$, eigenvalues 0.1608 and 2.5709, $\eta$ limit 0.7779, $\kappa = 15.99$, best rate 0.7321 with factor 0.8823; steps for a $10^6$ reduction 110.3 ($\kappa = 16$) and 930.4 ($\kappa = 134.7$); Exercise 2, 690.8 steps; decayed rate after 999 steps 0.0091. All correct.
- evidence 3: references in "22(3), 1951" style with no pages, not alphabetical, "2nd edition"; Kingma and Ba not in conference format.
- language 3: "strikingly similar", "really", "essentially", "wildly"; two sentences of 51 and 48 words.
- consistency 3: five title-case headings; "numpy".
- publishing 2: description 381 characters; duplicate heading "Worked example" (3.3 and 4.3) gives ambiguous anchors.

## Priority

P2: metadata and structural inconsistencies a reader notices; content correct.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 381 characters. |
| P2 | Should fix | `:132`, `:260` | publishing | Duplicate heading "Worked example". |
| C1 | Should fix | `:19`, `:90`, `:231`, `:303` (and `:48`) | consistency | Title-case headings. |
| C2 | Should fix | `:380–386` | evidence | Volume style "22(3), 1951", no pages, not alphabetical, "2nd edition", conference entry without "in *...*". |
| D1 | Should fix | `:227` | accuracy/structure | "with the strong curvature of Section 3.2 ($\lambda_{\min} > 0$) the convergence is geometric, as seen there": the property (strong convexity) is not named, and "slow in the worst case" does not say how slow ($1/t$). |
| C3 | Optional | `:34` | language | "takes a form strikingly similar to least squares": vague; the difference (residual $\mathbf{p}-\mathbf{y}$, no factor 2) can be stated. |
| C4 | Optional | `:88`, `:305` | language | "is really a form of regularization"; "essentially that of a gradient evaluation". |
| C5 | Optional | `:215`, `:301` | language | 51- and 48-word sentences; "wildly different scales". |
| C6 | Optional | `:17` | consistency | "numpy". |

### C2. Reference format
- **Where:** `:380–386`
- **Text:** "H. Robbins and S. Monro, "A Stochastic Approximation Method," *The Annals of Mathematical Statistics*, 22(3), 1951."
- **Problem:** standards 7.3 require "vol. 22, no. 3, pp. 400–407, 1951", alphabetical order and "2nd ed.".
- **Correction:** verified details: Robbins and Monro, vol. 22, no. 3, pp. 400–407 (Columbia-hosted scan of the paper); Polyak, English translation in *USSR Comput. Math. Math. Phys.* vol. 4, no. 5, pp. 1–17 (Math-Net.ru record, DOI 10.1016/0041-5553(64)90137-5; the Russian original is *Zh. Vychisl. Mat. Mat. Fiz.* 4(5), 791–803); Bottou, Curtis and Nocedal, *SIAM Review* vol. 60, no. 2, pp. 223–311 (author's PDF); Kingma and Ba, 3rd ICLR, 2015 (no page numbers exist).

## Revision log (wave 1)

- Structure: headings 3.3 and 4.3 renamed "Worked example: four learning rates" and "Worked example: batch size and schedule" (unique anchors).
- Prose: logistic-regression gradient now states exactly how it differs from least squares; "really", "essentially", "wildly" cut; Section 3.4 and Section 4.3 long sentences split; Section 3.5 now names **strong convexity** and says the general bound falls as $1/t$ (D1; the bound $L\lVert\mathbf{w}_0-\mathbf{w}^*\rVert^2/(2t)$ shown just above is $O(1/t)$, so the statement follows from the displayed formula).
- Terminology/style: five headings to sentence case ("Gradient descent", "The learning rate", ...); "NumPy" in prose.
- Metadata: description one sentence, 160 characters.
- References: house format with verified volume, issue and pages (see C2), alphabetical (Bottou, Boyd, Goodfellow, Kingma, Nocedal, Polyak, Robbins), "2nd ed.", Kingma and Ba as a conference paper.
- Cross-references: anchors `#33-worked-example` and `#43-worked-example` no longer exist; nothing in `src/` links to them. `#32-many-dimensions-curvature-and-conditioning` (linked from entry 3) unchanged. The slug of `## 3. The learning rate` is unchanged.
- Technical corrections: none. Code unchanged; outputs re-verified.
- Remaining suggestions and why they stay: `acronym-expansion` SIAM, MIT, USSR at `:380–385`: parts of journal and publisher names in the reference list.
- Flags for independent review: fact-check that the Polyak citation should give the English translation (pages 1–17) rather than the Russian original (pages 791–803); the entry previously cited the translation journal, so that choice was kept.
- Vietnamese translation affected: no translation exists. `publishedAt` 2026-10-13, so no `updatedAt`.

## Revision log (wave 2 resolution)

Resolves `reviews/machine-learning-fundamentals.md` F1, T1, T4, F2.
- F1: Adam library defaults no longer claimed to match the paper; PyTorch (same values) and Keras 3 ($\epsilon = 10^{-7}$, the paper's "epsilon hat") named, verified against both libraries' documentation on 2026-10-15 (`:322`).
- T1: divisor-$n$ standard deviation stated where $z$ is defined (`:186`) and at the $H = 2I$ claim (`:213`); recomputed: eigenvalues 2, 2 with `ddof=0`, 1.9, 2 with `ddof=1`.
- T4: Exercise 2 now $\ln(10^{-6})/\ln(99/101) \approx 691$ (recomputed 690.75) (`:342`).
- F2: "The most widely used is Adam" became "A widely used one is Adam" (`:315`).
- Code and outputs unchanged. Lint: 0 errors, 0 warnings; syntax compiles.
- Meaning changes for the translation follow-up (no translation exists yet): Sections 3.4 and 5, Exercise 2.

## Revision log (QA findings)

Resolves `reviews/machine-learning-fundamentals.md` Q1 and Q2.
- Prose: the 54-word sentence at `:186` split in two ("... feature $z = (x - \bar{x})/s_x$. When $s_x$ is the standard deviation computed with divisor $n$ ..., $z$ has mean 0 and standard deviation 1 on the training set."), serial comma removed in it; serial comma removed at `:262`; entry 3's title in the link text at `:376` without the serial comma. Kept: `:322` (list across a display equation, second item ends in a parenthetical of formulas); `:213` is a clause series.
- Lint: 0 errors, 0 warnings; the `sentence-length` suggestion at `:186` is gone. No heading, anchor, code or number changed.
