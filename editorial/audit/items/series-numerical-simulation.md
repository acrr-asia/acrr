<!-- audit: {"slug":"numerical-simulation","type":"series","series":"numerical-simulation","priority":"P2","before":{"purpose":3,"structure":2,"accuracy":4,"evidence":4,"language":2,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":1}} -->
# Audit: Numerical Simulation for Engineers

- Path: `src/content/series/numerical-simulation.md` · Route: `/series/numerical-simulation` · Type: series overview · 5 entries, status published, no planned entries · Words: 134 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: reader and prerequisites are stated, but the page does not say why the entries come in this order.
- structure 2: the body is a single paragraph whose core is one 77-word sentence listing the five topics; it gives no sequence rationale and no shared conventions (standards 6.5), and it does not say how the entries connect.
- accuracy 4.
- evidence 4: the overview makes no claim that needs a source.
- language 2: the 77-word sentence (`eos lint` sentence-length, line 13) is hard to read and lists rather than explains.
- consistency 3: objective 4 bundles two unrelated outcomes; "the control systems series" is named but not linked.
- publishing 2: description of 225 characters (`description-length` warning).

Total 20 of 28.

## Priority

P2: the overview is the series' front door and its description is the card summary on `/series`; the defects are structural and metadata problems a reader notices, not errors.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `numerical-simulation.md:3` | publishing | Description is 225 characters and lists every topic |
| D1 | Should fix | `numerical-simulation.md:13` | structure | No sequence rationale, no shared conventions, no account of how entries connect |
| D2 | Should fix | `numerical-simulation.md:10` | structure | Objective 4 combines two outcomes (FEM; V&V) in one line |
| C1 | Should fix | `numerical-simulation.md:13` | language | 77-word list sentence |
| C2 | Optional | `numerical-simulation.md:13` | consistency | "the control systems series" not linked |

### P1. Description too long
- **Where:** `src/content/series/numerical-simulation.md:3`
- **Text:** "A series on computing what equations predict: discretizing differential equations, finite differences for heat and waves, solving large linear systems, the finite element method, and checking that a simulation can be trusted."
- **Problem:** 225 characters (limit 165, standards 8.1); it lists every entry instead of saying what the reader will learn.
- **Correction:** "A five-entry course on computing what differential equations predict, from discretization and finite differences to linear solvers, finite elements and verification." (165 characters or fewer; checked after revision.)

### D1. Overview lacks the elements of standards Section 6.5
- **Where:** `numerical-simulation.md:13`
- **Text:** "Over five entries it goes from the heat, wave and Poisson equations and their boundary conditions to finite-difference schemes and their stability, from the sparse linear systems ... and finally to verification and validation ..."
- **Problem:** The page names the topics but not why they come in this order (each entry produces the input of the next: discrete equations → time stepping → linear systems → a second route to the same systems → checking the whole chain). It omits the conventions every entry relies on and that entry 1 Section 4.1 and 2.3 fix: $-\nabla^2 u = f$ sign convention, capital $U$ for discrete and lowercase $u$ for exact values, SI units, Python 3 with NumPy in double precision.
- **Correction:** Rewrite as three short paragraphs: reader and prerequisites; sequence rationale with one clause per entry; shared conventions.

### D2. Objective 4 is two outcomes
- **Where:** `numerical-simulation.md:10`
- **Text:** "Explain the finite element method from its variational form, and verify and validate a simulation."
- **Problem:** Standards 6.5 asks for 3-6 checkable outcomes; this line joins the outcome of entry 4 and the outcome of entry 5, and "verify and validate a simulation" is not checkable as written.
- **Correction:** Split into "Derive the finite element method from the weak form of a boundary value problem and explain why its error follows the mesh size and element degree." and "Verify a simulation code and result by measuring the observed order and estimating numerical error, and validate a model against measurements with stated uncertainties."

### C1. 77-word sentence
- **Where:** `numerical-simulation.md:13`
- **Text:** the sentence quoted in D1.
- **Problem:** `eos lint` sentence-length; a list of eight noun phrases in one sentence.
- **Correction:** Resolved by the rewrite in D1.

### C2. Unlinked series reference
- **Where:** `numerical-simulation.md:13`
- **Text:** "the ordinary differential equations met in the control systems series"
- **Problem:** The prerequisite is named but the reader cannot reach it.
- **Correction:** Link `/series/foundations-of-control-systems`.

## Revision log (wave 1)

- Structure: body rewritten as three paragraphs (reader and prerequisites; why the five entries come in this order and what each hands to the next; shared conventions: sign convention, $U$/$u$ notation, SI units, Python 3 with NumPy in double precision, the observed-order experiments).
- Prose: the 77-word sentence removed.
- Metadata: description shortened to one sentence of 165 characters. Objectives: objective 4 split into two (FEM; verification and validation); objective 1 now begins with "Discretize" (an assessable verb); the others reworded only for precision. Title, status, category and the entry list unchanged.
- Cross-references: link to `/series/foundations-of-control-systems` and to the numerical integration notes added; "ODEs" expanded at first use.
- Remaining warnings: none.
- Flags for independent review: series editor to confirm that the new objective 5 ("Verify ... and validate ...") is fully covered by entry 5 (it is, Sections 2-4, in this editor's reading).
- Vietnamese translation affected: yes. `src/content/series/vi/numerical-simulation.md` now differs in meaning: new description, five objectives instead of four (objective 4 split), and a rewritten body with a conventions paragraph. No copied field changed (status, category, example, plannedEntries untouched), so the build is not affected.

## Independent review (wave 2)

- Reviewer: independent reviewer (fact-check, technical, series), 2026-10-14; report `reviews/numerical-simulation.md`.
- Fact-check: pass (no factual claims needing a source; objectives and promises match the entries).
- Technical: pass (shared conventions stated correctly; objective 5 confirmed covered by entry 5 §2-4).
- Findings concerning this item: S1 (series-level notation; correction proposed in entry 3, optionally also a line in the conventions paragraph).
- Not verified: none.
