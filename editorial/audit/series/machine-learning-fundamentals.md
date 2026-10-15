# Series audit: Machine Learning Fundamentals

- Series: `machine-learning-fundamentals` (4 entries, status published, no planned entries); overview `src/content/series/machine-learning-fundamentals.md`
- Audited at commit `e21dcc8`, 2026-10-13, wave 1 (content audit, then developmental and copy revision). The earlier series review `reviews/machine-learning-fundamentals.md` (F1–F16, resolved) was read first; none of its corrections was undone.

## Structural consistency across entries

| Entry | Opening (builds on, versions) | Numbered sections | Exercises | Summary table + lead-on | References |
|---|---|---|---|---|---|
| 1 Learning from Data | yes; Python 3.13, NumPy 2.5.3, seed policy | 1–6 | §7 (4, with answers) | §8; leads to entry 2 | 5 books |
| 2 Gradient Descent | yes; links entry 1 §5 | 1–5 | §6 (4) | §7; leads to entry 3 | 7 |
| 3 Generalization | yes; links entries 1, 2, 4 | 1–5 | §6 (4) | §7; leads to entry 4 | 7 |
| 4 Evaluating Models | yes; links entries 1, 3 | 1–6 | §7 (5) | §8; closes the series | 8 |

Consistent: every entry numbers its sections, numbers Exercises and Summary, and puts `### References` under the Summary. Before revision all four used title-case section headings, and all four reference lists used the "vol(issue), year" style without pages and out of alphabetical order; both are now fixed throughout.

## Notation and terminology

- Consistent across entries: $\mathbf{w}$, $X$ (design matrix with a leading column of ones), $n$, $p = d + 1$, $\hat{R}_n$, $R$, $\sigma^2$, $f^*$, "fresh-data MSE", "irreducible error", MSE without the factor 1/2.
- Eigenvalue symbol: entry 2 uses $\lambda_i$, entry 3 uses $\mu_i$ (because $\lambda$ is the ridge strength) and says so explicitly; acceptable.
- "Bias" in three senses (intercept, estimator bias, evaluation bias): entries 1, 3 and 4 each flag the distinction; consistent.
- House forms: "data set" throughout (the only "Dataset" is the published title of the Quiñonero-Candela et al. book, which keeps its spelling). "numpy" (prose) changed to the library's proper name "NumPy" in all five files; code is unchanged. Note for the orchestrator: other series (DSP, numerical simulation, sensor systems) also write "numpy" in prose; a glossary entry would settle it site-wide.
- Percent: "2 %" style replaced by "2%" in prose.

## Overlap and gaps

- No harmful duplication: entry 4 refers back to entry 1's rule and entry 3's simulation instead of repeating them; entry 3 refers back to entry 2 for conditioning and to entry 1 for the optimal predictor.
- Standardization is introduced in entry 2 §3.4 and its leakage aspect in entry 4 §4.2, with explicit forward and backward references. Good.
- Gap (optional): classification is defined in entry 1 and used in entry 4, but no entry fits a classifier by gradient descent beyond the logistic-regression gradient formula in entry 2 §1.1. The objectives do not promise it, so this is not a defect.
- Seed disclosure: entries 1, 2, 3 and 4 state seeds and, after the earlier series review, the spread over seeds where a result depends on it.

## Overview page (standards 6.5)

Before: one paragraph with reader, prerequisites and a topic list; no sequence rationale, no account of how the entries connect, conventions only implicit. After wave 1: three paragraphs (reader and prerequisites; the question each entry answers and how the next takes it up; shared conventions). Objectives (4, each beginning with an assessable verb) unchanged and each met: Formulate (entry 1 §1–3), Explain gradient-based optimization (entry 2 §2–5), Distinguish training and generalization error (entry 1 §5–6, entry 3 §1–3), Identify leakage and bias (entry 4 §4–5). The last entry's closing paragraph now states this mapping in reader terms.

## Cross-references

- Checked every internal link and section citation in the four entries: `/blog/learning-from-data#5-worked-example-least-squares-on-synthetic-data`, `#33-empirical-risk` and `/blog/gradient-descent-and-its-variants#32-many-dimensions-curvature-and-conditioning` keep their slugs after the case change. `eos lint` reports no `series-crossref` or `section-reference` problems.
- Slugs that changed: entry 1 `#6-what-empirical-risk-does-and-does-not-tell-us` → `#6-what-empirical-risk-does-and-does-not-reveal`; entry 2 `#33-worked-example` → `#33-worked-example-four-learning-rates`, `#43-worked-example` → `#43-worked-example-batch-size-and-schedule`; entry 3 `#21-the-set-up` → `#21-the-setup`. A grep of `src/` found no link to any of them, inside or outside this series.
- Ordinal references ("the third entry", "the fourth entry") all point to the right entries.

## Vietnamese

None of the four articles has a translation. The series overview has one (`src/content/series/vi/machine-learning-fundamentals.md`); its body and description no longer match the revised English overview. No copied field (status, category, example, plannedEntries) changed.
