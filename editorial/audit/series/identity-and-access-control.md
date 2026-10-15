# Series audit: Identity and Access Control

- Series: `identity-and-access-control`, 7 entries, status published, no planned entries
- Audited at commit `e21dcc8`, 2026-10-13. The second-pass series review (`reviews/identity-and-access-control.md`, F1–F14) is resolved in the text; nothing below undoes it.

## Structural consistency across entries

| Entry | Numbered sections | Opening links what it builds on | Summary | Closing leads on | References | Description (chars) |
|---|---|---|---|---|---|---|
| 1 token-based-authentication | Yes (§1–§11) | n/a (first) | §11, table + lessons | No | "The specifications" (RFC numbers only) | 237 |
| 2 authenticators-passwords-otp-passkeys | Yes (§1–§8) | Names entry 1, unlinked | §8, Q&A table | Yes | "The specifications" | 204 |
| 3 sessions-and-cookies | Yes (§1–§10) | Names entry 2, unlinked | §10, Q&A table | Yes | "The specifications" | 260 |
| 4 authorization-models | Yes (§1–§7) | Names entries 1–3, unlinked | §7, Q&A table | Yes | "References" (not house format) | 264 |
| 5 oauth-grants-and-client-types | Yes (§1–§8) | Names entry 1, unlinked | §8, Q&A table | Yes | "The specifications" | 283 |
| 6 sender-constrained-tokens | Yes (§1–§6) | Names entries 1 and 5, unlinked | §6, Q&A table | Yes | "The specifications" | 278 |
| 7 service-to-service-authentication | Yes (§1–§8) | "earlier entries", unlinked | §7 table, then §8 series recap | Series recap is in §8, after the Summary | "References" under §8 (not house format) | 326 |

Systemic problems:

1. **No internal links at all.** A grep of `src/` finds no link to any of the seven slugs, although the entries refer to one another about 40 times ("the first entry", "Section 5.5 of the first entry", "the third entry"). Standards 8.1 requires the first mention of another entry to be linked, and 6.2 requires the opening to link what the entry builds on. Every other series on the site links its entries.
2. **References.** Six of seven entries have "### The specifications" instead of References; none is in the house format of standards 7.3; works named in the text (Anderson 1972, Saltzer and Schroeder 1975, OpenID Connect Core, XACML, NIST SP 800-63B) are listed without authors or years, or not at all.
3. **Headings.** 47 H2 headings in title case across the series; duplicate H3 headings in entries 3 and 4.
4. **Descriptions.** All seven exceed 165 characters (204–326) and each is a list of the sections.
5. **Abbreviations.** Each entry uses some of PKCE, JWT, URI, HMAC, SHA, PIN, CORS before expanding them, because the expansion lives in an earlier entry; standards 5.3 asks for expansion at first use in each article.
6. **Endings.** Entry 1's Summary does not lead to entry 2; entry 7 closes the series in a section after its Summary and without reference to the objectives.

## Notation and terminology

Consistent: the same illustrative issuer (`https://id.example.com`), subject (`user-48213`), client (`photo-printer`), code and verifier across entries 1, 5 and 6; timestamps on 2026-10-12 in all JWT examples (recomputed); "bearer token", "sender-constrained", "resource server", "authorization server" used identically. HTTP/1.1 syntax convention is stated once (entry 1 §3.1) and repeated in entries 3, 5 and 6 as the series review asked. Minor: British "organisation" in entries 1, 4 and 7 (prose and pseudocode) against American "organization" elsewhere.

## Overlap and gaps

- Planned overlap, handled by reference: entry 1 gives the overview of each topic and later entries go deeper, saying so ("The first entry presented authorization models as rows in a table").
- The OWASP API Security Top 10 and the BOLA example appear in entry 1 §4.3 and entry 1 §9; entry 4 §6.1 refers back rather than repeating. Good.
- No gap against the four objectives (the series review's coverage table still holds). Entries 2, 6 and 7 deliver outcomes that no objective names (see the overview audit, D3).

## Overview page (standards 6.5)

Fails three of five requirements: no sequence rationale, no prerequisites, no shared conventions; objectives do not cover entries 2, 6 and 7. See `editorial/audit/items/series-identity-and-access-control.md`.

## Cross-references

Every ordinal reference ("the first/second/.../sixth entry") and every "Section x.y of the first entry" was checked against the target: all correct (for example entry 5 line 85 "Section 8 of the first entry and Section 6 of the third entry" both treat token storage and XSS; entry 4 line 216 "Section 5.2 of the first entry" is the scopes paragraph). `eos lint` reports no `series-crossref` or `section-reference` problems.

## Facts that changed since publication

- NIST SP 800-63B revision 3, cited by entry 2, was withdrawn on 1 August 2025 and replaced by SP 800-63B-4 (July 2025); the statements still hold under revision 4.
- OAuth 2.0 for Browser-Based Applications, described by entry 5 as in progress, was published as RFC 10017 in August 2026.
- WebAuthn Level 3, cited by entry 2, became a W3C Recommendation on 25 August 2026.
