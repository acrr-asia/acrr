<!-- audit: {"slug":"learning-from-data","type":"article","series":"machine-learning-fundamentals","priority":"P1","before":{"purpose":4,"structure":4,"accuracy":4,"evidence":3,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":5}} -->
# Audit: Learning from Data: Models, Loss Functions, and Risk

- Path: `src/content/blog/learning-from-data.mdx` · Route: `/blog/learning-from-data` · Type: article (series entry) · Series `machine-learning-fundamentals`, entry 1 of 4 · Words: 3315 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4
- structure 4: context, concepts, derivation, worked example, limits, exercises, summary, in that order.
- accuracy 4: the Python block was rerun with Python 3.13.16 and NumPy 2.5.3 and reproduces the quoted output byte for byte. Recomputed: risk of the fitted line 0.25836 (excess 0.00836); cross-entropy values 0.105, 2.303, 0.693, 0.223, 1.609; MSE table 20.4/16.4 and MAE 2.4/3.2; expected training MSE $\sigma^2(n-p)/n = 0.225$. All correct.
- evidence 3: five real textbooks, but not in alphabetical order and "2nd edition" instead of "2nd ed.".
- language 3: "actually", "really", "very"; a 55-word and a 53-word sentence in the opening paragraph.
- consistency 3: six title-case section headings; "2 %" and "98 %" (house style: no space); "numpy" for NumPy.
- publishing 2: description 326 characters, a list of contents.

## Priority

P1: the foundational first entry of the series; every later entry relies on its definitions.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 326 characters, a list of every section. |
| C1 | Should fix | `:32`, `:58`, `:117`, `:165`, `:178`, `:261` | consistency | Title-case headings. |
| C2 | Should fix | `:328–332` | evidence | References not alphabetical; "2nd edition". |
| C3 | Should fix | `:15` | language | Opening sentences of 55 and 53 words; "the number one actually cares about". |
| C4 | Optional | `:141` | language | "The same argument with the absolute loss gives the conditional median" (the completing-the-square argument does not apply to the absolute loss). |
| C5 | Optional | `:176` | language | "If a large error really is much more costly". |
| C6 | Optional | `:237` | language | "QR- or SVD-based solver": abbreviations not expanded. |
| C7 | Optional | `:293`, `:298`, `:23` | consistency | "2 %", "98 %", "numpy". |
| C8 | Optional | `:321` | language | "make that very error small". |

### C4. "The same argument"
- **Where:** `:141`, Section 3.2
- **Text:** "The same argument with the absolute loss gives the conditional **median** of $y$, and with the zero-one loss it gives the most probable class."
- **Problem:** the argument just given is completing the square, which is specific to the squared loss. What carries over is the method (minimize the conditional expected loss at each $\mathbf{x}$), not the argument.
- **Correction:** "Minimizing the conditional expected loss at each $\mathbf{x}$ in the same way gives the conditional **median** of $y$ for the absolute loss, and the most probable class for the zero-one loss."

### C3. Opening paragraph
- **Where:** `:15`
- **Text:** "... all do the same thing: they produce a prediction for a case they have never seen, using rules that were not written by hand but extracted from past cases whose answers are known." / "... and why the error a model makes on the data it was fitted to is not the number one actually cares about."
- **Problem:** two sentences over 50 words (standards 5.2); "actually" adds nothing; serial comma before "and a program" (house style omits it).
- **Correction:** split each sentence; "the number that matters".

## Revision log (wave 1)

- Structure: unchanged (already in the required order; opening, numbered sections, exercises, Summary with a lead to entry 2, References).
- Prose: opening paragraph split into shorter sentences, serial comma removed, "actually" cut; Section 3.2 sentence on the median and most probable class rewritten (C4); "really is much more costly" → "costs disproportionately more"; summary row "that very error" → "the training error itself".
- Terminology/style: six headings to sentence case ("6. What empirical risk does and does not reveal" replaces "... Tell Us", which addressed the reader as "us"); "2%", "98%"; "NumPy" in prose (code unchanged); QR and SVD expanded at first use.
- Metadata: description now one sentence of 152 characters.
- References: alphabetical (Bishop, Hastie, James, Shalev-Shwartz, Vapnik); "2nd ed.". All five are standard textbooks with the stated publisher and year; no volume/page data apply.
- Cross-references: heading slugs unchanged by the case change (`#5-worked-example-least-squares-on-synthetic-data`, `#33-empirical-risk` still resolve); the slug of Section 6 changed from `#6-what-empirical-risk-does-and-does-not-tell-us` to `#6-what-empirical-risk-does-and-does-not-reveal`; nothing in `src/` links to it.
- Technical corrections: none needed. Code unchanged; output re-verified.
- Remaining suggestions and why they stay: `acronym-expansion` "QR" at `:237`: QR is the name of the decomposition (the factors Q and R), not an abbreviation with an expansion.
- Flags for independent review: none beyond the standard fact-check of the five textbook entries.
- Vietnamese translation affected: no translation exists (`src/content/blog/vi/learning-from-data.mdx` absent). `publishedAt` is 2026-10-13, so no `updatedAt`.
