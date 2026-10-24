# Phase 3, batch 1: the 15 priority pages

Library audit combined with the first live review (adoption plan, Phase 3). Recommendations only: no page was edited, merged or retired.

- Pages: the 15 P1 items of the 13 October audit (`editorial/audit/audit-report.md`).
- Captures: https://acrr.asia at `1eb85d4`, run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC), 1280 px light, 360 px light and dark.
- Reviewers: four independent live-review passes (none wrote or revised these pages), following `plugins/editorial-os/skills/live-review/SKILL.md`. Every number on each page was recomputed or its script re-run; all matched.
- Each page's report is in `editorial/live-reviews/<type>/<slug>.md`; its queue entry has format, value category, risk, a reconstructed contract, the findings and the decision.

## Decisions

| Page | Live-review decision | Library decision | Critical / major / minor |
|---|---|---|---|
| article/token-based-authentication | accepted with follow-up | retain | 0 / 0 / 5 |
| article/feedback-and-system-behavior | accepted with follow-up | retain | 0 / 0 / 4 |
| article/introduction-to-control-systems | accepted with follow-up | retain | 0 / 0 / 3 |
| article/state-space-models-primer | accepted with follow-up | retain | 0 / 0 / 2 |
| article/learning-from-data | revision requested | retain and update | 0 / 1 / 3 |
| article/what-is-a-robot | accepted | retain | 0 / 0 / 0 |
| article/measurement-systems-and-sensor-characteristics | accepted with follow-up | retain | 0 / 0 / 4 |
| article/signals-and-systems-in-discrete-time | revision requested | retain | 0 / 1 / 4 |
| article/inside-a-microcontroller | revision requested | retain | 0 / 1 / 3 |
| article/from-differential-equations-to-discrete-problems | revision requested | retain and update | 0 / 1 / 2 |
| article/logic-and-sequential-control | in review (high risk: San decides) | retain | 0 / 0 / 2 |
| article/numerical-integration-notes | accepted with follow-up | retain | 0 / 0 / 3 |
| series/identity-and-access-control | accepted | retain | 0 / 0 / 0 |
| series/sensor-systems | accepted with follow-up | retain | 0 / 0 / 1 |
| series/industrial-automation | accepted | retain | 0 / 0 / 0 |

No page is recommended for merge, reclassification or retirement.

## For San

1. **logic-and-sequential-control is classed high risk** (it gives safety-relevant guidance: normally closed stop buttons, reset-dominant latches, interlocks, time-outs; it does say that real safety functions belong to safety-rated systems). Only San may accept it. The reviewer recommends acceptance with follow-up; San may instead reclassify it as routine.
2. **token-based-authentication was classed routine.** It is security guidance; if San counts security practice as "safety-relevant guidance", it becomes high risk and needs San's acceptance. Its L4 corrects one claim: a reused refresh token does not always mean an attacker (a legitimate client retrying after a lost response also reuses it, RFC 9700 4.14.2).

## The four major findings

- **inside-a-microcontroller L1:** code ligatures. The code font (JetBrains Mono) draws `|=` as one symbol resembling "⊨", `!=` as "≠", `==` as a long bar and `->` as an arrow, in the very sentence that teaches the bit operators. Nothing in the site styles turns ligatures off, so every page with code is affected.
- **signals-and-systems-in-discrete-time L1, learning-from-data L1, from-differential-equations-to-discrete-problems L1:** central equations cut off at the right edge with no visible scroll cue (at 1280 px for one equation in two of the pages, at 360 px for most central equations). The same defect was fixed in dft-and-fft by breaking the equations over lines.

## Site-level fixes that would close many findings at once

These are styling changes outside any article (no review record goes stale), proposed for Phase 4:

1. `font-variant-ligatures: none` on `.prose code` and `.prose pre` (closes the major finding above and the `>=` minor in signals-and-systems).
2. A visible scroll cue for wide display equations, figures and Mermaid diagrams (as tables already have), or top-to-bottom layouts for wide flowcharts. Cut equations, figures and diagrams at 360 px are the most frequent minor finding (on 11 of the 15 pages).
3. The 7rem minimum table-cell width in `prose.css` makes tables with five or more columns overflow at 1280 px and small tables overflow at 360 px.
4. Non-breaking spaces between numbers and units, and punctuation kept with the inline equation before it.
5. Opening quotation marks rendered as closing marks in two pages (`”+”`).

Equations that stay too wide on a phone after the scroll cue still need to be broken over lines in the article, through the normal review stages.

## Content points (minor)

- learning-from-data L4: says the sample's training error fell "well below" its expected value without saying how unusual that is; a simulation of 20 000 runs puts it at about the 4th percentile.
- measurement-systems-and-sensor-characteristics L4: "transfer function" means the static curve here but links to the control series, where it means G(s); the page never says the two uses differ.
- signals-and-systems-in-discrete-time: Exercise 5 asks "how many samples" and answers with the index n = 59 (the 60th sample).
- foundations-of-control-systems: entry 2 is dated 20 September and entry 1 11 October.

## Overlap noticed (for the site overlap map)

All are linked, complementary treatments; none is duplication:

- First-order time constant: introduction-to-control-systems 3.3 and measurement-systems 4.1.
- "Transfer function" in two meanings across the sensor and control series.
- Eigenvalues and stability: state-space-models-primer, stability-and-eigenvalues, numerical-integration-notes, z-transform-poles-and-stability.
- learning-from-data and the Vietnamese originals `/vi/blog/ml-basic-concepts` and `/vi/blog/ml-linear-regression` (same loss and regression concepts, no links between them).
- inside-a-microcontroller and programmable-logic-controllers (superloop against scan cycle, watchdog).
- logic-and-sequential-control and the Logic series (truth tables, De Morgan's laws, different purpose).
- token-based-authentication summarizes entries 2 to 7 of its own series by design.
