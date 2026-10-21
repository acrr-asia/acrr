# Series review: Bayesian Deep Learning

- Series: `bayesian-deep-learning` (10 articles, status published, 0 planned entries)
- Reviewed commit: 6cdf06e
- Date: 2026-10-21
- Content hash: sha256:9f8502ae020e344e5e0631a776381e85e000763e449bf900603e7ae31378a273

## Summary

This is the independent second-pass review of the complete series. A first wave reviewed it before: findings D1–D37 covered entries 1–5 (6 blocking, 18 should fix, 13 optional) and E1–E28 covered entries 6–10 and the overview (0 blocking, 11 should fix including E25, which would have been blocking without the owner's confirmation, and 17 optional). All 65 were checked against the current text, and 61 are fully resolved. D21 and the E15/E26 notation alignment were applied incompletely, and D35 was resolved only approximately. These residues appear below as S4, S5 and S12. The series is technically strong. All ten listings run under Python 3.13.16 and NumPy 2.5.3 and reproduce their quoted output exactly. Every derived number checked in the prose is correct, including the memory figures of entry 8 (400 TB = 363.8 TiB; 4 TiB, 8 MiB and 17 MiB blocks). Three blocking problems remain. One is a false internal cross-reference in entry 5 left over from the section renumbering. The other two are single sentences that closely paraphrase the source collection, in entries 6 and 10. The should-fix findings are mostly about consistency: leftover symbols that the conventions file reserves, reference formats that differ from entry to entry and break the binding conventions, and one misdirected forward reference. The Kronecker product is also used without being introduced. The series is not ready as published until S1–S3 are fixed; the remaining findings are quick edits.

Findings: 3 blocking, 9 should fix, 8 optional (second pass S1–S18 and third pass T1–T2; all blocking and should-fix findings are resolved, see Resolution).

## Resolution

First-wave findings (verified against commit 6cdf06e by this review):

- D1: resolved. Entry 1 output now `-11.67`; listing re-run, matches.
- D2: resolved. "the ten observations of the left cluster".
- D3: resolved. Offset attributed to bumps at $c_k = 3$ and 4 (recomputed −0.036 and −0.074).
- D4: resolved. Der Kiureghian and Ditlevsen "discuss it"; Kendall and Gal "popularized".
- D5: resolved. Restricted to "a regression network with Gaussian noise".
- D6: resolved. "Bernoulli (or, with several classes, categorical)".
- D7: resolved. "about 15% (one seventh) of the stability limit".
- D8: resolved. Range stated along principal directions (recomputed 0.081 to 1.0).
- D9: resolved. Seeds 0–5, 4000 transitions, 500 discarded; recomputed fixed 0.140–0.160 (mean 0.149), jittered 0.134–0.145 (mean 0.138).
- D10: resolved. Irreducible and aperiodic.
- D11: resolved. "a variant of Geyer's initial positive sequence rule".
- D12: resolved. Izmailov et al. described per conventions in entries 2 and 5.
- D13: resolved. Caption "its states (dots)".
- D14: resolved. Exactness stated for linear-Gaussian regression.
- D15: resolved. Entry 3 Section 1.2 rewritten; no n-gram overlap found.
- D16: resolved. Data-augmentation clause removed.
- D17: resolved. MacKay attribution rewritten.
- D18: resolved. Decimal units stated in entry 3 Exercise 4.
- D19: resolved. SVI attributed to mini-batch estimates.
- D20: resolved. Foong et al. stated as a bound.
- D21: partly resolved. Formula and code use $M$, but the prose of entry 4 Section 4.1 still writes $S$ (see S4).
- D22: resolved. No "minibatch" remains in the series.
- D23: resolved. Whole KL term weighted 500 times.
- D24: resolved. "a measure of discrepancy between distributions".
- D25: resolved. Entry 5 opening rewritten.
- D26: resolved. Entry 5 Section 1 restructured and rewritten.
- D27: resolved. Section 3 rebuilt on an own two-mode experiment (listing re-run, matches).
- D28: resolved. Section 6 rewritten.
- D29: resolved. Remaining n-gram hits are terminology only.
- D30: resolved. Section 5 closing corrected.
- D31: resolved. Fast geometric ensembling description corrected.
- D32: resolved. "perturb-then-optimize"; Bardsley et al. cited as related.
- D33: resolved. Depeweg et al. cited in Section 1.4.
- D34: resolved. "Inside the data clusters, at $x = \pm 2$".
- D35: partly resolved. The "Figure 1." prefix was dropped, but the caption's "beyond about ±5.5" does not match the recomputed crossings at −5.06 and 5.76 (see S12).
- D36: resolved. Volumes and pages added; venue abbreviations aligned.
- D37: resolved. Self-pairs included in the tandem example.
- E1: resolved. RBF synonym mentioned once, in entry 6.
- E2: resolved. $\varphi$ distinguished from $\phi$ in entry 6.
- E3: resolved. Entry 6 references aligned to the conventions.
- E4: resolved. Link text names *Evaluating Models Honestly* in the fundamentals series.
- E5: resolved. "squared-exponential kernel of the sixth entry".
- E6: resolved. "a broad slab distribution".
- E7: resolved. MacKay 1992 papers named by title in entry 7.
- E8: resolved. Identifiable latent variable models softened to an interpretation.
- E9: resolved. Transitions versus visible turns reconciled.
- E10: resolved. Neal (1996) aligned; Chen and Sussmann pages still omitted as unverified.
- E11: resolved. K-FAC $A \otimes G$ throughout; listing re-run (4.9e-15), matches.
- E12: resolved. "lengthscale 1".
- E13: resolved. "400 terabytes (about 364 TiB)"; recomputed 363.8 TiB.
- E14: resolved. Claim tied to the cost table and the fifth entry.
- E15: resolved in entry 9. In entry 7 the alignment is incomplete: line 38 still has $\sigma_v$ (see S5).
- E16: resolved. Section 2.1 reworded.
- E17: resolved. $0 < r < 1$ with the two-class and $C$-class bounds.
- E18: resolved. Exercise 4 replaced (0.495 nats recomputed).
- E19: resolved. "post-hoc route" in entry 8.
- E20: resolved. Singularity attributed to continuous degeneracies.
- E21: resolved. $L_n$ defined at $\theta_0$ with $K(\theta_0) = 0$.
- E22: resolved. $P$ for the parameter count; subspace matrix $U$.
- E23: resolved. Lone subsections removed.
- E24: resolved. Uncited "Recent work" rewritten.
- E25: kept. Authorship of the source collection confirmed by the repository owner (2026-10-20).
- E26: resolved in the overview. Entry-level alignment is incomplete in entries 6 and 7 (see S5, S6).
- E27: resolved. Sequence rationale stated.
- E28: resolved. Python 3.13 and NumPy 2.5.3 stated once in the overview.

### Second pass

Second-pass findings (resolved in commit ae8d3c0, verified by the third pass below):

- S1: resolved. Entry 5 Section 2.1 now refers to the average-noise term of Section 1.3.
- S2: resolved. Entry 6 Section 5.1 prediction sentence rewritten ("For a test input $x^*$, the trained network is run once ..."); no n-gram hit on it against part05.
- S3: resolved. Entry 10 Section 6.2 myopic and amortized sentences rewritten; no n-gram hit against part10.
- S4: resolved. Entry 4 Section 4.1 writes $M$ in both prose occurrences.
- S5: resolved. Entry 7 line 38 "$v_j$ has variance $s_v^2$"; entry 6 uses $s_v$, $s_w$, $s_b$ in Sections 3.1 and 3.3 (prose and displays). No $\sigma_v$, $\sigma_w$ or $\sigma_b$ remains in the series.
- S6: resolved. Entry 6 Section 3.2 uses $V$ (variance and kurtosis formula), Section 3.3 $\Sigma^{(l)}$. Remaining $\Lambda$ uses are precisions or output-space curvatures.
- S7: resolved. Entry 1 Section 5 says the eighth entry collects the first two combinations and links the tenth for subspace inference.
- S8: resolved. NeurIPS volume numbers added in entries 3, 4, 7 and 8 (all pairs consistent: conference year − 1987, or the publication year for Williams (1997) vol. 9 and Williams and Seeger (2001) vol. 13); one ICLR form ("in *Proceedings of the International Conference on Learning Representations (ICLR)*") everywhere; sentence-case titles in all ten entries; Maddox et al. (2019) "W. J. Maddox, T. Garipov, P. Izmailov, D. Vetrov and A. G. Wilson" in entries 5 and 8; "D. Vetrov" throughout; Daxberger et al. (2021) in one form. A script finds no work cited in two forms. No pages or volumes beyond the NeurIPS numbers were added.
- S9: resolved. Entry 3 Section 2.3 defines the Kronecker product; entry 8 Section 3.1 points to it.
- S10: partly resolved. Entry 5 Section 1.4 uses $\mathbb{H}$ and $\log$, and entry 6 Sections 2.3–2.4 use $\log$; but entry 5 Section 8.1 still writes $\ln$ twice in prose under a display that now uses $\log$ (see T1).
- S11: resolved. Entry 9 Section 4.1 and entry 6 Section 1.2 reworded; remaining n-gram hits on entry 6 line 37 are standard terms.
- S12: resolved. Caption and generator `<desc>` give 3.2 to 5.0, below −5.1 and above 5.8; recomputed crossings −5.06, 3.23, 4.96 and 5.76 agree.
- S13: resolved. Entry 3 Section 3.3 names *The evidence framework applied to classification networks*.
- S14: resolved. Entry 10 *Open* items at lines 50, 190 and 236 now end in questions, with context first.
- S15: resolved. Entry 4 Section 2.2 "with ReLU activations, scaling one layer up ...".
- S16: resolved. Overview notation paragraph adds $s_0$ ($\alpha = 1/s_0^2$), $M$ and $J$.
- S17: resolved. Entry 2 Section 5.3 "neither $\hat{R}$ nor the effective sample size (Section 7)".
- S18: resolved. "post-hoc uncertainty", "parameterization" and "Gauss–Newton"; no variant remains.

### Third pass (verification)

An independent verifier checked commit ae8d3c0 against S1–S18, re-ran every listing, re-checked every cross-entry reference, repeated the originality scan and ran the site checks. Seventeen of the eighteen second-pass findings are fully resolved, and the renames are applied consistently: no $\sigma_v$, $\sigma_w$, $\sigma_b$, $\Lambda^{(l)}$, prose $S$ for a sample count, $H[\cdot]$ for entropy, "NeurIPS)" without volume, bare ICLR form, "D. P. Vetrov", "post hoc", "parametrization" or "Gauss-Newton" remains in the ten entries. The changed formulas are still correct (the Kronecker definition matches the column-stacked $\operatorname{vec}(W)$ of entry 8; the kurtosis formula with $V$ and the NNGP recursion with $\Sigma^{(l)}$ are unchanged in substance). All 22 listings reproduce their quoted output exactly. All cross-entry section references resolve to the current headings. The 6-word scan found no run of six or more words outside standard terms, formulas and generic phrases. One residue of S10 remains (T1, should fix), and entry 8 has one optional $\ln$ (T2). No blocking problem remains; the series is publishable once T1 is fixed.

Resolution of the third pass (lead): T1 fixed: entry 5 Section 8.1 now writes $\log(2\sqrt{2000}/0.05) \approx 7.49$ and $\mathrm{KL} = \log 5 \approx 1.61$, matching the displayed bound. T2 applied: entry 8 Section 6 now writes $2000 / \log 2 \approx 2885$ bits. The same two edits were made in the Vietnamese translations. No `\ln` remains in the series; no blocking or should-fix finding remains open.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Explain what a posterior distribution over network parameters or functions is, how the posterior predictive is formed, and how epistemic and aleatoric uncertainty differ. | Entry 1 (Sections 1–3), entry 5 (Sections 1.3–1.4), entry 9 (Section 5.2) | Met. |
| Compare the main approximate-inference families for neural networks (MCMC, Laplace, VI and ensembles) by their assumptions, cost and failure modes. | Entries 2–5, entry 1 Section 5 table, entry 8 Section 1.2 cost table | Met. |
| Relate neural networks to Gaussian processes and kernel methods, and explain how priors, symmetries and identifiability shape a Bayesian neural network. | Entries 6 and 7; entry 10 Section 5 | Met. |
| Choose a method that scales to a given model and data set, and evaluate predictive uncertainty with calibration, proper scoring rules and selective prediction. | Entry 8 (Sections 1, 7), entry 9 (Sections 2–4) | Met. |
| Describe current research directions in Bayesian deep learning and state the open problems each one addresses. | Entry 10 | Met. Some *Open* items are statements, not the questions that line 20 promises (S14). |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| S1 | Blocking | `src/content/blog/deep-ensembles.mdx` | Section 2.1 (line 75) | Cross-article references | "the average-noise term of Section 1.2": after the renumbering, the average-noise term is in Section 1.3. |
| S2 | Blocking | `src/content/blog/gaussian-processes-and-kernels.mdx` | Section 5.1 (line 284) | Fit with site rules (originality) | A sentence closely paraphrases the source collection, with an exact nine-word run. |
| S3 | Blocking | `src/content/blog/frontiers-of-bayesian-deep-learning.mdx` | Section 6.2 (line 206) | Fit with site rules (originality) | The "myopic ... as if it were the last" sentence closely paraphrases the source. |
| S4 | Should fix | `src/content/blog/variational-inference-for-neural-networks.mdx` | Section 4.1 (lines 170, 176) | Notation | The Monte Carlo pass count is written $S$ in the prose, while the displayed formula uses $M$ (incomplete D21; the conventions reserve $S$ for covariances). |
| S5 | Should fix | `src/content/blog/priors-symmetries-and-identifiability.mdx` | Section 1.3 (line 38); entry 6 lines 170–179, 244–247 | Notation | "$v_j$ has variance $\sigma_v^2$", then $s_v^2$ in the formula. Entry 6 writes $\sigma_v$, $\sigma_w$ for the quantities entry 7 calls $s_v$, $s_w$. |
| S6 | Should fix | `src/content/blog/gaussian-processes-and-kernels.mdx` | Section 3.2 (line 194), Section 3.3 (lines 247–250) | Notation | $S$ is a sample variance and $\Lambda^{(l)}$ a covariance matrix; the conventions reserve $S$ for posterior covariances and $\Lambda$ for precision matrices. |
| S7 | Should fix | `src/content/blog/bayesian-inference-for-neural-networks.mdx` | Section 5 (line 293) | Cross-article references | The text says the eighth entry collects these combinations, but subspace MCMC is treated only in the tenth entry, Section 2. |
| S8 | Should fix | Entries 2–10 (reference lists) | see detail | Consistency (conventions) | Reference formats differ: NeurIPS without a volume number in 4 entries; two ICLR forms; inconsistent author order and titles for the same paper. |
| S9 | Should fix | `src/content/blog/laplace-approximations.mdx` | Section 2.3 (line 91); entry 8 lines 154–166 | Concept introduction | The Kronecker product $A \otimes G$ is used, and its eigen-identity relied on, without ever being defined. It is outside the stated linear-algebra prerequisite. |
| S10 | Should fix | `src/content/blog/deep-ensembles.mdx` | Section 1.4 (lines 60, 63); entry 6 lines 85, 92 | Notation | Entropy is written $H[\cdot]$ with $\ln$, while entries 1 and 9 use $\mathbb{H}$ and $\log$ for the same split. $H$ is the Hamiltonian in entry 2 and the Hessian in entry 3. |
| S11 | Should fix | `src/content/blog/evaluating-and-using-uncertainty.mdx` | Section 4.1 (line 189); entry 6 line 37 | Fit with site rules (originality) | Distinctive clauses are reused from the source ("ranks correct predictions above incorrect ones"; "corresponds to an inner product ... (possibly infinite-dimensional)"). |
| S12 | Optional | `src/content/blog/deep-ensembles.mdx` | Figure caption (line 138) | Technical accuracy | "beyond about ±5.5": the recomputed crossings are −5.06 and 5.76, and the SVG `<desc>` gives only "below about x = −5". |
| S13 | Optional | `src/content/blog/laplace-approximations.mdx` | Section 3.3 (line 129) | Evidence | "(MacKay, 1992; ...)" is ambiguous among three MacKay 1992 references. |
| S14 | Optional | `src/content/blog/frontiers-of-bayesian-deep-learning.mdx` | lines 50, 190, 236 | Structure | Some *Open* items are statements, although line 20 says they are "phrased as questions". |
| S15 | Optional | `src/content/blog/variational-inference-for-neural-networks.mdx` | Section 2.2 (line 78) | Technical accuracy | "scaling one layer up and the next down leaves the function unchanged" holds only for positively homogeneous activations such as ReLU. |
| S16 | Optional | `src/content/series/bayesian-deep-learning.md` | line 22 | Overview completeness | The shared-notation paragraph omits the series-wide symbols $s_0$, $M$, $J$ and the reserved $S$ and $\Lambda$. |
| S17 | Optional | `src/content/blog/sampling-the-posterior-mcmc.mdx` | Section 5.3 (line 278) | Writing quality | "neither diagnostic of Section 7": Section 7 lists four checks, two of which are diagnostics. |
| S18 | Optional | entries 3 and 6 | entry 3 line 3; entry 6 lines 266, 268 | Terminology | "post hoc uncertainty" (modifier), "parametrization" and "Gauss-Newton" (hyphen) differ from the series forms "post-hoc", "parameterization" and "Gauss–Newton". |
| T1 | Should fix | `src/content/blog/deep-ensembles.mdx` | Section 8.1 (line 315) | Notation | Residue of S10: the prose writes $\ln(2\sqrt{2000}/0.05)$ and $\mathrm{KL} = \ln 5$ directly under the bound at line 310, which now writes $\log$. |
| T2 | Optional | `src/content/blog/scaling-bayesian-deep-learning.mdx` | Section 6 (line 252) | Notation | "$2000 / \ln 2 \approx 2885$ bits" is the only other $\ln$ in the series; the series writes $\log$ for natural logarithms. |

### S1. False section reference after renumbering
- **Where:** `src/content/blog/deep-ensembles.mdx:75`, section "2.1 Setup"
- **Text:** "The members predict only a mean, and the noise variance is fixed at its true value, so the average-noise term of Section 1.2 is $\sigma^2 = 0.01$ everywhere."
- **Problem:** Section 1.2 is now "The ensemble predictive" (line 29). The variance split with the "average noise" term is in "1.3 Splitting the predictive variance" (lines 43–49). This is a false cross-reference (standards 9.1, C6). It was introduced when D26 renumbered Section 1.
- **Recommended correction:** "... so the average-noise term of Section 1.3 is $\sigma^2 = 0.01$ everywhere."

### S2. Close paraphrase of the source in the deep kernel learning description
- **Where:** `src/content/blog/gaussian-processes-and-kernels.mdx:284`, section "5.1 Deep kernel learning"
- **Text:** "Prediction needs one forward pass through $g_\psi$ followed by GP prediction in the learned feature space, and the GP part supplies a predictive variance."
- **Problem:** Source (00-bdl-2, chapter on cost comparisons): "Deep kernel learning (Chapter 24) [1769] requires one forward pass through its feature extractor for each test input, followed by GP prediction in the learned feature space." The structure is the same and nine words match exactly ("followed by GP prediction in the learned feature space"); a second source passage repeats the phrase. The overview states that the text was written for the series, and the lead's rule is that close paraphrase is blocking.
- **Recommended correction:** "At test time the network is evaluated once and its output is treated as the input of an ordinary GP, so the predictive mean and variance come from the formulas of Section 2.2 applied to $g_\psi(x^*)$."

### S3. Close paraphrase of the source on myopic design
- **Where:** `src/content/blog/frontiers-of-bayesian-deep-learning.mdx:206`, section "6.2 Established practice and open problems"
- **Text:** "Most practical methods are **myopic**: they choose each design as if it were the last. Amortized methods train a network that maps the data gathered so far directly to the next design, ..."
- **Problem:** Source (part10, experimental design chapter): "the vast majority of active-learning methods choose a single design at a time and treat each design decision as if it were the last. This myopic approach ...", and elsewhere "we can use the data gathered so far". The claim, its order and the distinctive simile all match.
- **Recommended correction:** "Most practical methods are **myopic**: each design maximizes the immediate information gain and ignores the experiments that will follow. Amortized methods train a network that maps the observations made up to now directly to the next design, ..."

### S4. Monte Carlo pass count still written $S$
- **Where:** `src/content/blog/variational-inference-for-neural-networks.mdx:170` and `:176`, section "4.1 Monte Carlo dropout"
- **Text:** "averaging $S$ stochastic forward passes"; "at the cost of $S$ forward passes."
- **Problem:** The displayed formula at line 173 averages over $M$. The conventions file reserves $S$ for posterior covariances and makes $M$ the number of Monte Carlo samples. This is a residue of D21.
- **Recommended correction:** Replace $S$ by $M$ at lines 170 and 176.

### S5. Output-weight symbol inconsistent within entry 7 and with entry 6
- **Where:** `src/content/blog/priors-symmetries-and-identifiability.mdx:38`, section "1.3 Scaling with width"; also `gaussian-processes-and-kernels.mdx:170–179`, `:244–247`
- **Text:** Entry 7: "If all three have independent zero-mean priors and $v_j$ has variance $\sigma_v^2$, then ... $H s_v^2\, \mathbb{E}[\phi(u x + b)^2]$". Entry 6: "with $\operatorname{Var}(v_h) = \sigma_v^2$"; "With weight variance $\sigma_w^2$ divided by the fan-in"; entry 7 line 94: "weights of variance $s_w^2$ divided by the fan-in".
- **Problem:** In entry 7 the symbol is introduced as $\sigma_v^2$ and then used as $s_v^2$, so the formula uses an undefined symbol. The resolution notes say $\sigma_v$ was renamed $s_v$; line 38 was missed. Across entries 6 and 7 the same prior quantities have different symbols. The conventions reserve $\sigma$ for the noise standard deviation.
- **Recommended correction:** Entry 7 line 38: "and $v_j$ has variance $s_v^2$". In entry 6, rename $\sigma_v \to s_v$, $\sigma_w \to s_w$ and $\sigma_b \to s_b$ (lines 170, 173, 179, 244, 247). Alternatively, state in entry 6 that $\sigma_f$, $\sigma_v$, $\sigma_w$ and $\sigma_b$ are prior scales, not noise, and use the same symbols in entry 7.

### S6. Reserved symbols reused in entry 6
- **Where:** `src/content/blog/gaussian-processes-and-kernels.mdx:194` and `:247–250`
- **Text:** "$f(x)$ is Gaussian with variance $S = \frac{1}{H}\sum_h a_h^2$"; "where $\Lambda^{(l)}$ is the $2 \times 2$ covariance matrix of the layer-$l$ pre-activations".
- **Problem:** The binding conventions make $S$ a posterior covariance only and $\Lambda$ a precision matrix. Here $S$ is a random variance and $\Lambda^{(l)}$ a covariance. Entries 2 and 4 use $\Lambda$ for a precision.
- **Recommended correction:** Write $V = \frac{1}{H}\sum_h a_h^2$ (and $3\operatorname{Var}(V)/\mathbb{E}[V]^2$) at line 194. At lines 247 and 250 write $\Sigma^{(l)}$ for the $2 \times 2$ pre-activation covariance.

### S7. Forward reference points to the wrong entry
- **Where:** `src/content/blog/bayesian-inference-for-neural-networks.mdx:293`, section "5. A map of approximate inference"
- **Text:** "Ensembles of Laplace approximations combine several modes with local widths, and MCMC can be run in a low-dimensional subspace found by optimization. The [eighth entry](/blog/scaling-bayesian-deep-learning) collects these combinations when it deals with cost."
- **Problem:** Entry 8 covers last-layer Laplace (Section 2) and Laplace per ensemble member (Section 7), but never subspace MCMC; `grep subspace` finds nothing in it. Subspace inference with MCMC is in the tenth entry, Section 2.1 (`frontiers-of-bayesian-deep-learning.mdx:40–42`). The promise is therefore only partly fulfilled.
- **Recommended correction:** "... found by optimization. The [eighth entry](/blog/scaling-bayesian-deep-learning) collects the first two combinations when it deals with cost, and the [tenth](/blog/frontiers-of-bayesian-deep-learning) treats subspace inference."

### S8. Reference formats differ across entries, against the binding conventions
- **Where:** reference lists of entries 2–10
- **Text and problem:**
  - NeurIPS papers are given as "*Advances in Neural Information Processing Systems (NeurIPS)*, 2021" with no volume number in entry 3 (lines 376, 378, 383, 386), entry 4 (347, 348, 350, 351, 359, 362, 365, 368, 372), entry 7 (386, 389, 396, 398, 404) and entry 8 (348, 349, 357, 358, 360, 364, 371). BDL-CONVENTIONS requires "in *Advances in Neural Information Processing Systems 30*, 2017", which entries 1, 2, 5, 6, 9 and 10 use.
  - ICLR appears as "in *International Conference on Learning Representations (ICLR)*" in entries 2, 3, 4, 9 and 10, but as "in *Proceedings of the International Conference on Learning Representations (ICLR)*" in entries 5, 6, 7 and 8.
  - The same work is cited differently. Maddox et al. (2019) lists "T. Garipov, P. Izmailov" in entry 5 (line 399) and "P. Izmailov, T. Garipov" in entry 8 (line 360); which order is correct was not verified, but both cannot be. Garipov et al. (2018) has "D. Vetrov" in entries 5 and 10 and "D. P. Vetrov" in entry 7. The Daxberger et al. (2021) title is "Laplace Redux: Effortless ..." in entries 1 and 9 and "Laplace redux – effortless ..." in entries 3 and 8. Titles are in title case in entries 1, 2, 9 and 10 and in sentence case in entries 3–8, so for example Wenzel et al. and Izmailov et al. differ between entries 2, 4, 5 and 7.
- **Recommended correction:** Use the NeurIPS form with the volume number (2007 = 20, 2011 = 24, 2015 = 28, 2016 = 29, 2017 = 30, 2018 = 31, 2019 = 32, 2020 = 33, 2021 = 34, 2022 = 35, 2023 = 36, 2001 = 14) in entries 3, 4, 7 and 8. Choose one ICLR form, preferably "in *Proceedings of the International Conference on Learning Representations (ICLR)*" per the conventions template, and apply it everywhere. Check the Maddox et al. author order against the paper and use it in both entries. Use one title form for each work across the series.

### S9. The Kronecker product is used without being introduced
- **Where:** `src/content/blog/laplace-approximations.mdx:91`, section "2.3 Making the curvature affordable"; `scaling-bayesian-deep-learning.mdx:154–166`
- **Text:** "approximate the block of the GGN by a Kronecker product $A \otimes G$"; entry 8: "then $A \otimes G + \alpha I$ has eigenvectors $Q_A \otimes Q_G$ and eigenvalues $\lambda_{A,i} \lambda_{G,j} + \alpha$".
- **Problem:** The overview's prerequisite is "linear algebra at the level of eigenvalues and positive-definite matrices". No entry says what $A \otimes G$ is, yet entry 8 builds a derivation and a listing on its properties (standards 6.1, concepts before mechanics).
- **Recommended correction:** In entry 3 after "Kronecker product $A \otimes G$", add: "(the block matrix whose $(i, j)$ block is $A_{ij} G$, so an $m \times m$ and an $n \times n$ factor give an $mn \times mn$ matrix)". Entry 8 can then refer back to it.

### S10. Entropy notation differs for the same decomposition
- **Where:** `src/content/blog/deep-ensembles.mdx:60`, `:63`; `gaussian-processes-and-kernels.mdx:85`, `:92`
- **Text:** "$H[\bar p] = \frac{1}{J}\sum_{j} H[p_j] + \dots$", "where $H[p] = -\sum_c p_c \ln p_c$".
- **Problem:** Entry 5 says "The same split applies" as entry 1 Section 2.2, but writes it with $H$ and $\ln$, whereas entries 1 and 9 use $\mathbb{H}$ and $\log$ ("logarithms are natural", entry 1 line 23). $H$ already denotes the Hamiltonian (entry 2) and the Hessian (entry 3). Entry 6 likewise writes $\ln p(y \mid X)$ where the rest of the series writes $\log p(\mathcal{D})$.
- **Recommended correction:** In entry 5 write $\mathbb{H}$ throughout Section 1.4 and $\log$ in the definition. In entry 6, Sections 2.3–2.4, write $\log$.

### S11. Distinctive phrases reused from the source
- **Where:** `src/content/blog/evaluating-and-using-uncertainty.mdx:189`; `gaussian-processes-and-kernels.mdx:37`
- **Text:** Entry 9: "the question becomes how well its confidence ranks correct predictions above incorrect ones." Entry 6: "every positive semi-definite kernel corresponds to an inner product of some, possibly infinite-dimensional, feature map".
- **Problem:** Source (part09, selective classification): "how well the chosen confidence score ... ranks correct predictions above incorrect ones". Source (kernel chapter): "the kernel corresponds to an inner product in some (possibly infinite-dimensional) feature space". These are clause-level reuses rather than whole-sentence paraphrases, so they are not blocking, but they should be reworded.
- **Recommended correction:** Entry 9: "the question becomes whether higher confidence reliably goes with a correct prediction." Entry 6: "Conversely, Mercer's theorem and its relatives show that every positive semi-definite kernel can be written as $\phi(x)^\top\phi(x')$ for some feature map $\phi$, which may have infinitely many components (Schölkopf and Smola, 2002)."

### S12. Ensemble caption imprecise about where the truth leaves the band
- **Where:** `src/content/blog/deep-ensembles.mdx:138` (and `src/components/diagrams/BdlEnsembleDisagreement.astro:7`)
- **Text:** "... at x between about 3.3 and 4.9 and beyond about ±5.5, where the truth leaves the band."
- **Problem:** Retraining the five members and scanning $x \in [-7, 7]$ in steps of 0.005 puts the transitions at −5.06, 3.23, 4.96 and 5.76. Between −5.5 and −5.06 the truth is already outside the band; between 5.5 and 5.76 it is still inside. The SVG `<desc>` gives only "below about x = −5" and omits the right-hand region.
- **Recommended correction:** Caption: "... at x between about 3.2 and 5.0, below about −5.1 and above about 5.8, where the truth leaves the band." Update the generator's `<desc>` text to match.

### S13. Ambiguous MacKay citation
- **Where:** `src/content/blog/laplace-approximations.mdx:129`
- **Text:** "gives an accurate approximation (MacKay, 1992; Bishop, 2006)"
- **Problem:** The entry lists three MacKay 1992 papers. The probit moderation comes from "The evidence framework applied to classification networks". E7 fixed the same ambiguity in entry 7 by naming the papers.
- **Recommended correction:** "(MacKay, *The evidence framework applied to classification networks*, 1992; Bishop, 2006)".

### S14. Some *Open* items are not phrased as questions
- **Where:** `src/content/blog/frontiers-of-bayesian-deep-learning.mdx:50`, `:190`, `:236`
- **Text:** Line 190: "And the conditions exclude common cases, such as networks with rectified linear units, whose models are not analytic." Line 236: "An approximate posterior that is too narrow, ... under-explore."
- **Problem:** Line 20 promises that "statements under *Open* are questions without an agreed answer, phrased as questions." These sentences are statements of fact or context.
- **Recommended correction:** Move such sentences in front of the question as context, or rephrase them. For example, line 190: "And since networks with rectified linear units are not analytic models, which parts of the theory still hold for them?"

### S15. Rescaling claim needs its condition
- **Where:** `src/content/blog/variational-inference-for-neural-networks.mdx:78`
- **Text:** "scaling one layer up and the next down leaves the function unchanged"
- **Problem:** This holds for positively homogeneous activations such as ReLU (entry 7, Section 4.2), not for tanh or sigmoid.
- **Recommended correction:** "with ReLU activations, scaling one layer up and the next down leaves the function unchanged".

### S16. Overview notation paragraph incomplete
- **Where:** `src/content/series/bayesian-deep-learning.md:22`
- **Text:** "$P$ is the number of parameters, $C$ the number of classes and $\sigma$ the standard deviation of Gaussian observation noise."
- **Problem:** The entries also share $s_0$ (prior standard deviation, with $\alpha = 1/s_0^2$), $M$ (Monte Carlo samples) and $J$ (ensemble size), and they reserve $S$ and $\Lambda$. Standards 6.5 asks the overview to state shared conventions once.
- **Recommended correction:** Append: "$s_0$ is the standard deviation of a Gaussian prior on each weight ($\alpha = 1/s_0^2$ where a precision is clearer), $M$ the number of Monte Carlo samples and $J$ the number of ensemble members."

### S17. "neither diagnostic" with four items
- **Where:** `src/content/blog/sampling-the-posterior-mcmc.mdx:278`
- **Text:** "neither diagnostic of Section 7 would detect it without the exact answer."
- **Problem:** Section 7 lists four checks. Only $\hat{R}$ and the ESS are diagnostics, and the fourth check, "Check against a known answer", is the exception the sentence itself names.
- **Recommended correction:** "neither $\hat{R}$ nor the effective sample size (Section 7) would detect it without the exact answer."

### S18. Minor spelling variants
- **Where:** `laplace-approximations.mdx:3` ("post hoc uncertainty"); `gaussian-processes-and-kernels.mdx:266` ("parametrization"), `:268` ("Gauss-Newton")
- **Problem:** The series forms are "post-hoc" before a noun (E19), "parameterization" (entries 3 and 4) and "Gauss–Newton" with an en dash (entries 3 and 8).
- **Recommended correction:** "post-hoc uncertainty"; "parameterization"; "Gauss–Newton".

### T1. Natural logarithm still written $\ln$ in entry 5, Section 8.1
- **Where:** `src/content/blog/deep-ensembles.mdx:315`, section "8.1 Frequentist bounds with a prior"
- **Text:** "the logarithmic term is $\ln(2\sqrt{2000}/0.05) \approx 7.49$"; "costs $\mathrm{KL} = \ln 5 \approx 1.61$".
- **Problem:** The S10 resolution changed the displayed bound at line 310 to $\log(2\sqrt{N}/\delta)$ and states that all $\ln$ in entry 5 became $\log$, but these two prose occurrences were missed. The same quantity is now written two ways in consecutive paragraphs. The numbers are correct (recomputed 7.489, 0.043 and 0.048).
- **Recommended correction:** "$\log(2\sqrt{2000}/0.05) \approx 7.49$" and "$\mathrm{KL} = \log 5 \approx 1.61$".

### T2. One $\ln$ in entry 8
- **Where:** `src/content/blog/scaling-bayesian-deep-learning.mdx:252`
- **Text:** "can be communicated in about $2000 / \ln 2 \approx 2885$ bits"
- **Problem:** Correct (2885.4), and $\ln 2$ is a common way to write a nats-to-bits conversion, but the series otherwise writes $\log$ for natural logarithms.
- **Recommended correction:** "$2000 / \log 2 \approx 2885$ bits", or leave as is.

## Concept introduction map

| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Prior, likelihood, posterior, evidence | bayesian-inference-for-neural-networks.mdx:23 | same file, 35–49 | Good. |
| Posterior predictive, Bayesian model averaging | bayesian-inference-for-neural-networks.mdx:21 | same file, 67–74 | Good. |
| Aleatoric and epistemic uncertainty, entropy, mutual information | bayesian-inference-for-neural-networks.mdx:86 | same file, 86–106 | Good. |
| Gaussian distribution notation $\mathcal{N}(\mu, \Sigma)$ | bayesian-inference-for-neural-networks.mdx:23 | same line | Good. |
| KL divergence | bayesian-inference-for-neural-networks.mdx:289 (table) | variational-inference-for-neural-networks.mdx:28–34 | Acceptable: the table names the fourth entry. |
| Markov chain, stationary distribution, detailed balance | sampling-the-posterior-mcmc.mdx:31 | same file, 31, 45–51 | Good. |
| Hessian, Jacobian, GGN, Fisher information | laplace-approximations.mdx:39, 66, 76, 84 | same lines | Good. |
| Kronecker product | laplace-approximations.mdx:91 | not introduced | S9. |
| vec operator (column stacking) | scaling-bayesian-deep-learning.mdx:154 | same line | Good. |
| Gaussian process, kernel | laplace-approximations.mdx:125 (forward aside) | gaussian-processes-and-kernels.mdx:37, 51 | Acceptable: a forward pointer to the sixth entry. |
| Neural tangent kernel | laplace-approximations.mdx:125 | gaussian-processes-and-kernels.mdx:264 | Acceptable: forward pointer. |
| Reparameterization trick, ELBO | variational-inference-for-neural-networks.mdx:43–55 | same | Good. |
| Proper scoring rule | deep-ensembles.mdx:37 | same line (brief); evaluating-and-using-uncertainty.mdx:45 (full) | Good. |
| PAC-Bayes, tandem loss | deep-ensembles.mdx:307, 321 | same lines | Good. |
| Weight-space symmetry, identifiability | bayesian-inference-for-neural-networks.mdx:256 | priors-symmetries-and-identifiability.mdx:166, 260 | Good. |
| Calibration | bayesian-inference-for-neural-networks.mdx:304 | same line; evaluating-and-using-uncertainty.mdx:31 | Good. |
| Bi-Lipschitz, spectral normalization | scaling-bayesian-deep-learning.mdx:216, 226 | same lines | Good. |
| Exchangeability, de Finetti | frontiers-of-bayesian-deep-learning.mdx:58 | same line | Good. |
| Real log canonical threshold, free energy | frontiers-of-bayesian-deep-learning.mdx:134–140 | same | Good. |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| Python 3.13, NumPy 2.5.3 | every listing | Overview line 14 and each entry's opening | Good; verified with Python 3.13.16 and NumPy 2.5.3. |
| Natural logarithms, nats | entries 1 and 9 | entry 1:23, entry 9:23 | Entry 5 uses $\ln$, entry 6 $\ln$ (S10). |
| Decimal versus binary memory units | entry 3 Exercise 4; entry 8 | entry 3:357 (decimal); entry 8:20 (binary) | Good; both stated. |
| 32-bit floats (4 bytes) | entries 3 and 8 | yes | Good. |
| Column vectors | entries 1 and 3 | yes | Good. |
| vec by column stacking in K-FAC | entry 8 | 154, 181 (code `order="F"`) | Good. |
| Loss orientation of scoring rules (lower is better) | entry 9 | 45 | Good. |
| Prior parameterized by $s_0$ or $\alpha = 1/s_0^2$ | entries 1, 3, 4, 5, 8 | each entry states it | Good; not in the overview (S16). |
| NTK parameterization | entry 6 | 266 | Stated. |
| Fixed random seeds | every stochastic listing | yes | Good. |
| Library versions in entry 9, Section 8 | entry 9 | 359 explains that none are named | Deliberate and stated. |

## Series design

**Purpose, audience and scope.** The overview states the reader (people who have trained networks), the prerequisites (the Machine Learning Fundamentals series, probability with Bayes' theorem, linear algebra up to eigenvalues and positive-definite matrices), the content and the order. The prerequisite list does not cover the Kronecker product used in entries 3 and 8 (S9).

**Sequence and rationale.** Problem, then four inference families in decreasing directness, then function space, priors, scale, practice and frontiers. The order is sound and the overview explains it (E27).

**Prerequisites and dependencies.** No entry depends on a later one. Entry 3's GP and NTK remarks are explicit forward pointers to entry 6. Entry 1's forward reference for subspace MCMC points to the wrong entry (S7).

**Notation and depth.** Depth is comparable throughout: every entry has a runnable worked example, exercises with answers, a summary table and references. Notation is mostly aligned with the conventions file; S4, S5, S6 and S10 are the remaining exceptions.

**Overview completeness.** The overview matches the entries. The shared-notation paragraph could add $s_0$, $M$ and $J$ (S16).

## Series-level notes

- **Terminology.** "mini-batch" is used throughout (no "minibatch" remains). "squared-exponential kernel" and "lengthscale" are consistent, with RBF mentioned once (entry 6, line 39). K-FAC and $A \otimes G$ with the conventions' definitions appear in entries 3 and 8. "post-hoc" before a noun is used in entries 8 and 9, but not in entry 3's description (S18).
- **Izmailov et al. (2021).** Entries 2 (line 304) and 5 (line 198) describe it identically per the conventions; entry 2 is aligned. Entry 2 line 314 cites the same paper for the data-augmentation explanation of the cold posterior, which is consistent with entry 7 line 160.
- **Cross-reference map.** Every "entry N, Section X.Y" reference was checked against the current headings: e2→e1 §4.2 (twice), e5→e1 §2.2, §3 and Exercise 1, e9→e1 §2.2, e10→e7 §4.2, e10→e9 §2 and §5. All are correct. Intra-entry section references were checked in all ten entries. The one failure is entry 5 line 75 (S1). The "next entry" closing links all point to the actual next entry, and entry 10 walks through the five objectives.
- **Promises checked:** e1→e3 evidence for networks (yes); e1→e8 combinations (partly, S7); e2→e5 HMC comparison (yes, §3.3); e2→e7 prior side of cold posteriors (yes, §3.4); e3→e6 NTK (yes, §4); e3→e8 trade-offs at scale (yes); e4→e7 tempering (yes); e6→e7 NNGP use (yes, §1.3); e6→e8 distance-preserving extractors (yes, §4); e7→e8 last-layer evidence (yes, §2.4).
- **Structure and tone.** The structure is uniform: opening without heading, numbered sections, exercises, Summary with a table, references. The tone is consistent. Entry 10's *Established*/*Open* format is applied throughout, with S14 as a minor gap.

## Verification log

- `npm run build:local`: exit 0. `astro check` 0 errors, 0 warnings, 0 hints; Pagefind indexed 2 languages and 138 pages; localhost warning from `check-site-url` as expected for a local build.
- `npm run check:links`: 417 pages and 13 203 internal references checked; all resolve.
- `npm run -s eos -- validate-site`: 417 pages checked; no issues.
- `npm run -s eos -- lint` on the 11 series files: 0 errors, 0 warnings, 33 suggestions. These are sentence length, acronyms such as FAC, DNN and ACRR inside names or titles, and one serial-comma false positive on an appositive at entry 9:181. None needs a change.
- Mermaid diagrams: largest min-width 377px (entry 8), 291px (entries 1 and 6); none above 600px.
- Text glued to inline elements: only KaTeX-internal `lo<span>g` matches (false positives).
- Listings: all code blocks of all ten entries were extracted and run, each entry as one script, under Python 3.13.16 and NumPy 2.5.3. All quoted output matches exactly. Run times: entry 2 18.6 s (text says "about 15 seconds"), entry 5 7.5 s for three listings, entry 7 44.8 s, the rest under 4 s.
- Recomputed:
  - Entry 1: $50!\,2^{50} = 3.42 \times 10^{79}$. $s_0 = 0.3$ gives an epistemic sd of 0.325 at 4.5 and 0.112 at −2, with prior value 0.332. $s_0\lVert\phi(4.5)\rVert = 1.106$. Seed 3 gives a gap mean of −0.587. Exercise 3 gives 0.0146. Bump contributions at 4.5 are −0.036 and −0.074. $e^{3.25} \approx 26$. Exercise 2 entropies are 0.673, 0.500, 0.587 and 0.086.
  - Entry 2: principal sds range from 0.081 to 1.0 and include 0.382; $\lambda_{\max} = 152.2$. Fixed and jittered HMC over seeds 0–5 give 0.140–0.160 (mean 0.149) and 0.134–0.145 (mean 0.138). Exercise 3 gives 1.18 and $1.3 \times 10^{-4}$. The figure's sds are 0.224 and 1.396. ESS ratio 493/17 ≈ 29; 16 000/17 ≈ 940.
  - Entry 3: $\Phi(1.326/0.498) = 0.996$; probit limit 0.986. Exercise 1 gives 0.2165, Beta sd 0.178 and tail 0.124. Exercise 4 gives 400 TB, 40 MB, 105 MB and about 1 MB. The six $\alpha$ values are ranked identically by both evidences, with a maximum gap of 0.126.
  - Entry 4: $r = -0.8625$, ratio 1.976, minimum KL 0.681. Exercise 5 terms are 0.0482, −0.0783, 0.0427 and 0.0126. Mean-field sd exceeds exact sd on $x \in [1.22, 3.71]$, inside the training range [0.11, 3.80], consistent with "most of the shaded range". The step-size decay ends at 0.000995.
  - Entry 5: Section 1.4 example gives a mutual information of 0.194. $s_0 = 1.58$ and 0.5. Exercise 2 retrained gives a spread of 0.005. Band crossings are at −5.06, 3.23, 4.96 and 5.76 (S12). PAC terms are 7.49, 0.043 and 0.048. Monte Carlo error 0.003.
  - Entry 6: Exercise 1 gives 0.600 and 0.797; Exercise 4 gives 0.279; the log-marginal-likelihood gaps are 2.5 and 11.7.
  - Entry 7: $(2^8 8!)^2 = 1.07 \times 10^{14}$; $(2^{100} 100!)^2 = 1.4 \times 10^{376}$. Exercise 1 gives 184 320. Exercise 2 gives 0.795. Exercise 4 algebra checked.
  - Entry 8: $4 \times 10^{14}$ B = 363.8 TiB. The 1024×1024 block is 4 TiB, the factors 8 MiB and the diagonal 4 MiB. Exercise 1 gives 17.0 MiB. The SVGP step costs $1.9 \times 10^8$. Exercise 4 ratio 6.65. 2000 nats / ln 2 = 2885 bits. $K^2C^2 = 4.2 \times 10^{12}$.
  - Entry 9: table scores 0.611, 0.765, 0.693, 0.42 and 0.50. BALD 0.431 and 0.495. ECE ratio 11. Exercise 3 checked.
  - Entry 10: 1/30 for both sequences. Exercise 3 gives 9.21 and 23.0. The slope formula $\tfrac12 - 1/\log n$ checked.
- Originality: a 5-gram scan of each entry body, without its references, was run against both source volumes (00-bdl-1.txt, 00-bdl-2.txt) with `d15/ngram.py`. A sentence-level scan followed (4-gram overlap ratio of at least 0.5, or two or more 8-gram runs). The worked examples were checked for signatures in the source (rule of succession, 18 432, $(ab)^2$, BALD probabilities, $15/H$, $\sin(2x)$): none found. Section structure of entries 9 and 10 was compared with the part09 and part10 chapter outlines; the topic order is shared, as the overview declares, and the prose is the entries' own except S2, S3 and S11. Remaining matches are standard terminology.
- Not verified:
  - Bibliographic details recalled rather than checked against the publications: the pages added under D36, the Maddox et al. (2019) author order (S8), and missing pages for Neal (2011), Chen et al. (1993), Sussmann (1992) and Honkela and Valpola (2004).
  - Empirical results attributed to cited papers. Examples: Lee et al. (2018), Arora et al. (2019), Ovadia et al. (2019), Fort et al. (2019), Shen et al. (2024), Yang et al. (2024), Kadavath et al. (2022), Kuhn et al. (2023), Hollmann et al. (2025, "up to 10 000 samples"), Falck et al. (2024) and Tran et al. (2022).
  - Entry 8's SWAG memory row ("$P$ to $(r + 2)P$").
  - The overview's statement about who authored the source collection, which the owner confirmed.
- Third pass (verification of commit ae8d3c0, 2026-10-21):
  - `npm run build:local`: exit 0; `astro check` 0 errors; Pagefind indexed 2 languages and 138 pages; localhost warning from `check-site-url` as expected for a local build.
  - `npm run check:links`: 417 pages and 13 204 internal references; all resolve.
  - `npm run -s eos -- validate-site`: 417 pages; no issues.
  - `npm run -s eos -- lint --quiet`: 86 files, 0 errors, 1 warning (`signals-and-systems-in-discrete-time.mdx:27`, outside this series). On the 11 series files: 0 errors, 0 warnings, 33 suggestions.
  - Listings: all 22 Python blocks extracted afresh and run per entry under Python 3.13.16 and NumPy 2.5.3; every quoted output matches exactly (entry 2 15.8 s, entry 5 7.1 s, entry 7 50.0 s, the rest under 4 s).
  - Recomputed: entry 5 band crossings −5.06, 3.23, 4.96 and 5.76 (scan of $[-7, 7]$ in steps of 0.005) agree with the new caption and `<desc>`; entry 5 PAC terms 7.489, 0.043 and 0.048; entry 8 2000 / ln 2 = 2885.4.
  - Residue grep over the ten entries for $\sigma_v$, $\sigma_w$, $\sigma_b$, $\ln$, $H[$, "(NeurIPS)", the bare ICLR form, "D. P. Vetrov", "Laplace Redux", "minibatch", "post hoc", "parametrization" and "Gauss-Newton": only the two $\ln$ lines of T1 and T2.
  - References: script check of the ten reference lists finds no work cited in two forms, no title-case title, no NeurIPS entry without volume and no non-standard ICLR form; every NeurIPS volume matches its year. The fix commit adds no pages.
  - Cross-references: every "entry N, Section X" and "Section X of the [Nth entry]" reference re-checked against the current headings (e2→e1 §4.2 twice, e5→e1 §2.2, §3 and Exercise 1, e8→e3 §2.3, e9→e1 §2.2, e10→e9 §2 and §5, e10→e7 §4.2); all correct.
  - Originality: `d15/ngram.py` (5-grams) and a maximal-run scan (6 words and more) of each entry body without code and references against its source parts (1: part01+part06; 2: part01; 3: part02; 4: part03; 5: part04; 6: part05; 7: part06+part07; 8: part08; 9: part09+part10; 10: part10). Longest run 9 words, "the true conditional distribution of y given x and" (entry 10:254, a standard formulation in an unrelated context); all other runs of 6–7 words are terms or generic phrases ("the maximum a posteriori MAP estimate", "known as the neural tangent kernel NTK", "a single GP with a stationary kernel"). No hit on the rewritten S2, S3 and S11 sentences.
  - `eos status`: all 11 series files `needs-review` (no review records yet), as expected before recording.
