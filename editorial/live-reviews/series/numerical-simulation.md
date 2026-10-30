# Live review: Numerical Simulation for Engineers (series overview)

- URL: https://acrr.asia/series/numerical-simulation
- Source: `src/content/series/numerical-simulation.md` (five entries, status published, no planned entries)
- Commit deployed: `7e20c2c`; the source is unchanged between that commit and the reviewed branch
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 3 desktop-light, 6 mobile-light, 6 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-25. The reviewer did not write or revise this page.
- Risk: routine (a series front door for technical explainers; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept. The overview meets standards 6.5. Every promise on it was checked against the entries and is kept, and no finding was raised on this page. The open revision requests are on the entry pages (entries 2 to 5, presentational: cut displays), not on the overview.

**Library decision: retain.** The page is the series' entry point. The 13 October revision replaced a single list paragraph with three paragraphs: reader and prerequisites, why the five entries come in this order, and shared conventions. Nothing on it should be merged elsewhere or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who uses simulation results, knows calculus, basic linear algebra and the ODEs of Foundations of Control Systems, and is deciding whether and where to start.
- Problem: knowing what the five entries cover, why they come in this order and which conventions they share.
- Outcome: the reader can follow the chain the series uses as its spine (equations, then discrete problem, then time stepping, then linear solve, then a second route by finite elements, then trust in the result). They also know the sign convention, the U/u notation, SI units and the code environment, and have five checkable objectives, one per entry.
- Distinctive contribution: each entry supplies what the next needs, and the overview says so in one clause per entry.
- Evidence (the entries, checked in this review and in the live reviews of entries 2 to 5):
  - −∇²u = f, and its one-dimensional form −(ku′)′ = f, is the convention in entries 1, 3, 4 and 5; the positive-definite matrices are derived in entries 3 and 4.
  - Capital U is used for discrete approximations throughout.
  - Every script is Python 3 with NumPy in double precision. Entry 3's float32 exercise is the deliberate exception.
  - Each entry shows its printed output.
  - Entry 4 builds the same SPD system from the weak form.
  - Entry 5 verifies the code and the solution and validates against measurements.
- Limitations: an overview; total reading time (about 120 minutes from the card estimates of 25, 23, 24, 24 and 24) is not stated.

The page delivers what it promises.
- The opening screen gives the title, a one-sentence description (165 characters), the category, the Published status and "Start with entry 1".
- The three paragraphs each add something the entry list does not.
- The five objectives begin with assessable verbs (discretize, analyze, choose, derive, verify) and map one to one onto the entries.
- The five entry cards each show a one-sentence description of what the reader learns ("How ..."). This avoids the fragment problem noted on other series overviews.

Value category: reference value. Format: reference.

Overlap: none on the overview itself. Overlaps at entry level are recorded in the entry reviews and belong in the Phase 3 overlap map:
- entry 2 with `numerical-integration-notes` (time stepping), which the overview links as background;
- entry 3 with `distributed-memory-and-message-passing` and `gradient-descent-and-its-variants`;
- entry 5 with the insights `what-makes-a-simulation-trustworthy` and `floating-point-in-long-simulations`, and with `measurement-systems-and-sensor-characteristics` (GUM).

## C. Substantive findings

None.

## D. Visual and structural findings

None.

Layout:
- At 1280 px, the entry timeline and the objectives sit side by side (desktop-light-01 to 03).
- At 360 px, objectives and progress come first, then the entry timeline (mobile-light-01 to 06).
- The inline math −∇²u = f is legible in light and dark mode (mobile-dark-03).

`facts.json`:
- HTTP 200 on all three viewports.
- No horizontal scroll.
- No overflowing element.
- No console error.
- No KaTeX error.
- No figures, tables or code.

## E. Technical and source findings

None. The statements about sequence and conventions were checked against the entries (see B).

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] The total reading time (about two hours) could be stated.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| (none) | | | |
