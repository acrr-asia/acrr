# Series review: Identity and Access Control

- Series: `identity-and-access-control` (7 articles, status published, 0 planned entries)
- Reviewed commit: 2e79a4b (series content as revised in wave 1, commit 49941d2)
- Date: 2026-10-15
- Review type: independent review (wave 2) of the wave-1 revision (audit logs in `editorial/audit/series/identity-and-access-control.md` and `editorial/audit/items/`), combining fact-check (F), technical review (T) and series review (S). The reviewer did not write or revise any of the text. This report replaces the earlier second-pass report (commit 6e6f2ee) and its Resolution and stamp.

## Summary

The series is accurate, well ordered and consistent, and the wave-1 revision improved it without damaging its substance. The dated facts that wave 1 updated were checked against the primary sources and hold: SP 800-63B-4 (July 2025) and the withdrawal of revision 3 on 1 August 2025; RFC 10017 (Best Current Practice, August 2026), including its description of the token-mediating back end; WebAuthn Level 3 as a W3C Recommendation of 25 August 2026; and RFC 8471–8473 still listed as Proposed Standard. Every worked value was recomputed and is correct: the PKCE challenge, the DPoP `jkt` and `ath`, the Basic credentials, the JWT segments and timestamps, and the TOTP guessing probability. No HOTP vector is printed in the text, so the HOTP definition was checked by running it against the RFC 4226 vectors. Every new reference exists with the stated authors, title and year. The build, links and rendering of the seven pages are clean, and `eos lint` reports no errors or warnings.

Four points need fixing. Entry 5 gives the ID-token `azp` rule from before errata set 2 of OpenID Connect Core, although it cites errata set 2 (F1). Entry 2 says it follows SP 800-63B-4, but it presents email codes alongside SMS codes without saying that revision 4 forbids email for out-of-band authentication (F2). Entry 2 also states the relying party ID rule without the related-origins exception that the Level 3 Recommendation it follows adds (T1). Finally, wave 1 changed the meaning of several English files without updating their Vietnamese translations, and one translation now carries a dated fact that is no longer true (S1). Four optional items follow. Once the four should-fix findings are resolved, the series is ready.

Findings: 0 blocking, 4 should fix, 4 optional.

## Objectives coverage

| Objective (from the series file) | Covered by | Assessment |
|---|---|---|
| Separate identification, authentication, authorization and audit, and say which mechanism answers which question. | Entry 1 §1.2 (four stages), §4.4 (401 and 403), §11 (layer table) | Met. |
| Evaluate authenticators by their resistance to online guessing, verifier compromise, replay and phishing, and explain why origin-bound public-key credentials resist phishing. | Entry 2 §1.2–1.3 (the four properties), §2–§5, §6 (comparison table), §5.4 (why origin binding resists phishing) | Met. This confirms the wave-1 flag on the new objective 2. The §5.4 explanation needs the precision in T1. |
| Compare server-side sessions with self-contained tokens in terms of where state lives, how revocation works and what a verifier needs. | Entry 1 §3.3–3.5 (reference versus value table), §7.1; entry 3 §1.1–1.3, §7.3 | Met. |
| Explain delegated authorization with OAuth 2.0 and federated authentication with OpenID Connect, including why public clients need PKCE. | Entry 1 §5; entry 5 §1.2, §3 (PKCE in §3.2, ID token in §3.4) | Met. The ID-token validation steps need the correction in F1. |
| Validate an access token correctly and enforce object-level authorization at the resource server. | Entry 1 §6.5, §9; entry 4 §6.1–6.2; entry 6 §3.4 | Met. |
| Design authentication between services with workload identities, sender-constrained tokens and per-hop token exchange instead of network location, forwarded tokens or trusted headers. | Entry 6 (whole); entry 7 §1–§5 (network location §1, workload identity §2, mutual TLS and tokens §3, token exchange and the comparison with trusted headers and forwarded tokens §5.2–5.3) | Met. This confirms the wave-1 flag on the new objective 6. |

The objectives paragraph that wave 1 added to entry 7's Summary (`service-to-service-authentication.mdx:203`) maps each of the six objectives to the entries above and agrees with this table.

## Findings

| ID | Severity | Article | Location | Dimension | Finding |
|---|---|---|---|---|---|
| F1 | Should fix | `src/content/blog/oauth-grants-and-client-types.mdx` | §3.4 (line 168) | Technical accuracy / evidence | The `azp` rule for multi-audience ID tokens is the one that OpenID Connect Core errata set 2 removed; the entry cites errata set 2. |
| F2 | Should fix | `src/content/blog/authenticators-passwords-otp-passkeys.mdx` | §3.4 (line 133); §6 table (line 225) | Factual consistency | The entry follows SP 800-63B-4, which says email "SHALL NOT be used for out-of-band authentication", but treats email codes alongside SMS codes without saying so. |
| T1 | Should fix | `src/content/blog/authenticators-passwords-otp-passkeys.mdx` | §5.4 (line 192) | Technical accuracy / stated versions | The relying party ID rule is stated without the related-origins exception of WebAuthn Level 3, the version the entry says it follows. |
| S1 | Should fix | Vietnamese translations of the series file and entries 1, 2, 5, 6 and 7 | `src/content/series/vi/identity-and-access-control.md`; `src/content/blog/vi/oauth-grants-and-client-types.mdx:79`; `src/content/blog/vi/service-to-service-authentication.mdx:193` | Fit with site rules | Wave 1 changed the English meaning and structure, but no Vietnamese file was updated. The Vietnamese entry 5 still calls the browser-based-apps guidance a draft in progress. |
| F3 | Optional | `src/content/blog/authorization-models.mdx` | §1.3 (line 48) | Evidence | Bell–LaPadula (1973) and Biba (1977) are dated attributions with no reference. |
| F4 | Optional | `src/content/blog/sessions-and-cookies.mdx` | §8 (line 235) | Factual consistency | "browser proposals such as Device Bound Session Credentials" is dated; DBSC is now a W3C Working Draft. |
| T2 | Optional | `src/content/blog/oauth-grants-and-client-types.mdx` | §3.4 (lines 164–166) | Technical accuracy | "as OpenID Connect Core requires: 1. Verify the signature" omits the TLS alternative that Core allows for ID tokens received directly from the token endpoint. |
| S2 | Optional | `src/content/blog/authorization-models.mdx` | §6.1 (line 210) | Cross-article references | "broken object-level authorization flaw (described in the first entry)" is the only back-reference in entry 4 without a link. |

### F1. The `azp` rule predates OpenID Connect Core errata set 2

- **Where:** `src/content/blog/oauth-grants-and-client-types.mdx:168`, section "3.4 Signing the user in: the ID token"
- **Text:** "3. Check that `aud` contains the client's own `client_id`; if it lists other audiences as well, check that `azp` is the client's `client_id`."
- **Problem:** The entry cites *OpenID Connect Core 1.0 incorporating errata set 2* (reference list, line 328), and introduces the steps with "the client validates it as OpenID Connect Core requires" (line 164). Errata set 2 (15 December 2023) changed this step. Section 3.1.3.7 now says, in step 3, that "The ID Token MUST be rejected if the ID Token does not list the Client as a valid audience, or if it contains additional audiences not trusted by the Client". It says, in step 4, that if extensions cause an `azp` claim to appear, the client "SHOULD validate the azp value as specified by those extensions", and in step 5 that when `azp` is present, "the Client SHOULD verify that its client_id is the Claim Value" (openid.net/specs/openid-connect-core-1_0.html, fetched 2026-10-15). The entry's rule (multiple audiences, therefore check `azp`) is the pre-errata rule. It also omits the requirement that matters for security: reject a token that names an audience the client does not trust.
- **Recommended correction:** Replace step 3 with: "3. Check that `aud` contains the client's own `client_id`, and reject the token if it also lists an audience the client does not trust. If an `azp` (authorized party) claim is present, check that it is the client's `client_id`." Apply the same change to the Vietnamese translation.

### F2. Email codes under SP 800-63B-4

- **Where:** `src/content/blog/authenticators-passwords-otp-passkeys.mdx:133`, section "3.4 Codes sent by SMS or email"; also the comparison table row "SMS / email code" (line 225)
- **Text:** "A code sent by text message (SMS, the Short Message Service) or email is not generated from a seed the user holds ... email codes are only as strong as the email account. NIST's guidelines, since the 2017 revision and still in revision 4, classify authentication over the public telephone network as *restricted*: usable, but with additional risk that the verifier must assess and disclose."
- **Problem:** The opening (line 21) says the entry follows the password guidance of SP 800-63B as revised in 2025, and §3.4 cites revision 4 for the SMS rule. The same section of revision 4 is stricter about email: "Email SHALL NOT be used for out-of-band authentication because it may be vulnerable to" access using only a password, interception in transit and rerouting attacks (SP 800-63B-4, Section 3.1.3.1; pages.nist.gov/800-63-4/sp800-63b.html, fetched 2026-10-15). The PSTN statement is correct ("Use of the PSTN for out-of-band verification is *restricted*", Section 3.1.3.3). By naming only the SMS rule, the entry implies that the cited guidance treats email codes the same way, and the table ranks the two together. What the entry says about email is true; the omission is what misleads.
- **Recommended correction:** After "...classify authentication over the public telephone network as *restricted*: usable, but with additional risk that the verifier must assess and disclose." insert: "Revision 4 goes further for email: it does not accept email as an out-of-band authenticator at all, because an email account is often protected only by a password and messages can be intercepted or rerouted." Optionally change the table row label to "SMS code (email codes are weaker still; Section 3.4)". Apply the same change to the Vietnamese translation.

### T1. The relying party ID rule in WebAuthn Level 3

- **Where:** `src/content/blog/authenticators-passwords-otp-passkeys.mdx:192`, section "5.4 Why this resists phishing"
- **Text:** "the browser will not let that page request a signature for `example.com`, because a page may only use a relying party ID equal to, or a registrable suffix of, its own domain."
- **Problem:** The entry states that it follows WebAuthn Level 3 (line 21). Level 3 keeps the base rule ("The RP ID must be equal to the origin's effective domain, or a registrable domain suffix of the origin's effective domain"), but it adds an exception. Section 5.11, "Using Web Authentication across related origins", lets a client accept an RP ID that is not a suffix of the caller's domain. It does so when the relying party lists the caller's origin in a well-known file served from the RP ID's domain (w3.org/TR/webauthn-3, Recommendation of 25 August 2026, fetched 2026-10-15). "May only" is therefore no longer exact. The phishing argument still holds, because only the relying party can publish that list, but a reader who checks the specification will find the absolute rule contradicted.
- **Recommended correction:** Replace the sentence's second half with: "because a page may use only a relying party ID equal to, or a registrable suffix of, its own domain. Level 3 adds one exception, *related origins*: a site may also accept origins that it lists itself in a file served from its own domain, which an attacker cannot edit." Apply the same change to the Vietnamese translation.

### S1. Vietnamese translations not updated after wave 1

- **Where:** `src/content/series/vi/identity-and-access-control.md` (four objectives, old body); `src/content/blog/vi/oauth-grants-and-client-types.mdx:79`; `src/content/blog/vi/service-to-service-authentication.mdx:193`; the opening paragraphs and References of the Vietnamese entries 1, 2, 3, 4 and 6
- **Text:** Vietnamese entry 5, line 79: "được mô tả trong bản hướng dẫn đang được IETF soạn thảo cho các ứng dụng chạy trên trình duyệt" ("described in the guidance for browser-based applications that the IETF is drafting"). Vietnamese entry 7, line 193: "## 8. Toàn bộ loạt bài trong một bức tranh".
- **Problem:** `git show --stat 49941d2` lists no file under `vi/`. Each wave-1 revision log marks "Vietnamese translation affected: yes". `CLAUDE.md` ("Languages") and the series-review procedure (section 6) require translations to follow the original, and the pairing check does not catch these differences. Three differences are more than wording. The Vietnamese series page lists four objectives against six. The Vietnamese entry 7 keeps the section that the English entry merged into its Summary. The Vietnamese entry 5 states as current a dated fact that is no longer true: RFC 10017 was published in August 2026 (rfc-editor.org/info/rfc10017).
- **Recommended correction:** When the findings in this report are resolved, update every Vietnamese file of the series to the revised English text, following `docs/translation-vi.md`. Start with the series file (description, six objectives, three-paragraph body), entry 5 §2.3 and its References (RFC 10017 as published), entry 7 (§8 merged into §7, the objectives paragraph, References), entry 2 (versions paragraph, revision 4 of SP 800-63B, plus F2 and T1), and then the References lists and openings of entries 1, 3, 4 and 6.

### F3. Bell–LaPadula and Biba without references

- **Where:** `src/content/blog/authorization-models.mdx:48`, section "1.3 Who may change the matrix"
- **Text:** "Bell–LaPadula (1973) protects confidentiality with the rules \"no read up, no write down\" across clearance levels, and Biba (1977) protects integrity with the reverse."
- **Problem:** The entry references every other dated work it names (Lampson, HRU, Ferraiolo and Kuhn, Sandhu, Zanzibar), but not these two. Wave 1 flagged this. The dates and the rules are correct. The primary reports exist: Bell and LaPadula, *Secure Computer Systems: Mathematical Foundations*, vol. I, The MITRE Corporation, November 1973 (DTIC AD0770768, title page fetched); Biba, *Integrity Considerations for Secure Computer Systems*, ESD-TR-76-372, The MITRE Corporation, April 1977 (CERIAS report record, fetched).
- **Recommended correction:** Add to the References, in alphabetical position: "- D. E. Bell and L. J. LaPadula, *Secure Computer Systems: Mathematical Foundations*, vol. I, The MITRE Corporation, 1973." and "- K. J. Biba, *Integrity Considerations for Secure Computer Systems*, ESD-TR-76-372, The MITRE Corporation, 1977."

### F4. Device Bound Session Credentials described as a proposal

- **Where:** `src/content/blog/sessions-and-cookies.mdx:235`, section "8. Theft after authentication"
- **Text:** "browser proposals such as Device Bound Session Credentials aim to provide it for ordinary cookies."
- **Problem:** The W3C published *Device Bound Session Credentials* as a First Public Working Draft on 21 August 2025 (w3.org/TR/dbsc, fetched). The opening (line 19) says the entry describes cookies "as current browsers implement it". Press reports say Chrome began shipping DBSC on Windows in 2026; that was not verified against a primary source, so the correction below does not rely on it.
- **Recommended correction:** "Device Bound Session Credentials, a W3C Working Draft that not every browser supports yet, aims to provide it for ordinary cookies."

### T2. The ID-token signature check and its TLS alternative

- **Where:** `src/content/blog/oauth-grants-and-client-types.mdx:164–166`, section "3.4 Signing the user in: the ID token"
- **Text:** "the client validates it as OpenID Connect Core requires: 1. Verify the signature with a key from the provider's published key set, using the algorithm registered for the client."
- **Problem:** OpenID Connect Core §3.1.3.7, step 6, allows a client that receives the ID token directly from the token endpoint over TLS to rely on TLS server validation instead of checking the signature. Verifying the signature is never wrong, so this is polish. "Requires" is slightly stronger than the source.
- **Recommended correction:** Replace "as OpenID Connect Core requires" with "following OpenID Connect Core". Optionally add after step 1: "(Core also allows a client that received the token directly from the token endpoint over TLS to rely on the TLS connection instead; checking the signature is the safer habit.)"

### S2. One unlinked back-reference

- **Where:** `src/content/blog/authorization-models.mdx:210`, section "6.1 Filtering lists"
- **Text:** "is a broken object-level authorization flaw (described in the first entry) waiting to be found."
- **Problem:** Wave 1 linked the other back-references in entry 4 (lines 16, 18, 41, 216). Standards 8.1 asks for the first mention of another entry to be linked. This mention is not the first one, so the link is polish.
- **Recommended correction:** "(described in [Section 4.3 of the first entry](/blog/token-based-authentication#43-where-decisions-are-made-and-enforced))".

## Concept introduction map

| Concept | First used (path:line) | Introduced where | Assessment |
|---|---|---|---|
| Authentication, authorization | `token-based-authentication.mdx:19` | Same place, then §1.2 | Good. |
| Reference monitor, complete mediation | `token-based-authentication.mdx:31` | `:31–37` | Good. |
| RFC, IETF, W3C, WHATWG | `token-based-authentication.mdx:23` | `:23` | Good. |
| HTTP (request, method, header, status) | `token-based-authentication.mdx:114` | `:114–116` | Good. The earlier blocking finding is resolved. |
| TLS, X.509 certificate | `token-based-authentication.mdx:102` | `:126`, with a forward pointer at `:102` | Acceptable: the forward pointer is explicit. |
| Cookie | `token-based-authentication.mdx:136` | `:136` (parenthetical); in depth in `sessions-and-cookies.mdx:49–85` | Good. |
| XSS, CSRF | `token-based-authentication.mdx:146` | `:146` | Good. |
| Scope | `token-based-authentication.mdx:187` ("the scopes granted to the client") | `:244` | Used once in a list before §5.2 defines it; the meaning is clear from context. Not a finding. |
| JSON, base64url, JWT | `token-based-authentication.mdx:150` (JWT) | `:331` (JSON and base64url defined with JWT; §3.4 points to Section 6) | Good. |
| HMAC | `token-based-authentication.mdx:378`; `authenticators-passwords-otp-passkeys.mdx:104` | Defined at each first use | Good. |
| Cryptographic hash function | `authenticators-passwords-otp-passkeys.mdx:58` | `:58` | Good. The overview names it as a prerequisite. |
| Origin, site, registrable domain | `token-based-authentication.mdx:94` (origin); `authenticators-passwords-otp-passkeys.mdx:148` | `sessions-and-cookies.mdx:95–102`; entry 2 links forward to it | Good. |
| CORS | `token-based-authentication.mdx:539`; `sessions-and-cookies.mdx:182` | `token-based-authentication.mdx:539`; `sessions-and-cookies.mdx:183` | Good. |
| Relying party ID, attestation, discoverable credential | `authenticators-passwords-otp-passkeys.mdx:147` | `:147`, `:170`, `:203` | Good. |
| Access matrix, ACL, capability | `authorization-models.mdx:24` | `:24–41` | Good. |
| Grant, client types | `oauth-grants-and-client-types.mdx:15` | `:15`, `:34–41` | Good. |
| `cnf`, JWK thumbprint | `sender-constrained-tokens.mdx:36` | `:36–50` | Good. |
| Workload identity, SPIFFE, trust domain, attestation | `service-to-service-authentication.mdx:18` | `:40–54` | Good. |
| Confused deputy | `service-to-service-authentication.mdx:117` | `:117` | Good. |

## Versions, defaults and conventions

| Assumption | Where it appears | Stated in the text? | Assessment |
|---|---|---|---|
| HTTP/1.1 text syntax; HTTP/2 and HTTP/3 carry the same semantics | Every HTTP example | Yes: overview `:22`, entry 1 `:124`, entries 3 `:51`, 5 `:110`, 6 `:154` | Good. |
| OAuth 2.0 (RFC 6749 + RFC 9700), OAuth 2.1 as a draft | Entries 1, 5, 6 | Yes: entry 5 `:19`, `:268` | Good. OAuth 2.1 confirmed still an Internet-Draft (draft-ietf-oauth-v2-1-16, 3 September 2026). |
| RFC 10017 for browser-based apps | Entry 5 `:81` | Yes | Verified (Best Current Practice, 21 August 2026). |
| NIST SP 800-63B revision 3 and revision 4 | Entry 2 `:21`, `:88`, `:133` | Yes | Verified. Email under revision 4: F2. |
| WebAuthn Level 3, CTAP 2.3 | Entry 2 `:21`, `:208`, references | Yes | Verified. Related origins: T1. |
| Cookie specification (RFC 6265 and draft 6265bis) | Entry 3 `:19`, references | Yes | Verified: draft-22 (1 December 2025) is still in the RFC Editor queue, not yet an RFC. |
| Browser default for absent `SameSite` | Entry 3 `:116` | Yes ("Browsers differ") | Good. |
| OpenID Connect Core errata set 2 | Entries 1 and 5, references | Yes | The validation steps follow the pre-errata text: F1. |
| INCITS 359 editions (2004, 2012), XACML 3.0 | Entry 4 `:60`, `:120` | Yes | Good. |
| Unix timestamps (seconds, UTC) | Entries 1, 6, 7 | Entry 1 `:358` ("Unix timestamps") | Good. All values fall on 2026-10-12 UTC. |
| TOTP parameters ($T_0 = 0$, $X = 30$ s, $d = 6$, HMAC-SHA-1) | Entry 2 `:107–124` | Yes | Good. |
| TLS version | Entries 1, 6, 7 | Not stated | Not needed: no claim depends on TLS 1.2 versus 1.3 (both prove client-key possession in the handshake). |

## Series design

**Purpose, audience and scope.** The revised overview names the reader (people who build or review networked software), the prerequisites (code that sends and handles web requests; what signatures and hashes guarantee) and what is introduced along the way. The six objectives are checkable and each is met by named entries (table above). Scope is consistent: XSS defenses are explicitly excluded (entry 3 §6), and nothing outside the stated scope is promised.

**Sequence and rationale.** The overview now explains the order as the path of a request: the model (1), authentication in depth (2, 3), authorization (4), delegation (5), binding (6) and internal calls (7). Each entry's opening and closing paragraphs match this account. The order serves the reader. Entry 5 returning to OAuth after entry 4 is justified, because entry 4 needs only the overview of OAuth from entry 1.

**Prerequisites and dependencies.** No entry relies on a later one except through explicit forward pointers to a deeper treatment (entry 1 → entries 3 and 6; entry 2 → entry 3 §3.1 for the definition of origin). Each of these gives a working definition at the point of use.

**Notation and depth.** Illustrative values are shared and consistent across entries: issuer `https://id.example.com`, subject `user-48213`, client `photo-printer`, the RFC 7636 verifier and challenge in entries 5 and 6, the RFC 9449 key and token in entry 6, and timestamps on 2026-10-12. Depth is comparable across entries: each has a summary table and references, and the protocol-heavy entries (5, 6) carry full message examples. No entry has exercises, which is acceptable for a non-computational topic (standards 6.2, item 5).

**Overview completeness.** The overview's account of each entry matches the entries, and its conventions paragraph is true of all seven: HTTP/1.1 syntax, illustrative values, language-neutral pseudocode, standards cited by number and listed in each entry's References. The Vietnamese overview is out of step (S1).

## Series-level notes

- **Cross-references.** Every ordinal reference and every "Section x.y of the first entry" was checked against its target and is correct. Examples: entry 5 `:87` (entry 1 §8, entry 3 §6), entry 5 `:53` (entry 2 §5.5), entry 6 `:62` (entry 5 §1.3), entry 6 `:181` ("as the previous entry noted": entry 5 §5.1 on rotation), entry 7 `:85` (entry 5 §5), entry 7 `:91` (entry 6 §2), entry 4 `:216` (entry 1 §5.2), entry 3 `:28` and `:227` (entry 1 §3.5 and §7.3). Each "next entry" sentence names the actual next entry. Every link's text matches its target.
- **Terminology.** "Bearer token", "sender-constrained", "resource server", "authorization server", "relying party", "back end for front end (BFF)" and "workload identity" are used with one meaning throughout. "Organization" is now American in all entries.
- **Structure.** All seven entries have numbered sections in sentence case, a Summary with a table and a closing paragraph leading on, and `### References` in house format, in alphabetical order.
- **Promises.** Entry 1 promises deeper treatment of sessions and CSRF (entry 3) and of sender-constrained tokens (entry 6); entry 5 promises identity propagation (entry 7 §5). All are fulfilled.

## Verification log

- Build: not run, by instruction (parallel reviewers). The orchestrator's build of the whole site at `/tmp/claude-0/b6` (built after wave 1; it contains the wave-1 text, for example "RFC 10017" in entry 5) was used.
- `node scripts/check-links.mjs /tmp/claude-0/b6`: "Checked 314 pages and 9693 internal references ... All internal links resolve."
- Rendering of `/tmp/claude-0/b6/blog/<slug>.html` for the seven entries: `katex-error` count 0 in each. Mermaid `min-width` values: 357, 426, 340 and 431 px (entry 1); 344 (2); 331 and 336 (3); 441 and 350 (4); 344 and 469 (5); 331 (6); 428 and 126 (7). All are below 600 px. No letter or punctuation mark is glued to `<span`, `<strong>`, `<a ` or `<code` (grep count 0 in each).
- `npm run -s eos -- lint identity-and-access-control`: 8 files, 0 errors, 0 warnings, 27 suggestions. The suggestions are the ones wave 1 recorded and explained: abbreviations in reference titles, HS256 and SHA as algorithm names, SVID glossed in words, and sentence-length artifacts.
- `npm run -s eos -- syntax` on the series file and the seven entries: "All files compile."
- Recomputed with `python3 -I` (standard library):
  - PKCE: BASE64URL(SHA-256(`dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk`)) = `E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM` (entry 5 `:118`); the verifier has 43 characters and the challenge decodes to 32 bytes. Correct.
  - DPoP `jkt`: the RFC 7638 thumbprint of `{"crv":"P-256","kty":"EC","x":"l8tF…BFs","y":"9VE4…GRDA"}` (lexicographic members, no whitespace) = `0ZcOCORZNYy-DWpqq30jZyJGHTN0d2HglBV3uiguA4I` (entry 6 `:44`). Correct.
  - DPoP `ath`: BASE64URL(SHA-256(`Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU`)) = `fUHyO2r2Z3DZ53EsNrWBb0xWXoaNy59IiKCAqksmQEo` (entry 6 `:137`). Correct, and the same token appears in §3.3 and §3.4.
  - Basic credentials: `cGhvdG8tcHJpbnRlcjpleGFtcGxlLXNlY3JldA==` decodes to `photo-printer:example-secret` (entry 5 `:136`). Consistent with `client_id=photo-printer`.
  - JWT and DPoP segments: `eyJhbGciOiJSUzI1NiIsInR5cCI6ImF0K2p3dCJ9` → `{"alg":"RS256","typ":"at+jwt"}`; `eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Li4ufX0` → `{"typ":"dpop+jwt","alg":"ES256","jwk":{...}}`; `eyJhbGciOiJFUzI1NiJ9` → `{"alg":"ES256"}`; `eyJzdWIiOi` → `{"sub":`; `eyJqdGkiOi` → `{"jti":`. All are consistent with the surrounding JSON.
  - Session identifiers: `Q2hvb3NlIGEgcmFuZG9tIHZhbHVl` (entry 1) decodes to "Choose a random value". `Vb9xQm4tR2kz8YpLw7nJcA` (entry 3) is canonical base64url for 16 bytes (128 bits), as §9 states.
  - Timestamps: 1791795600 = 2026-10-12 09:00:00 UTC and 1791796200 = 09:10:00, ten minutes apart as entry 1 `:358` says; 1791795700 = 09:01:40 (DPoP `iat`); 1791795900 = 09:05:00 (entry 7 `exp`).
  - HOTP: no test vector is printed in entry 2. The definition in §3.1 (dynamic truncation at the offset in the last four bits, top bit cleared, mod $10^d$) was implemented and reproduces all ten RFC 4226 Appendix D values (755224, 287082, …, 520489) and the RFC 6238 SHA-1 vector for $T = 59$ (94287082, 8 digits).
  - TOTP guessing probability (entry 2 `:124`): with three valid codes in $10^6$ and five distinct guesses, $1 - \binom{10^6-3}{5}/\binom{10^6}{5} = 1.49999 \times 10^{-5}$, so "about $15/10^6$" is correct.
- Fact-check of dated facts and references (all fetched 2026-10-15 unless noted):
  - rfc-editor.org/info/rfc10017: *OAuth 2.0 for Browser-Based Applications*, A. Parecki, P. De Ryck, D. Waite, 21 August 2026, Best Current Practice. Section 6.2 confirms that the token-mediating back end gives the browser the access token and keeps the refresh token.
  - rfc-editor.org/info/rfc8471: Proposed Standard, authors as listed, October 2018, with no status change. The entry 6 wording "no longer supported by browsers" is therefore right not to say "Historic". RFC 8472 and 8473 have the same status per the wave-1 check; only RFC 8471 was re-fetched.
  - csrc.nist.gov SP 800-63B-4: *Digital Identity Guidelines: Authentication and Authenticator Management*, Temoshok, Fenton, Choong, Lefkovitz, Regenscheid, Galluzzo, Richer, July 2025. SP 800-63B (revision 3, June 2017, updates as of 2 March 2020, Grassi et al., *... Authentication and Lifecycle Management*): "Withdrawn on August 1, 2025", superseded by 800-63B-4. The revision 4 text confirms each bullet of entry 2 §2.3 (no other composition rules, no periodic change, forced change on evidence of compromise, blocklist, rate limiting, printing ASCII and space, maximum length of at least 64) and the PSTN "restricted" classification. Email: F2.
  - w3.org/TR/webauthn-3: W3C Recommendation, 25 August 2026, editors led by T. Cappalli, title as cited. It defines the backup eligibility (BE) and backup state (BS) flags. Related origins: T1.
  - fidoalliance.org specifications page: CTAP 2.3 Proposed Standard, 26 February 2026. The "FIDO (Fast IDentity Online)" expansion was confirmed in press coverage of the alliance's formation (Linux Magazine), not on a FIDO page.
  - openid.net: *OpenID Connect Core 1.0 incorporating errata set 2*, 15 December 2023, Sakimura, Bradley, Jones, de Medeiros, Mortimore. ID-token validation: F1 and T2.
  - datatracker: draft-ietf-httpbis-rfc6265bis-22 (1 December 2025; Bingler, West, Wilander, Eds.; RFC Editor queue); draft-ietf-oauth-v2-1-16 (3 September 2026; Hardt, Parecki, Lodderstedt; WG document); draft-ietf-oauth-transaction-tokens-11 (30 July 2026; Tulshibagwale, Fletcher, Kasselman).
  - w3.org/TR: *Fetch Metadata Request Headers*, WD 21 September 2026, M. West, with the four `Sec-Fetch-Site` values and only potentially trustworthy URLs, as entry 3 states. *Clear Site Data*, WD 30 November 2017, M. West: "cookies" clears by registrable domain and "storage" by origin, as entry 3 `:223` states. *Device Bound Session Credentials*, FPWD 21 August 2025 (F4).
  - Anderson (ESD-TR-73-51, October 1972) and Lampson ("Protection", Proc. 5th Princeton Symp., March 1971, pp. 437–443): confirmed in the reference list of Saltzer and Schroeder's paper (web.mit.edu). Ferraiolo and Kuhn: csrc.nist.gov conference record, 15th NCSC, 13–16 October 1992, pp. 554–563. INCITS 359-2004 title "Information technology - Role Based Access Control", historical, revised by INCITS 359-2012 (webstore.ansi.org). Bell–LaPadula (MITRE, vol. I, November 1973, DTIC AD0770768) and Biba (ESD-TR-76-372, April 1977, CERIAS record) for F3.
  - SPIFFE: spiffe.io lists the SPIFFE ID, X509-SVID and JWT-SVID standards. The X509-SVID page states "the corresponding SPIFFE ID is set as a URI type in the Subject Alternative Name extension", as entry 7 `:80` states.
  - The other RFC bibliographic entries (6265, 6749, 6750, 6797, 7009, 7515–7517, 7519, 7523, 7591, 7617, 7636, 7638, 7662, 7800, 7914, 8018, 8252, 8628, 8693, 8705, 8707, 9068, 9101, 9106, 9110, 9126, 9207, 9440, 9449, 9700, 4226, 6238) were checked by wave 1 at rfc-editor.org. The reviewer found the authors and years consistent with the RFC index from independent knowledge, but did not re-fetch each one.
- Not verified:
  - Saltzer and Schroeder, *Proc. IEEE* 63(9):1278–1308, 1975: the MIT page fetched does not print the volume, issue and pages, and IEEE Xplore was not reached. The details match every secondary listing found, so the entry is left as it is.
  - Hardy, "The Confused Deputy", *ACM SIGOPS Operating Systems Review*, 1988, pp. 36–38: dl.acm.org could not be fetched, so the volume and issue (22(4)) remain unconfirmed. Wave 1 omitted them, which is the right choice.
  - The exact document titles of the three SPIFFE standards as cited ("The X.509 SPIFFE Verifiable Identity Document" and so on): github.com could not be read from here, and spiffe.io shows short titles ("X509-SVID", "JWT-SVID", "SPIFFE Identity and Verifiable Identity Document").
  - Unsourced but uncontested general statements: "billions of SHA-256 hashes per second" on a graphics processor (entry 2 `:58`); "automated kits for this attack are widely available" (entry 2 `:129`); the browser defaults for an absent `SameSite` (entry 3 `:116`). No source was checked for them; each is stated qualitatively and is consistent with common knowledge in the field.
  - Chrome shipping DBSC in 2026: secondary press source only (not used in the F4 correction).
