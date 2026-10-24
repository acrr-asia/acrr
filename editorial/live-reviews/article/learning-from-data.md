# Live review: Learning from Data: Models, Loss Functions and Risk

- URL: https://acrr.asia/blog/learning-from-data
- Source: `src/content/blog/learning-from-data.mdx` (Machine Learning Fundamentals, entry 1)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 19 desktop-light, 36 mobile-light, 36 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): at 360 px the two displays that carry the results of Sections 3.2 and 5.4 are cut off, and the cut parts are not restated in full elsewhere. The desktop page is clean, the argument is sound and every number on it was reproduced in this review. The other findings are minor.

**Library decision: retain and update.** This is the vocabulary entry of the Machine Learning Fundamentals series (risk, empirical risk, ERM, Bayes risk, training error), on which entries 2 to 4 build explicitly; Generalization, Overfitting and Regularization reuses its definitions and its Bayes-risk floor. The content is correct and well ordered, and nothing on the site replaces it. The update needed is presentational (L1 to L3, narrow screens) plus one small content addition the page itself promises (L4). A rewrite, merge or reclassification would gain nothing.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a programmer comfortable with calculus, linear algebra and elementary probability who is starting machine learning and wants its framing rather than a library tutorial.
- Problem: understanding what a supervised learning problem is made of, what "a good model" means, and why the error on the training data is not the number that matters.
- Outcome: define features, labels, model family, hypothesis class and loss; compare the common losses; define risk, Bayes risk, empirical risk and ERM; derive the conditional mean as the best squared-loss predictor; compute the exact risk of a fitted line on synthetic data and explain why training error is optimistic; state the held-out rule.
- Distinctive contribution: a synthetic example in which the risk is known exactly, so training error, Bayes risk and the fitted line's true risk can be put side by side (0.1124, 0.2500, 0.2584), with a reproducible seeded script.
- Evidence: derivations in the text; one NumPy script with its quoted output; Bishop (2006); Hastie, Tibshirani and Friedman (2009); James et al. (2013); Shalev-Shwartz and Ben-David (2014); Vapnik (1995).
- Limitations: supervised learning only; one feature and a linear model in the worked example; no generalization bounds; evaluation deferred to entry 4.

The benefit is delivered. Spot checks recomputed in this review: the script re-run with Python 3 and NumPy 2.5.3 reproduces `w = [1.181 1.707]`, 0.1124 and 0.2578 exactly; $a = 0.1812$, $b = -0.2929$, $a^2 + ab + b^2/3 = 0.00836$, so the risk is 0.2584; cross-entropy values 0.105, 2.303, 0.693, 0.223 and 1.609; the MSE and MAE table (20.4, 2.4; 16.4, 3.2); $\sigma^2(n - p)/n = 0.225$; Exercise 4, 0.29. A 20,000-repetition simulation of the same setup gives a mean training MSE of 0.224, confirming the formula.

Value density: high. The three-number table of Section 5.4 is the most valuable thing on the page, because it makes "training error is optimistic" visible with exact numbers; Section 4 shows in five labels why the loss matters. The list of the four entries in the opening and the Summary table are useful navigation. No section is padding.

Overlap with other ACRR articles: the Vietnamese-original series Machine Learning from the Ground Up covers loss functions and linear regression (`/vi/blog/ml-basic-concepts`, `/vi/blog/ml-linear-regression`) from a different angle (library-based, no risk framing); the two do not link to each other. Generalization, Overfitting and Regularization reuses this entry's Bayes-risk floor by design and says so. Value category: conceptual understanding. Format: explainer.

## C. Substantive findings

### L4. The seed's luck is noted but not quantified

- Location: Section 6, first paragraph ("The sample in Section 5 happened to fall well below even that average"), and Section 5.4 ("the price of estimating two parameters from 20 noisy points").
- Problem: the opening promises that "where a result varies noticeably from one seed to another, the text says by how much", but Section 6 only says the training MSE fell "well below" its expected value 0.225, without saying how unusual that is, and Section 5.4 presents the excess risk of 0.0084 as "the price" of estimating two parameters although it is one sample's value. In a simulation run for this review (20,000 repetitions of the same setup) only about 4% of samples have a training MSE as low as 0.1124 (90% fall between 0.12 and 0.36), and the average excess risk is about 0.027, three times this sample's.
- Why it matters: a reader who takes the seeded numbers as typical underestimates both the spread of training error and the usual cost of estimation, which are the subjects of entries 3 and 4.
- Required action: add one or two sentences in Section 6 (or after the 5.4 table) giving the spread over repeated samples and the average excess risk, computed by a stated, reproducible run; call 0.0084 "this sample's excess risk".
- Priority: minor
- Acceptance condition: the live page states how typical the seed's training MSE and excess risk are, with numbers from a stated computation.

## D. Visual and structural findings

### L1. Result displays of Sections 3.2 and 5.4 cut at 360 px

- Location: Section 3.2, the decomposition after "Expanding around the conditional mean" (mobile-light-16); Section 5.4, the risk of the fitted line (mobile-light-25); the same tiles in dark mode.
- Problem: at 360 px both displays are wider than the column and their right end is hidden behind an unmarked sideways scroll. In 3.2 the reader sees "$= (c - \mu(\mathbf{x}))^2 + \mathrm{V}$" and the variance term, the irreducible error the section is about, is cut. In 5.4 the reader sees "$R(\hat{\mathbf{w}}) = \sigma^2 + \mathbb{E}[(a + bx)^2] = \sigma^2 +$" and the formula $a^2 + ab + b^2/3$ used to compute 0.2584 is hidden; it appears nowhere else on the page.
- Why it matters: these are the two results the page's argument rests on (the Bayes floor and the exact risk of the fitted line). A phone reader who does not discover the hidden scroll cannot follow or check the computation of the key number.
- Required action: break both displays over lines (for example an `aligned` block with the right-hand side on its own line), so that no line is wider than about 300 px.
- Priority: major
- Acceptance condition: on new 360 px captures (light and dark) both displays are fully visible without sideways scrolling; at 1280 px they still render on as few lines as before or fewer.

### L2. Other cut displays and the loss table at 360 px

- Location: Section 2.2 linear-model display (mobile-light-11); Section 2.3 loss table (mobile-light-12 and 13); Section 5.1 data-generating display (mobile-light-21).
- Problem: at 360 px the loss table shows only the Loss and Formula columns; Task and Notes are beyond the scroll shadow, and the cross-entropy formula itself is cut at "$\ln(1 - p$". The Section 2.2 display stops at "$w_2 x_2 + \cdots$" (only the final $+ w_d x_d$ is hidden, so the meaning survives). The Section 5.1 display shows "$y = 1 + 2x$" and hides the noise distribution $\varepsilon \sim \mathcal{N}(0, 0.5^2)$; the noise variance is restated in the next paragraph, so this one is minor.
- Why it matters: the Notes column carries the comparison (smoothness, outlier sensitivity, differentiability) the table exists for.
- Required action: put the three parts of the 5.1 display on separate lines (and shorten or break the 2.2 display); for the table, either drop the Task column into the Loss cell ("Squared loss (regression)") so three columns fit, or accept the scroll with a visible cue (site-level).
- Priority: minor
- Acceptance condition: at 360 px the 2.2 and 5.1 displays are fully visible and the loss table's Notes are visible without scrolling, or a visible cue shows that the table scrolls.

### L3. Ingredients diagram: last node off-screen at 360 px

- Location: Section 2, the Mermaid flowchart (mobile-light-08, mobile-dark-08).
- Problem: the left-to-right diagram keeps its minimum width at 360 px, so the last node, "Predictions on new x", is hidden to the right with no scroll cue.
- Why it matters: small; the node the diagram leads to is the one a phone reader does not see.
- Required action: a top-to-bottom layout (`flowchart TB`) for this diagram, or the site-level scroll cue for wide figures.
- Priority: minor (the site-wide part is also recorded on Spectra: The DFT and the FFT, L2)
- Acceptance condition: at 360 px all six nodes are visible, or a visible cue shows that the figure scrolls.

At 1280 px every equation, table, code block and the diagram fit (desktop-light-04 to 18). Dark mode renders the diagram, tables and code correctly (mobile-dark-08, 16, 23).

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors. The five textbook references are standard and support the material; chapter and page were not checked in this review. Code blocks scroll sideways inside their frame at 360 px, which is the site's normal behavior for code.

## F. Required changes

Mandatory:

- [ ] L1: split the Section 3.2 and 5.4 displays so that they fit at 360 px.

Optional:

- [ ] L2: split the 5.1 display; make the loss table fit or show a scroll cue.
- [ ] L3: top-to-bottom layout for the ingredients diagram.
- [ ] L4: quantify how typical the seed's training MSE and excess risk are.
- [ ] Section 2.1, desktop-light-05: the final "$y$." of "a whole conditional distribution of $y$." wraps so that the period sits alone on the next line; keeping the period inside the math or rewording avoids it.
- [ ] A link from the Vietnamese-original series' loss-function entry to this one (and back, once a Vietnamese translation exists) would connect two treatments of the same concepts.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
