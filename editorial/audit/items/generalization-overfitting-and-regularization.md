<!-- audit: {"slug":"generalization-overfitting-and-regularization","type":"article","series":"machine-learning-fundamentals","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":5}} -->
# Audit: Generalization, Overfitting, and Regularization

- Path: `src/content/blog/generalization-overfitting-and-regularization.mdx` · Route: `/blog/generalization-overfitting-and-regularization` · Type: article (series entry) · Series `machine-learning-fundamentals`, entry 3 of 4 · Words: 3504 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4
- structure 4
- accuracy 4: all three Python blocks rerun (Python 3.13.16, NumPy 2.5.3): identical output. Recomputed the seed-variation claim of Section 2.3 over seeds 0–20: best degree 3 for 14 seeds, 5 for 6, 7 for 1; first degree with fresh-data MSE above 1 ranges 7–15, as stated. Sorted seed-9 training inputs confirm the gap 0.065–0.287 and the extremes 0.006 and 0.983. Checked algebraically: an unpenalized intercept means adding a constant $c$ to every label shifts $w_0$ by $c$ and leaves the other weights unchanged ($X\mathbf{e}_0 = \mathbf{1}$, $D\mathbf{e}_0 = \mathbf{0}$).
- evidence 3: "12(1), 1970" style, no pages, not alphabetical, "2nd edition"; Belkin et al. title not in its original case.
- language 3: contraction "can't" (summary table); "simply" ×2, "very" ×3, "essentially"; several sentences of 49–55 words; "It is often the most effective remedy" (unsupported).
- consistency 3: four title-case headings; "set-up" as a noun; "mean squared error or MSE".
- publishing 2: description 351 characters.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 351 characters. |
| C1 | Should fix | `:21`, `:37`, `:104`, `:268` | consistency | Title-case headings. |
| C2 | Should fix | `:330–336` | evidence | Reference format and order. |
| C3 | Should fix | `:318` | language | Contraction "Why can't the training error choose the model?". |
| D1 | Should fix | `:263` | evidence | "It is often the most effective remedy when available." Unsupported general claim. |
| C4 | Optional | `:94`, `:196` | language | "simply does not contain"; "simply shifts the fit" (vague: what shifts?). |
| C5 | Optional | `:15`, `:98`, `:182`, `:299` | language | "that very error", "The very large errors", "Very large modern models", "essentially zero". |
| C6 | Optional | `:100`, `:129`, `:174`, `:176`, `:182`, `:202`, `:204` | language | Sentences of 47–55 words. |
| C7 | Optional | `:19` | language | "mean squared error or MSE" inside a parenthesized list. |
| C8 | Optional | `:39` | consistency | "The set-up" (noun is "setup"). |

### D1. Unsupported ranking of remedies
- **Where:** `:263`, Section 4.4
- **Text:** "It is often the most effective remedy when available."
- **Problem:** a comparative claim with no evidence in the entry or a source. What the entry does establish is that the variance term falls as $1/n$ and that more data adds no bias.
- **Correction:** "Unlike the other remedies, more data reduces the variance without adding bias, but it is often expensive or impossible to obtain."

### C2. References
- **Where:** `:330–336`
- **Problem:** house format needs vol./no./pp.; order Belkin, Bishop, Geman, Goodfellow, Hastie, Hoerl, Tibshirani; titles in original spelling (Belkin et al. is printed in sentence case).
- **Correction:** verified details: Hoerl and Kennard, *Technometrics* vol. 12, no. 1, pp. 55–67 (CMU-hosted scan); Tibshirani, JRSS B vol. 58, no. 1, pp. 267–288 (scan of the paper); Geman et al., *Neural Computation* vol. 4, pp. 1–58 (scan; issue 1 from the DOI 10.1162/neco.1992.4.1.1); Belkin et al., PNAS vol. 116, no. 32, pp. 15849–15854 (NSF PAR record; DOI 10.1073/pnas.1903070116).

## Revision log (wave 1)

- Structure: Section 3.2's long paragraph split into three (projection matrix; the two definitions; the derivation), no content change.
- Prose: "simply", "very", "essentially" removed where they added nothing; the intercept sentence now says exactly what shifts; seven long sentences split; Section 4.4 "More data" claim replaced (D1); summary row reworded without the contraction; the vocabulary list in the opening moved out of parentheses so MSE is expanded as "mean squared error (MSE)".
- Terminology/style: headings to sentence case; "2.1 The setup"; "NumPy".
- Metadata: description one sentence, 161 characters.
- References: house format with verified details (C2), alphabetical, "2nd ed."; Belkin et al. title in its original sentence case.
- Cross-references: anchor `#21-the-set-up` became `#21-the-setup` (no links to it in `src/`); others unchanged.
- Technical corrections: none. Code unchanged; outputs re-verified.
- Remaining suggestions and why they stay: `acronym-expansion` MIT at `:337` (publisher name in the reference list).
- Flags for independent review: technical reviewer may confirm the D1 replacement sentence ("reduces the variance without adding bias") for the polynomial setting of the entry: with a fixed model family the bias term does not depend on $n$ in the fixed-design formula, which is how the entry uses it.
- Vietnamese translation affected: no translation exists. `publishedAt` 2026-10-13, so no `updatedAt`.

## Revision log (wave 2 resolution)

Resolves `reviews/machine-learning-fundamentals.md` T2, T5, T6, F3 (entry 3 part).
- T2: "Unlike the other remedies," removed from the more-data item (`:267`); averaging models also reduces variance without changing the bias.
- T5: test-error standard deviation now "shrinks in proportion to $1/\sqrt{m}$" (`:31`).
- T6: cyclic-trace reason and the linear-independence condition added to the trace-of-projection step (`:133`).
- F3: Hoerl and Kennard (1970) attached to ridge (`:194`), Tibshirani (1996) to the lasso (`:255`), Geman, Bienenstock and Doursat (1992) to the decomposition (`:108`).
- Code and outputs unchanged. Lint: 0 errors, 0 warnings; syntax compiles.
- Meaning changes for the translation follow-up (no translation exists yet): Sections 1.1, 3.1, 3.2, 4.1, 4.2, 4.4.

## Revision log (QA findings)

Resolves `reviews/machine-learning-fundamentals.md` Q1.
- Metadata: title "Generalization, Overfitting and Regularization" (no serial comma, standards 5.1); slug `generalization-overfitting-and-regularization` unchanged, so every link still resolves.
- Prose: serial comma removed at `:15` ("why and what can be done about it"). Kept: `:143` (last item "the squared bias and the variance" contains "and"); `:96`, `:108`, `:249` are independent clauses or close a parenthetical.
- Lint: 0 errors, 0 warnings. No heading, anchor, code or number changed.
