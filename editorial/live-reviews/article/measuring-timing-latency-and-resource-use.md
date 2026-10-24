# Live review: Measuring Timing, Latency and Resource Use

- URL: https://acrr.asia/blog/measuring-timing-latency-and-resource-use
- Source: `src/content/blog/measuring-timing-latency-and-resource-use.mdx` (Embedded and Real-Time Systems, entry 5)
- Commit deployed: `7e20c2c` (master after PR #57; the article source is unchanged between that commit and the reviewed branch)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 24 desktop-light, 43 mobile-light, 43 mobile-dark tiles (dark tiles checked for the figure and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Accept with minor follow-up. The article delivers its contract and closes the series honestly; every deterministic program reproduces its output and no technical error was found. Three minor findings: the wake-up experiment's output lines are cut so that the jitter and mean columns are hidden, the workflow diagram has no caption, and a few typographic defects (an opening quotation mark as apostrophe, grouped numbers split across lines).

**Library decision: retain.** This is the only ACRR page on timing measurement (instruments, high-water marks versus WCET, the probe effect, release jitter, idle-counter load, stack painting), and it is what makes the series' analysis trustworthy: it feeds measured execution times back into the response-time analysis of entry 4 and states what measurement cannot prove. The 13 October audit found language and reference-format defects only; all were fixed. Its one non-reproducible experiment (the Linux wake-up run) is labeled as a single session on a named kind of machine, as the series review required, and the text draws only patterns from it. No merge, rewrite or reclassification is warranted.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a firmware developer who has done (or read) a schedulability analysis and must now obtain its inputs and check its outcomes on real hardware.
- Problem: measuring execution time, response time, latency, jitter, processor load and memory use correctly, and knowing how far a measured maximum can be trusted as a worst case.
- Outcome: choose an instrument (GPIO pin and logic analyzer, cycle counter, trace buffer); keep high-water marks with wrap-safe arithmetic; explain why the observed maximum is not the WCET and quantify the risk; feed measured values with a margin into response-time analysis; report latency as a distribution; measure load with an idle counter and stack use by painting; run the verification cycle on every build.
- Distinctive contribution: measurement treated as the closing half of the analysis of entry 4, with a quantified argument for why tests miss rare paths ((1 − p)^n), a worked feedback of measured times into RTA, an actual drift experiment comparing absolute and relative sleeping, and small runnable demonstrations (wrap-safe subtraction, stack painting).
- Evidence: one Python script and three C programs with real output (the Python script and the two deterministic C programs re-run in this review: identical output; the wake-up program is a one-session measurement by design); Arm DDI 0403E.e, IEEE Std 1003.1-2017, Wilhelm et al. (2008), Buttazzo (2011), Lee and Seshia (2017), White (2011), Yiu (2014).
- Limitations: the jitter experiment runs on a desktop Linux virtual machine, not a microcontroller; vendor trace tools and static WCET tools are described, not demonstrated; all example sizes and counts not produced by a program are labeled as assumed.

The benefit is delivered. The opening states what entry 4 left on trust; the table of Section 1.1 maps every analysis input to its measurement, and the sections follow that table; Section 7 turns the pieces into a procedure; the closing paragraph summarizes the series without overstating it. Checks in this review: 0xE00 − 0xFFFFFF00 mod 2^32 = 3840 cycles = 80.00 µs; 2^32/48 MHz = 89.48 s; the (1 − p)^n table; the RTA with margins (0.984, 1.968, 3.252 ms; R = 1.484, 3.452, 10.140 ms); 40 × 86.8 µs = 3.47 ms; load 1 − 1.92/4.8 = 60%; 41 872 + 1 228 = 43 100 B (16.4% of 256 KiB) and 1 228 + 6 144 = 7 372 B (11.2% of 64 KiB); the stack-painting output (181 words = 724 B, 71%); the ratios of maximum to median in the printed wake-up runs (68.8, 47.8 and 132, "roughly fifty to more than a hundred"), and the drift per period (314.0/2000 = 0.157 ms to 363.1/2000 = 0.182 ms, "0.16 to 0.18"); Exercises 1 to 3.

Value density: every section serves the central question; the summary table is a review sheet. Value category: practical implementation. Format: explainer.

Overlap noticed: none that duplicates. The bus-load remarks of Section 5.2 point back to the CAN bus load of [Serial Buses: UART, SPI, I2C and CAN](/blog/serial-buses-uart-spi-i2c-and-can) by reference rather than repeating it; the jitter vocabulary is the first entry's, by link.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Wake-up experiment: the jitter and mean values are cut off

- Location: Section 4.1, the output block of the three runs (the lines beginning "absolute:"); desktop-light-13, mobile-light-23.
- Problem: each "absolute" line is longer than the code box. At 1280 px it ends at "jitter (max-mi", so the jitter and the mean of every run are hidden; at 360 px only "min", "median" and the label "99th" are visible (mobile-light-23, mobile-dark-23). The box scrolls sideways, but nothing shows it.
- Why it matters: minor; the section is titled release jitter and the program computes it, but the prose that follows quotes only medians and maxima, and the jitter can be derived from min and max. A reader who wants the program's own jitter figure must find the hidden scroll.
- Required action: optional; print each run on two lines (min, median and 99th percentile on one; max, jitter and mean on the next) and re-run, or, without re-running, keep the program and present the recorded values of the three runs as a small table (run, min, median, 99th percentile, max, jitter, mean, relative drift) under the output block.
- Priority: minor
- Acceptance condition: on new captures at 1280 px, the jitter and mean of each run are readable without sideways scrolling.

### L2. Verification-workflow diagram has no caption

- Location: Section 7, the Mermaid flowchart (desktop-light-19 and 20, mobile-light-34, mobile-dark-34). `facts.json` reports one SVG figure without a title on every viewport.
- Problem: the diagram fits at both widths and reads well in dark mode, but has no caption saying what to notice (the loop back to the model when a bound is exceeded).
- Why it matters: minor; the numbered list below repeats the cycle.
- Required action: add a caption, for example "Figure 1. The verification cycle: a measured value above its bound sends the work back to the model, not to the number."
- Priority: minor
- Acceptance condition: `facts.json` of new captures reports 0 SVG figures without a title, and the diagram has a caption.

### L3. Opening quotation mark as apostrophe; grouped numbers split across lines

- Location: Section 3.3, "$\tau_3$‘s execution time" (desktop-light-10, mobile-light-19); Section 6.1, "6 / 144 of bss" and "7 / 372 bytes" (desktop-light-16), "and 6 / 144", "and 7 / 372" (mobile-light-29); Exercise 3, "and 3 / 360 000" (desktop-light-21), "4 / 800 000" and "3 / 360 000" (mobile-light-36).
- Problem: the possessive after inline math renders as a left quotation mark (‘), and the digit-group spaces are breaking spaces, so numbers split across lines.
- Why it matters: polish; "6" at the end of one line and "144" at the start of the next reads as two numbers. The same defects are recorded as L2 of [Real-Time Operating Systems and Scheduling](/blog/real-time-operating-systems-and-scheduling) and L4 of [Inside a Microcontroller](/blog/inside-a-microcontroller), where a site-wide fix is proposed.
- Required action: write ’ after the math (or "the execution time of $\tau_3$"); non-breaking spaces in grouped numbers, preferably by the site-wide remark step.
- Priority: minor
- Acceptance condition: none of the listed defects appears on new captures at 1280 or 360 px.

Site-level issues already recorded, affecting this page: code blocks scroll sideways at 360 px without a cue (most visibly the wake-up program and its output, mobile-light-21 to 23). The three-column Section 1.1 table fits at 360 px (mobile-light-04 and 05), and the summary table fits at both widths (desktop-light-21). Dark mode: the workflow diagram and the code are legible (mobile-dark-23, 34). Code ligatures are gone.

## E. Technical and source findings

No technical or source errors found. The numbers checked in B are correct; the Python script and the two deterministic C programs reproduce their printed output (re-run here with Python 3 and `gcc -std=c11 -O2 -Wall`). The printed wake-up output cannot be reproduced by design and is labeled as such; the "earlier session ... up to 38 ms" remark has no kept output (13 October audit; not verified here either). The statement that the DWT cycle counter is optional in Armv7-M and absent in Armv6-M agrees with the Arm architecture as the reviewer knows it; not checked against a fetched copy of DDI 0403 in this review. `facts.json`: HTTP 200 on all three viewports, one h1, no horizontal page scroll, no overflowing element, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L1: make the jitter and mean of each wake-up run visible (two-line output or a small table).
- [ ] L2: caption for the workflow diagram.
- [ ] L3: apostrophe after $\tau_3$; non-breaking spaces in grouped numbers (site-wide).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
