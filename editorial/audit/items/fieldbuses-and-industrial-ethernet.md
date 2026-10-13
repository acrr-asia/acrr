<!-- audit: {"slug":"fieldbuses-and-industrial-ethernet","type":"article","series":"industrial-automation","priority":"P2","before":{"purpose":4,"structure":4,"accuracy":3,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":3}} -->
# Audit: Fieldbuses and Industrial Ethernet

- Path: `src/content/blog/fieldbuses-and-industrial-ethernet.mdx` · Route: `/blog/fieldbuses-and-industrial-ethernet` · Type: article (series entry) · Series `industrial-automation`, entry 3 of 5 · Words: 4,316 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 4.
- structure 4: vocabulary → media access → two worked fieldbuses → process buses → Ethernet's limits → industrial Ethernet → time sync → TSN.
- accuracy 3: all three Python programs re-run with identical output (CRC `C5 CD`, 27.9 ms per device; `winner: 0x123`; 111/135 bits, 54 %). Recomputed: Exercise 1 (0.0955 ms, 11.65 ms, 116.5 ms, factor 2.39), Exercise 3 (540 µs, 11 frames), Ethernet 6.72/123.04 µs, Exercise 4 (12.3 µs, 36.9 µs), EtherCAT 432 bytes / 36.16 µs, PTP example and Exercise 5, bit patterns of Exercise 2. One wording overstates a specification (A1).
- evidence 2: three reference entries each bundle several works (IEEE line: three standards; IEC 61784-1 and -2; two Modbus documents); the Davis et al. entry has no pages; no years except Davis.
- language 3: 54- and 72-word sentences; "plainly".
- consistency 3: CRC and CAN abbreviations used before expansion.
- publishing 2: description 360 characters; five level-2 headings in title case.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| A1 | Should fix | `:304` | accuracy | "the Modbus serial-line specification fixes the silent interval at 1.75 ms" — the specification recommends it |
| P1 | Should fix | `:3` | publishing | Description 360 characters |
| P2 | Should fix | `:19, 46, 71, 129, 189, 208, 257` | publishing | Level-2 headings in title case |
| C1 | Should fix | `:367-374` | evidence | References bundle several works per entry; Davis et al. without pages and with title-cased title; Modbus documents without versions or years; not alphabetical |
| C2 | Should fix | `:17`, `:43` | consistency | "CAN" (intro) and "CRC" (layer table) used before their expansion in Sections 4.1 and 3.2 |
| C3 | Optional | `:212`, `:230` | language | Sentences of 54 and 72 words |
| C4 | Optional | `:216` | language | "which is plainly not deterministic" |
| C5 | Optional | `:17` | language | "RTU" never expanded |

### A1. 1.75 ms is a recommendation
- **Where:** `:304`, Exercise 1
- **Text:** "(At bit rates above 19 200 bit/s the Modbus serial-line specification fixes the silent interval at 1.75 ms instead of 3.5 characters.)"
- **Evidence:** *MODBUS over Serial Line Specification and Implementation Guide* V1.02 (Dec 20, 2006), Section 2.5.1.1: for baud rates greater than 19 200 bit/s, fixed values are recommended, "a value of 1.750 ms for inter-frame delay (t3.5)" (fetched and read).
- **Correction:** "recommends a fixed silent interval of 1.75 ms". The calculation is unchanged.

### C1. References
- **Correction:** one entry per work, alphabetical: Davis et al. with "vol. 35, no. 3, pp. 239–272, 2007" (University of York publication page); IEC 61158 (series); IEC 61784-1; IEC 61784-2; IEEE 1588; IEEE 802.1AS; IEEE 802.1Q; IEEE 802.3; IEC 61131-9; ISO 11898-1; Modbus Organization, *MODBUS Application Protocol Specification*, V1.1b3, 2012; Modbus Organization, *MODBUS over Serial Line Specification and Implementation Guide*, V1.02, 2006 (cover read). IEEE and IEC multipart standards stay undated: the text relies on features present in the current editions, and the IEEE editions have changed during 2025 (search results show 802.1AS-2025), so a guessed year would be worse than none.

## Revision log (wave 1)
- Technical correction: Exercise 1 note now says the serial-line specification "recommends a fixed silent interval of 1.75 ms" instead of "fixes". Evidence: *MODBUS over Serial Line Specification and Implementation Guide* V1.02 (20 Dec 2006), fetched: for rates above 19 200 bit/s "a value of 1.750ms for inter-frame delay (t3.5)" is recommended. Calculation and answer unchanged. (A1)
- Prose: Ethernet frame sentence split into three; EtherNet/IP paragraph split; TSN closing sentence split; "plainly not deterministic" → "not deterministic". (C3, C4)
- Terminology: CAN expanded at first use in the introduction; Modbus RTU glossed as "the remote terminal unit mode of Modbus"; CRC expanded at first use in the layer table (Section 3.2 keeps the bold term). (C2, C5)
- Headings: seven level-2 headings to sentence case; anchors unchanged (`#9-time-sensitive-networking`, linked from entry 5, still resolves). (P2)
- Metadata: description 360 → 151 characters. (P1)
- References: one entry per work (13 entries from 8 lines), alphabetical; Davis et al. completed to vol. 35, no. 3, pp. 239–272, 2007 (University of York publication page); ISO 11898-1:2024 with its current title ("physical coding sublayer", iso.org page fetched); IEC 61784-2 title as on the ANSI webstore listing of edition 4.0; IEC 61131-9 title as on the IEC webstore listing; Modbus documents with versions and years (V1.1b3, 2012; V1.02, 2006 from the document cover). (C1)
- Remaining warnings: none. Suggestions: 8 `reference-format` (multipart IEC series and IEEE standards left undated: the text relies on features in the current editions, and IEEE editions changed during 2025, so a year would be a guess); one 50-word sentence in Exercise 4's answer; acronym false positives (TX in 100BASE-TX, FFFF, AND, DP/PA/FD/IRT given as product names and expanded where first defined, ODVA is an organization name).
- Flags for independent review: (1) fact-check "the joint IEC/IEEE 60802 project defines a TSN profile" (line 300): the profile may now be published as a standard, in which case "project" should become the standard's designation; (2) fact-check "Protocols such as PROFINET and EtherNet/IP ... are being adapted to run over it" for currency; (3) another series cites ISO 11898-1:2015 (`serial-buses-uart-spi-i2c-and-can.mdx`); both editions exist, but the Series Editor may want one edition site-wide.
- Vietnamese translation affected: no translation of this article exists.
- Coordinator request (embedded-series editor, Davis et al. reference): applied. Line 367 now reads exactly `R. I. Davis, A. Burns, R. J. Bril and J. J. Lukkien, "Controller Area Network (CAN) schedulability analysis: Refuted, revisited and revised," *Real-Time Systems*, vol. 35, no. 3, pp. 239–272, 2007.` This is the published sentence-case title. It matches the form that editor checked against the Springer page, so this series and the embedded series cite the paper identically.
