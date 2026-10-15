# Series review: Embedded and Real-Time Systems

- Series: `embedded-and-real-time-systems` (5 articles, status published, 0 planned entries)
- Reviewed commit: 9232ed9
- Date: 2026-10-14
- Reviewer: independent reviewer for wave 2 (fact-check, technical review, series review). The reviewer did not author or revise any text in this scope.
- Content hash: sha256:344fdf1b66249bee3edd495dc8fdb973ba4fff5e4eecddf7c15fe6c763a8536f

## Summary

The series is technically sound and ready to publish after three should-fix corrections; nothing is blocking. Every program in the five entries was recompiled or rerun and reproduces its printed output. The exception is the wake-up experiment of the fifth entry, which by design gives different numbers on every run; a rerun showed the same pattern. Every worked number and exercise answer was recomputed and is correct, and the 25 distinct references are real works; those fetched in this pass have correct details, the rest are listed in the verification log. The wave-1 revision changed prose, headings, descriptions and reference formatting but no technical content, and it introduced no error.

The three should-fix findings:
- the Arm reference, cited in three entries, still has no issue or year (now verified: DDI 0403E.e, 2021);
- the Mars Pathfinder account in the fourth entry is a dated factual claim with no source;
- the new sequence paragraph of the series overview says that every entry removes a limit of the previous one, which is not true of the third entry, and it says the second entry replaces the superloop's waiting "with polling", although the superloop already polls.

The reworded objective 4 matches what the fourth and fifth entries deliver.
Findings: 0 blocking, 3 should fix, 6 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Describe how a microcontroller's CPU, memory, timers, converters and peripherals work together. | Entry 1, §§2–7 | Met: core, flash/SRAM, memory map, startup, clocks, timers, GPIO, ADC, firmware layers. |
| Choose between polling, interrupts and DMA for moving sensor data. | Entry 2, §§2–6 (decision table and four worked decisions in §6) | Met. |
| Compare serial buses (UART, SPI, I2C, CAN) by topology, speed and error handling. | Entry 3, §§2–6 (comparison table in §6) | Met. |
| Explain real-time scheduling, calculate worst-case response times and check them against measurements. | Entry 4, §§1–4 (RM/DM, utilization bound, RTA, EDF, blocking, worked design); entry 5, §§3.3–3.4, 4.1, 7 | Met. The wave-1 wording ("check them against measurements") matches entry 5 §3.2 and §4.1, which argue that measurement alone cannot establish a worst case. The wave-1 flag is confirmed. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Should fix | `src/content/blog/inside-a-microcontroller.mdx`, `interrupts-polling-and-dma.mdx`, `measuring-timing-latency-and-resource-use.mdx` | References (lines 455, 393, 461) | evidence | Arm DDI 0403 is cited without issue or year; the verified current issue is DDI 0403E.e (2021). |
| F2 | Should fix | `src/content/blog/real-time-operating-systems-and-scheduling.mdx` | §3.3 (line 295) | evidence | The Mars Pathfinder account (1997, resets, priority inheritance fix) has no source. |
| S1 | Should fix | `src/content/series/embedded-and-real-time-systems.md` | Body, second paragraph (line 15) | accuracy | "each one removing a limit that the previous one exposes" is false for the third entry, and "replaces that waiting with polling" misdescribes the second entry. |
| F3 | Optional | `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx` | References (line 416) | evidence | The Di Natale et al. title omits its subtitle "Theory and Practice" (verified). |
| S2 | Optional | `src/content/series/embedded-and-real-time-systems.md` | Body (lines 13–17) | purpose | The overview does not say what the series leaves out. |
| S3 | Optional | `src/content/blog/inside-a-microcontroller.mdx` | Opening (line 15) | consistency | "how to check by measurement that it does" restates the claim that objective 4 was reworded to avoid. |
| T1 | Optional | `src/content/blog/interrupts-polling-and-dma.mdx` | §3.4 (line 119), §6 (line 334) | structure | "task" is used in its RTOS sense two entries before tasks are introduced. |
| T2 | Optional | `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx` | §5.1 (line 200) | structure | "characteristic impedance" and "reflections" are used without a gloss. |
| T3 | Optional | `src/content/blog/interrupts-polling-and-dma.mdx` | Opening (line 21) | language | "data shared between code that can interrupt itself" is imprecise. |

### F1. Arm reference without issue or year
- **Where:** `src/content/blog/inside-a-microcontroller.mdx:455`, `src/content/blog/interrupts-polling-and-dma.mdx:393`, `src/content/blog/measuring-timing-latency-and-resource-use.mdx:461`, section "References"
- **Text:** "Arm Limited, *Armv7-M Architecture Reference Manual*, document ARM DDI 0403."
- **Problem:** Standards 7.3 requires a year for every reference, and 7.2 requires the edition or issue; the wave-1 logs flagged this for the fact-checker (A1). The front matter of the manual reads "Armv7-M Architecture Reference Manual", "ARM DDI 0403E.e (ID021621)", Issue E.e, 15 February 2021. Arm's own documentation pages returned no content when fetched, so this was read from a copy of the PDF at kib.kiev.ua (`DDI0403E_e_armv7m_arm.pdf`, fetched 2026-10-14); the same index lists issues C, D, E.b, E.c, E.d and E.e. The content these entries cite (address map regions, exception entry, PRIMASK and BASEPRI, the optional DWT cycle counter) is the same in every E issue, so citing the current issue is safe.
- **Recommended correction:** in all three entries, replace the entry with:
  `- Arm Limited, *Armv7-M Architecture Reference Manual*, ARM DDI 0403E.e, 2021.`

### F2. Mars Pathfinder account without a source
- **Where:** `src/content/blog/real-time-operating-systems-and-scheduling.mdx:295`, section "3.3 Priority inversion"
- **Text:** "A widely reported case occurred on the Mars Pathfinder lander in 1997, whose computer repeatedly reset itself because a high-priority task was kept waiting this way; the fix was to enable priority inheritance on the mutex concerned."
- **Problem:** This is a dated historical claim, and standards 7.2 does not allow it to stand without a source; "widely reported" is not a source (wave-1 flag A1). The substance is correct. G. E. Reeves of the Jet Propulsion Laboratory gave a first-hand account in an email of 15 December 1997 (copy fetched 2026-10-14 at https://www.cs.unc.edu/~anderson/teach/comp790/papers/mars_pathfinder_long_version.html). In it:
  - the high-priority bus distribution task (`bc_dist`) was blocked on a semaphore held by the low-priority ASI/MET task while medium-priority tasks ran;
  - the scheduler task then detected the overrun, and the computer reset;
  - the fix was a global setting that created those semaphores with priority inheritance enabled.
- **Recommended correction:** attribute the account and add a reference. Replace the sentence with:
  "A widely cited case occurred on the Mars Pathfinder lander in 1997. According to the account of G. E. Reeves of the Jet Propulsion Laboratory, its computer repeatedly reset itself because a high-priority task was kept waiting this way, and the fix was to enable priority inheritance on the semaphore concerned."
  Add to the references, in alphabetical order (after Liu and Layland):
  `- G. E. Reeves, account of the Mars Pathfinder resets, email of 15 December 1997, Jet Propulsion Laboratory.`
  If a primary email account is not acceptable to the author, delete the sentence. The paragraph's argument does not depend on it.

### S1. Overview sequence paragraph misdescribes two entries
- **Where:** `src/content/series/embedded-and-real-time-systems.md:15`, body, second paragraph (new in wave 1)
- **Text:** "The entries follow data through an embedded system and then turn to the question of time, each one removing a limit that the previous one exposes. ... The second replaces that waiting with polling, interrupts and direct memory access (DMA) ... The third follows data off the chip over four serial buses ..."
- **Problem:**
  1. The third entry does not remove a limit exposed by the second. The second entry ends by handing over to buses as the next topic (`interrupts-polling-and-dma.mdx:389`). The limit it does expose, "they leave the processing work in a single main loop, where long and short jobs still delay each other" (`:336`), is removed by the fourth entry. Standards 6.5 forbids an overview that promises what the entries do not deliver.
  2. The superloop's waiting is already periodic polling. The second entry says so ("Periodic polling: the program checks the flag once per pass of a loop ... as in the superloop of the first entry", `interrupts-polling-and-dma.mdx:50`). So "replaces that waiting with polling" is self-contradictory.
- **Recommended correction:** replace the paragraph with:
  "The entries follow data through an embedded system and then turn to the question of time. The first entry defines the timing vocabulary of the whole series (events, deadlines, latency and jitter) and the parts of a microcontroller, and ends with the simplest firmware structure, the superloop, in which every event waits for the rest of the loop. The second analyzes the polling that the superloop performs and shows how interrupts and direct memory access (DMA) let hardware events be handled when they occur, with what each method costs in latency and processor time. The third follows data off the chip over four serial buses: the universal asynchronous receiver-transmitter (UART), the Serial Peripheral Interface (SPI), Inter-Integrated Circuit (I2C) and the Controller Area Network (CAN). The fourth removes the limit the second leaves, processing that still runs in one loop, by organizing it into prioritized tasks under a real-time operating system, and calculates whether every deadline is met in the worst case. The fifth measures execution time, latency, jitter, processor load and memory use on real hardware, and checks the calculation against those measurements."
  Update `src/content/series/vi/embedded-and-real-time-systems.md` accordingly.

### F3. Di Natale et al. title incomplete
- **Where:** `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx:416`
- **Text:** "M. Di Natale, H. Zeng, P. Giusto and A. Ghosal, *Understanding and Using the Controller Area Network Communication Protocol*, Springer, 2012."
- **Problem:** Springer's book page (link.springer.com/book/10.1007/978-1-4614-0314-2, fetched 2026-10-14) gives the subtitle "Theory and Practice"; the authors, publisher (Springer New York) and year (2012) are correct. This settles the item that wave 1 left unverified.
- **Recommended correction:** `*Understanding and Using the Controller Area Network Communication Protocol: Theory and Practice*, Springer, 2012.`

### S2. Scope exclusions not stated
- **Where:** `src/content/series/embedded-and-real-time-systems.md:13–17`
- **Text:** The body states the reader, the prerequisites, the sequence and the conventions, but not what is left out.
- **Problem:** The series-review dimension "Purpose, audience and scope" asks for what the series leaves out. Standards 6.5 does not require it, so this is optional.
- **Recommended correction:** append to the first paragraph: "It treats single-core microcontrollers; multicore scheduling, embedded Linux, the API of any particular kernel, circuit design and safety certification are outside its scope."

### S3. Entry 1 opening repeats the overclaim that objective 4 removed
- **Where:** `src/content/blog/inside-a-microcontroller.mdx:15`
- **Text:** "how their software is organized so that it meets its deadlines, and how to check by measurement that it does."
- **Problem:** Wave 1 reworded objective 4 because "verify ... by measurement" contradicts entry 5 §3.2 and §4.1. This sentence makes a weaker form of the same claim. The end of §7.2 (line 382) already has the right wording: "predicted (fourth entry) and checked by measurement (fifth entry)".
- **Recommended correction:** "... how their software is organized so that its worst-case timing can be calculated, and how to check that calculation by measurement."

### T1. "Task" used before it is introduced
- **Where:** `src/content/blog/interrupts-polling-and-dma.mdx:119` ("setting a variable or signaling a task") and `:334` ("busy-waiting for completion inside a task")
- **Problem:** Tasks are defined in the fourth entry (§1.1). In the second entry the program is still a superloop, so at line 334 "inside a task" has no referent.
- **Recommended correction:** line 119: "setting a variable or signaling a task (a unit of an operating system's schedule, fourth entry)"; line 334: "busy-waiting for completion in the main program (or, under an operating system, in a task of the fourth entry)".

### T2. Characteristic impedance not glossed
- **Where:** `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx:200`
- **Text:** "terminated at each end by a 120 Ω resistor, which matches the cable's nominal 120 Ω characteristic impedance and so prevents reflections"
- **Problem:** Transmission-line ideas are not among the series prerequisites (`embedded-and-real-time-systems.md:13`).
- **Recommended correction:** after "characteristic impedance", insert "(the ratio of voltage to current of a wave travelling along the cable; a line ended in that resistance absorbs the wave instead of reflecting it back)".

### T3. Imprecise phrase in entry 2's opening
- **Where:** `src/content/blog/interrupts-polling-and-dma.mdx:21`
- **Text:** "It then treats the problem that interrupts create, data shared between code that can interrupt itself, and ends with a way to choose."
- **Problem:** "Code that can interrupt itself" suggests reentrancy. What is meant is data shared between the main program and the handlers that interrupt it (§4).
- **Recommended correction:** "It then treats the problem that interrupts create, data shared between the main program and the interrupt handlers that preempt it, and ends with a way to choose."

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| Embedded system, firmware | `inside-a-microcontroller.mdx:15` | `inside-a-microcontroller.mdx:27` | OK |
| Real-time, event, job, release, deadline, response time, latency, jitter | `inside-a-microcontroller.mdx:15` | `inside-a-microcontroller.mdx:37–46` | OK; reused by link in entries 2, 4, 5 |
| CPU, registers, stack pointer, link register, PC | `inside-a-microcontroller.mdx:74` | `inside-a-microcontroller.mdx:74, 89` | OK |
| Memory-mapped I/O, `volatile` | `inside-a-microcontroller.mdx:123` | `:123, :127` | OK |
| Interrupt handler | `inside-a-microcontroller.mdx:198` | `:198`, in full in `interrupts-polling-and-dma.mdx:70` | OK (forward reference stated) |
| DMA | `inside-a-microcontroller.mdx:217` | `interrupts-polling-and-dma.mdx:19, 252` | OK (expanded at first use) |
| Vector table, reset handler | `inside-a-microcontroller.mdx:223` | `:223` | OK |
| Timer, prescaler, PWM, input capture, watchdog | `inside-a-microcontroller.mdx:254` | `:254–320` | OK |
| Open-drain output | `inside-a-microcontroller.mdx:329` | `:329`; reused in `serial-buses-uart-spi-i2c-and-can.mdx:133` | OK |
| ADC | `inside-a-microcontroller.mdx:217` | `:217` (expanded), `:337` | OK |
| NVIC, exception, priority, preemption | `interrupts-polling-and-dma.mdx:72` | `:72, :111` | OK |
| Race condition, critical section, atomics | `interrupts-polling-and-dma.mdx:138` | `:138, :152, :166` | OK |
| Task (RTOS sense) | `interrupts-polling-and-dma.mdx:119` | `real-time-operating-systems-and-scheduling.mdx:25` | Used before introduction: T1 (optional) |
| Synchronous/asynchronous, differential, bit time, baud | `serial-buses-uart-spi-i2c-and-can.mdx:27` | `:27, :42` | OK |
| Characteristic impedance, reflections | `serial-buses-uart-spi-i2c-and-can.mdx:200` | not introduced | T2 (optional) |
| CRC | `serial-buses-uart-spi-i2c-and-can.mdx:239` | `:239` (table: "Cyclic redundancy check") | OK; polynomial given at `:248` |
| RTOS, TCB, context switch, tick, PendSV | `real-time-operating-systems-and-scheduling.mdx:17` | `:25, :31, :51, :57` | OK |
| WCET, utilization, RM, DM, RTA, critical instant, hyperperiod, EDF | `real-time-operating-systems-and-scheduling.mdx:90` | `:90–138, :260, :264` | OK |
| Mutex, semaphore, priority inversion, inheritance, ceiling | `real-time-operating-systems-and-scheduling.mdx:274` | `:274–302` | OK |
| High-water mark, BCET, probe effect, stack painting | `measuring-timing-latency-and-resource-use.mdx:35` | `:45, :116, :330` | OK (high-water mark in the table at :35, defined at :45, ten lines later) |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| C11 (ISO/IEC 9899:2011) | All code | Yes, every entry's Conventions and the overview | OK |
| Generic Armv7-M Cortex-M at 48 MHz, 3.3 V; invented register layouts | Entries 1–5 | Yes | OK |
| Arm-specific statements (12-cycle entry, 8-word frame, PRIMASK/BASEPRI, PendSV, DWT) | Entries 2, 4, 5 | Yes, marked as Arm-specific | OK |
| GCC 13, `-std=c11` | Entries 1, 2, 5 | Yes | OK; reproduced here with GCC 13.3.0 |
| Python 3, standard library | All calculations | Yes | OK; rerun with Python 3.13.16 |
| POSIX IEEE Std 1003.1-2017, note on 2024 edition | Entries 4, 5 | Yes | OK |
| ISO 11898-1:2015 / -2:2016 (classical CAN, CAN FD), with a note on the 2024 editions | Entry 3 | Yes | OK |
| I2C UM10204 rev. 7.0 (2021); controller/target terms | Entry 3 | Yes | OK (verified on the NXP PDF) |
| UART 8N1, 16× oversampling | Entries 2, 3 | Yes (`serial-buses...:57, :61`) | OK |
| Priority numbering (lower number = higher on Cortex-M) | Entries 2, 4 | Yes | OK |
| Timer $P$, $N$ as actual ratios, not register values | Entry 1 | Yes (`:270`) | OK |
| SI time prefixes, binary memory prefixes | Overview, entry 1 | Yes | OK |
| Jitter as peak-to-peak | Entries 1, 5 | Yes | OK |
| $D_i \le T_i$, no self-suspension, synchronous release | Entry 4 | Yes (`:92–94`) | OK |

## Series design

**Purpose, audience and scope.** The overview and entry 1 agree on the reader (basic C and digital logic, no embedded experience) and the goal. The overview does not say what is left out (S2, optional). The four objectives are checkable, each starts with an assessable verb, and each is met by named entries (table above).

**Sequence and rationale.** The order (hardware, data movement, buses, software organization, measurement) suits the stated reader. The fourth entry depends on the second (ISR load in RTA) and the fifth on the fourth. The third is a side path whose CAN arbitration prepares the scheduling view of the fourth; the overview's claim that every entry removes a limit of the previous one is wrong for it (S1). Moving the buses after scheduling was considered and rejected. Entry 4's view of CAN as a non-preemptive scheduler, and its use of entry 2's UART ISR in the worked design, read better with the buses already covered.

**Prerequisites and dependencies.** Nothing depends on a later entry, except the optional T1 ("task" in entry 2). Every cross-entry reference was checked against the target heading and content (map below).

**Notation and depth.** $C_i, T_i, D_i, B_i, R_i, U$ agree between entries 4 and 5; $L$ (entry 2), $t_\text{bit}$ and $C_m$ (entry 3) are local and defined. Letters are reused for unrelated local quantities: $C$ and $N$ for the PWM compare value and count in entry 1, $N$ for the idle count in entry 5, $c$ for cycles per interrupt in entry 2. Each is defined where it is used and never mixed with the scheduling symbols in one passage, so this is acceptable. Depth is even: every entry has a worked example, runnable code with real output, 4–5 exercises with answers, a summary table and references.

**Overview completeness.** The reader, prerequisites, sequence and shared conventions (C11, Cortex-M at 48 MHz, invented registers, POSIX, Python 3, SI and binary prefixes) are all present, as standards 6.5 requires. The only promise that the entries do not keep is the "each one removing a limit" claim (S1). The description is one sentence of 151 characters.

## Series-level notes

Cross-reference map (all checked by hand; every link resolves in the build):

| From | Reference | Target says what is claimed |
|---|---|---|
| Entry 2 :21, entry 4 :92, entry 5 :17 | Section 1.2 of the first entry | Yes |
| Entry 2 :50 | First entry §7.2, superloop | Yes |
| Entry 2 :87 | Section 4.1 of the first entry, vector table | Yes |
| Entry 2 :140, entry 5 :53 | Section 3.3 of the first entry, read-modify-write and set/clear registers | Yes |
| Entry 2 :274 | Section 6.2 of the first entry, timer-triggered ADC | Yes |
| Entry 2 :113 | "deadline-based priority assignment of the fourth entry" | Yes (entry 4 §2.2, DM) |
| Entry 3 :71 / :79 / :125 / :133 | First entry §4.2; second entry §1.1; second entry §6 (7 µs SPI); first entry §6.1 | Yes |
| Entry 4 :31 | First entry §3.4, 64 KiB SRAM | Yes |
| Entry 4 :45 / :57 / :118 / :274 / :280 / :319 | Second entry §2.1; first entry §5.1; second entry §3.3; §4.1; §3.4; §3.5 | Yes |
| Entry 4 :225 (entry 3) / entry 4 :150 | Davis et al. corrected analysis | Consistent wording in both entries |
| Entry 5 :42, :59, :61, :161, :204, :298, :316, :326 | First entry §§2.3, 5, 3.4; second entry §§5.3, 4.4, 3.2; fourth entry §§2.4, 1.4, 1.2, 4 | Yes |
| Promises: entry 1 :215 (stack measured in the fifth), :316 (input capture for latency), entry 4 :31, :53, :76 | Entry 5 §§6.2, 2.1, 2.1, 4.1 | Fulfilled |

Terminology is consistent: "utilization" for the scheduling quantity, "controller/target" (I2C) and "controller/peripheral" (SPI), I2C written in ASCII, "startup" throughout, American spelling. All five entries have the same structure: opening, Conventions, numbered sections, Exercises, Summary table, closing paragraph that leads to the next entry, and `### References`.

## Verification log

- Build: not run, as the brief instructs. The current full-site build at `/tmp/claude-0/b2` (SITE_URL=https://acrr.asia) was used. It reflects the reviewed text: the wave-1 descriptions, headings and objective 4 wording are present in the built pages.
- `node scripts/check-links.mjs /tmp/claude-0/b2`: "Checked 314 pages and 9667 internal references ... All internal links resolve."
- Built pages:
  - `grep -c katex-error` returns 0 for all five.
  - Mermaid min-widths are 449 px (entry 1), 335/418 px (entry 2), 474 px (entry 3), 398 px (entry 4) and 233 px (entry 5), all under 600 px.
  - Glued inline text: none. The two hits in entry 1 are inside KaTeX markup for $\log_2$.
- `npm run -s eos -- lint embedded-and-real-time-systems`: 6 files, 0 errors, 0 warnings, 60 suggestions. The suggestions are the acronym-expansion and sentence-length items that wave 1 accounted for, and none is re-reported here.
- `npm run -s eos -- syntax <series file and five entries>`: "All files compile."
- Code rerun (GCC 13.3.0, Python 3.13.16):
  - Entry 1: GPIO program (`-std=c11 -Wall -Wextra -pedantic`) and timer-settings script: output identical.
  - Entry 2: ring-buffer program (`-std=c11 -O2 -pthread`), three runs, all identical to the printed output; DMA/interrupt load table identical.
  - Entry 3: CAN frame/CRC script identical; CRC-15 of "123456789" = 0x059E.
  - Entry 4: all three Python programs (RTA sets A/B/blocking, unit-time FP/EDF simulation, worked design with exact fractions) identical.
  - Entry 5: cycle-counter program identical; combined Python script (three fragments) identical; stack-painting program identical.
  - Wake-up program (`-std=c11 -O2`, x86-64 Linux container): "absolute: min 66.0 us, median 98.9 us, 99th pct 1129.6 us, max 5033.3 us ...; relative: ... 309.1 ms behind the grid". These are different numbers with the same pattern (no drift with absolute sleeping, about 0.15 ms per period with relative sleeping, maximum about 50 times the median), as the text says to expect.
- Recomputed:
  - Entry 1:
    - 20.83 ns; 12.2% (8000/65 536); 1.728 s; 1.365 ms; 89.48 s;
    - log2 2400 = 11.23; 0.806 mV; 1.25 µs and 800 kS/s; servo C = 1500;
    - exercises 2.083 µs, 2.417 V, 10.91 bits, 7.2 KiB / 1.2 KiB;
    - the Armv7-M address map table agrees with the architecture's default map.
  - Entry 2:
    - 86.8 µs; U = 2.4%, 20.8%, 100%; 15.25 µs = 61× entry time; jitter 15 µs;
    - 25.6 ms; 39.1 interrupts/s;
    - exercises 1.8 ms, 29.25 µs (margin 20.75 µs), 10 ms.
  - Entry 3:
    - UART: 5.26%, 4.61%; 26.04 → 115 385 baud (+0.16%); 8.68 → 111 111 baud (−3.55%); Exercise 1 9615 baud (+0.16%).
    - I2C: ln(0.7/0.3) = 0.8473; pull-up limits 967, 1770 and 5901 Ω; Exercise 2 885 and 2950 Ω; 81 clocks = 202.5 µs = 28.9× the SPI time.
    - SPI: 56 clocks = 7 µs; mode table and Exercise 3 (mode 2).
    - CAN arbitration: binary forms of 0x65A, 0x652, 0x6A0, 0x100 and 0x0FF, and the drop-out bits.
    - CAN timing: worst-case 8-byte frame 135 bits, 270 µs, 47%; bus load 27%; Exercise 4 95 bits, 380 µs, 38%; bus length 40 m and 115 m.
  - Entry 4:
    - U = 0.833; bounds 0.828 and 0.780, limit ln 2 = 0.693;
    - RTA iterations 3 → 6 → 7 → 9 → 10; set C U = 0.971 with RM 4 → 6 → 8 > 7; timeline slots 3, 5, 9;
    - ISR increments 0.0375, 0.0875 and 0.2479 ms, margins 2.46, 2.41 and 1.75 ms; 10 KiB = 15.6% of 64 KiB;
    - Exercises 1–5, including the DM/RM counterexample (R_a = 4 under RM, 2 under DM, R_b = 4).
  - Entry 5:
    - 3840 cycles = 80 µs; 0x2000 = 8192 cycles = 170.7 µs; 3.47 ms;
    - P(never seen) table; 4.61 × 10⁶ runs = 5.12 h;
    - margin-fed RTA 1.484, 3.452 and 10.140 ms; load 60% and 30%;
    - flash/SRAM 43 100 B (16.4%) and 7372 B (11.2%); stack 724 B (71%);
    - wake-up bullets: drift 0.157–0.182 ms per period; max/median ratios 68.8, 47.8 and 132.
- References checked (fetched 2026-10-14 unless stated):
  - NXP UM10204 rev. 7.0, 1 October 2021 (NXP PDF): controller/target terms introduced in rev. 7, 16 reserved addresses, Sm rise time 1 µs, 400 pF, 3 mA, bus clear with nine clocks, Hs 3.4 Mbit/s, UFm 5 Mbit/s, and a resistor pull-up limited to about 200 pF in Fast-mode (consistent with entry 3 §4.4 and Exercise 2).
  - Di Natale et al. on Springer: F3.
  - Arm DDI 0403E.e: F1.
  - Wilhelm et al. 2008: the spelling "J. Staschulat" is confirmed by the authors' preprint (F. Mueller's site, NCSU) and the CiteDrive record for DOI 10.1145/1347375.1347389. The Chalmers record's "Stachulat" is the error, so no change is needed (resolves the wave-1 flag); volume 7, issue 3 and year 2008 are confirmed by the Chalmers record.
  - Reeves's Mars Pathfinder account: F2.
  - Not fetched again in this pass, and consistent with the reviewer's knowledge of the works: Davis et al. (vol. 35, no. 3, pp. 239–272, verified by wave 1 on Springer); Liu and Layland; Leung and Whitehead; Joseph and Pandya; Audsley et al.; Sha et al.; Kopetz 2nd ed. 2011; Lee and Seshia 2nd ed. 2017; White 2011; Yiu 3rd ed. 2014; Ganssle 2nd ed. 2008; Burns and Wellings 4th ed. 2009; Buttazzo 3rd ed. 2011; Horowitz and Hill 3rd ed. 2015; Bosch CAN 2.0 (1991); TIA-232-F (1997); TIA-485-A (1998); ISO 11898-1:2015 and 11898-2:2016 titles.
- Not verified:
  - The printed wake-up output in entry 5 §4.1 (`measuring-timing-latency-and-resource-use.mdx:275–280`). It describes one session on a shared VM and cannot be reproduced by design; the text says so, and a rerun here showed the same pattern.
  - "an earlier session on the same machine gave maxima of up to 38 ms" (`measuring-timing-latency-and-resource-use.mdx:287`). The only record is the resolution section of the earlier series review; no output was kept. The sentence is qualified and not load-bearing.
  - Wilhelm et al. article number and pages (the ACM Digital Library could not be fetched), so the citation correctly stops at vol. 7, no. 3.
  - Arm DDI 0403E.e date: read from an unofficial copy of the Arm PDF, because Arm's site returned no content.
  - Arm's 12-cycle interrupt entry for Cortex-M3/M4 (`interrupts-polling-and-dma.mdx:97`), the I2C Fm/Fm+ rise-time, capacitance and current values (`serial-buses-uart-spi-i2c-and-can.mdx:164–166`), and the CAN fault-confinement thresholds (`:325`): checked against the reviewer's knowledge of the Yiu book, UM10204 Table 10 and ISO 11898-1, not against fetched text. The ISO standard is paywalled, and the fetched part of UM10204 did not include Table 10.

## Resolution

- F1 (Should fix): fixed - all three entries now cite "Arm Limited, *Armv7-M Architecture Reference Manual*, ARM DDI 0403E.e, 2021." (`inside-a-microcontroller.mdx:455`, `interrupts-polling-and-dma.mdx:393`, `measuring-timing-latency-and-resource-use.mdx:461`). Issue E.e (ID021621, 15 February 2021) was re-checked on 2026-10-15 in the front matter of the PDF copy at kib.kiev.ua; Arm's own pages still return no content.
- F2 (Should fix): fixed - the Mars Pathfinder sentence is now attributed to G. E. Reeves, as recommended, and the reference "G. E. Reeves, account of the Mars Pathfinder resets, email of 15 December 1997, Jet Propulsion Laboratory." is added between Liu and Layland and Sha et al. (`real-time-operating-systems-and-scheduling.mdx:295, 435`). The account was re-fetched on 2026-10-15: the author, the date, the bc_dist/ASI/MET inversion, the reset and the priority-inheritance fix on the select() semaphore all agree with the text.
- S1 (Should fix): fixed - the sequence paragraph is replaced with the recommended text (`src/content/series/embedded-and-real-time-systems.md:15-17`). It is split into two paragraphs after the third entry, so that the fourth entry's "removes the limit the second leaves" stands at the start of its own paragraph. No copied field changed, so the Vietnamese series file still builds. Its prose is now out of date (see below).

Optional findings applied: F3 (subtitle "Theory and Practice", re-checked on Springer's book page on 2026-10-15), S2 (scope sentence appended to the first paragraph of the overview), S3 (entry 1 opening), T1 (both locations in entry 2), T2 (entry 3 §5.1: a separate gloss sentence, not a parenthesis, with "characteristic impedance" in bold as the term being defined and the American spelling "traveling"), T3 (entry 2 opening). Optional findings not applied: none.

Translation follow-up: `src/content/series/vi/embedded-and-real-time-systems.md` should take the new scope sentence (S2) and the new sequence paragraphs (S1). Its objective 4 still has the old "verify by measurement" meaning that wave 1 changed. None of the five entries has a Vietnamese translation.

Checks: `eos lint` (series file and five entries): 0 errors, 0 warnings, 58 suggestions. `eos syntax`: "All files compile." No code or number was changed, so nothing was rerun.

Resolved by the wave-1 author on 2026-10-15; awaiting the reviewer's resolution check.

## Resolution check
QA editor (final gate), 2026-10-15, against the current files; build `/tmp/claude-0/b9`.
- F1 (Should fix): confirmed - `inside-a-microcontroller.mdx:455`, `interrupts-polling-and-dma.mdx:393` and `measuring-timing-latency-and-resource-use.mdx:461` all read "Arm Limited, *Armv7-M Architecture Reference Manual*, ARM DDI 0403E.e, 2021."
- F2 (Should fix): confirmed - `real-time-operating-systems-and-scheduling.mdx:295` attributes the Mars Pathfinder account to G. E. Reeves of the Jet Propulsion Laboratory and says "semaphore"; the reference is at `:435`, in alphabetical order between Liu and Layland and Sha et al. The entry's argument does not depend on the example.
- S1 (Should fix): confirmed - overview lines 15-17 no longer claim that every entry removes a limit of the previous one; the second entry "analyzes the polling that the superloop performs", and the limit the second entry leaves (processing in one loop) is assigned to the fourth, which matches `interrupts-polling-and-dma.mdx:336` and the fourth entry's opening.
- Optional F3, S2, S3, T1, T2, T3: confirmed applied (Di Natale subtitle at entry 3 `:416`; scope sentence at overview line 13; entry 1 opening line 15; "task" glossed at entry 2 `:119` and `:334`; characteristic impedance defined at entry 3 `:200`; entry 2 opening line 21).
- Checks: `eos lint embedded-and-real-time-systems` 0 errors, 0 warnings; `eos syntax` on the six files: all compile; `check-links` on the build: 314 pages, all internal links resolve; `eos validate-site --json`: no issue on any page of this series (all 29 issues are `/vi/` pages); `katex-error` 0 in all five built pages. Re-run with GCC 13.3.0 and Python 3.13: GPIO, ring-buffer, cycle-counter and stack-painting programs and all Python blocks reproduce the printed output; the wake-up program gave different numbers with the same pattern (absolute: max about 41 times the median; relative: 248.6 ms behind the grid after 2000 periods), as the text says to expect.
- Reopened: none.
