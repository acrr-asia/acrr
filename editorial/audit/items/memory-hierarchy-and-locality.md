# Editorial review: The Memory Hierarchy and Locality

- Path: `src/content/blog/memory-hierarchy-and-locality.mdx` · Route: `/blog/memory-hierarchy-and-locality` · Type: article · Series `parallel-and-high-performance-computing`, entry 2 of 5 · Words: about 10,000 (including code and output)
- Stages in this report: developmental (EOS 6.1) and copy edit (EOS 6.2), 2026-10-16. Later stages (fact-check, technical review, resolution, QA) append their own sections below.
- Inputs read: `editorial/standards.md`, `editorial/glossary.json`, `CLAUDE.md`, the series overview, this entry in full, and the headings and cited sections of entries 1, 3 and 4.
- Line numbers refer to the file after this stage's edits.

## Developmental review

The entry does its job well. It opens from the roofline bound of the first entry, says what it adds (where the bytes come from and how to reduce them), and states versions, machine and units. Each concept comes before its mechanics: lines before sets, the miss kinds before the simulator that counts them, reuse before tiling. Every major claim is backed by a measurement, a hand derivation of a simulator count, or a citation. Limits are stated in the sections they apply to (virtual-machine noise, the reported L3 that the guest does not appear to get, the simulator's exact LRU, an assumed TLB size). The exercises are computational, and their answers follow from the text. The summary table and closing paragraph lead on to the third entry. All four findings concern presentation.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:16`, opening | purpose | Second opening paragraph was a table of contents in prose and did not state the assumed background. |
| D2 | Should fix | `:30`, Section 1.1 | consistency | "Section 6.3" directly after "Section 5.4 of the first entry" read as a section of the first entry. |
| D3 | Should fix | `:834`, Section 8 | evidence | Closing claim "by factors that dwarf most arithmetic optimizations" generalized beyond what the entry measures. |
| D4 | Optional | `:602–611`, Section 4.5 | structure | The fourth result bullet ran on into a code block outside the list, and the "seven times faster" result came only after the output. |

### D1. Opening reads as a table of contents
- **Where:** `:16`, opening paragraphs
- **Text:** "It treats the memory hierarchy, how a cache works, locality in loops, blocking, data layout and finally translation, prefetching and bandwidth. Each idea is measured on one machine or, where a timing would be too noisy, counted exactly with a small cache simulator that the reader can run."
- **Problem:** Standards 6.1 and 6.2 (item 1) and the developmental brief (item 6) say the opening states what the entry builds on and assumes, and does not list the sections in prose. The section list repeated the headings. The stated reason for the simulator ("too noisy") also differed from the reason Section 3.3 gives: timings show *that* order matters but not *why*, and miss counters are unavailable in the virtual machine.
- **Correction (applied):** "The entry assumes the roofline bound and the measurement practice of the first entry, and a reading knowledge of C and Python. Every program runs on one core except the bandwidth test at the end. Each effect is measured on one machine or, where a timing shows that order matters but not why, counted exactly with a small cache simulator that the reader can run." (The one-core statement repeats what the Summary already says at `:834`.)

### D2. Ambiguous section reference
- **Where:** `:30`, Section 1.1
- **Text:** "...in the fused multiply-add microbenchmark of [Section 5.4 of the first entry](...) and sustained 13.4 GB/s from DRAM on the streaming loop of Section 6.3."
- **Problem:** Coming right after a section of the first entry, "Section 6.3" reads as Section 6.3 of the first entry ("Problem size and compiler settings"). The 13.4 GB/s actually comes from this entry's triad in Section 6.3.
- **Correction (applied):** "...on the streaming triad of Section 6.3 below."

### D3. Unsupported generalization in the ending
- **Where:** `:834`, Section 8, closing paragraph
- **Text:** "Loop order, blocking and data layout arrange this, and they change the bytes moved, the $I$ of the roofline, by factors that dwarf most arithmetic optimizations."
- **Problem:** The entry measures no arithmetic optimization, so "dwarf most arithmetic optimizations" is a claim with no evidence in the text (standards 6.1, evidence; 2.3, no overclaiming). Also, the factors the entry does measure are run-time ratios, not byte ratios alone.
- **Correction (applied):** "Loop order, blocking and data layout arrange this. They change the bytes moved, the $I$ of the roofline, and with them the run time: on the reference machine, loop order alone gave a factor of 22 for matrix multiply and the particle layout a factor of 4.9." (Both numbers come from Sections 4.5 and 5.2.)

### D4. List item that runs into a code block
- **Where:** `:602–611`, Section 4.5
- **Text:** "- **These loops are far from the machine's capability.** NumPy's `a @ b` calls the OpenBLAS implementation ... `OPENBLAS_NUM_THREADS=1`:" followed by the output and then "The library is seven times faster than the blocked loop and ..."
- **Problem:** The colon at the end of a list item introduced a code block that renders outside the list. The bullet also did not state its result: "seven times faster" came only after the output.
- **Correction (applied):** The bullet now states its result: "A tuned library multiplies the same matrices seven times faster than the blocked loop." A separate paragraph introduces the NumPy/OpenBLAS output, and the paragraph after the output begins "It reached about two-thirds of ...". No number changed.

### Considered and not raised
- The Mermaid lookup flowchart (Section 2.1) earns its place: it shows the order of the hit/miss steps, including write-back of a dirty victim, which the prose does not spell out.
- The forward references (Sections 2.4 → 3.3, 1.3 → 6.1/6.2) are signposted and do not assume material the reader needs at that point.
- `###` headings: none renamed or renumbered. Incoming links from entries 1, 3 and 4 target `#2-how-a-cache-works`, `#23-writes`, `#4-blocking-for-reuse`, `#5-data-layout`, `#53-layout-and-threads`, `#6-translation-prefetching-and-bandwidth` and `#64-what-limits-one-core-and-what-limits-many`, and all remain valid.

**Developmental verdict: pass.** D1 to D3 (should fix) and D4 (optional) are applied, and no blocking or should-fix finding is open.

## Copy edit

`eos lint` (before): 0 errors, 0 warnings, 9 suggestions. `eos fix --rules spelling-variant,terminology`: 0 fixes needed. A manual check found no em dashes, contractions, serial commas, "simply/obviously/clearly/of course", or "we"/"our". Headings are in sentence case and numbered in sequence.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:217`, `:679` | language | Two long sentences (48 and 46 words) joined independent points (lint `sentence-length`). |
| C2 | Should fix | `:186` | language | A comma between the subject and the verb in the definition of $S$. |
| C3 | Optional | `:14`, `:176`, `:184`, `:809` | language | "eight times more of them" (ambiguous); a sentence-initial "And"; a "This" with no noun; a misread serial-comma pattern in Exercise 4. |
| C4 | Should fix | `:658`, `:809` | accuracy | For the technical reviewer: "both loops ran near 20 GB/s, the bandwidth limit" does not match the one-core bandwidth of Section 6.3. |
| C5 | Optional | `:693`, `:830` | accuracy | For the technical reviewer: "a fifth to a third" understates the largest reduction (35% at 32 MiB). |
| C6 | Optional | `:582` | accuracy | For the technical reviewer: "one $C$ tile per tile product" is slightly above the printed write-back counts. |

### C1. Long sentences
- **Where:** `:217`, Section 2.3; `:679`, Section 6.1
- **Text:** "Write-back caches normally write-allocate, so a loop that only writes an array, such as `a[i] = 0`, still reads every line of `a` before overwriting it and moves twice the bytes its source code suggests." / "This virtual processor does not report its TLB sizes; an assumed 2048 entries would cover 8 MiB with 4 KiB pages, beyond which a random pattern also misses in the TLB."
- **Correction (applied):** "Write-back caches normally write-allocate. A loop that only writes an array, such as `a[i] = 0`, therefore still reads every line of `a` before overwriting it, and moves twice the bytes its source code suggests." / "This virtual processor does not report its TLB sizes. An assumed 2048 entries would cover 8 MiB with 4 KiB pages; beyond that, a random pattern also misses in the TLB."

### C2. Comma between subject and verb
- **Where:** `:186`, Section 2.1
- **Text:** "A cache of capacity $C$ bytes, with line size $L$ bytes and **associativity** $W$ (...) has"
- **Correction (applied):** The comma after "$C$ bytes" is removed.

### C3. Small wording fixes (applied)
- `:14` "move eight times more of them" → "move eight times as many of them" (same meaning, no "more than" ambiguity).
- `:176` "And the step to DRAM-like latency" → "Finally, the step to DRAM-like latency".
- `:184` "This is the first reason" → "This granularity is the first reason".
- `:809` "Estimate the bytes moved per particle in AoS and in SoA layout, counting write-backs, and the time each takes" → "Counting write-backs, estimate the bytes moved per particle in AoS and in SoA layout and the time each takes" (removes the false serial-comma reading that lint flagged).

### C4. Bandwidth figure in Section 5.2 (for the technical reviewer; text left unchanged)
- **Where:** `:658`, Section 5.2; also Exercise 4 at `:809` ("at 20 GB/s")
- **Text:** "The traffic ratio, $2048/384 = 5.3$, is close to the measured 4.9; both loops ran near 20 GB/s, the bandwidth limit."
- **Problem:** Recomputed from the printed times: AoS 2 GiB / 100.97 ms = 21.3 GB/s, and SoA 384 MiB / 20.56 ms = 19.6 GB/s. Section 6.3 gives the one-core bandwidth as 13.4 GB/s by the STREAM count, or 17.9 GB/s counting write-allocate. The single-threaded particle loops therefore ran faster than the stated one-core limit, and "the bandwidth limit" is not reconciled with Section 6.3. Possible explanations include a different read-to-write mix, run-to-run noise, or part of the data hitting in the reported L3. Settling this needs a technical judgment, not a copy change.
- **Correction:** For the technical reviewer: reconcile the two figures (for example, "both loops ran at about 20 GB/s, above the 17.9 GB/s of the triad in Section 6.3, which ...") or qualify "the bandwidth limit".

### C5. "A fifth to a third" (for the technical reviewer; text left unchanged)
- **Where:** `:693`, Section 6.1; repeated in the Summary at `:830`
- **Text:** "From 32 MiB up, huge pages removed 34 to 59 ns per access, a fifth to a third of the latency"
- **Problem:** Recomputed from the table: 39.8/114.74 = 35% (32 MiB), 34.3/182.63 = 19% (64 MiB), 47.4/222.16 = 21% (256 MiB) and 59.3/269.39 = 22% (1 GiB). The range is 19% to 35%, so "a third" is slightly low at the top.
- **Correction:** Optional. "about a fifth to a third", or "19% to 35%".

### C6. Write-back count (for the technical reviewer; text left unchanged)
- **Where:** `:582`, Section 4.4
- **Text:** "The write-backs (dirty lines evicted during the run) of the blocked loops are one $C$ tile per tile product, the $8b^2$ term above."
- **Problem:** One tile per product predicts 4096 lines ($b = 8$) and 2048 lines ($b = 16$). The printed counts are 4088/4071 and 2040/2032, because lines still dirty at the end of the run are never evicted.
- **Correction:** Optional. "close to one $C$ tile per tile product (lines still dirty at the end are not counted)".

### Lint suggestions kept
- `18:59 acronym-expansion "GNU"`: GNU is the project's name (a recursive acronym), and the text already expands it as "GNU Compiler Collection (GCC)".
- `717:185 acronym-expansion "STREAM"`: STREAM is the benchmark's proper name, attributed to McCalpin (1995).
- `840:89 acronym-expansion "ACM"`: this is in the reference list, where publication names keep their original form.
- `233:1`, `772:50`, `776:1 sentence-length`: false positives. The sentences on these lines are short (the longest is about 30 words); the linter treats bold-led definitions and decimal numbers such as "45.6, 3.4" as one sentence.

`eos lint` (after): 0 errors, 0 warnings, 6 suggestions (all listed above with reasons).

**Copy verdict: pass.** C1 and C2 (should fix) are applied. C4 is a should-fix finding about accuracy, handed to the technical reviewer under the brief's rule that copy editing does not change technical claims; it is not an open copy finding. C3 is applied; C5 and C6 are optional and left for the technical reviewer.

<!-- Later stages: Fact-check, Technical review, Resolution, QA -->
