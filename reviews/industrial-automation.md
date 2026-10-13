# Series review: Industrial Automation

- Series: `industrial-automation` (5 articles, status published, 0 planned entries)
- Reviewed commit: 6fe0853
- Date: 2026-10-13
- Content hash: sha256:e542d8a7c8ea29013800b8b575a45fc396da0aae2a523d5bee9a3f3684a2be99

## Summary
The series is technically strong and well structured: it moves from Boolean logic and state machines through the PLC, fieldbuses and industrial Ethernet, and PID control to ISA-95, OPC UA and digital twins, and every worked example that could be recomputed was correct (all nine Python programs reproduce their printed output byte for byte, and the CRC, CAN frame, Ethernet timing, PTP, scaling, tuning and observer formulas check out). The problems are local. Three statements are wrong: the fourth entry says the control series "called regulation" what that series calls disturbance rejection; the second entry says the 4–20 mA loop current "must never fall below about 4 mA" a few lines before it lists NE 43 levels of 3.8 and 3.6 mA; and the third entry says CAN identifiers 0x123 and 0x124 differ only in their last two bits (they differ in three). The most important should-fix item is that the series presents IEC 61131-3:2013 as current although a fourth edition, which removes Instruction List, was published in May 2025. Other items are a link whose text names the control series but targets its first entry, a promise in the first entry that the second only partly keeps, an imprecise remark on Modbus data age, the NE 43 reference, the PNP/NPN regional remark, and some redundancy. With these corrections the series is ready.
Findings: 3 blocking, 7 should fix, 6 optional.

## Resolution

All findings were applied on branch `review/industrial-automation` (one commit on top of 6fe0853).

- **F1** (`pid-control-of-process-variables.mdx`): removed "which the control series called regulation"; the sentence now says disturbance rejection and setpoint tracking are two of the requirements listed in the control series' [first entry](/blog/introduction-to-control-systems), which names "Tracking" and "Disturbance rejection".
- **F2** (`programmable-logic-controllers.mdx`, Section 3.3): the loop-power item now says the transmitter's own consumption must stay below the lowest current it ever signals, the 3.6 mA failure level.
- **F3** (`fieldbuses-and-industrial-ethernet.mdx`, Section 4.1): "last two bits" corrected to "last three bits", with both identifiers written in binary.
- **F4**: the fourth edition, IEC 61131-3:2025 (published May 2025, Instruction List removed), is now mentioned in the first entry (Section 4.1), and in the second entry's introduction, Section 4.1 (edition history, and five languages in the third edition, four in the fourth), Section 5.4 and the summary table. The series still follows the third edition, which is stated.
- **F5**: the first entry now links the [Foundations of Control Systems](/series/foundations-of-control-systems) series page under its name, plus its introduction and Feedback and System Behavior entries. The fourth entry names it the "five-entry" series. No text in the series called the control series in progress; nothing needed changing there. Links to `/blog/stability-and-eigenvalues` and `/blog/state-feedback-controller-design` were not added because those pages do not exist on this branch's older base and would fail `check:links`; the series-page link reaches them after the merge.
- **F6**: the first entry's promise now reads "why the order of statements within one evaluation matters", which the second entry's Sections 2.1 and Exercise 4 deliver.
- **F7**: "every value is at least one full poll cycle old" replaced by "a value can be up to a full poll cycle old before it is refreshed".
- **F8**: the PNP/NPN remark is now phrased as a general tendency ("predominate in Europe ... more common in parts of Asia, but both are found everywhere").
- **F9**: NE 43 reference now carries its title (*Standardization of the Signal Level for the Failure Information of Digital Transmitters*) and edition (2021), confirmed on namur.net; the text says the 3.8–20.5 mA and ≤3.6 / ≥21 mA figures are the transmitter signal levels and that receiver thresholds, for which the 2021 edition adds a safety margin, should be taken from the current edition and the module documentation.
- **F10**: redundancy cut: the second entry's language-choice table (repeated each language section and the summary) replaced by one sentence; its Section 1.1 relay history shortened and the first bullet of Section 1.3 condensed (both restated Sections 1.1 and 2); in the first entry, the controller sentence of Section 1.1 (repeated by the series table), the tool list in the introduction (repeated in the description and the table), the restatement of the relay column after the Boolean table, and a sentence restating the Moore form; in the third entry, a repeated clause on PROFINET RT device processing; in the fourth, a sentence repeating that the valve dominates flow loops; in the fifth, the "Not a single universal model" bullet, which restated the "Purposeful" bullet of Section 5.1 (folded into it). Net prose change, with the added corrections: 5160 → 5122, 5057 → 5116, 5029 → 5051, 4615 → 4630, 5033 → 5025 words. Deviation: the entries remain above 4,500 words. The remaining length is worked examples, exercises and distinct technical content, not repetition; the end-of-entry summary tables are part of the series structure and were kept.
- **F11–F16** (optional) applied: capacitive sensors "most other materials, including non-metals"; "Besides its n data bytes"; a sentence in the second entry explaining why its reset-dominant jam latch is harmless despite the first entry's advice for alarms; the fourth entry points back to where the Laplace variable and the proportional offset were introduced; Manchester coding glossed; the series file (and its Vietnamese translation, `src/content/series/vi/industrial-automation.md`, as "loạt bài Cơ sở hệ thống điều khiển", the translated title of that series) names the Foundations of Control Systems series. No English article of this series has a Vietnamese translation, so no article translation was changed.
- **Second pass** (full re-read after the corrections):
  - S1 (Blocking, missed in the first pass): the answer to Exercise 1 of the second entry said "The relay output contributes as much as the input filter and the scan combined in the best case"; 10 ms is not 6 + 15 = 21 ms. Replaced by "The relay output alone contributes 10 ms, about a third of the best case" (10/31 = 32 %).
  - S2 (Should fix, introduced by F4): the second entry's Section 4.1 still said the standard defines "five programming languages"; now "five in the third edition, four in the fourth, which drops Instruction List".
  - S3 (Should fix, introduced by F10): shortening the second entry's Section 1.1 left "those panels" without an antecedent; the sentence was rewritten ("machine logic was wired from relays in a cabinet ... to replace those relay panels").
  - A further full pass found no Blocking or Should-fix issue.
- **Re-run results:** `npm run build:local` exit 0 (0 errors, 81 pages indexed); `npm run check:links`: 222 pages, 6326 internal references, all resolve. Mermaid min-widths after the change: 410, 487, 291, 234, 527, 142 and 269 px (all ≤ 600); no `katex-error`; no text glued to `<a`, `<strong>`, `<code>` or `<span>`. All nine Python blocks re-run: seven printed output blocks match byte for byte, and the three outputs quoted in prose (`True`; `min 13.5 ms, max 23.5 ms, mean 18.5 ms`; `winner: 0x123`) match.

## Objectives coverage
| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Express control tasks as Boolean logic and as sequential, state-based programs. | Entry 1 (Sections 2–5), entry 2 (Section 5: LD, ST `CASE`, SFC) | Fully covered, with worked examples and exercises. |
| Describe how a programmable logic controller executes a program, and the languages defined for it. | Entry 2 (scan cycle, response time, tasks, IEC 61131-3 model and languages) | Fully covered; needed the 2025 edition note (F4). |
| Compare fieldbus and industrial Ethernet systems by timing, topology and determinism. | Entry 3 (Sections 1–2, 3–9, comparison table in 7.4) | Covered. Topology is treated briefly (Section 2.2) and not in the comparison table; adequate for the objective. |
| Tune PID loops for typical process variables such as temperature, level, flow and pressure. | Entry 4 (Sections 2–6, simulations and exercises) | Fully covered. |

## Findings
| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `src/content/blog/pid-control-of-process-variables.mdx` | Section 1.1 (line 42) | Cross-article references | Claims the control series "called regulation" what it calls disturbance rejection. |
| F2 | Blocking | `src/content/blog/programmable-logic-controllers.mdx` | Section 3.3 (line 145) | Technical accuracy | Loop current "must never fall below about 4 mA" contradicts the 3.8 and 3.6 mA NE 43 levels four lines later. |
| F3 | Blocking | `src/content/blog/fieldbuses-and-industrial-ethernet.mdx` | Section 4.1 (line 149) | Technical accuracy | 0x123 and 0x124 differ in their last three bits, not two. |
| F4 | Should fix | entries 1 and 2 | `logic-and-sequential-control.mdx:231`; `programmable-logic-controllers.mdx:17, 194, 356, 381, 453, 455` | Stated versions and defaults | IEC 61131-3:2013 presented as current; the fourth edition (May 2025), which removes Instruction List, is not mentioned. |
| F5 | Should fix | `src/content/blog/logic-and-sequential-control.mdx` | Introduction (line 19) | Cross-article references | Link text "control systems series" targets the series' first article, not the series. |
| F6 | Should fix | `src/content/blog/logic-and-sequential-control.mdx` | Section 3.4 (line 225) | Cross-article references | Promises the second entry shows "why it matters where in the program the update of x_prev is placed"; it does not discuss that. |
| F7 | Should fix | `src/content/blog/fieldbuses-and-industrial-ethernet.mdx` | Section 3.3 (line 125) | Technical accuracy | "every value is at least one full poll cycle old" is wrong; a value is up to one cycle old. |
| F8 | Should fix | `src/content/blog/programmable-logic-controllers.mdx` | Section 3.1 (line 123) | Technical accuracy | PNP/NPN regional remark stated as a rule rather than a tendency. |
| F9 | Should fix | `src/content/blog/programmable-logic-controllers.mdx` | Section 3.3 (line 149), References (line 466) | Factual consistency | NE 43 reference gives a paraphrase instead of the title and no edition; the 2021 revision on receiver detection is not reflected. |
| F10 | Should fix | all five | see detail | Writing quality | Each entry exceeds 5,000 words of prose; several passages restate nearby material. |
| F11 | Optional | `src/content/blog/logic-and-sequential-control.mdx` | Section 1.1 (line 27) | Technical accuracy | Capacitive sensors detect "any material": overstated. |
| F12 | Optional | `src/content/blog/fieldbuses-and-industrial-ethernet.mdx` | Section 4.2 (line 155) | Writing quality | "Around n data bytes" means "besides". |
| F13 | Optional | `src/content/blog/programmable-logic-controllers.mdx` | Section 5.3 (line 303) | Factual consistency | Reset-dominant jam latch without comment, while entry 1 recommends set-dominant latches for alarms. |
| F14 | Optional | `src/content/blog/pid-control-of-process-variables.mdx` | Sections 2.1, 3.1 (lines 58, 98) | Concept introduction | Laplace variable and the proportional offset rely on the control series without pointing to where. |
| F15 | Optional | `src/content/blog/fieldbuses-and-industrial-ethernet.mdx` | Section 5.2 (line 200) | Concept introduction | "Manchester-coded" used without explanation. |
| F16 | Optional | `src/content/series/industrial-automation.md` | Body (line 13) | Cross-article references | "the control systems series" not named. |

### F1. False claim about the control series' terminology
- **Where:** `src/content/blog/pid-control-of-process-variables.mdx:42`, section "1.1 The loop"
- **Text:** "so **disturbance rejection**, which the control series called regulation, usually matters more than **setpoint tracking**."
- **Problem:** The Foundations of Control Systems series never uses "regulation". Its first entry (`introduction-to-control-systems.mdx`, "What makes a controller good") lists "Tracking" and "Disturbance rejection" as requirements. The cross-reference is false.
- **Recommended correction:** "so **disturbance rejection** usually matters more than **setpoint tracking** (two of the requirements listed in the control series' [first entry](/blog/introduction-to-control-systems))."

### F2. Loop current lower limit contradicts NE 43
- **Where:** `src/content/blog/programmable-logic-controllers.mdx:145`, section "3.3 Analog signals: the 4–20 mA current loop"
- **Text:** "A two-wire transmitter can draw its own operating power from the loop current, which must never fall below about 4 mA"
- **Problem:** Line 149 says measurement currents go down to 3.8 mA and failures are signalled at or below 3.6 mA, so the loop current routinely falls below 4 mA. What is true is that the transmitter's own consumption must be below the lowest current it signals.
- **Recommended correction:** "... from the loop current, so one pair of wires carries both power and signal. Its own consumption must therefore stay below the lowest current it ever signals, the 3.6 mA failure level described below."

### F3. CAN identifiers differ in three bits, not two
- **Where:** `src/content/blog/fieldbuses-and-industrial-ethernet.mdx:149`, section "4.1 Dominant and recessive bits"
- **Text:** "The identifiers 0x123 and 0x124 agree until their last two bits"
- **Problem:** 0x123 = 001 0010 0011 and 0x124 = 001 0010 0100 first differ at bit 2, so they differ in their last three bits (011 vs 100). The conclusion (0x123 wins) is right.
- **Recommended correction:** "The identifiers 0x123 (001 0010 0011) and 0x124 (001 0010 0100) agree until their last three bits, and 0x123 wins because at the first of those bits it has a dominant 0 where 0x124 has a 1."

### F4. IEC 61131-3 fourth edition not mentioned
- **Where:** `src/content/blog/logic-and-sequential-control.mdx:231`; `src/content/blog/programmable-logic-controllers.mdx:17, 194, 356, 381, 453, 455`
- **Text:** "IEC 61131-3:2013, which is the edition most current programming tools implement"; "first published in 1993, with a second edition in 2003 and the third edition in 2013"; "Instruction List (deprecated in 2013)"
- **Problem:** IEC 61131-3:2025, edition 4.0, was published on 22 May 2025 (standards-body listing); its scope lists ST, LD, FBD and SFC, and Instruction List, deprecated in the third edition, is removed. The series presents the 2013 edition as the current one and the edition history as ending in 2013; the claim about "most current programming tools" cannot be verified.
- **Recommended correction:** Keep the third edition as the series' basis, and state that a fourth edition, IEC 61131-3:2025, was published in May 2025 and removes Instruction List; update the edition history, Section 5.4 and the summary table; drop the unverifiable claim about tools.

### F5. Link text names the series but targets an article
- **Where:** `src/content/blog/logic-and-sequential-control.mdx:19`, introduction
- **Text:** "the feedback ideas of the [control systems series](/blog/introduction-to-control-systems)"
- **Problem:** The text names a series, the link goes to its first article, and the series is not named. The Foundations of Control Systems series is complete (five entries on master).
- **Recommended correction:** "the feedback ideas of the [Foundations of Control Systems](/series/foundations-of-control-systems) series, from its [introduction](/blog/introduction-to-control-systems) and its entry on [feedback and system behavior](/blog/feedback-and-system-behavior)."

### F6. Promise about the x_prev update not kept
- **Where:** `src/content/blog/logic-and-sequential-control.mdx:225`, section "3.4 Edge detection"
- **Text:** "the second entry shows that this is exactly how a programmable controller works, and why it matters where in the program the update of $x_{\text{prev}}$ is placed."
- **Problem:** The second entry (Section 2.1 and Exercise 4) explains that statement order within a scan matters, but never discusses where the `x_prev` update goes.
- **Recommended correction:** "... and why the order of statements within one evaluation matters."

### F7. Age of polled data misstated
- **Where:** `src/content/blog/fieldbuses-and-industrial-ethernet.mdx:125`, section "3.3 What the numbers say"
- **Text:** "every value is at least one full poll cycle old when the client has collected it."
- **Problem:** A value just read is fresh; values age up to one poll cycle before they are refreshed.
- **Recommended correction:** "... and a value can be up to a full poll cycle old before it is refreshed."

### F8. PNP/NPN regional remark
- **Where:** `src/content/blog/programmable-logic-controllers.mdx:123`, section "3.1 Digital inputs"
- **Text:** "PNP sensors with sinking inputs are the usual choice in European practice, while NPN wiring is common in parts of Asia"
- **Problem:** This is a tendency, not a rule, and the text gives no source; it should be phrased as such.
- **Recommended correction:** "As a general tendency, PNP sensors with sinking inputs predominate in Europe and NPN wiring is more common in parts of Asia, but both are found everywhere;"

### F9. NE 43 reference and edition
- **Where:** `src/content/blog/programmable-logic-controllers.mdx:149, 466`
- **Text:** "NAMUR Recommendation NE 43, on the standardization of signal levels for failure information from transmitters with analog output, NAMUR."
- **Problem:** The reference paraphrases instead of giving the title. NAMUR's own page gives the title "Standardization of the Signal Level for the Failure Information of Digital Transmitters" and an edition dated 2021-07-26, which mainly adds a safety margin for signal detection in the control system. The text's figures (3.8–20.5 mA measurement, ≤ 3.6 or ≥ 21 mA failure) are the transmitter signal levels; receiver thresholds may differ under the 2021 edition, which the text does not say.
- **Recommended correction:** Give the title and edition in the reference; describe the figures as transmitter signal levels and say receiver thresholds should be taken from the current edition and the module documentation.

### F10. Redundancy
- **Where:** all five entries (prose word counts without code: 5160, 5057, 5029, 4615, 5033).
- **Text (examples):** `programmable-logic-controllers.mdx:374–384` (Section 5.6 table repeating the "best for" sentence of every language section and the summary row); `programmable-logic-controllers.mdx:23` and `:41` (relay history and cyclic execution, restated from Section 1.1 and Section 2); `logic-and-sequential-control.mdx:17` (tool list repeated in the description and Section 1.4), `:30` (controller sentence repeated by the table row two lines below), `:74` (restating the relay column of the table above), `:286` ("an actuator is on only in the states that list it", the Moore definition of Section 5.1); `fieldbuses-and-industrial-ethernet.mdx:234` ("This shortens processing in the end devices", repeating the previous sentence); `pid-control-of-process-variables.mdx:293` ("The valve's dynamics ... often dominate the loop", repeating the first sentence of the paragraph); `networked-automation-and-digital-twins.mdx:170` ("Not a single universal model", repeating the "Purposeful" bullet at line 150).
- **Problem:** Repetition lengthens the entries without adding information.
- **Recommended correction:** Remove or fold the passages listed; keep worked examples, exercises and summary tables, which are not repetition.

### F11. Capacitive sensors
- **Where:** `src/content/blog/logic-and-sequential-control.mdx:27`
- **Text:** "or any material (capacitive type) comes near"
- **Problem:** Capacitive sensors detect most materials, not every one; overstated.
- **Recommended correction:** "or most other materials, including non-metals (capacitive type), come near".

### F12. "Around"
- **Where:** `src/content/blog/fieldbuses-and-industrial-ethernet.mdx:155`
- **Text:** "Around $n$ data bytes it has 44 bits of fixed fields"
- **Recommended correction:** "Besides its $n$ data bytes it has 44 bits of fixed fields".

### F13. Jam latch dominance
- **Where:** `src/content/blog/programmable-logic-controllers.mdx:303`
- **Text:** "jam := NOT reset AND (jam_tmr.Q OR jam);    (* reset-dominant latch *)"
- **Problem:** The first entry (`logic-and-sequential-control.mdx:215`) recommends set-dominant latches for alarms; the reader may see a contradiction.
- **Recommended correction:** Add: "The alarm latch is reset-dominant rather than the set-dominant form the first entry recommends for alarms; that is harmless here because the jam stops the motor, which resets the timer and so removes the alarm condition."

### F14. Prerequisites from the control series not pointed to
- **Where:** `src/content/blog/pid-control-of-process-variables.mdx:58, 98`
- **Text:** "where $s$ is the Laplace variable"; "as the control series showed for a first-order plant."
- **Recommended correction:** "(introduced with the transfer function in the control series' first entry)"; link "[Feedback and System Behavior](/blog/feedback-and-system-behavior)".

### F15. Manchester coding
- **Where:** `src/content/blog/fieldbuses-and-industrial-ethernet.mdx:200`
- **Text:** "Manchester-coded, bus-powered transmission"
- **Recommended correction:** "Manchester-coded (every bit contains a transition, so the signal carries its own clock and has no direct-current component), bus-powered transmission".

### F16. Series file
- **Where:** `src/content/series/industrial-automation.md:13`
- **Text:** "the feedback ideas of the control systems series."
- **Recommended correction:** "the feedback ideas of the Foundations of Control Systems series." (and the same in the Vietnamese series file).

## Concept introduction map
| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Plant, field device, sensor, actuator, controller | logic-and-sequential-control.mdx:25 | same, 25–30 | Good. |
| Boolean variable, AND/OR/NOT | logic-and-sequential-control.mdx:66 | same, 66–72 | Good. |
| Karnaugh map, Gray code | logic-and-sequential-control.mdx:106 | same, 106 | Good. |
| Latch, seal-in, edge | logic-and-sequential-control.mdx:181 | same, 181–225 | Good. |
| IEC 61131-3, function block | logic-and-sequential-control.mdx:231 | same, 231 (briefly), full in programmable-logic-controllers.mdx:194 | Good. |
| Finite-state machine, Moore/Mealy | logic-and-sequential-control.mdx:259 | same, 259–265 | Good. |
| GRAFCET (IEC 60848), SFC | logic-and-sequential-control.mdx:359 | same; SFC in programmable-logic-controllers.mdx:360 | Good. |
| PLC, scan cycle, process image | programmable-logic-controllers.mdx:15 | same, 15, 50–65 | Good. |
| 4–20 mA loop, live zero, NE 43 | programmable-logic-controllers.mdx:139 | same, 139–149 | Good after F2/F9. |
| Quantization | programmable-logic-controllers.mdx:160 | sampling-quantization-and-data-conversion (linked) | Good. |
| OSI layers, media access | fieldbuses-and-industrial-ethernet.mdx:38 | same, 38–59 | Good. |
| RS-485, Modbus, CRC | fieldbuses-and-industrial-ethernet.mdx:69 | same, 69–90 | Good. |
| CAN, dominant/recessive, bit stuffing | fieldbuses-and-industrial-ethernet.mdx:133 | same, 133–155 | Good. |
| Manchester coding | fieldbuses-and-industrial-ethernet.mdx:200 | not introduced | F15. |
| Ethernet frame, switch queuing | fieldbuses-and-industrial-ethernet.mdx:212 | same, 212–222 | Good. |
| PTP, TSN | fieldbuses-and-industrial-ethernet.mdx:261 | same, 261–300 | Good. |
| Feedback loop, steady-state error, Laplace variable, transfer function | pid-control-of-process-variables.mdx:17, 58 | Foundations of Control Systems (linked at 17) | Good; F14 adds pointers. |
| FOPDT, integrating process | pid-control-of-process-variables.mdx:52 | same, 52–74 | Good. |
| PID forms, windup, bumpless transfer | pid-control-of-process-variables.mdx:90 | same, 90–164 | Good. |
| ISA-95 levels | networked-automation-and-digital-twins.mdx:23 | same, 23–42 | Good. |
| OPC UA address space, subscriptions, PubSub | networked-automation-and-digital-twins.mdx:54 | same, 54–110 | Good. |
| MQTT | networked-automation-and-digital-twins.mdx:110 | same, 114 | Good. |
| Zones and conduits (IEC 62443) | networked-automation-and-digital-twins.mdx:132 | same, 132–136 | Good. |
| State estimation, residual, Kalman filter | networked-automation-and-digital-twins.mdx:185 | same, and sensing-and-state-estimation (linked) | Good. |

## Versions, defaults and conventions
| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| IEC 61131-3 edition | entries 1, 2 | Yes (2013) | Fourth edition (2025) not mentioned: F4. |
| Python 3, standard library | all entries | Yes | Good. |
| 24 V DC signal convention | logic-and-sequential-control.mdx:46 | Yes | Good. |
| Analog count range 0–27 648 | programmable-logic-controllers.mdx:153 | Yes, labelled vendor-specific | Good. |
| Direct-address mapping | programmable-logic-controllers.mdx:220, 314 | Yes, vendor-specific | Good. |
| Task priority (0 highest), pre-emption | programmable-logic-controllers.mdx:113–115 | Yes | Good. |
| NE 43 levels | programmable-logic-controllers.mdx:149 | Yes | Edition and receiver thresholds: F9. |
| Modbus RTU 11-bit characters, 3.5-character gap, 1.75 ms above 19 200 bit/s | fieldbuses-and-industrial-ethernet.mdx:86, 304 | Yes | Good. |
| Classical CAN, 11-bit identifier | fieldbuses-and-industrial-ethernet.mdx:135, 155 | Yes | Good. |
| Ethernet 100 Mbit/s, untagged frames | fieldbuses-and-industrial-ethernet.mdx:212–214 | Yes | Good. |
| PID standard (ISA) form, signals in %, time in s, e = r − y | pid-control-of-process-variables.mdx:19, 92 | Yes | Good. |
| Vendor-specific PID block forms and units | pid-control-of-process-variables.mdx:114 | Yes | Good. |
| MQTT 3.1.1 and 5.0, ports 1883/8883 | networked-automation-and-digital-twins.mdx:114 | Yes | Good. |
| OPC UA port 4840, UA Binary | networked-automation-and-digital-twins.mdx:108 | Yes | Good. |
| Linearized tank outlet | networked-automation-and-digital-twins.mdx:208 | Yes | Good. |

## Series-level notes
- **Spelling:** American throughout (behavior, labeled, meter, energized); consistent.
- **Structure:** every entry has an introduction, numbered sections, five exercises with answers, a summary table and references; the closing paragraph of each correctly names the next entry.
- **Cross-reference map (checked):** 1→2 (scan, order of statements; F6), 1→4, 2→1 Section 5.2 anchor, 2→1 Section 5.3, 2→3, 2→4, 2→5 (virtual commissioning, fulfilled in 5 Section 5.5), 3→2, 3→5 (OPC UA PubSub, fulfilled), 4→1/2/3, 4→2 Section 3.3, 4→control series (F1, F14), 4→5 (virtual commissioning and model-based monitoring, fulfilled), 5→1–4, 5→3 Section 3.1 and Section 9 anchor, 5→2 Section 3.3, 5→numerical-integration-notes, 5→sensing-and-state-estimation. All resolve.
- **Control series status:** no article calls the Foundations of Control Systems series in progress or incomplete.
- **Frontmatter:** consistent category (Engineering), publishedAt 2026-10-13, seriesOrder 1–5, tags all lower-case.

## Verification log
- `npm run build:local` (before corrections): exit 0, 0 errors.
- `npm run check:links` (before corrections): 222 pages, 6324 internal references, all resolve.
- Dist checks (before): Mermaid min-widths 410, 291, 487, 234, 527, 142, 269 px (all ≤ 600); no `katex-error`; no glued inline text.
- Recomputed (Python 3):
  - All nine Python blocks re-run; the seven with printed output blocks match byte for byte; prose outputs `True`, `min 13.5 ms, max 23.5 ms, mean 18.5 ms`, `winner: 0x123` match.
  - Modbus CRC of `01 03 00 00 00 0A`: `C5 CD`, from the article's reflected (A001) routine and again from an independent MSB-first implementation of polynomial 8005 with reflected input and output, init FFFF, low byte sent first.
  - Entry 1: level-plausibility truth table and K-map; don't-care map; Exercise 1 (`B'D' + BD`, exhaustive over 16 inputs: True); timer delay bounds by brute force over event phases: PT 100/Tc 10 → 100–110 ms, PT 100/Tc 30 → 120–150 ms, PT 50/Tc 20 → 60–80 ms, PT 40/Tc 20 → 40–60 ms; mixing-tank timings by hand.
  - Entry 2: scaling (12.8 mA → 5.5 bar, 15 206.4 counts, 0.000 36 bar per count); Exercise 2 (16.80 mA, 3.20 m, −4 000 counts → 1.69 mA); Exercise 5 (321 Ω); Exercise 4 statement-order reasoning; Exercise 1 arithmetic (31 and 46 ms; the accompanying "as much as" remark was wrong, see Resolution S1).
  - Entry 3: per-device poll 27.9 ms; Exercise 1 (0.0955 ms per character, 11.65 ms per device, 117 ms, factor 2.4); CAN frame 8n + 47 + ⌊(34 + 8n − 1)/4⌋ = 135 bits at n = 8 (Davis et al. 2007), bus load 54 %; Exercise 2 bit positions; Exercise 3 (11 frames); Ethernet 6.72 µs and 123.04 µs; 5 × 123 µs ≈ 0.6 ms; Exercise 4 (12.3 µs, 36.9 µs); EtherCAT frame 432 bytes, 36.16 µs; PTP example (0.350 µs, 0.500 µs) and Exercise 5 (0.30, 1.00, error 0.10 µs).
  - Entry 4: two-point identification (t28 = 129.8 s and t63 = 329.9 s from K = 1.5, τ = 300 s, θ = 30 s); ZN and SIMC settings; Exercises 1–3; integrating-loop ζ and ωn formulas derived from the characteristic equation; Exercise 5 (ζ = 0.5, ωn = 0.025 rad/s, period 290 s, ζ = 0.35 after halving); load IAE of SIMC equals d·Ti/Kc = 360 %·s (hence identical at θ = 45 s); the claim that the ZN loop with θ = 45 s is unstable without limits (run without limits: peak error 45.8 % in 1000–2000 s, 622.6 % in 5000–6000 s); clamped windup peak 29.99999 %, so "without overshoot" holds.
  - Entry 5: residual formula (−9.29 mm for 0.001 m³/s, −4.65 mm for 0.0005 m³/s, L = 0.0274 for 8 mm); 40-seed claims re-run with seeds 0–39 and 1–40: alarms 36–49 s after the 0.001 m³/s leak and 62–102 s after the 0.0005 m³/s leak, no false alarms, as stated; Exercise 2 (100 vs 5 000 values per second); level at t = 899 s (1.705 m).
- Facts checked against sources or knowledge: NAMUR NE 43 levels and title/edition (namur.net news item and DIN Media listing; F9); IEC 61131-3 task PRIORITY with 0 highest (consistent with the standard and vendor documentation); IEC 61131-3 editions 1993, 2003, 2013 and 2025 (standards-body listing of IEC 61131-3:2025 ED4, 22 May 2025), IL deprecated in 2013 and removed in 2025, OOP features (methods, interfaces, inheritance, classes) added in 2013; PROFIBUS DP 1200 m at ≤ 93.75 kbit/s and 100 m at 12 Mbit/s; CAN about 40 m at 1 Mbit/s (commonly quoted, and stated so); EtherCAT header 2 bytes, datagram header 10 bytes, working counter 2 bytes; EtherNet/IP TCP 44818 and UDP 2222; Modbus TCP port 502 and 7-byte MBAP header; EtherTypes 0x8892 (PROFINET) and 0x88A4 (EtherCAT); ISA-95 level names and time frames (Level 4: months, weeks, days; Level 3: days, shifts, hours, minutes, seconds; Level 2 sub-second real-time, per the OPC Foundation's ISA-95 companion summary) and the Level 1/2 placement remark (already hedged in the text); OPC UA parts 2, 3, 4, 5, 6, 8, 14 and 100; ISO 23247 title; HART FSK 1200/2200 Hz at 1200 bit/s; IO-Link rates and 20 m cable.
- References checked: Mano and Ciletti 5th ed. (Pearson 2013), Cassandras and Lafortune 2nd ed. (Springer 2008), Bolton 6th ed. (Newnes 2015), Petruzella 5th ed. (McGraw-Hill 2016), John and Tiegelkamp 2nd ed. (Springer 2010), Davis, Burns, Bril and Lukkien (Real-Time Systems 35(3), 2007), Åström and Hägglund (ISA 2006), Skogestad (J. Process Control 13(4), 2003), Ziegler and Nichols (Trans. ASME 64, 1942), Seborg et al. 4th ed. (Wiley 2016), Shinskey 4th ed. (McGraw-Hill 1996), Kritzinger et al. (IFAC-PapersOnLine 51(11), 2018), Mahnke, Leitner and Damm (Springer 2009). All are real works with plausible details; none is doubtful.
- Not verified: the exact content of NE 43:2021 (behind a paywall; the text now defers to the current edition); the exact change list of IEC 61131-3:2025 beyond the removal of IL and the addition of UTF-8 strings (the series does not depend on it); years for IEC 60848, 61131-2, 62541 and 62443 (left without years, as the texts cite them as series or undated).
