# Series review: Embedded and Real-Time Systems

- Series: `embedded-and-real-time-systems` (5 articles, status published, 0 planned entries)
- Reviewed commit: b27867d
- Date: 2026-10-13

## Summary

The series is technically strong and well built. It moves from the vocabulary of real-time systems and the parts of a microcontroller, through polling, interrupts and DMA, serial buses, and RTOS scheduling theory, to measurement. Each entry builds on the previous ones with accurate, linked cross-references. Every program and calculation in the five entries was recompiled or rerun and reproduced its printed output, and the CAN CRC-15 check value 0x059E was confirmed. All nineteen references were checked and are real, with consistent authors, titles, venues and years.

There is one blocking finding. The concurrency fix in the second entry's Exercise 3 claims a guarantee that does not hold: the overflow interrupt can still be pending when the high half is re-read. The should-fix findings are:
- the CAN termination sentence, which reads as if 60 Ω matched the cable;
- an exception-frame size given without the floating-point case, which the fifth entry does mention;
- ISO 11898-1/-2 and POSIX editions that were superseded in 2024, cited without saying so;
- the wake-up experiment of the fifth entry, whose numbers could not be reproduced and whose framing needs to say plainly that they describe one session on a shared machine;
- an understated superloop latency.

The series can be published once these are corrected.
Findings: 1 blocking, 6 should fix, 6 optional.

## Resolution

At the owner's request, all 13 findings (F1–F13) were applied on 2026-10-13 in the English articles. None of the five articles has a Vietnamese translation, and the series file did not change, so no translation needed updating.

Applied as recommended:
- F1, Exercise 3 of entry 2: the false guarantee is replaced by the pending-interrupt caveat and the overflow-flag check.
- F2, entry 3 §5.1: the termination sentence is reworded.
- F3, entry 2 §3.1: the floating-point case is added to the exception frame.
- F4, entry 3 Conventions: a note says that the cited ISO 11898 editions have been revised in 2024.
- F5, Conventions of entries 4 and 5: a note says that the POSIX interfaces used are unchanged in the 2024 edition. The reference entries still cite the 2017 edition the examples were written against.
- F7, entry 1 §7.2: the latency is now "more than 20 ms, a whole pass of the loop".
- F9, F10, F11, F12 and F13: applied with the wording given in each finding.

Applied with changes:
- F6, entry 5 §4.1: the unverifiable output was replaced by output reproduced for this review. It comes from one session of three successive runs of the unchanged `wakeup.c`, built with GCC 13.3 `-std=c11 -O2` on a four-core x86-64 Linux VM shared with other jobs. The text now says that the numbers describe that machine at that moment, and that a rerun gives different numbers. The bullets were recomputed from the new output:
  - drift of 314.0–363.1 ms, that is 0.16–0.18 ms per period;
  - medians of about 0.12 ms;
  - maxima of 5.8–15.3 ms, 48–132 times the median of the same run;
  - an earlier session on the same machine gave maxima of up to 38 ms.
- F8, entry 1: the introduction is shortened to one sentence, and the closing paragraph of §7.2 to one sentence. The §1.3 table remains the one full roadmap.
- Entry 3, the other long entry, was checked for redundancy. Apart from the wording fixes nothing was cut, because its overlapping passages each serve a distinct purpose (definitions, then the comparison table).

Second pass (full re-read of all five entries after the corrections):
- **S1 (should fix, entry 3 §5.7, line 329 of the reviewed commit).** "bit rate times bus length is roughly constant, so halving the bit rate roughly doubles the usable length" contradicted the section's own model: at 500 kbit/s the same assumptions give $(750 - 175)/5 = 115$ m, not 80 m. The sentence now says that halving the bit rate at least doubles the length (more than doubles it in this model, because the node delays are fixed) and gives the 115 m figure.
- **S2 (should fix, entry 4 §2.4, line 150).** "The same equation, with a blocking term ..., gives the worst-case response times of the CAN messages ..., as worked out by Davis, Burns, Bril and Lukkien (2007)" misattributed the result. The paper is known for showing that this direct adaptation can be optimistic. The text now says that an adapted form of the equation applies, and that Davis et al. showed the earlier direct version could be optimistic and gave the corrected analysis.
- Wording fixes introduced by the corrections:
  - F7 "after its check" became "after the loop has checked for it";
  - the F4 note was split into its own sentence;
  - the F6 framing sentence was tightened.
- A further full pass over the changed passages found no blocking and no should-fix issues.

Re-run results:
- `npm run build:local`: exit 0, with 0 errors and 0 warnings from `astro check`.
- Pagefind: 81 pages indexed, in 2 languages.
- `npm run check:links`: "Checked 216 pages and 6146 internal references in dist. All internal links resolve."
- dist checks: Mermaid min-widths are 449, 335/418, 474, 398 and 233 px. No `katex-error`, and no text glued to inline elements.

All code blocks were unchanged by the corrections, so their recomputed outputs (Verification log) still apply.

Line numbers below refer to the reviewed commit, not to the corrected articles.

## Objectives coverage
| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Describe how a microcontroller's CPU, memory, timers, converters and peripherals work together. | Entry 1 (§§2–7) | Met: core, flash/SRAM, memory map, startup, clocks, timers, GPIO, ADC and firmware layering, with worked numbers. |
| Choose between polling, interrupts and DMA for moving sensor data. | Entry 2 (§§2–6) | Met: mechanisms, latency and load models, a decision table and four worked decisions. |
| Compare serial buses (UART, SPI, I2C, CAN) by topology, speed and error handling. | Entry 3 (§§2–6) | Met: each bus treated in a common frame, comparison table in §6. |
| Explain real-time scheduling and verify that deadlines are met by measurement. | Entries 4 and 5 | Met: RM/DM, utilisation bound, RTA, EDF, blocking; entry 5 measures and feeds results back into RTA. |

## Findings
| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `src/content/blog/interrupts-polling-and-dma.mdx` | §7 Exercise 3 answer (line 363) | Technical accuracy | The double-read fix for a 64-bit tick is said to be safe "as long as interrupts are enabled"; it is not. |
| F2 | Should fix | `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx` | §5.1 (line 200) | Technical accuracy | "60 Ω in total, matching the cable's characteristic impedance" reads as if the 60 Ω total matched the cable. |
| F3 | Should fix | `src/content/blog/interrupts-polling-and-dma.mdx` | §3.1 (line 87) | Technical accuracy / Factual consistency | Exception entry said to save eight registers, 32 bytes, with no floating-point case; entry 5 (line 380) adds it. |
| F4 | Should fix | `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx` | Conventions (line 19), references (416–417) | Stated versions | ISO 11898-1:2015 and ISO 11898-2:2016 are presented as current; both were replaced by 2024 editions. |
| F5 | Should fix | `src/content/blog/real-time-operating-systems-and-scheduling.mdx`, `src/content/blog/measuring-timing-latency-and-resource-use.mdx` | Conventions (line 19 in both), code comment (entry 5 line 207) | Stated versions | IEEE Std 1003.1-2017 is cited as if current; IEEE Std 1003.1-2024 has replaced it. |
| F6 | Should fix | `src/content/blog/measuring-timing-latency-and-resource-use.mdx` | §4.1 (lines 272–288) | Fit with site rules / Technical accuracy | The wake-up output came from one session on a shared VM and could not be reproduced. The text draws precise ratios from it without saying that a rerun gives different numbers. |
| F7 | Should fix | `src/content/blog/inside-a-microcontroller.mdx` | §7.2 (line 378) | Technical accuracy | "a sample may wait up to 20 ms" understates the wait: it can be a whole loop pass, more than 20 ms. |
| F8 | Optional | `src/content/blog/inside-a-microcontroller.mdx` | Introduction (line 17), §7.2 (line 380) | Writing quality | The roadmap is given three times (introduction, §1.3 table, closing paragraph of §7.2). |
| F9 | Optional | `src/content/blog/interrupts-polling-and-dma.mdx` | §6 (line 332) | Writing quality | "Bytes arrive irregularly, every 86.8 µs at most" is ambiguous. |
| F10 | Optional | `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx` | §6 table (line 346) | Terminology | "ADCs" is not expanded in this entry. |
| F11 | Optional | `src/content/blog/measuring-timing-latency-and-resource-use.mdx` | §2.2 (line 59) | Technical accuracy | The DWT cycle counter must be enabled before it counts; not mentioned. |
| F12 | Optional | `src/content/blog/inside-a-microcontroller.mdx` | §4.1 (lines 225–230) | Technical accuracy | The numbered startup steps imply an order; many startup files configure clocks before copying `.data`. |
| F13 | Optional | `src/content/blog/inside-a-microcontroller.mdx` | §2.2 (line 91) | Technical accuracy | The list of Cortex-M profiles omits Armv8.1-M (Cortex-M55, M85). |

### F1. False guarantee in the overflow-read fix
- **Where:** `src/content/blog/interrupts-polling-and-dma.mdx:363`, section "7. Exercises", Exercise 3 answer
- **Text:** "A standard fix is to read `ticks_high`, then the counter, then `ticks_high` again, and repeat if the two high reads differ. (The fix also assumes the overflow ISR is not delayed past the read, which holds as long as interrupts are enabled.)"
- **Problem:** Interrupts being enabled is not enough to guarantee that the overflow ISR has run by the second read.
  - The counter can wrap between the first read of `ticks_high` and the read of `TIMER->COUNT`. The overflow interrupt is then pending, but its entry takes 12 or more cycles (§3.2 of the same entry), while the second load of `ticks_high` follows within a few cycles. Both high reads then return the old value, the low half is the new small value, and the result is wrong by $2^{32}$ counts: the very error the fix is meant to remove.
  - The same happens whenever the reader runs at a priority equal to or higher than the overflow ISR, for example inside another ISR, or inside a critical section.
  - As written, the parenthesis gives the reader a false guarantee for concurrency code.
- **Recommended correction:** Replace the parenthesis with: "(This assumes that the overflow ISR has run before the second read of `ticks_high`. That is not guaranteed even with interrupts enabled: the interrupt may still be pending, during its entry time or because the reading code runs at the same or a higher priority. Robust code therefore also checks the timer's overflow flag: if it is set and the counter value is small, it adds one to the high half.)"

### F2. CAN termination and characteristic impedance
- **Where:** `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx:200`, section "5.1 The physical layer"
- **Text:** "terminated at each end by a 120 Ω resistor (60 Ω in total, matching the cable's characteristic impedance to prevent reflections)"
- **Problem:** The sentence attaches "matching the cable's characteristic impedance" to "60 Ω in total". ISO 11898-2 specifies a cable with a nominal characteristic impedance of 120 Ω. Each 120 Ω terminator matches the cable at its own end, and 60 Ω is only the resistance between the two wires that the transmitters see.
- **Recommended correction:** "terminated at each end by a 120 Ω resistor, which matches the cable's nominal 120 Ω characteristic impedance and so prevents reflections (the two in parallel present 60 Ω between the wires)."

### F3. Exception frame size without the floating-point case
- **Where:** `src/content/blog/interrupts-polling-and-dma.mdx:87`, section "3.1 The mechanism"
- **Text:** "On Cortex-M, hardware saves eight registers (R0 to R3, R12, the link register LR, the program counter PC and the status register, 32 bytes) on the stack"
- **Problem:** The text is correct for the basic frame. On a core with a floating-point unit, such as the Cortex-M4 with FPU whose 12-cycle entry the next section quotes, an interrupted context that uses floating point gets an extended frame of 26 words (104 bytes), or lazy reservation of that space. The fifth entry says so: "32 bytes, more if floating-point state is saved" (`measuring-timing-latency-and-resource-use.mdx:380`). Readers of the second entry are given the figure as if it were universal.
- **Recommended correction:** "...the status register, 32 bytes; on cores with a floating-point unit, more when the interrupted code was using floating-point registers) on the stack".

### F4. ISO 11898 editions superseded
- **Where:** `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx:19` and references at lines 416–417
- **Text:** "CAN follows ISO 11898-1:2015 (data link layer) and ISO 11898-2:2016 (high-speed physical layer)"
- **Problem:** The text presents these editions as current. ISO 11898-1:2024 ("Data link layer and physical coding sublayer", which adds CAN XL) and ISO 11898-2:2024 ("High-speed physical medium attachment (PMA) sublayer") have replaced them. Citing the earlier editions is legitimate, but the text should say that they have been superseded.
- **Recommended correction:** Append to the Conventions sentence: "(both have since been revised in 2024 editions, which add CAN XL; this entry describes classical CAN and CAN FD as specified in the editions cited)".

### F5. POSIX edition superseded
- **Where:** `src/content/blog/real-time-operating-systems-and-scheduling.mdx:19`, `src/content/blog/measuring-timing-latency-and-resource-use.mdx:19` and `:207`
- **Text:** "the real-time interface of POSIX, the Portable Operating System Interface (IEEE Std 1003.1-2017)"
- **Problem:** IEEE Std 1003.1-2024 (POSIX.1-2024, Issue 8) has replaced the 2017 edition. The interfaces the examples use (`clock_gettime`, `clock_nanosleep` with `TIMER_ABSTIME`, `CLOCK_MONOTONIC`) are in both editions, so nothing in the examples is wrong, but the edition is presented as if it were the current one.
- **Recommended correction:** "(IEEE Std 1003.1-2017; the interfaces used here are unchanged in the current 2024 edition)".

### F6. Framing of the wake-up experiment
- **Where:** `src/content/blog/measuring-timing-latency-and-resource-use.mdx:272–288`, section "4.1 Release jitter of a periodic task: an experiment"
- **Text:** "It was compiled with GCC 13 (`-std=c11 -O2`) and run three times in succession, as an ordinary process without real-time priority, on a four-core x86-64 Linux virtual machine under other load" and "the maxima were 5.4 to 9.4 ms, roughly fifty to eighty times the median of the same run"
- **Problem:** The printed output was captured in one session on a shared virtual machine. Rerunning `wakeup.c` for this review (GCC 13.3, four-core x86-64 Linux VM shared with other jobs) gave medians of 98–107 µs, consistent with the article. The maxima, however, were 7.0, 37.9 and 34.3 ms, and the relative-sleep drift was 303.0, 999.0 and 405.7 ms. The qualitative conclusions all hold. The quoted output, though, cannot be checked, and the bullets draw specific ratios from it ("fifty to eighty times") as if it were a representative measurement. The site's rules require measured results to be genuine and presented for what they are.
- **Recommended correction:** Replace the output block with output that was reproduced and can be vouched for, and describe it as one session on a shared machine. Say explicitly that another run, or another machine, gives different maxima and drift and that only the pattern should be taken from it. Make the bullets match the new numbers.

### F7. Superloop latency understated
- **Where:** `src/content/blog/inside-a-microcontroller.mdx:378`, section "7.2 The superloop"
- **Text:** "If `update_display()` takes 20 ms, a sample may wait up to 20 ms to be processed"
- **Problem:** A result that becomes ready just after `adc_result_ready()` has been checked waits for the rest of the pass: `button_changed()`/`update_mode()`, the 20 ms `update_display()`, `watchdog_feed()`, and the next check. The wait is at least 20 ms in the worst case, not at most 20 ms. Entry 2 §2.2 correctly gives the bound as one whole loop pass $L$.
- **Recommended correction:** "If `update_display()` takes 20 ms, a sample that becomes ready just after its check waits more than 20 ms, a whole pass of the loop, to be processed".

### F8. Repeated roadmap in the first entry (author asked for redundancy to be cut)
- **Where:** `src/content/blog/inside-a-microcontroller.mdx:17` and `:380`
- **Text:** line 17 lists the entry's contents item by item; line 380 restates the whole series plan already given in the §1.3 table.
- **Problem:** The same plan is given three times in one entry, which adds length (the entry is about 5,600 words of prose) without adding information.
- **Recommended correction:** Shorten line 17 to a one-sentence statement of the entry's scope. Reduce line 380 to two sentences that link the superloop's weakness to the next entries.

### F9. Ambiguous byte rate
- **Where:** `src/content/blog/interrupts-polling-and-dma.mdx:332`
- **Text:** "Bytes arrive irregularly, every 86.8 µs at most."
- **Recommended correction:** "Bytes arrive irregularly, at most one every 86.8 µs."

### F10. "ADCs" not expanded in entry 3
- **Where:** `src/content/blog/serial-buses-uart-spi-i2c-and-can.mdx:346`
- **Text:** "Fast sensors, flash memory, displays, ADCs"
- **Recommended correction:** "Fast sensors, flash memory, displays, analog-to-digital converters".

### F11. Cycle counter needs enabling
- **Where:** `src/content/blog/measuring-timing-latency-and-resource-use.mdx:59`
- **Text:** "Where it exists, it gives cycle resolution with a single register read."
- **Problem:** The DWT cycle counter does not run until trace is enabled in the debug control registers and the counter itself is enabled. "The counter reads zero" is a common bring-up surprise.
- **Recommended correction:** "Where it exists, and once it has been enabled (it is off after reset), it gives cycle resolution with a single register read."

### F12. Order of startup steps
- **Where:** `src/content/blog/inside-a-microcontroller.mdx:225–230`
- **Text:** "1. Copy the initial values of `.data` ... 3. Configure the clocks (Section 4.2) ... 4. Call `main`."
- **Problem:** The numbering implies a fixed order. Many vendor startup files call the clock set-up first, before `.data` and `.bss` are initialised.
- **Recommended correction:** Add after the list: "The order varies: many startup files configure the clocks first, so that the copying runs at full speed."

### F13. Armv8.1-M missing from the profile list
- **Where:** `src/content/blog/inside-a-microcontroller.mdx:91`
- **Text:** "defined by the Armv6-M, Armv7-M and Armv8-M architecture profiles"
- **Recommended correction:** "defined by the Armv6-M, Armv7-M and Armv8-M architecture profiles (the newest cores implement Armv8.1-M, an extension of Armv8-M)".

## Concept introduction map
| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Embedded system, firmware | `inside-a-microcontroller.mdx:15` | `inside-a-microcontroller.mdx:27` | Good |
| Real-time, deadline, latency, jitter, response time | `inside-a-microcontroller.mdx:15` | `inside-a-microcontroller.mdx:37–46` | Good; reused consistently in all later entries |
| Microcontroller, CPU, peripherals | `inside-a-microcontroller.mdx:15` | `inside-a-microcontroller.mdx:74` | Good |
| Registers, SP/LR/PC, load-store, Thumb | `inside-a-microcontroller.mdx:89` | same lines | Good |
| Memory map, memory-mapped I/O, `volatile` | `inside-a-microcontroller.mdx:108` | `inside-a-microcontroller.mdx:108, 123, 127` | Good |
| Vector table, reset handler | `inside-a-microcontroller.mdx:223` | same line | Good |
| Timer, prescaler, PWM, input capture, watchdog | `inside-a-microcontroller.mdx:223` (watchdog) | `inside-a-microcontroller.mdx:252–318` | Good; watchdog forward-referenced to §5.4 |
| ADC, LSB | `inside-a-microcontroller.mdx:217` | `inside-a-microcontroller.mdx:217, 337`; sampling theory linked to another series | Good |
| Interrupt, ISR | `inside-a-microcontroller.mdx:198` | `inside-a-microcontroller.mdx:198`; `interrupts-polling-and-dma.mdx:70` | Good |
| DMA | `inside-a-microcontroller.mdx:217` | `inside-a-microcontroller.mdx:217`; `interrupts-polling-and-dma.mdx:19, 252` | Good |
| Exception, NVIC, PRIMASK, BASEPRI | `interrupts-polling-and-dma.mdx:72` | `interrupts-polling-and-dma.mdx:72, 152, 160` | Good |
| Race condition, critical section, C11 atomics, memory order | `interrupts-polling-and-dma.mdx:138` | `interrupts-polling-and-dma.mdx:138, 152, 166` | Good |
| Bit rate, baud, synchronous/asynchronous, differential | `serial-buses-uart-spi-i2c-and-can.mdx:27` | `serial-buses-uart-spi-i2c-and-can.mdx:27, 42` | Good |
| UART, SPI, I2C, CAN | `interrupts-polling-and-dma.mdx:31` (UART), `:62` (SPI) | expanded at first use in entry 2; defined in `serial-buses-uart-spi-i2c-and-can.mdx:17, 48, 95, 133, 198` | Good |
| CRC, bit stuffing, dominant/recessive | `serial-buses-uart-spi-i2c-and-can.mdx:202` | `serial-buses-uart-spi-i2c-and-can.mdx:202–246` | Good |
| RTOS, task, TCB, context switch, PendSV | `interrupts-polling-and-dma.mdx:336` | `real-time-operating-systems-and-scheduling.mdx:25–51` | Good |
| WCET, utilisation, RM, DM, RTA, EDF, hyperperiod | `real-time-operating-systems-and-scheduling.mdx:90` | `real-time-operating-systems-and-scheduling.mdx:90–264` | Good |
| Mutex, semaphore, priority inversion, inheritance, ceiling | `real-time-operating-systems-and-scheduling.mdx:45` | `real-time-operating-systems-and-scheduling.mdx:274–302` | Good |
| High-water mark, BCET, probe effect, stack painting | `measuring-timing-latency-and-resource-use.mdx:35` | `measuring-timing-latency-and-resource-use.mdx:45, 116, 330` | Good |
| Characteristic impedance | `serial-buses-uart-spi-i2c-and-can.mdx:200` | not introduced | Acceptable for the stated prerequisites; F2 rewords the sentence |

## Versions, defaults and conventions
| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| C11 (ISO/IEC 9899:2011) | all entries | Yes (entry 1 line 21, conventions of each entry) | Deliberate, stated; later C editions do not affect the examples |
| GCC 13, host x86-64 Linux for runnable C | entry 1 line 21; entry 2 line 239; entry 5 line 272 | Yes | Reproduced with GCC 13.3 |
| Generic Cortex-M at 48 MHz, 3.3 V; invented register layouts | entry 1 line 21; conventions of entries 2, 5 | Yes | Good |
| Armv7-M memory map, exception frame, PRIMASK/BASEPRI, DWT | entries 1, 2, 5 | Yes, marked as Arm-specific | F3 adds the FP case |
| SI prefixes for time and bit rate, binary prefixes for memory | entry 1 line 21; entry 3 line 19 | Yes | Good |
| Priority numbering (lower number = higher on NVIC) | entry 2 line 111; entry 4 line 19 | Yes | Good |
| UART 8N1, 16× oversampling | entry 3 lines 57, 61 | Yes | Good |
| I2C per UM10204 rev 7.0 (2021); controller/target terminology | entry 3 line 19 | Yes | Values in the table agree with the specification's Sm/Fm/Fm+ limits |
| CAN per ISO 11898-1:2015 / 11898-2:2016; classical base-format frame | entry 3 line 19 | Yes, but superseded editions not flagged | F4 |
| POSIX IEEE Std 1003.1-2017 | entry 4 line 19; entry 5 lines 19, 207 | Yes, but superseded edition not flagged | F5 |
| Python 3, standard library | all entries | Yes | Reproduced with Python 3.13 |
| Times in ms in task examples, deadlines $D \le T$ | entry 4 lines 19, 92 | Yes | Good |

## Series-level notes
- **Terminology and spelling.** British spelling is consistent: initialise, organise, prioritise, utilisation, synchronisation, analyse, behaviour. "Analog-to-digital" and "quantization" follow the site-wide convention used by the other series and by the linked article title, so they are not counted as inconsistencies. "Synchronization" appears only in the title of a cited paper.
- **Cross-references.** Every "the first/second/third/fourth/fifth entry" claim was checked against its target. The checked claims include:
  - interrupts treated in entry 2;
  - SPI transfer time computed in entry 3 §3.3;
  - deadline-monotonic priority in entry 4 §2.2;
  - context switch, stack use and wake-up latency measured in entry 5 §§2.1, 6.2, 4.1;
  - CAN response-time analysis mentioned in entry 4 §2.4.

  Every "Section N of entry M" link points to the stated section, and its anchor resolves. Link texts match their targets.
- **Consistency of numbers across entries.**
  - UART 115 200 baud: 86.8 µs and 11 520 bytes/s (entries 2, 3, 4, 5).
  - ISR at 100 cycles: 2.4 % load (entries 2, 4).
  - 64 KiB SRAM (entries 1, 4, 5).
  - 32-bit counter wrap of 89.48 s (entries 1, 5).
  - SPI transfer of 7 µs (entries 2, 3).
  - Blocking of 0.5 ms and $R_2 = 3.5$ ms (entries 4, 5).

  All agree.
- **Structure.** Each entry has a Conventions paragraph, numbered sections, exercises with answers, a summary table, a pointer to the next entry and a reference list. Frontmatter (category "Computing Systems", series, `seriesOrder` 1–5, date) is consistent.

## Verification log
- `npm run build:local`: passed (exit 0; localhost warning only, as expected for a local build).
- `npm run check:links`: "Checked 216 pages and 6146 internal references in dist. All internal links resolve."
- dist checks: Mermaid min-widths are 449, 335/418, 474, 398 and 233 px (all ≤ 600). No `katex-error`. No text glued to `<a>`, `<code>` or `<strong>` in the five pages.
- Recomputed with GCC 13.3 (`-std=c11 -Wall -Wextra -pedantic`, plus `-O2 -pthread` for the ring buffer) and Python 3.13:
  - entry 1:
    - GPIO program output: identical;
    - `timer_settings` output: identical (1000 Hz, 50 Hz exact; 44 100 Hz → 44 117.647 Hz, +400.2 ppm);
    - 20.83 ns, 1.365 ms, 89.48 s, 1.73 s/day, PWM 2400 steps and 11.2 bits, 0.806 mV, 1.650 V, 1.25 µs, 8000 B ≈ 12 % of 64 KiB, and Exercises 1–5 (2.08 µs, 2.417 V, 1920 steps and 10.9 bits, 7.2 KiB): all correct.
  - entry 2:
    - ring buffer: three runs, each "received 1000000 items, 0 out of order / buffer was full at least once", on a four-core x86-64 host as stated;
    - load table: identical;
    - 86.8 µs, 15.25 µs (×61 of 250 ns), 2.4 % / 20.83 %, 25.6 ms, 39.1 interrupts/s, Exercise 2 (29.25 µs) and Exercise 4 (10 ms): correct.
  - entry 3:
    - CAN program output: identical;
    - CRC-15 of ASCII "123456789" (bits MSB first, register 0, polynomial 0x4599) = 0x059E: confirmed;
    - UART tolerance 5.26 % and 4.6 %; dividers 26.04 → 115 385 baud (+0.16 %) and 8.68 → 111 111 baud (−3.55 %); Exercise 1 (9615 baud, +0.16 %): correct;
    - I2C pull-up limits 967 Ω, 1770 Ω, 5901 Ω, 885 Ω and 2950 Ω, and ln(0.7/0.3) = 0.8473: correct;
    - I2C 81 clocks and 202.5 µs (≈29 × 7 µs): correct;
    - arbitration bit patterns of 0x65A/0x652/0x6A0 and 0x100/0x0FF: correct;
    - worst-case frame of 135 bits / 270 µs, 47 %, 27 % load; Exercise 4 (95 bits, 380 µs, 38 %): correct;
    - bus length bound of 40 m: correct.
  - entry 4:
    - all three program outputs: identical;
    - RTA table iterations, RM bound 0.7798 and 0.828: correct;
    - Set C RTA (8 > 7) and $U$ = 0.971: correct;
    - margins of 2.46, 2.41 and 1.75 ms: correct;
    - Exercises 1–5: correct.
  - entry 5:
    - wrap program and stack-painting program outputs: identical;
    - Python script outputs (probabilities, margin RTA, load): identical;
    - Exercise 1 (8192 cycles, 170.7 µs), Exercise 2 (4.6 × 10⁶ runs, ≈5.1 h), Exercise 3 (30 %), and the size arithmetic (43 100 B ≈ 16 %, 7372 B ≈ 11 %): correct.
  - entry 5 `wakeup.c`: compiled cleanly. Three reruns gave:
    - absolute sleeping: medians 98.3, 102.1 and 107.3 µs; maxima 7029.1, 37925.2 and 34306.0 µs;
    - relative sleeping: drift of 303.0, 999.0 and 405.7 ms.

    The medians and the qualitative pattern agree with the article; the maxima and drift differ (F6).
- References checked:
  - Scheduling and timing papers: Liu & Layland (JACM 20(1), 1973); Leung & Whitehead (Performance Evaluation 2(4), 1982); Joseph & Pandya (Computer Journal 29(5), 1986); Audsley, Burns, Richardson, Tindell & Wellings (Software Engineering Journal 8(5), 1993); Sha, Rajkumar & Lehoczky (IEEE Trans. Computers 39(9), 1990); Davis, Burns, Bril & Lukkien (Real-Time Systems 35(3), 2007); Wilhelm et al. (ACM TECS 7(3), 2008, fifteen authors as listed).
  - Books: Buttazzo (3rd ed., Springer, 2011); Burns & Wellings (4th ed., Addison-Wesley, 2009); Kopetz (2nd ed., Springer, 2011); Lee & Seshia (2nd ed., MIT Press, 2017); Yiu (3rd ed., Newnes, 2014); White (O'Reilly, 2011); Ganssle (2nd ed., Newnes, 2008); Di Natale, Zeng, Giusto & Ghosal (Springer, 2012); Horowitz & Hill (3rd ed., CUP, 2015).
  - Specifications and standards: Bosch CAN Specification 2.0 (1991); ARM DDI 0403 (Armv7-M ARM); ISO/IEC 9899:2011; UM10204 rev 7.0 (1 October 2021, confirmed from the NXP document); TIA-232-F (1997); TIA-485-A (1998); ISO 11898-1:2015; ISO 11898-2:2016; IEEE Std 1003.1-2017 (published 2018).

  All are real works with the details given. Later editions of the last three are noted in F4/F5.
- Facts checked:
  - Cortex-M3/M4 entry of 12 cycles with zero-wait-state memory;
  - Armv7-M memory map regions;
  - basic exception frame of 8 words;
  - PRIMASK masks all configurable-priority exceptions; BASEPRI in Armv7-M;
  - PendSV used for context switching at lowest priority;
  - DWT CYCCNT optional in Armv7-M, absent in Armv6-M;
  - MSPLIM/PSPLIM in Armv8-M Mainline;
  - I2C limits per UM10204 (Sm/Fm/Fm+ $t_r$ 1000/300/120 ns, $C_b$ 400/400/550 pF, $I_{OL}$ 3/3/20 mA at 0.4 V; 16 reserved addresses; nine-clock bus clear; Hs 3.4 Mbit/s, UFm 5 Mbit/s);
  - CAN fault confinement (TEC +8, REC +1, −1 on success, error-passive above 127, bus-off above 255, recovery after 128 × 11 recessive bits);
  - nominal levels 2.5/3.5/1.5 V;
  - RS-485 32 unit loads;
  - RS-232 ±3 V receiver thresholds;
  - Mars Pathfinder account (1997 resets from priority inversion, fixed by enabling priority inheritance on the semaphore): accurate at the level of generality given.
- Not verified:
  - the original `wakeup.c` numbers in entry 5 (one session on a different shared machine; not reproducible by nature);
  - the exact text of ISO 11898 and TIA standards, which are paywalled. The values the articles take from them are the widely documented ones listed above.
