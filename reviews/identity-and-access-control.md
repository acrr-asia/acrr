# Series review: Identity and Access Control

- Series: `identity-and-access-control` (7 articles, status published, 0 planned entries)
- Reviewed commit: 841f4e6
- Date: 2026-10-13

## Summary

The series is technically sound, consistently structured and moves from the general to the specific as its introduction promises. Every cross-reference between entries resolves to the section it names, every "next entry" pointer matches the actual next article, and every promise of later coverage is fulfilled. All recomputable values agree with each other and with their sources (PKCE, Basic credentials, the DPoP thumbprint and token hash, HOTP/TOTP test vectors, timestamps). No statement was found to be wrong outright, so there are no blocking findings. Five statements are imprecise or inconsistent:
- an overstated staleness window;
- an OTP guessing probability that ignores the article's own acceptance window;
- an overstated rule for when browsers send `Origin` and `Sec-Fetch-Site`;
- a question order that does not match its own flowchart;
- a stray "checkout" service that contradicts the article's own example.

The third objective (OpenID Connect) is only partly met, and three spellings break the series' `authorization` convention. The series is ready as published; the should-fix items are worth correcting in one editing pass.

Findings: 0 blocking, 7 should fix, 4 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Separate identification, authentication, authorization and audit, and say which mechanism answers which question. | Entry 1 §1.2 (four stages), §11 (layer table); entry 7 §8 | Met. Entry 1 calls the fourth stage "Accountability" while the objective and entry 7 say "audit" (F11). |
| Compare server-side sessions with self-contained tokens in terms of where state lives, how revocation works and what a verifier needs. | Entry 1 §3.3–3.5, §7.1; entry 3 §1.1–1.3, §7.3 | Met. The comparison table in entry 1 §3.5 states all three dimensions explicitly. |
| Explain delegated authorization with OAuth 2.0 and federated authentication with OpenID Connect, including why public clients need PKCE. | Entry 1 §5.1–5.6; entry 5 (whole) | Partly met. OAuth 2.0 and PKCE are treated in depth (entry 5 §1.2, §3.2). OpenID Connect is explained only conceptually in entry 1 §5.5–5.6; no entry says how a client validates an ID token or identifies the user, although every other layer of the series receives a deeper treatment (F6). |
| Validate an access token correctly and enforce object-level authorization at the resource server. | Entry 1 §6.5, §9; entry 4 §6.1–6.2; entry 6 §3.4 | Met. |

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Should fix | `src/content/blog/token-based-authentication.mdx` | §7.1 (line 417) | Technical accuracy | The staleness window is said to equal the token lifetime; it is at most the lifetime, as the article's own example shows |
| F2 | Should fix | `src/content/blog/authenticators-passwords-otp-passkeys.mdx` | §3.3 (line 122) | Technical accuracy | The OTP guessing probability ignores the ±1 step acceptance window stated in §3.2 |
| F3 | Should fix | `src/content/blog/sessions-and-cookies.mdx` | §5.3 (line 182) | Technical accuracy | Overstates when browsers send `Origin` and `Sec-Fetch-Site` |
| F4 | Should fix | `src/content/blog/oauth-grants-and-client-types.mdx` | Introduction (line 17) vs §7 (lines 258–266) | Logical flow | The three grant-selection questions are listed in a different order from the flowchart that applies them |
| F5 | Should fix | `src/content/blog/service-to-service-authentication.mdx` | §5.3 (line 161) | Factual consistency | "Only checkout may obtain payments tokens" contradicts the article's own orders→payments example |
| F6 | Should fix | `src/content/blog/oauth-grants-and-client-types.mdx` (series-level) | §3 (after line 158) | Completeness | Objective 3 is only partly met: ID token validation and stable user identification are never explained |
| F7 | Should fix | `token-based-authentication.mdx`, `service-to-service-authentication.mdx` | Lines 309, 313; line 40 | Terminology | "Authorise"/"authorised" break the series' spelling of `authorization`/`authorize` (used over 140 times) |
| F8 | Optional | `src/content/blog/token-based-authentication.mdx` | Lines 21, 35, 63, 106, 168, 535 | Writing quality | Entry 1 calls itself "this chapter" while every other entry, including references to entry 1, says "entry" |
| F9 | Optional | `token-based-authentication.mdx`, `oauth-grants-and-client-types.mdx` | Line 147; line 231 | Factual consistency | Example access tokens decode to headers without `typ: at+jwt`, which the series says resource servers should check |
| F10 | Optional | `src/content/blog/sessions-and-cookies.mdx` | §10 (line 258) | Completeness | The summary says the identifier "is never logged"; the body never states that rule |
| F11 | Optional | `src/content/blog/token-based-authentication.mdx` | §1.2 (line 46) | Terminology | The stage named "Accountability" is called "audit" in the series objective and in entry 7 |

### F1. The staleness window is at most, not exactly, the token lifetime
- **Where:** `src/content/blog/token-based-authentication.mdx:417`, section "7.1 Expiry and the staleness window"
- **Text:** "That interval is the **staleness window**, and its length equals the access-token lifetime."
- **Problem:** The window runs from the account change to the token's `exp`, so its length depends on when the token was issued. It equals the lifetime only if the change happens at the moment of issue. The article's own example (disabled at 10:00, token expires at 10:08) gives a window of 8 minutes, not a full lifetime.
- **Recommended correction:** "That interval is the **staleness window**, and it can be as long as the access-token lifetime."

### F2. OTP guessing probability ignores the acceptance window
- **Where:** `src/content/blog/authenticators-passwords-otp-passkeys.mdx:122`, section "3.3 What a one-time code adds, and what it does not"
- **Text:** "With six digits there are $10^6$ possible codes, so an online guesser allowed five attempts per code has a $5 / 10^6$ chance per code; the verifier must still rate-limit, or an attacker can simply try many codes."
- **Problem:** §3.2 (line 118) says the verifier "typically accepts one step either side of the current one". Three codes are then valid at any moment, so each guess succeeds with probability about $3/10^6$, and five guesses with about $15/10^6$. The figure as written understates the risk by a factor of three. "Per code" is also ambiguous: the attacker's limit is per time step or per account.
- **Recommended correction:** "With six digits there are $10^6$ possible codes. A verifier that accepts one step either side of the current one has three valid codes at any moment, so an online guesser allowed five attempts per time step succeeds with probability of about $15 / 10^6$ per step. The verifier must therefore rate-limit across steps too, or an attacker can simply keep trying."

### F3. When browsers send `Origin` and `Sec-Fetch-Site`
- **Where:** `src/content/blog/sessions-and-cookies.mdx:182`, section "5.3 Request-level defences"
- **Text:** "Browsers send an `Origin` header on cross-origin and on `POST` requests, and modern browsers send `Sec-Fetch-Site` (`same-origin`, `same-site`, `cross-site` or `none`) on every request."
- **Problem:** The WHATWG Fetch standard does not attach `Origin` to every cross-origin request. It is sent with CORS requests and with requests whose method is not `GET` or `HEAD`. A cross-origin image load or a top-level `GET` navigation carries no `Origin`. Fetch metadata headers (`Sec-Fetch-*`) are sent only to potentially trustworthy (HTTPS) URLs, not on every request. The defence the paragraph recommends is still right, but a reader who relies on `Origin` for a state-changing `GET` would be unprotected; the article warns against such endpoints elsewhere (§3.2, §5.2).
- **Recommended correction:** "Browsers send an `Origin` header on every request whose method is not `GET` or `HEAD`, and on cross-origin requests made with CORS. Modern browsers also send `Sec-Fetch-Site` (`same-origin`, `same-site`, `cross-site` or `none`) on requests to HTTPS origins. A server can reject state-changing requests whose `Sec-Fetch-Site` is `cross-site`, or whose `Origin` is not its own, at very low cost."

### F4. Grant-selection questions out of order
- **Where:** `src/content/blog/oauth-grants-and-client-types.mdx:17`, introduction; flowchart at lines 258–266, section "7. Choosing a Grant"
- **Text:** "a grant is chosen by answering three questions about the situation, in order: *Is there a user?* *Can the client keep a secret?* *Can the user reach a browser on the device where the client runs?*"
- **Problem:** The flowchart asks "Is a user involved?", then "Can the user use a browser on the device running the client?", then "Can the client keep a secret?". The introduction says "in order" but gives a different order, so the organising idea of the entry and its conclusion disagree.
- **Recommended correction:** "a grant is chosen by answering three questions about the situation, in order: *Is there a user?* *Can the user reach a browser on the device where the client runs?* *Can the client keep a secret?*"

### F5. "Checkout" contradicts the orders→payments example
- **Where:** `src/content/blog/service-to-service-authentication.mdx:161`, section "5.3 Delegation chains"
- **Text:** "orders may obtain inventory tokens for users, inventory may obtain pricing tokens, and nothing may obtain tokens for the payments service except checkout."
- **Problem:** No checkout service appears anywhere else in the series. The same article says "the orders service may call `POST /payments`" (§4, line 105) and builds the confused-deputy example on "the orders service calls the payments service on behalf of a user" (§5.1, lines 115–117). Under the stated rule, that call could not obtain a token.
- **Recommended correction:** "orders may obtain inventory and payments tokens for users, inventory may obtain pricing tokens, and no other service may obtain tokens for the payments service."

### F6. OpenID Connect is not taken beyond the overview
- **Where:** series level. Entry 1 §5.5–5.6 (`src/content/blog/token-based-authentication.mdx:284-301`) is the only treatment; the natural place to extend it is entry 5, `src/content/blog/oauth-grants-and-client-types.mdx`, after §3.3 (line 158).
- **Text:** Objective 3: "Explain delegated authorization with OAuth 2.0 and federated authentication with OpenID Connect, including why public clients need PKCE."
- **Problem:** The series introduction promises that "each later entry takes one layer of that picture and goes further into it". Every layer gets that deeper treatment except OpenID Connect. No entry explains how a client validates an ID token (signature, `iss`, `aud`/`azp`, `exp`, `nonce`) or which claims identify the user. Those are the steps a client must get right for federated sign-in to be secure, and the access-token equivalent receives an eight-step procedure (entry 1 §6.5).
- **Recommended correction:** add to entry 5, after §3.3 (and renumber the current §3.4 to §3.5):

  ```markdown
  ### 3.4 Signing the user in: the ID token

  When the client includes the `openid` scope (and a fresh `nonce`) in the authorization request, the token response also contains an ID token (Section 5.5 of the first entry). Before treating the user as signed in, the client validates it as OpenID Connect Core requires:

  1. Verify the signature with a key from the provider's published key set, using the algorithm registered for the client.
  2. Check that `iss` equals the provider's issuer identifier exactly.
  3. Check that `aud` contains the client's own `client_id`; if it lists other audiences as well, check that `azp` is the client's `client_id`.
  4. Check that `exp` is in the future and that `iat` is recent.
  5. Check that `nonce` equals the value the client sent in the authorization request for this sign-in.

  Only then does the client identify the user, by the pair of `iss` and `sub`. Claims such as an email address are profile data, not stable identifiers: an address can be reassigned, and two providers can assert the same one.
  ```

  Add a summary row: "| How does a client sign a user in with OpenID Connect? | By validating the ID token (signature, `iss`, `aud`, `exp`, `nonce`) and identifying the user by `iss` and `sub`. |". Add "OpenID Connect Core 1.0" to the specifications list.

### F7. "Authorise" and "authorised" break the series' spelling
- **Where:** `src/content/blog/token-based-authentication.mdx:309` and `:313`, section "6.1 Kinds of token"; `src/content/blog/service-to-service-authentication.mdx:40`, section "2.1 What a workload identity names"
- **Text:** "| Access token | Client | Resource server | Authorise specific requests within scopes and a lifetime |"; "| Single-purpose token | ... | Authorise one operation, ..."; "what it is and where it is authorised to run"
- **Problem:** The series otherwise uses British spelling (organisation, standardised, synchronised) but always spells the central term with a z: `authorization`/`authorize`/`authorized`, 140+ times, matching the OAuth and RFC terminology. Entry 7 uses both spellings within its first 40 lines ("are authorized", line 18; "authorised", line 40).
- **Recommended correction:** line 309: "Authorize specific requests within scopes and a lifetime"; line 313: "Authorize one operation, such as a password reset or email verification"; entry 7 line 40: "what it is and where it is authorized to run".

### F8. Entry 1 calls itself a chapter
- **Where:** `src/content/blog/token-based-authentication.mdx:21`, `:35`, `:63`, `:106`, `:168`, `:535`
- **Text:** "This chapter therefore works from the general to the specific."; "The rest of the chapter uses the following terms precisely."
- **Problem:** Every other entry refers to itself as "this entry" and to this article as "the first entry"; the series page calls them entries. The book-chapter style is deliberate and should stay; only the word is inconsistent.
- **Recommended correction:** Replace "chapter" with "entry" in the six places listed, for example "This entry therefore works from the general to the specific." and "The rest of the entry uses the following terms precisely."

### F9. Example access tokens lack the `at+jwt` type the series tells servers to require
- **Where:** `src/content/blog/token-based-authentication.mdx:147`, section "3.4 Strategy three"; `src/content/blog/oauth-grants-and-client-types.mdx:231`, section "5.2 Token exchange"
- **Text:** "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImsxIn0.eyJzdWIiOi..."; "&subject_token=eyJhbGciOiJSUzI1NiJ9..."
- **Problem:** The headers decode to `{"alg":"RS256","kid":"k1"}` and `{"alg":"RS256"}`. Entry 1 §6.3 and §6.5 step 7 say an access token carries `typ: at+jwt` and that resource servers should check it, so these examples would fail the series' own validation. Entry 5 line 150 already uses a correct prefix (`{"alg":"RS256","typ":"at+jwt"}`).
- **Recommended correction:** In both places, start the token with `eyJhbGciOiJSUzI1NiIsInR5cCI6ImF0K2p3dCJ9.` (which decodes to `{"alg":"RS256","typ":"at+jwt"}`), for example `Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6ImF0K2p3dCJ9.eyJzdWIiOi...` and `&subject_token=eyJhbGciOiJSUzI1NiIsInR5cCI6ImF0K2p3dCJ9...`.

### F10. "Never logged" appears only in the summary
- **Where:** `src/content/blog/sessions-and-cookies.mdx:258`, section "10. Summary"
- **Text:** "| How is it protected at rest? | It is never logged and is stored on the server only as a hash. |"
- **Problem:** The body explains hashing (§1.2, line 41) and mentions that session tables are copied into logs, but never states the rule that the identifier itself must not be logged. A summary should not introduce a requirement.
- **Recommended correction:** At the end of line 41, add: "For the same reason, the identifier itself should never be written to logs, error reports or analytics events."

### F11. "Accountability" versus "audit"
- **Where:** `src/content/blog/token-based-authentication.mdx:46`, section "1.2 Four distinct questions"
- **Text:** "| Accountability | What happened, and who did it? | Audit logs that record the authenticated subject and the decision |"
- **Problem:** The series objective ("identification, authentication, authorization and audit") and entry 7 §8 (line 197, "the separation of authentication, authorization and audit") name the fourth stage "audit". The two words are close, but a reader mapping the objective to the article meets a different term.
- **Recommended correction:** Rename the stage "Accountability (audit)" in the table.

## Series-level notes

**Cross-reference map.** Every inter-entry reference was checked against its target, and all resolve:
- Entry 2 → entry 1 (claimant/verifier, carrying forward).
- Entry 3 → entry 1 (reference vs value, federated logout §7.3) and entry 2.
- Entry 4 → entry 1 (§4.2 table, fail-safe defaults §1.1, PEP/PDP §4.3, BOLA §4.3, scopes "Section 5.2 of the first entry").
- Entry 5 → entry 1 (refresh, "Section 8 of the first entry"), entry 2 (asymmetric vs shared secrets) and entry 3 ("Section 6 of the third entry").
- Entry 6 → entries 1, 3 and 5.
- Entry 7 → entries 1, 4, 5 and 6.

All five "the next entry …" sentences describe the actual next article. The forward promises are fulfilled:
- entry 1 §3.6 → entry 6;
- entry 3 §8 → entry 6;
- entry 5 §1.3 → entry 6;
- entry 5 §5.2 → entry 7 §5.

All internal section references (for example "Section 6.5", "Section 4.3", "Section 2.4", "Section 3.5") point to sections that exist and say what is claimed.

**Terminology.** Defined terms are used consistently across entries:
- reference/value token;
- bearer/sender-constrained;
- confidential/public client;
- relying party (entry 1 vocabulary) and relying party ID (the WebAuthn term, entry 2);
- staleness window;
- policy enforcement/decision/information point;
- confused deputy.

Abbreviations are expanded on first use in each entry. Spelling is British apart from the deliberate `authorization`/`authorize` family; F7 lists the exceptions.

**Structure and tone.** Each entry opens by connecting to its predecessor, numbers its sections, and ends with a summary table and either "The specifications" (standards) or "References" (papers: entries 4 and 7). Tone and depth are even across the series; no material is repeated beyond deliberate one-line recaps.

**Frontmatter.** Category (`Computing Systems`), `series` and `seriesOrder` (1–7, contiguous) are consistent. Entry 1 alone carries `draft: false` (the default) and `updatedAt`, which is harmless. Tags differ by topic, as expected.

**Content rules.**
- No fabricated statistics, results, quotations or URLs; numerical examples are labelled illustrative, or are the RFC sample values and say so (entry 6 §1.2).
- No external links; standards are cited by number or title.
- English only.
- Nothing is labelled as example content, and none needs to be.

## Verification log

- `npm run build:local`: passed. `astro check` reported 0 errors and 0 warnings, the build completed, and Pagefind indexed 24 pages. The expected localhost warning appeared because `SITE_URL` was not set.
- `npm run check:links`: passed. It checked 72 pages and 1664 internal references; all resolve.
- Mermaid widths in `dist/blog/*.html`, all under 600px: entry 1: 357, 426, 340, 431px; entry 2: 344px; entry 3: 331, 336px; entry 4: 441, 350px; entry 5: 344, 469px; entry 6: 331px; entry 7: 428, 126px.
- Text glued to inline elements: none found in the seven pages.
- Recomputed:
  - PKCE: S256 of `dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk` = `E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM` (entry 5 line 116). Matches.
  - Basic credentials: base64 of `photo-printer:example-secret` = `cGhvdG8tcHJpbnRlcjpleGFtcGxlLXNlY3JldA==` (entry 5 line 134). Matches.
  - DPoP `ath`: SHA-256 of `Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU` = `fUHyO2r2Z3DZ53EsNrWBb0xWXoaNy59IiKCAqksmQEo` (entry 6 line 137). Matches.
  - DPoP `jkt`: RFC 7638 thumbprint of the entry 6 key = `0ZcOCORZNYy-DWpqq30jZyJGHTN0d2HglBV3uiguA4I` (entry 6 line 44). Matches.
  - JWT header prefixes decoded:
    - entry 1 line 147: `{"alg":"RS256","kid":"k1"}` (see F9);
    - entry 5 line 150: `{"alg":"RS256","typ":"at+jwt"}`;
    - entry 5 line 183: `{"alg":"ES256"}`;
    - entry 5 line 231: `{"alg":"RS256"}` (see F9);
    - entry 6 line 160: `{"typ":"dpop+jwt","alg":"ES256","jwk":{...}}`.
  - Timestamps:
    - 1791795600 = 2026-10-12T09:00:00Z and 1791796200 = 09:10:00Z, 600 s apart, matching "ten minutes apart" (entry 1 line 350);
    - entry 6 `iat` 1791795700 (09:01:40Z) and entry 7 `exp` 1791795900 (09:05:00Z) are consistent with them.
  - HOTP truncation as described in entry 2 §3.1 reproduces RFC 4226 Appendix D (755224, 287082, 359152 for C = 0, 1, 2), and TOTP with a 30 s step reproduces the RFC 6238 SHA-1 vector for T = 59 (94287082).
  - Session identifiers:
    - entry 3's sample `Vb9xQm4tR2kz8YpLw7nJcA` is 22 base64url characters (132 bits of encoding, consistent with a 128-bit identifier as recommended);
    - entry 1's sample `Q2hvb3NlIGEgcmFuZG9tIHZhbHVl` decodes to the placeholder text "Choose a random value", a harmless illustration.
  - Mobility and other formulas: none in this series beyond the above.
- Not verified:
  - Citations (RFC numbers and titles, NIST SP 800-63B / 800-162 / 800-207, OWASP API Security Top 10 2023, ANSI INCITS 359-2004, and the dates and venues of the Lampson, HRU, Ferraiolo–Kuhn, Sandhu, Hardy and Zanzibar papers) were checked against the reviewer's knowledge of those documents, not re-read from the sources in this run.
  - Browser behaviour that varies by vendor and version (the default `SameSite` treatment, Token Binding support, Device Bound Session Credentials) was likewise not re-tested.
