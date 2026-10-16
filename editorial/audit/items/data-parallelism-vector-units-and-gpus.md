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

## Fact-check

Stage EOS 6.3, performed by a reviewer who did not write or revise the entry. Line numbers refer to the file as it stands after the copy edit. Sources were searched with WebSearch. Direct fetches of publisher, DBLP and NVIDIA pages were refused by this session's network proxy (`docs.nvidia.com`, `dblp.org`: CONNECT 403; `en.wikipedia.org`: not resolvable), so bibliographic details rest on catalogue and Crossref records returned by search, and on standard textbook knowledge where stated. Compiler claims were also checked by running GCC 13.3.0 on this machine (see the technical review log).

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Optional | `:32`, Section 1.2 | evidence | Flynn's classes first appeared in his 1966 paper; the text dates them to 1972 only (D6, confirmed). |
| F2 | Optional | `:315`, Section 5.4 | evidence | FP64/FP32 claim has no citation; none of the listed works could be confirmed to state it. Keep as a qualified general statement (D5). |

### F1. Origin of Flynn's taxonomy (resolves D6)
- **Where:** `:32`, Section 1.2; References `:476`
- **Text:** "Flynn (1972) classified computer organizations by the number of instruction streams and data streams they process at once."
- **Problem:** The 1966 paper exists: M. J. Flynn, "Very high-speed computing systems," *Proceedings of the IEEE*, vol. 54, no. 12, pp. 1901–1909, December 1966 (Crossref citation record: 1966, pp. 1901–1909; UC Berkeley CS252 reading list: vol. 54, no. 12, December 1966; DOI 10.1109/PROC.1966.5273). Course material and reference works consistently date the taxonomy to 1966 and describe the 1972 paper as its development ("Flynn's taxonomy (1966)", University of Washington CSE 471; "slightly expanded in 1972"). The 1972 paper does classify organizations this way, so the sentence is not false, only incomplete about the origin.
- **Correction:** "Flynn (1966) classified computer organizations by the number of instruction streams and data streams they process at once, and developed the classification in a later paper (Flynn, 1972). The four classes are:" and add to the References, before the 1972 entry: "- M. J. Flynn, "Very high-speed computing systems," *Proceedings of the IEEE*, vol. 54, no. 12, pp. 1901–1909, 1966." Optional: leaving the text unchanged is defensible.

### F2. FP64 throughput by product class (resolves D5)
- **Where:** `:315`, Section 5.4
- **Text:** "The throughput of double-precision (FP64) arithmetic relative to single precision (FP32) differs widely between GPU products, and is much lower on products designed mainly for graphics than on those designed for scientific computing."
- **Problem:** The claim is correct as general knowledge (NVIDIA's *CUDA C++ Programming Guide* tabulates FP64 and FP32 operations per clock per SM by compute capability; a third-party reproduction of that table gives 32 FP64 operations per clock per SM for compute capability 8.0, the A100). I could not fetch the guide itself, and I could not confirm from the text of Hwu, Kirk and El Hajj (2022) or Hennessy and Patterson (2017) that either states it, so citing them would attribute a claim they may not make.
- **Correction:** No change. The sentence is hedged, quotes no figure and sends the reader to vendor documentation. Do not attach a citation to a listed book unless its page is checked.

### Verification table

| Claim | Location | Status | Source |
|---|---|---|---|
| Flynn 1972 reference: authors, title, *IEEE Trans. Computers*, vol. C-21, no. 9, pp. 948–960, 1972 | `:476` | Verified | Crossref record, DOI 10.1109/TC.1972.5009071 (September 1972) |
| Flynn's four classes SISD, SIMD, MISD, MIMD by instruction and data streams; MISD has few examples | `:32–37` | Verified; origin corrected (F1) | Flynn 1966 and 1972; Computer History Museum oral-history record; course material |
| Hennessy and Patterson, 6th ed., Morgan Kaufmann, 2017; chapter 4 compares vector, SIMD and GPU architectures | `:57`, `:477` | Verified | Chapter 4 "Data-Level Parallelism in Vector, SIMD, and GPU Architectures" (6th-edition lecture material, OpenPOWER Foundation; Diyala University outline) |
| Hwu, Kirk and El Hajj, *Programming Massively Parallel Processors: A Hands-on Approach*, 4th ed., Morgan Kaufmann, 2022 | `:478` | Verified | Elsevier and O'Reilly listings: print ISBN 978-0-323-91231-0 (August 2022), eBook ISBN 978-0-323-98463-8; Heidelberg University catalogue |
| Intel SDM cited for SSE/AVX/AVX-512 widths and AVX-512 mask registers | `:49–57`, `:479` | Verified (content); year 2024 matches the revisions issued that year | Intel 64 and IA-32 Architectures SDM (standard knowledge; `xmm`/`ymm`/`zmm` and opmask registers `k0`–`k7`); GCC output on this machine uses `%k1` masks (technical log) |
| Lindholm, Nickolls, Oberman, Montrym, *IEEE Micro* vol. 28, no. 2, pp. 39–55, 2008 | `:480` | Verified | NVIDIA Research publication page (March/April 2008); DOI 10.1109/MM.2008.31; university reading lists give pp. 39–55 |
| Tesla architecture of 2006 unified the graphics pipeline into one programmable processor array; CUDA described for Tesla; SIMT named by Lindholm and colleagues | `:191`, `:193`, `:220` | Verified | Lindholm et al. 2008 (abstract and reprint: GeForce 8800, late 2006, unified vertex and pixel processors, C programming through CUDA); SIMT terminology is the paper's |
| Little 1961: *Operations Research*, vol. 9, no. 3, pp. 383–387; L = λW stated correctly | `:233`, `:481` | Verified | DOI 10.1287/opre.9.3.383; Little, "Little's Law as viewed on its 50th anniversary," *Operations Research*, 2011, cites it so |
| OpenMP 5.2, 2021; `simd` construct accepts `reduction`, one private copy per SIMD lane, combined in arbitrary order | `:165`, `:482` | Verified | OpenMP ARB press release "OpenMP ARB releases OpenMP 5.2", 9 November 2021; OpenMP 5.2 spec HTML, reduction clause sections. (The third entry formats this reference "Version 5.2, November 2021"; this entry matches the first entry. Series-level harmonization only.) |
| GCC manual, *Using the GNU Compiler Collection*, by R. M. Stallman and the GCC Developer Community, FSF | `:483` | Verified (title and authors; publisher shown as GNU Press, a division of the FSF, on the manual's title page) | Title pages of GCC 13.x manual copies; GCC 13.3.0 release exists (Debian, MacPorts packages) |
| `-fopt-info-vec`, `-fopt-info-vec-missed`, `-fopt-info-vec-all`, `-fno-tree-vectorize`, `-mprefer-vector-width=512`, `-fopenmp-simd` behave as described | `:61`, `:92`, `:116`, `:165` | Verified | GCC 13.3.0 run on this machine (technical log) |
| `-march=sapphirerapids` default preferred vector width 256 | `:92` | Verified | `gcc -march=sapphirerapids -Q --help=target`: `-mprefer-vector-width= 256` (generic `x86-64` and `znver4`: `none`) |
| `-march=native` selects `sapphirerapids` on the reference machine | `:92` | Not verified | The VM this review ran on reports a different processor (see Not verified) |
| Under `-std=c11` GCC does not contract a*b+c into FMA without `-ffp-contract=fast` | `:92` | Verified | Run: poly has 0 `vfmadd` with `-std=c11`, 24 with `-std=gnu11` and 24 with `-std=c11 -ffp-contract=fast`. GCC 13.3 manual, "Floating point implementation": "Expressions are currently only contracted if -ffp-contract=fast, -funsafe-math-optimizations or -ffast-math are used". (The GCC 13 "Optimize Options" page states the default as `fast` without the ISO-mode exception, which the GCC 14 page adds; the behavior shown in the article is the real GCC 13.3 behavior.) |
| `-fassociative-math` requires `-fno-signed-zeros` and `-fno-trapping-math`; `-ffast-math` includes it | `:165` | Verified | Run: alone it prints "cc1: warning: '-fassociative-math' disabled; other options take precedence" and the sum stays scalar; with both flags, or `-ffast-math`, it vectorizes. GCC manual wording ("requires that both -fno-signed-zeros and -fno-trapping-math be in effect") |
| C99 `restrict`: promise of no other access during the call; violation is undefined behavior | `:137` | Verified | ISO/IEC 9899:1999 and 9899:2011, 6.7.3.1 (formal definition of restrict; "If these requirements are not met, then the behavior is undefined") |
| Warps of 32 threads; blocks on one SM; block-level `__syncthreads`; no global barrier in an ordinary launch; launch errors reported by later query; launches asynchronous; same-stream kernels run in order; `atomicAdd` | `:197`, `:220`, `:295`, `:311`, `:321–324`, `:307` | Verified as standard CUDA behavior; book page not checked | Hwu, Kirk and El Hajj (2022) chapters 3–5 (book text not accessible here); CUDA C++ Programming Guide (via search snippets) |
| Divergent paths executed one after the other, then reconverge after the branch | `:301` | Corrected (T4) | CUDA C++ Programming Guide, "Independent Thread Scheduling": from compute capability 7.0 "threads can now diverge and reconverge at sub-warp granularity"; NVIDIA Volta material: do not assume threads are reconverged after a conditional |
| FP64/FP32 ratio differs by product class | `:315` | Not verified against a cited source (F2) | — |
| Assumed GPU, CPU and link figures; occupancy limits; 128-byte segments | `:233`, `:235`, `:256`, `:338` | Labeled as assumed in the text; no verification needed | — |

### Not verified
- `:92` "here `-march=native` selects GCC's `sapphirerapids` target": the VM available to this review is not the reference machine (it reports `Intel(R) Xeon(R) Processor @ 2.80GHz`, family 6 model 85, 32 KiB L1d and 1 MiB L2 per core, 33 MiB L3; GCC resolves `-march=native` to `cascadelake`). The writer's binaries are byte-identical to builds for `sapphirerapids`, `cascadelake` and `icelake-server`, so they do not identify the target. The reference machine's 48 KiB 12-way L1 and 2 MiB L2 (second entry, Section 1.2) are consistent with a Sapphire Rapids core. The point the sentence makes (256-bit default, overridden by `-mprefer-vector-width=512`) holds for every one of these targets.
- `:315` FP64/FP32 claim (F2): no fetched source.
- Claims attributed to Hwu, Kirk and El Hajj (2022) were checked against standard CUDA behavior, not against the book's pages (no access to the text).
- Timings in Sections 2.3 to 2.5 could not be reproduced on the reference machine (above); reruns on this VM are reported in the technical log.

### Fact-check verdict

**pass.** Counts: 0 blocking, 0 should fix, 2 optional (F1, F2). Every reference exists and its bibliographic details are correct; each supports the sentences that cite it, with the exception handled under T4 (the cited book's classic model of reconvergence needs a qualification for current hardware).

## Technical review

Stage EOS 6.4, performed by a reviewer who did not write or revise the entry. T1 to T4 were referred by the copy editor and keep their IDs; T5 onward are new. Scratch files: `/tmp/claude-0/hpc/review/data-parallelism-vector-units-and-gpus/`.

**Machine note.** This review ran on a different KVM guest from the reference machine (Cascade Lake class, 2.8 GHz nominal, see Not verified above). Deterministic outputs (compiler reports, disassembly, sums, the offload model) were reproduced by building with `-march=sapphirerapids`, which yields binaries identical to the writer's. Timings were rerun under `flock /tmp/claude-0/hpc/bench.lock` with the writer's binaries; they describe this other VM and are used only to judge whether the qualitative claims are plausible, not to replace the article's numbers.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `:92`, Section 2.2 | accuracy | "16 `vmulpd` and 16 `vaddpd`" counts the 256-bit main loop (8 + 8) and the 128-bit remainder loop (8 + 8) together. |
| T2 | Should fix | `:112`, `:463` | accuracy | "1.4 to 1.5 times" excludes the run printed above it (256-bit: 1.56). |
| T3 | Should fix | `:26`, Section 1.1 | consistency | $W = 2n$ operations over $D = 1$ update mixes units of the first entry's work-span model. |
| T4 | Should fix | `:301`, Section 5.1 | accuracy | Reconvergence "after the branch" stated unqualified; not guaranteed on NVIDIA GPUs since Volta. |
| T5 | Should fix | `:177`, Section 2.5 | accuracy | Proposed reason for the >4 speedup ("separate partial sums also break the chain") is contradicted by the disassembly: one accumulator, one chain. |
| T6 | Optional | `:453`, Exercise 6 | accuracy | "Doubling $T$" from 32 gives 4096 threads per block; phrase the trade-off from $T = 16$ to $32$. |
| T7 | Optional | `:81`, Section 2.2 | accuracy | The trimmed report lines include the copies of both loops inlined into `main`, not only initialization loops. |
| T8 | Optional | `:139`, Section 2.4 | accuracy | Clamp loop: GCC emitted a compare into a mask register and a masked move, which the text calls "a blend". |
| T9 | Optional | `:357`, Section 6.1 | accuracy | The listing omits the header `print` of `offload.py` without an ellipsis, yet the output shows the header. |

### T1. Instruction count in the polynomial loop
- **Where:** `:92`, Section 2.2
- **Text:** "The disassembly confirms 16 `vmulpd` and 16 `vaddpd` instructions in the vectorized polynomial loop"
- **Problem:** `objdump -d kernels_vec` (writer's binary), function `poly`: 8 `vmulpd` and 8 `vaddpd` on `%ymm` registers (the 4-lane main loop, one vector per iteration, not unrolled) and 8 `vmulpd` and 8 `vaddpd` on `%xmm` registers (the 2-lane remainder loop that the 16-byte report line refers to); 0 `vfmadd`. Scalar build: 8 `vmulsd`, 8 `vaddsd`. The 512-bit build: 8 + 8 on `%zmm`. The total 16 is right, but "in the vectorized polynomial loop" reads as one loop with 16 of each, twice the 8 multiplications and 8 additions per element that Horner's rule needs.
- **Correction:** "The disassembly confirms 8 `vmulpd` and 8 `vaddpd` instructions on 256-bit `ymm` registers in the main polynomial loop, one per Horner step, 8 more of each on 128-bit `xmm` registers in the remainder loop, and their scalar forms `vmulsd` and `vaddsd` in the scalar build."

### T2. Range of the axpy gain
- **Where:** `:112`, Section 2.3; Summary `:463`
- **Text:** "Vectorization made the loop 1.4 to 1.5 times faster than the scalar build in repeated runs"; Summary "(axpy gained 1.4 to 1.5 times, and nothing more from 8 lanes)"
- **Problem:** Recomputed from the printed output: 0.112/0.072 = 1.556 (rates 22.3/14.4 = 1.549) for the 256-bit build, 0.112/0.077 = 1.455 for the 512-bit build. The run shown lies outside the stated range. The writer's earlier runs are not logged, so the lower bound cannot be rechecked; on this review's VM (different processor) the scalar axpy already reached 15–16 GB/s and vectorization gave no gain (0.100 vs 0.103 s; 0.106 vs 0.109 s), which confirms that the gain is machine-dependent and supports the hedged "suggests" reading.
- **Correction:** `:112`: "Vectorization made the loop 1.4 to 1.6 times faster than the scalar build in repeated runs (1.56 for the 256-bit build in the run shown)"; `:463`: "(axpy gained 1.4 to 1.6 times, and nothing more from 8 lanes)".

### T3. Units of work and span
- **Where:** `:26`, Section 1.1
- **Text:** "the work is $W = 2n$ operations and the span is $D = 1$ update, so the parallelism $W/D$ grows with $n$."
- **Problem:** The first entry (Section 4.1, `performance-models-and-scaling-laws.mdx:222`) defines $W$ and $D$ as counts of unit-time tasks in one dependence graph. With the task as one operation, each update is a multiplication followed by the addition that uses it, so $D = 2$ and $W/D = n$; with the task as one update, $W = n$ and $D = 1$. As written the ratio is $2n$ in mixed units. The conclusion is unchanged.
- **Correction:** "the work is $W = 2n$ operations and the span is $D = 2$ operations (a multiplication, then the addition that uses it), so the parallelism $W/D = n$ grows with $n$."

### T4. Reconvergence after divergence
- **Where:** `:301`, Section 5.1
- **Text:** "the hardware executes one path with the other threads masked off, then the other path, and the threads reconverge after the branch (Hwu, Kirk and El Hajj, 2022)."
- **Problem:** That is the classic (pre-Volta) SIMT model. NVIDIA's *CUDA C++ Programming Guide*, section "Independent Thread Scheduling": from compute capability 7.0 the GPU keeps a program counter per thread and "threads can now diverge and reconverge at sub-warp granularity"; code that assumes lockstep warps should use `__syncwarp()`. NVIDIA's Volta material states that programmers should not assume threads are reconverged after a conditional. Stated without qualification, the sentence describes every current NVIDIA GPU wrongly. The cost conclusion (a divergent warp spends the time of both paths) still holds.
- **Correction:** "When they disagree, the warp **diverges**: the hardware executes one path with the other threads masked off, then the other path (Hwu, Kirk and El Hajj, 2022). In the classic SIMT model the threads reconverge after the branch; NVIDIA GPUs since the Volta generation schedule each thread independently and do not guarantee reconvergence at that point. Either way the result is correct, but the warp takes as long as both paths together: the masking of Section 2.4, done by the hardware." (If the author wants a citation for the second sentence, NVIDIA, *CUDA C++ Programming Guide*, section "Independent Thread Scheduling", is the primary source; add it only after fetching the page, which this session could not do.)

### T5. Why the reordered sum gained more than 4 times
- **Where:** `:177`, Section 2.5
- **Text:** "The reordered sum ran 4.6 times faster (4.3 to 5.9 times in other runs), more than 4 lanes alone would give; one reading is that the separate partial sums also break the chain of dependent additions that limits the ordered loop."
- **Problem:** `objdump -d reduce_reassoc` (writer's binary), function `sum`: the main loop is `vaddpd (%rax),%ymm0,%ymm0; add $0x20,%rax; cmp; jne`, a single 256-bit accumulator. The four partial sums are the four lanes of one register, and every `vaddpd` waits for the previous one: the additions still form one dependent chain, now one vector addition per four elements instead of one scalar addition per element. Breaking that chain further would need several accumulator registers, which GCC did not use. The lanes therefore account for a factor of about 4; the reading offered describes the same factor twice. (On this review's VM the ratio was 0.490/0.115 = 4.26 and 0.488/0.111 = 4.40, close to 4.)
- **Correction:** "The reordered sum ran 4.6 times faster (4.3 to 5.9 times in other runs). The disassembly shows a single 256-bit accumulator (`vaddpd (%rax),%ymm0,%ymm0`), so the additions still form one dependent chain, now of one vector addition per four elements: the four lanes account for a factor of about 4, and this entry did not establish the source of the rest."

### T6. Exercise 6: doubling the tile from 32
- **Where:** `:453`, Exercise 6 answer
- **Text:** "Doubling $T$ doubles the intensity but quadruples the shared memory and the threads per block, which limits how many blocks an SM can hold"
- **Problem:** The exercise sets $T = 32$, where a block already has $32^2 = 1024$ threads; doubling gives 4096 threads and 64 KiB of tiles, which no longer describes a block an SM holds fewer of but a block the one-thread-per-element kernel cannot use. The trade-off is right for smaller $T$.
- **Correction:** "Going from $T = 16$ to $T = 32$ doubles the intensity (2 to 4 FLOP/byte) but quadruples the shared memory (4 KiB to 16 KiB) and the threads per block (256 to 1024), which limits how many blocks an SM can hold: the tile size trades reuse against occupancy."

### T7. What the trimmed report lines are
- **Where:** `:81`
- **Text:** "(line 31 is the polynomial loop, line 41 the axpy loop; the reports for the initialization loops are cut)"
- **Problem:** The full `-fopt-info-vec` output (reproduced with `-march=sapphirerapids`) also repeats `kernels.c:41:24` and `kernels.c:31:24 ... 32 byte vectors` for the copies of `axpy` and `poly` that GCC inlined into `main`; those are among the cut lines.
- **Correction:** "(line 31 is the polynomial loop, line 41 the axpy loop; the reports for the copies inlined into `main` and for the initialization loops are cut)".

### T8. Clamp loop instructions
- **Where:** `:139`
- **Text:** "became a comparison and a blend"
- **Problem:** Disassembly of `clamp`: `vcmpltpd %ymm0,%ymm1,%k1` then `vmovapd %ymm1,%ymm0{%k1}`, an AVX-512 masked move, not a `vblend` instruction. "Blend" is defensible as a description of the effect.
- **Correction (optional):** "became a comparison into a mask register and a masked move, which blends the two results".

### T9. Listing of `offload.py`
- **Where:** `:340–362`
- **Problem:** The program prints the header line (lines 19–20 of `offload.py`) before the loops; the listing drops it and the comments without an ellipsis, while the trailing `...` stands for the break-even search. The output shown is exactly what the full program prints.
- **Correction (optional):** add `...` as a line before `for n in (10**6, 10**8):`, or add the two header-print lines.

### Checks with no defect found
- Section 1: Flynn classes; GPU as MIMD of SIMD groups; task versus data parallelism.
- Section 2.1: lane counts 2/4/8 doubles and 4/8/16 floats; bound of 4 for 256-bit doubles.
- Section 2.2: GCC reports reproduced exactly (`kernels.c:31:24` and `41:24`, 32- and 16-byte); `sapphirerapids` preferred width 256 (generic `x86-64`: `none`); `-std=c11` gives no FMA (0 `vfmadd`), `-std=gnu11` 24, `-std=c11 -ffp-contract=fast` 24.
- Section 2.4: `blockers.c` report reproduced (versioning for aliasing at 6, `couldn't vectorize loop` at 11, 32-byte at 16, 22, 29, 34; the article's trimming drops the 16-byte and `no vectype` lines with "..."); the four `vaddsd` lines of `sum` match byte for byte, addresses `240`–`252`; AoS loop has exactly 3 vector loads (`vmovupd` and two memory-operand `vpermt2pd`), 2 `vpermt2pd`, 4 scalar stores (`vmovlpd`, `vmovhpd`, 2 `vmovsd`); prefix sum dependence; Exercise 2 answers (a) yes, (b) no, (c) yes, checked against the dependence distances; `restrict` semantics.
- Section 2.5: sums `517024.43791358318` (ordered) and `517024.43791358295` (reassociated) reproduced exactly by the writer's binaries on this VM; a Python model of 4 lane sums combined as $(s_0+s_1)+(s_2+s_3)$ gives `517024.43791358295`, the same value; `math.fsum` gives `517024.43791358318`; ulp $= 2^{-34} = 5.82 \times 10^{-11}$; errors +0 and −4 ulp; `-fassociative-math` alone is disabled with a warning; `#pragma omp simd reduction(+:s)` with `-fopenmp-simd` gives `vaddpd ... %ymm0`; worst-case bound statement (four chains of $n/4$ versus one of $n$) is the standard recursive-summation bound.
- Section 3: $10^8/256 = 390\,625$ blocks exactly; Little's law $10^{12} \times 5 \times 10^{-7} = 5 \times 10^5$ bytes, 62 500 loads; occupancy $65\,536/64 = 1024$ threads, 32 warps, 50%.
- Section 4: coalesced warp 256 bytes; stride 16: 32 segments, 4096 bytes, 6.25%; Exercise 3 (2, 4, 32 segments; 100%, 50%, 6.25%); direct matmul intensity $2n/(16n) = 1/8$; tiled $2T^3/(16T^2) = T/8$, 2 FLOP/byte at $T = 16$, 4 at $T = 32$; tiled kernel indexing checked (`A[row*n+k0+tx]`, `B[(k0+ty)*n+col]`, `As[ty][k]*Bs[k][tx]`); both barriers needed for the reasons given; Exercise 6 16 384 bytes.
- Section 5: Exercise 4 (8 and 24 threads per warp; 160 cycles; 120 or 40 cycles with no divergence); atomics, cross-block deadlock, failure modes.
- Section 6: `offload.py` rerun, output identical to the article in every digit; closed-form break-even $12/(25 \times 10^9 \times 1.9 \times 10^{-12}) = 252.63$; intensity at 253: $253/12 = 21.08$; $P_{\mathrm{cpu}}/B_{\mathrm{link}} = 20$; axpy ratio $0.24 \approx B_{\mathrm{link}}/B = 0.25$; transfer/kernel $0.96/0.024 = 40$; both processors compute-bound for matmul above $n = 60$ (CPU) and $n = 120$ (GPU); Exercise 5: CPU 5 s, (a) 0.54 s (9.3 times faster), (b) 40.5 s (8.1 times slower).
- Printed-figure arithmetic: $16 \times 2048 \times 10^5 / 0.421 = 7.78$ GFLOP/s; $28.40/7.79 = 3.65$ (text 3.6); $30.14/7.79 = 3.87$ (3.9); $22.3 \times 2/24 = 1.86$; AoS/SoA $0.129/0.056 = 2.30$; reduction $2048 \times 2 \times 10^5 / 0.237 = 1.73$ GFLOP/s, $0.237/0.051 = 4.65$ and $8.03/1.73 = 4.64$ (text 4.6).
- GPU listings are labeled as not compiled or run (`:20`, `:199`, `:202`, `:248`, `:268`, `:271`); every GPU and link figure is labeled assumed; no GPU result is presented as measured.

### Log of what was recomputed and run
- `gcc --version`: GCC 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1); `python3 --version`: 3.13.16. `lscpu`: different VM from the reference machine (see Not verified).
- Built `kernels.c`, `blockers.c` with `-std=c11 -O3 -march=sapphirerapids` (also `cascadelake`, `icelake-server`): disassembly identical to the writer's `kernels_vec` and `blockers.o`.
- `objdump -d` of `poly` (vec, scalar, 512), `sum` (ordered, reassoc), `shift_aos`, `clamp`, `sum_simd`: counts as given under T1, T5, T8 and the checks.
- Flag checks: `-fassociative-math` alone, with `-fno-signed-zeros -fno-trapping-math`, `-ffast-math`; `-std=c11` versus `-std=gnu11` versus `-ffp-contract=fast`; `-Q --help=target` for `x86-64`, `znver4`, `sapphirerapids`, `cascadelake`.
- Timings under `flock /tmp/claude-0/hpc/bench.lock`, writer's binaries, this VM (two rounds): poly scalar 0.700/0.707 s, 256-bit 0.181/0.193 s (3.7–3.9 times), 512-bit 0.140/0.156 s (4.5–5.0 times); axpy scalar 0.100/0.106 s, 256-bit 0.103/0.109 s, 512-bit 0.100/0.097 s (no gain; 15–16.6 GB/s); AoS 0.134/0.149 s, SoA 0.070/0.057 s (1.9–2.6 times); reduction ordered 0.490/0.488 s, reassociated 0.115/0.111 s (4.3–4.4 times), sums identical to the article. Qualitative claims of Sections 2.3–2.5 (compute-bound loop gains about the lane count; wider vectors do not help axpy; SoA beats AoS by about 2; reassociation gives about 4) hold on this VM except the axpy vectorization gain, which is absent here and is presented in the article as a property of the reference machine.
- `python3 offload.py`: output identical. `dumpdata | exact_sum.py`: output identical. Python recomputation of every number listed under "Checks with no defect found".

### Technical verdict

**fail** until T1 to T5 are applied or answered (0 blocking, 5 should fix, 4 optional). Each should-fix correction is ready to paste and changes no conclusion of the entry; after they are applied the stage passes without a further run.

## Resolution

Stage EOS step 7, by the author. The container now runs on a different processor, so no reference-machine timing was re-run and no measured number was changed except where a finding required it (T2, a range recomputed from the printed output). Final `npm run eos -- lint`: 0 errors, 0 warnings, 6 suggestions (the five acronym suggestions kept for the reasons in the copy edit; "Very" is inside the title of Flynn's 1966 paper).

| ID | Decision | How handled |
|---|---|---|
| D1–D6, C1–C6 | Accepted as applied by the editors | No further change; D5 and D6 resolved as F2 and F1 below. |
| T1 | Applied | Reviewer's text: 8 `vmulpd` and 8 `vaddpd` on `ymm` in the main loop, one per Horner step, 8 more of each on `xmm` in the remainder loop. Matches my own disassembly count (16 in the whole function). |
| T2 | Applied | "1.4 to 1.6 times faster ... (1.56 for the 256-bit build in the run shown)" in Section 2.3; Summary row changed to "1.4 to 1.6 times". The sentence was split after the parenthesis (lint sentence-length). |
| T3 | Applied | $D = 2$ operations (a multiplication, then the addition that uses it), $W/D = n$, consistent with the first entry's units. |
| T4 | Applied | Reviewer's text: classic SIMT reconvergence after the branch; NVIDIA GPUs since Volta schedule threads independently and do not guarantee reconvergence there. No citation added for the Volta sentence, since the CUDA guide page was not fetched. |
| T5 | Applied | Correct: the reassociated loop has one `ymm0` accumulator, so the earlier reading counted the lane factor twice. Reviewer's text used: the lanes account for about 4, the rest is not explained. |
| T6 | Applied | Exercise 6 answer now states the trade-off from $T = 16$ to $T = 32$ (2 to 4 FLOP/byte, 4 to 16 KiB, 256 to 1024 threads). |
| T7 | Applied | The trim note now mentions the copies inlined into `main`. |
| T8 | Applied | "a comparison into a mask register and a masked move, which blends the two results". |
| T9 | Applied | Added a `...` line before the first loop of the `offload.py` listing, marking the omitted header print. |
| F1 | Applied | "Flynn (1966) classified ... and developed the classification in a later paper (Flynn, 1972)"; reference M. J. Flynn, "Very high-speed computing systems," *Proceedings of the IEEE*, vol. 54, no. 12, pp. 1901–1909, 1966, added before the 1972 entry (details as verified by the fact-checker). |
| F2 | No change | As the fact-checker recommends: the sentence stays a qualified general statement with no figure and no citation to an unchecked page. |

## QA

Stage EOS 10, by an independent QA editor who did not write, revise or review the entry in an earlier stage. Review input: `/tmp/claude-0/hpc/qa/data-parallelism-vector-units-and-gpus.json`.

**Decision: revise. Not recorded.** Two should-fix defects are open (Q1, Q2). Provisional scores: purpose 4, structure 3, accuracy 3, evidence 3, language 2, consistency 3, publishing 4, total 22/28. These scores fail the article thresholds (24 total, 3 per dimension). Critical conditions C1-C8: none holds. Q2 is a misleading code comment, not a wrong result. C9: the series review is resolved but not yet stamped.

Confirmed resolved in the text: D1-D3, C1-C3, T1-T5 (and T6-T9, F1), series F1, F2, F3, F11, F15. QA recomputed `offload.py` (the output matches every digit), the break-even point 252.6, the 4-ulp difference between the two sums, 13.4 × 32/24 = 17.9 GB/s, 0.112/0.072 = 1.56 and 0.237/0.051 = 4.6. The cross-references to entry 1 (Sections 4, 5, 5.4, 6, 6.3), entry 2 (Sections 4, 5, 5.2, 6.3, 6.4), entry 3 (Sections 3 and the whole entry), entry 5, the two insights and `solving-large-linear-systems` Section 4 all exist and say what is claimed. Lint gives 0 errors, 0 warnings and 8 suggestions. Two of the suggestions are new since the Resolution: `paragraph-length` and `sentence-length` at `:112`. `eos validate-site dist` reports no issues.

### Q1. Should fix (structure, language). The Section 2.3 paragraph is overloaded and uses an unintroduced figure
- **Where:** `src/content/blog/data-parallelism-vector-units-and-gpus.mdx:112`, Section 2.3
- **Text:** "... Axpy reads the array it writes, so it moves no write-allocate traffic, and, as Section 5.2 of the second entry found, how much one core sustains depends on the mix of reads and writes; the one-core ridge point of about 6.8 FLOP/byte is therefore a rough figure. Going from 4 lanes to 8, however, ..."
- **Problem:** The series F2 fix made this a 232-word paragraph (lint `paragraph-length`) with a 50-word sentence (lint `sentence-length`). The paragraph covers three topics: the intensity and roofline, the bandwidth reconciliation, and the lane-width result. "The one-core ridge point of about 6.8 FLOP/byte" appears nowhere else in this entry, has no link, and is not introduced; it comes from Section 1.1 of the second entry. "Section 5.2 of the second entry" is also unlinked. The "however" sentence now follows the reconciliation instead of the vectorization gain it contrasts with.
- **Correction:** Split the paragraph in two places and replace the middle part. Keep the first paragraph as is, up to and including "(1.56 for the 256-bit build in the run shown)." Then add:

  "This suggests that the scalar loop did not keep enough memory requests in flight. The vectorized loop's 22.3 GB/s is well above the 13.4 GB/s that one core sustained on the triad of [Section 6.3 of the second entry](/blog/memory-hierarchy-and-locality#63-measuring-sustainable-bandwidth), 17.9 GB/s counting the write-allocate read. Axpy reads the array it writes, so it moves no write-allocate traffic. As [Section 5.2 of the second entry](/blog/memory-hierarchy-and-locality#52-array-of-structures-and-structure-of-arrays) found, how much one core sustains depends on the mix of reads and writes, so the one-core ridge point of about 6.8 FLOP/byte that [Section 1.1 of the second entry](/blog/memory-hierarchy-and-locality#11-the-processor-memory-gap) derived from the triad is only a rough figure."

  Start a new paragraph at "Going from 4 lanes to 8, however, changed nothing beyond the noise, ..." and leave its text unchanged to the end. Both fragments exist in `dist/blog/memory-hierarchy-and-locality.html`.

### Q2. Should fix (accuracy). The listing comment contradicts the byte count
- **Where:** `src/content/blog/data-parallelism-vector-units-and-gpus.mdx:358`, Section 6.1 listing
- **Text:** `for n in (10**6, 10**8):         # axpy: 2n FLOP, 24n bytes each way`
- **Problem:** The program passes `Q_link = 24 * n` in total, and `:376` says "x and y are sent and y is returned, 24 bytes per element". "Each way" means 24n in each direction, 48n in all. The program `offload.py` does not have this comment: its comment reads "memory traffic 24n bytes; send x and y, return y". The model's output is unaffected.
- **Correction:** `for n in (10**6, 10**8):         # axpy: 2n FLOP, 24n bytes in memory and over the link`

### Q3. Optional (language, consistency)
- `:18`: "with 4 cores of an Intel Xeon processor reported at 2.1 GHz (Section 5.4 of the first entry infers that the cores ran faster) that supports the 512-bit vector extensions". The relative clause after the parenthesis is ambiguous, and standards 5.5 call for words for small counts that are not measurements, as in the other entries. Suggested text: "with four cores of an Intel Xeon processor that supports the 512-bit vector extensions, reported at 2.1 GHz (Section 5.4 of the first entry infers that the cores ran faster)".

After Q1 and Q2 are applied, the entry needs only a re-lint, a rebuild and a fresh QA record. No technical re-review is needed: the changes add no new claim.

Not verified: the reference-machine timings and the ranges from repeated runs that were not logged (the reference VM is no longer available; the text presents them as measurements of that machine); the Volta independent-scheduling statement, which is verified by search but not cited; the FP64 statement, which is qualified and uncited; and the claims attributed to Hwu, Kirk and El Hajj, which were checked against standard CUDA behavior, not against the book's pages.

## Resolution of the QA findings

- Q1 (should fix): applied with the QA editor's text. The F2 sentence is now its own paragraph, links Sections 5.2 and 1.1 of the second entry, and says where the 6.8 FLOP/byte ridge point comes from. "Going from 4 lanes to 8" starts a new paragraph.
- Q2 (should fix): the listing comment now reads "24n bytes in memory and over the link".
- Q3 (optional): applied ("four cores of an Intel Xeon processor that supports the 512-bit vector extensions, reported at 2.1 GHz ...").

## QA (second pass)

The independent QA editor ran this pass after the author applied Q1 to Q3 (see "Resolution of the QA findings" above). The record is `editorial/records/article/data-parallelism-vector-units-and-gpus.json`.

**Decision: publish, total 26/28.** None of the critical conditions C1-C8 holds. C9: the series review is resolved but not yet stamped.

Checked:
- **Q1.** `:112` now ends after the 1.56 parenthesis. `:114` carries the reconciliation in the QA wording, with working links to the second entry's Sections 6.3, 5.2 and 1.1. `:116` starts "Going from 4 lanes to 8, however,", which now follows the vectorization result it contrasts with.
- **Q2.** `:362` reads `# axpy: 2n FLOP, 24n bytes in memory and over the link`.
- **Q3.** `:18` is applied.
- **Lint.** 0 errors, 0 warnings and 7 suggestions. The paragraph-length suggestion is gone. The remaining sentence-length suggestion at `:114` (50 words) is one connected inference and is kept.
- **Site checks.** `eos validate-site dist` reports no issues. `check:links` reports that all internal links resolve. `dist/` was rebuilt after the edit.

| Dimension | Score | Justification |
|---|---|---|
| purpose | 4 | Purpose, prior results and conventions are explicit. |
| structure | 4 | Section 2.3 now runs intensity, then gain, then reconciliation, then width. |
| accuracy | 4 | Every finding is resolved; the listing comment now matches the program and the text. |
| evidence | 3 | The Volta and FP64 statements are uncited (verified by search, or qualified). |
| language | 4 | House style throughout; the remaining suggestions are justified. |
| consistency | 3 | In-text citation style differs between entries (series F18, deferred). |
| publishing | 4 | Lint, build, links and validate-site are clean. |

Not verified: unchanged from the first pass.
