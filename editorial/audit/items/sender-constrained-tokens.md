<!-- audit: {"slug":"sender-constrained-tokens","type":"article","series":"identity-and-access-control","priority":"P2","before":{"purpose":3,"structure":3,"accuracy":4,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":5,"optional":2}} -->
# Audit: Sender-Constrained Tokens: DPoP and Mutual TLS

- Path: `src/content/blog/sender-constrained-tokens.mdx` · Route: `/blog/sender-constrained-tokens` · Type: article · Series `identity-and-access-control`, entry 6 of 7 · Words: 2325 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: clear; the previous and first entries are not linked.
- structure 3: sound (concept, two mechanisms, limits, choice, summary). Slightly under the 2,500-word guide for a series entry, but complete; no padding is needed.
- accuracy 4: sample values recomputed (below).
- evidence 2: no References list; RFC numbers only. "RFC 8471 to RFC 8473 (Token Binding, historical)" could be read as the RFCs' status; the RFC Editor lists all three as Proposed Standard.
- language 3: "simply" (211); a 49-word sentence (48); "towards" (270).
- consistency 3: references to the first, third and fifth entries unlinked.
- publishing 2: description 278 characters; two title-case H2 headings.

## Accuracy check

Recomputed with python3: the RFC 7638 thumbprint of the JWK in §3.2 (members `crv`, `kty`, `x`, `y`, sorted, no whitespace) is `0ZcOCORZNYy-DWpqq30jZyJGHTN0d2HglBV3uiguA4I`, the `cnf.jkt` of §1.2; base64url SHA-256 of the access token `Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU` is `fUHyO2r2Z3DZ53EsNrWBb0xWXoaNy59IiKCAqksmQEo`, the `ath` of §3.2. The claim at line 48 that the values are mutually consistent holds.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 278 characters. |
| P2 | Should fix | lines 231, 254 | language | Title-case headings. |
| P3 | Should fix | lines 286–292 | evidence | No References list in house format. |
| D1 | Should fix | lines 16, 30, 62, 248 | consistency | Entries named but not linked. |
| C1 | Should fix | lines 36, 48, 145, 270 | language | JWT, JWK, SHA, DER, URI, BFF not expanded at first use. |
| C2 | Optional | lines 211, 48, 270 | language | "simply"; 49-word sentence; "towards". |
| A1 | Optional | line 291 | accuracy | "(Token Binding, historical)" reads as an RFC status; say "no longer supported by browsers". |

## Revision log (wave 1)
- Structure: opening links the previous and first entries and names the two specifications (RFC 8705, RFC 9449); its last sentence now also mentions the choice between them (§5), which it previously omitted.
- Prose: §1.2 sample-values sentence split; "simply" removed; "towards" → "toward".
- Terminology/style: two H2 headings in sentence case; JWT, JWK, DER, URI, BFF expanded at first use.
- Metadata: description 149 characters.
- References: `### References` (11 entries, house format, alphabetical); all RFCs checked at rfc-editor.org; Web Cryptography API (W3C Recommendation, 26 January 2017, M. Watson, Ed.). "Token Binding, historical" replaced by "(no longer supported by browsers; Section 4.3)", because the RFC Editor lists RFC 8471–8473 as Proposed Standard, not Historic (A1).
- Cross-references: links to the first entry §3.6 and §6.5, the previous entry and its §1.3, the third entry §8, and the final entry.
- Remaining suggestions and why they stay: SHA-256 is an algorithm name.
- Flags for independent review: none.
- Vietnamese translation affected: yes, in the opening sentence (specification numbers, mention of §5) and the References list; no technical change.
