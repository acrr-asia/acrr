# Editorial review: Distributed Memory and Message Passing

- Path: `src/content/blog/distributed-memory-and-message-passing.mdx` · Route: `/blog/distributed-memory-and-message-passing` · Type: article (series entry) · Series `parallel-and-high-performance-computing`, entry 5 of 5 (last)
- Stages in this report: developmental (EOS 6.1) and copy edit (EOS 6.2), done by an editor who did not write the entry. Later sections (fact-check, technical review, resolution, QA) are added by their reviewers.
- Read for this review: the series overview, the article in full, the headings and cited sections of the four earlier entries, `finite-differences-for-heat-and-waves` (Sections 2.1, 2.2) and `solving-large-linear-systems` (Section 4.2). The reproduction script and outputs in the author's work directory (`run.sh`, `model.out`) were consulted as evidence only.

## Developmental review

The entry does its job well. The opening links what it builds on, says what it covers and states versions, machine and units. Each numbered section opens with its concept (distributed memory before MPI calls, blocking semantics before eager and rendezvous, the affine model before the ping-pong, collective semantics before their algorithms, decomposition before ghost cells), the worked examples are run with real output, limits are stated in 3.4, 5.4 and 6.4, and the exercises have answers. The `##` headings are unchanged; no `###` heading was renamed or renumbered, so no fragment changed (the only inbound fragment link, `#6-predicting-scaling` from the first entry, is intact).

Numbers spot-checked while reading (not a substitute for the technical stage): the collective table of 4.3 (rows p = 8), the 0.74 µs eager estimate of 4.4, the speedups and medians of 5.3, the relative difference 2.6e-13, the machine model of 6.1, the p = 4096 block rows of 6.2 and 6.3, and Exercises 1, 3 and 4. All agree except the item in D5.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Optional | `:16`, opening | structure | Second opening paragraph is a sentence-by-sentence table of contents ("It shows ... It measures ... It ends by ..."). Applied. |
| D2 | Should fix | `:615–617`, Section 8 closing | purpose | The closing restates every entry, overstates ("its last model draws on all of the earlier ones") and ends on a claim that Section 6.1 and 6.4 contradict ("predicts which design achieves that before a line of the program is tuned"). Applied. |
| D3 | Should fix | `:165`, Section 2.4 | evidence | "Both safe versions worked at every size tried, up to 8,000,000 bytes": the quoted run and `run.sh` show one size per safe version (506 doubles with `sendrecv`, 1,000,000 with `isend`). Deferred to the technical reviewer. |
| D4 | Should fix | `:36`, Section 1.3 | evidence | "a Version 5.0 followed in 2025" is an uncited factual claim, not in the reference list. Deferred to the fact-checker. |
| D5 | Should fix | `:549`, Section 6.3 | accuracy | The Gustafson check "0.0297 + 0.9703 × 4096 = 3974.4 ... against 3974.2 ... They differ only by f_s": the 0.2 difference shown comes from rounding f_s, not from f_s (0.03). Deferred to the technical reviewer. |
| D6 | Optional | `:429–458`, Section 5.3 | structure | "Checking against a serial run" also carries the speedups and the subnormal-number episode; the heading undersells the subsection. Not applied (heading kept to avoid changing a fragment; the content is in the right place). |

### D1. Opening reads as a list of contents
- **Where:** `:16`, opening paragraphs
- **Text:** "It shows blocking and nonblocking point-to-point messages ... It measures and models the cost of a message, derives the cost of collective operations, and distributes the grid ... It ends by predicting the scaling of that stencil on an assumed cluster."
- **Problem:** Standards 6.1 and the agent brief ask the introduction to set up what follows without a prose table of contents; each sentence names one section. It also carries a serial comma (C1).
- **Correction (applied):** the paragraph now states the line of argument (message-passing model, then a cost model built on it, then its use for collectives, the distributed stencil and scaling) and ties the end to the last series objective.

### D2. Closing restates and overclaims
- **Where:** `:615–617`, Section 8, the two paragraphs after the table
- **Text:** "This entry completes the series, and its last model draws on all of the earlier ones." ... "a simple, stated model of the cost of moving data predicts which design achieves that before a line of the program is tuned."
- **Problem:** Standards 6.2 item 6 asks the last entry to lead back to the series objectives; the paragraph listed the five objectives in paraphrase and then recapped each entry, without saying where this entry meets its own objective. The model of Section 6 does not draw on the fourth entry's GPU material. The final claim conflicts with `:499` ("Such a model gives the shape of a scaling curve, not a run time to a few percent") and `:560` ("its predictions checked against a few real runs").
- **Correction (applied):** the first paragraph now names where the fifth objective is met (Sections 3, 4 and 6) and links each earlier entry to what this entry actually uses from it (the speedup laws, $t_c$ and locality, the hybrid model of Section 1.4, the data-movement comparison of the offload model). The final sentence now reads "A simple, stated model of the cost of moving data shows which design can achieve that before the program is tuned, and measurements on the target machine then confirm it." No technical claim was added: every link back restates something the earlier entries or this entry's sections already establish.

### D3. "Every size tried" is not shown
- **Where:** `:165`, Section 2.4
- **Text:** "Both safe versions worked at every size tried, up to 8,000,000 bytes."
- **Problem:** The quoted output (`:154–159`) and the reproduction script run `sendrecv` only at 506 doubles and `isend` only at 1,000,000 doubles. A sweep of sizes is not in evidence.
- **Correction (for the technical reviewer):** either run both safe modes at several sizes (for example 505, 506, 10^4, 10^6) and keep the sentence, or narrow it to what is shown: "Both safe versions completed at the sizes shown, including 8,000,000 bytes for the nonblocking one." Text left unchanged.

### D4. MPI 5.0 date uncited
- **Where:** `:36`, Section 1.3
- **Text:** "the version cited here is Version 4.1 (Message Passing Interface Forum, 2023), and a Version 5.0 followed in 2025."
- **Problem:** A dated factual claim with no reference (standards 7.2). The reference list cites only Version 4.1.
- **Correction (for the fact-checker):** verify against the MPI Forum's published documents; if confirmed, add the Version 5.0 document to the references or attribute it; otherwise remove the clause. Text left unchanged.

### D5. Gustafson check: shown difference is a rounding artifact
- **Where:** `:549`, Section 6.3
- **Text:** "$f_s + (1 - f_s)\,p$ gives $0.0297 + 0.9703 \times 4096 = 3974.4$ for blocks at $p = 4096$, against 3974.2 from the model. They differ only by $f_s$"
- **Problem:** Recomputed in Python 3 from the article's own model (blocks, $p = 4096$, $t_c = 1.149$ ns, $\alpha = 2$ µs, $\beta = 0.1$ ns/byte): $T_p = 1.18421$ ms, $f_s = 0.029733$, model $S_s = 3974.215$, Gustafson $f_s + (1-f_s)p = 3974.245$. The true difference is $f_s \approx 0.03$, so both round to 3974.2. The 3974.4 in the text comes from using the rounded $f_s = 0.0297$ ($0.9703 \times 4096 = 3974.35$), which makes the displayed difference 0.2, about seven times $f_s$, so the numbers shown contradict the sentence that explains them.
- **Correction (for the technical reviewer):** use the unrounded value, for example "gives $0.02973 + 0.97027 \times 4096 \approx 3974.25$ ... against 3974.22 from the model. They differ by exactly $f_s$ ...". Text left unchanged.

### D6. Section 5.3 heading
- **Where:** `:429`, "5.3 Checking against a serial run"
- **Problem:** The subsection also reports speedups and the subnormal-number imbalance. Optional; a rename such as "Checking and timing against a serial run" would change the fragment. No inbound link targets it today (grep of `src/content/blog/*.mdx`), so the author may rename it if desired.

### Changes made (developmental)
- Rewrote the second opening paragraph (D1).
- Rewrote the two closing paragraphs of Section 8 (D2).

**Developmental verdict: pass.** Blocking 0, should fix 4 (D2 applied; D3, D4, D5 deferred to the technical and fact-check stages, which own those dimensions), optional 2 (D1 applied, D6 not applied). No should-fix finding within this stage's remit remains open.

## Copy edit

`npm run eos -- lint` before: 0 errors, 0 warnings, 16 suggestions. `npm run eos -- fix --rules spelling-variant,terminology`: 0 fixes applied. Manual checks: no em dashes, contractions, "we", "simply", "obviously", "clearly" or "of course"; headings are in sentence case; abbreviations (MPI, GCC, KVM, SPMD, RDMA, GB/s) expanded at first use; American spelling throughout. After: 0 errors, 0 warnings, 7 suggestions (listed under C6).

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| C1 | Should fix | `:16`; `:615` (old text) | language | Serial commas ("derives the cost of collective operations, and distributes"; "judging when an accelerator pays, and predicting"). Fixed. |
| C2 | Should fix | `:499` (81 words), `:615` (82 words, old text) | language | Two sentences far over the 45-word guideline, each joining three or more separate points. Fixed. |
| C3 | Optional | `:161`, `:253`, `:259`, `:376`, `:456`, `:475` | language | Sentences of 48–51 words flagged by `sentence-length`. Five split; `:259` kept (C6). |
| C4 | Optional | `:456`, `:458`, `:549` | language | Imprecise or throat-clearing wording: "The cause was arithmetic"; "The general lesson is that"; "Weak scaling is far kinder". Fixed. |
| C5 | Should fix | `:612`, Summary table | accuracy | "global sums to a small multiple of rounding error" understates the observed discrepancy. Deferred to the technical reviewer. |
| C6 | Optional | lint suggestions kept | language | Seven suggestions kept, with reasons below. |

### C1. Serial commas
- **Where:** `:16`, `:615`
- **Problem:** Standards 5.1: no serial comma.
- **Correction (applied):** both sentences were rewritten (with D1 and D2) without the serial comma.

### C2. Overlong sentences
- **Where:** `:499`, `:615`
- **Text:** "The four processes share one machine's memory system and are disturbed by its other tenants, the processes do not arrive at each exchange at the same moment, and $t_c$ is not one number: in a separately timed four-process run, ..."
- **Correction (applied):** split into "The four processes share one machine's memory system and are disturbed by its other tenants, and they do not arrive at each exchange at the same moment. Nor is $t_c$ one number. In a separately timed four-process run, ... against the predicted 0.575 s. The processes compete for the shared memory system and a smaller subdomain uses the caches differently (...)." The closing sentence at `:615` was replaced in D2.

### C3. Other long sentences
- **Correction (applied):** `:161` deadlock sentence split before the definition; `:253` split at the semicolon and the half-performance check turned into a full sentence ("The half-performance size can be checked against the large-message fit. A 25,620-byte message achieves ..."); `:376` amplification-factor parenthesis split into two sentences; `:456` "The cause lay in the arithmetic itself." as its own sentence; `:475` the two practical costs of blocks given as separate sentences.

### C4. Wording
- **Correction (applied):** "The cause was arithmetic:" → "The cause lay in the arithmetic itself."; "The general lesson is that every process waits ..." → "Every process waits ..."; "Weak scaling is far kinder." → "Weak scaling is far more favorable." LogP sentence: "..., which the affine model folds into $\alpha$." → "... The affine model folds both into $\alpha$." (the relative clause was ambiguous between the overhead and the gap).

### C5. Summary: "a small multiple of rounding error"
- **Where:** `:612`, Summary row "How is it checked?"
- **Text:** "The grid must match a serial run exactly; global sums to a small multiple of rounding error."
- **Problem:** Section 5.3 reports a relative difference of $2.6 \times 10^{-13}$ in the change norm, about 1,200 times the double-precision unit roundoff ($1.1 \times 10^{-16}$). That is well within the error bound of a reordered sum of $10^6$ terms, but "a small multiple" misdescribes it.
- **Correction (for the technical reviewer):** for example "global sums agree only to within the rounding error of a reordered sum ($2.6 \times 10^{-13}$ relative here)." Text left unchanged.

### C6. Lint suggestions kept
- `:18` `GNU` (acronym-expansion): the project's own name, whose expansion is recursive; "GNU Compiler Collection (GCC)" is already expanded.
- `:36` `MPICH` (acronym-expansion): product name, not an abbreviation the reader needs expanded.
- `:259` sentence of 48 words: a single list of the four LogP parameters; splitting it would separate the list from its introduction.
- `:621` `ACM`, `:622` `MIT`, `:623` `MPP`, `CS`: inside reference entries (venue, publisher and a cited title), which keep their original form.
- Program output keeps "Karp-Flatt" with a hyphen and "us" for microseconds: quoted output is not edited.

### Changes made (copy)
- Language: serial commas removed (2), long sentences split (7), four imprecise phrasings replaced, one ambiguous relative clause resolved.
- No technical claim, number, equation, code block, quoted output, unit, citation or link target changed. Two links in the closing now wrap "third entry" and "fourth entry" instead of "The third entry" (same targets).

**Copy-edit verdict: pass.** Blocking 0, should fix 3 (C1, C2 fixed; C5 deferred to the technical reviewer), optional 3 (C3, C4 applied; C6 kept with reasons). Final `npm run eos -- lint`: 0 errors, 0 warnings, 7 suggestions.

## Fact-check

Stage EOS 6.3, by a reviewer who did not write or revise the entry. Sources were found with WebSearch (catalogue, DBLP, publisher and MPI Forum listings). WebFetch and direct downloads failed in this environment (DNS failure and proxy 403), so no full text was read; claims about what a paper's body says rest on the abstract and listings found, or are listed under Not verified. Version claims about the installed software were checked with `ompi_info`, `mpicc --version` and verbose `mpirun` runs.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| F1 | Should fix | `:36`, Section 1.3 | evidence | Resolves D4. "a Version 5.0 followed in 2025" is correct (approved by the MPI Forum on June 5, 2025) but uncited; add the reference. |
| F2 | Should fix | `:626`, References | evidence | Patarasuk and Yuan (2009): issue number missing; it is vol. 69, no. 2. |
| F3 | Optional | `:36`, Section 1.3 | accuracy | "all of them are unchanged in Version 4.1": semantics are unchanged, but the C bindings of the send-side functions gained `const` in MPI 3.0. |
| F4 | Optional | `:273`, Section 4.1 | evidence | "the costs below follow that analysis": the ring allreduce is the algorithm of Patarasuk and Yuan, not one of the MPICH algorithms analyzed by Thakur et al. |

### F1. MPI 5.0 date (resolves D4)
- **Where:** `:36`, Section 1.3 "The MPI standard"
- **Text:** "the version cited here is Version 4.1 (Message Passing Interface Forum, 2023), and a Version 5.0 followed in 2025."
- **Problem:** The claim is true but has no reference (standards 7.2). Evidence: the MPI Forum documents page and the MPI 5.0 report give the approval date June 5, 2025 (mpi-forum.org/docs; "MPI: A Message-Passing Interface Standard Version 5.0", mpi-forum.org/docs/mpi-5.0/mpi50-report/; mpi-forum mailing list post "MPI 5.0 Voted In", lists.mpi-forum.org/pipermail/mpi-forum/2025-June/007905.html). The same sources give Version 4.1 as November 2, 2023, which confirms the 4.1 reference.
- **Correction:** Text: "..., and Version 5.0 followed in 2025 (Message Passing Interface Forum, 2025)." Add to the References, after the 4.1 entry: "- Message Passing Interface Forum, *MPI: A Message-Passing Interface Standard*, Version 5.0, 2025."

### F2. Patarasuk and Yuan: issue number
- **Where:** `:626`, References
- **Text:** "*Journal of Parallel and Distributed Computing*, vol. 69, pp. 117–124, 2009."
- **Problem:** Standards 7.3 require the issue when it exists. Library and publisher listings give vol. 69, no. 2, pp. 117–124, 2009 (authors P. Patarasuk and X. Yuan, Florida State University; author-hosted copy cs.fsu.edu/~xyuan/paper/09jpdc.pdf listed).
- **Correction:** "P. Patarasuk and X. Yuan, "Bandwidth optimal all-reduce algorithms for clusters of workstations," *Journal of Parallel and Distributed Computing*, vol. 69, no. 2, pp. 117–124, 2009."

### F3. "unchanged in Version 4.1"
- **Where:** `:36`
- **Text:** "and all of them are unchanged in Version 4.1."
- **Problem:** MPI 3.0 added `const` to the input buffer arguments of the C bindings (for example `MPI_Send(const void *buf, ...)`), so the prototypes are not literally unchanged since MPI 1; their semantics are. (From the MPI 3.0 change log; full text not fetched here, hence optional.)
- **Correction:** "and their semantics are unchanged in Version 4.1."

### F4. Attribution of the ring allreduce cost
- **Where:** `:273`, `:299`
- **Text:** "Thakur, Rabenseifner and Gropp (2005) describe the algorithms used in the MPICH implementation and their costs in the latency-bandwidth model; the costs below follow that analysis"
- **Problem:** Thakur et al. cover binomial broadcast, recursive doubling and Rabenseifner's reduce-scatter plus allgather for allreduce; the ring allreduce of 4.2 is the algorithm whose bandwidth optimality Patarasuk and Yuan prove. The sentence is not wrong for the other formulas, but it over-attributes. (Full text of Thakur et al. not fetched; abstract and listings confirm its scope.)
- **Correction:** "...the costs below follow that analysis (the ring allreduce follows Patarasuk and Yuan, 2009) but leave out ..."

### Verification table

| Claim | Location | Status | Source |
|---|---|---|---|
| MPI Version 4.1, 2023 | `:36`, `:625` | Verified | MPI Forum, MPI 4.1 report (November 2, 2023) |
| Version 5.0 followed in 2025 | `:36` | Verified, uncited (F1) | MPI Forum documents page and MPI 5.0 report (June 5, 2025); mpi-forum list post 2025-06 |
| Open MPI 4.1.6 implements MPI 3.1 | `:36` | Verified | `ompi_info`: "MPI API: 3.1.0", Open MPI 4.1.6 |
| MPI_Init_thread added in MPI 2.0; other functions used in MPI 1 | `:36` | Verified (standard history) | MPI-2.0 introduced the thread levels and `MPI_Init_thread`; send/recv/sendrecv/isend/irecv/wait/collectives/`MPI_Type_vector`/`MPI_Cart_create`/`MPI_PROC_NULL` are MPI-1 |
| "unchanged in Version 4.1" | `:36` | Corrected (F3, optional) | MPI 3.0 change log (`const` in C bindings) |
| GCC 13.3, Open MPI 4.1.6, Python 3.13, NumPy 2.5 | `:18` | Verified | `mpicc --version` 13.3.0, `mpirun --version` 4.1.6, Python 3.13.16, NumPy 2.5.3 |
| Non-overtaking order of messages | `:75` | Verified | MPI 4.1, point-to-point chapter (semantics of point-to-point communication, order) |
| Standard-mode send may buffer or wait; "unsafe" programs | `:77` | Verified | MPI 4.1, point-to-point chapter (communication modes; "unsafe") |
| `MPI_THREAD_FUNNELED`: only the main thread calls MPI | `:69` | Verified | MPI 4.1, thread support section |
| `MPI_PROC_NULL` send/receive completes at once, no effect | `:394` | Verified | MPI 4.1, null processes section |
| ob1 and vader selected; `btl_vader_eager_limit` 4,096 bytes including header | `:95` | Verified | `ompi_info --param btl vader --level 9`: "Maximum size (in bytes, including header) of "short" messages", current value 4096; `--mca pml_base_verbose 10` shows ob1 selected, vader initialized |
| Hockney (1994), affine model, r_inf and n_1/2 | `:171`, `:177`, `:623` | Verified (bibliographic) | DBLP: R. W. Hockney, *Parallel Computing* 20(3): 389–398, 1994 |
| LogP: L, o, g, P | `:259`, `:621` | Verified (bibliographic and parameters) | Illinois Experts and Berkeley listings: Proc. 4th ACM SIGPLAN PPoPP, pp. 1–12, May 1993, eight authors as listed; parameters P, g (bandwidth), L, o |
| Karp and Flatt (1990), experimentally determined serial fraction | `:503`, `:624` | Verified | CACM 33(5): 539–543, May 1990 (ACM listing, library record) |
| Gropp, Lusk and Skjellum, *Using MPI*, 3rd ed., MIT Press, 2014 | `:36`, `:622` | Verified | MIT Press listing, ISBN 9780262527392, November 2014 |
| Thakur, Rabenseifner and Gropp (2005), MPICH collectives | `:273`, `:627` | Verified (bibliographic) | MPICH publications page and Crossref: IJHPCA 19(1): 49–66, 2005 |
| Patarasuk and Yuan (2009): lower bound met by ring allreduce | `:299`, `:626` | Verified; issue missing (F2) | JPDC 69(2): 117–124, 2009; abstract: tight lower bound on data communicated, ring algorithm bandwidth optimal |
| Rabenseifner's algorithm: 2 log2 p latency terms, same bandwidth term | `:299` | Verified (standard result) | Thakur et al. 2005 (scope per abstract); formula checked by derivation in the technical review |
| Smallest normal double 2.2e-308 | `:456` | Verified | `numpy.finfo(float).tiny` = 2.2250738585072014e-308 |
| Subnormal operands slow on this processor | `:456` | Verified by measurement | Per-rank timing, technical log (ranks with subnormals 2.0–2.5 times slower) |
| Reference machine: KVM, 4 Xeon cores at 2.1 GHz, 2 MiB L2 per core, 16 GiB | `:18` | Consistent with the series; not re-observed | The writer's host matches the earlier entries (2.1 GHz in their outputs); this reviewer's session ran on a different KVM host (Xeon reported at 2.8 GHz, 1 MiB L2 per core, 15 GiB), see Not verified |

### Not verified
- Exact cost formulas as printed in Thakur et al. (2005) and the wording of the lower bound in Patarasuk and Yuan (2009): full text could not be fetched (DNS failure, proxy 403). Existence and bibliographic details are confirmed; the formulas themselves are verified by derivation in the technical review.
- Definition of the LogP gap $g$ as the minimum interval between consecutive messages at one processor: the listings give "g: communication bandwidth"; the article's definition is the standard one but the paper's text was not read.
- The reference machine's 2.1 GHz and 2 MiB L2 per core: this session ran on another host, so the hardware statement and the writer's timings could not be re-observed on the same machine.
- "Repeated runs differed by up to about 15% for the largest messages" (`:234`): a statement about the writer's session; no record of the repeated runs is kept (see T8).

**Fact-check verdict: fail until F1 and F2 are applied** (blocking 0, should fix 2, optional 2). Every reference exists and its details are right apart from the missing issue number; no reference was found that fails to support its claim.

## Technical review

Stage EOS 6.4, by the same independent reviewer. Every program was copied from the writer's directory to `/tmp/claude-0/hpc/review/distributed-memory-and-message-passing/`, rebuilt with `mpicc -O2 -Wall` (Open MPI 4.1.6, GCC 13.3.0) and run with `mpirun --allow-run-as-root --oversubscribe`; timed runs held `flock /tmp/claude-0/hpc/bench.lock`. Every C and Python block in the article was extracted and matched line by line against `hello.c`, `exchange.c`, `pingpong.c`, `allreduce.c`, `jacobi_mpi.c`, `fit.py` and `collectives.py`: no line differs. Every line of every quoted output block is present in the writer's saved outputs (`pingpong.quoted.out`, `fit.out`, `allreduce.out`, `collectives.out`, `jacobi.out`, `model.out`), except the `hello` and `exchange` outputs, which were not saved and which this review reproduced. Note: this session ran on a different KVM host from the writer's (Xeon reported at 2.8 GHz, 1 MiB L2 per core), so timings are compared for magnitude and shape only.

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| T1 | Should fix | `:165`, Section 2.4 | evidence | Resolves D3. "every size tried, up to 8,000,000 bytes" was not in evidence; rerun at 7 sizes confirms it. State the sizes and add the sweep to `run.sh`. |
| T2 | Should fix | `:549`, Section 6.3 | accuracy | Resolves D5. 3974.4 comes from the rounded $f_s$; the true Gustafson value is 3974.245 against the model's 3974.215, a difference of exactly $f_s$. |
| T3 | Should fix | `:612`, Summary | accuracy | Resolves C5. "a small multiple of rounding error": the change norm differs by 4,700 unit roundoffs in the sum of squares; within the reordered-sum bound, not a small multiple. |
| T4 | Should fix | `:454`, Section 5.3 | evidence | "in an earlier session an instrumented copy of the blocking version also ran in 0.65 s": the only recorded instrumented run took 0.861 s; 0.650 s was the largest per-rank compute time in it. |
| T5 | Should fix | `:259`, Section 3.4 | accuracy | "The affine model folds both into $\alpha$": the overhead $o$ is part of $\alpha$, but the gap $g$ has no counterpart in a one-message model. |
| T6 | Should fix | `:456`, Section 5.3 | accuracy | Subnormal band "up to about 21,000 points (2% of the grid)" was read from samples every 200 sweeps; the maximum over all sweeps is 22,952 (2.3%). |
| T7 | Optional | `:362`, Section 4.4 | accuracy | 9.756e-9 differs from the true tail (9.99999994e-9) by 2.4e-10, the rounding error of the four sequential partial sums; the paragraph attributes order dependence only to the combination of partial sums. |
| T8 | Optional | `:234`, `:253`, `:608` | evidence | The eager-range fit is the least stable result: three reruns gave 1/β = 1.57–4.78 GB/s and measured/model up to 2.22; the "within a factor of 1.22" and "about 0.37 µs and 2.1 GB/s" describe one run. |

### T1. Safe exchanges at every size tried (resolves D3)
- **Where:** `:165`, Section 2.4 "Safe exchanges"
- **Text:** "Both safe versions worked at every size tried, up to 8,000,000 bytes."
- **Problem:** The quoted run and `run.sh` show `sendrecv` only at 506 doubles and `isend` only at 1,000,000. Rerun here (`d3_sweep.out`): both `sendrecv` and `isend` completed, `received 1`, at 1, 505, 506, 1,000, 10,000, 100,000 and 1,000,000 doubles (8 to 8,000,000 bytes), each under `timeout 10`. The claim is true, but the evidence must be in the reproduction script.
- **Correction:** Replace with "Both safe versions completed at every size tried, from 1 to 1,000,000 doubles (8 to 8,000,000 bytes), including 505 and 506." and add to `run.sh` after the exchange loop: `for m in sendrecv isend; do for n in 1 505 506 1000 10000 100000 1000000; do timeout 10 $MPIRUN -np 4 ./exchange $n $m; done; done`.

### T2. Gustafson check (resolves D5)
- **Where:** `:549`, Section 6.3
- **Text:** "$f_s + (1 - f_s)\,p$ gives $0.0297 + 0.9703 \times 4096 = 3974.4$ for blocks at $p = 4096$, against 3974.2 from the model. They differ only by $f_s$"
- **Problem:** Recomputed from `model.py`'s own formulas (blocks, $N = 64000$, $p = 4096$): $T_p = 1.1842096$ ms, $f_s = 0.0297326$, model $S_s = p\,T_1^{\mathrm{local}}/T_p = (1 - f_s)\,p = 3974.2154$, Gustafson $f_s + (1 - f_s)\,p = 3974.2451$. With the rounded $f_s$, $0.0297 + 0.9703 \times 4096 = 3974.3785$, so the shown difference (0.2) is seven times $f_s$ and contradicts the explanation. The explanation itself is right: the model's one-process run has no communication, so $T_1 = (1 - f_s)\,p\,T_p$, while Gustafson's serial part $f_s$ also runs on one process.
- **Correction:** "$f_s + (1 - f_s)\,p$ gives $0.029733 + 0.970267 \times 4096 \approx 3974.24$ for blocks at $p = 4096$, against 3974.22 from the model. They differ by exactly $f_s$, because communication, unlike a serial part, takes no time on one process."

### T3. Summary: rounding error of the global sum (resolves C5)
- **Where:** `:612`, Summary row "How is it checked?"
- **Text:** "global sums to a small multiple of rounding error."
- **Problem:** Recomputed from `jacobi.out`: the change norm differs from the serial value by a relative $2.36 \times 10^{-13}$ ($p = 2$), $2.62 \times 10^{-13}$ ($p = 4$) and $2.65 \times 10^{-13}$ (overlap). The norm is a square root, so the sum of squares differs by about $5.2 \times 10^{-13}$, which is 4,260 to 4,770 unit roundoffs ($u = 2^{-53}$). The worst-case bound for a reordered sum of $10^6$ positive terms is about $(n-1)u = 1.1 \times 10^{-10}$, so the agreement is well within rounding error but not "a small multiple" of it.
- **Correction:** "The grid must match a serial run exactly; global sums agree only to within the rounding error of a reordered sum ($2.6 \times 10^{-13}$ relative here)."

### T4. Unsupported "0.65 s in an earlier session"
- **Where:** `:454`, Section 5.3
- **Text:** "in an earlier session an instrumented copy of the blocking version also ran in 0.65 s on four processes, so the difference between the two versions here is within the spread between sessions."
- **Problem:** The writer's directory records one instrumented blocking run with the 0.5 initial guess (`per_rank.out`, from `jt5`): total 0.861 s; per-rank compute 0.563 to 0.650 s. The 0.65 s is the largest compute time, not a run time. The earlier instrumented program (`diag/jd.c`) left no output; rerun here three times it took 1.00 to 1.54 s (on a different host). No record supports a 0.65 s blocking run. The conclusion still holds from the article's own data: the three blocking runs at $p = 4$ span 0.721 to 0.883 s (0.16 s), more than the 0.118 s between the blocking and overlap medians; in this review's rerun the ranges overlapped (blocking 1.007 to 1.080 s, overlap 0.848 to 1.141 s).
- **Correction:** "On a noisy shared virtual machine these figures are approximate. The three blocking runs at $p = 4$ span 0.72 s to 0.88 s, a wider range than the 0.12 s between the blocking and overlapping medians, so these runs do not show that the overlap helps."

### T5. LogP gap and the affine model
- **Where:** `:259`, Section 3.4
- **Text:** "An algorithm analyzed under LogP is charged for overhead it cannot overlap and for the gap it must respect. The affine model folds both into $\alpha$."
- **Problem:** For one message between idle processors LogP gives $L + 2o$, which is what $\alpha$ measures (the ping-pong's 0-byte time). The gap $g$ limits only consecutive messages from one processor, which the affine model does not describe at all; it is not part of $\alpha$. (The copy edit, C4, turned the original ambiguous relative clause into "both", which makes the error explicit.)
- **Correction:** "The affine model folds the overheads and the latency into $\alpha$ (for one short message, $\alpha \approx L + 2o$) and has no counterpart of the gap, because it describes one message at a time."

### T6. Size of the subnormal band
- **Where:** `:456`, Section 5.3
- **Text:** "a band of up to about 21,000 points (2% of the grid) held **subnormal numbers**"
- **Problem:** `zero_count.c` counts subnormal values only every 200 sweeps; its largest sample is 21,018 at sweep 1400. Counting after every sweep (`zc_all.c`, the same program with the test made unconditional) gives a maximum of 22,952 values (2.3% of $10^6$) at sweep 1475, rows 975–999; subnormals are present from sweep 511 to about 1545. With the initial guess 0.5 (`hc_all.c`), no sweep has a subnormal value, which confirms "no subnormal values occur".
- **Correction:** "a band of up to about 23,000 points (2.3% of the grid) held ..."

### T7. Tail of the series and rounding (optional)
- **Where:** `:362`
- **Text:** "differs from the limit $\pi^2/6$ by $9.8 \times 10^{-9}$, close to the tail ... The total depends on the order in which the partial sums are added"
- **Problem:** The accurate sum (`math.fsum` over the same four cyclic shares) is 1.6449340568482265, so $\pi^2/6$ minus the exact finite sum is $9.99999994 \times 10^{-9}$; the program's total is $2.4 \times 10^{-10}$ higher, the rounding error of the four long sequential loops (rank 0's partial is off by $2.5 \times 10^{-10}$). The combination of four numbers contributes far less.
- **Correction (optional):** add "The remaining $2.4 \times 10^{-10}$ is rounding error accumulated in the four partial sums." and change "the order in which the partial sums are added" to "the order in which the terms and partial sums are added".

### T8. Stability of the eager fit (optional)
- **Where:** `:234`, `:253`, `:608`
- **Problem:** Three reruns of `pingpong` here (different host) gave: large-message fit α = 3.2–4.3 µs, 1/β = 8.0–9.7 GB/s, consistent with the article's 3.1 µs and 8.3 GB/s; eager fit α = 0.24–0.44 µs but 1/β = 1.57–4.78 GB/s and measured/model up to 1.59–2.22; the 8 MiB time varied from 879 to 1,732 µs. The two-protocol conclusion holds (one line gives ratios up to 2.9–3.4), but the eager bandwidth and the factor 1.22 are single-run figures.
- **Correction (optional):** at `:253` "Two lines, one per protocol, fit every point of this run to within a factor of 1.22; the eager-range bandwidth is the least repeatable of the fitted values." No change needed to the summary row if `:18`'s "describes this machine only" is kept.

### Checks with no finding
- Definitions: distributed memory, SPMD, rank, communicator, blocking, standard mode, eager and rendezvous, deadlock, latency, $n_{1/2}$, collectives, ghost cells, halo, surface-to-volume ratio, Karp-Flatt $e$, scaled speedup: standard usage; $T_1$, $S$, $E$, $f_s$, $S_s$ consistent with the first entry (its Section 3.1 and conventions).
- $n_{1/2} = \alpha/\beta$ from $m/(\alpha + \beta m) = 1/(2\beta)$; units s/(s/byte) = bytes. Check at `:253`: $25620/(3.086\,\mu\text{s} + 25620/8.30\,\text{GB/s}) = 4.1505$ GB/s, half of 8.30.
- Collective costs: binomial broadcast $\lceil\log_2 p\rceil(\alpha + \beta m)$; recursive doubling $\log_2 p(\alpha + \beta m)$; ring $2(p-1)\alpha + 2\frac{p-1}{p}\beta m$; Rabenseifner $2\log_2 p\,\alpha$ with the ring's bandwidth term; barrier lower bound by the doubling-of-knowledge argument. Special case $p = 2$: ring gives $2\alpha + \beta m$, recursive doubling $\alpha + \beta m$ (ring sends two half-messages), correct.
- 2-D FTCS: $u + \mu(\text{4 neighbors} - 4u)$ with $\mu = 1/4$ is the Jacobi average; amplification factor range evaluated on a 401 × 401 grid of angles: min $G = -1.0000$ at $\mu = 0.25$, $-1.0008$ at $0.2501$, $-1.08$ at $0.26$, max 1; so stable exactly when $\mu \le 1/4$ (equal spacing, implied by the square grid).
- Surface-to-volume: strips/blocks ratio $(2p/N)/(4\sqrt p/N) = \sqrt p/2$ (2.0 at $p = 16$); equal at $p = 4$. At $p = 4$, $N = 8192$: strip halo 17.110 µs, block halo 21.107 µs, difference 4.0 µs = $2\alpha$, as stated at `:524`.
- Strong-scaling claims at `:524`–`:526`: $E \ge 0.98$ to $p = 64$; communication 68.6% and 63.3% at 4,096; $e$ 0.00035 to 0.00053 for strips; speedup does eventually fall (blocks: $S$ peaks at 1,884 at $p = 16384$, then 1,867, 1,738, ... down to 1,285 at $p = 2^{26}$).
- Halo exchange code: `MPI_PROC_NULL` at both ends, tags 0 upward and 1 downward match in both branches; overlap branch updates rows 2 to $n-1$ before `MPI_Waitall` and never touches the send rows' buffers or the ghost rows before completion; `n > 1` guard correct.

### Log of recomputations and runs
| What | Command / script | Result | Article |
|---|---|---|---|
| hello | `mpirun -np 4 ./hello` | 4 lines, order 0, 2, 3, 1 | matches (order varies, as stated) |
| exchange, 4 argument sets | quoted loop with `timeout 10` | 505 completes, 506 killed by timeout, sendrecv 506 and isend 10^6 complete | identical |
| exchange sweep (T1) | both safe modes × 7 sizes | all complete | supports `:165` |
| eager limit, PML | `ompi_info`, `--mca pml_base_verbose 10` | 4096 including header; ob1; vader; single copy CMA | matches `:95` |
| fit of writer's ping-pong | `python3 fit.py pingpong.out` | identical three lines | identical |
| ping-pong × 3, locked | `pingpong`, `fit.py` | see T8 | magnitudes hold |
| allreduce × 2, locked | `allreduce` | partials and total bitwise identical; 9.756e-09; 1.17 and 1.19 µs | identical; 1.11 µs, same magnitude |
| allreduce model | Python | $2(0.366 + 8/2130) = 0.7395$ µs | 0.74 |
| accurate series sum | `math.fsum` | see T7 | |
| collectives table | `collectives.py` | `diff` with writer's output: identical | identical |
| scaling model | `model.py` | `diff`: identical | identical |
| Jacobi serial/MPI, locked | `run_jacobi.sh` loop | all change norms identical to the digit; all four comparisons bitwise identical; times serial 2.92–3.09 s, p = 2 1.70–2.11 s, p = 4 1.01–1.08 s, overlap 0.85–1.14 s | deterministic parts identical; speedups 1.68, 2.83, 3.10 here vs 1.75, 2.98, 3.52 (same shape) |
| speedups, $t_c$ | Python | 1.7529, 2.9805, 3.5191; $t_c$ = 1.149 ns | match |
| model vs measurement, 6.1 | Python | predicted 1.1659 and 0.5922 s; communication 2.99% at $p = 4$; measured/predicted 1.12, 1.30, 1.10 | match "10% to 30%", "about 3%" |
| per-rank timing, 0 and 0.5 guesses, locked | `jt0`, `jt5` | 0 guess: 2.324 s, ranks 2 and 3 compute 1.57 s vs rank 0 0.77 s (2.0×); 0.5 guess: 1.100 s, compute 0.74–0.81 s | writer: 1.95 s, 2.5×; 0.861 s, 0.56–0.65 s (see T4) |
| subnormal counts | `zero_count`, `half_count`, `zc_all`, `hc_all` | see T6 | |
| Gustafson check | Python | see T2 | |
| change-norm differences | Python | see T3 | |
| Exercise 1 | Python | 102 µs; 0.476 GB/s | match |
| Exercise 3 | Python | 408 µs; 247.5 µs | match |
| Exercise 4 | Python | 18.825, 8.410, 24.010, total 51.244 µs; overlap $S$ = 1800.1, $E$ = 0.4395; every 10 sweeps $S$ = 3632.7, $E$ = 0.887; $T_1$ = 77.108 ms | match |

**Technical verdict: fail until T1 to T6 are applied** (blocking 0, should fix 6, optional 2). No equation, code block or deterministic output is wrong; the open findings are one miscomputed illustration (T2), two imprecise numbers (T3, T6), one unsupported statement (T4), one inaccurate model comparison (T5) and one claim whose evidence is missing from the reproduction script (T1).

## Resolution

Stage EOS 7, by the author. Every should-fix finding was applied using the reviewers' proposed text, and so were all four optional findings. The container now runs on a different processor, so no reference-machine timing was re-run and no measured number was changed except where a finding required it (T4, T6). After resolution, `npm run eos -- lint`: 0 errors, 0 warnings, 8 suggestions (those kept under C6, plus the sentence-length suggestion for the T5 sentence in Section 3.4).

| ID | Disposition | Change |
|---|---|---|
| D1, D2, C1–C4 | Accepted as applied by the editors | No further change. |
| D3 / T1 | Applied | Section 2.4 now reads "Both safe versions completed at every size tried, from 1 to 1,000,000 doubles (8 to 8,000,000 bytes), including 505 and 506." The sweep is added to the author's `run.sh` after the exchange loop, as proposed; the evidence is the reviewer's `d3_sweep.out` (all 14 runs completed). |
| D4 / F1 | Applied | "and Version 5.0 followed in 2025 (Message Passing Interface Forum, 2025)"; the Version 5.0 document was added to the References after the 4.1 entry. |
| D5 / T2 | Applied | Section 6.3 uses the unrounded values: "$0.029733 + 0.970267 \times 4096 \approx 3974.24$ ... against 3974.22 from the model. They differ by exactly $f_s$". |
| D6 | Not applied | Heading kept, for the reason given in the developmental section. |
| C5 / T3 | Applied | Summary row: "global sums agree only to within the rounding error of a reordered sum ($2.6 \times 10^{-13}$ relative here)." |
| C6 | Accepted | Suggestions kept for the reasons given. |
| F2 | Applied | Patarasuk and Yuan: "vol. 69, no. 2, pp. 117–124, 2009". |
| F3 (optional) | Applied | "and their semantics are unchanged in Version 4.1." |
| F4 (optional) | Applied | Section 4.1: "the costs below follow that analysis (the ring allreduce follows Patarasuk and Yuan, 2009) but leave out ...". |
| T4 | Applied | The unsupported "0.65 s in an earlier session" sentence is replaced by the reviewer's text, which uses only the quoted runs: the three blocking runs at $p = 4$ span 0.72 s to 0.88 s, a wider range than the 0.12 s between the medians, "so these runs do not show that the overlap helps." The author confirms the 0.65 s figure was the instrumented run's largest per-rank compute time, not a run time. |
| T5 | Applied | Section 3.4: "The affine model folds the overheads and the latency into $\alpha$ (for one short message, $\alpha \approx L + 2o$) and has no counterpart of the gap, because it describes one message at a time." |
| T6 | Applied | "a band of up to about 23,000 points (2.3% of the grid)". The author copied the reviewer's every-sweep counters (`zc_all.c`, `hc_all.c`) into the work directory, added them to `run.sh` and re-ran them. They are deterministic, so the change of host does not matter: the largest band is 22,952 values at sweep 1475 (rows 975–999), and there are 0 subnormal values over all sweeps with the guess 0.5. |
| T7 (optional) | Applied | Section 4.4 adds "The remaining $2.4 \times 10^{-10}$ is rounding error accumulated in the four partial sums." and now says "the order in which the terms and partial sums are added". |
| T8 (optional) | Applied | Section 3.3: "fit every point of this run to within a factor of 1.22; the eager-range bandwidth is the least repeatable of the fitted values." |

No open should-fix or blocking finding remains.
