# Live review: Real-Time Operating Systems and Scheduling

- URL: https://acrr.asia/blog/real-time-operating-systems-and-scheduling
- Source: `src/content/blog/real-time-operating-systems-and-scheduling.mdx` (Embedded and Real-Time Systems, entry 4)
- Commit deployed: `7e20c2c` (master after PR #57; the article source is unchanged between that commit and the reviewed branch)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 24 desktop-light, 42 mobile-light, 42 mobile-dark tiles (dark tiles checked for the figure, tables and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, safety guidance or commercial relationship). The one statement about a named organization, the Mars Pathfinder resets in Section 3.3, is a historical technical account attributed to the engineer's own published description (G. E. Reeves, JPL, 1997) and cited; it makes no claim about anyone's conduct, so it does not make the page high-risk in the sense of standards 3.

## A. Decision

Accept with minor follow-up. The article delivers its contract, every program reproduces its printed output, and no technical error was found. The two findings are presentation polish: the task-state diagram has no caption and is cut at 360 px, and five possessives after inline math show an opening quotation mark instead of an apostrophe.

**Library decision: retain.** The entry is the analytical center of the series: it turns the timing vocabulary of entry 1 and the interrupt costs of entry 2 into a schedulability test (utilization bound, response-time analysis, blocking), checks the analysis against a simulation, and ends with a worked design that includes the UART ISR of entry 2. No other ACRR page teaches RTOS scheduling or priority inversion, so there is nothing to merge with. The 13 October audit found metadata, sentence-length and reference-format defects only; all were fixed, and the Mars Pathfinder statement was given its source in wave 2.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a firmware developer who has outgrown the superloop (entries 1 and 2 of the series) and must decide whether a set of periodic jobs will meet its deadlines under an RTOS.
- Problem: structuring firmware as prioritized tasks and proving, before the system is built, that every task meets its deadline in the worst case, including the effect of shared resources and interrupts.
- Outcome: explain task states, context switches and periodic release with "delay until"; assign rate- or deadline-monotonic priorities; apply the Liu and Layland bound and know when it is inconclusive; compute response times by iteration, with blocking; recognize priority inversion and bound it with inheritance or ceilings; fold ISR load into the analysis.
- Distinctive contribution: one running three-task example carried from the utilization bound through response-time analysis, a schedule simulation that confirms the computed response time, a fixed-priority versus EDF counterexample, and a worked design that ties the ISR cost of entry 2 into the analysis with exact fractions.
- Evidence: three Python programs with real output (re-run in this review: identical output); Liu and Layland (1973), Leung and Whitehead (1982), Joseph and Pandya (1986), Audsley et al. (1993), Sha et al. (1990), Davis et al. (2007), Burns and Wellings (2009), Buttazzo (2011), IEEE Std 1003.1-2017, Reeves (1997).
- Limitations: single-core, fixed-priority, deadlines no longer than periods, no self-suspension; kernel overheads only by folding them into $C_i$; no particular kernel's API.

The benefit is delivered. The opening states the central question ("will every task meet its deadline in the worst case?"), Section 1 gives the kernel model the analysis needs, Section 2 answers the question for independent tasks, Section 3 adds shared resources, and Section 4 shows the whole check on one design and says honestly what it cannot establish (the inputs). Checks in this review: the three programs re-run (identical output); the τ3 iteration 3 → 6 → 7 → 9 → 10; the bounds 0.828, 0.780 and ln 2; Set C (U = 0.971, RM τ2 4 → 6 → 8 > 7); the simulation timeline ("1223132213..": τ3 in slots 3, 5 and 9, complete at 10 ms); Exercises 2, 3 and 5 by hand (R3 = 10; B2 = 1 and R2 = 4; RM R_a = 4 > 3, DM R_a = 2 and R_b = 4).

Value density: no section is padding. The summary table is a review sheet. The simulation output is a string of digits that the reader must decode slot by slot; a small schedule (Gantt) figure for set A would show the critical instant and the 10 ms response time at a glance (optional, F). Value category: conceptual understanding (scheduling theory), with practical implementation close behind (the RTA procedure and design check). Format: explainer.

Overlap noticed: the CAN response-time remark in Section 2.4 (Davis et al. 2007) is also the basis of the CAN timing analysis in [Fieldbuses and Industrial Ethernet](/blog/fieldbuses-and-industrial-ethernet), which cites the same paper; that is a shared source rather than duplicated teaching, and a cross-link from either page would help (Phase 7 overlap map). No other page covers RTOS scheduling.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Task-state diagram: no caption, and the "Blocked" state is cut at 360 px

- Location: Section 1.2, the Mermaid flowchart of Ready, Running and Blocked (desktop-light-03; mobile-light-06, mobile-dark-06). `facts.json` reports one SVG figure without a title on every viewport.
- Problem: at 360 px the diagram keeps its minimum width and the "Blocked" box and the end of the "waits for event, time or resource" label are cut at the right edge, with no scroll cue (known site-level behavior). The figure has no caption.
- Why it matters: minor; the bullet list below names all three states. But the state that distinguishes an RTOS from busy-waiting is the one a phone reader does not see.
- Required action: add a caption (for example "Figure 1. Task states: the scheduler moves a task between Ready and Running; a task that waits is Blocked and uses no processor time.") and, if the site-level scroll cue is not added, lay the diagram out top to bottom so it fits at 360 px.
- Priority: minor
- Acceptance condition: `facts.json` of new captures reports 0 SVG figures without a title, and at 360 px the "Blocked" box is visible or a visible cue shows that the figure scrolls.

### L2. Opening quotation mark instead of an apostrophe after a task symbol

- Location: Section 2.5 ("$\tau_2$‘s first job", desktop-light-13); Section 3.4, the priority-inheritance bullet ("$\tau_1$‘s priority", "$\tau_3$‘s critical section") and the paragraph after the list ("$\tau_3$‘s critical section", "$\tau_1$‘s priority"), desktop-light-16; mobile-light-23, 28, 29 and 30.
- Problem: the possessive after inline math is rendered as a left single quotation mark (‘), so the text reads "τ1‘s".
- Why it matters: polish; the mark is the wrong glyph in five places in the section that explains the protocols. The same defect is finding L2 of the live review of [Coordinate Frames and Transformations](/blog/coordinate-frames-and-transformations).
- Required action: write the apostrophe as ’ after the math in these five places (or rephrase, "the priority of $\tau_1$"); a site-level fix in the typographic-quote step would cover every page.
- Priority: minor
- Acceptance condition: the five possessives show an apostrophe (’) on new captures.

Site-level issues already recorded, affecting this page: no scroll cue for the wide state diagram at 360 px (L1); the 7rem minimum cell width hides the last columns of the running-example table and of the iteration table of Section 2.4 behind the table scroll at 360 px (mobile-light-13 to 18; the "New R" column of each row reappears as "R" in the next row, so the iteration can still be followed). Dark mode: the diagram, tables and code are legible (mobile-dark-06, 15, 18, 22). Code ligatures are gone.

## E. Technical and source findings

No technical or source errors found. All three programs were re-run in this review (Python 3, standard library) and print exactly the output shown. The statements of the classical results (RM and DM optimality, the Liu and Layland bound, the EDF condition, the ceiling-protocol blocking bound including intermediate-priority tasks) are correctly qualified. The Mars Pathfinder account is attributed to Reeves and cited; the source was re-fetched by the author on 2026-10-15 (audit log) and was not re-fetched in this review. `facts.json`: HTTP 200 on all three viewports, one h1, no horizontal page scroll, no overflowing element, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: caption for the task-state diagram; top-to-bottom layout or site-level scroll cue.
- [ ] L2: apostrophes after inline math (five places).
- [ ] A small schedule figure for set A (tasks on the vertical axis, 0 to 12 ms on the horizontal) beside or instead of the digit timeline of Section 2.4, generated from the simulation so that it stays true to it.
- [ ] Cross-link Section 2.4's CAN remark with the CAN timing analysis in Fieldbuses and Industrial Ethernet (Phase 7 overlap map).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
