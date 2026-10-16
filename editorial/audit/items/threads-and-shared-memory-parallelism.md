# Editorial review: Threads and Shared-Memory Parallelism

Item: `src/content/blog/threads-and-shared-memory-parallelism.mdx` (series `parallel-and-high-performance-computing`, entry 3 of 5).
Stages in this report: developmental review (EOS 6.1) and copy edit (EOS 6.2), performed by an editor who did not write the draft. Fact-check, technical review, resolution and QA sections are to be added by their reviewers below.

Inputs read: `editorial/standards.md`, `editorial/glossary.json`, `CLAUDE.md`, the series overview, the article in full, and the headings and cited sections of the first, second, fourth and fifth entries (`performance-models-and-scaling-laws`, `memory-hierarchy-and-locality`, `data-parallelism-vector-units-and-gpus`, `distributed-memory-and-message-passing`). All cross-entry links in the article were checked against the target headings: every fragment exists (`#2-amdahls-law-and-strong-scaling`, `#4-work-span-and-parallelism`, `#5-the-roofline-bound`, `#42-greedy-scheduling-and-brents-bound`, `#2-how-a-cache-works`, `#23-writes`, `#53-layout-and-threads`, `#6-translation-prefetching-and-bandwidth`, `#64-what-limits-one-core-and-what-limits-many`).

## Developmental review

Overall: the entry does its job for the series reader. The opening links what it builds on and states versions, flags and the machine; every section opens with its concept before code or output; each failure mode is demonstrated with a run program and then explained; limits are stated in the sections (noise, the unverified explanation of the plain-increment result, the triad's failure to saturate bandwidth); the Summary table and closing paragraph lead to the fourth entry; Exercises have answers; References are in house format. The findings below are structural refinements.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:16`, opening | structure | Second opening paragraph was a table of contents in prose |
| D2 | Should fix | Section 5, old 5.2/5.3 | structure | The critical-section subsection was separated from the lock costs it extends by the false-sharing subsection |
| D3 | Should fix | Section 2.3 end, Section 2.4 end | structure | Two orphan sentences placed away from the material they qualify |
| D4 | Should fix | `:660`, Summary closing paragraph | purpose | Closing sentence attributed idle threads to careless data sharing |
| D5 | Optional | Section 6.5, last sentence | structure | Final sentence restated its own first clause |
| D6 | Optional | Section 4.3 | accuracy | For the technical reviewer: "the only reordering other threads can see" omits store forwarding |
| D7 | Optional | Section 4.3 | accuracy | For the technical reviewer: confirm GCC 13 emits `xchg` for a seq_cst store |

### D1. Opening paragraph lists sections
- **Where:** `src/content/blog/threads-and-shared-memory-parallelism.mdx:16`, opening
- **Text:** "Sections 1 and 2 describe threads and parallelize loops with OpenMP. Sections 3 to 6 treat what goes wrong: ..."
- **Problem:** Standards 6.1 and the developmental-editor brief ask the introduction to set up the argument without a table of contents in prose. The paragraph named section numbers instead of the tension the entry resolves.
- **Correction (applied):** "Sharing memory makes parallel code easy to start and easy to get wrong. One directive can make a loop run nearly four times faster on four cores, and the same directive on a slightly different loop can give a wrong result or a slower program without any warning. The entry first shows threads and OpenMP loops working as intended, then measures each way in which they fail: ..." (The "nearly four times" restates the measured 3.87 of Section 2.4; no new number.)

### D2. Critical section placed after false sharing
- **Where:** Section 5, former "5.2 False sharing" and "5.3 A critical section as a serial fraction"
- **Text:** 5.1 ends "The contended increments of Section 3.3, at about 53 and 240 ns, are the same cost on a smaller scale." and the lock-as-serial-fraction analysis came only after false sharing.
- **Problem:** 5.1 measures barriers and locks; the critical-section model is the direct continuation (what a lock's serialization does to speedup). False sharing is a separate cost with its own cause and remedies. The old order interrupted the lock argument.
- **Correction (applied):** swapped the two subsections: 5.2 is now "A critical section as a serial fraction", 5.3 "False sharing". Internal references updated ("the bound of Section 5.2" twice in Exercise 1). The section heading "## 5. Synchronization cost and false sharing" is unchanged and now matches the order. No other file links to either `###` fragment (grep of `src/` for `threads-and-shared-memory-parallelism#5[23]`: no hits; incoming links target only `#3-...`, `#5-...` and `#6-...`).

### D3. Orphan sentences
- **Where:** end of Section 2.3 and end of Section 2.4
- **Text:** "Times are taken with `omp_get_wtime()`, ..." (closing 2.3, before any timing appears); "The 24 bytes per element follow the STREAM convention; ..." (closing 2.4, after the conclusion about $B$).
- **Problem:** Each qualifies material elsewhere: the timer belongs with the first timed program; the byte-count convention belongs where $I = 2/24$ is stated. Placed at the end, the second one undercut the section's conclusion.
- **Correction (applied):** moved the timer sentence into the introduction of `loops.c` in 2.4, and the STREAM convention sentence directly after "The triad has $I = 2/24 \approx 0.083$ FLOP/byte", followed by "Either way, its roofline bound is $B\,I$ ...". Wording unchanged otherwise.

### D4. Closing paragraph misattributes load imbalance
- **Where:** Summary, closing paragraph
- **Text:** "races, reorderings, contended lines and idle threads undid that gain wherever the threads shared data carelessly."
- **Problem:** Idle threads (Section 6) come from uneven division of work, not from data sharing; the sentence misstated the entry's own result.
- **Correction (applied):** "Races, reorderings and contended cache lines undid that gain wherever threads shared data carelessly, and idle threads undid it wherever the work was divided unevenly."

### D5. Redundant ending of Section 6.5
- **Text:** "Load imbalance is not a lack of parallelism but a failure to use it, and the schedule decides whether the parallelism of the work-span analysis is used."
- **Correction (applied):** "..., and the schedule is what decides whether it is used."

### D6. TSO "only reordering" (for the technical reviewer)
- **Where:** Section 4.3
- **Text:** "the only reordering other threads can see is a load that completes before an earlier store of the same thread, to a different address, has left the buffer."
- **Problem:** In x86-TSO a thread can also read its own buffered store before other threads see it (store forwarding), which some litmus tests observe; the sentence may be a deliberate simplification. Not changed. Technical reviewer to decide whether "the main reordering" or a qualifier is needed.

### D7. seq_cst store code generation (for the technical reviewer)
- **Where:** Section 4.3
- **Text:** "GCC compiles such a store to `xchg`, which drains the store buffer before the load runs."
- **Problem:** Older GCC releases used `mov` plus `mfence`; the claim should be confirmed against the disassembly of `litmus.c` built with GCC 13.3. Not changed.

Changes made in this stage: D1 to D5 applied as above. Nothing technical, numerical, code, output, citation or link target was changed.

Counts: 0 blocking, 4 should fix (all applied), 3 optional (D5 applied; D6 and D7 left for the technical reviewer).

**Developmental verdict: pass.**

## Copy edit

Commands: `npm run eos -- lint` (before: 0 errors, 0 warnings, 7 suggestions); `npm run eos -- fix --rules spelling-variant,terminology` (0 fixes needed). Manual checks: no em dashes, no contractions, no "we", no "simply/obviously/clearly/of course", no glossary phrases; American spelling throughout; headings in sentence case and numbered sequentially.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | Section 2.1 | language | OpenMP's three parts were run together in an ambiguous list |
| C2 | Should fix | Conventions paragraph | language | 50-word machine description sentence |
| C3 | Should fix | Section 5.2 (end) | language | Serial comma and non-parallel list of remedies |
| C4 | Should fix | Section 4.4 (end) | language | Redundant "For programs without data races ... a program that avoids all data races" |
| C5 | Optional | Section 5.3 | language | List introduction "There are three:" after a loose sentence |
| C6 | Optional | various | language | Small wording fixes |
| C7 | Optional | Conventions paragraph | language | GFLOP/s used before its expansion |

### C1. Ambiguous list in Section 2.1
- **Text:** "through **directives**, which in C are `#pragma omp` lines placed before a statement or block, a runtime library with functions such as `omp_get_thread_num`, and environment variables such as `OMP_NUM_THREADS`."
- **Problem:** The relative clause made the list read as a description of directives; it also needed a serial comma to parse.
- **Correction (applied):** "through three means: **directives** (in C, `#pragma omp` lines placed before a statement or block), a runtime library (functions such as `omp_get_thread_num`) and environment variables (such as `OMP_NUM_THREADS`)."

### C2. Long sentence on the reference machine
- **Correction (applied):** split into "It has four cores of an Intel Xeon processor at 2.1 GHz, with one hardware thread per core, and 16 GiB of memory. Each core has a 48 KiB level-1 (L1) data cache and a 2 MiB level-2 (L2) cache, and the cores share a level-3 (L3) cache that `lscpu` reports as 260 MiB." Same facts.

### C3. Remedies list in Section 5.2
- **Text:** "are short critical sections, work moved out of them, and private accumulation (Section 3.3)."
- **Correction (applied):** "are keeping critical sections short, moving work out of them and accumulating privately (Section 3.3)." (Standards 5.1, no serial comma; 5.6, parallel items.)

### C4. Redundancy in Section 4.4
- **Correction (applied):** "C11 restores the intuitive model for correctly synchronized code: a program that avoids all data races and synchronizes only with mutexes and sequentially consistent atomics behaves as if ..."

### C5. List introduction in Section 5.3
- **Correction (applied):** "Three remedies follow from the cause; the second, a change of layout, is the one [Section 5.3 of the second entry](...) anticipated:" (link target unchanged).

### C6. Wording
- "The lesson for the roofline is that" became "For the roofline, this means that" (Section 2.4).
- "of the order of 100 ns" became "on the order of 100 ns" (American idiom, Section 6.4).
- Opening and closing sentences of 48 and 55 words split (lint `sentence-length`).

### C7. GFLOP/s before expansion
- **Correction (applied):** "Arithmetic rates are given in units of $10^9$ floating-point operations (FLOP) per second, written GFLOP/s". The linter still flags "GFLOP" (it does not recognize the derived unit as expanded); kept, see below.

### Remaining lint suggestions (kept)
- `18` acronym-expansion "GNU": part of the proper name "GNU Compiler Collection (GCC)"; GNU is a recursive name, not an expandable abbreviation.
- `20` acronym-expansion "GFLOP": the unit is defined in the same sentence from FLOP, which is expanded.
- `140` acronym-expansion "STREAM": the name of McCalpin's benchmark, not an abbreviation.
- `297` sentence-length (66 words): almost all of it is Lamport's verbatim definition, which must not be split or altered.
- `671` acronym-expansion "ACM": inside the journal title *Communications of the ACM* in the reference list.

### Notes for later stages (not copy findings)
- Section 3.2: the expected total 4 999 998 was recomputed in Python 3 (`sum((i*0x9E3779B97F4A7C15 mod 2^64) >> 63 for i < 10^7)` = 4999998). Spot recomputations of derived figures in the prose (53 and 240 ns per increment, factors 9 and 14, 21 times, 1800 cycles, 2900 FLOP, 16/7, 0.023 s and 0.162 s, 400 times, 0.04%, Exercise answers) all agree with the quoted outputs.
- Fact-checker: the Lamport quotation (Section 4.1) should be checked word for word against the 1979 paper.
- Number formatting: large counts appear as "4 999 998" (space-grouped) and "1800" (ungrouped); the standards do not fix a rule, so left unchanged.
- The Vietnamese translation does not exist for this entry, so nothing is marked for update.

Counts: 0 blocking, 4 should fix (all applied), 3 optional (all applied).

Final lint: `npm run eos -- lint src/content/blog/threads-and-shared-memory-parallelism.mdx` reports 0 errors, 0 warnings, 5 suggestions (justified above).

**Copy verdict: pass.**

<!-- Later sections: Fact-check, Technical review, Resolution, QA -->
