<!-- audit: {"slug":"oauth-grants-and-client-types","type":"article","series":"identity-and-access-control","priority":"P2","before":{"purpose":3,"structure":3,"accuracy":3,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":6,"optional":1}} -->
# Audit: OAuth 2.0 Grants and Client Types

- Path: `src/content/blog/oauth-grants-and-client-types.mdx` · Route: `/blog/oauth-grants-and-client-types` · Type: article · Series `identity-and-access-control`, entry 5 of 7 · Words: 2842 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: clear organizing idea (three questions); first entry not linked.
- structure 3: sound; ends in a table, a decision flowchart and a summary.
- accuracy 3: the text calls OAuth 2.0 for Browser-Based Applications "the IETF's ongoing guidance" (79) and lists it as "In progress at the IETF" (314). It was published as RFC 10017 (Best Current Practice) in August 2026 (rfc-editor.org/info/rfc10017, fetched); its Section 6 describes the same three patterns ("Backend for Frontend (BFF)", "Token-Mediating Backend", "Browser-Based OAuth 2.0 Client"). OAuth 2.1 is still an Internet-Draft (draft-ietf-oauth-v2-1-16, September 2026), so line 266 stands.
- evidence 2: no References list; "### The specifications" lumps RFC numbers.
- language 3: "simply" (198), "very" (264); two 53-word sentences (17, 235).
- consistency 3: cross-references to the first, second and third entries unlinked.
- publishing 2: description 283 characters; five title-case H2 headings.

## Accuracy check

Recomputed with python3: `BASE64URL(SHA-256("dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"))` = `E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM`, the challenge in the authorization request (the RFC 7636 Appendix B pair); the Basic credentials `cGhvdG8tcHJpbnRlcjpleGFtcGxlLXNlY3JldA==` decode to `photo-printer:example-secret`, matching `client_id=photo-printer`. RFC numbers and subjects verified at rfc-editor.org.

## Priority

P2.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| A1 | Should fix | lines 79, 314 | accuracy | Browser-based applications guidance described as in progress; now RFC 10017 (2026). |
| P1 | Should fix | `:3` | publishing | Description 283 characters. |
| P2 | Should fix | H2 headings | language | Title case. |
| P3 | Should fix | lines 308–315 | evidence | No References list in house format. |
| D1 | Should fix | lines 15, 51, 85, 162 | consistency | References to other entries unlinked. |
| C1 | Should fix | lines 15, 26, 48 | language | PKCE (expanded only at 95), URI, JWT not expanded at first use. |
| C2 | Optional | lines 198, 264, 17, 235 | language | "simply", "very"; long sentences. |

### A1. RFC 10017
- **Text:** "described in the IETF's ongoing guidance for browser-based applications" (79); "In progress at the IETF: OAuth 2.1, and OAuth 2.0 for Browser-Based Applications." (314)
- **Correction:** "described in RFC 10017, *OAuth 2.0 for Browser-Based Applications* (2026)"; list it in References (A. Parecki, P. De Ryck and D. Waite, RFC 10017, IETF, 2026).

## Revision log (wave 1)
- Technical/factual correction (A1): §2.3 now cites "RFC 10017, *OAuth 2.0 for Browser-Based Applications* (2026)" instead of "the IETF's ongoing guidance"; the References list it as published. Evidence: rfc-editor.org/info/rfc10017 (A. Parecki, P. De Ryck, D. Waite, August 2026, Best Current Practice); its Section 6 headings are "Backend for Frontend (BFF)", "Token-Mediating Backend", "Browser-Based OAuth 2.0 Client", matching the three options in §2.3. OAuth 2.1 remains an Internet-Draft (draft-ietf-oauth-v2-1-16, 3 September 2026), so §6's last paragraph stands.
- Structure: opening links the first entry and adds one sentence on the specifications followed (RFC 6749 as amended by RFC 9700; OAuth 2.1 as a draft).
- Prose: §5.2 forwarding sentence split; "simply", "very" removed.
- Terminology/style: seven H2 headings in sentence case; PKCE, URI, JWT expanded at first use.
- Metadata: description 154 characters.
- References: `### References` (17 entries, house format, alphabetical); all RFCs checked at rfc-editor.org; OpenID Connect Core errata set 2 (openid.net); OAuth 2.1 draft (datatracker).
- Cross-references: links to the first entry (opening, §5, §5.5, §7.2, §8), the second entry §5.5, the third entry §6, the final entry §5 and the next entry.
- Remaining suggestions and why they stay: line 17 counts three italic questions as one sentence; "URIs" (line 28) is expanded in the same phrase in plural form.
- Flags for independent review: (fact-check) confirm RFC 10017's status and that it still describes the token-mediating back end as passing access tokens to the browser.
- Vietnamese translation affected: yes, meaning changed in §2.3 (published RFC instead of ongoing guidance) and the References (RFC 10017 no longer "in progress"); one added sentence in the opening.

## Independent review (wave 2)

- Report: `reviews/identity-and-access-control.md`
- Fact-check: fail
- Technical: pass
- Findings: F1 (should fix), T2 (optional), S1 (should fix, Vietnamese translation still calls RFC 10017 a draft)
- Not verified: none.
