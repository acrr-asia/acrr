# Series review: Machine Learning Fundamentals

- Series: `machine-learning-fundamentals` (4 articles, status published, 0 planned entries)
- Reviewed commit: 0654c71
- Date: 2026-10-13
- Content hash: sha256:fa76c5d851e830c40a198b9f2c6c3f6a91a2958a5567e3c8cb9d9d413f4d1e21

## Summary

The series is technically strong. It builds supervised learning in a clear order (problem, optimizer, generalization, evaluation), each entry links back to the one before it, and the four series objectives are all met. All eleven Python blocks were rerun with Python 3.13.16 and numpy 2.5.3, and every quoted output matches byte for byte. Every number in the prose that can be recomputed was checked and is correct except one step count, and all 25 cited works exist as cited.

The one blocking finding is in entry 3: the sentence on feature scale in ridge regression has the millimetre/metre relation backwards. The should-fix findings cover:
- the early-stopping ≈ ridge correspondence, which is called "precise" but is only a heuristic;
- an unsupported claim about why very large models generalize;
- two links whose text names a subsection while the link goes to the parent section;
- an incorrect step count (910 instead of 930);
- seed choices that are not presented as one sample among many (entries 3 and 4);
- the framing of the coin-flip selection example;
- the scope of the fixed-design bias–variance simulation;
- two linear-algebra objects (trace, covariance matrix) that are used without being introduced;
- an overstated claim about early stopping.

The build and the link check pass. The series is ready once the blocking and should-fix items are corrected.

Findings: 1 blocking, 11 should fix, 4 optional.

## Resolution

All 16 findings (F1–F16) were applied on 2026-10-13, at the owner's request:
- **F1:** the units sentence now says that the metre-scale weight is the larger one and is penalized a million times more. It uses American spelling ("meters", "millimeters"), which also covers that part of F13.
- **F2:** §4.3 of entry 3 now gives both shrinkage fractions. These are $1-(1-\eta\mu_i)^t$ for gradient descent and $\mu_i/(\mu_i+2\lambda)$ for ridge with every weight penalized. The text calls the correspondence a rule of thumb that holds roughly, for the flat directions, when $2\lambda \approx 1/(\eta t)$.
- **F3:** the large-model remark is rephrased as an observation, with the cause called an open research question. It cites Belkin, Hsu, Ma and Mandal, PNAS 116(32), 2019, which was confirmed online (par.nsf.gov record; DOI 10.1073/pnas.1903070116; abstract: "they often obtain high accuracy on test data"). The reference was added to entry 3's list. No other reference was added or removed: all 25 existing ones were confirmed.
- **F4, F5:** the two anchors now point to `#32-many-dimensions-curvature-and-conditioning` and `#33-empirical-risk`. Both resolve in `dist/`.
- **F6:** "about 930 steps".
- **F7:** entry 1 now says that seeds are not claimed to be typical and that the text states the variation where it matters. Entry 3 §2.3 has a new paragraph giving the spread over seeds 0–20:
  - the three regimes appear every time;
  - the best degree is 3 for 14 seeds, 5 for 6 and 7 for 1;
  - the first degree with a fresh-data MSE above 1 ranges from 7 to 15.
- **F8:** entry 4 §3.2 now says that the CV minimum falls below 0.09 only for seeds 4, 5, 8 and 14 of 0–20.
- **F9:** the coin-flip paragraph now:
  - speaks of the "best of 50 noisy estimates";
  - presents the coin flips as a simulation of 50 equally good candidates that ignore their inputs;
  - explains that 0.45 is consistent with 0.5 (standard deviation 0.05);
  - says that seed 5 is typical (mean best validation accuracy 0.61 over seeds 0–199).
- **F10:** entry 3 §3.1 defines random versus fixed design. §3.3 says that the "expected error" column is the in-sample expected error at the 20 inputs and is not comparable with §2.
- **F11:** entry 3 §3.2 glosses the covariance matrix (including covariance itself and the rule $ACA^\top$), the trace, and $P^\top = P$, $PP = P$.
- **F12:** "costs little beyond periodic evaluations of the held-out error … widely used for neural networks, often together with weight decay".
- **F13–F16:** "defenses", the condition for $\sigma^2(n-p)/n$, $p = d+1$ in entry 2, and "Cross-validation (CV), in its usual $k$-fold form" were applied as recommended.

Second pass: a full reread after the corrections found four problems introduced by them, all fixed:
- the new seed paragraph in entry 3 §2.3 referred to "the three regimes" before they were described, so it was moved after the regime bullets and the gap paragraph;
- §3.1 repeated "a new sample of 20 examples", now "as just described";
- "which is why it shows" had lost its subject, now "the simulation shows";
- the early-stopping paragraph used $\lambda_i$ for a Hessian eigenvalue next to the ridge strength $\lambda$. The eigenvalue is now $\mu_i$, with a note that entry 2 calls it $\lambda_i$.

Before writing the seed paragraph, I confirmed that the "three regimes every time" claim holds: degree 1 never goes below 0.285, and every seed explodes at high degree. A third read of the changed paragraphs found nothing further.

No Vietnamese file needed changing. None of the four articles has a translation in `src/content/blog/vi/`, and the series file and its translation were not edited.

Re-run results after the final edit:
- `npm run build:local`: 0 errors, 0 warnings, 80 pages indexed.
- `npm run check:links`: 217 pages, 6138 internal references, all resolve.
- `dist/` checks: no `katex-error`, Mermaid min-widths 475/532/288px, no glued inline text.
- All 11 Python blocks still reproduce their quoted output byte for byte. Code and outputs were not changed.

The series content hash stamp (`node scripts/series-pipeline.mjs stamp`) was not added, because this task did not include publication.

Line numbers below refer to the reviewed commit 0654c71, not to the corrected articles.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Formulate a supervised learning problem in terms of a model, a loss function, and a data set. | Entry 1 §1–3 | Met. |
| Explain gradient-based optimization and the role of the learning rate. | Entry 2 §2–5 | Met; the 1-D and eigenvalue analyses are exact and match the code. |
| Distinguish training error from generalization error, and explain why held-out evaluation matters. | Entry 1 §5–6, entry 3 §1–3, §5 | Met. |
| Identify common sources of data leakage and bias in an evaluation setup. | Entry 4 §4–5 | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `src/content/blog/generalization-overfitting-and-regularization.mdx` | §4.1 (line 202) | Technical accuracy | The millimetre/metre scaling of a ridge weight is stated backwards |
| F2 | Should fix | `src/content/blog/generalization-overfitting-and-regularization.mdx` | §4.3 (line 253) | Technical accuracy | Early stopping ≈ ridge with λ ~ 1/(ηt) is said to be "made precise" but is a rough heuristic |
| F3 | Should fix | `src/content/blog/generalization-overfitting-and-regularization.mdx` | §3.4 (line 180) | Fit with site rules / Technical accuracy | Unsupported claim, and an asserted mechanism, for why very large models generalize |
| F4 | Should fix | `src/content/blog/generalization-overfitting-and-regularization.mdx` | §4.3 (line 253) | Cross-article references | Link text "Section 3.2 of the second entry" targets `#3-the-learning-rate` |
| F5 | Should fix | `src/content/blog/evaluating-models-honestly.mdx` | §2.1 (line 38) | Cross-article references | Link text "Section 3.3 of the first entry" targets `#3-risk-and-empirical-risk` |
| F6 | Should fix | `src/content/blog/gradient-descent-and-its-variants.mdx` | §3.4 (line 213) | Technical accuracy | "about 910 steps" should be about 930 |
| F7 | Should fix | `src/content/blog/generalization-overfitting-and-regularization.mdx` (and `learning-from-data.mdx` line 23) | §2.2–2.3 (lines 76–100) | Fit with site rules | Seed 9 is presented without saying how the outcome varies with the seed |
| F8 | Should fix | `src/content/blog/evaluating-models-honestly.mdx` | §3.2 (line 173), Exercise 5 (line 375) | Fit with site rules | The "CV score below the irreducible error" point depends on seed 4; it occurs for only 4 of seeds 0–20 |
| F9 | Should fix | `src/content/blog/evaluating-models-honestly.mdx` | §2.2 (lines 50, 74) | Technical accuracy / Writing quality | Coin-flip example framing: "minimum" of estimates but code takes a maximum; 0.45 called "at chance" without noise context |
| F10 | Should fix | `src/content/blog/generalization-overfitting-and-regularization.mdx` | §3.1 (line 106–108), §3.3 (line 172) | Technical accuracy | Fixed-design simulation: what is redrawn, and what "expected error" measures, is not stated clearly |
| F11 | Should fix | `src/content/blog/generalization-overfitting-and-regularization.mdx` | §3.2 (line 127) | Concept introduction | Covariance matrix and trace are used without introduction (not among the stated prerequisites) |
| F12 | Should fix | `src/content/blog/generalization-overfitting-and-regularization.mdx` | §4.3 (line 255) | Technical accuracy | "costs nothing extra" and "the most common regularizer" are unsupported/overstated |
| F13 | Optional | `src/content/blog/generalization-overfitting-and-regularization.mdx`, `evaluating-models-honestly.mdx` | lines 202; 298 | Terminology | British spellings "millimetres", "metres", "defences" in an American-spelled series |
| F14 | Optional | `src/content/blog/learning-from-data.mdx` | §6 (line 263) | Technical accuracy | σ²(n−p)/n does not need Gaussian noise, but does need the model to contain the true mean |
| F15 | Optional | `src/content/blog/gradient-descent-and-its-variants.mdx` | §3.2 (line 125) | Terminology | $p$ (number of parameters) is used without definition in this entry |
| F16 | Optional | `src/content/blog/evaluating-models-honestly.mdx` | §3.1 (line 102) | Terminology | "K-fold" with capital K while $k$ is used everywhere else |

### F1. Ridge penalty and feature units stated backwards
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:202`, section "4.1 Ridge regression: penalizing large weights"
- **Text:** "a weight on a feature measured in millimetres must be a thousand times larger than on the same feature in metres, so it is penalized a million times more."
- **Problem:** A length in millimetres is a thousand times larger numerically than the same length in metres. To produce the same prediction $w_{\text{mm}} x_{\text{mm}} = w_{\text{m}} x_{\text{m}}$, the millimetre weight must be a thousand times *smaller*: $w_{\text{mm}} = w_{\text{m}}/1000$. The weight on the metre feature is the larger one, and it is the one penalized a million times more. The sentence's conclusion (the penalty depends on units, so standardize) is right, but the stated relation is wrong.
- **Recommended correction:** "The penalty depends on the scale of each feature: the same length recorded in meters instead of millimeters takes values a thousand times smaller, so its weight must be a thousand times larger to give the same predictions, and that weight is penalized a million times more."

### F2. Early stopping and ridge: a heuristic presented as precise
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:253`, section "4.3 Early stopping"
- **Text:** "For least squares the analogy can be made precise: after $t$ steps with learning rate $\eta$, the iterates behave roughly like a ridge solution with $\lambda$ of the order of $1/(\eta t)$."
- **Problem:** "made precise" and "roughly" contradict each other. The correspondence is a heuristic. Along an eigenvector of $H$ with eigenvalue $\lambda_i$, gradient descent from zero recovers the fraction $1-(1-\eta\lambda_i)^t$ of the least-squares component. Ridge with a penalty on every weight recovers $\lambda_i/(\lambda_i+2\lambda)$. The two filters agree only in the limits (steep and flat directions) and when $2\lambda \approx 1/(\eta t)$. Recomputed on the entry-1 data with $\eta=0.05$, $t=20$, they give 0.149 vs 0.139 for the flat direction and 0.936 vs 0.720 for the steep one. The author's note asks for this to be labelled as a heuristic.
- **Recommended correction:** state the two filter factors, say they agree only roughly and only in the limits, and call it a rule of thumb (text in the Resolution).

### F3. Unsupported remark on very large models
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:180`, section "3.4 The trade-off"
- **Text:** "Very large modern models, with far more parameters than training examples, can still generalize well when they are trained in ways that restrict which of their many possible solutions is reached."
- **Problem:** The sentence has no source. It also presents one candidate explanation (implicit restriction by the training procedure) as the established reason, although this is still an open research question. The phenomenon itself is documented, for example in Belkin, Hsu, Ma and Mandal, PNAS 116(32), 2019, whose abstract says such models "often obtain high accuracy on test data". The cause is not settled.
- **Recommended correction:** "Very large models, such as neural networks with more parameters than training examples, have been observed to predict well in many applications even when they fit their training data almost exactly (Belkin et al., 2019); when and why this happens is an active research question outside the scope of this series. The decomposition still holds for such models, since it is an identity; what fails is the use of the parameter count as a measure of the variance, as in the formula of Section 3.2." Add the reference.

### F4. Link text names Section 3.2 but links to Section 3
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:253`
- **Text:** "(Section 3.2 of the [second entry](/blog/gradient-descent-and-its-variants#3-the-learning-rate))"
- **Problem:** The anchor goes to the "3. The Learning Rate" heading, not to §3.2. The id `32-many-dimensions-curvature-and-conditioning` exists in `dist/blog/gradient-descent-and-its-variants.html`.
- **Recommended correction:** link to `/blog/gradient-descent-and-its-variants#32-many-dimensions-curvature-and-conditioning`.

### F5. Link text names Section 3.3 but links to Section 3
- **Where:** `src/content/blog/evaluating-models-honestly.mdx:38`
- **Text:** "by the argument of [Section 3.3 of the first entry](/blog/learning-from-data#3-risk-and-empirical-risk)"
- **Problem:** The anchor goes to the parent heading. The id `33-empirical-risk` exists.
- **Recommended correction:** link to `/blog/learning-from-data#33-empirical-risk`.

### F6. Step count after rescaling
- **Where:** `src/content/blog/gradient-descent-and-its-variants.mdx:213`, section "3.4 Feature scaling"
- **Text:** "reducing it by a factor of $10^6$ takes about 910 steps instead of about 110."
- **Problem:** With the unrounded factor $(\kappa-1)/(\kappa+1) = 0.98526$ ($\kappa = 134.69$), $\ln 10^{-6}/\ln 0.98526 = 930.3$. The figure 910 (914) comes from the rounded factor 0.985, and a rounding in the third decimal changes the count by 2 %. The 110 figure is correct (110.3).
- **Recommended correction:** "about 930 steps instead of about 110".

### F7. Seed 9 presented without its variability
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:76–100`; series-wide statement at `src/content/blog/learning-from-data.mdx:23`
- **Text:** "With seed 9 it prints:" followed by a reading of the table ("A good fit (degree 3 to about 7)", "Overfitting (degree 9 and above)") as if it were the general pattern.
- **Problem:** The seeds used across the series (0, 1, 4, 5, 6, 7, 9, 11) are not one fixed default, and the entries never say how sensitive each result is to the seed. A rerun with seeds 0–20 shows the following:
  - Every seed gives the three regimes and a training MSE that falls with degree.
  - The lowest fresh-data MSE is at degree 3 for 14 seeds, at degree 5 for 6 seeds and at degree 7 for 1 seed.
  - The first degree with a fresh-data MSE above 1 ranges from 7 to 15.

  Seed 9 is an ordinary member of this set, but the reader cannot know that, and entry 4 already reports seed sensitivity (§3.2, §4.4). Seed choices must be disclosed honestly. Entry 1 says only that the seed is fixed and stated.
- **Recommended correction:** after the entry-3 table, add a sentence giving the spread over seeds 0–20 (text in the Resolution). In entry 1 line 23, add: "The seeds are not claimed to be typical; where a result varies noticeably from one seed to another, the text says by how much."

### F8. The CV score below the noise floor depends on the seed
- **Where:** `src/content/blog/evaluating-models-honestly.mdx:173` (and Exercise 5, line 375)
- **Text:** "The CV score of the chosen setting, 0.0886, is below the irreducible error of 0.09, which no predictor can genuinely achieve."
- **Problem:** The rerun is correct, but over seeds 0–20 the CV minimum is below 0.09 only for seeds 4, 5, 8 and 14. For the other 17 seeds it lies between 0.0937 and 0.1493. The bullet and Exercise 5 present a seed-specific event without saying so. The seed-2 failure that the text does mention (λ = 1e-5, test 1.31, fresh 0.65, and 0.14 at λ = 1e-2) was confirmed.
- **Recommended correction:** append: "This particular seed shows the effect starkly; among seeds 0 to 20 the CV minimum falls below 0.09 only for seeds 4, 5, 8 and 14, but the selection effect of Section 2.2 is present whatever the seed."

### F9. Framing of the coin-flip selection example
- **Where:** `src/content/blog/evaluating-models-honestly.mdx:50, 74`
- **Text:** "The reported error of the winner is now the minimum of 50 noisy estimates, and the minimum of noisy estimates is biased downwards even when every candidate is equally good. The code below makes this concrete with the most extreme case: 50 "models" that each guess every label by a fair coin flip" … "and is at chance on data that played no part in the selection."
- **Problem:** The prose speaks of the minimum error, but the code and output report the maximum accuracy. The candidates are described as "the most extreme case", but the example's real point is that they are *equally good*: these models ignore their inputs, and the coin flip is only a way of simulating candidates of identical true accuracy. A test accuracy of 0.45 is called "at chance" with no mention that the standard deviation for 100 examples is 0.05. Seed 5 is typical: over seeds 0–199 the best validation accuracy averages 0.613, median 0.61.
- **Recommended correction:** reword as "the best of 50 noisy estimates … biased in the winner's favor"; describe the code as a simulation of 50 candidates of equal quality, represented by input-ignoring coin-flip guessers; say that 0.45 is consistent with 0.5 given a standard deviation of 0.05; and note that the seed is typical.

### F10. Fixed-design simulation: what is averaged
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:106–108, 172`
- **Text:** "a different sample of 20 examples would give a different curve" … "averaging over both the training set and the new noise"; the simulation prints "expected error 0.1115" etc.
- **Problem:** §3.1 motivates the randomness by redrawing whole samples (inputs and noise), while §3.2–3.3 redraw only the noise at fixed inputs. The printed "expected error" is the expected squared error on a new label *at the 20 training inputs*. It is not the risk at random new inputs that §2 measured, so 0.1115 at degree 3 and 0.1047 in §2 are different quantities. Line 174 hints at this, but the label "expected error" invites a direct comparison.
- **Recommended correction:** in §3.1, say that the training set can be random in its inputs and noise, or in its noise only (a fixed design), and that the decomposition holds in both cases. After the simulation output, say that "expected error" is the in-sample expected error at the 20 fixed inputs and is not directly comparable with the fresh-data MSE of Section 2.

### F11. Covariance matrix and trace used without introduction
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:127`
- **Text:** "the covariance of $P\mathbf{y}$ is $\sigma^2 P P^\top = \sigma^2 P$, and the trace of a projection matrix equals the dimension it projects onto"
- **Problem:** The series prerequisites (entry 1 lines 19–21) list vectors, matrices, product, transpose and inverse, plus the variance of a random variable. The covariance matrix of a random vector, the trace, and the projection identities $P^\top = P$, $P^2 = P$ are not among them and are used without a gloss.
- **Recommended correction:** gloss them inline (text in the Resolution).

### F12. Early stopping: overstated cost and prevalence
- **Where:** `src/content/blog/generalization-overfitting-and-regularization.mdx:255`
- **Text:** "It costs nothing extra in computation and is the most common regularizer for large neural networks, usually combined with weight decay."
- **Problem:** Monitoring requires repeated evaluations on held-out data, so it is cheap but not free. "The most common regularizer" is an unsourced ranking.
- **Recommended correction:** "It costs little beyond periodic evaluations of the held-out error, and it is widely used for neural networks, often together with weight decay."

### F13. British spellings
- **Where:** `generalization-overfitting-and-regularization.mdx:202` ("millimetres", "metres"); `evaluating-models-honestly.mdx:298` ("defences").
- **Problem:** The series otherwise uses American spelling ("behavior", "regularization", "centered", "favor").
- **Recommended correction:** "millimeters", "meters", "defenses".

### F14. Condition for the expected training MSE
- **Where:** `src/content/blog/learning-from-data.mdx:263`
- **Text:** "For least squares with $p$ parameters and Gaussian noise of variance $\sigma^2$, the expected training MSE is $\sigma^2 (n - p)/n$"
- **Problem:** Gaussianity is not needed: independent noise with mean zero and variance σ² is enough. The formula does require the model family to contain the true conditional mean (here it does).
- **Recommended correction:** "For least squares with $p$ parameters, when the model family contains the true conditional mean (as it does here) and the noise is independent with variance $\sigma^2$, …"

### F15. $p$ undefined in entry 2
- **Where:** `src/content/blog/gradient-descent-and-its-variants.mdx:125`
- **Text:** "real **eigenvalues** $\lambda_1 \le \dots \le \lambda_p$"
- **Recommended correction:** add "where $p = d + 1$ is the number of parameters".

### F16. "K-fold"
- **Where:** `src/content/blog/evaluating-models-honestly.mdx:102`
- **Text:** "**K-fold cross-validation** (CV) uses every example"
- **Recommended correction:** "**Cross-validation** (CV), in its usual $k$-fold form, uses every example".

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| Supervised learning, example, feature, label | learning-from-data.mdx:15 | learning-from-data.mdx:36–45 | Introduced before use. |
| Probability distribution, i.i.d. | learning-from-data.mdx:73 | learning-from-data.mdx:21 (prerequisite), 73 | OK. |
| Loss, risk, empirical risk, ERM | learning-from-data.mdx:100 | learning-from-data.mdx:100–163 | OK. |
| Design matrix, normal equations | learning-from-data.mdx:92 | learning-from-data.mdx:92, 204 | OK. |
| Logistic (sigmoid) function | learning-from-data.mdx:113 | learning-from-data.mdx:113 | OK. |
| Gradient, Hessian | gradient-descent…:52, 113 | gradient-descent…:52, 113 | OK. |
| Eigenvalues, eigenvectors | gradient-descent…:125 | gradient-descent…:125 (recalled, announced at line 17) | OK. |
| Condition number | gradient-descent…:130 | gradient-descent…:130 | OK. |
| Convexity, L-smoothness | gradient-descent…:221 | gradient-descent…:221 | OK. |
| Mini-batch, epoch | gradient-descent…:243–249 | same | OK. |
| Projection matrix | generalization…:127 | generalization…:127 | OK (defined by formula). |
| Covariance matrix, trace | generalization…:127 | not introduced | F11. |
| Singular value decomposition | generalization…:49 | named only | Acceptable (only the name of a solver). |
| Bias–variance decomposition | generalization…:110 | generalization…:106–121 | OK. |
| Hoeffding's inequality, union bound | evaluating…:40, 74 | evaluating…:40–46, 74 | OK. |
| Standard error, normal-approximation CI | evaluating…:316 | evaluating…:316 | OK; uses the prerequisite normal distribution. |
| McNemar's test | evaluating…:318 | described in one clause, cited (Dietterich 1998) | Acceptable. |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| Python 3.13, numpy 2.5.3, `default_rng` streams | all entries (learning-from-data.mdx:23, gradient…:17, generalization…:19, evaluating…:17) | Yes | Matches this environment (Python 3.13.16, numpy 2.5.3); all outputs reproduce. |
| MSE without factor ½ | learning-from-data.mdx:115 | Yes | Consistent with every gradient formula. |
| Natural logarithm (nats) in cross-entropy | learning-from-data.mdx:113 | Yes | OK. |
| Binary labels coded {0, 1} | learning-from-data.mdx:50 | Yes | Consistent with entry 2's logistic gradient. |
| Intercept unpenalized in ridge; ridge scaling $n\lambda$ | generalization…:194–197 | Yes | Consistent with the code in entries 3 and 4. |
| Adam defaults (β₁ 0.9, β₂ 0.999, ε 1e-8) | gradient…:322 | Yes, with "check the documentation" | OK. |
| Seeds | all code | Stated, but their typicality is not | F7, F8. |
| Fixed versus random design | generalization…:127–174 | Partly | F10. |

## Series-level notes

- **Cross-references.** Checked every in-series reference:
  - learning-from-data.mdx:78 → entry 4 §5.1 ✓; :94 → entry 3 §2.1 ✓; :151 → entry 4 §6.1 ✓; :298 → entry 4 §5.2 ✓.
  - gradient…:88 → entry 3 §4.3 ✓; :215 → entry 4 §4.2 ✓; :299 → entry 4 §3.2/§6.1 ✓.
  - generalization…:268 "next entry" ✓.
  - evaluating…:190 "as recommended in the second entry" ✓; :302 "the first entry's third exercise" ✓; :320 ✓.
  - Every "next entry" link names the actual next article. The only link-text mismatches are F4 and F5.
- **Terminology.** The three meanings of "bias" are explicitly separated (entry 1 line 92, entry 3 line 123, entry 4 line 32). "Fresh-data MSE" is used consistently. "Generalization error" = risk throughout.
- **Structure.** Every entry has numbered sections, exercises with answers, a summary table and a reference list; tone is consistent.
- **References.** All 25 references were checked. The four that the author flagged were confirmed online:
  - Polyak 1964: Zh. Vychisl. Mat. Mat. Fiz. 4(5) 791–803; English translation USSR Comput. Math. Math. Phys. 4(5) 1–17 (mathnet.ru).
  - Kaufman, Rosset, Perlich, Stitelman: ACM TKDD 6(4), article 15, 2012 (DOI 10.1145/2382577.2382579).
  - Ambroise & McLachlan: PNAS 99(10) 6562–6566, 2002 (PMC124442).
  - Cawley & Talbot: JMLR 11, 2010 (jmlr.org/papers/v11/cawley10a).

  The others are standard works whose bibliographic details as given are correct (Robbins–Monro 1951 AMS 22(3); Kingma–Ba ICLR 2015; Hoerl–Kennard 1970 Technometrics 12(1); Tibshirani 1996 JRSS-B 58(1); Geman et al. 1992 Neural Computation 4(1); Hoeffding 1963 JASA 58(301); Stone 1974 JRSS-B 36(2); Dietterich 1998 Neural Computation 10(7); Bottou–Curtis–Nocedal 2018 SIAM Review 60(2); and the textbooks).
- **Frontmatter.** The frontmatter is consistent: category "AI and Machine Learning", `seriesOrder` 1–4, all dated 2026-10-13. The tag `numerical-methods` (entry 2) is hyphenated unlike the others, but it is an existing site tag shared with another article, so it was left as is.

## Verification log

- `npm run build:local`: passed (astro check 0 errors, 0 warnings; Pagefind indexed 80 pages in 2 languages).
- `npm run check:links`: 217 pages, 6138 internal references, all resolve.
- `dist/blog/<slug>.html`:
  - Mermaid min-width 475px (entry 1), 532px (entry 2) and 288px (entry 4), all under 600px.
  - No `katex-error`.
  - No prose text glued to `<a>`, `<strong>` or `<code>`.
- Code: all 11 Python blocks were rerun (Python 3.13.16, numpy 2.5.3) and every quoted output matches byte for byte. The blocks are:
  - entry 1 §5.3;
  - entry 2 §3.3, §3.4 and §4.3;
  - entry 3 §2.2, §3.3 and §4.1;
  - entry 4 §2.2, §3.2, §4.3 and §4.4.
- Recomputed, entry 1:
  - cross-entropy values 0.105/2.303/0.693/0.223/1.609 (ratio 7.2);
  - Section 4 table (20.4, 2.4, 16.4, 3.2);
  - a = 0.1812, b = −0.2929, risk 0.25836, excess 0.00836.
- Recomputed, entry 2:
  - 1-D table (all twelve values);
  - H = [[2.000, 1.025], [1.025, 0.732]], λ = 0.1608/2.5709, η limit 0.778, κ 15.99, best η 0.732, factor 0.882;
  - factors 0.992, 0.920, 0.928, 1.057;
  - steps 110.3 (correct) and 930.3 (text 910, F6);
  - Exercise 2: 690.8 steps;
  - final SGD η 0.0091;
  - SGD over shuffle seeds 1–20: medians 4.13e-3, 1.91e-4, 4.40e-5; batch-1 range 2.48e-5 to 3.05e-2. All as stated.
- Recomputed, entry 3:
  - training-input gap 0.065–0.287, minimum 0.006, maximum 0.983 ✓;
  - degree 9 with n = 2000: fresh-data MSE 0.090 (three seeds) ✓;
  - exact squared bias 0.1928 / 0.0039 / 1.33e-5 ✓;
  - ratio 2.3751/0.2533 = 9.4 ✓;
  - exercises 0.05 and 0.00045 ✓;
  - seed spread 0–20 (F7);
  - early-stopping and ridge filter factors (F2).
- Recomputed, entry 4:
  - Hoeffding m = 738 and 6623; deviations 0.195 and 0.136; normal-approximation SE 0.0252 and CI ±0.049; Hoeffding ±0.096; SE 0.0266 at 0.83 ✓;
  - seed 2: λ 1e-5, test 1.3079, fresh 0.6479, fresh at 1e-2 0.1421 ✓;
  - over seeds 0–20, test above fresh in 10 of 21 ✓;
  - group seeds 8 and 9: 0.404 and 0.488 ✓;
  - coin-flip typicality (mean maximum 0.613);
  - feature selection over seeds 0–20: leaky mean 0.935, honest mean 0.461 (seed 6 typical).
- Not verified: none of the numerical claims. The general statements about practice (for example that step and cosine decay are common) are standard and were not checked against a source.
