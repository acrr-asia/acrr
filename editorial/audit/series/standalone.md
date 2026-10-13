# Scope audit: insights, standalone article and Learning entries

- Scope: six insights (`src/content/insights/*.md`), one standalone article (`src/content/blog/numerical-integration-notes.mdx`), and the English fields of `src/data/learning.json`.
- Audited at commit `e21dcc8`, 2026-10-13. Item audits: `editorial/audit/items/<slug>.md` and `editorial/audit/items/learning.md`.

## Structural consistency across the insights

| Insight | Framing paragraph | Three sections in order | Links to in-depth articles | Description a sentence, 70–165 chars |
|---|---|---|---|---|
| closing-the-sim-to-real-gap | no | yes | none | no (184, noun phrase) |
| compute-bound-or-memory-bound | no | yes | none | no (177, noun phrase) |
| control-vs-learning-approaches | no | yes | none | no (noun phrase) |
| floating-point-in-long-simulations | no | yes | none | no (noun phrase) |
| what-makes-a-simulation-trustworthy | no | yes | none | no (103, noun phrase) |
| when-a-kalman-filter-is-enough | no | yes | none | no (noun phrase) |

Systemic problems, all six:

1. **No framing paragraph** (standards 6.4; the item fails critical condition C7 until fixed). Every insight opens with `## Established`.
2. **No links to in-depth articles** (standards 6.4, 8.2), although the site now has nine complete series that treat most of these subjects. Links are one-directional: the Numerical Simulation series links the floating-point insight twice, and nothing links back.
3. **Descriptions are noun phrases** beginning "A short ...", not sentences; three exceed 165 characters. They also repeat the content type ("A short research question", "A short concept explanation"), which the card already shows as the `kind` badge.
4. Attribution: two named results are stated without a source (the roofline model; the recursive-summation error bound). Insights have no References section by design (exactly three sections), so attribution is inline.

Strengths kept: the Established / Interpretation / Open questions separation is already well observed; interpretations are labeled ("One reading is ..."), open questions are real questions, and every number recomputed correctly (see the item audits).

## Notation and terminology

- Unit roundoff: the insight writes $u$; the series writes $u_r$ and explains why (`from-differential-equations-to-discrete-problems` line 217 says "written $u$ in the floating-point note"). Consistent as documented; no change.
- "Runge–Kutta": en dash in `what-makes-a-simulation-trustworthy`, hyphen in `numerical-integration-notes` (twice) and `stability-and-eigenvalues` (once, outside scope). House practice for two-person names is the en dash (Gauss–Seidel, Crank–Nicolson). Fixed in scope; the out-of-scope occurrence is reported to the orchestrator.
- "unmodelled" (British) in the Kalman insight; house spelling is American.
- Sim-to-real gap is defined in two insights (`closing-the-sim-to-real-gap`, `control-vs-learning-approaches`); the second should link to the first.

## Overlap and gaps

- `what-makes-a-simulation-trustworthy` is a short form of `verifying-and-validating-a-simulation` (the fifth Numerical Simulation entry) plus the order test of `numerical-integration-notes`. Overlap is appropriate for an insight (judgment plus pointers), provided it links them.
- `when-a-kalman-filter-is-enough` overlaps `sensing-and-state-estimation` Sections 5–6 (including a "Choosing" table). The guide should agree with that table on where the UKF sits.
- `compute-bound-or-memory-bound` has no in-depth counterpart on the site (no article on processor performance or memory hierarchies). Gap noted for the Editorial Director; the insight links the nearest material honestly (the flop counts of `solving-large-linear-systems` Section 7) and does not imply more.
- `closing-the-sim-to-real-gap` and `control-vs-learning-approaches` have no in-depth robot-learning article on the site; the nearest material is validation (Numerical Simulation entry 5), state feedback and LQR (Foundations of Control Systems entry 5) and the Machine Learning Fundamentals series.
- **Standalone article vs the Numerical Simulation series.** The brief suspected duplication with `from-differential-equations-to-discrete-problems`. There is none: the series treats PDEs and defers ODE time stepping, explicit Euler's stability limit and the stability regions to these notes (series entry 1 lines 19, 352; entry 2 lines 58, 258), and six entries across four series link the notes. Decision: keep the note standalone and bring it up to the standalone standard (opening, defined concepts and derived orders, limits, summary, references), pointing to the series for stiffness and implicit schemes rather than duplicating them.

## Series-overview standard (6.5)

Not applicable: the scope has no series overview.

## Cross-references

- Inbound links to the notes have no fragments, so renumbering its sections breaks nothing. Inbound links rely on content that must stay: the factor $1 + h\lambda$, the condition $|1 + h\lambda| \le 1$, the fast-decaying example, the stability-region figure.
- Inbound links to the insights: `/insights/floating-point-in-long-simulations` from two series entries, no fragment.
- Learning entries name the Foundations of Control Systems and Machine Learning Fundamentals series correctly; none claims a resource exists; no URL anywhere.

## Revision summary (wave 1)

- All six insights now have a framing paragraph, links to the in-depth articles (or, for the roofline insight, the nearest material), one-sentence descriptions of 138–163 characters, and inline attribution for the two named results. Front-matter copied fields unchanged; no `updatedAt` on insights.
- `numerical-integration-notes` brought to the standalone standard (opening, Sections 1–6 with derivation of order, limits, summary, three verified references); `updatedAt: "2026-10-13"` in English and Vietnamese.
- Learning: two English descriptions revised; `vi` fields need the same change (not edited).
- Out of scope, for the orchestrator: `stability-and-eigenvalues.mdx` line 65 "Runge-Kutta" (hyphen) vs the en dash used elsewhere.
