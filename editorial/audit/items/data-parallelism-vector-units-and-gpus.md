# Editorial review: Data Parallelism: Vector Units and GPUs

- Path: `src/content/blog/data-parallelism-vector-units-and-gpus.mdx` · Route: `/blog/data-parallelism-vector-units-and-gpus` · Type: article (series entry) · Series `parallel-and-high-performance-computing`, entry 4 of 5
- Stages in this report so far: developmental edit (EOS 6.1) and copy edit (EOS 6.2), performed by an editor who did not write the entry. Line numbers refer to the file after this revision.
- Read for context: the series overview, the first, second, third and fifth entries (headings and the sections this entry cites: first entry 4, 5 and 6.3; second entry 4 and 5.2; third entry 3), the insights `compute-bound-or-memory-bound` and `floating-point-in-long-simulations`, and `solving-large-linear-systems` Section 4.

## Developmental review

The entry does its job well. The opening names what it builds on (three linked sections of earlier entries), what it covers, and the versions, machine and conventions it assumes, including the integrity statement that no GPU code was run. Concepts come before mechanics throughout (data parallelism and Flynn's classes before registers; warps before divergence; global and shared memory before tiling; the cost model before its reading). Measured claims are shown with their program output; GPU figures are labeled as assumed or cited. Exercises have answers, the Summary table matches the body, and the closing paragraph leads to the fifth entry. The fifth entry's description of this one ("moved data to a graphics processor and back, and found that the transfer decides whether offloading pays") is accurate. The structure needed no reordering.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:16`, opening | purpose | Second opening paragraph was a table of contents in prose ("The first half ... The second half ..."). |
| D2 | Should fix | `:463`, Summary | consistency | Summary said memory-bound loops "stop at the bandwidth roof" without the measured 1.4 to 1.5 times gain of Section 2.3, which reads as "no gain". |
| D3 | Should fix | `:163`, Section 2.5 | consistency | "the first entry met the same effect in a dot product": unlinked, unnumbered cross-reference (standards 8.1). |
| D4 | Optional | `:199`, Section 3.2 | structure | Third statement that GPU listings were not run (Conventions and the code comment already say so). |
| D5 | Optional | `:315`, Section 5.4 | evidence | Uncited general claim on FP64/FP32 throughput by product class; referred to the fact-checker. |
| D6 | Optional | `:32`, Section 1.2 | evidence | Flynn's classification is attributed to the 1972 paper; it first appeared in Flynn's 1966 paper. Referred to the fact-checker. |

### D1. Opening reads as a table of contents
- **Where:** `:16`, opening paragraphs
- **Text:** "The first half shows vector instructions on a CPU at work, with compiler reports and timings, and the program properties that stop a compiler from using them. The second half turns to the GPU, its execution model, memory and limits, and ends with ..."
- **Problem:** Agent checklist item 6 and standards 6.1: the introduction should set up the argument, not list the sections.
- **Correction (applied):** "The same roofline reasoning runs through both halves. On the CPU, compiler reports and timings show which loops gain from vector instructions and which program properties stop a compiler from using them. On the GPU, the execution model, the memory system and the limits explain how the hardware keeps thousands of lanes busy, and a cost model decides when moving a computation to the GPU repays the cost of moving its data."

### D2. Summary understated the memory-bound result
- **Where:** `:463`, Summary table
- **Text:** "memory-bound loops stop at the bandwidth roof."
- **Problem:** Section 2.3 reports that vectorization made axpy 1.4 to 1.5 times faster and that wider vectors then gave nothing; the summary row omitted the first half of that result.
- **Correction (applied):** "... memory-bound loops stop at the bandwidth roof (axpy gained 1.4 to 1.5 times, and nothing more from 8 lanes)." (Numbers copied from the body; see T2 for the range itself.)

### D3. Vague cross-reference
- **Where:** `:163`, Section 2.5
- **Text:** "the first entry met the same effect in a dot product."
- **Problem:** Standards 8.1 ("Cross-references cite numbered sections"). The effect is in Section 6.3 of the first entry ("without permission to reorder the additions it keeps them in one sequential chain").
- **Correction (applied):** "[Section 6.3 of the first entry](/blog/performance-models-and-scaling-laws#63-problem-size-and-compiler-settings) measured the same effect in a dot product." The heading "### 6.3 Problem size and compiler settings" exists; the link checker should confirm the fragment.

### D4. Repeated not-run statement
- **Where:** `:199`, Section 3.2
- **Text:** "The listing is an illustration in CUDA C++; it was not compiled or run for this entry, because the reference machine has no GPU:"
- **Correction (applied):** "The listing, in CUDA C++, is an illustration that was not compiled or run (see Conventions):". The label stays visible at the listing and in the code comment.

### D5. FP64 throughput claim without a source (referred)
- **Where:** `:315`, Section 5.4
- **Text:** "is much lower on products designed mainly for graphics than on those designed for scientific computing."
- **Problem:** A general, hedged claim with no citation. It is widely documented, but the entry quotes no source.
- **Correction:** For the fact-checker: cite a source already in the list that states it (Hwu, Kirk and El Hajj, 2022, or Hennessy and Patterson, 2017, chapter 4), if it does; otherwise leave as a qualified general statement. Text unchanged.

### D6. Date of Flynn's taxonomy (referred)
- **Where:** `:32`, Section 1.2
- **Text:** "Flynn (1972) classified computer organizations by the number of instruction streams and data streams"
- **Problem:** The four classes were introduced in M. J. Flynn, "Very high-speed computing systems," *Proceedings of the IEEE*, 1966; the 1972 paper is the commonly cited development of them. Not a falsehood (the 1972 paper does classify them), but a reader may take 1972 as the origin.
- **Correction:** For the fact-checker: verify, and if confirmed consider "Flynn (1966, 1972)" with the 1966 reference added after its details are checked. Text unchanged.

### Developmental verdict

**pass.** Counts: 0 blocking, 3 should fix (all applied), 3 optional (D4 applied; D5 and D6 referred to the fact-checker, text unchanged). No `##` or `###` heading was changed.

## Copy edit

Commands: `npm run eos -- lint` (before: 0 errors, 0 warnings, 12 suggestions); `npm run eos -- fix --rules spelling-variant,terminology` (0 fixes needed). Manual checks: no contractions, no em dashes, no "simply/obviously/clearly/of course", headings in sentence case, "we" only in the derivation step at `:387` ("Dividing by $2n^2$, we get"), American spelling, no serial comma in lists.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:96`, Section 2.3 | language | "run under the benchmark lock": undefined jargon. |
| C2 | Should fix | `:233`, Section 3.4 | language | "How many are needed": no noun for "many". |
| C3 | Should fix | `:18` | language | Conventions paragraph of 185 words covering two topics (lint `paragraph-length`). |
| C4 | Optional | `:28`, Section 1.1 | language | "The hardware of this entry is built for that second way." |
| C5 | Optional | `:141`, `:191`, `:241`, `:311`, `:439` | language | Sentences of 46 to 53 words (lint `sentence-length`). |
| C6 | Optional | `:16` (before) | language | Lint `serial-comma` on "its execution model, memory and limits, and ends with": a compound predicate, not a serial comma; the sentence was rewritten under D1. |
| T1 | Should fix | `:92`, Section 2.2 | accuracy | "16 `vmulpd` and 16 `vaddpd` instructions in the vectorized polynomial loop": Horner of degree 8 needs 8 of each per vector; referred to the technical reviewer. |
| T2 | Should fix | `:112`, Section 2.3 | accuracy | "1.4 to 1.5 times faster" does not include the run shown: 0.112/0.072 = 1.56 (256-bit) and 22.3/14.4 = 1.55; referred. |
| T3 | Optional | `:26`, Section 1.1 | accuracy | "the work is $W = 2n$ operations and the span is $D = 1$ update": mixed units in $W/D$; referred. |
| T4 | Optional | `:301`, Section 5.1 | accuracy | "the threads reconverge after the branch": true of the classic SIMT model; on architectures with independent thread scheduling reconvergence is not guaranteed at the branch end; referred. |

### C1. Undefined term
- **Text:** "The same source was built three ways and run under the benchmark lock:"
- **Correction (applied):** "... and run with no other benchmark on the machine:" (the meaning stated in Conventions: "taken while no other benchmark ran").

### C2. Missing noun
- **Text:** "How many are needed follows from **Little's law**"
- **Correction (applied):** "The number of warps needed follows from **Little's law**".

### C3. Long Conventions paragraph
- **Correction (applied):** split before "The reference machine has no GPU:", separating the CPU measurement conventions from the GPU and unit conventions.

### C4. Awkward closing sentence
- **Correction (applied):** "The hardware this entry describes is built for the second way."

### C5. Long sentences
- **Applied:** split the AoS/SoA sentence (`:141`) at the semicolon; the timing lead-in sentence into two; the SM sentence (`:191`) after "a small fast memory"; the shared-memory definition (`:241`); the cross-block deadlock sentence (`:311`); Exercise 5 (`:439`) into "In (a) ... In (b) ...". No technical content changed.

### T1. Instruction count in the polynomial loop (for the technical reviewer)
- **Where:** `:92`, Section 2.2
- **Text:** "The disassembly confirms 16 `vmulpd` and 16 `vaddpd` instructions in the vectorized polynomial loop"
- **Problem:** The source performs 8 multiplications and 8 additions per element, so one 4-lane vector iteration needs 8 of each. 16 is consistent with a loop unrolled by two, or with counting the 32-byte loop and the 16-byte epilogue together; the text does not say which.
- **Correction:** check the disassembly and state what the 16 covers (for example "16 ... in the vectorized loop, which GCC unrolled to two vectors per iteration", or "8 per vector iteration"). Text unchanged.

### T2. Range of the axpy gain (for the technical reviewer)
- **Where:** `:112`, Section 2.3, and Summary `:463` (copied there under D2)
- **Text:** "Vectorization made the loop 1.4 to 1.5 times faster than the scalar build in repeated runs"
- **Problem:** Recomputed from the output printed in the same section: 256-bit 0.112/0.072 = 1.56 (rates 22.3/14.4 = 1.55); 512-bit 0.112/0.077 = 1.45. The shown run is outside the stated range for the 256-bit build.
- **Correction:** widen the range to the runs actually observed (for example "1.4 to 1.6"), or say which builds the range refers to; update the Summary row to match. Text unchanged.

### T3. Units of the span (for the technical reviewer)
- **Where:** `:26`, Section 1.1
- **Text:** "the work is $W = 2n$ operations and the span is $D = 1$ update, so the parallelism $W/D$ grows with $n$."
- **Problem:** The first entry defines $W$ and $D$ in operations; in those units one update is a multiply then an add, $D = 2$, and $W/D = n$. The conclusion (grows with $n$) is unaffected.
- **Correction:** consider "$D = 2$ operations (one multiplication, then one addition), so $W/D = n$". Text unchanged.

### T4. Reconvergence (for the technical reviewer)
- **Where:** `:301`, Section 5.1
- **Text:** "and the threads reconverge after the branch (Hwu, Kirk and El Hajj, 2022)."
- **Correction:** check against the cited book; if needed qualify ("and, in the classic SIMT model, reconverge after the branch"). Text unchanged.

### Accuracy spot-checks by the copy editor (no defect found)
Recomputed from the printed figures: poly 3.2768 × 10^9 FLOP / 0.421 s = 7.78 GFLOP/s, 28.40/7.79 = 3.6, 30.14/7.79 = 3.9; axpy rates and 22.3 × 0.083 = 1.86; AoS/SoA 0.129/0.056 = 2.3; reduction 4.096 × 10^8 additions, 1.73 and 8.03 GFLOP/s, ratio 4.6; difference of 4 ulp (ulp 2^−34 at 5.2 × 10^5); Little's law 5 × 10^5 bytes and 62 500 loads; occupancy 50%; 390 625 blocks; stride-16 4096 bytes; tiling $T/8$; every row of the offload table; break-even 252.6; Exercises 2 to 6.

### Lint suggestions kept
- `:18` "GNU": part of the proper name "GNU Compiler Collection", already given in full; GNU is a recursive acronym with no useful expansion.
- `:53` "SSE2", `:54` "AVX2": product names of extension versions; the base names SSE and AVX are expanded in the same table rows.
- `:191` "NVIDIA": a company name, not an abbreviation.
- `:479` "IA": inside the title of a cited work (Intel manual), which keeps its original form.

### Copy-edit verdict

**pass.** Counts (copy findings): 0 blocking, 3 should fix (applied), 3 optional (applied or answered). Referred to the technical reviewer, text unchanged: T1 and T2 (should fix), T3 and T4 (optional). Final `npm run eos -- lint`: 0 errors, 0 warnings, 5 suggestions (kept, reasons above).

<!-- Later stages (fact-check, technical review, resolution, QA) add their sections below. -->
