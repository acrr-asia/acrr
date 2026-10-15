# Editorial tool evaluation (Phase 1)

Date: 13 October 2026. Evaluator: the editorial engineering pass that built `plugins/editorial-os`. Environment: the project's cloud container (Node 22.22, Python 3, Go 1.26, Java present; outbound access through a proxy that allows package registries and the Go module proxy, and blocks GitHub release downloads and most other hosts for command-line tools; WebSearch and WebFetch available).

Every claim below was checked by running the tool on ACRR's content or by reading its source or listing; where a tool could not be run here, that is stated.

## 1. Criteria

Each candidate was scored against the seven criteria of the brief: (1) editorial quality and linguistic precision, (2) technical and scientific accuracy, (3) research and source verification, (4) long-form and series review, (5) compatibility with the stack (Astro 7, MDX, KaTeX math, Mermaid, Node, GitHub Actions, Claude Code), (6) automation, extensibility, maintainability, licensing, (7) portability across sites and domains.

## 2. Candidates examined

### 2.1 Claude ecosystem

| Candidate | Source | What was verified | Verdict |
|---|---|---|---|
| ACRR `series-review` and `complete-series` skills | This repository (`.claude/skills/`) | Read in full; they produced the nine resolved, stamped series reviews in `reviews/` and are wired to `scripts/series-pipeline.mjs`, the PostToolUse hook and CI | **Adopted and extended**: Phase 5 runs on `series-review`; the new suite calls it rather than replacing it |
| "Writing Skills" (surendranb/writing-skills) | Anthropic Directory listing; GitHub repository read via WebFetch | MIT; 14 prose-style skills (plain language, ASD-STE100, Google developer docs, GOV.UK, AP, Orwell's rules) plus character voices; plain SKILL.md files with checklists and a skill validator; no fact-checking, no technical review, no series handling | Not adopted: general-purpose style frameworks; their measurable rules (sentence length, banned words, passive ceilings) are covered by `eos lint` with ACRR's own thresholds. Its `google-dev-docs` skill is a reasonable optional reference for documentation projects |
| "anti-ai-writing" | Anthropic Directory listing (community) | Listing only (no public source); rewrites text to remove "AI tells" | Not adopted: a rewrite-first tool risks changing technical meaning; the useful part (a phrase and pattern list) is implemented transparently in `glossary.json` and the copy-editor agent's instructions |
| "writing-quality" (claim-boundary-checker, writing-enforcer) | Anthropic Directory listing (community) | Listing only | Not adopted; its claim-boundary idea is covered by the fact-checker stage and Policy C of the standards |
| "Proofread" | Anthropic Directory listing (community) | Listing only; conservative proofreading and translation review | Not adopted now; **candidate for the Vietnamese translation work**, which is outside this English-scope pass |
| "Copywriting & Positioning", copy-editing skills on claudemarketplaces.com (several repositories) | Listings | Marketing copy for product pages | Not relevant to research writing |
| `every-style-editor` (EveryInc compound-engineering plugin) | claudemarketplaces.com listing | One SKILL.md enforcing Every's house style; explicitly does not assess structure or argument | Not adopted: publication-specific; the pattern (house style as a skill) is what `style-guide` + `standards.md` generalize |
| anthropics/skills | GitHub repository page | Document skills (docx, pdf, pptx, xlsx) and creative/technical skills; no editorial, fact-checking or review skill found | Nothing to adopt for this purpose |
| Skills on the user's claude.ai account | `SearchSkills` (editing, copy edit, proofreading, style guide, fact check, technical writing) | No results | — |

No existing skill or plugin covered the core requirement: a configurable, multi-role editorial workflow with deterministic checks, review records and a publication gate for technical content in MDX.

### 2.2 Deterministic prose and structure checkers

| Tool | Version, licence | How it was tested | Result on ACRR content | Verdict |
|---|---|---|---|---|
| **Vale** | 3.24.0, MIT (Go) | Built from source through the Go module proxy (GitHub release downloads are blocked here); styles Google 0.7.1, Microsoft 0.15.1, proselint 0.3.4, write-good 0.4.1 and Readability 0.2.0 fetched the same way; `mdx2vast` for MDX | Six articles with all four packages: 50 to 1,001 alerts per article, dominated by rules that conflict with academic writing (write-good E-Prime 170 in one article; Acronyms 90; Parens 82; Passive 52). A curated set across all 63 items: 837 alerts, of which 437 were Microsoft.Vocab ("verify your use of 'against'") and 282 write-good Weasel ("usually"). Domain false positives: "discriminant" flagged as needless (suggests "discriminating"), "decimate" as a skunked term, hexadecimal `0x123` as a typography error (suggests "×"), and a cited author's surname "Workman" as gender bias | **Adopted as an optional editor integration, not as the gate.** The engine is excellent (MDX-aware, IDE plugins, CI action); the generic packages are too noisy for this domain. `eos vale-style` generates a Vale style from ACRR's own glossary and spelling rules (verified to run with Vale 3.24.0) |
| proselint | 0.16.0, BSD (Python) | Installed with pip | Same rule set as Vale's proselint package (results above) | Not adopted separately |
| textlint + write-good + sentence-length + MDX plugin | 15.8.0, MIT (Node) | Installed with npm and run on two articles | 243 problems on two articles; 133 of 196 on the DFT article were sentence-length hits that counted display math and reference lists as sentences (one "sentence" of 207 words was a reference list) | Not adopted: no math awareness without custom filters, and it would add about a hundred npm dependencies to a site whose scripts are dependency-free |
| LanguageTool | LGPL (Java) | Maven Central reachable; not run (the public API would send the text to a third party; a local server is a large Java service) | — | Optional second opinion for grammar, documented in the plugin README. The corpus has few grammar errors; its problems are structural and stylistic |
| markdownlint | MIT (Node) | Rules read | Overlaps with `eos` heading rules; does not understand MDX components or KaTeX | Not adopted |
| ACRR `scripts/check-links.mjs` | In repo | Ran on the full build: 314 pages, 9,628 internal references | Clean | **Adopted** as the internal link and fragment gate |

### 2.3 Source and link verification

| Tool | Verified | Verdict |
|---|---|---|
| Crossref / DOI resolution, RFC Editor, standards catalogues | Not reachable from command-line tools here (proxy refuses); reachable through WebSearch/WebFetch | Used by the fact-checker agent through WebSearch/WebFetch; a claim that cannot be checked is recorded as "not verified" |
| lychee (external link checker) | Cannot be downloaded here (GitHub releases blocked) | Documented as the recommended CI alternative; `eos check-external` provides the same check dependency-free and reports unreachable hosts as "not verified", never as "broken" |
| ACRR content | `eos check-external` and `eos refs` | The site contains no external URLs outside `example.com` code samples; its 224 reference entries (176 distinct works) are book and paper citations without URLs, so verification is bibliographic |

## 3. Selection and rationale

The selected combination is complementary, with one tool per job and no redundant layers:

| Job | Selected | Why |
|---|---|---|
| Workflow orchestration and roles | `editorial-os` plugin (new): `editorial`, `content-audit`, `editorial-review`, `series-editorial-review`, `style-guide` skills; five role agents | Nothing existing covered it; native Claude Code packaging (validated with `claude plugin validate`, installed at project scope) |
| Series-level review | ACRR `series-review` skill (existing) + `scripts/series-pipeline.mjs` | Proven on all nine series; kept and referenced by the new suite |
| Deterministic style, structure, cross-reference and metadata checks | `eos lint` / `eos fix` (new, dependency-free Node) | Masks code, math, JSX, URLs and front-matter keys, so it has no math false positives; checks things no prose linter does (ordinal and section cross-references between series entries, required sections, heading numbering, description length); reads one configuration shared with the AI stages |
| In-editor style feedback | Vale with the generated house style (`eos vale-style`) | Best editor integration; optional |
| Built-site rendering and accessibility | `eos validate-site` (new) + build + `check-links` | Catches what the build does not: KaTeX errors, heading order, glued inline text, oversized diagrams, duplicate ids, meta description length, spelling on non-content pages |
| Fact-checking and citations | `fact-checker` agent with WebSearch/WebFetch | Judgment-intensive; the agent records evidence and "not verified" items |
| Technical accuracy | `technical-reviewer` agent, recomputing with Python | Judgment plus execution |
| Final gate | `eos record` + `eos gate` (review records with content hashes) + existing series gate | Deterministic, auditable, blocks publication in CI |

## 4. Installation notes for the tools not bundled

- **Vale**: `brew install vale` or a release binary from https://github.com/errata-ai/vale/releases; where release downloads are blocked, `go install github.com/vale-cli/vale/v3/cmd/vale@latest` (the module path is `vale-cli/vale`, not `errata-ai/vale`). For MDX, `npm i -g mdx2vast`. Then `npm run eos -- vale-style` and `vale --config editorial/vale/.vale.ini src/content/blog/<file>.mdx`.
- **LanguageTool** (optional): run a local server (`docker run -p 8010:8010 erikvl87/languagetool`) and query it from an editor plugin; do not send unpublished text to the public API.
- **lychee** (optional, CI): `lycheeverse/lychee-action` in a workflow, if the site gains external URLs.
