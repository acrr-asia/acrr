# Series review: Machine Learning Fundamentals

- Series: `machine-learning-fundamentals` (4 articles, status published, 0 planned entries)
- Reviewed commit: 9232ed9 (the series' content was last changed in d0a5aa8, "Audit and revise the Machine Learning Fundamentals series (wave 1)")
- Date: 2026-10-14
- Review type: independent review, wave 2 (fact-check, technical review and series review in one report; the reviewer did not write or revise any of this text)

## Summary

The series is accurate and well built. All eleven Python blocks reproduce their printed output byte for byte with Python 3.13.16 and NumPy 2.5.3, every number in the prose that can be recomputed was recomputed and is right (including the seed-variation claims added after the first review), and all 27 entries in the four reference lists exist with the bibliographic details given. The wave-1 attributions to Cawley and Talbot and to Dietterich are supported by the papers. There are no blocking findings. The five should-fix findings are local: the claim that library defaults for Adam match the paper is not true of Keras (entry 2); the exact result $H = 2I$ after standardization depends on the divisor-$n$ convention, which is not stated (entry 2); a sentence added in wave 1 says that only more data reduces variance without adding bias, which the entry's own "averaging models" remedy contradicts (entry 3); the definition of label shift leaves out the condition that makes it a special case (entry 4); and the standard error and the confidence interval are used in entry 4 without being said to be what they are. The series is ready as published once those five are corrected.
Findings: 0 blocking, 5 should fix, 6 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Formulate a supervised learning problem in terms of a model, a loss function, and a data set. | Entry 1, Sections 1–3 (examples, models, loss functions, risk, ERM); Section 5 worked example | Met. |
| Explain gradient-based optimization and the role of the learning rate. | Entry 2, Sections 2–5 (update rule, $0 < \eta < 2/\lambda_{\max}$, conditioning, SGD, schedules, momentum, Adam) | Met. |
| Distinguish training error from generalization error, and explain why held-out evaluation matters. | Entry 1, Sections 3 and 6; entry 3, Sections 1–3 and 5; entry 4, Section 2 | Met. |
| Identify common sources of data leakage and bias in an evaluation setup. | Entry 4, Sections 4 and 5 (with the summary table in Section 4.7) | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Should fix | `src/content/blog/gradient-descent-and-its-variants.mdx` | Section 5 (line 322) | Stated versions and defaults | "library implementations generally use the same values": Keras 3 uses $\epsilon = 10^{-7}$, not $10^{-8}$. |
| T1 | Should fix | `src/content/blog/gradient-descent-and-its-variants.mdx` | Section 3.4 (lines 186, 213) | Stated versions and defaults | $H = 2I$ after standardization holds only with the divisor-$n$ standard deviation; the convention is not stated. |
| T2 | Should fix | `src/content/blog/generalization-overfitting-and-regularization.mdx` | Section 4.4 (line 267) | Technical accuracy | "Unlike the other remedies, more data reduces the variance without adding bias" is contradicted by the averaging remedy two lines below. |
| T3 | Should fix | `src/content/blog/evaluating-models-honestly.mdx` | Section 5.1 (line 300) | Technical accuracy | Label shift defined only as "the class proportions change", without $P(\mathbf{x} \mid y)$ fixed. |
| S1 | Should fix | `src/content/blog/evaluating-models-honestly.mdx` | Section 6.1 (line 318) | Concept introduction | Standard error and confidence interval used without saying what they are. |
| T4 | Optional | `src/content/blog/gradient-descent-and-its-variants.mdx` | Section 6, Exercise 2 (line 342) | Technical accuracy | $\ln(10^{-6})/\ln(0.980)$ is 684, not 690; 690 comes from the unrounded $99/101$. |
| T5 | Optional | `src/content/blog/generalization-overfitting-and-regularization.mdx` | Section 1.1 (line 31) | Technical accuracy | "a standard deviation of order $1/\sqrt{m}$" omits the loss's own spread; "proportional to" is meant. |
| T6 | Optional | `src/content/blog/generalization-overfitting-and-regularization.mdx` | Section 3.2 (line 133) | Concept introduction | "the trace of a projection matrix equals the dimension" is asserted without the one-line reason or the full-rank condition. |
| F2 | Optional | `src/content/blog/gradient-descent-and-its-variants.mdx` | Section 5 (line 315) | Evidence | "The most widely used is Adam": an unsourced superlative. |
| F3 | Optional | `generalization-overfitting-and-regularization.mdx`, `evaluating-models-honestly.mdx` | References (entry 3 lines 336, 339, 340; entry 4 lines 408, 410) | Evidence | Five listed works (Geman et al., Hoerl and Kennard, Tibshirani, Kaufman et al., Stone) are never attached to the claims they support. |
| S2 | Optional | `src/content/series/machine-learning-fundamentals.md` | Body (line 13) | Overview completeness | The overview names neither the stated seed policy's caveat (digits may differ with other NumPy versions) nor where the entries recall extra mathematics; minor, entry 1 states both. |

### F1. Adam defaults in libraries
- **Where:** `src/content/blog/gradient-descent-and-its-variants.mdx:322`, section "5. Momentum and adaptive methods"
- **Text:** "The defaults proposed in the original paper are $\beta_1 = 0.9$, $\beta_2 = 0.999$ and $\epsilon = 10^{-8}$; library implementations generally use the same values, but check the documentation of the version in use."
- **Problem:** The paper's values are right (Kingma and Ba, arXiv:1412.6980, Algorithm 1). But the Keras 3 API documentation (keras.io/api/optimizers/adam/, fetched 2026-10-14) gives `keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07, ...)` and notes that this epsilon is the "epsilon hat" of the paper's alternative formulation, not the $\epsilon$ of Algorithm 1. PyTorch (`torch.optim.Adam`, documentation version 2.14, fetched 2026-10-14) uses `eps=1e-08`. One of the two most common libraries differs, so "generally use the same values" misleads a reader who copies hyperparameters from one library to another. Standards 5.3 ("Name versions") and the series-review dimension "Stated versions and defaults" apply.
- **Recommended correction:** Replace from "; library implementations" to the end of the sentence with: ". Library defaults do not always match: PyTorch's `torch.optim.Adam` uses the same three values, while Keras 3's `Adam` uses $\epsilon = 10^{-7}$ (applied in a slightly different place in the update), so check the documentation of the library and version in use."

### T1. Standardization and the divisor of the standard deviation
- **Where:** `src/content/blog/gradient-descent-and-its-variants.mdx:186` and `:213`, section "3.4 Feature scaling"
- **Text:** "the **standardized** feature $z = (x - \bar{x})/s_x$, which has mean 0 and standard deviation 1 on the training set" and "With a centered feature of unit variance, $\frac{1}{n}X^\top X$ is the identity matrix, so $H = 2I$, both eigenvalues equal 2, and $\eta = 0.5$ reaches the minimum in a single step."
- **Problem:** $\frac{1}{n}\sum_i z_i^2 = 1$ only when $s_x$ is computed with divisor $n$, which is what the code does (`x.std()`, NumPy's default `ddof=0`). With the divisor $n - 1$ that many readers and libraries use for "the standard deviation", $\frac{1}{n}\sum_i z_i^2 = (n-1)/n = 0.95$ for $n = 20$, so $H = \operatorname{diag}(2, 1.9)$: the eigenvalues are 2 and 1.9, not equal, and $\eta = 0.5$ no longer reaches the minimum in one step. The exact result depends on a convention the prose does not state (standards 5.5, "State conventions that a result depends on"). The series already uses this convention explicitly elsewhere (entry 1, Exercise 2: "the sample variance (with divisor $n$)").
- **Recommended correction:** At line 186, after "$z = (x - \bar{x})/s_x$", insert ", where $s_x$ is the standard deviation computed with divisor $n$ (NumPy's default for `x.std()`)". At line 213, change "With a centered feature of unit variance" to "With a centered feature whose mean square is 1 (the divisor-$n$ convention)".

### T2. "Unlike the other remedies" (sentence added in wave 1)
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:267`, section "4.4 Other remedies"
- **Text:** "Unlike the other remedies, more data reduces the variance without adding bias, but it is often expensive or impossible to obtain."
- **Problem:** The fixed-design reasoning behind the main clause is right (the bias term of Section 3.1 does not depend on $n$ for a fixed model family, and $\sigma^2 p/n$ falls with $n$), so the first half of the wave-1 flag is confirmed. The contrast with "the other remedies" is not: the list continues at line 270 with "**Averaging models.** ... reduces variance, because the fluctuations of the individual models partly cancel", and averaging identically distributed fitted models leaves their expected prediction, and therefore the bias, unchanged (Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, 2nd ed., Section 15.2, make this point for bagged trees; the book is in the entry's reference list). Data augmentation with transformations that truly preserve the label (line 269) also does not by itself add bias. The comparative is therefore false as stated for at least one item of the same list.
- **Recommended correction:** "More data reduces the variance without adding bias, but it is often expensive or impossible to obtain."

### T3. Definition of label shift
- **Where:** `src/content/blog/evaluating-models-honestly.mdx:300`, section "5.1 Unrepresentative data and distribution shift"
- **Text:** "Common special cases are **covariate shift**, where the distribution of the inputs changes but the relation $P(y \mid \mathbf{x})$ does not, and **label shift**, where the class proportions change."
- **Problem:** A special case of distribution shift is defined by what stays fixed, as the covariate-shift half of the sentence does. As written, any shift in which the class proportions $P(y)$ change qualifies as label shift, including shifts in which $P(y \mid \mathbf{x})$ or $P(\mathbf{x} \mid y)$ also change, so the term no longer names a special case. The standard definition keeps the class-conditional input distribution $P(\mathbf{x} \mid y)$ fixed; that invariant is what lets label shift be corrected by reweighting classes. The reader is left with an imprecise definition of a term the entry introduces in bold.
- **Recommended correction:** "... and **label shift**, where the class proportions $P(y)$ change but the distribution of the inputs within each class, $P(\mathbf{x} \mid y)$, does not."

### S1. Standard error and confidence interval not introduced
- **Where:** `src/content/blog/evaluating-models-honestly.mdx:318`, section "6.1 Uncertainty of a test score" (forward reference at `:29`; also mentioned in `src/content/blog/learning-from-data.mdx:151`)
- **Text:** "A test accuracy $\hat{p}$ measured on $m$ independent examples is an average of $m$ zero-one values, so its standard error is approximately $\sqrt{\hat{p}(1 - \hat{p})/m}$, and for large $m$ an approximate 95% confidence interval is $\hat{p} \pm 1.96\sqrt{\hat{p}(1 - \hat{p})/m}$ (the normal approximation)."
- **Problem:** The series' stated prerequisites are expected value, variance and the normal distribution (overview line 13; entry 1 line 21), and the overview says each entry recalls any further idea where it first uses it. "Standard error" and "confidence interval" are used here, and the confidence interval is the recommended way to report a score (Section 6.2 table, "A score without an interval cannot be compared"), but neither is said to be what it is: that the standard error is the standard deviation of the estimate over repeated test sets, and that a 95% interval is produced by a rule that covers the true value in 95% of repeated samples. The ingredients are in the series (entry 1 Section 3.3; entry 4 line 74 computes the same quantity as "a standard deviation"), so only the definitions are missing. Not raised to blocking because the concept is a reporting tool rather than what the series is about, and its derivation from the prerequisites is otherwise present.
- **Recommended correction:** Replace the sentence with: "A test accuracy $\hat{p}$ measured on $m$ independent examples is an average of $m$ zero-one values. Its **standard error**, the standard deviation of such an estimate over repeated test sets of the same size (Section 3.3 of the first entry), is approximately $\sqrt{\hat{p}(1 - \hat{p})/m}$. A **95% confidence interval** is an interval computed from the sample by a rule that, over repeated samples, contains the true value 95% of the time. For large $m$ the average is approximately normally distributed, and the rule $\hat{p} \pm 1.96\sqrt{\hat{p}(1 - \hat{p})/m}$ gives such an interval (the normal approximation)."

### T4. Step count in Exercise 2 of entry 2
- **Where:** `src/content/blog/gradient-descent-and-its-variants.mdx:342`, section "6. Exercises"
- **Text:** "so reducing it by a factor of $10^6$ takes about $\ln(10^{-6})/\ln(0.980) \approx 690$ steps."
- **Problem:** Recomputed: $\ln(10^{-6})/\ln(0.980) = 683.8$; $\ln(10^{-6})/\ln(99/101) = 690.75$. The printed expression and the printed value use different roundings of the factor.
- **Recommended correction:** "... takes about $\ln(10^{-6})/\ln(99/101) \approx 691$ steps."

### T5. "Of order $1/\sqrt{m}$"
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:31`, section "1.1 The two quantities"
- **Text:** "With $m$ test examples the test error has a standard deviation of order $1/\sqrt{m}$ around the risk"
- **Problem:** The standard deviation is $\sigma_\ell/\sqrt{m}$, where $\sigma_\ell$ is the standard deviation of the per-example loss; "of order $1/\sqrt{m}$" reads as if the constant were 1. Entry 1 (line 151) says it correctly: "shrinks in proportion to $1/\sqrt{n}$".
- **Recommended correction:** "has a standard deviation around the risk that shrinks in proportion to $1/\sqrt{m}$".

### T6. Trace of a projection matrix
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:133`, section "3.2 Variance grows with the number of parameters"
- **Text:** "and the trace of a projection matrix equals the dimension of the space it projects onto, here the number of parameters $p$."
- **Problem:** The fact is correct but is the one step of the derivation the reader cannot check from what precedes it, and it needs the columns of $X$ to be linearly independent (true for every degree used, all below 20 with distinct inputs).
- **Recommended correction:** "and the trace of a projection matrix equals the dimension of the space it projects onto (its eigenvalues are 0 or 1, and $\operatorname{tr} P = \operatorname{tr}\big((X^\top X)^{-1}X^\top X\big) = p$ when the $p$ columns of $X$ are linearly independent)."

### F2. "The most widely used"
- **Where:** `src/content/blog/gradient-descent-and-its-variants.mdx:315`, section "5. Momentum and adaptive methods"
- **Text:** "The most widely used is **Adam** (Kingma and Ba)"
- **Problem:** A superlative about usage with no source (standards 7.2). Nothing in the entry depends on the ranking.
- **Recommended correction:** "A widely used one is **Adam** (Kingma and Ba)".

### F3. Listed works not attached to claims
- **Where:** entry 3 references at `src/content/blog/generalization-overfitting-and-regularization.mdx:336, 339, 340`; entry 4 references at `src/content/blog/evaluating-models-honestly.mdx:408, 410`
- **Text:** Geman et al. (1992), Hoerl and Kennard (1970), Tibshirani (1996); Kaufman et al. (2012), Stone (1974)
- **Problem:** Wave 1 attached Belkin, Ambroise, Cawley, Dietterich and Quiñonero-Candela to their claims; these five specific papers remain unattached, so the reader cannot tell which claim each supports (standards 6.1). They are the original sources of the ridge and lasso, an early systematic treatment of cross-validation, and a formal treatment of leakage, so the attachment is natural.
- **Recommended correction:** Entry 3, line 194 after "adds a penalty on the size of the weights to the objective": "(Hoerl and Kennard, 1970)"; line 255 after "The **lasso**": "(Tibshirani, 1996)"; line 104 section 3.1, end of the first paragraph: "Geman, Bienenstock and Doursat (1992) discuss the decomposition for neural networks." Entry 4, line 104 after "**Cross-validation** (CV)": "(Stone, 1974, is an early systematic treatment)"; line 186, end of the first paragraph: "Kaufman et al. (2012) give a formal definition and methods for detecting and avoiding it."

### S2. Overview: reproducibility caveat
- **Where:** `src/content/series/machine-learning-fundamentals.md:17`
- **Text:** "Every data set is synthetic and generated with a stated seed, so the true relation and the irreducible error are known and each number can be reproduced."
- **Problem:** Entry 1 (line 23) adds the necessary qualification that the digits are reproducible "with the same NumPy version (other versions may produce different random streams)". The overview states the conventions shared by all entries (standards 6.5) and is where a reader decides whether to run the code; the unqualified "each number can be reproduced" overstates slightly.
- **Recommended correction:** "... so the true relation and the irreducible error are known and each number can be reproduced with the stated NumPy version."

## Concept introduction map

| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Supervised learning, example, feature, label | `learning-from-data.mdx:15` | `learning-from-data.mdx:15, 36–39, 45` | Good. |
| i.i.d. assumption, data-generating distribution | `learning-from-data.mdx:73` | `learning-from-data.mdx:73` | Good. |
| Loss function, squared/absolute/zero-one/cross-entropy loss | `learning-from-data.mdx:100` | `learning-from-data.mdx:100–115` | Good. |
| Logistic (sigmoid) function | `learning-from-data.mdx:113` | `learning-from-data.mdx:113`; reused `gradient-descent-and-its-variants.mdx:32` | Good. |
| Risk, empirical risk, ERM, Bayes risk | `learning-from-data.mdx:121` | `learning-from-data.mdx:121–163` | Good. |
| Gradient, normal equations, design matrix | `learning-from-data.mdx:92, 198` | `learning-from-data.mdx:92, 198–204` | Good. |
| Hessian, eigenvalues and eigenvectors, condition number | `gradient-descent-and-its-variants.mdx:113` | `gradient-descent-and-its-variants.mdx:113–130` (recalled where used, as the opening promises) | Good. |
| Convexity, $L$-smoothness, strong convexity, saddle point | `gradient-descent-and-its-variants.mdx:221` | `gradient-descent-and-its-variants.mdx:221–229` | Good. |
| Mini-batch, epoch, learning-rate schedule | `gradient-descent-and-its-variants.mdx:243` | `gradient-descent-and-its-variants.mdx:243–258` | Good. |
| Capacity, underfitting, overfitting | `generalization-overfitting-and-regularization.mdx:17` | `generalization-overfitting-and-regularization.mdx:17, 35, 94–96` | Good. |
| Bias, variance (estimator sense), fixed design | `generalization-overfitting-and-regularization.mdx:108` | `generalization-overfitting-and-regularization.mdx:108–125` | Good; the three senses of "bias" are separated at `:125` and in entry 4 `:32`. |
| Projection matrix, covariance matrix, trace | `generalization-overfitting-and-regularization.mdx:129` | `:129` (projection, by its properties), `:131` (covariance, trace) | Adequate; the trace property is asserted (T6, optional). |
| Ridge, lasso, elastic net, early stopping | `generalization-overfitting-and-regularization.mdx:194` | `:194–263`; early stopping first named `gradient-descent-and-its-variants.mdx:88` with a forward reference | Good. |
| Hoeffding's inequality, union bound | `evaluating-models-honestly.mdx:40` | `evaluating-models-honestly.mdx:40–46, 76` | Good. |
| Cross-validation, folds, stratification, nested CV | `evaluating-models-honestly.mdx:104` | `evaluating-models-honestly.mdx:104–112, 180` | Good. |
| Data leakage, group split, target leakage | `evaluating-models-honestly.mdx:186` | `evaluating-models-honestly.mdx:186–281` | Good. |
| Covariate shift, label shift | `evaluating-models-honestly.mdx:300` | `evaluating-models-honestly.mdx:300` | Label shift definition incomplete (T3). |
| Standard error, confidence interval | `learning-from-data.mdx:151`; `evaluating-models-honestly.mdx:29` | not introduced (used at `evaluating-models-honestly.mdx:318`) | S1. |
| McNemar's test, paired comparison | `evaluating-models-honestly.mdx:320` | `evaluating-models-honestly.mdx:320` (what it counts and tests) | Adequate for the stated purpose. |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| Python 3.13, NumPy 2.5.3 | All code blocks | Yes: overview `:17`; entry 1 `:23`; entry 2 `:17`; entry 3 `:19`; entry 4 `:17` | Good; outputs reproduced with Python 3.13.16 and NumPy 2.5.3. |
| `default_rng` streams depend on NumPy version | All seeded examples | Yes, entry 1 `:23` | Good; overview omits it (S2, optional). |
| MSE without the factor 1/2 | Every MSE | Yes: overview `:17`; entry 1 `:115` | Good; consistent with gradients $\frac{2}{n}X^\top(X\mathbf{w}-\mathbf{y})$ in entries 1–2 and the ridge normal equations in entry 3. |
| Classes coded $\{0, 1\}$ | Cross-entropy, logistic regression, accuracy | Yes: overview `:17`; entry 1 `:50` | Good. |
| Natural logarithm (nats) | Cross-entropy, Hoeffding | Yes: entry 1 `:113`; Exercise 1 | Good. |
| Standard deviation with divisor $n$ in standardization | Entry 2 `:186, 200, 213` | No (code only) | T1. |
| Variance with divisor $n$ in Exercise 2 of entry 1 | Entry 1 `:284` | Yes | Good. |
| Intercept unpenalized in ridge; $D$ with zero first entry | Entry 3 `:200–206`; entry 4 code | Yes | Good; checked algebraically (below). |
| Polynomial features in $t = 2x - 1$ | Entries 3–4 code | Yes, entry 3 `:49` | Good. |
| Adam defaults | Entry 2 `:322` | Paper values stated; library defaults overstated | F1. |
| Eigenvalue symbol $\lambda_i$ vs $\mu_i$ | Entry 2 `:125`; entry 3 `:261` | Yes, the change is explained at entry 3 `:261` | Good. |
| Normal-approximation interval conditions | Entry 4 `:318` | Yes ("$m$ large enough and $\hat{p}$ not too close to 0 or 1") | Good. |

## Series design

**Purpose, audience and scope.** The overview (`src/content/series/machine-learning-fundamentals.md:13`) names the reader (can program; derivatives, vectors and matrices, basic probability), says that further ideas are recalled where first used, and the entries keep that promise (eigenvalues in entry 2 Section 3.2, covariance matrix and trace in entry 3 Section 3.2, Hoeffding's inequality in entry 4 Section 2.1), except for the confidence interval (S1). Unsupervised learning is excluded explicitly in entry 1 Section 1.2. The four objectives each begin with an assessable verb and each is met (table above).

**Sequence and rationale.** Problem, optimizer, generalization, evaluation is the right order for this reader: each entry resolves a question the previous one leaves open, and the overview's second paragraph (`:15`) says so entry by entry. No entry would serve the reader better moved, split or merged. Entry 3's choice of $\lambda$ by peeking at fresh data is deliberately deferred to entry 4, and both entries say so (entry 3 Section 5, entry 4 opening and Section 3.2).

**Prerequisites and dependencies.** Nothing depends on a later entry. Forward references (early stopping in entry 2 Section 2.3 to entry 3; standardization on the training set only in entry 2 Section 3.4 to entry 4 Section 4.2; confidence intervals in entry 1 Section 3.3 to entry 4) are announcements, not dependencies.

**Notation and depth.** $\mathbf{w}$, $X$ with a leading column of ones, $n$, $p = d + 1$, $\hat{R}_n$, $R$, $\sigma^2$ and $f^*$ are used identically in all four entries; the switch from $\lambda_i$ to $\mu_i$ for eigenvalues is explained. Depth is comparable: every entry has a derivation, at least one runnable worked example with stated seeds and multi-seed context where a result depends on the seed, four or five exercises with answers, a summary table and references.

**Overview completeness.** The overview states the sequence rationale, what each entry contributes, the shared conventions and checkable objectives (standards 6.5). It promises nothing the entries do not deliver. One small qualification is missing (S2).

## Series-level notes

- **Cross-reference map (all checked against the targets):** entry 2 → entry 1 Section 5 (`#5-worked-example-least-squares-on-synthetic-data`, resolves; link text matches); entry 3 → entry 2 Section 3.2 (`#32-many-dimensions-curvature-and-conditioning`, resolves; text matches); entry 4 → entry 1 Section 3.3 (`#33-empirical-risk`, resolves; the cited argument is there). Ordinal references checked: "the first entry's third exercise" (entry 4 `:304`) is Exercise 3 of entry 1 (2% disease), correct; "the second entry showed how much a single run of stochastic gradient descent (SGD) can vary" (entry 4 `:322`) matches entry 2 Section 4.3; "Exercise 3 asks why" (entry 3 `:102`) matches Exercise 3. Every "next entry" closing paragraph names the actual next entry; entry 4 closes against the four objectives.
- **Terminology:** "data set", "fresh-data MSE", "irreducible error", "excess risk", "generalization gap" and "held-out" are used consistently. "Bias" in its three senses is disambiguated in entries 1, 3 and 4.
- **Wave-1 flags resolved by this review:** (1) Polyak: citing the English translation (*USSR Comput. Math. Math. Phys.* 4(5), 1–17) under its English title is correct; Math-Net.ru lists it as the translation of *Zh. Vychisl. Mat. Mat. Fiz.* 4(5), 791–803. No change needed. (2) Entry 3 "more data ... without adding bias": the main clause is confirmed; the comparative is not (T2). (3) Cawley and Talbot: supported (Section 5.3 of the paper: "In many cases, the bias is of similar magnitude to the typical difference observed between competitive learning algorithms"; Section 5.2 notes benchmarks where it is larger). (4) Dietterich: supported (abstract: "For algorithms that can be executed only once, McNemar's test is the only test with acceptable Type I error"). (5) Dietterich issue 7 and (6) Kaufman et al. article 15: see the verification table.
- **Vietnamese:** none of the four articles has a translation. `src/content/series/vi/machine-learning-fundamentals.md` has the old one-paragraph body and the old description, so it no longer matches the revised English overview (copied fields are unchanged, so the build passes). Wave 1 marked it for update, as standards Section 11 requires; it is outside this review.
- **Working tree:** during the review an uncommitted one-line change appeared in `src/content/blog/gradient-descent-and-its-variants.mdx` (tag `numerical-methods` → `numerical methods`), made outside this review. It changes no line number cited here and no content reviewed.

## Verification log

- Build: not run, per the wave-2 brief (parallel reviewers). The prebuilt site `/tmp/claude-0/b2` (built after wave 1 with `SITE_URL=https://acrr.asia`) contains the wave-1 text (checked: "Cawley and Talbot (2010) show" in entry 4, "costs disproportionately more" in entry 1).
- `node scripts/check-links.mjs /tmp/claude-0/b2`: "Checked 314 pages and 9667 internal references ... All internal links resolve."
- Rendered pages `/tmp/claude-0/b2/blog/<slug>.html`: `katex-error` count 0 in all four; Mermaid `min-width` 475px (entry 1), 532px (entry 2), none (entry 3), 288px (entry 4), all under 600px; no letter or punctuation glued to `<strong>`, `<a `, `<code>` or `<em>`.
- `npm run -s eos -- lint machine-learning-fundamentals`: 5 files, 0 errors, 0 warnings, 9 suggestions (entry 4: `sentence-length` at 180 and 300, splitter artifacts before bold-initial sentences, confirmed by reading; `acronym-expansion` for ACM, MIT, SIAM, USSR in reference lists and QR in entry 1, all names rather than abbreviations to expand). Not re-reported.
- `npm run -s eos -- syntax` on the five files: "All files compile."
- Code: all eleven Python blocks extracted and run with `python3 -I` (Python 3.13.16, NumPy 2.5.3); every stdout is byte-identical to the printed output block (entry 1: 1 block; entry 2: 3; entry 3: 3; entry 4: 4).
- Recomputed, entry 1: $a = 0.18120$, $b = -0.29287$, risk of the fitted line $0.25836$, excess $0.00836$ (text 0.2584, 0.0084); cross-entropy $0.105, 2.303, 0.693, 0.223, 1.609$, ratio 7.2 ("about seven times"); MSE 20.4/16.4, MAE 2.4/3.2; $\sigma^2(n-p)/n = 0.225$; Exercise 4, 0.29.
- Recomputed, entry 2: $H = \begin{psmallmatrix}2&1.0247\\1.0247&0.7317\end{psmallmatrix}$, eigenvalues 0.16079 and 2.57091, limit 0.7779, $\kappa = 15.99$, best rate 0.7321, factor 0.8823; per-direction factors 0.992, 0.920, 0.928, 1.057; steps for $10^6$: 110.3 ($\kappa = 16$) and 930.5 ($\kappa = 134.7$), factor 0.985; 1-D table rows for $\eta = 0.1, 0.5, 0.75, 1.1$; Exercise 1 (0.25, 0.125); Exercise 2: 0.0396, 0.9802, 690.75 steps (683.8 with 0.980, T4); Exercise 3 derivation; decayed rate after 999 steps 0.0091. Multi-seed SGD (shuffle seeds 1–20): medians $4.13\times10^{-3}$, $1.91\times10^{-4}$, $4.40\times10^{-5}$; batch-1 constant-rate range $2.48\times10^{-5}$ to $3.05\times10^{-2}$ (text: $2.5\times10^{-5}$ to $3.1\times10^{-2}$), all as stated. Convergence bound $L\lVert\mathbf{w}_0-\mathbf{w}^*\rVert^2/(2t)$ for $\eta = 1/L$ checked against the standard result for convex $L$-smooth functions; Robbins–Monro conditions and the schedule $\eta_0/(1+t/\tau)$ checked.
- Recomputed, entry 3: seeds 0–20, best degree 3 for 14, 5 for 6, 7 for 1; first degree with fresh-data MSE > 1 ranges 7–15 (seed 9: 12); seed-9 sorted training inputs, gap 0.065–0.287, extremes 0.006 and 0.983; exact squared bias in the fixed design 0.19276 (degree 1), 0.0039203 (3), $1.33\times10^{-5}$ (5), $3.4\times10^{-12}$ (9); $0.1047 - 0.09 = 0.0147$ ("within 0.015"); $2.3751/0.2533 = 9.38$ ("almost a factor of ten"); Exercise 1, 0.05; Exercise 3, 0.00045; degree 9 with 2000 examples, fresh-data MSE 0.0903–0.0908 over seeds 0–4 (no overfitting, as stated). Algebra: ridge normal equations $(X^\top X + n\lambda D)\mathbf{w} = X^\top\mathbf{y}$ and Hessian increment $2\lambda D$ from $J_\lambda$; invertibility for $\lambda > 0$ given the column of ones; intercept shift under $\mathbf{y} \to \mathbf{y} + c\mathbf{1}$; early-stopping fraction $1-(1-\eta\mu)^t$ and ridge fraction $\mu/(\mu+2\lambda)$, matching at $2\lambda \approx 1/(\eta t)$ for flat directions; $\operatorname{Cov}(P\mathbf{y}) = \sigma^2 P$, $\operatorname{tr}P = p$.
- Recomputed, entry 4: $\ln 40/0.005 = 737.8$ (738); union-bound deviations 0.1949 ($M = 50$) and 0.1358 ($M = 1$); mean best validation accuracy over seeds 0–199, 0.6127 ("averages 0.61"); CV minimum below 0.09 for seeds 4, 5, 8, 14 among 0–20 (as stated); seed 2: CV chooses $10^{-5}$, test MSE 1.308, fresh-data MSE 0.648, $\lambda = 10^{-2}$ would give 0.142 (as stated); group split seeds 8 and 9: 0.404 and 0.488 (text 0.40, 0.49); standard errors 0.02525 (0.85) and 0.02656 (0.83), half-width 0.0495, Hoeffding half-width for $m = 200$ 0.0960; Exercise 1, 6622.9 (6623).
- Fact-check verification table:

| Claim or reference | Location | Status | Source consulted |
|---|---|---|---|
| Bishop, *PRML*, Springer, 2006 | entry 1 `:328`, entry 3 `:335` | Verified (existence, publisher) | Bookseller and repository listings (Springer, Information Science and Statistics) |
| Hastie, Tibshirani, Friedman, *ESL*, 2nd ed., Springer, 2009 | entries 1, 3, 4 | Verified (second edition, ISBN 9780387848570) | MIT Press Bookstore and library listings |
| James, Witten, Hastie, Tibshirani, *ISL*, Springer, 2013 | entry 1 `:330` | Verified (first edition; a second edition exists, 2021) | statlearning.com and library listings |
| Shalev-Shwartz and Ben-David, CUP, 2014 | entry 1 `:331` | Verified | Library/bookseller listings |
| Vapnik, *The Nature of Statistical Learning Theory*, Springer, 1995 | entry 1 `:332` | Not verified by a fetched source (well-known first edition; no listing retrieved) | none retrieved |
| Bottou, Curtis, Nocedal, *SIAM Review* 60(2), 223–311, 2018 | entry 2 `:380` | Verified | First-page header of the author-hosted PDF (leon.bottou.org) |
| Boyd and Vandenberghe, CUP, 2004; Nocedal and Wright, 2nd ed., Springer, 2006 | entry 2 `:381, 384` | Verified (existence, publisher) | Authors' book pages (ucla.edu, northwestern.edu), WorldCat OCLC 53331084 |
| Goodfellow, Bengio and Courville, *Deep Learning*, MIT Press, 2016 | entry 2 `:382`, entry 3 `:337` | Not verified by a fetched source (well-known; no listing retrieved) | none retrieved |
| Kingma and Ba, Adam, ICLR 2015 | entry 2 `:383` | Verified (arXiv:1412.6980; the arXiv page carries no venue line; ICLR 2015 publication is the standard citation) | arxiv.org/abs/1412.6980 |
| Adam paper defaults $0.9, 0.999, 10^{-8}$ | entry 2 `:322` | Verified | Kingma and Ba, Algorithm 1 |
| Library Adam defaults "generally the same" | entry 2 `:322` | Corrected (F1) | keras.io Adam page (epsilon 1e-07); PyTorch 2.14 `torch.optim.Adam` page (eps 1e-08) |
| Polyak 1964, *USSR Comput. Math. Math. Phys.* 4(5), 1–17 | entry 2 `:385` | Verified (translation of *Zh. Vychisl. Mat. Mat. Fiz.* 4(5), 791–803) | Math-Net.ru record zvmmf7713 |
| Robbins and Monro, *Ann. Math. Statist.* 22(3), 400–407, 1951 | entry 2 `:386` | Verified | Scan of the paper (columbia.edu), journal header |
| Robbins–Monro step-size conditions | entry 2 `:258` | Verified | Same paper; standard result |
| Belkin et al., PNAS 116(32), 15849–15854, 2019; title in sentence case | entry 3 `:334` | Verified | NSF PAR record; author PDF (title, abstract: interpolating models "often obtain high accuracy on test data") |
| Geman, Bienenstock, Doursat, *Neural Computation* 4(1), 1–58, 1992 | entry 3 `:336` | Verified | ML Anthology record, DOI 10.1162/neco.1992.4.1.1 |
| Hoerl and Kennard, *Technometrics* 12(1), 55–67, 1970 | entry 3 `:339` | Verified | CMU-hosted scan (path VOL-12-01/v1201055) |
| Tibshirani, JRSS B 58(1), 267–288, 1996 | entry 3 `:340` | Verified | Scan with journal header (washington.edu) |
| Ambroise and McLachlan, PNAS 99(10), 6562–6566, 2002; supports feature-selection leakage | entry 4 `:196, 403` | Verified | Scan of the paper, header "6562–6566 · PNAS · May 14, 2002 · vol. 99 · no. 10"; text on optimistic CV error within gene selection |
| Cawley and Talbot, JMLR 11, 2079–2107, 2010; optimism comparable to differences between methods | entry 4 `:180, 404` | Verified | jmlr.org abstract page and PDF (Section 5.3) |
| Dietterich, *Neural Computation* 10(7), 1895–1923, 1998; McNemar when trained once | entry 4 `:320, 405` | Verified: volume, pages, year and claim from ML Anthology record and the author's PDF abstract; issue 7 from a secondary listing only (Raschka lecture notes, "10.7") | mlanthology.org; web.engr.oregonstate.edu author PDF |
| Hoeffding, JASA 58(301), 13–30, 1963 | entry 4 `:407` | Verified | Bibliographic record (cs.utexas.edu reading list) |
| Kaufman et al., *ACM TKDD* 6(4), art. 15, 2012 | entry 4 `:408` | Verified (article 15; no page range in the record consulted) | IUCC research portal, DOI 10.1145/2382577.2382579 |
| Quiñonero-Candela et al., Eds., *Dataset Shift in Machine Learning*, MIT Press, 2009 | entry 4 `:300, 409` | Verified | Bookseller and MPI listings (ISBN 9780262170055) |
| Stone, JRSS B 36(2), 111–147, 1974 | entry 4 `:410` | Verified | Scan with journal header (washington.edu) |

- Not verified: (1) Dietterich (1998) issue number 7: confirmed only by a secondary listing (lecture notes); the MIT Press page could not be fetched. The value is the conventional one and consistent with the October 1998 issue; recommend keeping it. (2) Kaufman et al. (2012) page range: not given in the record consulted; the entry correctly gives only "art. 15". (3) Vapnik (1995) and Goodfellow et al. (2016): no catalogue listing was retrieved in this session; both are standard textbooks and the details given are the conventional ones, so no change is recommended. The other textbooks were checked against listings (existence, publisher, edition), not against title pages.

## Resolution

- F1 (Should fix): fixed - the sentence now gives the paper's values, then says that PyTorch's `torch.optim.Adam` uses the same three values while Keras 3's `Adam` uses $\epsilon = 10^{-7}$ (applied in a slightly different place in the update); `src/content/blog/gradient-descent-and-its-variants.mdx:322`. Verified 2026-10-15 against keras.io/api/optimizers/adam/ (`epsilon=1e-07`, the "epsilon hat" of the paper) and docs.pytorch.org/docs/2.14 (`betas=(0.9, 0.999)`, `eps=1e-08`).
- T1 (Should fix): fixed - the divisor-$n$ convention is stated where $z$ is defined (worded as a condition after "standard deviation 1 on the training set", so "which" keeps $z$ as its antecedent) and "a centered feature whose mean square is 1 (the divisor-$n$ convention)" replaces "unit variance"; `gradient-descent-and-its-variants.mdx:186, 213`. Recomputed with the entry's data (seed 0, $n = 20$): eigenvalues 2.0, 2.0 with `ddof=0` and 1.9, 2.0 with `ddof=1`.
- T2 (Should fix): fixed - "Unlike the other remedies," removed; the sentence now reads "More data reduces the variance without adding bias, but it is often expensive or impossible to obtain."; `src/content/blog/generalization-overfitting-and-regularization.mdx:267`.
- T3 (Should fix): fixed - label shift now keeps $P(\mathbf{x} \mid y)$ fixed while $P(y)$ changes, matching Lipton, Wang and Smola (ICML 2018, PMLR 80) abstract: "the label marginal p(y) changes but the conditional p(x|y) does not". To keep the lint clean, the 48-word sentence was split into "One common special case is covariate shift ... Another is label shift ...", and the 179-word paragraph was split before "Distribution shift is the general term"; `src/content/blog/evaluating-models-honestly.mdx:300–302`.
- S1 (Should fix): fixed - the reviewer's wording applied: standard error defined as the standard deviation of the estimate over repeated test sets (pointing to Section 3.3 of the first entry), the 95% confidence interval defined by its coverage, then the normal-approximation rule; `evaluating-models-honestly.mdx:320`. The numbers that follow are unchanged and recomputed (standard error 0.0252, half-width 0.0495).

Optional findings applied: T4 (the expression now uses $\ln(99/101)$, $\approx 691$; recomputed 690.75, while $\ln(0.980)$ gives 683.8; `gradient-descent-and-its-variants.mdx:342`), T5 (`generalization-overfitting-and-regularization.mdx:31`), T6 (a parenthetical gives the cyclic-trace argument $\operatorname{tr} P = \operatorname{tr} I_p = p$ and the linear-independence condition, which holds because every fixed-design degree has $p \le 16 < n = 20$ with distinct inputs; `:133`), F2 (`gradient-descent-and-its-variants.mdx:315`), F3 (Hoerl and Kennard at entry 3 `:194`, Tibshirani at `:255`, Geman, Bienenstock and Doursat at the end of the first paragraph of Section 3.1 `:108`; Kaufman et al. at the end of the first leakage paragraph of entry 4 `:186`; Stone placed as its own sentence at the end of the paragraph after the $k$-fold steps, `:110`, instead of inside the opening sentence, because the inserted parenthetical made that sentence 49 words long), S2 (the overview now says each number can be reproduced "with the stated NumPy version (other versions may produce different random streams)"; `src/content/series/machine-learning-fundamentals.md:17`). Not applied: none.

Checks: `eos lint` on the four articles and the series file: 0 errors, 0 warnings (9 suggestions, all pre-existing: acronyms in reference lists and one long sentence at entry 4 `:180`); `eos syntax`: all files compile. No headings changed, so every anchor is kept. No code or output changed. No build was run (outside this task). Vietnamese: no article has a translation; `src/content/series/vi/machine-learning-fundamentals.md` has no copied field affected, but its body should gain the S2 qualification when it is next updated (it already lags the wave-1 overview).

Resolved by the wave-1 author on 2026-10-15; awaiting the reviewer's resolution check.
