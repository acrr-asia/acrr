<!-- audit: {"slug":"token-based-authentication","type":"article","series":"identity-and-access-control","priority":"P1","before":{"purpose":3,"structure":3,"accuracy":4,"evidence":2,"language":3,"consistency":3,"publishing":2},"findings":{"blocking":0,"shouldFix":7,"optional":3}} -->
# Audit: Authentication and Authorization: From First Principles to Tokens

- Path: `src/content/blog/token-based-authentication.mdx` · Route: `/blog/token-based-authentication` · Type: article · Series `identity-and-access-control`, entry 1 of 7 · Words: 5716 (from `eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: purpose and approach are explicit; the opening's second paragraph is partly a prose table of contents ("It starts with ..., treats ..., explains ..., and only then turns to tokens").
- structure 3: sound top-down order; the Summary (§11) ends with "The recurring lessons are short ..." and never leads to the second entry (standards 6.2 item 6).
- accuracy 4: every value recomputed (below); every RFC number checked against the RFC Editor.
- evidence 2: there is no References list. "### The specifications" gives bare RFC numbers grouped by topic; the Anderson report (line 31), Saltzer and Schroeder (line 37), the OWASP API Security Top 10 (line 207), XACML (line 205) and SAML 2.0 (line 309) are named in the text but not listed.
- language 3: four sentences over 50 words (lines 21, 37, 146, 290); "actually" (286); British "organisation" (309; `order.organisation` in pseudocode, 518).
- consistency 3: forward references to the third and sixth entries are unlinked (146, 176).
- publishing 2: description 237 characters; all ten H2 headings in title case (lint flags three; "1. The Access-Control Model", "5. Delegation and Federation", "6. Tokens in Detail", "7. The Token Lifecycle", "10. Threats and Controls" are also title case).

## Accuracy check

Recomputed with python3: `iat` 1791795600 and `exp` 1791796200 are 2026-10-12 09:00 and 09:10 UTC, ten minutes apart as stated (line 358); the JWT header prefix `eyJhbGciOiJSUzI1NiIsInR5cCI6ImF0K2p3dCJ9` decodes to `{"alg":"RS256","typ":"at+jwt"}`, consistent with the header shown; the session value `Q2hvb3NlIGEgcmFuZG9tIHZhbHVl` decodes to "Choose a random value" (see C4). RFC numbers and their subjects (9110, 7617, 6265, 6749, 6750, 7636, 7662, 7009, 8628, 9068, 9700, 8705, 9449, 7519, 7515, 7516, 7517) verified at rfc-editor.org. The Anderson report is dated October 1972 (DTIC AD0758206, ESD-TR-73-51), as the text says.

## Priority

P1: the foundational entry that every later entry refers back to.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| P1 | Should fix | `:3` | publishing | Description 237 characters and a list of sections. |
| P2 | Should fix | ten H2 headings | language | Title case. |
| P3 | Should fix | lines 559–567 | evidence | No References list; bare RFC numbers; works named in the text are not listed. |
| D1 | Should fix | §11, line 557 | structure | Summary does not lead to the next entry. |
| D2 | Should fix | lines 146, 176 | consistency | Forward references to later entries unlinked. |
| C1 | Should fix | lines 23, 31, 88, 124, 205, 207, 255, 294, 309 | language | Abbreviations not expanded at first use: WHATWG, US, PIN, QUIC, OASIS, OWASP (expanded after its use), PKCE (used at 255, expanded at 259), JWT, SAML. |
| C2 | Should fix | lines 21, 37, 146, 290 | language | Sentences of 52–79 words. |
| C3 | Optional | lines 286, 309, 518 | language | "actually"; British "organisation". |
| D3 | Optional | line 21 | structure | Prose table of contents in the opening. |
| C4 | Optional | line 141 | accuracy | The example "random" session identifier decodes to the English text "Choose a random value"; harmless, but it contradicts the point the paragraph makes. |

### P1. Description
- **Text:** "A top-down account of access control in networked systems: the reference monitor, authentication and sessions, authorization models, delegation with OAuth 2.0 and OpenID Connect, and the design, validation and lifecycle of access tokens."
- **Correction:** "Learn how networked systems decide who is asking and what they may do, from the reference monitor to OAuth 2.0, OpenID Connect and validating access tokens." (one sentence, under 165 characters).

### P3. References
- **Where:** lines 559–567, "### The specifications"
- **Text:** "OAuth 2.0: RFC 6749 (framework), RFC 6750 (bearer tokens), RFC 7636 (PKCE), ..."
- **Problem:** Standards 6.2 item 7 and 7.3: a `### References` list in house format, one entry per work, alphabetical, with authors, title and year. Works cited in the text (Anderson 1972; Saltzer and Schroeder 1975) are missing.
- **Correction:** Replace with `### References` in house format, every RFC verified at rfc-editor.org/info/rfcNNNN (authors, title, year), plus Anderson (DTIC), Saltzer and Schroeder (*Proc. IEEE* 63(9):1278–1308, per the MIT 6.033 reading list), OpenID Connect Core 1.0 errata set 2 (openid.net), the cookie revision draft (datatracker, draft-ietf-httpbis-rfc6265bis-22), XACML 3.0 (OASIS, 22 January 2013).

### D1. Summary ending
- **Text:** "The recurring lessons are short. ... and how it is withdrawn."
- **Correction:** Add a closing paragraph that leads to the second entry (linked): the authenticators that §2 treated as a single box.

### D2. Unlinked cross-references
- **Text:** "The third entry treats both attacks in detail." (146); "Later entries in this series treat them in detail" (176).
- **Correction:** Link `/blog/sessions-and-cookies#5-cross-site-request-forgery` and `/blog/sender-constrained-tokens`.

### C1. Abbreviations
- **Correction:** "Web Hypertext Application Technology Working Group (WHATWG)"; "United States Air Force"; "personal identification number (PIN)"; "QUIC, a transport protocol that runs over UDP"; "the Organization for the Advancement of Structured Information Standards (OASIS)"; "the Open Worldwide Application Security Project (OWASP)" before its first use; line 255 "Proof Key for Code Exchange (PKCE)"; line 294 "JSON Web Token (JWT)"; line 309 "Security Assertion Markup Language (SAML) 2.0".

### C2. Long sentences
- **Text (146):** "`Secure` restricts the cookie to HTTPS; `HttpOnly` hides it from page scripts, so a cross-site scripting (XSS) bug, ... carries the user's cookie." (79 words)
- **Correction:** Split into one sentence per attribute.

## Revision log (wave 1)
- Structure: Summary (§11) now ends with a paragraph leading to the second entry (linked) (D1). Opening: the long sentence split; one sentence added on what the entry assumes and that later entries go deeper.
- Prose: long sentences split at lines 37 (Saltzer and Schroeder), 124 (HTTP/2 and HTTP/3), 146 (cookie attributes, now one sentence per attribute), 205 (XACML: PEP and PDP now separate sentences), 290 (deprecated grants). "actually" removed. §4.3: the OWASP sentence rewritten so the organization is named and expanded before its list ("head the 2023 list of the ten most serious API security risks ...").
- Terminology/style: all ten H2 headings in sentence case (anchors unchanged, since slugs are lower case); abbreviations expanded at first use: WHATWG, PIN, OASIS, OWASP, PKCE (now at §5.3, its first use), JWT (§5.5), SAML, HMAC (§6.4); "US Air Force" → "United States Air Force"; "organisation" → "organization" in prose and in the `can_view` pseudocode.
- Metadata: description 163 characters, one sentence. `updatedAt: 2026-10-13` was already present (and in the Vietnamese file).
- References: "### The specifications" replaced by `### References`, 23 entries in house format, alphabetical. Every RFC's authors, title and year checked at rfc-editor.org/info/rfcNNNN; Anderson (DTIC AD0758206: vol. I, ESD-TR-73-51, October 1972); Saltzer and Schroeder (MIT 6.033 reading list: *Proc. IEEE* 63(9):1278–1308, September 1975); OpenID Connect Core 1.0 errata set 2 (openid.net, 15 December 2023); draft-ietf-httpbis-rfc6265bis-22 (datatracker, 1 December 2025, in the RFC Editor queue); XACML 3.0 (oasis-open.org, OASIS Standard 22 January 2013); "OWASP Top 10 API Security Risks – 2023" (api-security.owasp.org).
- Cross-references: links added to the third entry (§5) and the sixth entry; the closing paragraph links the second entry.
- Technical corrections: none needed.
- Remaining suggestions and why they stay: line 146 "52-word sentence" is a splitter artifact (it joins sentences that begin with inline code; the longest real sentence there is 33 words); HS256 and SHA-256 are algorithm names, HS256 is explained in the same sentence; ESD and TR are part of a report number in the reference list.
- Flags for independent review: (fact-check) Saltzer and Schroeder volume/issue/pages taken from the MIT 6.033 reading list, not from IEEE Xplore (not reachable); OWASP reference has no named authors (organization only). (technical) none.
- Vietnamese translation affected: yes, but only lightly in meaning: new closing paragraph of §11 leading to entry 2; one added sentence at the end of the opening's second paragraph; §4.3 OWASP sentence reworded; References replace "The specifications" (new works listed: Anderson, Saltzer and Schroeder, XACML, OWASP, the cookie draft).

## Independent review (wave 2)

- Report: `reviews/identity-and-access-control.md`
- Fact-check: pass
- Technical: pass
- Findings: S1 (should fix, Vietnamese translation only)
- Not verified: Saltzer and Schroeder volume, issue and pages not confirmed from a primary page (IEEE Xplore unreachable); consistent with all secondary listings.

## Revision log (wave 2 resolution)

- No English change. Vietnamese (S1): closing paragraph leading to the next entry, References, description.
- Lint: `eos lint identity-and-access-control` 0 errors, 0 warnings (suggestions only, none on the changed lines). Syntax: `eos syntax` "All files compile"; Vietnamese MDX compiled with @mdx-js/mdx.
- Vietnamese translation: updated in this resolution (scope S1); copied front-matter fields unchanged.
