# Live review: Embedded and Real-Time Systems (series overview)

- URL: https://acrr.asia/series/embedded-and-real-time-systems
- Source: `src/content/series/embedded-and-real-time-systems.md` (five entries, status published, no planned entries)
- Commit deployed: `7e20c2c` (master after PR #57; the series file is unchanged between that commit and the reviewed branch)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 3 desktop-light, 6 mobile-light, 6 mobile-dark tiles (the page has no figure, table, code or equation, so no dark tile needed checking for one)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this page.
- Risk: routine (a series front door for technical explainers; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The overview meets standards 6.5 (reader and prerequisites, scope, sequence with what each entry adds, shared conventions, assessable objectives), and every statement on it was checked against the entries. One minor finding (L1): four of the five entry cards show a description that is a "How ..." fragment, not a sentence, unlike the first entry's card.

**Library decision: retain.** The page is the series' entry point. The 13 October revision and the wave-2 resolution replaced a single list paragraph with a sequence in which each entry removes a limit of the one before (superloop, then interrupts and DMA, then buses, then tasks under an RTOS, then measurement), added the scope sentence and corrected objective 4 so that it no longer promises verification by measurement alone. Nothing here should be merged or reclassified.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a C programmer with basic digital logic and no embedded experience, deciding whether and where to start the series.
- Problem: knowing what the five entries cover, why they come in this order, what is out of scope and which conventions they share.
- Outcome: the reader knows the prerequisites, sees the order as one path (data through the system, then the question of time), knows that single-core microcontrollers are the scope and that multicore scheduling, embedded Linux, kernel APIs, circuit design and safety certification are not, knows the code, platform and unit conventions, and has four assessable objectives.
- Distinctive contribution: the sequence is explained as a chain of limits removed, which tells the reader why the RTOS comes after the buses and why measurement comes last.
- Evidence: the entries. Checked in this review: entry 1 defines events, deadlines, latency and jitter and ends with the superloop; entry 2 analyzes the superloop's polling, then interrupts and DMA with their latency and processor cost, and closes by handing the single-loop limit to the fourth entry (its final paragraph, mobile capture of the interrupts page); entry 3 covers UART, SPI, I2C and CAN; entry 4 calculates worst-case response times; entry 5 measures execution time, latency, jitter, load and memory and feeds them back into the response-time analysis. The conventions (C11, generic Cortex-M at 48 MHz, invented register layouts, POSIX for the desktop experiment, Python 3 with the standard library, SI and binary prefixes) match the entries' own convention paragraphs.
- Limitations: an overview; the total reading time (about 132 minutes from the card estimates) is not stated.

The benefit is delivered. The opening screen gives the title, the one-sentence description, the category, the Published status and "Start with entry 1" (desktop-light-01, mobile-light-01). The objectives begin with assessable verbs (describe, choose, compare, explain and calculate), and the reworded objective 4 now matches entries 4 and 5. Value category: reference value. Format: reference.

Overlap: entry 3's CAN material and the CAN response-time remark in entry 4 overlap with [Fieldbuses and Industrial Ethernet](/blog/fieldbuses-and-industrial-ethernet) in the Industrial Automation series; that is recorded as finding L4 of the live review of [Serial Buses: UART, SPI, I2C and CAN](/blog/serial-buses-uart-spi-i2c-and-can) and belongs in the Phase 7 overlap map. The overview itself names no neighboring series; a pointer would be a nicety, not a requirement.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Entry cards 2 to 5: descriptions are "How ..." fragments

- Location: the Entries list, cards 2 to 5 (desktop-light-02 and 03; mobile-light-05 and 06).
- Problem: the card summaries come from the entries' `description` fields. Card 1 is a sentence ("Learn the timing vocabulary of real-time systems, ..."); cards 2 to 5 are noun clauses without a main verb: "How polling, interrupts and DMA move data from peripherals to memory, ...", "How UART, SPI, I2C and CAN frame, clock, address and check data, ...", "How a real-time operating system schedules prioritized tasks, ...", "How to measure execution time, latency, jitter, ...". Card 2 also ends with "ISR", which a reader arriving at the series front door has not yet seen expanded. Standards 8.1 asks for one complete sentence that says what the reader will learn.
- Why it matters: minor; the cards are specific and informative, but they are not sentences, they differ in form from card 1 on the same page, and the same text is each entry's meta description and RSS summary. The same finding was recorded for the Sensor Systems overview (its L1).
- Required action: rewrite the four descriptions as sentences of 70 to 165 characters (for example "Learn how polling, interrupts and DMA move data from peripherals to memory, what each costs, and how to share data safely with an interrupt handler."), through the normal review stages of each entry (the change stales their review records), and update the Vietnamese descriptions in the same commit.
- Priority: minor
- Acceptance condition: on new captures every entry card of this page shows a one-sentence description, and card 2 uses no unexpanded abbreviation other than DMA, which the overview expands.

Layout: at 1280 px the entries and the objectives sit side by side; at 360 px the body, objectives and progress come first, then the entry timeline; titles wrap cleanly and nothing is cut (mobile-light-01 to 06). Dark mode legible (mobile-dark-01 to 06, checked as a set only, since the page has no figure, table or code). `facts.json`: HTTP 200 on all three viewports, one h1, no horizontal scroll, no overflowing element, no console error, 0 figures without a title. The objectives in the sidebar show a straight apostrophe ("microcontroller's"), because front-matter strings are not typographically processed; that is site-level behavior of the objectives list, not raised here.

## E. Technical and source findings

None. The statements about the sequence, scope and conventions were checked against the entries (see B). The Vietnamese overview (`src/content/series/vi/embedded-and-real-time-systems.md`) carries the corrected objective 4 and the wave-2 sequence wording (commit 567c1b8); it was read, not reviewed as a translation.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: one-sentence descriptions for entries 2 to 5 (and their Vietnamese counterparts).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
