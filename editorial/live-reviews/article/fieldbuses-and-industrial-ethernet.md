# Live review: Fieldbuses and Industrial Ethernet

- URL: https://acrr.asia/blog/fieldbuses-and-industrial-ethernet
- Source: `src/content/blog/fieldbuses-and-industrial-ethernet.mdx` (Industrial Automation, entry 3 of 5)
- Commit deployed: `7e20c2c`
- Captures: `live-captures` branch, run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 25 desktop-light, 48 mobile-light, 48 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-25. The reviewer did not write or revise this article.
- Risk: **routine.** The page explains how control networks bound their timing and compares protocols; it gives no instructions for designing safety functions or intrinsically safe circuits. Its two safety mentions are descriptive: a "safety-relevant stop command must arrive within a guaranteed time" (Section 1.1) motivates determinism, and intrinsic safety (Section 5.2) explains why process buses are slow. No reporting, named-party claims beyond neutral descriptions of standards bodies, or commercial relationship. If San prefers to treat all plant-network content as high risk, this classification can be changed; nothing on the page would then need revision.

## A. Decision

Accept with follow-up. No critical or major finding; the contract is delivered and the technical content was verified by computation. Three minor findings stay open.

**Library decision: retain and update.** The page is the series' only treatment of network timing for control (polling, arbitration, switched-Ethernet queuing, industrial Ethernet, PTP, TSN) and the later entries depend on it. Its CAN section, however, repeats the arbitration principle, the worst-case stuffing bound, the 135-bit/270 µs worked numbers and the Davis et al. reference of `serial-buses-uart-spi-i2c-and-can` (Embedded series), and neither page links to the other (L2). The update is a cross-link and an optional trim, not a merge: each page uses CAN for its own argument (bus timing in a plant here, peripheral buses there).

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who has followed entry 2 (scan cycle, response time) and now meets distributed I/O, drives and plant networks.
- Problem: why a control network must be deterministic, and how the common fieldbuses and industrial Ethernet systems achieve, or fail to achieve, bounded latency and jitter.
- Outcome: compute a Modbus RTU poll cycle and a CAN frame's worst-case length and bus load; trace CAN arbitration; compute Ethernet frame times and switch blocking delay; explain how PROFINET RT/IRT, EtherCAT, POWERLINK, PTP and TSN deal with it; choose an approach by timing need.
- Distinctive contribution: one timing argument carried from serial polling to TSN, with numbers for each step reproduced by runnable code, and a comparison table organized by where determinism comes from.
- Evidence: three Python programs with real output; Davis et al. (2007); IEC 61158, IEC 61784-1-0/-2-0:2023, IEC/IEEE 60802:2026, IEC 61131-9, IEEE 1588, 802.1AS, 802.1Q, 802.3, ISO 11898-1:2024, Modbus specifications.
- Limitations: protocol survey, not an implementation guide; product-dependent parameters labeled; no wireless, no network security (deferred to entry 5).

The benefit is delivered. The opening states the question (the delay a network adds must be bounded); Section 1 defines the vocabulary; each later section answers it for one class of network with numbers; Section 7.4 and the summary table make the comparison reusable. Recomputed for this review: CRC `C5 CD` for the example request; 0.573 ms per character, 27.9 ms per device, 279 ms for ten; Exercise 1 (11.65 ms per device, 117 ms, factor 2.4); CAN fixed fields 44 bits and stuffing region 34 + 8n bits, worst case 135 bits; 54 % load; Exercise 2 bit patterns; Exercise 3 (11 frames); 6.72 and 123.04 µs; EtherCAT 432 bytes and 36.16 µs; PTP example (0.350 and 0.500 µs) and Exercise 5 (0.10 µs error). Value category: technical decision (helps choose between network approaches by explicit timing criteria), with conceptual understanding close behind. Format: explainer. Worth its 26-minute reading effort.

Overlap: `serial-buses-uart-spi-i2c-and-can` (CAN arbitration, stuffing bound, 135 bits, RS-485), see L2; `real-time-operating-systems-and-scheduling` and `measuring-timing-latency-and-resource-use` (CAN schedulability mentioned); `networked-automation-and-digital-twins` (TSN and OPC UA PubSub, linked both ways).

## C. Substantive findings

### L2. CAN material duplicates the Embedded series without a link

- Location: Section 4, CAN: priority arbitration (desktop-light-09 to 11); compare `serial-buses-uart-spi-i2c-and-can` Sections 5.3 to 5.7.
- Problem: the arbitration mechanism, the worst-case stuffing bound ⌊(34 + 8n − 1)/4⌋, the 135-bit and 270 µs worst case and the Davis et al. reference appear on both pages, derived separately; the Embedded page also derives the 40 m length limit that this page quotes as "commonly quoted". Neither page links to the other, and the related-articles block lists only series siblings.
- Why it matters: a reader of either series does not learn that a fuller derivation exists, and the site maintains two explanations of the same result that can drift apart.
- Required action: add a sentence in Section 4.1 or 4.2 pointing to `serial-buses-uart-spi-i2c-and-can` for the bit-level derivation (stuffing, CRC, error handling, length limit); optionally shorten Section 4.2 to the formula and the bus-load use. Record the pair in the Phase 3 overlap map.
- Priority: minor
- Acceptance condition: the live page links to the serial-buses article from Section 4.

## D. Visual and structural findings

### L1. PTP delay formula hidden at 360 px

- Location: Section 8.2, the second display equation (mobile-light-35; mobile-dark-35 the same).
- Problem: at 360 px the pair "θ = …, d = …" shows θ and only "d =" at the edge; the delay formula is off-screen, with no scroll cue (site-level behavior).
- Why it matters: d is one of the two results of the section; the summary table restates only θ. A phone reader can rebuild it from the worked example, so the finding is minor.
- Required action: put θ and d on separate lines (`aligned` block), and do the same for the pair above it.
- Priority: minor
- Acceptance condition: at 360 px both the θ and the d formulas are fully visible.

### L3. Sequence diagram without caption or accessible name

- Location: Section 8.2, PTP message-exchange diagram (desktop-light-18; `facts.json`: 1 SVG figure without title).
- Problem: no caption, no accessible title; the "Follow_Up" and "Delay_Req" labels touch the lifelines.
- Why it matters: the caption is where the reader would be told which time stamps each clock reads, which the next paragraph relies on; screen-reader users get nothing.
- Required action: add `accTitle`/`accDescr` and a caption ("t1 and t4 are read on the master clock, t2 and t3 on the slave clock").
- Priority: minor
- Acceptance condition: a visible caption under the diagram, and `facts.json` reports 0 SVG figures without title.

Site-level behavior also seen here (already recorded): at 360 px the layer, media-access, ADU and comparison tables scroll under the 7rem cell minimum; code and output lines are cut at the box edge (desktop-light-10 docstring; mobile-light-13 output); the C_max equation loses "bit times." at 360 px. Dark mode: diagram, equations and code legible (mobile-dark-14, 19, 34, 35).

## E. Technical and source findings

No technical or source errors found; all figures recomputed (Section B). The IEC/IEEE 60802 and IEC 61784 references were corrected in wave 2 and are correct on the live page. Not verified in this review: PROFIBUS DP segment lengths, HART frequencies and IO-Link rates were checked against reviewer knowledge only (they agree), not against the specifications. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none.

Optional (follow-up):

- [ ] L2: link to `serial-buses-uart-spi-i2c-and-can` from Section 4; optionally trim Section 4.2.
- [ ] L1: split the PTP equation pairs for narrow screens.
- [ ] L3: caption and accessible title for the PTP diagram.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
