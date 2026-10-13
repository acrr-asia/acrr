---
name: series-review
description: Comprehensive editorial and technical review of every article in a completed ACRR series (technical accuracy, factual consistency, concept introduction, stated versions and defaults, logical flow, terminology, cross-article references, completeness, writing quality, fit with the series objectives). Use when a series has just been marked complete (status "published", no planned entries), when the series-complete hook or the Series review workflow asks for it, or when the user asks to review a series. Argument - the series id (file name in src/content/series without extension).
---

# Series review

Review one series as a whole, the way a technical editor reviews a book before it goes to print. The output is a report of findings with recommended corrections. **Do not edit articles or the series file during the review**; corrections are applied only if the user asks afterwards.

The argument is a series id, such as `identity-and-access-control`. If none was given, run `node scripts/series-review.mjs detect HEAD~1 HEAD`, or ask which series.

## 1. Collect the series

1. Run `node scripts/series-review.mjs list <id>`. It prints the series file, its status, the number of planned entries, the articles in `seriesOrder` with their paths and routes, and warnings: gaps or duplicates in `seriesOrder`, drafts, and an incomplete series.
2. If the series is not complete, say so at the top of the report and still review the published articles, unless the user only wanted a completeness check.
3. Read `CLAUDE.md`, in particular "Content-integrity rules". Those rules are part of the review criteria.
4. Read the series file (title, description, `objectives`, body text) and then **every article in full, in reading order**. Do not sample or skim. Keep notes per article as you go: every technical concept it relies on (protocols, data formats, standards, mathematical objects, algorithms) and where, if anywhere, it says what that concept is; every version, default or convention its examples assume; the terms it defines, the claims it makes that later articles rely on, its references to other entries ("the second entry", "Section 5.2 of the first entry", "the next entry ..."), and its promises ("a later entry treats ...").

## 2. Verify mechanically

Run these, record the results in the report's verification log, and treat any failure as a blocking finding:

- `npm run build:local` (type and schema check, build, Mermaid and KaTeX rendering, search index). Use `SITE_URL=https://acrr.asia npm run build` instead when running locally and a release check is wanted.
- `npm run check:links`.
- For each article, look in `dist/blog/<slug>.html` for Mermaid diagrams whose `min-width` exceeds about 600px (they overflow the text column), and for text glued to inline elements (see "Whitespace before inline elements" in `CLAUDE.md`).

Where an article contains values that can be recomputed (hashes, encodings, worked numerical examples, formula checks such as substituting a special case), recompute them if a tool is available in this environment, and record each check and its result. If you cannot recompute a value, list it under "Not verified" rather than assuming it is right.

## 3. Review dimensions

Assess every article against each dimension, and the series as a whole where the dimension is about the series. For each problem, record a finding (format in section 5).

| Dimension | What to check |
|---|---|
| Technical accuracy | Definitions, formulas, protocol details, parameter names, numerical values and standard or RFC numbers are correct. Claims about standards match what those standards say. Edge cases and limits are stated where omitting them would mislead. Examples are internally consistent (values in one example agree with values in another). |
| Factual consistency | The same fact, value, name or date is stated the same way everywhere in the series. No article contradicts another. Dates, authors and titles of cited works are consistent and plausible. Nothing is fabricated (statistics, results, quotes, URLs) in breach of the content-integrity rules. |
| Concept introduction | Every technical concept an article relies on is introduced before its details: what it is, what problem it solves or what role it plays, and its scope, in a sentence or two, either in that article or in an earlier entry that is explicitly referred to. A section must not open with mechanics (message formats, fields, equations, code) of something it has never said what it is. Example of a defect: a section headed "HTTP is stateless" that describes request structure without first saying that HTTP is the application-level request–response protocol between a client and a server. Check this especially for foundational concepts that a series treats as "obvious" (HTTP, TLS, TCP, JSON, a matrix, a probability distribution), and for the first article of a series, which sets the foundation for all others. |
| Stated versions and defaults | Every example, syntax or claim that depends on a version, edition, platform, default or convention says which one it uses and whether the point depends on it. Examples: HTTP messages written in HTTP/1.1 text syntax must say so, and note that HTTP/2 and HTTP/3 carry the same semantics (RFC 9110) in a binary framing; TLS 1.2 vs 1.3; OAuth 2.0 vs 2.1; IPv4 vs IPv6; a programming-language or library version; units (degrees vs radians, metres); coordinate and sign conventions; quaternion component order. Also flag a version or default presented as the only or current form when it is legacy or one of several in common use. |
| Logical flow | Within each article, concepts are introduced before they are used, and sections follow the order the introduction promises. Across the series, each article builds on earlier ones in order, nothing assumes material from a later entry, and the series moves from the general to the specific. |
| Terminology | Each technical term is defined once (where it first appears) and used with the same meaning thereafter. Spelling and capitalisation of terms and product-neutral names are consistent (for example British vs American spelling within the series). Abbreviations are expanded on first use in each article. |
| Cross-article references | Every reference to another entry ("the third entry", "Section 4.3 of the first entry") points to an article and section that exist and say what is claimed. "The next entry ..." matches the actual next article. Promises such as "a later entry treats X" are fulfilled somewhere in the series. Internal links resolve (already checked by `check:links`; also check that the linked text matches the target). |
| Completeness | Every objective in the series file is covered by at least one article. Topics promised in the series description or introductions are covered. Each article's summary reflects its body. Nothing essential to the series' stated scope is missing; note gaps, but do not demand material outside the scope. |
| Writing quality | Clear, precise, concise English; no padding or repetition across articles; consistent tone and structure (headings, summary tables, reference lists); correct grammar and punctuation; tables and diagrams that earn their place and match the prose. |
| Fit with objectives and site rules | The series meets its own objectives and description. The `CLAUDE.md` content-integrity rules hold (no fabrication, original writing, English only; examples labelled). Frontmatter is consistent across the series (category, tags, `seriesOrder`, dates). |

## 4. Severity

- **Blocking**: factually wrong, contradicts another article, broken or false cross-reference, an unmet objective, a content-integrity breach, or a failed build or link check. Must be fixed before the series is considered final.
- **Should fix**: misleading or imprecise statements, inconsistent terminology, flow problems, unfulfilled minor promises, writing that obscures meaning, a concept used without being introduced, and an example whose version or convention is assumed but not stated. Raise a missing introduction of a concept that the series itself is about (or that its first article builds on) to **Blocking** when the series description or introduction promises a top-down or from-first-principles treatment.
- **Optional**: style and polish.

Be specific and conservative. Report only problems you can point to in the text, with a quotation. Do not report personal stylistic preferences as defects, and do not re-litigate a deliberate editorial choice unless it causes one of the problems above.

## 5. Report

Write the report to `reviews/<id>.md` (create the directory if needed), overwriting any earlier report for the same series. Use this structure:

```markdown
# Series review: <series title>

- Series: `<id>` (<n> articles, status <status>, <planned> planned entries)
- Reviewed commit: <output of `git rev-parse --short HEAD`>
- Date: <YYYY-MM-DD>

## Summary
<Three to six sentences: overall assessment, the most important problems, and whether the series is ready as published.>
Findings: <b> blocking, <s> should fix, <o> optional.

## Objectives coverage
| Objective (from the series file) | Covered by | Assessment |
|---|---|---|

## Findings
| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Blocking | `<path>` | Section 3.2 (line 141) | Technical accuracy | <one line> |

### F1. <short title>
- **Where:** `<path>:<line>`, section "<heading>"
- **Text:** "<exact quotation>"
- **Problem:** <what is wrong and why, with evidence: a standard, a recomputation, the contradicting passage with its own path:line>
- **Recommended correction:** <replacement text, ready to paste, or a precise instruction>

## Concept introduction map
| Concept | First used (path:line) | Introduced where (path:line, or "not introduced") | Assessment |
|---|---|---|---|
<One row per foundational concept the series relies on (protocols, formats, standards, mathematical objects). A concept used before it is introduced, or never introduced, is also a finding.>

## Versions, defaults and conventions
| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
<One row per version, default or convention an example or claim depends on (protocol versions, units, coordinate conventions, library versions). An unstated one that matters is also a finding.>

## Series-level notes
<Consistency across articles: terminology table if useful, cross-reference map, structure and tone.>

## Verification log
- `npm run build:local`: <result>
- `npm run check:links`: <result>
- Recomputed: <each value checked and the result>
- Not verified: <claims that could not be checked here, and why>
```

Number findings in severity order (all blocking first). Use repository-relative paths and the line numbers of the source `.mdx`/`.md` files.

## 6. Finish

Reply with the report path, the counts by severity, and the blocking findings in one line each. Then offer to apply the recommended corrections. Apply them only on request, one commit per review, and re-run the build and link check afterwards.
