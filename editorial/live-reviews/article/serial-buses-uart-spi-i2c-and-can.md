# Live review: Serial Buses: UART, SPI, I2C and CAN

- URL: https://acrr.asia/blog/serial-buses-uart-spi-i2c-and-can
- Source: `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx` (Embedded and Real-Time Systems, entry 3)
- Commit deployed: `7e20c2c` (master after PR #57; the article source is unchanged between that commit and the reviewed branch)
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/40087219510 (2026-10-24 10:51 UTC): 26 desktop-light, 49 mobile-light, 49 mobile-dark tiles (dark tiles checked for the equations, figure, tables and code)
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-24. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship; Bosch, Motorola and NXP are named only as the originators or publishers of the specifications)

## A. Decision

Request revision. One major presentation finding (L1): at 360 px the display equation that gives the UART rate tolerance, the result of Section 2.2, is cut after "= 5", so a phone reader sees a wrong statement instead of 5.26%. The other findings are minor: an uncaptioned diagram cut at 360 px, missing waveform figures, and an overlap with Fieldbuses and Industrial Ethernet that neither page links.

**Library decision: retain and update.** The article is technically sound (every number recomputed, the CAN script re-run, the CRC check value confirmed) and is the only ACRR page that teaches UART, SPI and I2C at all; its CAN half is what connects the series to the scheduling analysis of entry 4. It should stay. The update is presentation and connection, not content: fix L1, add the waveform figures that the topic calls for (L3), and link the CAN material with the parallel treatment in [Fieldbuses and Industrial Ethernet](/blog/fieldbuses-and-industrial-ethernet) (L4). A merge is not recommended: the two pages serve different readers (firmware on one board versus a plant network) and each needs its CAN section to stand alone.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a firmware developer who has to bring up a sensor, memory or controller link on a microcontroller and choose between the four common serial links.
- Problem: knowing how each link frames, clocks, addresses and checks data, and computing the numbers that make a link work or fail (baud error, transfer time, pull-up value, CAN frame time and bus load).
- Outcome: compute UART divider error against the tolerance budget; set an SPI mode from a datasheet; size I2C pull-ups from rise time and sink current; follow CAN arbitration bit by bit; compute worst-case CAN frame time and bus load; choose a bus from the comparison table.
- Distinctive contribution: one common frame of six questions (Section 1.2) applied to all four links, worked numbers drawn from the series' running examples (the 86.8 µs UART byte and the 7 µs SPI read of entry 2), and a runnable CAN frame builder with CRC and bit stuffing whose output is verified against the standard CRC check value.
- Evidence: worked arithmetic; one Python program with real output; NXP UM10204 rev. 7.0, ISO 11898-1:2015 and 11898-2:2016, Bosch CAN 2.0, TIA-232-F, TIA-485-A, Davis et al. (2007), Di Natale et al. (2012), Horowitz and Hill (2015).
- Limitations: classical CAN and CAN FD as in the cited editions (CAN XL and the 2024 revisions not covered); the CAN bus-length model uses illustrative delays; High-speed and Ultra Fast-mode I2C only mentioned.

The benefit is delivered. The opening names the four links and the plan; Section 1.2 sets the questions, Sections 2 to 5 answer them for each link, Section 6 compares and Section 7 exercises. Checks in this review: 0.5/9.5 = 5.26% and (0.5 − 1/16)/9.5 = 4.6%; 48 MHz/(16 × 115 200) = 26.04 → 115 385 baud, +0.16%; 16 MHz → 8.68 → 111 111 baud, −3.55%; ln(0.7/0.3) = 0.8473; 2.9 V/3 mA = 967 Ω, 300 ns/(0.8473 × 200 pF) = 1770 Ω, 5901 Ω; 81 clocks at 400 kHz = 202.5 µs; the three identifiers of Section 5.3 in binary and both drop-out points; the worst-case 8-byte frame (111 + 24 = 135 bits, 270 µs); Exercises 1, 2, 4 and 5; the CAN script re-run (identical output), and its CRC function returns 0x059E for "123456789". The I2C speed-mode table agrees with UM10204 as the reviewer knows it (the 13 October audit records that Table 10 was not fetched; not verified here either).

Value density: no section is padding; the comparison table (Section 6) and the summary table each earn their place. What is missing is the representation the topic is usually taught with: timing waveforms (L3). The page has one figure, a box diagram of an I2C read; the UART frame with its sample points, the four SPI clock modes and the I2C START, STOP and ACK conditions are described only in words and tables. Value category: practical implementation. Format: explainer.

Overlap noticed (L4): [Fieldbuses and Industrial Ethernet](/blog/fieldbuses-and-industrial-ethernet) (Industrial Automation, Section 2.3 and Section 4) explains RS-485, CAN dominant and recessive bits, arbitration, the worst-case frame length with the same stuffing bound and the 40 m at 1 Mbit/s rule. The two treatments agree (8n + 47 bits plus ⌊(34 + 8n − 1)/4⌋ there; g + 8s + 13 plus the same bound here), but neither page links the other. The UART timing of Section 2 is also what [Interrupts, Polling and DMA](/blog/interrupts-polling-and-dma) builds on, and that link exists.

## C. Substantive findings

None of content. (L1 is a presentation defect that makes a result read wrongly; see D.)

## D. Visual and structural findings

### L1. UART tolerance equation cut at 360 px so that it reads "= 5"

- Location: Section 2.2, the display equation "9.5 |Δ| < 0.5 ⇒ |Δ| < 0.5/9.5 = 5.26 %"; mobile-light-09, mobile-dark-09. Also Section 5.5, the worst-case frame-time equation for $C_m$, which loses its closing bracket and $t_\text{bit}$ at 360 px (mobile-light-34, mobile-dark-34).
- Problem: at 360 px the first equation is wider than the screen and is cut immediately after "= 5", with no visible cue that it scrolls. A phone reader sees "|Δ| < 0.5/9.5 = 5", which is false as shown. At 1280 px both equations fit (desktop-light-05, 18).
- Why it matters: 5.26% is the result of the section, the theoretical tolerance budget against which the divider errors (+0.16%, −3.55%) and Exercise 1 are judged. Cutting it at the result turns a correct derivation into an apparently wrong one. The $C_m$ case is less serious (the following paragraph evaluates it in full).
- Required action: split the tolerance equation into two lines (for example an `aligned` block: "9.5 |Δ| < 0.5" on one line and "|Δ| < 0.5/9.5 = 5.26 %" on the next), and break the $C_m$ equation after the "+ 13 +" term, so that both fit at 360 px.
- Priority: major
- Acceptance condition: on new captures at 360 px, light and dark, "5.26 %" is visible in Section 2.2 without sideways scrolling, and the $C_m$ equation shows $t_\text{bit}$.

### L2. I2C transaction diagram: no caption, and its last two steps are cut at 360 px

- Location: Section 4.2, the Mermaid flowchart START → register address → repeated START → data bytes → STOP (desktop-light-10; mobile-light-20, mobile-dark-20). `facts.json` reports one SVG figure without a title on every viewport.
- Problem: at 360 px the "data bytes, ACK, last NACK" and "STOP" boxes are off-screen to the right (site-level minimum figure width, no scroll cue). The figure has no caption.
- Why it matters: minor; the prose names the steps. But the end of the transaction (the NACK on the last byte, the STOP) is exactly what a phone reader does not see.
- Required action: a caption ("Figure 1. Reading registers over I2C: a write of the register address, then a repeated START and a read; the controller NACKs the last byte and sends STOP.") and a top-to-bottom layout so it fits at 360 px, or the site-level scroll cue.
- Priority: minor
- Acceptance condition: `facts.json` of new captures reports 0 SVG figures without a title, and at 360 px all five steps are visible or a visible cue shows that the figure scrolls.

### L3. No timing waveforms for the frame and clock conventions

- Location: Section 2.1 and 2.2 (UART frame and sampling), Section 3.2 (SPI clock modes), Section 4.2 (START, STOP, ACK).
- Problem: the three ideas that bus bring-up depends on, where each bit is sampled, which clock edge each SPI mode samples on, and how START and STOP differ from data changes, are given only as prose and a table. These are conventionally shown as timing diagrams, and a diagram would replace a paragraph each (standards 6.8).
- Why it matters: minor; the text is correct and complete, but a reader matching a logic-analyzer trace to the article has nothing to compare it with, and Exercise 3 (SPI mode from edge and idle level) is easier with the four waveforms in view.
- Required action: add up to three generated inline-SVG timing diagrams (`scripts/generate-diagrams.py`, token colors, captioned): an 8N1 frame of one byte with the 16× sample points marked; SCLK for CPOL 0 and 1 with the sampling edge for CPHA 0 and 1; SDA and SCL around START, one data bit, ACK and STOP.
- Priority: minor
- Acceptance condition: the live page shows captioned timing diagrams for the UART frame, the SPI modes and the I2C conditions, legible at 360 px in light and dark mode.

Site-level issues already recorded, affecting this page: no scroll cue for wide display equations and figures at 360 px (L1, L2); the 7rem minimum cell width hides columns of several tables at 360 px, most notably the SPI mode table, whose "Clock idles" and "Data sampled on" columns, the point of the table, are behind the scroll (mobile-light-16); the CAN frame table and the comparison table are similar (mobile-light-29 to 31, 39 and 40). Dark mode: equations, the diagram, tables and code are legible (mobile-dark-09, 20, 34, 38). Code ligatures are gone.

## E. Technical and source findings

### L4. CAN arbitration and frame timing duplicated in Fieldbuses and Industrial Ethernet, with no link either way

- Location: Section 2.4 (RS-485) and Sections 5.1 to 5.7 (CAN) of this page; Sections 2.3 and 4 of [Fieldbuses and Industrial Ethernet](/blog/fieldbuses-and-industrial-ethernet).
- Problem: both pages explain dominant and recessive bits, bitwise arbitration, the worst-case stuffed frame length with the same bound (Davis et al. 2007) and the bit-rate-versus-length limit. The two agree, but neither mentions or links the other, so a reader of one does not learn that the other exists (for example the fieldbus page's Modbus RTU and IEEE 1588 context, or this page's CRC script and error confinement).
- Why it matters: minor; no reader is misled, but the library presents the same concept twice without connection, and a future correction to one could miss the other.
- Required action: add a one-sentence cross-reference in each direction (here, at the end of Section 5.5 or 5.7: CAN in plant networks and its comparison with Modbus RTU and industrial Ethernet; there, in Section 4: the CAN frame fields, CRC and fault confinement in this entry). Record the pair in the Phase 7 overlap map. A merge is not recommended (see A).
- Priority: minor
- Acceptance condition: each live page links the other at the CAN section.

No technical or source errors found. The numbers checked in B are correct; the CAN program reproduces its printed output and its CRC passes the standard check; the fault-confinement thresholds agree with ISO 11898-1 as the reviewer knows it (not verified against the paywalled text, as the 13 October audit also records). `facts.json`: HTTP 200 on all three viewports, one h1, no horizontal page scroll, no overflowing element, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory:

- [ ] L1: split the Section 2.2 tolerance equation (and the Section 5.5 $C_m$ equation) so that they fit at 360 px.

Optional:

- [ ] L2: caption and top-to-bottom layout for the I2C diagram.
- [ ] L3: timing diagrams for the UART frame, SPI modes and I2C conditions.
- [ ] L4: cross-links with Fieldbuses and Industrial Ethernet.
- [ ] Section 6, "Typical speed": give I2C in the same unit as the other columns ("100 kbit/s, 400 kbit/s, 1 Mbit/s"), since the row compares bit rates.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
