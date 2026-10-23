# Live review: Logic and Sequential Control

- URL: https://acrr.asia/blog/logic-and-sequential-control
- Source: `src/content/blog/logic-and-sequential-control.mdx` (Industrial Automation, entry 1 of 5)
- Commit deployed: `1eb85d4` (master after PR #53); the source is unchanged between that commit and the reviewed branch
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 23 desktop-light, 43 mobile-light, 43 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: **high (proposed), safety-relevant guidance.** The page tells readers how to wire stop buttons (normally closed, Section 1.3), which latch to use "for anything that moves" (Section 3.3), how to assign don't-cares so that a sensor failure fails safe (Section 2.5) and how to write interlocks and step time-outs (Section 5.4). It frames this correctly (Section 1.3 says fail-safe wiring is not a safety function and that ordinary control logic must never be the only protection), but a reader could apply it to real machinery. Under standards 3 that makes it high risk, so only San may accept it. If San judges that the disclaimer and the textbook level make it routine, the classification can be changed and the page accepted with follow-up on this report.

## A. Decision

Leave in review for San (high risk). No critical or major finding: the contract is delivered, the technical content was verified, and the two findings (L1, L2) are minor rendering defects at 360 px. Recommendation to San: accept with follow-up.

**Library decision: retain.** The page is the first entry of its series, and entries 2 to 5 reuse its vocabulary, its seal-in circuit, its timers and its mixing-tank state machine (`programmable-logic-controllers` translates the last into Structured Text and Sequential Function Chart). No other ACRR page covers combinational simplification, latches, timers and sequences for control. It is long (24 minutes) but each section is used later in the page or in the series, and the exercises and summary make it reusable.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer with basic electrical knowledge and no background in digital logic or programmable controllers, starting on industrial automation.
- Problem: how the yes-or-no and step-by-step behavior of a machine is specified, simplified and checked before it is programmed on a controller.
- Outcome: write and simplify Boolean control logic with identities and Karnaugh maps; assign don't-cares deliberately; build seal-in circuits and latches and choose set or reset dominance; use edge detection, timers and counters and bound their timing error in a cyclic controller; describe a sequence as a Moore state machine with permissives, interlocks and time-outs.
- Distinctive contribution: digital-logic tools taught through automation cases (level-switch plausibility, a fail-safe refill request, a mixing tank), with the failure-mode reasoning a textbook on digital design omits, and every result checked by a runnable Python program.
- Evidence: two Python programs with their real output (re-run for this review: `True`, and the four transition lines identical); worked Karnaugh maps; Bolton (2015), Cassandras and Lafortune (2008), IEC 60848:2013, IEC 61131-3:2013, Mano and Ciletti (2013), Petruzella (2016).
- Limitations: logic and sequence layer only (feedback control in entry 4); safety functions to machinery-safety standards explicitly out of scope; single-active-state machines only (parallel branches deferred to entry 2).

The contract is delivered. The opening names the two kinds of control question and the prerequisites; Section 1 grounds the vocabulary in plant hardware; Sections 2 to 5 add one capability each (combinational logic, memory, time, sequence); every section has a worked example; the exercises test each capability; the summary table answers the page's questions. Checked by computation for this review: both programs; Exercise 1 ($\overline{B}\,\overline{D} + BD$, exhaustive check over 16 inputs); the timer bounds of Section 4.3 (100 to 110 ms, 120 to 150 ms) and Exercise 4 (60 to 80 ms; 40 to 60 ms for a 40 ms preset); the mixing-tank timings (37.5 s, 39.5 s, 87.0 s seen at 87.5 s, 2-point overshoot); Exercises 2 and 3 by hand. Section 1.2's table and 1.4's series map are the only passages that are not directly used, and both are short orientation. Value category: practical implementation (the reader can specify, simplify and check control logic). Format: explainer.

Overlap noticed:

- `programmable-logic-controllers` (entry 2) reuses the seal-in rung, `stop_ok`, TON and the mixing tank; it extends rather than repeats them and links back. Its Section 2.2 treats scan-cycle response time, which Section 4.3 here introduces and defers to it.
- The Logic series (`what-logic-studies`, `sentential-logic`, `predicate-logic`) treats Boolean connectives as propositional logic for reasoning; this page treats them as switching algebra for circuits. Different readers and purposes, no duplication. For the site-level overlap map: "truth tables and De Morgan's laws" are explained both in `sentential-logic` and here; a cross-link (Phase 7) could help readers who come from either side.

## C. Substantive findings

None. No technical or factual error was found on the page.

## D. Visual and structural findings

### L1. Mixing-tank state diagram: DRAIN state off-screen at 360 px

- Location: Section 5.2, the Mermaid diagram of the four-state sequence (mobile-light-29, mobile-dark-29).
- Problem: at 360 px the left-to-right diagram is wider than the screen; IDLE, FILL and MIX are visible, but the DRAIN state and the label "timer ≥ 30 s" are hidden to the right, with no scroll cue. At 1280 px the diagram is complete and legible (desktop-light-15/16).
- Why it matters: the text says "the sequence has four states"; a phone reader sees three and a return arrow from nowhere.
- Required action: a top-to-bottom layout (`flowchart TB`) for this cycle, or the site-level scroll cue for wide figures recommended in the DFT review (`dft-and-fft` L2).
- Priority: minor
- Acceptance condition: at 360 px all four states and all four transition labels are visible, or a visible cue shows that the figure scrolls.

### L2. Karnaugh maps and the state-output table: columns hidden at 360 px

- Location: Section 2.4, the Karnaugh map of the fault signal (mobile-light-16); Section 2.5, the map with don't-cares (mobile-light-18); Section 5.2, the output table (mobile-light-29). Same in dark mode.
- Problem: the site gives every table cell a minimum width of 7 rem, so these narrow tables (cells holding one digit or letter) become wider than the phone column; only the columns 00 and 01 of each map are visible, and the "Drain valve" column of the output table is hidden. The scroll shadow on the right edge is the only cue.
- Why it matters: the paragraph after each map reads groups in the columns 11 and 10, which the phone reader must scroll to find; the maps are small enough to fit if their cells were allowed to be narrow.
- Required action: site-level, in `prose.css`: let compact tables (for example tables whose cells are short, or a class on these tables) use a smaller cell minimum width so that a 5-column map fits at 360 px. No change to the article text is needed.
- Priority: minor (site styling, not specific to this article)
- Acceptance condition: at 360 px all five columns of both maps and all four columns of the output table are visible without scrolling.

The page uses the right representations: truth tables and Karnaugh maps for combinational logic, a relay rung in text form, comparison tables for latches and timers, a state diagram plus output table for the sequence, and simulation output that the text checks by hand. Dark mode: tables, equations, the ASCII rung, code token colors and the Mermaid diagram are legible (mobile-dark tiles 9 to 12, 17 to 21 and 29 to 32 checked).

## E. Technical and source findings

No technical or source errors found. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll at 360 px, 0 KaTeX errors, no broken images, no console errors, no overflowing elements, capture not truncated. The statement that IEC 61131-3 Ed. 4.0 replaced the third edition in 2025 was verified in the 13 October independent review and was not re-checked here; book editions were not re-verified.

## F. Required changes

Mandatory: none.

Optional:

- [ ] L1: top-to-bottom layout for the Section 5.2 state diagram (or the site-level scroll cue).
- [ ] L2: narrower minimum cell width for compact tables (site-level).
- [ ] Section 2.4, after the map: the quotation "M without L, or H without M, or H without L" opens with a closing quotation mark (”M ...) on the live page (mobile-light-16); write the opening mark explicitly.
- [ ] For San's risk decision: if the page stays high risk, consider a one-line pointer in Section 5.4 back to the Section 1.3 statement that interlocks protecting people belong to safety-rated systems, since the agitator interlock there is a machine-protection example.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
