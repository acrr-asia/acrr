# Live review: Interrupts, Polling and DMA

- URL: https://acrr.asia/blog/interrupts-polling-and-dma
- Source: `src/content/blog/interrupts-polling-and-dma.mdx` (Embedded and Real-Time Systems, entry 2)
- Commit deployed: `7e20c2c` (master after PR #57; the article source is unchanged between that commit and the reviewed branch)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 23 desktop-light, 42 mobile-light, 42 mobile-dark tiles (dark tiles checked for the figures, tables and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The article delivers its contract and no technical error was found; the three findings are presentation polish (diagram captions, an inline-code line break that splits the `->` operator, numbers split across lines at 360 px).

**Library decision: retain.** This is the entry of the series that turns "an event happened" into "the data reached the code on time", and it does so with quantities a reader can reuse (polling latency, the worst-case interrupt-latency sum, the $r\,c/f_\text{CPU}$ load model, the DMA block deadline) and a tested lock-free ring buffer. The 13 October audit found only metadata and language defects, all fixed in wave 1; this review found no error and no padding. No other ACRR page covers interrupts, critical sections or DMA, so there is nothing to merge with, and the format (explainer with worked numbers and exercises) fits the content.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a C programmer who has read the first entry (or knows a microcontroller's registers and the superloop) and now needs peripheral data to reach the program without loss.
- Problem: choosing between polling, interrupts and DMA for a given input, and writing interrupt code that neither misses deadlines nor corrupts shared data.
- Outcome: compute polling latency, worst-case interrupt latency and the processor load of interrupt-per-item and DMA handling; follow the ISR rules; recognize race conditions and torn reads; protect shared data with a short critical section or a single-producer, single-consumer ring buffer; set up double buffering and know its deadline and delay; pick a method from the decision table.
- Distinctive contribution: one quantitative thread (the 115 200 bit/s UART and its 86.8 µs deadline, the 10 kHz ADC) carried through all three methods; a C11 ring buffer with correct acquire/release ordering and its real test output; a decision table plus four worked design decisions.
- Evidence: worked arithmetic; the ring-buffer program and the load-comparison script with real output (both reproduced by the 13 October auditor); Arm DDI 0403E.e, ISO/IEC 9899:2011, Ganssle (2008), Lee and Seshia (2017), White (2011), Yiu (2014).
- Limitations: a generic Cortex-M at 48 MHz with invented register names; vendor DMA specifics, multi-core concurrency and operating-system primitives (left to the fourth entry) are out of scope.

The benefit is delivered. The opening names the three methods and the question; Sections 2, 3 and 5 treat one method each with its latency and cost; Section 4 handles the problem interrupts create; Section 6 decides. Spot checks recomputed in this review: 115 200/10 = 11 520 B/s and 1/11 520 = 86.8 µs; 12 cycles at 48 MHz = 0.25 µs; 0.25 + 10 + 5 = 15.25 µs (61 times the entry time, "about sixty"); 11 520 × 100/48 MHz = 2.40%, 100 000 → 20.83%, 480 000 → 100%; the DMA column (1000/256 × 300/48 MHz = 0.0024%, 480 000 → 1.1719%); 256/10 kHz = 25.6 ms and 10 000/256 = 39.1 interrupts/s; Exercise 2 (29.25 µs) and Exercise 4 (10 ms); six bytes at 8 MHz = 6 µs of clocking, "about 7 µs" with select overhead.

Value density: every section serves the central question; nothing is repeated except the summary table, which is a deliberate review sheet. The sequence diagram of Section 3.1 and the numbered list after it say the same thing twice, but the diagram is the quicker read and the list carries the details (registers saved, vector table), so both earn their place. Value category: practical implementation, with conceptual understanding close behind. Format: explainer.

Overlap noticed: none that duplicates. Section 6's push-button example (polling from a timer tick) touches the scan cycle of [Programmable Logic Controllers](/blog/programmable-logic-controllers); the double-buffered ADC of Section 5.2 is the firmware side of what [Sampling, Quantization and Data Conversion](/blog/sampling-quantization-and-data-conversion) treats as signal theory. Cross-links would serve readers (Phase 7 overlap map), but there is no duplicated explanation.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. The two Mermaid diagrams have no caption

- Location: Section 3.1, the sequence diagram (Peripheral, NVIC, CPU; desktop-light-05 and 06, mobile-light-09); Section 5.2, the double-buffering flowchart (desktop-light-15, mobile-light-27). `facts.json` reports two SVG figures without a title on every viewport.
- Problem: neither figure has a caption saying what it shows or what to notice. At 360 px the flowchart's last node ("Software processes full half") is cut at the right edge (known site-level behavior, no scroll cue), so a phone reader sees a diagram that ends in two boxes with arrows to nowhere.
- Why it matters: minor; the surrounding text explains both. A caption would give the phone reader the missing destination in words.
- Required action: add a one-sentence caption to each (for example "Figure 1. Interrupt entry and return on Cortex-M: the NVIC forwards the highest-priority pending request; the core saves context, runs the ISR and restores context." and "Figure 2. Double buffering: the DMA channel fills one half while software processes the other."). A top-to-bottom layout (`flowchart TB`) would also make the flowchart fit at 360 px.
- Priority: minor
- Acceptance condition: `facts.json` of new captures reports 0 SVG figures without a title, and both diagrams have a caption.

### L2. Exercise 3: the inline code breaks inside the `->` operator

- Location: Section 7, Exercise 3, the expression `((uint64_t)ticks_high << 32) | TIMER->COUNT`; desktop-light-20.
- Problem: at 1280 px the inline code wraps at the hyphen, so the reader sees "TIMER-" at the end of one line and ">COUNT" at the start of the next. (At 360 px the break falls before `TIMER->COUNT` and the operator stays whole, mobile-light-36.)
- Why it matters: the exercise asks the reader to diagnose this exact expression; a split operator looks like a subtraction followed by a stray ">".
- Required action: keep this expression from breaking at its hyphen, for example with a word joiner (U+2060) between `-` and `>`, or move the expression into a code block; a site-level rule that stops inline code from breaking after a hyphen would prevent the same defect elsewhere.
- Priority: minor
- Acceptance condition: on new captures at 1280 and 360 px, `TIMER->COUNT` appears on one line.

### L3. Grouped numbers split across lines at 360 px

- Location: Section 3.5, "(11 / 520 bytes/s)" and "for 100 / 000 items per second"; mobile-light-16.
- Problem: the digit-group spaces are ordinary breaking spaces, so a phone reader sees "11" at the end of a line and "520" at the start of the next.
- Why it matters: polish; the split reads as two numbers. The same defect is finding L4 of the live review of [Inside a Microcontroller](/blog/inside-a-microcontroller), where a site-wide fix is proposed.
- Required action: non-breaking (or narrow non-breaking) spaces inside grouped numbers and between numbers and units, preferably by the site-wide remark step proposed there.
- Priority: minor
- Acceptance condition: neither split appears on new captures at 360 px.

Site-level issues already recorded, affecting this page: no scroll cue for the wide double-buffering flowchart at 360 px (see L1); the Section 6 decision table hides its DMA column, and the Section 1.2 table its "Processor involvement" column, behind the table scroll at 360 px (7rem minimum cell width, mobile-light-05, 32 and 33); the output of the load-comparison script shows its DMA column only after sideways scrolling at 360 px (code blocks have no scroll cue, mobile-light-29). At 360 px the sequence diagram of Section 3.1 is scaled down to fit and its labels are small but legible (mobile-light-09). Dark mode: diagrams, tables and code are legible (mobile-dark-09, 27, 29, 32). Code ligatures are gone (`->`, `!=`, `==` render as typed).

## E. Technical and source findings

No technical or source errors found. The numbers checked in B are correct; the C11 ring buffer's memory orders are right for one producer and one consumer (release on the publishing store, acquire on the reading load); the Exercise 3 answer correctly notes that the double-read fix also needs the overflow-flag check. The Arm 12-cycle entry latency was not checked against a fetched source in this review (the 13 October audit records the same limitation); it agrees with the Cortex-M3/M4 documentation as the reviewer knows it. `facts.json`: HTTP 200 on all three viewports, one h1, no horizontal page scroll, no overflowing element, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: captions for the two diagrams; top-to-bottom layout for the flowchart.
- [ ] L2: keep `TIMER->COUNT` on one line.
- [ ] L3: non-breaking spaces in grouped numbers (site-wide).
- [ ] Cross-links to Programmable Logic Controllers (scan cycle) and Sampling, Quantization and Data Conversion (Phase 7 overlap map).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
