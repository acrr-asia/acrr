# Series review: Industrial Automation

- Series: `industrial-automation` (5 articles, status published, 0 planned entries)
- Reviewed commit: 49941d2 (series content last changed in 699e575, the wave-1 revision; diff against e21dcc8 read in full)
- Date: 2026-10-14
- Review type: independent review (wave 2): fact-check (F), technical review (T) and series review (S) by a reviewer who did not write or revise the series
- Content hash: sha256:76d1f534200cdb3a3ac3f31c22beb7c94ed73d27cf6c6c15fa1ad72630c39623

## Summary
The series is accurate and coherent. Every Python program (ten blocks in five entries) was re-run and reproduces its printed output byte for byte, and every worked number, exercise answer and derivation that could be recomputed checks out, including the claims stated in prose (the unbounded growth of the Ziegler–Nichols loop without output limits, the 40-seed alarm ranges of the leak example). The wave-1 revision changed metadata, headings, references and prose. It changed no technical content, and the one technical wording change (Modbus 1.75 ms "recommends") is correct. No finding is blocking. Four should-fix items remain. The third entry still calls IEC/IEEE 60802 a "project", although it was published as a standard on 29 June 2026. Its IEC 61784-1 and -2 references give, undated, the titles of the 2019 editions, which IEC replaced in 2023. In the fifth entry, Exercise 4 says a smaller observer gain "doubles" the fault signature when it raises it 1.7 times. In the second entry, one sentence places the reset of the mixing-tank timer one scan late. The fourth edition of IEC 61131-3 (22 May 2025) is confirmed. Its removal of Instruction List could not be confirmed from a primary source here (see Not verified). With the four corrections the series is ready.
Findings: 0 blocking, 4 should fix, 4 optional.

## Objectives coverage
| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Express control tasks as Boolean logic and as sequential, state-based programs. | Entry 1, Sections 2–5 and Exercises 1–5; entry 2, Section 5 (LD, ST `CASE`, SFC) | Fully covered. |
| Describe how a programmable logic controller executes a program, and the languages defined for it. | Entry 2, Sections 2 (scan cycle, response time, watchdog, tasks) and 4–5 (software model, languages) | Fully covered. |
| Compare fieldbus and industrial Ethernet systems by timing, topology and determinism. | Entry 3, Sections 1–2, 3–9 and the comparison table in 7.4 | Covered. Topology gets only a short treatment (Section 2.2) and does not appear in the comparison table. That is enough for the objective, as the previous review also found. |
| Tune PID loops for typical process variables such as temperature, level, flow and pressure. | Entry 4, Sections 2–6, the simulations and the exercises | Fully covered. |
| Explain how plant data reach higher-level systems through the ISA-95 levels and OPC UA, and how a digital twin uses residuals to detect faults. (new in wave 1) | Entry 5, Sections 1–2 and 5.4–5.6; Exercises 1, 2 and 4 | Fully covered; the objective is an accurate summary of entry 5. Its closing paragraph (line 341) now maps the series back to all five objectives. |

## Findings
| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Should fix | `src/content/blog/fieldbuses-and-industrial-ethernet.mdx` | Section 9 (line 300) | Stated versions and defaults (`evidence`) | Calls IEC/IEEE 60802 a "project"; it was published as IEC/IEEE 60802-2026 on 29 June 2026 and is not in the reference list. |
| F2 | Should fix | `src/content/blog/fieldbuses-and-industrial-ethernet.mdx` | References (lines 370–371) | `evidence` | IEC 61784-1 and IEC 61784-2 are cited undated, with the titles of the 2019 editions. IEC replaced those editions in 2023 with the IEC 61784-1-x and 61784-2-x parts, titled "Industrial networks – Profiles". |
| T1 | Should fix | `src/content/blog/networked-automation-and-digital-twins.mdx` | Exercise 4 answer (line 314) | `accuracy` | "The smaller gain doubles the fault signature". The answer's own numbers give 4.6 mm → 8 mm, a factor of 1.7. |
| T2 | Should fix | `src/content/blog/programmable-logic-controllers.mdx` | Section 5.3 (line 342) | `accuracy` | Says the mix timer resets "in the scan after MIX ends". In the program shown, it resets in the same scan in which the state changes from MIX to DRAIN. |
| S1 | Optional | `src/content/series/industrial-automation.md` | Body (line 18) | Overview completeness | "the second entry notes what the 2025 edition changes". The entry notes one change, the removal of Instruction List. |
| S2 | Optional | `src/content/series/industrial-automation.md` | Body (line 14) | Prerequisites and dependencies | Names the Foundations of Control Systems series as a prerequisite without linking it. |
| T3 | Optional | `src/content/blog/networked-automation-and-digital-twins.mdx` | Section 5.6 (line 260) | Notation and depth (`consistency`) | $k$ is the outflow coefficient and, in the same sentence, the time-step index ($e_k$, $h_k$). |
| F3 | Optional | `src/content/blog/pid-control-of-process-variables.mdx` | Introduction (line 15) | `evidence` | "in the great majority of loops" is a quantitative claim with no source. |

### F1. IEC/IEEE 60802 is a published standard
- **Where:** `src/content/blog/fieldbuses-and-industrial-ethernet.mdx:300`, section "9. Time-Sensitive Networking"
- **Text:** "The joint IEC/IEEE 60802 project defines a TSN profile for industrial automation that selects among the options."
- **Problem:** The IEEE 802.1 TSN task group page for IEC/IEEE 60802 (1.ieee802.org/tsn/iec-ieee-60802/, fetched) shows "Status: Published Standard (2026-06-29)" and "Document: IEC/IEEE 60802-2026". An IEEE 802.1 note from July 2026 (ieee802.org/1/files/public/docs2026/60802-blog-post-0726-v01.pdf, fetched) also announces the publication of the "IEC/IEEE 60802 TSN Profile for industrial automation" and says it is available from the IEEE and IEC stores. Calling it a "project" is out of date. The wave-1 author flagged this item for checking.
- **Recommended correction:** Replace the sentence with "The joint standard IEC/IEEE 60802, published in 2026, defines a TSN profile for industrial automation that selects among the options." Add to the References, in alphabetical position after IEC 61784-2: `IEC/IEEE 60802-2026, *Time-Sensitive Networking Profile for Industrial Automation*, International Electrotechnical Commission and IEEE, 2026.` Before pasting, the author should confirm the exact title against the IEEE or IEC store listing. The title given here is the one on the IEEE 802.1 pages.

### F2. IEC 61784 references give superseded titles
- **Where:** `src/content/blog/fieldbuses-and-industrial-ethernet.mdx:370-371`, "References"
- **Text:** "IEC 61784-1, *Industrial communication networks – Profiles – Part 1: Fieldbus profiles*, International Electrotechnical Commission." and "IEC 61784-2, *Industrial communication networks – Profiles – Part 2: Additional fieldbus profiles for real-time networks based on ISO/IEC/IEEE 8802-3*, International Electrotechnical Commission."
- **Problem:** The second title is that of IEC 61784-2:2019 (fourth edition, 2019-04-09; Standards Council of Canada catalogue, fetched), which that catalogue marks as replaced. In 2023 IEC published IEC 61784-2-0:2023, "Industrial networks – Profiles – Part 2-0: Additional real-time fieldbus profiles based on ISO/IEC/IEEE 8802-3 – General concepts and terminology" (22 March 2023; GlobalSpec reference listing, fetched). It also published IEC 61784-1-0:2023, "Industrial networks – Profiles – Part 1-0: Fieldbus profiles – General concepts and terminology" (2023-03-23; SCC catalogue, fetched). Wave 1 left the references undated on the grounds that "the text relies on features present in the current editions". That reasoning does not hold for a title that no current edition carries, and the reader cannot tell which document is meant. The body text (lines 193 and 226) is still correct as a description of the IEC 61784 family.
- **Recommended correction:** Cite the current documents: `IEC 61784-1-0:2023, *Industrial networks – Profiles – Part 1-0: Fieldbus profiles – General concepts and terminology*, International Electrotechnical Commission, 2023.` and `IEC 61784-2-0:2023, *Industrial networks – Profiles – Part 2-0: Additional real-time fieldbus profiles based on ISO/IEC/IEEE 8802-3 – General concepts and terminology*, International Electrotechnical Commission, 2023.` Alternatively, keep the present titles and date them to the editions they belong to (for Part 2: `IEC 61784-2:2019, ..., 4th ed., International Electrotechnical Commission, 2019`), after checking the Part 1 edition in the same way.

### T1. "Doubles" overstates the gain change
- **Where:** `src/content/blog/networked-automation-and-digital-twins.mdx:314`, Exercise 4 answer
- **Text:** "The smaller gain doubles the fault signature but also lets the twin drift further when the model is imperfect."
- **Problem:** The answer computes $\bar r \approx -4.6$ mm at $L = 0.05$ and chooses $L \approx 0.027$ so that $|\bar r| = 8$ mm. 8/4.65 = 1.72 (recomputed: $-0.25/(1 - 0.996 \times 0.95) = -4.647$ mm; $1 - L = 0.96875/0.996 = 0.97264$, $L = 0.0274$). The factor is 1.7, not 2.
- **Recommended correction:** "The smaller gain enlarges the fault signature by about 70 % (from 4.6 to 8 mm) but also lets the twin drift further when the model is imperfect."

### T2. Scan in which the mix timer resets
- **Where:** `src/content/blog/programmable-logic-controllers.mdx:342`, Section 5.3
- **Text:** "In the scan in which the state changes to MIX, the timer is called with `IN` TRUE and starts; in the scan after MIX ends, it is called with `IN` FALSE and resets, ready for the next batch."
- **Problem:** In `MixingTank` the `CASE` statement (transitions) runs before the timer call. In the scan in which `mix_tmr.Q` is TRUE, the `CASE` changes `state` to DRAIN, and the timer call later in the same scan has `IN := (state = MIX)` = FALSE, so the timer resets in that scan. "The scan after MIX ends" reads as the following scan. The first half of the sentence uses the same-scan logic, so the two halves do not match. The entry stresses that statement order sets timing (Section 2.1, Exercise 4), so the sentence should be exact.
- **Recommended correction:** "In the scan in which the state changes to MIX, the timer is called with `IN` TRUE and starts; in the scan in which the state changes from MIX to DRAIN, it is called with `IN` FALSE and resets, ready for the next batch."

### S1. Overview: "what the 2025 edition changes"
- **Where:** `src/content/series/industrial-automation.md:18`
- **Text:** "The programming examples follow the third edition of IEC 61131-3 (2013), and the second entry notes what the 2025 edition changes."
- **Problem:** Entry 2 (lines 17, 194, 356) mentions one change ("among its changes, removes Instruction List"), not an account of the changes. Standards 6.5: the overview must not promise more than the entries deliver.
- **Recommended correction:** "... and the second entry notes that the 2025 edition removes Instruction List."

### S2. Overview: prerequisite series not linked
- **Where:** `src/content/series/industrial-automation.md:14`
- **Text:** "The entry on proportional–integral–derivative (PID) control also uses the feedback ideas of the Foundations of Control Systems series."
- **Recommended correction:** Link the series name: `[Foundations of Control Systems](/series/foundations-of-control-systems)`, as entry 1 (line 19) and entry 4 (line 17) do. The Vietnamese overview has to be updated in any case (see Series-level notes).

### T3. Symbol $k$ used twice
- **Where:** `src/content/blog/networked-automation-and-digital-twins.mdx:260`
- **Text:** "With the twin's state error $e_k = h_k - \hat h_k$, a per-step decay factor $a = 1 - k\,\Delta t/A = 0.996$ ..."
- **Recommended correction:** Write the step index as $j$ ($e_j = h_j - \hat h_j$), or rename the outflow coefficient in the prose to match the code's `K_OUT` (for example $c$), in Section 5.6 (lines 207, 213, 260 and 268).

### F3. "Great majority of loops" not attributed
- **Where:** `src/content/blog/pid-control-of-process-variables.mdx:15`
- **Text:** "In process plants the answer is computed, in the great majority of loops, by a **proportional–integral–derivative** (PID) **controller**."
- **Recommended correction:** Attribute it to the reference already listed: "..., in the great majority of loops according to Åström and Hägglund (see References), ...". Or drop "in the great majority of loops" and write "in most loops". The claim is widely accepted, so this is optional.

## Concept introduction map
| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| Boolean variable, AND/OR/NOT, truth table | `logic-and-sequential-control.mdx:66` | Same place (2.1), with relay equivalents | Good: built from first principles, as the overview promises. |
| Karnaugh map, Gray code, don't-care | `logic-and-sequential-control.mdx:102` | `:106`, `:160` | Good. |
| Latch, seal-in, edge | `logic-and-sequential-control.mdx:181` | `:177–225` | Good. |
| Timer function blocks (TON/TOF/TP) | `logic-and-sequential-control.mdx:231` | Same place, with "function block" defined | Good. |
| Finite-state machine, Moore/Mealy | `logic-and-sequential-control.mdx:259` | `:259–265` | Good. |
| PLC, scan cycle, input/output image | `programmable-logic-controllers.mdx:15` | `:15`, `:50–62` | Good. |
| 4–20 mA loop, NE 43 | `programmable-logic-controllers.mdx:139` | `:139–149` | Good. |
| IEC 61131-3 software model, POU | `programmable-logic-controllers.mdx:194` | `:194–212` | Good. |
| OSI layers, media access, CRC | `fieldbuses-and-industrial-ethernet.mdx:38` | `:38–59`, `:90` | Good; CRC expanded in the layer table, explained in 3.2. |
| Ethernet frame, switch queuing, VLAN | `fieldbuses-and-industrial-ethernet.mdx:212` | `:212–222` | Good. |
| PTP offset/delay | `fieldbuses-and-industrial-ethernet.mdx:261` | `:261–289` | Good. |
| Feedback loop, Laplace variable, proportional offset | `pid-control-of-process-variables.mdx:17`, `:58`, `:98` | Foundations of Control Systems: `introduction-to-control-systems.mdx:35–37, 50–51, 62`; `feedback-and-system-behavior.mdx:65–73` (checked in the current files) | Good: explicit back-references, all accurate. |
| FOPDT model, dead time | `pid-control-of-process-variables.mdx:52` | Same place | Good. |
| ISA-95 levels, IT/OT | `networked-automation-and-digital-twins.mdx:23` | `:23–46` | Good. |
| OPC UA address space, subscriptions | `networked-automation-and-digital-twins.mdx:54` | `:50–104` | Good. |
| State estimation, residual | `networked-automation-and-digital-twins.mdx:184` | Same place, linked to `sensing-and-state-estimation` | Good. |

## Versions, defaults and conventions
| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| IEC 61131-3 edition (2013 third edition; fourth 2025) | Entries 1 (`:231`, `:422`) and 2 (`:17`, `:194`, `:356`, `:445–447`); overview `:18` | Yes | Consistent. The fourth edition's date (22 May 2025) is verified. Its removal of IL is not verified from a primary source (see Not verified). |
| Python 3, standard library | Opening of every entry; overview `:18` | Yes | All programs run on Python 3.13 with the output shown. |
| Signals in percent of span; $e = r - y$; time in s | Entry 4, `:19` | Yes | Applied consistently. |
| Scaling counts (27 648) | Entry 2, `:153` | Yes, as vendor-specific | Good. |
| Modbus t3.5 above 19 200 bit/s | Entry 3, `:304` | Yes, as a recommendation | Correct wording (wave 1). |
| Classical CAN, 11-bit identifier | Entry 3, `:155–163` | Yes | Good; CAN FD distinguished at `:187`. |
| Ethernet at 100 Mbit/s and 1 Gbit/s | Entry 3, `:214`, Exercise 4 | Yes | Good. |
| PTP symmetric path | Entry 3, `:277`, `:289` | Yes | Good. |
| TSN profile status | Entry 3, `:300` | Stated, but out of date | F1. |
| PID form (standard/ISA) and units | Entry 4, `:90–114` | Yes | Good. |
| ISA-95 vs Purdue Level 1/2 boundary | Entry 5, `:42`, Exercise 1 | Yes | Good. |
| MQTT versions; OPC UA port 4840 | Entry 5, `:108`, `:114` | Yes | Good. |

## Series design
**Purpose, audience and scope.** The rewritten overview states the reader (basic electrical engineering), the assumptions (no digital logic or PLC knowledge; the control series for entry 4), the scope and, through five verb-first objectives, what the reader can do at the end. Each objective is met by named entries (table above). The new fifth objective is an accurate summary of entry 5.

**Sequence and rationale.** The order goes from logic, to the controller that executes it, to the networks that extend its I/O, to continuous loops through that I/O, to the systems above. The overview now explains this order (`:16`), and entry 5 restates it at the end (`:341`). No entry would serve the reader better moved, split or merged.

**Prerequisites and dependencies.** Nothing depends on a later entry. Forward references are promises ("the second entry shows ...", "the fifth entry returns to it as virtual commissioning"), and all are kept. The control-series dependency is explicit and linked in entries 1 and 4. The overview names it without a link (S2).

**Notation and depth.** Shared symbols agree: `stop_ok`, seal-in, TON/TOF/TP, input/output image, $e = r - y$, percent of span. Entry 1's $T_c$ becomes $T_\text{scan}$ in entry 2, which defines its own symbol for the PLC case. Symbols reused across entries with different meanings ($\theta$ for PTP offset in entry 3 and dead time in entry 4; $L$ for the low switch in entry 1 and the observer gain in entry 5) are each defined locally and cause no confusion. The one clash within an entry is T3. Depth is even: every entry has worked examples with run code, five exercises with answers, a summary table and references.

**Overview completeness.** The overview now meets standards 6.5: sequence rationale, reader and prerequisites, how the entries connect, shared conventions, five objectives, and a 143-character description. Its one overstatement is S1.

## Series-level notes
- **Cross-reference map (all checked against the target text):** entry 2 → entry 1 Sections 2.1, 5.2 (anchor), 5.3; entry 3 → entry 2 Section 2.2 and its own Sections 3.2, 3.3, 6, 6.2, 8, 9; entry 4 → entry 2 Section 3.3, the control series' first and second entries, its own Sections 2.2, 2.3, 5.2–5.4, 6.5, 6.6; entry 5 → entry 3 Section 3.1 and `#9-time-sensitive-networking`, entry 2 Section 3.3, its own Sections 2.2, 4, 5.1; entry 1 → its own Sections 1.3, 2.4, 3.2, 3.4, 4.3, 5.2. All resolve and say what is claimed. Entry 1's promise (line 225) that entry 2 shows "why the order of statements within one evaluation matters" is kept by entry 2 Section 2.1 (line 67) and Exercise 4.
- **Terminology:** consistent (setpoint, scan cycle, data sets, American spelling). The six `contractions` warnings on "don't-care" in entry 1 are justified (it is the established term, defined in bold at line 160).
- **Vietnamese translation:** `src/content/series/vi/industrial-automation.md` still has the old description, four objectives and the old body (last changed in a92a94a). Translations are not reviewed. The wave-1 audit already marks this translation as needing an update. When this review's corrections are applied, the update should cover the wave-1 overview changes and S1/S2 together. No article in the series has a Vietnamese translation.

## Verification log
- Build: not run (parallel reviewers). Used the post-wave-1 build in `/tmp/claude-0/b2` (SITE_URL=https://acrr.asia). It is current for this scope: the wave-1 strings "remote terminal unit mode" (entry 3) and the fifth objective (overview) are present.
- `node scripts/check-links.mjs /tmp/claude-0/b2`: 314 pages, 9667 internal references, all resolve.
- Rendering in `/tmp/claude-0/b2/blog/<slug>.html`: `katex-error` count 0 in all five pages. Mermaid min-widths 410 (entry 1); 487, 291 (entry 2); 234 (entry 3); 527 (entry 4); 142, 269 px (entry 5), all ≤ 600 px. No letter or punctuation glued to `<span`, `<strong>`, `<a ` or `<code`.
- `npm run -s eos -- lint industrial-automation`: 6 files, 0 errors, 6 warnings (the justified "don't-care" contractions in entry 1), 94 suggestions (acronym false positives, undated standard series, sentence length; reviewed, none re-reported).
- `npm run -s eos -- syntax` on the six files: "All files compile."
- Code re-run with `python3 -I` (Python 3.13), each block extracted from the source. Entry 4's two blocks were run as one script, because the second calls `run`. Output identical to the text for all ten blocks:
  - entry 1: `True`; the four transition lines;
  - entry 2: `min 13.5 ms, max 23.5 ms, mean 18.5 ms`; the four scaling lines;
  - entry 3: CRC `C5 CD`, 0.573/4.58/14.32 ms, 27.9 ms per device, 279 ms; `winner: 0x123`; 111/135 bits and 54 % load;
  - entry 4: the six tuning/result lines and both windup lines;
  - entry 5: the three trace lines and `leak alarm at t = 941 s`.
- Claims stated in prose, re-run:
  - Entry 4, Section 5.3: the Ziegler–Nichols loop with 45 s dead time and no output limits is unstable. Confirmed: the peak-to-peak envelope grows in every 500 s window, from 25.3/−6.3 % to 88.1/−73.7 %.
  - Entry 4, Section 5.4: "approaches 30 % from below without overshoot". Confirmed: maximum PV 29.99999 %.
  - Entry 5, Section 5.6 and Exercise 4, 40-seed ranges. With seeds 0–39 (and 1–40): alarms 36–49 s after the leak, none before it; the 0.0005 m³/s leak gives alarms 62–102 s after it. Matches the text.
- Recomputed by hand or with Python:
  - Entry 1: Karnaugh results (Fault = $\overline{L}M + \overline{M}H$; $Y = \overline{M}$ vs $\overline{M}\,\overline{H}$); Exercise 1 ($\overline{B}\,\overline{D} + BD$); Exercise 2 (De Morgan); timer bounds 100–110 ms, 120–150 ms, Exercise 4 60–80 / 40–60 ms; mixing-tank timings 37.5 s, 87.0/87.5 s, 2-point overshoot.
  - Entry 2: response bounds; scaling 5.5 bar, 15 206.4 counts, 0.000 36 bar/count; Exercise 1 31/46 ms and 10/31 = 32 %; Exercise 2 16.80 mA, 3.20 m, 1.69 mA; Exercise 4 statement-order trace (correct); Exercise 5 6.75 V, 321 Ω.
  - Entry 3: 0x123/0x124 binary; Exercise 2 bit positions; CAN fixed fields 44 + 3 bits and the stuffing bound (matches Davis et al.'s $g + 8s + 13 + \lfloor (g + 8s - 1)/4 \rfloor$ with $g = 34$); Ethernet 6.72/123.04 µs; 5 switches ≈ 0.6 ms; EtherCAT 432 bytes, 36.16 µs; PTP example and Exercise 5; Exercise 1 0.0955 ms, 11.65 ms, 116.5 ms, ×2.4; Exercise 3 540 µs, 11 frames; Exercise 4 12.3/36.9 µs.
  - Entry 4: 28.3 % = $1 - e^{-1/3}$; $\tau$ = 300.1 s, $\theta$ = 29.8 s; ZN 6.00/100 s; SIMC 3.33/240 s; Exercises 1–3; level SIMC 2.0/40 s and 0.19/420 s with $k'K_cT_i$ = 4.0; characteristic equation and $\omega_n$, $\zeta$ derived; Exercise 5 0.025 rad/s, 290 s, $\zeta$ = 0.354.
  - Entry 5: steady states 1.25/1.75 m, $A/k$ = 250 s; residual recursion derived from the code ($r = a(1-L)r - d$), $\bar r$ = −9.29 mm; Exercise 2 100 vs 5 000 values/s; Exercise 4 −4.65 mm, $L$ = 0.0274 (T1).
- Fact-check, verified (sources fetched in this review):
  - IEC 61131-3:2025, Ed. 4.0, published 22 May 2025 (Standards Norway listing; ANSI webstore listing: "revises IEC 61131-3 Ed. 3.0 (2013)"; UTF-8 strings; Annex B lists added/removed/deprecated features).
  - NAMUR NE 43 revised edition 2021-07-26 (previous 2003-02-03) under the cited title, adding a safety margin for detection in control systems (namur.net news item).
  - IEC/IEEE 60802-2026 published 2026-06-29 (F1).
  - IEC 61784-2:2019 fourth edition and its replacement status; IEC 61784-1-0:2023 and 61784-2-0:2023 titles (F2).
  - IEC 61131-2:2017 edition 4.0 and title (SCC/VDE listings in search results).
  - ISO 11898-1:2024 title (several national catalogue listings in search results).
  - Petruzella, *Programmable Logic Controllers*, 5th ed., McGraw-Hill Education, 13 January 2016 (bookseller record, ISBN 9780073373843).
- Fact-check, consistent with domain knowledge but not fetched in this pass: Modbus data model, function codes, 247 addresses, 11-bit characters, MBAP 7-byte header and port 502; EtherNet/IP ports 44818/2222; EtherTypes 0x8892 and 0x88A4; HART Bell 202 frequencies; IEC 61158-2 MBP 31.25 kbit/s; IO-Link rates and 20 m; OPC UA node classes, security modes, port 4840; MQTT ports and QoS levels; IEC 61131-3 task attributes, priority 0 highest; standard FB interfaces; Davis et al. (2007) bibliographic details; Kritzinger et al. (2018), Skogestad (2003), Ziegler and Nichols (1942) bibliographic details; ZN reaction-curve and SIMC formulas.
- Not verified:
  - **Removal of Instruction List by IEC 61131-3:2025** (`programmable-logic-controllers.mdx:17, 194, 356, 445, 447`; overview `:18` by implication). The standard's catalogue abstracts (ANSI, Standards Norway) mention only UTF-8 strings and an Annex B list of added, removed and deprecated features, without naming IL. The IEC preview was not reachable as a document. Supporting secondary sources: a 2016 trade article (computer-automation.de, "The further development of IEC 61131") reporting the committee's decision "to remove the 'Instruction List' programming language from the standard with the future 4th edition", and the Wikipedia article (uncited statement). Recommended: the author confirms against the standard's Annex B or foreword (IEC webstore preview). If that cannot be done, qualify the statements, for example "the fourth edition, which according to its working group removes Instruction List". The previous review reported confirming this on the IEC listing; that confirmation could not be reproduced here.
  - Modbus serial-line V1.02 wording for the 1.75 ms recommendation (`fieldbuses-and-industrial-ethernet.mdx:304`): modbus.org PDF fetch failed. The wording matches the reviewer's knowledge of Section 2.5.1.1 and the wave-1 author's fetched quotation.
  - PROFIBUS DP segment lengths (1200 m at ≤93.75 kbit/s, 100 m at 12 Mbit/s) and the 40 m CAN length at 1 Mbit/s (`fieldbuses-and-industrial-ethernet.mdx:69, 151`): standard published values, not fetched. The text qualifies the CAN figure as "commonly quoted".
  - Book editions and years of Bolton (6th ed., 2015), Cassandras and Lafortune (2nd ed., 2008), Mano and Ciletti (5th ed., 2013), John and Tiegelkamp (2nd ed., 2010), Åström and Hägglund (2006), Seborg et al. (4th ed., 2016), Shinskey (4th ed., 1996), Mahnke et al. (2009): consistent with the reviewer's knowledge, not fetched.

## Resolution
- F1 (Should fix): fixed - "The joint standard IEC/IEEE 60802, published in 2026, defines a TSN profile ..." (`src/content/blog/fieldbuses-and-industrial-ethernet.mdx:300`); reference added: `IEC/IEEE 60802:2026, *Time-sensitive networking profile for industrial automation*` (`:372`), title and designation checked against the Standards Council of Canada catalogue record (scc-ccn.ca/standardsdb/standards/2058859).
- F2 (Should fix): fixed - references replaced by IEC 61784-1-0:2023 and IEC 61784-2-0:2023 with their current titles (`src/content/blog/fieldbuses-and-industrial-ethernet.mdx:370-371`); Part 1-0 title and date (2023-03-24) checked on the IEC webstore (webstore.iec.ch/publication/83453), Part 2-0 title on AFNOR and GlobalSpec catalogue listings.
- T1 (Should fix): fixed - "enlarges the fault signature by about 70% (from 4.6 to 8 mm)" (`src/content/blog/networked-automation-and-digital-twins.mdx:314`); recomputed with `python3 -I`: r = -4.6468 mm, 8/4.6468 = 1.72, L = 0.0274.
- T2 (Should fix): fixed - "in the scan in which the state changes from MIX to DRAIN, it is called with `IN` FALSE and resets" (`src/content/blog/programmable-logic-controllers.mdx:342`).
- Not verified (IL removal in IEC 61131-3:2025): qualified - the IEC-derived abstract of IEC 61131-3:2025 (AFNOR store listing, fetched) lists ST, LD, FBD and SFC, does not name Instruction List, and refers removed features to Annex B, which could not be read. Every statement now says what that source supports: "its published scope no longer lists Instruction List among the standard's languages" (`programmable-logic-controllers.mdx:17, 194, 356, 447`; overview `src/content/series/industrial-automation.md:18`). No text now asserts the removal outright.

Optional findings applied: S1 (overview line 18, now names the one change, with the same qualified wording), S2 (overview line 14 links Foundations of Control Systems), T3 (step index renamed to $j$, `networked-automation-and-digital-twins.mdx:260`; $k$ kept for the outflow coefficient, the only other use of either symbol in the prose), F3 (`pid-control-of-process-variables.mdx:15`, "in most loops"). Not applied: none.

Resolved by the wave-1 author on 2026-10-15; awaiting the reviewer's resolution check.

## Resolution check
QA editor (final gate), 2026-10-15, against the current files; build `/tmp/claude-0/b9`.
- F1 (Should fix): confirmed - `fieldbuses-and-industrial-ethernet.mdx:300` calls IEC/IEEE 60802 a standard published in 2026; `IEC/IEEE 60802:2026` is in the References (`:372`) in alphabetical position.
- F2 (Should fix): confirmed - `:370-371` cite IEC 61784-1-0:2023 and IEC 61784-2-0:2023 with the current "Industrial networks – Profiles" titles; the body text (`:193`, `:226`) still describes the IEC 61784 family correctly.
- T1 (Should fix): confirmed - `networked-automation-and-digital-twins.mdx:314` reads "enlarges the fault signature by about 70% (from 4.6 to 8 mm)"; recomputed with `python3 -I`: r = -4.6468 mm at L = 0.05, 8/4.6468 = 1.72, L = 0.0274.
- T2 (Should fix): confirmed - `programmable-logic-controllers.mdx:342` now places the reset in the scan in which the state changes from MIX to DRAIN, which matches the `CASE`-before-timer order of `MixingTank`.
- Not verified (IL removal): confirmed as qualified - lines 17, 194, 356, 447 of entry 2 and overview line 18 state only that the published scope of the 2025 edition no longer lists Instruction List; no sentence asserts the removal outright.
- Optional S1, S2, T3, F3: confirmed applied (overview lines 14 and 18; step index $j$ at entry 5 line 260 with $k$ kept for the outflow coefficient; "in most loops" at entry 4 line 15).
- Checks: `eos lint industrial-automation` 0 errors, 6 warnings (the "don't-care" contractions in entry 1, justified in its revision log); `eos syntax` on the six files: all compile; `check-links` on the build: 314 pages, all internal links resolve; `eos validate-site --json`: no issue on any page of this series (all 29 issues are `/vi/` pages). All ten Python blocks re-run: output identical to the text.
- Reopened: none.
