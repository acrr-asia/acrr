# Live review: Programmable Logic Controllers

- URL: https://acrr.asia/blog/programmable-logic-controllers
- Source: `src/content/blog/programmable-logic-controllers.mdx` (Industrial Automation, entry 2 of 5)
- Commit deployed: `7e20c2c`
- Captures: `live-captures` branch, run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 26 desktop-light, 48 mobile-light, 48 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-25. The reviewer did not write or revise this article.
- Risk: **high (proposed), safety-relevant guidance.** Section 6 tells readers how to write programs that run machinery: which variables to retain through a power failure ("a 'motor running' latch should not be, or a machine could restart by itself when power returns"), how outputs should behave when the CPU stops ("a cooling-water valve may need to stay open"), and that emergency stops belong to safety-rated hardware. Section 2.3 (watchdog) and Section 3.3 (checking a 4–20 mA signal before using it in a control loop) are of the same kind. The guidance is correct and properly framed (safety functions are sent to IEC 61508, IEC 62061 and ISO 13849-1, not to program logic), but a reader could apply it to real equipment. This matches the classification proposed for entry 1 (`logic-and-sequential-control`). Under standards 3 only San may accept it. If San judges the textbook level and the explicit separation of safety functions make it routine, the page can be accepted with follow-up on this report.

## A. Decision

Leave in review for San (high risk). No critical or major finding: the reader-value contract is delivered, the technical content was checked, and the four findings are minor. Recommendation to San: accept with follow-up.

**Library decision: retain.** The page is the series' bridge from logic (entry 1) to networks (entry 3) and PID (entry 4), and no other ACRR page covers the scan cycle, PLC I/O, 4–20 mA scaling with NE 43 diagnostics or the IEC 61131-3 software model. Its examples reuse entry 1's seal-in circuit and mixing tank, so the series reads as one argument; each section is used later in the page or in the series. Nothing in it is better served by another ACRR page, and it should not be merged.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineering student or engineer who knows Boolean logic, latches, timers and state machines (entry 1) and has not programmed a PLC.
- Problem: how control logic actually runs on industrial hardware, when it sees its inputs and changes its outputs, how field signals reach it, and how it is programmed in the standard languages.
- Outcome: compute best- and worst-case response time from input filter, scan time and output delay; explain why a waiting loop freezes a PLC; scale a 4–20 mA input and classify it by NE 43 levels; distinguish functions, function blocks and programs; read the same task in LD, FBD, ST and IL; name the rules that make a program safe to run.
- Distinctive contribution: one path from hardware and the scan cycle to the five IEC 61131-3 languages, using entry 1's examples, with the timing and scaling claims checked by runnable Python and the IEC 61131-3:2025 change stated.
- Evidence: two Python programs with their real output; worked exercises; IEC 61131-2:2017, IEC 61131-3:2013, IEC 61508, NAMUR NE 43 (2021), Bolton (2015), John and Tiegelkamp (2010), Petruzella (2016).
- Limitations: vendor-specific details (count ranges, addressing, task scheduling, fault behavior of outputs) labeled and not resolved; safety functions out of scope; the fourth edition of IEC 61131-3 noted but not followed.

The benefit is delivered. The opening states what the entry covers and which edition it follows. The scan-cycle section turns "the program runs in a loop" into a usable response-time bound, verified by simulation; the I/O section explains why 4–20 mA is used and what a program must do with a bad signal; the software model and language sections show one task in four languages, which is the clearest way to compare them. Exercises and the summary table make it reusable. Spot-checked: the response-time simulation (13.5, 23.5 and 18.5 ms follow from the stated values), scaling (12.8 mA, 5.5 bar, 15 206.4 counts), Exercise 2 (16.80 mA, 3.20 m, 1.69 mA for −4 000 counts), Exercise 4 (statement-order trace: with the published order the motor goes off one scan after the timer expires; with timer, latch, motor it goes off in the same scan), Exercise 5 (321 Ω). Value category: practical implementation (the reader can analyze timing, scale signals and read programs), with conceptual understanding close behind. Format: explainer. The page is worth its 25-minute reading effort; no section is padding.

Overlap: by design with `logic-and-sequential-control` (seal-in, timers, mixing tank, SFC mentioned there and defined here); light overlap with `sampling-quantization-and-data-conversion` (linked for quantization) and `inside-a-microcontroller` (a watchdog in another context). No duplication that calls for a merge.

## C. Substantive findings

### L1. Section 5 promises each language on the same task, but SFC is not shown

- Location: Section 5 introduction ("The same small task shows each one") and Section 5.5, Sequential Function Chart (desktop-light-19 and 20, mobile-light-35 and 36).
- Problem: LD, FBD, ST and IL each show the conveyor task; SFC, the only language whose value is its picture, gets a definition, a qualifier table and a link to entry 1's state diagram, but no chart. The FBD diagram also shows only the motor rung, not the jam timer.
- Why it matters: a reader cannot see what steps, transitions, the double-bordered initial step or a qualifier look like, which is exactly what the section describes in words; the introduction's promise is not kept for one of the five languages.
- Required action: add a small SFC drawing of the mixing tank (four steps, four transitions with their conditions, N actions), for example as a generated diagram component; or, if no drawing is added, reword the Section 5 introduction so that it does not claim every language is shown on the task.
- Priority: minor
- Acceptance condition: on the live page Section 5.5 shows an SFC chart of the mixing tank, or the introduction no longer says that the same task shows each language.

### L2. Safety standards cited in Section 6 are missing from the references

- Location: Section 6, last bullet ("IEC 61508 and its machinery counterparts IEC 62061 and ISO 13849-1"); References (desktop-light-22 and 24).
- Problem: IEC 62061 and ISO 13849-1 are named as the standards that govern safety functions but are not in the reference list; only IEC 61508 is.
- Why it matters: on a page classed high risk because of safety-relevant guidance, the standards the reader is sent to for the safety part are the ones that should be easiest to find.
- Required action: add IEC 62061 and ISO 13849-1 to the references in house style (undated series form is acceptable, as for IEC 61508).
- Priority: minor
- Acceptance condition: both standards appear in the reference list on the live page.

## D. Visual and structural findings

### L3. Two display equations cut at 360 px

- Location: Section 2.2, the response-time bound (mobile-light-09), and Section 3.4, the scaling equations (mobile-light-20; mobile-dark-20 the same).
- Problem: at 360 px the upper bound ends at "t_in + 2T_s…", and of the two scaling equations only the first (counts to milliamperes) is visible; the second, x = x_lo + (I − 4)/16 · (x_hi − x_lo), is entirely to the right of the screen. Both scroll inside their box with no cue (site-level behavior already recorded).
- Why it matters: the scaling formula is the result Section 3.4 exists to give, and a phone reader sees only half of it. It is recoverable from the worked numbers and the summary, so the finding is minor.
- Required action: put the two scaling equations on separate lines (an `aligned` or `gathered` block) and break the response-time bound after the middle term.
- Priority: minor
- Acceptance condition: at 360 px both scaling equations and both bounds of the response-time inequality are fully visible.

### L4. Diagrams without captions or accessible names

- Location: Section 2.1, scan-cycle flowchart; Section 5.2, FBD diagram (`facts.json`: 2 SVG figures without title on every viewport).
- Problem: neither diagram has a caption or an accessible title; at 1280 px their labels are noticeably smaller than the text.
- Why it matters: standards 6.8 asks captions to say what to notice (that the images are frozen during execution; that the network is the motor rung only); screen-reader users get nothing.
- Required action: add `accTitle`/`accDescr` and a one-sentence caption to each.
- Priority: minor
- Acceptance condition: both diagrams carry a visible caption, and `facts.json` reports 0 SVG figures without title.

Site-level behavior also seen here (already recorded, not raised again): the scan-cycle flowchart is cut after "Write outp…" at 360 px, with no scroll cue (mobile-light-07, mobile-dark-07); the output-type, POU and function-block tables scroll at 360 px under the 7rem cell minimum; code comments are cut at the right edge of the boxes. Dark mode: ladder ASCII art, code, diagrams and equations are legible (mobile-dark-07, 20, 29, 31). The ladder diagram keeps its alignment on both widths.

## E. Technical and source findings

No technical or source errors found. Both Python programs were re-run in the 13 October audit with identical output and their figures follow from the stated values; the exercise arithmetic was recomputed for this review. The IEC 61131-3:2025 statement is qualified to its published scope, as resolved in wave 2. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none (no critical or major finding).

Optional (follow-up):

- [ ] L1: SFC chart of the mixing tank in Section 5.5, or a corrected Section 5 introduction.
- [ ] L2: add IEC 62061 and ISO 13849-1 to the references.
- [ ] L3: split the Section 3.4 scaling equations and the Section 2.2 bound for narrow screens.
- [ ] L4: captions and accessible titles for the two diagrams.
- [ ] For San's risk decision: Section 6's "Keep safety functions separate" is the last bullet; moving it first would put the boundary before the advice that depends on it.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
