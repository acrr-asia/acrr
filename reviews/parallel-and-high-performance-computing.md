# Series review: Parallel and High-Performance Computing

- Series: `parallel-and-high-performance-computing` (5 articles, status published, 0 planned entries)
- Reviewed commit: 3ac0c65
- Date: 2026-10-16
- Reviewer: independent Series Editor (EOS step 8); I did not write or revise any of the entries or the series file.

## Summary

The series is technically strong and coherent. Each entry delivers its objective, the derivations and models recompute exactly, every cross-entry link resolves to a section that says what the link claims, and the per-item resolutions (developmental, copy, fact-check, technical) all landed in the text as recorded. The problems are at series level, where the per-item reviews could not look. The reference machine's clock is "reported", "rated" or plainly "at" 2.1 GHz depending on the entry, although the first entry infers that the cores ran near 2.8 GHz. The fourth entry measures one-core memory traffic of 22.3 GB/s without relating it to the 13.2 to 13.4 GB/s the first two entries present as what one core sustains. The second and fifth entries reuse symbols ($S$, $W$) that the first entry declares for the whole series. The overview's version statements do not match those of the entries, and one work is cited in two forms. None of these is a factual error in a single entry, and there is no blocking finding; the series should be published after the should-fix findings are resolved.

Findings: 0 blocking, 11 should fix, 7 optional.

## Resolution

All 11 should-fix findings and six of the seven optional ones were applied by the author side (the editor who coordinated the series, not the reviewer), mostly with the reviewer's recommended text. This series has no Vietnamese translations yet, so no translation needed the same changes.

| Finding | Resolution |
|---|---|
| F1 | Entries 2 and 5 now say "reported at 2.1 GHz". Entry 4 says "reported at 2.1 GHz (Section 5.4 of the first entry infers that the cores ran faster)". |
| F2 | Entry 4, Section 2.3, now relates its 22.3 GB/s to the one-core triad figures of entry 2, Section 6.3, and explains the difference by the absence of write-allocate traffic. It also calls the one-core ridge point a rough figure. |
| F3 | Entry 4, Section 2.2, no longer names the target that `-march=native` selected. It states that all four GCC 13.3 AVX-512 Xeon targets prefer 256-bit vectors. |
| F4 | Entry 1 Conventions now says what OpenMP is and how the thread count is set, and links Section 2 of the third entry. |
| F5 | Entry 2 uses $N_{\mathrm{ways}}$ for associativity and $N_{\mathrm{sets}}$ for the number of sets, in Section 2.1 and in the Summary. The reviewer's $k$ was not used because entry 2 already uses $k$ as the matrix-multiply loop index in Section 4. |
| F6 | Entry 5, Section 5.2, describes the row as "$N + 2$ values (the variable `W` in the code)". |
| F7 | Entry 1, Section 2.2: the communication model is "built from the latency and bandwidth of each message, measured on the reference machine and assumed for a cluster". |
| F8 | Entry 2 opening: "developed the roofline bound". |
| F9 | The series overview now names GCC 13.3, OpenMP specification 5.2, MPI through Open MPI 4.1.6, Python 3.13 and NumPy 2.5. |
| F10 | The DOI of Williams, Waterman and Patterson is added in entries 2 and 3. |
| F11 | Entry 4, Section 3.4, now refers back to entry 2, Section 6.4, for Little's law instead of defining it again. The Little (1961) reference is kept. |
| F12 (optional) | Applied: entry 2, Section 4.1, notes $n/12$ when the write of $C$ is not counted, with a link to entry 1, Section 5.2. |
| F13 (optional) | Applied, with the recommended wording. |
| F14 (optional) | Applied: "The C standard defines the problem precisely, in subclause 5.1.2.4 of both C11 and its 2018 revision". |
| F15 (optional) | Applied as part of F1: "a Kernel-based Virtual Machine (KVM) guest". |
| F16 (optional) | Applied: "most likely a small part of a large server processor". |
| F17 (optional) | Applied: the lead-in now says that `...` marks where the second run begins. |
| F18 (optional) | Not applied. Choosing one in-text citation form for the series is polish, and it is left for the next revision, as the reviewer suggested. |

Second pass. After the corrections, the whole series was checked again:
- `npm run build:local` exits 0, `npm run check:links` reports that all internal links resolve, and `eos validate-site dist` reports no issues.
- `eos lint` shows 0 errors and 0 warnings on all six files.
- The two new links (to `#63-measuring-sustainable-bandwidth` and `#64-what-limits-one-core-and-what-limits-many` of entry 2) and the links to entry 1 `#52-intensity-of-three-kernels` and entry 3 `#2-parallel-loops-with-openmp` resolve, and their targets say what the linking text claims.
- The F5 symbols do not collide with any other symbol in entry 2: $N_{\mathrm{ways}}$ and $N_{\mathrm{sets}}$ appear nowhere else in it.
- The independent QA stage re-reads each item before its record is written; anything it finds is added below.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Compute speedup, efficiency and the Amdahl and Gustafson bounds for a program, and use the roofline bound to decide whether a kernel is limited by arithmetic or by memory traffic. | Entry 1, Sections 1–3 and 5, Exercises 1–3 and 5; applied again in entry 5, Section 6 | Met. Checkable through the exercises. |
| Explain how caches exploit locality, and restructure a loop nest or a data layout to reduce the number of cache misses it causes. | Entry 2, Sections 2–5, with the simulator and Exercises 1–4 | Met. Miss counts are derived by hand and reproduced by the simulator. |
| Write a correct shared-memory parallel loop, and identify and remove data races, false sharing and load imbalance in one. | Entry 3, Sections 2, 3, 5 and 6, Exercises 2, 3 and 5 | Met. |
| Explain how vector units and GPUs execute data-parallel code, and estimate when offloading a computation to an accelerator pays for its data transfer. | Entry 4, Sections 2–6, Exercises 1–5 | Met. The GPU half is explicitly illustrative (no GPU on the reference machine), which the entry states. |
| Predict the communication cost of a message-passing program with the latency-bandwidth model, and use it to estimate strong and weak scaling. | Entry 5, Sections 3, 4 and 6, Exercises 1, 3 and 4 | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Should fix | entries 2, 4, 5 | Conventions (line 18 of each) | Factual consistency | The clock is given as "rated at" or "at 2.1 GHz", against entry 1's inference that the cores ran near 2.8 GHz. |
| F2 | Should fix | `src/content/blog/data-parallelism-vector-units-and-gpus.mdx` | Section 2.3 (line 112) | Factual consistency | One core drew 22.3 GB/s on axpy, unreconciled with the 13.2–13.4 GB/s one-core figure of entries 1 and 2. |
| F3 | Should fix | `src/content/blog/data-parallelism-vector-units-and-gpus.mdx` | Section 2.2 (line 92) | Technical accuracy | "`-march=native` selects GCC's `sapphirerapids` target" is unverified and conflicts with entry 1's "generic model name". |
| F4 | Should fix | `src/content/blog/performance-models-and-scaling-laws.mdx` | Conventions and Section 5.3 (lines 20, 337–382) | Concept introduction | OpenMP directives and environment variables are used without saying what OpenMP is or where it is explained. |
| F5 | Should fix | `src/content/blog/memory-hierarchy-and-locality.mdx` | Section 2.1 (lines 186–192), Summary (line 827) | Notation | $S$ (sets) and $W$ (ways) clash with the series-wide $S(p)$ and $W$ (work). |
| F6 | Should fix | `src/content/blog/distributed-memory-and-message-passing.mdx` | Section 5.2 (line 394) | Notation | $W = N + 2$ (row width) clashes with the series-wide work $W$. |
| F7 | Should fix | `src/content/blog/performance-models-and-scaling-laws.mdx` | Section 2.2 (line 144) | Cross-article references | The promise of a model "built from measured message costs" overstates entry 5, whose scaling predictions use assumed costs. |
| F8 | Should fix | `src/content/blog/memory-hierarchy-and-locality.mdx` | Opening (line 14) | Cross-article references | "The first entry ended with the roofline bound": it ends with Section 6, on measurement. |
| F9 | Should fix | `src/content/series/parallel-and-high-performance-computing.md` | Body, last paragraph (line 16) | Overview completeness | The version statements (GCC 13, no OpenMP version, "Open MPI 4.1", Python 3, no NumPy) do not match the entries. |
| F10 | Should fix | entries 1, 2, 3 | References | Factual consistency | Williams, Waterman and Patterson is cited with a DOI in entry 1 and without one in entries 2 and 3. |
| F11 | Should fix | `src/content/blog/data-parallelism-vector-units-and-gpus.mdx` | Section 3.4 (line 233) | Writing quality | Little's law is explained again from scratch instead of referring back to entry 2, Section 6.4. |
| F12 | Optional | `src/content/blog/memory-hierarchy-and-locality.mdx` | Section 4.1 (line 500) | Notation | $n/16$ for ideal reuse is not reconciled with entry 1's $n/12$. |
| F13 | Optional | `src/content/blog/distributed-memory-and-message-passing.mdx` | Section 6.3 (lines 530, 549) | Notation | $f_s$ is redefined as the communicating fraction. |
| F14 | Optional | `src/content/blog/threads-and-shared-memory-parallelism.mdx` | Section 3.1 (line 189) | Stated versions | "The C11 standard defines ... of ISO/IEC 9899:2018" names two editions as one. |
| F15 | Optional | `src/content/blog/data-parallelism-vector-units-and-gpus.mdx` | Conventions (line 18) | Terminology | "a kernel-based virtual machine (KVM)" calls the guest KVM, in lowercase, unlike the other entries. |
| F16 | Optional | `src/content/blog/threads-and-shared-memory-parallelism.mdx` | Section 2.4 (line 179) | Factual consistency | States as fact what entry 2, Section 6.4, labels an inference. |
| F17 | Optional | `src/content/blog/memory-hierarchy-and-locality.mdx` | Section 1.3 (lines 151, 166) | Writing quality | The `...` line in the latency output marks the join of two runs but reads as omitted rows. |
| F18 | Optional | all entries | In-text citations | Writing quality | In-text citation style varies between entries (names only, or author and year). |

### F1. The reference machine's clock rate

- **Where:** `src/content/blog/memory-hierarchy-and-locality.mdx:18`, `src/content/blog/data-parallelism-vector-units-and-gpus.mdx:18`, `src/content/blog/distributed-memory-and-message-passing.mdx:18`, Conventions.
- **Text:** entry 2: "four cores of an Intel Xeon processor rated at 2.1 GHz"; entry 4: "4 cores of an Intel Xeon processor at 2.1 GHz that supports the 512-bit vector extensions"; entry 5: "four cores of an Intel Xeon processor at 2.1 GHz, 2 MiB of L2 cache per core".
- **Problem:** Entry 1, Section 5.4 (`src/content/blog/performance-models-and-scaling-laws.mdx:461`), shows that the measured FMA rate is impossible at 2.1 GHz and infers an average clock of about 2.77 to 2.83 GHz; "the guest operating system reports a fixed nominal frequency". Entry 1 (line 22) and entry 3 (line 20) therefore say "reported at 2.1 GHz", and entry 3, Section 5.1, converts times to cycles at both clocks. "Rated at" (entry 2) asserts a specification no one has read, and "at 2.1 GHz" (entries 4 and 5) states as the operating clock what entry 1 shows it is not. A reader of entry 4 alone would convert its timings to cycles at the wrong clock.
- **Recommended correction:** Use the form of entries 1 and 3 in all three places. Entry 2: "four cores of an Intel Xeon processor reported at 2.1 GHz". Entry 4: "4 cores of an Intel Xeon processor reported at 2.1 GHz (Section 5.4 of the first entry infers that the cores ran faster) that supports the 512-bit vector extensions". Entry 5: "four cores of an Intel Xeon processor reported at 2.1 GHz, 2 MiB of L2 cache per core". Apply the same change to any Vietnamese translations.

### F2. One-core bandwidth: 22.3 GB/s against 13.4 GB/s

- **Where:** `src/content/blog/data-parallelism-vector-units-and-gpus.mdx:112`, Section 2.3.
- **Text:** "Vectorization made the loop 1.4 to 1.6 times faster than the scalar build in repeated runs (1.56 for the 256-bit build in the run shown). This suggests that the scalar loop did not keep enough memory requests in flight to reach the bandwidth one core can draw."
- **Problem:** The output at line 104 gives 22.3 GB/s for axpy on one thread from main memory (arrays of 512 MiB). The series has so far told the reader that one core sustains about 13 GB/s: entry 1, Section 5.3 (line 395, "One core alone reached about 13 GB/s") and Section 6.3 (line 586, the bound from "one core's measured 13.2 GB/s"), and entry 2, Section 1.1 (line 30), which builds the one-core ridge point of 6.8 FLOP/byte on 13.4 GB/s and uses it again in Exercise 3. Entry 4 never mentions those figures, and "the bandwidth one core can draw" implies a known value that the scalar loop (14.4 GB/s) failed to reach, although 14.4 GB/s already exceeds the earlier one-core figure. The numbers can be reconciled (axpy reads the array it writes, so its counted 24 bytes are its physical traffic, while the triad's are 32 physical bytes, 17.9 GB/s; entry 2, Section 5.2, line 658, already found that one core's rate "depends on the mix of reads and writes"), but the series does not do it, and a reader comparing the entries sees a contradiction.
- **Recommended correction:** Replace the second sentence quoted above with: "This suggests that the scalar loop did not keep enough memory requests in flight. The vectorized loop's 22.3 GB/s is well above the 13.4 GB/s that one core sustained on the triad of [Section 6.3 of the second entry](/blog/memory-hierarchy-and-locality#63-measuring-sustainable-bandwidth), 17.9 GB/s counting the write-allocate read. Axpy reads the array it writes, so it moves no write-allocate traffic, and, as Section 5.2 of the second entry found, how much one core sustains depends on the mix of reads and writes; the one-core ridge point of about 6.8 FLOP/byte is therefore a rough figure."

### F3. Unverified identification of the processor

- **Where:** `src/content/blog/data-parallelism-vector-units-and-gpus.mdx:92`, Section 2.2.
- **Text:** "GCC chose 256 bits although the processor supports 512: here `-march=native` selects GCC's `sapphirerapids` target, whose default preferred vector width is 256 bits, and `-mprefer-vector-width=512` overrides it."
- **Problem:** The writer's directory (`/tmp/claude-0/hpc/data-parallelism-vector-units-and-gpus/`) holds no output that records which target `-march=native` resolved to, and the item's fact-check lists the claim under "Not verified": the writer's binaries are byte-identical to builds for `sapphirerapids`, `cascadelake` and `icelake-server`. Stated as fact, it also sits awkwardly with entry 1, Section 5.4 (line 399), which says that "the virtual machine reports only a generic model name, so the count [of FMA units] cannot be read from `lscpu`", and with entry 2, Section 5.2 (line 660), which used `-march=sapphirerapids` only as a stand-in. The point the sentence makes does not depend on the target: GCC 13.3.0 here gives `-mprefer-vector-width=256` for `skylake-avx512`, `cascadelake`, `icelake-server` and `sapphirerapids` alike.
- **Recommended correction:** "GCC chose 256 bits although the processor supports 512: GCC 13.3's targets for AVX-512 Xeon processors (`skylake-avx512`, `cascadelake`, `icelake-server`, `sapphirerapids`) all set a default preferred vector width of 256 bits, and `-mprefer-vector-width=512` overrides it."

### F4. OpenMP used in the first entry without introduction

- **Where:** `src/content/blog/performance-models-and-scaling-laws.mdx:20` (Conventions), `:359` and `:366` (directives in the triad listing), `:382` (environment variables), Section 5.3.
- **Text:** "The code is C11 compiled with the GNU Compiler Collection (GCC) 13.3 and uses OpenMP for threads"; "#pragma omp parallel for schedule(static)"; "run with `OMP_NUM_THREADS=1` and then 4, with `OMP_PROC_BIND=close` to keep each thread on one core".
- **Problem:** The entry promises that "No parallel programming experience is needed: the later entries introduce threads" (line 16), yet its two four-core measurements rely on OpenMP directives, `omp_get_wtime`, `omp_get_max_threads` and two environment variables, and the entry never says what OpenMP is or points to where it is explained. The abbreviation is not expanded either (entry 2 expands it at line 18; entry 3 defines it at line 18 and Section 2). Standards 5.3 and 6.1 require a concept and abbreviation to be introduced at first use or referred back; here it can only be referred forward, which the entry does not do.
- **Recommended correction:** Replace the last sentence of line 20 from "The code is C11" with: "The code is C11 compiled with the GNU Compiler Collection (GCC) 13.3. The two four-core measurements of Section 5 use OpenMP, a set of compiler directives such as `#pragma omp parallel for` that divide a loop among threads, with the thread count set by `OMP_NUM_THREADS`; [Section 2 of the third entry](/blog/threads-and-shared-memory-parallelism#2-parallel-loops-with-openmp) explains it. The models are written in Python 3.13 with its standard library."

### F5. Cache symbols clash with the series notation

- **Where:** `src/content/blog/memory-hierarchy-and-locality.mdx:186–192`, Section 2.1, and `:827`, Summary.
- **Text:** "A cache of capacity $C$ bytes with line size $L$ bytes and **associativity** $W$ (the number of lines, or **ways**, per set) has $S = \frac{C}{L\,W}$ sets"; Summary: "$S = C/(L\,W)$ sets".
- **Problem:** Entry 1 declares its notation "for the whole series" (line 18), including the speedup $S(p)$ and the work $W$. Entry 2 uses $S$ and $W$ for the number of sets and the associativity, and in Section 4 it also discusses intensity and work, so the same letters carry two meanings in one entry and across the series (standards 5.5; skill "Notation and depth").
- **Recommended correction:** Use $k$ for the associativity and $N_{\mathrm{sets}}$ for the number of sets: line 186 "and **associativity** $k$ (the number of lines, or **ways**, per set) has", line 189 "$N_{\mathrm{sets}} = \frac{C}{L\,k}$", line 192 "sets; for the L1 data cache of the reference machine, $N_{\mathrm{sets}} = 49\,152/(64 \times 12) = 64$" and "the next $\log_2 N_{\mathrm{sets}} = 6$ bits", line 207 "($k = 1$)", and the Summary row "$N_{\mathrm{sets}} = C/(L\,k)$ sets".

### F6. $W$ as a row width in the fifth entry

- **Where:** `src/content/blog/distributed-memory-and-message-passing.mdx:394`, Section 5.2.
- **Text:** "with ghost rows $0$ and $n+1$, each of width $W = N + 2$ including the boundary columns."
- **Problem:** $W$ is the work in the series notation (entry 1, line 18), and the fifth entry relates its scaling results to the first entry's laws. The code variable `W` may stay, but the prose symbol should not reuse the series symbol.
- **Recommended correction:** "with ghost rows $0$ and $n+1$, each of $N + 2$ values including the boundary columns (the variable `W` in the code)."

### F7. Promise of a model "built from measured message costs"

- **Where:** `src/content/blog/performance-models-and-scaling-laws.mdx:144`, Section 2.2.
- **Text:** "The [fifth entry](/blog/distributed-memory-and-message-passing) replaces $c\,(p-1)$ with a communication model built from measured message costs."
- **Problem:** Entry 5 measures $\alpha$ and $\beta$ on the reference machine (Sections 3.2–3.3) and checks its sweep model against that machine (Section 6.1), but its strong- and weak-scaling predictions (Sections 6.2–6.3, the replacement for $c\,(p-1)$) use an assumed network, "illustrative, not measurements of any particular network" (line 255). The promise is only partly kept as worded.
- **Recommended correction:** "The [fifth entry](/blog/distributed-memory-and-message-passing) replaces $c\,(p-1)$ with a communication model built from the latency and bandwidth of each message, measured on the reference machine and assumed for a cluster."

### F8. "The first entry ended with the roofline bound"

- **Where:** `src/content/blog/memory-hierarchy-and-locality.mdx:14`, opening paragraph.
- **Text:** "[The first entry](/blog/performance-models-and-scaling-laws) ended with [the roofline bound](/blog/performance-models-and-scaling-laws#5-the-roofline-bound), ..."
- **Problem:** The roofline is Section 5 of the first entry; Section 6, "Measuring performance honestly", follows it, and the second entry itself refers to that section (line 20). The description of the earlier entry is inaccurate.
- **Recommended correction:** "[The first entry](/blog/performance-models-and-scaling-laws) developed [the roofline bound](/blog/performance-models-and-scaling-laws#5-the-roofline-bound), ..."

### F9. Overview version statements do not match the entries

- **Where:** `src/content/series/parallel-and-high-performance-computing.md:16`.
- **Text:** "The code uses C11 compiled with GCC 13, OpenMP for threads and Open MPI 4.1 for message passing, with Python 3 for the models."
- **Problem:** Standards 6.5 make the overview the place for "the conventions shared by all entries (notation, units, language versions)". Every entry states GCC 13.3 and Python 3.13; entries 2 and 5 also use NumPy 2.5 (verified as 2.5.3 by the item fact-checks). Entry 3 (line 18) says OpenMP specification 5.2 is "the version used throughout the series", and entries 1, 3 and 4 cite it, but the overview names no version. "Open MPI 4.1" names the library, while entry 5 (line 36) cites MPI Version 4.1 of the standard and notes that Open MPI 4.1.6 implements MPI 3.1: a reader of the overview can easily take "4.1" for the standard's version.
- **Recommended correction:** "The code uses C11 compiled with GCC 13.3, OpenMP (specification version 5.2) for threads and the Message Passing Interface (MPI), through Open MPI 4.1.6, for message passing, with Python 3.13, and NumPy 2.5 where stated, for the models." Update `src/content/series/vi/parallel-and-high-performance-computing.md` in the same commit if it exists.

### F10. One work cited in two forms

- **Where:** `src/content/blog/performance-models-and-scaling-laws.mdx:695`, `src/content/blog/memory-hierarchy-and-locality.mdx:850`, `src/content/blog/threads-and-shared-memory-parallelism.mdx:672`.
- **Text:** entry 1: "... *Communications of the ACM*, vol. 52, no. 4, pp. 65–76, 2009, doi: 10.1145/1498765.1498785."; entries 2 and 3: "... *Communications of the ACM*, vol. 52, no. 4, pp. 65–76, 2009."
- **Problem:** The DOI was added to entry 1 during its fact-check (resolution F5) and not carried to the other entries. Standards 9.2 ("references complete and consistent") and the brief expect the same work to be cited identically across the series. The other shared references (Hennessy and Patterson, McCalpin, Little, Karp and Flatt, OpenMP 5.2) are already identical.
- **Recommended correction:** End the Williams, Waterman and Patterson entry in both `memory-hierarchy-and-locality.mdx:850` and `threads-and-shared-memory-parallelism.mdx:672` with "2009, doi: 10.1145/1498765.1498785."

### F11. Little's law explained twice

- **Where:** `src/content/blog/data-parallelism-vector-units-and-gpus.mdx:233`, Section 3.4.
- **Text:** "The number of warps needed follows from **Little's law** (Little, 1961): in a steady state, the average number of requests in the system equals their arrival rate times the time each spends there. For memory, the bytes in flight equal bandwidth times latency."
- **Problem:** The same definition and the same application to memory are given in entry 2, Section 6.4 (`src/content/blog/memory-hierarchy-and-locality.mdx:779`), which entry 3 (line 181) already refers back to. Standards 6.1: "across a series, a later entry refers back instead of repeating." The back-reference would also show the reader that the GPU's warps play the role of the CPU core's miss trackers.
- **Recommended correction:** "The number of warps needed follows from **Little's law**, which [Section 6.4 of the second entry](/blog/memory-hierarchy-and-locality#64-what-limits-one-core-and-what-limits-many) applied to one CPU core: the bytes in flight equal bandwidth times latency. A GPU keeps them in flight with warps instead of miss trackers." Keep the Little (1961) reference.

### F12. Ideal-reuse intensity: $n/16$ and $n/12$

- **Where:** `src/content/blog/memory-hierarchy-and-locality.mdx:500`, Section 4.1.
- **Text:** "$I = \frac{2n^3}{32\,n^2} = \frac{n}{16}$ FLOP/byte"
- **Problem:** Entry 1, Section 5.2 (line 327), gives $n/12$ for the same case, ignoring the write of $C$, and entry 4, Section 6.2 (line 382), uses $n/12$ again over the link. Entry 2 reconciles its tile intensities with entry 1 in Section 4.3, but not this one.
- **Recommended correction:** After "$= \frac{n}{16}$ FLOP/byte," add "($n/12$ if the write of $C$ is not counted, as in [Section 5.2 of the first entry](/blog/performance-models-and-scaling-laws#52-intensity-of-three-kernels)),".

### F13. $f_s$ redefined in the fifth entry

- **Where:** `src/content/blog/distributed-memory-and-message-passing.mdx:530` and `:549`, Section 6.3.
- **Text:** "and $f_s$ is the fraction of $T_p$ spent communicating."
- **Problem:** In entry 1 (line 18), $f_s$ is the serial fraction of the parallel run. Entry 5 deliberately substitutes the communicating fraction and explains the difference (line 549), so this is not an error, but the symbol changes meaning without saying so where it is defined.
- **Recommended correction:** "and $f_s$, by analogy with Gustafson's serial fraction, is here the fraction of $T_p$ spent communicating."

### F14. "The C11 standard" cited as ISO/IEC 9899:2018

- **Where:** `src/content/blog/threads-and-shared-memory-parallelism.mdx:189`, Section 3.1.
- **Text:** "The C11 standard defines the problem precisely, in subclause 5.1.2.4 of ISO/IEC 9899:2018 (the 2018 edition, which replaced C11 and keeps these definitions in the same subclause)."
- **Problem:** The sentence names the 2011 edition and then cites the 2018 edition as its source. The meaning is recoverable, but the wording contradicts itself.
- **Recommended correction:** "The C standard defines the problem precisely, in subclause 5.1.2.4 of both C11 and its 2018 revision, ISO/IEC 9899:2018, which is cited here."

### F15. "a kernel-based virtual machine (KVM)"

- **Where:** `src/content/blog/data-parallelism-vector-units-and-gpus.mdx:18`.
- **Text:** "a kernel-based virtual machine (KVM) with 4 cores"
- **Problem:** KVM is the Kernel-based Virtual Machine hypervisor, a proper name; the other entries write "a virtual machine under the Kernel-based Virtual Machine (KVM) hypervisor" or "a Kernel-based Virtual Machine (KVM) guest".
- **Recommended correction:** "a Kernel-based Virtual Machine (KVM) guest with 4 cores" (combine with F1).

### F16. Saturation stated as fact in the third entry

- **Where:** `src/content/blog/threads-and-shared-memory-parallelism.mdx:179`, Section 2.4.
- **Text:** "these four cores are a small part of a large server processor, and together they did not reach its memory system's limit."
- **Problem:** Entry 2, Section 6.4 (line 781), presents the same point as "an inference from the near-linear scaling, not a measurement of where saturation lies". Standards 5.7 ask for interpretations to be worded as such.
- **Recommended correction:** "these four cores are most likely a small part of a large server processor, and together they did not reach its memory system's limit."

### F17. The `...` row in the latency output

- **Where:** `src/content/blog/memory-hierarchy-and-locality.mdx:151` and `:166`.
- **Text:** "(the median of five timings of $2^{23}$ steps for each size; the 8 KiB, 128 KiB, 512 KiB and 8 MiB rows are omitted)" and a `...` line between the 32 MiB and 64 MiB rows.
- **Problem:** The `...` marks where the second run (from 64 MiB) begins, but the convention elsewhere in the series is that `...` marks omitted lines, and the rows actually omitted are listed in the text.
- **Recommended correction:** Remove the `...` line, or change the lead-in to "...; the 8 KiB, 128 KiB, 512 KiB and 8 MiB rows are omitted, and `...` marks where the second run begins".

### F18. In-text citation style

- **Where:** e.g. `performance-models-and-scaling-laws.mdx:148` ("Karp and Flatt proposed"), `threads-and-shared-memory-parallelism.mdx:299` ("Adve and Gharachorloo's tutorial") against `memory-hierarchy-and-locality.mdx:26` ("Wulf and McKee (1995)") and `data-parallelism-vector-units-and-gpus.mdx:191` ("(Lindholm and colleagues, 2008; ...)").
- **Problem:** The standards fix the reference-list format but not the in-text form; entries 1 and 3 name authors without years, entries 2, 4 and 5 add years. This is polish, not a defect.
- **Recommended correction:** Choose one form for the series (names with year at first mention is the more common in the archive) and apply it when the entries are next revised.

## Concept introduction map

| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
| Speedup, efficiency, best sequential program | `performance-models-and-scaling-laws.mdx:18` | same, `:18` and `:34` | Good |
| Amdahl's and Gustafson's laws, $f$, $f_s$ | `performance-models-and-scaling-laws.mdx:18` | same, `:60–74`, `:164–172` | Good; $f_s$ reused in entry 5 (F13) |
| Work, span, DAG | `performance-models-and-scaling-laws.mdx:18` | same, `:221–229` | Good |
| Roofline, arithmetic intensity, ridge point | `performance-models-and-scaling-laws.mdx:18` | same, `:319`, with the insight as stated prerequisite | Good |
| Cache, cache line, L1/L2/L3 | `performance-models-and-scaling-laws.mdx:22`, `:52` | `memory-hierarchy-and-locality.mdx:28`, `:184`; entry 1 points forward at `:52` | Acceptable |
| Write-allocate | `performance-models-and-scaling-laws.mdx:333` | defined in place; developed `memory-hierarchy-and-locality.mdx:217` | Good |
| OpenMP | `performance-models-and-scaling-laws.mdx:20`, `:359` | `threads-and-shared-memory-parallelism.mdx:18`, `:85`; entry 2 points forward at `:773`; entry 1 does not | F4 |
| STREAM triad | `performance-models-and-scaling-laws.mdx:337` | same | Good |
| Fused multiply-add, AVX-512 | `performance-models-and-scaling-laws.mdx:22`, `:399` | same, `:399`; registers in `data-parallelism-vector-units-and-gpus.mdx:49` | Good |
| Thread, process, core, coherence | `performance-models-and-scaling-laws.mdx:18` | `threads-and-shared-memory-parallelism.mdx:26`, `:40`, `:59` | Good; entry 1 says later entries introduce them |
| Data race, happens-before | `threads-and-shared-memory-parallelism.mdx:189` | same | Good |
| False sharing | `memory-hierarchy-and-locality.mdx:672` | defined there; measured in entry 3, `:455` | Good |
| Little's law | `memory-hierarchy-and-locality.mdx:779` | same; repeated in entry 4 `:233` | F11 |
| Vector register, lane, SIMD | `data-parallelism-vector-units-and-gpus.mdx:35` | same, `:35`, `:49` | Good |
| GPU, SM, warp, SIMT | `data-parallelism-vector-units-and-gpus.mdx:14` | same, `:191–220` | Good |
| MPI, rank, communicator | `distributed-memory-and-message-passing.mdx:16` | same, `:32–36` | Good |
| Latency-bandwidth model, $n_{1/2}$ | `performance-models-and-scaling-laws.mdx:18` (announced) | `distributed-memory-and-message-passing.mdx:171–181` | Good |
| Domain decomposition, ghost cells | `distributed-memory-and-message-passing.mdx:378` | same, `:378–382` | Good |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| C11 (`-std=c11`) | All entries, Conventions | Yes | Consistent; entry 3 cites C17 for the memory model (F14) |
| GCC 13.3 | All entries | Yes; overview says "GCC 13" | F9 |
| `-std=c11` disables FMA contraction | Entry 1 `:599`, entry 4 `:92` | Yes, consistently | Good (reproduced by entry 4's technical review) |
| Preferred vector width 256 bits under `-march=native` | Entry 1 `:599`, entry 2 `:663`, entry 4 `:92` | Yes | Target name in entry 4 unverified (F3) |
| OpenMP specification 5.2 (GCC 13 reports 4.5) | Entry 3 `:18`; references of entries 1, 3, 4 | Yes in entry 3; not in the overview | F9 |
| MPI standard 4.1; Open MPI 4.1.6 implements MPI 3.1 | Entry 5 `:18`, `:36` | Yes | Overview's "Open MPI 4.1" ambiguous (F9) |
| Python 3.13; NumPy 2.5 | Entries 1–5; entries 2, 5 | Yes; overview says "Python 3", no NumPy | F9 |
| Eager limit 4,096 bytes (`btl_vader_eager_limit`) | Entry 5 `:95` | Yes, with "would differ with another library" | Good |
| Doubles of 8 bytes, row-major, 64-byte lines, 4 KiB pages | Overview; entries 1, 2 | Yes | Consistent |
| GB/s = $10^9$ B/s, KiB/MiB for sizes | Entries 1, 2, 3, 4, 5 | Yes | Consistent |
| STREAM byte count (24 bytes per triad element, write-allocate not counted) | Entries 1 `:342`, 2 `:722`, 3 `:179` | Yes | Consistent |
| Reference machine: 4 cores, 48 KiB L1d, 2 MiB L2, 260 MiB L3 reported, 16 GiB | Entries 1–5 | Yes | Consistent; clock wording differs (F1) |
| Measured $B \approx 50$ GB/s, $P_{\mathrm{peak}} \approx 354$ GFLOP/s, $I^* = 7.08$ | Entry 1 `:467`; entry 2 `:30` (6.8 for one core) | Yes, labeled estimates | Consistent; one-core bandwidth (F2) |
| Assumed GPU and cluster figures | Entry 4 `:338`; entry 5 `:255` | Yes, labeled assumed | Good |

## Series design

**Purpose, audience and scope.** The overview names the reader (engineers and students who write numerical code), the prerequisites (C, Python, cost of sequential code, the Numerical Simulation series and the roofline insight) and the scope from performance models to message passing. The objectives are checkable and each is met by a named entry. No finding beyond F9.

**Sequence rationale.** The overview explains the order (models first, then memory, threads, data parallelism, distributed memory) and each entry's closing paragraph leads to the next. The order serves the reader: every entry's measurements are judged with the first entry's models, and the second entry's bandwidth result is what the third entry's triad scaling and the fourth entry's roofline arguments build on.

**Prerequisites and dependencies.** Nothing depends on a later entry except entry 1's use of OpenMP for two measurements (F4) and entry 2's single four-thread triad, which points forward to entry 3. The forward pointers in entry 1 (caches, load imbalance, vector code, message costs) all reach sections that deliver them; F7 qualifies one.

**Notation and depth.** The first entry declares the series notation and the later entries keep it for $T_p$, $S(p)$, $E(p)$, $P_{\mathrm{peak}}$, $B$, $I$, $\alpha$ and $\beta$; $S$ and $W$ are reused in entries 2 and 5 (F5, F6) and $f_s$ in entry 5 (F13). Depth is comparable: every entry has derivations, run code with real output, a limits section, exercises with answers, a summary table and references. The GPU half of entry 4 is necessarily illustrative and says so.

**Overview completeness.** The overview's description and body match what the entries deliver; its one gap is the version paragraph (F9).

## Series-level notes

Cross-reference map (all links resolve, checked by `check:links` and by reading each target section):

| From | To | Claim | Holds |
|---|---|---|---|
| E1 §1.4, §5.2, end | E2 (§4, whole) | why access cost depends on location; blocking | Yes |
| E1 §2.2 | E5 | replaces $c\,(p-1)$ with a communication model | Partly (F7) |
| E1 §2.4, §4.2 | E3 §6 | load imbalance | Yes |
| E1 §3.3 | E5 §6 | communication in scaling predictions | Yes |
| E1 §4.3 | E3, E5 | reductions in OpenMP and MPI | Yes (E3 §2.3, §3.3; E5 §4.2) |
| E1 §5.5, §6.3 | E4 §2 | vectorization lowers the roof; vector code generation | Yes |
| E2 opening | E1 §5, §6 | roofline; measurement | "ended with" (F8) |
| E2 §2.4, §5.3 | E3 §5 | false sharing | Yes |
| E2 §5.2 | E4 §2 | unit stride for vector units | Yes (E4 §2.4) |
| E2 §6.3, §6.4 | E3 | OpenMP; bandwidth shared by cores | Yes (E3 §2, §2.4) |
| E3 §2.4, end | E4 | vector instructions | Yes |
| E4 opening, §2.2, §2.5, §4.1, §4.4, §5.5 | E1–E3 | roofline, layouts, races, compiler defaults, blocking, measurement | Yes |
| E5 opening, §6.2, §6.3, end | E1–E4 | laws, Karp–Flatt, overheads, Gustafson | Yes |

Repeated material that is deliberate and cross-referenced: three STREAM-style triads (entries 1, 2, 3), each comparing its figure with the earlier one; the reference-machine paragraph in each entry, required by standards 6.2. Repetition that should become a cross-reference: Little's law (F11).

Structure and tone are uniform: numbered sections, a Conventions paragraph, measured output with stated noise, Exercises, Summary table and References in every entry.

The per-item resolutions were checked against the text: every change recorded in the five Resolution sections is present (for example entry 1's `p* = 30.8` output line and Exercise 4 answer, entry 2's regenerated `layout.c:29:26` report and the 38 216 / 36 864 / 33 792 sentence, entry 3's "reported at 2.1 GHz" and the four "output was not kept" qualifications, entry 4's $D = 2$ and single-accumulator explanation, entry 5's 3974.24 / 3974.22 and "up to about 23,000 points"). No resolution introduced a new defect within its entry; F1 and F2 are inconsistencies the resolutions of entries 3 and 4 made visible but did not create.

## Verification log

- `npm run build:local`: exit 0 (astro check, build, Pagefind "Indexed 2 languages, Indexed 109 pages"; check-site-url warns about localhost URLs, as expected for a local build).
- `npm run check:links`: "Checked 330 pages and 10279 internal references in dist. All internal links resolve."
- Mermaid widths in `dist/blog/<slug>.html`: entry 1 415px, entry 2 193px, entry 3 321px, entry 4 607px (at the limit of the ~612px column; not raised), entry 5 142px and 235px.
- Glued inline elements: no letter or punctuation glued to `<a `, `<code>`, `<strong>` or `<em>` (and none after their closing tags) in the five pages outside KaTeX output.
- Recomputed (reviewer's runs on the current host; deterministic only):
  - Entry 1: `amdahl.py`, `gustafson.py`, `reduction.py`, `roofline.py` reproduce the quoted outputs exactly. By hand: $S(21) = 10.5$; Amdahl at $p = 32$, $f = 0.05$: 12.55; Karp–Flatt 0.083 and Exercise 2 (0.0526, 0.0588, 0.0612); $S_s(1024) = 972.85$; medians 354.0 and 90.6 GFLOP/s and clocks 2.77 and 2.83 GHz; 1.2% and 1.8% of peak; 1.65 GFLOP/s from 13.2 GB/s; 1.71 × median and 15% spread; −17% median change; 250,001 steps; Exercise 5 2.4%.
  - Entry 2: `cachesim.py` output is byte-identical to the writer's `cachesim.txt` (md5 e0b35e0e…); set index of `0x7ffd1234` (8), `0x10000` (0), `0x13040` (1); 11.3×, 21.9×, 7.9× for 7.4% more work, 1.31× and 1.43×, 7.4× and 6.7×, 68%; AoS/SoA 21.3 and 19.6 GB/s, traffic ratio 5.33; Little's law 2685 bytes, 42 lines; huge-page differences 34 to 59 ns; Exercises 1, 3, 4.
  - Entry 3: 52.8 and 240 ns per increment; 9.2× and 14.3×; 1785 and 2380 cycles; 2851 FLOP; triangular-loop shares, $16/7 = 2.29$, $64/15 = 4.27$; $W$, $W/p + D$, 0.04%; 405× for `dynamic,1`; 21× false-sharing ratio.
  - Entry 4: `offload.py` reproduces the table and break-even $n = 253$; formula 252.6; 390 625 blocks; 62 500 loads; 50% occupancy; GFLOP/s and GB/s from the axpy and reduction timings; Exercises 3, 5, 6. `gcc -Q --help=target` (13.3.0): preferred width 256 for `skylake-avx512`, `cascadelake`, `icelake-server`, `sapphirerapids` (F3).
  - Entry 5: `model.py` and `collectives.py` outputs identical to the writer's `model.out` and `collectives.out`; `fit.py` reproduces the three fits; $n_{1/2}$ values; half-bandwidth check 4.15 GB/s; allreduce model 0.74 µs; $\pi^2/6 - $ total and 2.4e-10 remainder; medians and $S(2) = 1.75$, $S(4) = 2.98$ and 3.52; relative difference 2.6e-13; Gustafson check $f_s = 0.0297326$, model 3974.215, law 3974.245; Exercise 4.
- Not verified: every reference-machine timing (the container now runs on a different host, 2.8 GHz with 32 KiB L1d and 1 MiB L2, so the timings cannot be re-observed; they are accepted as the writers' measurements, as the per-item reviews did); the target `-march=native` selected on the reference machine (F3); the primary text of Amdahl (1967), as recorded in entry 1's fact-check. Vietnamese translations were not reviewed.
