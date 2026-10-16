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

## Fact-check

Stage EOS 6.3, performed by a reviewer who did not write or revise the entry. Inputs: `editorial/standards.md` (Policy C), the review protocol, `CLAUDE.md`, the series overview, the article in full, and the cited sections of the first and second entries. Network note: direct downloads from this container were refused by the proxy (403 for dblp.org, crossref.org; DNS failure for cl.cam.ac.uk, lamport.org, upenn.edu), so references were checked through web search results and the pages that could be fetched (microsoft.com, which hosts Lamport's paper as a scan).

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Blocking | `:18`, Conventions | evidence | OpenMP 5.2 is called the "current specification"; OpenMP 6.0 was released in November 2024 |
| F2 | Optional | `:189`, Section 3.1 | evidence | "without changing its memory model" not verified against a source |
| F3 | Optional | `:670`, References | consistency | OpenMP entry formatted differently from the first and fourth entries |
| F4 | Optional | `:664`, References | evidence | The magazine's title is *Computer*, not *IEEE Computer* |

### F1. OpenMP 5.2 is not the current specification
- **Where:** `src/content/blog/threads-and-shared-memory-parallelism.mdx:18`, Conventions
- **Text:** "this entry cites its current specification, version 5.2."
- **Problem:** The OpenMP ARB released version 6.0 of the OpenMP API on 14 November 2024, at SC24 (OpenMP ARB news release "OpenMP ARB Releases OpenMP 6.0 for Easier Programming", openmp.org; Business Wire, 14 November 2024; HPCwire, 14 November 2024). The sentence is false as of the publication date (2026-10-16). Every OpenMP statement that the entry makes still holds in 5.2, which is the version cited by the whole series. Version 6.0 was not checked clause by clause, so the correction makes no claim about it.
- **Correction:** "this entry cites version 5.2 of its specification (November 2021), the version used throughout the series; a later version, 6.0, appeared in November 2024."

### F2. C17 and the memory model
- **Where:** `:189`, Section 3.1
- **Text:** "(the 2018 edition corrected C11 without changing its memory model)"
- **Problem:** The subclause number and both quoted definitions are correct: C11 (ISO/IEC 9899:2011) and C17 (ISO/IEC 9899:2018) both define "conflict" and "data race" in 5.1.2.4, and the text matches the standard's wording ("Any such data race results in undefined behavior"). I could not fetch a WG14 or ISO source stating that C17 left every part of the memory model unchanged. C17 is generally described as a defect-correction revision with no new features.
- **Correction:** "(the 2018 edition, which replaced C11 and keeps these definitions in the same subclause)", or keep the current wording if the copy desk can cite a WG14 source.

### F3. OpenMP reference format
- **Text:** "OpenMP Architecture Review Board, *OpenMP Application Programming Interface*, Version 5.2, November 2021."
- **Problem:** The first and fourth entries list the same document as "version 5.2, 2021". The details are right (the ARB announced 5.2 on 9 November 2021), but the series should use one form.
- **Correction:** "OpenMP Architecture Review Board, *OpenMP Application Programming Interface*, version 5.2, 2021."

### F4. Title of Adve and Gharachorloo's venue
- **Text:** "*IEEE Computer*, vol. 29, no. 12, pp. 66–76, 1996."
- **Problem:** The IEEE Computer Society magazine is titled *Computer*. "IEEE Computer" is common informal usage.
- **Correction (optional):** "*Computer*, vol. 29, no. 12, pp. 66–76, 1996."

### Verification table

| Claim | Location | Status | Source |
|---|---|---|---|
| Lamport's definition quoted word for word: "the result of any execution is the same as if the operations of all the processors were executed in some sequential order, and the operations of each individual processor appear in this sequence in the order specified by its program." | `:297` | Verified, exact | Scan of the paper on the Microsoft Research site (page 690). The text matches character for character. In the original the condition is followed by "A multiprocessor satisfying this condition will be called *sequentially consistent*." The article's frame, "A multiprocessor is sequentially consistent if", is a faithful paraphrase of that sentence. |
| Lamport, "How to make a multiprocessor computer that correctly executes multiprocess programs," *IEEE Trans. Computers*, vol. C-28, no. 9, pp. 690–691, 1979 | `:667` | Verified | Header of the scanned page: "IEEE Transactions on Computers, vol. C-28, no. 9, September 1979", p. 690. Microsoft Research publication page: pp. 690–691. |
| Adve and Gharachorloo tutorial, vol. 29, no. 12, pp. 66–76, 1996; describes relaxed models and how languages restore SC for programs that follow their rules | `:299`, `:411`, `:664` | Verified (venue name, see F4) | Wisconsin BibTeX entry; DTIC record; WRL Research Report 95/7. The tutorial covers relaxed hardware models (TSO, PSO, weak ordering, release consistency) and the programmer-centric data-race-free view. |
| Sewell et al., x86-TSO, *CACM* vol. 53, no. 7, pp. 89–97, 2010 | `:372`, `:671` | Verified | St Andrews research portal; CACM listing; DOI 10.1145/1785414.1785443; five authors in the order given |
| Williams, Waterman, Patterson, Roofline, *CACM* 52(4):65–76, 2009 | `:177`, `:672` | Verified | Same entry as in the first and second entries, verified in their reports. Identical text. |
| McCalpin 1995, TCCA Newsletter, pp. 19–25, Dec. 1995 | `:140`, `:669` | Verified | As in the first entry (verified there). Identical text. |
| Little 1961, *Operations Research* 9(3):383–387 | `:181`, `:668` | Verified | DOI 10.1287/opre.9.3.383 (verified in the fourth entry's report). Identical text. |
| Hennessy and Patterson, 6th ed., Morgan Kaufmann, 2017; describes snooping and directory protocols | `:59`, `:665` | Verified (chapter level) | The 6th-edition table of contents lists Chapter 5, "Multiprocessors and Thread-Level Parallelism", which covers centralized (snooping) and distributed (directory) coherence. Edition and year match the other entries. |
| ISO/IEC 9899:2018 title and publisher | `:666` | Verified | ISO catalogue title "Information technology — Programming languages — C". The en dash form follows house style. |
| C11/C17 5.1.2.4: definitions of conflict and data race, and UB | `:189` | Verified | 5.1.2.4 p4 and p35 (paragraph numbering of N1570/N2176). The wording matches. |
| "C17 corrected C11 without changing its memory model" | `:189` | Not verified | F2 |
| OpenMP 5.2 is the current specification | `:18` | Corrected | F1: 6.0 was released 14 Nov 2024 |
| OpenMP 5.2 date, November 2021 | `:670` | Verified | OpenMP ARB press release, 9 November 2021 (verified in the fourth entry's report) |
| `_OPENMP` = 201511 denotes OpenMP 4.5; GCC 13 reports it | `:18` | Verified | `echo | gcc -fopenmp -dM -E -` with GCC 13.3.0: `#define _OPENMP 201511`. The value is the 4.5 date (November 2015). |
| Array-section reduction `reduction(+ : hist[:256])` supported since OpenMP 4.5 | `:621` | Verified | OpenMP 4.5 added array sections to reduction list items for C/C++. `hist.c` compiles with GCC 13.3 (4.5) and prints `total 1000000`. |
| `atomic` without a memory-order clause is relaxed in OpenMP 5.2 | `:417` | Verified | OpenMP 5.x: without a `requires atomic_default_mem_order` directive or a clause, the memory order is `relaxed`. |
| Implicit flushes at barriers and at entry to and exit from `critical`; unnamed `critical` constructs share one name; schedule kinds and defaults (dynamic and guided chunk 1; static without chunk gives at most one chunk per thread); `runtime` reads `OMP_SCHEDULE` / `omp_set_schedule`; `omp_get_wtime` semantics | `:134`, `:287`, `:417`, `:505`–`:508`, `:140` | Verified | OpenMP 5.2 specification (worksharing-loop `schedule` clause, `critical` construct, flush synchronization, `omp_get_wtime` routine). The wording in the article is consistent with the specification text. |
| GCC without a schedule clause: contiguous near-equal blocks | `:134` | Verified | Test program (technical log): 10 iterations on 4 threads gave owners `0001112233` |
| x86 ordering rules (loads not reordered with loads; stores not with stores or older loads; loads may pass older stores to other locations; locked instructions have a total order; mfence/locked drain the buffer) | `:374`–`:376` | Verified | Intel SDM Vol. 3A, 8.2.2; x86-TSO CACM paper (abstract machine: FIFO store buffers, MFENCE and LOCK'd instructions flush the local buffer) |
| "the only reordering other threads can see" | `:372` | Corrected | See T1 (read-own-write-early, named by Adve and Gharachorloo) |
| GCC compiles a seq_cst store to `xchg` | `:400` | Verified | Disassembly of `litmus` built with GCC 13.3 (T log) |
| GCC treats a memory order known only at run time as seq_cst | `:400` | Verified | Test function `atomic_store_explicit(&x, v, mo)` with `mo` a parameter compiles to `xchg` (T log) |
| `_Thread_local` is C11; `nanosleep` needs `_POSIX_C_SOURCE 199309L` | `:34`, `:316` | Verified | C11 6.7.1; POSIX.1b; the programs compile with `-Wall` and give no warnings |
| Second entry measured 45.6 GB/s on four cores; Little's law in its Section 6.4; write-allocate in 2.3; layout and threads in 5.3 | `:179`, `:181`, `:487` | Verified | `memory-hierarchy-and-locality.mdx:767`, `:776`, `:213`, `:669` |
| First entry: definitions of $S$, $E$, $W$, $D$; greedy bound in 4.2 | `:14`, `:584` | Verified | `performance-models-and-scaling-laws.mdx:20`, `:230`–`:236` |
| "Apart from their bandwidth measurements, both entries treated one processor core" | `:14` | Corrected | See T4: the first entry also measured the four-thread peak rate |

### Not verified
- `:189` "the 2018 edition corrected C11 without changing its memory model": no WG14/ISO source could be fetched (F2).
- Observations from the writer's other runs that are not in `run-quoted.out`: "other runs of the same program gave totals as low as 1 275 620" (`:232`); "another run printed them in the order 0, 1, 2, 3" (`:123`); "no difference in some other runs" (`:485`); "Early versions of the program ... showed no reordering at all" (`:400`). These are plausible, and my own runs agree with them in kind: `clauses` printed the order 0, 1, 2, 3; racy totals were about 1.6 million; a run-time memory order compiles to `xchg`. However, no log of those runs was kept, so they cannot be checked on the reference machine. Keep them only if the writer can point to a log, or else attribute them ("in the writer's other runs").

Counts: 1 blocking (F1), 0 should fix, 3 optional.

**Fact-check verdict: fail** (F1 open; passes once F1 is applied).

## Technical review

Stage EOS 6.4, by the same independent reviewer. **Machine caveat:** the machine available for this review is not the reference machine. `lscpu` here reports an Intel Xeon @ 2.80 GHz, 32 KiB L1d, 1 MiB L2 and 33 MiB L3 per core/chip (the reference machine: 2.10 GHz, 48 KiB, 2 MiB, 260 MiB). Deterministic outputs were reproduced exactly. My timings test only whether the article's qualitative claims hold on comparable hardware, and they cannot confirm the reference machine's numbers. Every quoted timing is consistent with `run-quoted.out`, which is byte-identical to `run.out`.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `:372`, Section 4.3 (D6) | accuracy | "the only reordering other threads can see" omits read-own-write-early (store forwarding) |
| T2 | Should fix | `:140`, Section 2.4 | accuracy | The polynomial has degree 199, not 200 |
| T3 | Should fix | `:20`, `:430` | consistency | Cycle count uses 2.1 GHz as the real clock; the first entry inferred about 2.8 GHz |
| T4 | Should fix | `:14`, opening | consistency | "Apart from their bandwidth measurements, both entries treated one processor core" is false for the first entry |
| T5 | Optional | `:232`, Section 3.2 | accuracy | "the sequential one": `race.c` has no sequential version; the comparison is with one thread |
| T6 | Optional | `:580`, Section 6.4 | accuracy | "one request, on the order of 100 ns" is wall time per iteration across four threads |
| T7 | Optional | `:449`, Section 5.2 | accuracy | "the critical sections form one chain" holds for `sync.c` but in general they are only serialized |

D7 (seq_cst store compiled to `xchg`) is resolved with no finding. See the log.

### T1. TSO: the "only" reordering (D6)
- **Where:** `:372`, Section 4.3
- **Text:** "Each hardware thread has a first-in first-out store buffer, and the only reordering other threads can see is a load that completes before an earlier store of the same thread, to a different address, has left the buffer."
- **Problem:** In x86-TSO a thread also reads its own buffered store before other threads can see it (store forwarding; "read-own-write-early" in Adve and Gharachorloo's terminology, and a rule of the abstract machine of Sewell et al.). Some outcomes can only be explained this way, not by reordering alone. Derivation for the x86-TSO test n6 (Intel SDM 8.2.3.5 shows a similar test): T0 `x = 1; r1 = x; r2 = y;`, T1 `y = 2; x = 2;`, with the outcome `r1 = 1, r2 = 0, x = 1` at the end. Without forwarding, `r1 = 1` puts `x = 1` before `r1` in a global order. Loads are not reordered with loads, so `r2` follows `r1`, and `r2 = 0` puts `r2` before `y = 2`, which precedes `x = 2`. Then `x = 2` follows `x = 1`, and the final `x` would be 2. The outcome is allowed on x86 because T0 reads `x = 1` from its own buffer while the store is still invisible to T1. Section 4.2 already mentions forwarding, so a short qualifier is enough. The three bullets and the litmus discussion stay correct.
- **Correction:** "Each hardware thread has a first-in first-out store buffer, from which the thread's own later loads read its pending stores (Section 4.2). Seen from other threads, the one reordering this allows is a load that completes before an earlier store of the same thread, to a different address, has left the buffer. Hence:"

### T2. Degree of the polynomial
- **Where:** `:140`, Section 2.4
- **Text:** "One evaluates a polynomial of degree 200 by Horner's rule at $2^{21}$ points"
- **Problem:** The loop starts from `s = 0.0` and runs `DEG = 200` steps of `s = s * xi + 1.0`, which yields $\sum_{j=0}^{199} x^j$, a polynomial of degree 199. The first step multiplies 0. Check: 200 steps at $x = 0.5 + 0.4/2^{21}$ give 2.000000763, and $(1 - x^{200})/(1 - x)$ gives the same 2.000000763. The 400 FLOP per element and $I = 25$ are unaffected.
- **Correction:** "One evaluates, by 200 multiply-add steps of Horner's rule, a polynomial of degree 199 at $2^{21}$ points"

### T3. Clock rate used for the cycle count
- **Where:** `:20` "four cores of an Intel Xeon processor at 2.1 GHz"; `:430` "about 1800 clock cycles at 2.1 GHz"
- **Problem:** The first entry (`performance-models-and-scaling-laws.mdx:20`, Section 5.4) describes the processor as "reported at 2.1 GHz" and infers from its FMA measurement that the cores ran at about 2.77 to 2.83 GHz. Converting 0.85 µs at 2.1 GHz (1785 cycles) treats the nominal clock as the real one. At 2.77 GHz the barrier is about 2350 cycles.
- **Correction:** `:20`: "four cores of an Intel Xeon processor reported at 2.1 GHz". `:430`: "A barrier took 0.85 µs, about 1800 clock cycles at the reported 2.1 GHz, or about 2400 at the 2.8 GHz that the first entry's measurements suggest,"

### T4. What the first two entries measured
- **Where:** `:14`, opening
- **Text:** "Apart from their bandwidth measurements, both entries treated one processor core."
- **Problem:** The first entry also measured the four-thread peak arithmetic rate (354.0 GFLOP/s, `performance-models-and-scaling-laws.mdx`, Section 5.4) and used OpenMP threads to do it.
- **Correction:** "Apart from a few four-core measurements of peak arithmetic rate and bandwidth, both entries treated one processor core."

### T5. "Sequential one" in Section 3.2 (optional)
- **Text:** "The racy version is also barely faster than the sequential one"
- **Correction:** "The racy version with four threads is also barely faster than with one (0.0093 against 0.0110 s)" (ratio recomputed: 1.17).

### T6. Cost of one chunk request (optional)
- **Text:** "about 100 ns per iteration ... A chunk should be large enough that one request, on the order of 100 ns here, is small against its work"
- **Problem:** 0.10946 s / 2^20 = 104 ns is wall time per iteration with four threads requesting concurrently. Each thread spends about 4 × 104 ≈ 420 ns per request, including waiting. 100 ns is the serialized throughput of the queue.
- **Correction:** "A chunk should be large enough that one request, which costs each thread several hundred nanoseconds here when all four contend, is small against its work, ..."

### T7. Critical sections as one chain (optional)
- **Text:** "the critical sections form one chain, so the span is at least $f\,T_1$"
- **Correction:** "the critical sections run one at a time, as if they formed one chain (in `sync.c` they do, through `shared_sum`), so the span is at least $f\,T_1$"

### Section swap (5.2 and 5.3) check
After the editor's swap, Section 5.2 quotes the `f = ...` table from `sync.c` and Section 5.3 quotes the per-increment table from `falseshare.c`. Both match `run-quoted.out` line for line. The prose in each subsection refers to its own table (1.89 against 1.67; 1.53 and 1.55; 43.6, 122.6 and 5.8 ns; 21 times). The run order in `run.sh` (falseshare before sync) does not matter, because the programs are independent. Internal references are consistent: Exercise 1 cites the bound of Section 5.2, where it now is; `:430` cites Section 3.3; `:485` cites Section 4.3; `:489` cites Section 3.3. The `###` fragments have no incoming links (grep of `src/`), and the `#5-synchronization-cost-and-false-sharing` targets used by the second entry still exist.

### Log of what was recomputed and run
GCC 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1), Python 3.13.16. Builds use the flags of `run.sh`, scratch files are in `/tmp/claude-0/hpc/review/threads-and-shared-memory-parallelism/`, and timings ran under `flock /tmp/claude-0/hpc/bench.lock` with `OMP_PROC_BIND=close OMP_PLACES=cores`.

- **Code-text correspondence:** the `clauses.c` and `spin.c` blocks are byte-identical to the programs. The Python block matches `model.py` apart from one header comment line. The excerpts of `loops.c`, `race.c`, `litmus.c`, `falseshare.c` and `schedule.c` match the source functions; the schedule line `omp_set_schedule(omp_sched_dynamic, 100); /* or one of the others */` is illustrative, as marked. `run-quoted.out` and `run.out` are identical, and every quoted block appears in them verbatim. The `hist` output is missing from `run.out` because `run.sh` was extended after that run; I ran it: `total 1000000`.
- **Deterministic outputs:** `clauses`: a = 10..13, b = 100..103, c = 46; after the region a = 10, b = 10 (exact; one run printed threads in order 0,1,2,3, the other 0,3,2,1). `model.py`: identical output (shares 0.0625/0.1875/0.3125/0.4375; bound 2.29; W = 199990000; D = 19999; W/p + D = 50017499). Expected race total recomputed in Python: 4999998. `hist`: total 1000000.
- **D7 / disassembly** (`objdump -d` of the GCC 13.3 builds): in `litmus`, the seq_cst store to `x` is `xchg %eax,x` and the relaxed store is `movl $0x1,x`. The relaxed and release stores to `flag` are both `movl $0x1,flag`, and the relaxed and acquire loads of `flag` are both `mov flag,%eax`, which confirms `:415`. In `spin_plain` `main`: `110b: mov ready,%eax; test; jne; 1115: jmp 1115`, which matches the quoted address exactly. In `race`: `lock addq $0x1,(%rsi)` for `omp atomic` `count++`, and `GOMP_critical_start`/`GOMP_critical_end` for `critical`. In `falseshare` `bump_atomic`: `lock addq $0x1,(%rdi)` (unrolled twice). A run-time memory-order argument (`atomic_store_explicit(&x, v, mo)`) compiles to `xchg`, which confirms the seq_cst fallback.
- **Default schedule:** 10 iterations on 4 threads with no schedule clause gave owners `0001112233` (contiguous blocks).
- **Horner degree:** 200 steps from 0 give 2.000000763; $(1-x^{200})/(1-x)$ also gives 2.000000763 (degree 199; T2).
- **Recomputed figures** (Python 3.13). The article's values are in brackets:
  - Polynomial: GFLOP/s 1.34, 1.37, 2.67, 5.20 [same]; S 1.02, 1.98, 3.87 [same].
  - Triad: GB/s 10.93, 11.79, 23.41, 46.82 [23.42, 46.80; the times are printed rounded]; S 4.28 [same]; 25/11.8 = 2.12 [≈ 2.1].
  - Race: atomic 52.8 ns [53], critical 240.2 ns [240], ratios 9.18 [nine] and 14.29 [14]; reduction and partial speedups 4.40 and 4.20 ["slightly above four"]; racy p4/p1 1.17.
  - Synchronization and false sharing: barrier 1785 cycles at 2.1 GHz [1800] and 2355 at 2.77 GHz; region 2851 FLOP [roughly 2900]; false sharing 122.56/5.81 = 21.1 [21]; SB 23.5% [same].
  - Triangular loop: 16/7 = 2.286 [2.29]; 0.3711/16 = 0.0232 [0.023]; 0.1635 − 0.0232 = 0.140 [0.141 measured]; 7/16 × 0.3711 = 0.162 [same]; dynamic,1 ratio 405 [400]; 104 ns per iteration [about 100]; greedy excess 0.040% [0.04%].
  - Amdahl column: 2.00/4.00, 1.90/3.48, 1.67/2.50, 1.33/1.60 [same].
  - Exercises: 4.71, 6.67, 15/64 = 0.234, 64/15 = 4.27, E = 0.533 [same].
- **Derivations checked:** static-block shares $(2k+1)/p^2$ (cumulative work $\propto i^2$); critical-section bound $T_p \ge \max(T_1/p, f T_1)$ (the serialized time cannot overlap, and the total work divides at best evenly); greedy bound and $W/D = n/2$; triad intensity 2/24 and 32 bytes with write-allocate; polynomial $I = 400/16 = 25$; Exercise 5 `sizeof` (16 bytes, 64 with `_Alignas(64)`, 48 bytes unused).
- **Timed runs on the review machine** (different hardware; qualitative check only):
  - `loops`: polynomial S = 1.02/2.00/3.86; triad S = 1.04/1.81/3.65 (11.6 to 42.2 GB/s, no saturation either). Built without `-fno-tree-vectorize`: sequential polynomial 0.433 s against one-thread OpenMP 0.884 s, which confirms "about twice as long" (`:175`).
  - `race`: one thread correct, four threads 1.60 to 1.75 million (wrong, varying); atomic p4 0.145 s, critical p4 0.870 s, reduction/partial about 3 ms.
  - `litmus`: SB relaxed 0,0 = 181177; SB seq_cst 0,0 = 0; MP 1,0 = 0 in both.
  - `spin` behaves as described.
  - `falseshare`: atomic adjacent 6.5 → 30.0 → 78.5 ns, padded flat 6.5 to 6.9 ns; plain 2.3 to 3.3 ns, a small effect. The plain-increment cost here (2.3 ns) differs from the reference machine's 0.33 ns, a store-forwarding latency difference between processors. The article already qualifies the plain result as machine-dependent and unverified.
  - `sync`: barrier 0.87 µs, region 2.7 µs; f = 0.2, p = 2: S = 1.97 > Amdahl 1.67; f = 0.5: four threads 1.52 against two 1.65.
  - `schedule`: static S = 2.31 (bound 2.29); static,1 3.86; dynamic,1 3.81; dynamic,100 3.72; guided 4.01; uniform loop dynamic,1 326 times static.
  
  Every qualitative claim of the article held. The magnitudes differ as expected on different hardware, and the article labels its timings as measurements of the reference machine.
- **Labeling:** the only figure for another machine (B = 25 GB/s, `:181`) is labeled "assumed". Nothing is presented as run that was not run, apart from the unlogged "other runs" observations listed under Fact-check, Not verified.

Counts: 0 blocking, 4 should fix (T1 to T4), 3 optional (T5 to T7).

**Technical verdict: fail** (should-fix findings open; passes once T1 to T4 are applied or answered).

## Resolution

Stage EOS 7, by the author of the draft. All changes are in `src/content/blog/threads-and-shared-memory-parallelism.mdx`. No timing was re-run: the container now runs on a different processor, so the reference machine's numbers are unchanged.

| ID | Severity | Resolution |
|---|---|---|
| F1 | Blocking | Applied, with the reviewer's text: "this entry cites version 5.2 of its specification (November 2021), the version used throughout the series; a later version, 6.0, appeared in November 2024." |
| F2 | Optional | Applied. The unsourced clause is replaced by "(the 2018 edition, which replaced C11 and keeps these definitions in the same subclause)". |
| F3 | Optional | Applied: "version 5.2, 2021.", which matches the first and fourth entries. |
| F4 | Optional | Applied: venue now *Computer*. |
| T1 | Should fix | Applied, with the reviewer's text. Store forwarding is named, and the "one reordering" is stated as seen from other threads. |
| T2 | Should fix | Applied: "by 200 multiply-add steps of Horner's rule, a polynomial of degree 199". |
| T3 | Should fix | Applied. The Conventions now say "reported at 2.1 GHz", and Section 5.1 gives about 1800 cycles at the reported 2.1 GHz or about 2400 at the 2.8 GHz the first entry infers (its Section 5.4: 2.77 to 2.83 GHz). The long sentence was split. |
| T4 | Should fix | Applied, with the reviewer's text: "Apart from a few four-core measurements of peak arithmetic rate and bandwidth, ...". |
| T5 | Optional | Applied: "barely faster than with one (0.0093 against 0.0110 s)". |
| T6 | Optional | Applied, with the reviewer's text: "which costs each thread several hundred nanoseconds here when all four contend". The figure of about 100 ns per iteration (wall time) is kept, since it is computed from the quoted output. |
| T7 | Optional | Applied, with the reviewer's text: "run one at a time, as if they formed one chain (in `sync.c` they do, through `shared_sum`)". |

Unlogged observations (Fact-check, Not verified). The writer saw all four in runs on the reference machine, but none of those outputs was saved in the scratch folder (`/tmp/claude-0/hpc/threads-and-shared-memory-parallelism/` holds only `run.out` / `run-quoted.out`). Each is therefore now marked as unlogged:
- Section 2.2: "(an earlier, unlogged run printed them in the order 0, 1, 2, 3)".
- Section 3.2: "earlier runs of the same program, whose output was not kept, gave totals as low as about 1.3 million". The exact figure 1 275 620 was removed, and the claim keeps only the order of magnitude.
- Section 4.3: "Early versions of the program, whose output was not kept, ... showed no reordering". The reviewer's disassembly independently confirms the mechanism (a run-time order compiles to `xchg`).
- Section 5.3 (plain increments): "no visible difference in some earlier runs whose output was not kept".

Lint after resolution: `npm run eos -- lint src/content/blog/threads-and-shared-memory-parallelism.mdx` gives 0 errors, 0 warnings and 5 suggestions (GNU, GFLOP, STREAM, the Lamport quotation, ACM; all justified in the Copy edit section).

Open findings: none.
