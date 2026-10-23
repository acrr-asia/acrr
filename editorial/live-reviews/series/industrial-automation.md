# Live review: Industrial Automation (series overview)

- URL: https://acrr.asia/series/industrial-automation
- Source: `src/content/series/industrial-automation.md` (series overview, 5 entries, status published)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 3 desktop-light, 6 mobile-light, 6 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this page.
- Risk: routine (a series overview; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept. No finding of any priority. The page does what a series front door should, and every promise it makes was checked against the five entries.

**Library decision: retain.** The overview is the only entry point that explains why the five industrial-automation entries come in this order, and the 13 October audit's findings (no objective for entry 5, a one-sentence body, missing conventions, an over-long description) are all resolved on the live page. Nothing to merge, reclassify or retire.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: someone with basic electrical engineering (voltage, current, switches, relays) and no digital-logic or PLC background, deciding whether and where to start the series.
- Problem: knowing what the series covers, in what order, what it assumes, and what they will be able to do at the end.
- Outcome: choose a starting point; know the prerequisites (and that the PID entry uses the Foundations of Control Systems series); know the five objectives and the shared conventions.
- Distinctive contribution: the dependency chain of the five entries (logic, the PLC that executes it, the networks that extend its I/O, feedback loops closed through that I/O, the layers above and digital twins), stated in one paragraph, with one checkable objective per entry.
- Evidence: none needed beyond the entries; each claim about an entry was checked against its source.
- Limitations: an orientation page; it teaches nothing itself.

The benefit is delivered. On the opening screen the reader sees the title, a one-sentence description, the status and a "Start with entry 1" button; the three paragraphs then answer who the series is for, why the entries come in this order and which conventions they share; the five objectives map one to one onto the five entries; the entry cards give date, reading time and a one-line description each. Checks made against the entries: the second entry does state that the examples follow IEC 61131-3:2013 and that the published scope of the 2025 edition no longer lists Instruction List (its introduction and Section 5.4); percent of span is used in the fourth entry; every entry has Python blocks and the only imports in the five are `math`, `random` and `itertools`, all standard library; the fifth entry's digital-twin example detects an unmeasured leak from residuals, which supports both "estimate what no instrument measures" and the fifth objective. The Vietnamese overview carries the five objectives.

Value density: about 300 words of body; nothing repeated except what the entry cards necessarily restate. Value category: reference value (orientation). Format: reference.

Overlap noticed: none for the overview itself. Within the series, the PLC scan cycle and watchdog have a counterpart in the superloop and watchdog of [Inside a Microcontroller](/blog/inside-a-microcontroller) (Embedded and Real-Time Systems), and the feedback ideas the PID entry builds on come from the [Foundations of Control Systems](/series/foundations-of-control-systems) series, which the overview already links as a prerequisite (that series does not itself treat PID, so there is no duplication); cross-links between the embedded and industrial series belong in the Phase 7 overlap map.

## C. Substantive findings

None.

## D. Visual and structural findings

None. At 1280 px the entries timeline and the objectives and progress sidebar sit side by side; at 360 px the sidebar moves above the entries (objectives, then "5 of 5 entries published", then the numbered entry cards), which reads well. Dark mode is correct (button, badge, timeline and progress bar in the dark tokens). `facts.json`: HTTP 200 on all three viewports, one h1, no horizontal scroll at 360 px, no overflowing elements, no console errors.

## E. Technical and source findings

None. The overview makes no technical claim that is not delivered by an entry (checked as listed in B).

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] When the Phase 7 overlap map is made, link the PLC entry and Inside a Microcontroller (scan cycle and superloop, watchdogs) in both directions.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| (none) | | | |
