<!-- audit: {"slug":"compute-bound-or-memory-bound","type":"insight","series":null,"priority":"P2","before":{"purpose":2,"structure":3,"accuracy":4,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":1,"shouldFix":4,"optional":1}} -->
# Audit: Compute-Bound or Memory-Bound? The Roofline Idea

- Path: `src/content/insights/compute-bound-or-memory-bound.md` · Route: `/insights/compute-bound-or-memory-bound` · Type: insight (Concept explanation) · Words: 349
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 2: no framing paragraph (standards 6.4).
- structure 3: sound; the worked example sits in Established, which is acceptable because it is arithmetic on a stated hypothetical machine.
- accuracy 4: recomputed with python3: $I^* = 1000/100 = 10$ FLOP/byte; $I = 2/24 = 0.0833$; $B\,I = 8.33$ GFLOP/s; $1000/8.33 = 120$. Correct, and the bound is properly qualified ("The bound is not a prediction").
- evidence 2: the roofline model is a named model with an originating paper (Williams, Waterman and Patterson, *Communications of the ACM*, 2009) that is not attributed; the site has no in-depth article on processor performance, and the insight links to nothing.
- language 3: GFLOP/s, GB/s and FLOP not expanded (lint `acronym-expansion`).
- consistency 3: no link to the site's operation-count comparison of solvers (`solving-large-linear-systems`, Section 7), which counts flops only.
- publishing 2: description 177 characters, a noun phrase.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Blocking | line 12 | structure | No framing paragraph (standards 6.4, C7). |
| D2 | Should fix | line 14 | evidence | Roofline model not attributed to its source. |
| D3 | Should fix | whole file | consistency | No link to related site content. |
| P1 | Should fix | `:3` | publishing | Description 177 characters, not a sentence. |
| C1 | Should fix | line 18 | language | GFLOP/s, GB/s, FLOP not expanded. |
| C2 | Optional | line 22 | language | "Vectorization work would probably be wasted" is stronger than the bound supports for kernels near the ridge; acceptable for this example. |

### D2. Attribution
- **Correction:** "The roofline model of Williams, Waterman and Patterson (*Communications of the ACM*, vol. 52, no. 4, pp. 65–76, 2009)". Verified against the ACM DOI 10.1145/1498765.1498785 as listed by a course reference page and the search index (the Crossref API was blocked by the proxy).

### D3. Links
- **Correction:** link the operation counts of `/blog/solving-large-linear-systems#7-direct-or-iterative` as an example of a comparison that covers the arithmetic term only.

## Revision log (wave 1)

- Structure: added the framing paragraph.
- Evidence: attributed the model inline to Williams, Waterman and Patterson, *Communications of the ACM*, vol. 52, no. 4, pp. 65–76, 2009 (checked against a course reference page quoting DOI 10.1145/1498765.1498785 and the search index). $P$ defined; **roofline model** and **arithmetic intensity** in bold at definition.
- Language: GFLOP/s, GB/s and FLOP expanded at first use.
- Cross-references: added `/blog/solving-large-linear-systems#7-direct-or-iterative` with one sentence: flop counts bound only the arithmetic side.
- Metadata: description rewritten as one sentence (153 characters).
- Remaining suggestion: `acronym-expansion` "ACM" inside the journal title, a proper name.
- Flags for independent review: (technical) the added clause "for sparse matrices with few operations per stored entry [the data side] is often the one that binds" (Interpretation) is standard knowledge about sparse matrix-vector products but is not derived in the text. (series/editorial) the site has no in-depth article on processor performance; the insight cannot link one.
- Vietnamese translation affected: yes: framing paragraph, attribution, definition of $P$, expansions, new sentence with the link, new description.

## Independent review (wave 2)

- Report: `editorial/audit/review/standalone.md`
- Fact-check: pass
- Technical: pass
- Findings: F1 (optional)
- Not verified: none (citation verified against Crossref; sparse-matrix clause supported by the cited paper's SpMV results).

## Revision log (wave 2 resolution)

- F1 (optional): line 16: added "(the original paper calls it operational intensity)" after **arithmetic intensity**.
- Lint: 0 errors, 0 warnings; one suggestion ("ACM" in the journal title). Syntax: compiles.
- Vietnamese translation affected: yes, the parenthetical on the paper's term.
