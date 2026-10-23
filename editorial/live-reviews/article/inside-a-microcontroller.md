# Live review: Inside a Microcontroller

- URL: https://acrr.asia/blog/inside-a-microcontroller
- Source: `src/content/blog/inside-a-microcontroller.mdx` (Embedded and Real-Time Systems, entry 1)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 27 desktop-light, 51 mobile-light, 51 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): the code font's ligatures turn the C operators the article teaches (`|=`, `!=`, `==`, `->`) into mathematical symbols, in the prose that defines them, in the programs and in Exercise 3. The cause is site-wide styling, not the article text; the fix is one CSS rule. The other findings are minor.

**Library decision: retain.** The article is the foundation entry of its series, every later entry depends on its vocabulary (Section 1.2) and its hardware model (Sections 3 to 6), and the 13 October audit found no technical error; this review found none either. Its content does not need to change. The required revision is presentation only (L1 at site level; L2 to L4 are polish), so no rewrite, merge or reclassification is warranted.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a programmer who knows C and basic digital logic but has no embedded experience, starting the Embedded and Real-Time Systems series.
- Problem: understanding what is inside a microcontroller and how firmware reaches it, and what "real-time" means precisely enough to reason about deadlines.
- Outcome: use the timing vocabulary (release, deadline, response time, latency, jitter; hard, firm and soft); read a memory map and drive memory-mapped registers through `volatile` pointers; explain startup from reset to `main`; compute timer periods, PWM resolution and ADC step size; see why a superloop couples latencies.
- Distinctive contribution: one path from the definition of real time to the hardware that makes timing predictable, with every number worked (timer settings, PWM resolution, memory budget, ADC LSB), a runnable host-side model of a GPIO peripheral, and exercises with answers; it sets the vocabulary the rest of the series uses.
- Evidence: worked arithmetic in the text; two programs with their real output (a C model of a GPIO block, a Python timer-setting search); Arm DDI 0403E.e, ISO/IEC 9899:2011, Kopetz (2011), Lee and Seshia (2017), White (2011), Yiu (2014).
- Limitations: a generic Cortex-M with invented register layouts, not any vendor's part; interrupts, DMA, buses, scheduling and measurement are left to later entries.

The benefit is delivered. The opening names the question and the prerequisites; the sections follow the path from timing vocabulary to hardware to firmware structure, and the superloop at the end sets up the next entry. Spot checks (recomputed in this review): 1/48 MHz = 20.83 ns; 65 536/48 MHz = 1.365 ms; 2^32/48 MHz = 89.5 s; the timer script's three lines (15 × 64 000 = 960 000 gives exactly 50 Hz; 48 MHz/1088 = 44 117.647 Hz, +400.2 ppm, and no product closer to 1088.4 exists); log2 2400 = 11.2 and log2 1920 = 10.9 bits; 3.3 V/4096 = 0.806 mV and 3000 LSB = 2.417 V; 20 ppm × 86 400 s = 1.73 s; 8000 B of 65 536 B = 12.2%; Exercise 5 totals. The claim of Exercise 3 was checked by compiling its loop with GCC and Clang at `-O2`: both read the register once and branch into an endless loop, as the answer says.

Value density: no section is padding. The two tables that recap (Section 1.3, the series map, and Section 9, the summary) each serve a purpose, the first for orientation in a five-part series and the second as a review sheet. Value category: conceptual understanding (a foundation for the series), with practical implementation close behind. Format: explainer.

Overlap noticed: Section 6.2 touches the ADC also covered by [Sampling, Quantization and Data Conversion](/blog/sampling-quantization-and-data-conversion), but it defers sampling theory to that article by link and covers only how firmware uses the converter, which is the right division. The watchdog (Section 5.4) and the superloop (Section 7.2) have a counterpart in the scan cycle and watchdog of [Programmable Logic Controllers](/blog/programmable-logic-controllers); a cross-link would serve readers of either series (Phase 7 overlap map), but there is no duplication.

## C. Substantive findings

### L1. Code ligatures replace the C operators the article teaches

- Location: Section 3.2, second bullet ("`x |= mask` sets bits ... `(x & mask) != 0` tests them"); the GPIO program in Section 3.2; Section 3.3 first paragraph (`GPIOA->DIR |= BIT(LED_PIN)`); the Python script in Section 5.1 (`<=`, `==`); Exercise 3 (`== 0`). desktop-light-09 to 12, 17 and 23; mobile-light-19 to 21, 33 and 45; the same in dark mode.
- Problem: the monospace font's contextual ligatures are active, so `|=` is drawn as a single "⊨" glyph, `!=` as "≠", `==` as a long double bar, `->` as an arrow and `<=` as "≤". The sentence whose purpose is to show the reader the C syntax for setting, clearing and testing bits shows symbols that are not C.
- Why it matters: the article's reader knows basic C but is new to register manipulation; Exercise 3 asks them to read and diagnose a code fragment. A reader who copies what they see by hand (or reads it aloud, or searches for it) gets operators that do not exist in C. Copy-and-paste still yields the right characters, which is why the defect is easy to miss in review.
- Required action: turn off ligatures for code on the site, for example `font-variant-ligatures: none;` (or `font-feature-settings: "liga" 0, "calt" 0;`) on `.prose code` and `.prose pre` in `src/styles/prose.css`. Site-level change; it affects every page with code, which is the reason to do it once.
- Priority: major
- Acceptance condition: on new captures of this page, `|=`, `!=`, `==` and `->` appear as two separate characters in Section 3.2, Section 3.3 and Exercise 3, at 1280 and 360 px.

## D. Visual and structural findings

### L2. Block diagram of Section 2.1: right half off-screen at 360 px, and no caption

- Location: Section 2.1, the Mermaid diagram of CPU, memories, bus, peripherals and pins; mobile-light-11, mobile-dark-11.
- Problem: at 360 px the diagram keeps its minimum width (site rule: 60 percent of its natural width) and the "Peripherals" and "Pins" boxes are cut at the right edge with no scroll cue. The figure also has no caption (`facts.json`: one SVG figure without a title), so nothing tells the reader what to take from it.
- Why it matters: the point of the diagram is that peripherals reach the outside world through pins; a phone reader sees only the left half. Small, because the next paragraph says the same in words.
- Required action: either a top-to-bottom layout (`flowchart TB`) for this diagram so it fits at 360 px, or the site-level scroll cue for wide figures already proposed in the live review of [Spectra: The DFT and the FFT](/blog/dft-and-fft) (finding L2 there); and a one-sentence caption (for example "Figure 1. A microcontroller: core, memories and peripherals on one on-chip bus; peripherals reach the pins.").
- Priority: minor
- Acceptance condition: at 360 px all five boxes are visible, or a visible cue shows that the figure scrolls; the figure has a caption.

### L3. Section 3.4 table: the run-time column is hidden at 360 px

- Location: Section 3.4, the table of sections (`.text`, `.rodata`, `.data`, `.bss`, stack, heap); mobile-light-23 and 24. Also the memory-map table of Section 3.1, whose "Typical contents" column is cut (mobile-light-16 and 17).
- Problem: at 360 px the fourth column, "Lives at run time in", is entirely behind the table's horizontal scroll; only a faint shadow shows that there is more.
- Why it matters: that column is the point of the table (`.data` is stored in flash but lives in SRAM; Exercise 5 depends on it). Desktop readers see it; phone readers have to discover the scroll.
- Required action: make the table fit at 360 px, for example by merging the last two columns into one "Flash → SRAM" style column ("Location: stored → at run time") or by shortening the "Contents" cells; for the memory map, shorter "Typical contents" cells would let the three columns fit.
- Priority: minor
- Acceptance condition: at 360 px the run-time location of every section is visible without scrolling the table.

### L4. Numbers, units and punctuation split across lines

- Location: Section 5.3 ("1 part in 48 / 000", desktop-light-18 and 19; "20.83 / ns", desktop-light-18); Section 5.1 ("at 48 / MHz", "1.365 / ms", desktop-light-16, mobile-light-32); Conventions ("$10^{-6}$ / s)", mobile-light-03); Section 1.2 (the period after "relative deadline $D$" alone on a line, mobile-light-07); Section 5.2 (a comma alone at the start of a line after "compare value $C$", mobile-light-34).
- Problem: the digit-group spaces and the spaces between numbers and units are ordinary breaking spaces, and punctuation after inline math can wrap on its own.
- Why it matters: polish; "48" at the end of one line and "000" at the start of the next reads as two numbers.
- Required action: use non-breaking spaces (U+00A0, or the narrow U+202F for digit groups) between a number and its unit and inside grouped numbers in prose, and keep punctuation attached to inline math (inside the math or joined with a word joiner). A site-wide remark step that does this for "number + unit" would fix it once for every article.
- Priority: minor
- Acceptance condition: none of the listed splits appears on new captures at 1280 or 360 px.

The page already uses the right representations for its material: classification and summary tables, a block diagram, a memory-map table, worked numbers and runnable code with real output, and exercises with collapsible answers. No further visual is needed.

## E. Technical and source findings

No technical or source errors found. All numbers checked (Section B) are correct; the C and Python programs reproduce their printed output (13 October audit, and the arithmetic re-checked here); the references are complete and in house format, including the Arm manual's issue and year added in wave 2. `facts.json`: HTTP 200 on all three viewports, one h1, no horizontal page scroll at 360 px, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory:

- [ ] L1: disable font ligatures for inline and block code (site-level CSS).

Optional:

- [ ] L2: top-to-bottom layout or scroll cue for the Section 2.1 diagram, and a caption.
- [ ] L3: make the Section 3.4 (and 3.1) table fit at 360 px.
- [ ] L4: non-breaking spaces in grouped numbers and number-unit pairs; punctuation attached to inline math.
- [ ] Cross-link Section 5.4 and 7.2 with the scan cycle and watchdog of Programmable Logic Controllers (Phase 7 overlap map).

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
