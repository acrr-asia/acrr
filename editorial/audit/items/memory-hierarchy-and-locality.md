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

## Fact-check

Stage EOS 6.3, 2026-10-16, by an independent reviewer (not the writer or copy editor). Network: WebSearch worked; WebFetch, DBLP, Crossref and OpenAlex were unreachable from this container (DNS failure / proxy 403), so bibliographic details were confirmed from search-result records (publisher, library and DOI landing pages and citing works), not from fetched primary pages. No URL is proposed.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Should fix | `:61`, Section 1.2 table | evidence | "20-way" for L3 is not in the quoted `lscpu`/`getconf` output and is not in the writer's saved outputs or `run.sh`. |
| F2 | Should fix | `:840`, `:845`, References | evidence | Two entries lack pages that exist: Goto and van de Geijn (article 12, pp. 12:1–12:25) and McCalpin (pp. 19–25). |
| F3 | Optional | `:611`, Section 4.5 | evidence | "blocks for registers and every cache level at once" is broader than what Goto and van de Geijn (2008) describe. |

### F1. Unsupported L3 associativity
- **Where:** `:61`, Section 1.2, table row "L3 cache"
- **Text:** "| L3 cache | 260 MiB as reported | 64-byte lines, 20-way | All cores of the processor |"
- **Problem:** Every other figure in the table is derived from the listing above it (L1 64 sets = 49 152/(64 × 12); L2 2048 sets = 2 097 152/(64 × 16)). The listing does not query `LEVEL3_CACHE_ASSOC`, `run.sh` does not either, and no saved output in `/tmp/claude-0/hpc/memory-hierarchy-and-locality/` contains a 20-way figure. The reference machine is not available to this reviewer (the container now runs on a different host that reports an 11-way, 33 MiB L3), so the value cannot be checked.
- **Correction:** Either add `LEVEL3_CACHE_ASSOC` to the `getconf` loop and its printed value to the listing (rerun on the reference machine), or write "| L3 cache | 260 MiB as reported | 64-byte lines | All cores of the processor |".

### F2. Incomplete references
- **Where:** `:840`, `:845`
- **Problem:** Standards 7.3: volume, issue and pages are given when they exist. Goto and van de Geijn, *ACM TOMS* 34(3), May 2008, is Article 12, pp. 12:1–12:25, DOI 10.1145/1356052.1356053 (BibSonomy record and FLAME publication list). McCalpin's newsletter article is cited with pp. 19–25, December 1995, by several citing works (secondary sources; the newsletter itself was not opened).
- **Correction:**
  - "K. Goto and R. A. van de Geijn, "Anatomy of high-performance matrix multiplication," *ACM Transactions on Mathematical Software*, vol. 34, no. 3, article 12, pp. 12:1–12:25, 2008."
  - "J. D. McCalpin, "Memory bandwidth and machine balance in current high performance computers," *IEEE Computer Society Technical Committee on Computer Architecture (TCCA) Newsletter*, pp. 19–25, December 1995."

### F3. Scope of the Goto attribution (optional)
- **Where:** `:611`
- **Text:** "It blocks for registers and every cache level at once, packs tiles into contiguous buffers so that they cannot conflict, and keeps a block of $C$ in vector registers in a hand-written kernel (Goto and van de Geijn, 2008)."
- **Problem:** The paper's layered model blocks for the registers, the L1 and L2 caches and the TLB (it argues that the block of $A$ belongs in L2, not L1); it does not claim to block for "every cache level". Packing and the register kernel are as stated.
- **Correction:** "It blocks for the registers, the caches and the TLB, packs tiles ..."

### Verification table

| Claim | Location | Status | Source |
|---|---|---|---|
| Roofline $P \le \min(P_{\mathrm{peak}}, BI)$; Williams, Waterman, Patterson, *CACM* 52(4):65–76, 2009 | `:14`, `:847` | verified | CACM record, DOI 10.1145/1498765.1498785; Berkeley TR EECS-2008-134 |
| "memory wall" coined by Wulf and McKee; *SIGARCH CAN* 23(1):20–24, 1995 | `:26`, `:848` | verified | DOI 10.1145/216585.216588; UVA Libra full text |
| Bandwidth improved faster than latency; Patterson, *CACM* 47(10):71–75, 2004 | `:26`, `:846` | verified | CACM Oct 2004 abstract (title printed "bandwith" in the ACM listing); DOI 10.1145/1022594.1022596 |
| McCalpin (1995) named machine balance; TCCA Newsletter, Dec 1995 | `:26`, `:845` | verified (pages from secondary citations) | McCalpin's UVA page title; Springer and ACM reference lists give pp. 19–25 |
| Hennessy and Patterson, 6th ed., Morgan Kaufmann, 2017 | `:841` | verified | ISBN 9780128119051, released December 2017 (some catalogs give the 2019 copyright year; 2017 is acceptable) |
| 3C classification due to M. D. Hill | `:221` | verified | University of Wisconsin profiles of Hill ("developed the 3C model of cache misses") |
| Hill's classification presented in H&P Appendix B; write-back usual (App. B); hierarchy argument (Ch. 2) | `:28`, `:215`, `:221` | not verified | book not accessible here; chapter titles consistent |
| Bryant and O'Hallaron, *CS:APP* 3rd ed., Pearson, 2016; memory mountain in Ch. 6 | `:338`, `:838` | verified | Pearson catalogue (©2016, Ch. 6 "The Memory Hierarchy"); course decks reproducing the CS:APP memory mountain (working-set size × stride) |
| Hong and Kung, STOC '81, pp. 326–333; $\Omega(n^3/\sqrt{S})$ I/O for standard matrix multiply | `:555`, `:842` | verified | paper copy (Rochester course page) with header and pp. 326–333 |
| Lam, Rothberg, Wolf, ASPLOS IV, pp. 63–74, 1991; self-interference; block size chosen per matrix; copying | `:557`, `:843` | verified | abstract and reference lists (ASPLOS-IV, Santa Clara, April 1991) |
| Little, *Operations Research* 9(3):383–387, 1961; $L = \lambda W$ | `:776`, `:844` | verified | DOI 10.1287/opre.9.3.383; Little (2011) retrospective |
| Goto and van de Geijn, *TOMS* 34(3), 2008; packing, register kernel | `:611`, `:840` | verified; see F2, F3 | BibSonomy record, DOI 10.1145/1356052.1356053 |
| Drepper, "What every programmer should know about memory," Red Hat, 2007 | `:217`, `:677`, `:697`, `:839` | verified (existence, date 21 Nov 2007) | LWN serialization; PDF listing |
| Drepper supports: page walk, prefetchers, non-temporal stores | same | not verified (passages) | sections 4 (virtual memory), 3.3.2/6.3 (prefetching) and 6.1 (bypassing the cache) exist by title; text not fetched |
| STREAM counts 24 bytes per triad element and reports the best rate | `:717`, `:770` | verified (common knowledge, and consistent with entry 1 Section 5.3) | McCalpin STREAM documentation (not fetched) |
| AVX-512 has 32 vector registers of 64 bytes | `:58` | verified | Intel SDM (standard knowledge); `avx512f` flag present |
| GCC 13.3, Python 3.13, NumPy 2.5 with OpenBLAS | `:18`, `:604` | verified locally | `gcc --version` 13.3.0; Python 3.13.16; NumPy 2.5.3, `show_config()` names scipy-openblas 0.3.34 |
| GCC enables `-floop-interchange` at `-O3` but did not interchange the matmul loops | `:599` | verified | `gcc -Q --help=optimizers -O3` shows it enabled; the `linterchange` dump of `matmul.c` reports no interchange |
| THP in `madvise` mode | `:679` | verified (current host) | `/sys/kernel/mm/transparent_hugepage/enabled` = `always [madvise] never` |
| x86-64 Linux scalar alignment equals size | `:617` | verified | System V x86-64 psABI (standard knowledge); program output 24/16 reproduced |
| Reference machine: 2.1 GHz Xeon, KVM, 48 KiB L1, 2 MiB L2, 260 MiB L3 | `:18`, `:36–53` | consistent with entries 1 and 3, not re-observed | the container now runs on a different host (2.80 GHz, 32 KiB L1, 1 MiB L2, 33 MiB L3) |

### Not verified
- L3 associativity "20-way" (`:61`): no output shown or saved (F1).
- H&P (2017) chapter and appendix locations (`:28`, `:215`, `:221`): book not accessible.
- Drepper (2007) passages on page walks, prefetching and non-temporal stores (`:217`, `:677`, `:697`): document not fetchable here; claims are standard and consistent with the paper's section titles.
- McCalpin pages 19–25: from secondary citations only.
- Reference-machine outputs that have no saved raw file in the writer's directory: the huge-page column (`:681–691`), the sequential chase (`:699–709`), the matmul timings (`:588–595`), the NumPy timings (`:606–609`) and the vectorization report (`:662–665`). They appear in the writer's drafts only. Not presumed fabricated: reruns on the current host reproduce every qualitative result (see Technical review), but the exact figures cannot be re-observed because the host changed.

**Fact-check verdict: fail.** No blocking finding; F1 and F2 (should fix) are open. F3 is optional.

## Technical review

Stage EOS 6.4, 2026-10-16, independent reviewer. Scratch files: `/tmp/claude-0/hpc/review/memory-hierarchy-and-locality/`.

**Host caveat.** This session's container is on a different host from the series' reference machine: `lscpu` now reports "Intel(R) Xeon(R) Processor @ 2.80GHz", L1d 32 KiB 8-way, L2 1 MiB 16-way, L3 33 MiB 11-way, `-march=native` = `cascadelake`. Deterministic results (simulator, structure sizes, the compiler's decisions) were checked exactly. Timings were rerun under `flock` on this host to test the qualitative claims only; the article's figures are measurements of the reference machine and are so labeled.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Blocking | `:660–667`, Section 5.2 | accuracy | "nothing for the AoS loop": GCC 13.3 vectorizes the AoS loop too; `run.sh` filtered its report line out. |
| T2 | Should fix | `:336`, Section 3.2 | accuracy | With padded rows the 256 KiB column fits in L2, so "fetched from beyond the caches up to eight times over" is wrong for that case. |
| T3 | Should fix | `:658`, Section 5.2 (copy C4) | accuracy | "both loops ran near 20 GB/s, the bandwidth limit" contradicts the 17.9 GB/s one-core figure of Section 6.3. |
| T4 | Should fix | `:580`, Section 4.4 | accuracy | Unpadded blocking does not lose "most of the advantage": it takes more misses than ikj. |
| T5 | Should fix | `:555`, Section 4.3 | accuracy | $M$ is defined in bytes and then reused in words. |
| T6 | Optional | `:693`, `:830` (copy C5) | accuracy | "a fifth to a third": measured 19% to 35%. |
| T7 | Optional | `:582` (copy C6) | accuracy | Write-backs are slightly below one $C$ tile per product. |
| T8 | Optional | `:717`, `:744` | accuracy | "initialized by the threads that will use it" is true only for the 1-thread pass. |
| T9 | Optional | `:693` | accuracy | "Within L1 and L2 the page size makes little difference": the 1 MiB row differs by 34%, within the stated spread. |

### T1. The AoS loop is vectorized (blocking)
- **Where:** `:660–667`, Section 5.2
- **Text:** "GCC's report (`-fopt-info-vec-optimized`) says, for the SoA loop: [two lines for `layout.c:35:26`] and nothing for the AoS loop, whose `x` values are 64 bytes apart."
- **Problem:** `run.sh` pipes the report through `grep "layout.c:3[0-9]"`, which keeps lines 30–39 only. `move_aos` is at line 29. Unfiltered, with GCC 13.3.0:
  ```text
  layout.c:29:26: optimized: loop vectorized using 32 byte vectors
  layout.c:35:26: optimized: loop vectorized using 32 byte vectors
  layout.c:35:26: optimized:  loop versioned for vectorization because of possible aliasing
  ```
  The same `layout.c:29:26` line appears with `-march=native` here and with `-march=skylake-avx512`, `cascadelake`, `icelake-server` and `sapphirerapids`, so it does not depend on which AVX-512 Xeon the reference machine has. The generated code (`gcc -O3 -march=native -S`) loads whole structures with 256-bit `vmovupd` and assembles the `x` and `vx` fields with `vpermt2pd`. The statement is false and its explanation ("whose `x` values are 64 bytes apart") argues for a result that did not happen.
- **Correction:** Replace the report block and the sentence after it by:
  > Layout also decides how the compiler can use **vector instructions**, which apply one operation to several adjacent values. GCC's report (`-fopt-info-vec-optimized`) for the two loops is:
  > ```text
  > layout.c:29:26: optimized: loop vectorized using 32 byte vectors
  > layout.c:35:26: optimized: loop vectorized using 32 byte vectors
  > layout.c:35:26: optimized:  loop versioned for vectorization because of possible aliasing
  > ```
  > Both loops were vectorized, but not in the same way. The SoA loop (line 35) loads four consecutive `x` and four consecutive `vx` with one instruction each. In the AoS loop (line 29) the `x` values are 64 bytes apart, so the compiler loads whole structures and gathers the fields into vectors with permute instructions, extra work that unit-stride fields avoid. A vector load reads consecutive memory, so unit-stride fields are what vector units need, as [Section 2 of the fourth entry](...) shows; here both loops were limited by bandwidth, so the difference did not matter.

  Change the `run.sh` filter to `grep -E "layout.c:(29|3[0-9]):"` and regenerate the block on the reference machine before publishing. Keep the following sentence on the array of structures of arrays.

### T2. The padded column fits in L2
- **Where:** `:336`, Section 3.2
- **Text:** "The column order uses one and moves on; when it returns for the next column, 4096 lines later, the line has long been evicted from L1 and L2, so the array is fetched from beyond the caches up to eight times over."
- **Problem:** A column is 4096 lines, 256 KiB. With `ld = 4096` the rows are 32 KiB (512 lines) apart, so a column maps to only 4 of the 2048 L2 sets (64 lines), and it is evicted, by conflict. With `ld = 4104` the row stride is 513 lines, which is odd, so the column spreads evenly over all 2048 sets (2 lines per set) and fits in the 2 MiB, 16-way L2 by capacity. The article's own simulator, configured as the reference L1 and L2 (`l2col.py`, exact LRU), gives:
  ```text
  ld=4096 column, L1 48 KiB 12-way   misses 16777216  (compulsory 2097152, capacity 14680064, conflict 0)
  ld=4096 column, L2 2 MiB 16-way    misses 16777216  (compulsory 2097152, capacity 0, conflict 14680064)
  ld=4104 column, L1 48 KiB 12-way   misses 16777216  (compulsory 2097152, capacity 14680064, conflict 0)
  ld=4104 column, L2 2 MiB 16-way    misses  2097152  (compulsory 2097152, capacity 0, conflict 0)
  ```
  So with padding the array crosses the L2 boundary once, not eight times. Each column access also lands on a new 4 KiB page (4096 pages, 16 MiB, beyond the assumed 8 MiB TLB reach). On the current host, a variant of `traverse.c` on memory marked `MADV_HUGEPAGE` cut column order from 12.40 to 9.83 ns/element (`ld = 4096`) and from 12.05 to 9.03 ns/element (`ld = 4104`), with row order unchanged (`run_trav_huge.txt`). Translation is part of the cost.
- **Correction:** "The column order uses one and moves on. When it returns for the next column, 4096 lines (256 KiB) later, the line has long been evicted from the 48 KiB L1. With rows of exactly 4096 doubles, a column also maps to only 4 of the 2048 L2 sets, so it is evicted from L2 as well (the mechanism of Section 3.3), and the array is fetched from beyond L2 up to eight times over; with padded rows the column fits in L2. In both cases each access lands on a different 4 KiB page, so address translation (Section 6.1) adds to the cost."

### T3. Particle-loop bandwidth (copy finding C4)
- **Where:** `:658`, Section 5.2
- **Text:** "The traffic ratio, $2048/384 = 5.3$, is close to the measured 4.9; both loops ran near 20 GB/s, the bandwidth limit."
- **Problem:** Recomputed: AoS $2\ \text{GiB}/100.97\ \text{ms} = 21.3$ GB/s; SoA $384\ \text{MiB}/20.56\ \text{ms} = 19.6$ GB/s. Section 6.3 gives one core 13.4 GB/s by the STREAM count, $13.4 \times 32/24 = 17.9$ GB/s of actual traffic. So "the bandwidth limit" is not one number. The difference is reproducible and not noise: on the current host, one-thread triad 11.7 GB/s (15.6 GB/s with write-allocate) against AoS 16.8 GB/s and SoA 16.0 GB/s, the same ordering (`run_triad.txt`, `run_layout.txt`). The in-place update reads every line it writes, so it pays no extra write-allocate read, and it has fewer streams than the triad. The loops are still memory-bound (1 GiB of data, intensities far below the ridge point).
- **Correction:** "The traffic ratio, $2048/384 = 5.3$, is close to the measured 4.9. Counted this way, both loops moved about 20 GB/s (21.3 and 19.6 GB/s), somewhat more than the 17.9 GB/s that the one-core triad of Section 6.3 moved; how much one core sustains depends on the mix of reads and writes, but both loops were limited by memory bandwidth, not by arithmetic." Exercise 4's "at 20 GB/s" is an assumption and can stay.

### T4. Unpadded blocking is worse than ikj
- **Where:** `:580`, Section 4.4
- **Text:** "about 30 000 conflict misses, and most of the advantage over ikj is lost."
- **Problem:** Printed: blocked $b = 8$ 38 216 misses and $b = 16$ 36 864, ikj 33 792. Ratios 1.13 and 1.09: unpadded blocking took more misses than ikj, so all the advantage is lost, and more.
- **Correction:** "about 30 000 conflict misses, so the blocked loop takes more misses than ikj (38 216 and 36 864 against 33 792). The tile size was right; the addresses were wrong."

### T5. $M$ in bytes and in words
- **Where:** `:555`, Section 4.3
- **Text:** "three tiles must fit in $M$ bytes, $24\,b^2 \le M$, so the traffic for the whole product is proportional to $n^3/\sqrt{M}$. ... with a fast memory of $M$ words, moves on the order of $n^3/\sqrt{M}$ words"
- **Problem:** One symbol, two units (standards 5.5). The order-of-magnitude statement survives (a factor of 8 inside the root is a constant), but the reader is told two different things about $M$.
- **Correction:** "...Hong and Kung (1981) proved that this is optimal up to a constant factor: any evaluation of the $n^3$ products of the standard algorithm with a fast memory of $M$ bytes moves on the order of $n^3/\sqrt{M}$ bytes between fast and slow memory (they counted words, which changes only the constant)."

### T6. "A fifth to a third" (copy finding C5, optional)
Recomputed reductions: 39.8 ns (34.7%) at 32 MiB, 34.3 ns (18.8%) at 64 MiB, 47.4 ns (21.3%) at 256 MiB, 59.3 ns (22.0%) at 1 GiB. Correction: "about a fifth to a third" at `:693` and `:830`, or "19% to 35%". The "34 to 59 ns" range is correct.

### T7. Write-back count (copy finding C6, optional)
Agree. One $C$ tile per product predicts 512 × 8 = 4096 ($b = 8$) and 64 × 32 = 2048 ($b = 16$); printed 4088/4071 and 2040/2032 because lines still dirty at the end of the run are never evicted. Correction: "are close to one $C$ tile per tile product (lines still dirty at the end of the run are not counted), the $8b^2$ term above."

### T8. First touch in the triad (optional)
- **Where:** `:717` "each initialized by the threads that will use it"; code comment `:744`.
- **Problem:** Pages are placed when first touched, which is in the 1-thread pass ($k = 0$); the re-initialization by 2 and 4 threads touches pages that already exist. On this one-memory-node virtual machine (`lscpu`: 1 NUMA node) placement has no effect, so no number changes.
- **Correction:** `:717` "arrays of 1 GiB, initialized with the same static schedule as the triad"; comment "Initialized with the triad's schedule. (Pages are placed at their first touch, in the 1-thread pass; this machine has one memory node, so placement does not matter.)"

### T9. Page size within L2 (optional)
`:693` "Within L1 and L2 the page size makes little difference." The 1 MiB row gives 9.84 against 6.51 ns (−34%); `:178` already notes that this row gave 6.25 ns in another 4 KiB run, so the difference is within the spread. Correction: "Within L1 and L2 the page size makes little difference beyond the run-to-run spread."

### Checked and correct
- **Code listings match the programs.** The article's `latency.c`, `traverse.c`, `cachesim.py` and `triad.c` are byte-identical to the writer's files; every line of the `mm_*` and layout fragments occurs in `matmul.c` and `layout.c`. All five C programs compile with GCC 13.3.0 at the stated flags without warnings.
- **Simulator output matches exactly.** `python3 cachesim.py` reproduces both quoted blocks character for character; Exercise 2 prints `accesses 1024 misses 1024 (compulsory 128, capacity 0, conflict 896)` as stated.
- **Hand derivations (Sections 3.3, 4.4).** Line of $(i, j)$ = $8i + \lfloor j/8\rfloor$ ($ld = 64$, two sets, 3584 conflicts); $9i + \lfloor j/8\rfloor$ ($ld = 72$, 16 sets × 4 lines, 512 misses); $128 \times 128$ capacity misses. ikj $64 \times 528 = 33\,792$; blocked padded $b = 16$: 64 products × (32 for the resident $B$ tile + 16 rows × (2 + 2) for $A$ and $C$) = 6144; ratio 5.5; ijk/ikj 8.04. Unpadded tiles fall in 2 ($b = 8$) or 4 ($b = 16$) sets: correct.
- **Cache geometry and addresses.** $S$ = 64 (L1), 2048 (L2). `0x7ffd1234`: offset 52, index 8, period 4096. Exercise 1: sets 0 and 1; 16 lines in a 12-way set, conflict misses, 768-line fully associative cache. L2 at 8192-byte stride: 16 sets, 256 lines against 1024.
- **Intensity derivations.** $2n^3/32n^2 = n/16$ (64 at $n = 1024$); ijk 2 FLOP per 64-byte line; ikj $2/8 = 0.25$; tile $2b^3/32b^2 = b/16$, $b/12$ without write-backs, $b/8$ with `kk` innermost, consistent with entry 1 Section 5.2 ($16n^3/b$ traffic, $b/8$); $24b^2 \le M$ gives traffic ∝ $n^3/\sqrt{M}$. Exercise 3: $b \le 295.6$, 1.5 MiB at $b = 256$, 16 and 21.3 FLOP/byte. Exercise 4: 1.28 GB, 64 ms; 0.40 GB, 20 ms; ratio 3.2.
- **Numbers from outputs** (`recompute.py`): ridge $90.6/13.4 = 6.76$, 54 FLOP per double (90.6 is the median of entry 1's five 1-thread runs); 269.39/1.5 = 180; column/row 11.3; 128 MiB array; stride timings reproduce the printed ns/element within the rounding of the ms column; stride 64/stride 8 = 0.32; matmul GFLOP/s all match (0.29, 2.13, 6.36, 8.34, 5.90, 8.45, 61.7, 56.25); 21.9×, 7.89× for 7.4% more work, 1.31× and 1.43×, 96 KiB tiles, 32 MiB matrix; NumPy 7.4× and 6.7× the blocked loop, 68% and 62% of 90.6; structure 14 wasted bytes, one third saved; AoS/SoA 4.91, traffic ratio 5.33; TLB reach 8 MiB, ×512; huge-page climb 86.8 → 61.7 ns; seq/rand 35.8; triad 13.37, 24.74, 45.63 GB/s, $I = 0.083$, bound 3.8 GFLOP/s, 17.87 GB/s with write-allocate, 4t/1t 3.40; Little's law 2685 bytes, 42 lines.
- **Compiler claims.** `-floop-interchange` is enabled at `-O3` in GCC 13.3, and the `-fdump-tree-linterchange-details` dump of `matmul.c` records no interchange: "GCC at `-O3` did not interchange the loops" holds. The SoA report lines (`layout.c:35:26`, 32-byte vectors, versioned for aliasing) reproduce exactly.
- **Mechanisms.** Pointer-chase design (dependent loads, one line per element, shuffled cycle; the `perm[i] → perm[i+1]` links form one cycle whatever the shuffle) is sound. Write-allocate doubling, 3C definitions (simulator classifies with the fully associative LRU shadow as stated), the LRU caveat, the Little's law argument and the saturation caveat are correct and qualified. Cross-references to entries 1, 3 and 4 resolve to existing headings (`#5-the-roofline-bound`, `#52-…`, `#53-…`, `#54-…`, `#6-measuring-performance-honestly`, `#5-synchronization-cost-and-false-sharing`, `#2-vector-instructions-on-a-cpu`), and the values reused from entry 1 (90.6 GFLOP/s, 7.08, 12.3–13.2 GB/s, 0.125, $b/8$) agree with it.
- **Qualification.** Timings are stated as medians from the reference machine only; the 260 MiB L3 and the assumed TLB size are labeled; interpretations ("one reading", "one plausible reading", "an inference") are marked.

### Run log (current host, under `flock /tmp/claude-0/hpc/bench.lock`)

| Program | Result here | Article (reference machine) | Qualitative claim |
|---|---|---|---|
| `traverse` | row 24.4/25.3 ms, column 198.6/215.8 ms; strides 48.4 → 5.6 ms | 18.0/14.9, 202.9/166.8; 43.3 → 5.7 | column ≫ row (8×); stride-1 slower than stride-8; stride 64 ≈ a third of stride 8: hold. Padding did not speed column order here (consistent with T2). |
| `layout` | 24/16 bytes; AoS 127.51 ms, SoA 25.09 ms (5.1×) | 100.97, 20.56 (4.9×) | holds |
| `triad` | 11.7, 22.3, 37.1 GB/s (median) | 13.4, 24.7, 45.6 | near-linear rise with threads: holds (3.2× here) |
| `latency rand 4k` | L1 ≈1.6 ns, L2 ≈4.3 ns, 1 GiB 350.7 ns; DRAM-like step at 8 MiB | 1.5, 5, 269.4; step at 32–64 MiB | plateaus and an early step below the reported L3: hold |
| `latency rand huge` | 1 GiB 220.9 ns (−37%) | 210.1 (−22%) | huge pages cut large-working-set latency: holds |
| `latency seq 4k` | 1 GiB 9.08 ns (39× faster than random) | 7.52 (36×) | holds |
| `matmul_o3` | ijk 1024 3175 ms, 1000 1491 ms; ikj 332/5689 ms; blocked 311.5/2503 ms; all max difference 0 | 7402, 938; 337.5/2914; 257.6/2032 | loop order 9.6× here (22× there); blocking gain grows at $n = 2048$ (1.07× → 2.27×): hold. The power-of-two penalty is 2.1× here against 7.9× there; this host's L2 (1024 sets) holds 128 lines of an 8 KiB-stride column, so the size is machine-specific as the text implies. |
| `numpy_mm.py` | 55.1 and 63.4 GFLOP/s | 61.7, 56.3 | library ≈7–9× the blocked loop: holds |
| `l2col.py` (deterministic) | see T2 | — | — |
| `trav_huge.c` (variant) | column 12.40/12.05 → 9.83/9.03 ns with huge pages | — | see T2 |

**Technical verdict: fail.** T1 (blocking) and T2 to T5 (should fix) are open. T6 to T9 are optional. C4 is resolved as T3, C5 as T6 and C6 as T7.

## Resolution

Stage EOS step 7, 2026-10-16, by the writer. The container no longer runs on the reference machine, so no timing was rerun and no measured number was changed. The only regenerated output is the compiler report for T1, which does not depend on the host.

| ID | Severity | Resolution |
|---|---|---|
| T1 | Blocking | Applied with the reviewer's text. The report was regenerated with the fixed filter, `gcc -std=c11 -O3 -march=sapphirerapids -fopt-info-vec-optimized -c layout.c` piped through `grep -E "layout.c:(29\|3[0-9]):"` (GCC 13.3.0). It prints the three lines the reviewer gives, including `layout.c:29:26` for the AoS loop. The text now says the report was produced with `-march=sapphirerapids` in place of `-march=native`, and why. `run.sh` was updated to the new command and filter. |
| T2 | Should fix | Applied with the reviewer's text, split into shorter sentences. The 4104-element row stride is 513 lines, odd and so coprime with 2048 sets, which confirms that the padded column fits in L2. |
| T3 | Should fix | Applied with the reviewer's text (21.3 and 19.6 GB/s against the triad's 17.9 GB/s), split into two sentences. Exercise 4 keeps its stated assumption of 20 GB/s. |
| T4 | Should fix | Applied: the blocked loop takes more misses than ikj (38 216 and 36 864 against 33 792). |
| T5 | Should fix | Applied: $M$ is in bytes throughout, with the note that Hong and Kung counted words, which changes only the constant. |
| F1 | Should fix | Applied: "20-way" removed from the L3 row. |
| F2 | Should fix | Applied: Goto and van de Geijn now give article 12, pp. 12:1–12:25; McCalpin gives pp. 19–25. |
| F3 | Optional | Applied: "It blocks for the registers, the caches and the translation lookaside buffer (Section 6.1)". The abbreviation is avoided because it is first expanded in Section 6.1. |
| T6 | Optional | Applied: "about a fifth to a third" in Section 6.1 and in the Summary. |
| T7 | Optional | Applied: "close to one $C$ tile per tile product (lines still dirty at the end of the run are not counted)". |
| T8 | Optional | Applied: the text reads "initialized with the same static schedule as the triad". The code comment was replaced in both the article listing and `triad.c`, so they stay identical. The change is to a comment only, so the output is unchanged. |
| T9 | Optional | Applied: "makes little difference beyond the run-to-run spread". |

`eos lint` (after): 0 errors, 0 warnings, 6 suggestions. These are the GNU, STREAM and ACM names, as kept in the copy edit, and three sentence-length false positives.
