# Live review: Authentication and Authorization: From First Principles to Tokens

- URL: https://acrr.asia/blog/token-based-authentication
- Source: `src/content/blog/token-based-authentication.mdx` (Identity and Access Control, entry 1)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 38 desktop-light, 69 mobile-light, 69 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer of published standards; no reporting, no claims about named people or firms beyond what the standards bodies publish, no commercial relationship). Security engineering guidance is not treated here as "safety-relevant guidance" in the sense of standards Section 3; if San reads that category to include security practice, the page becomes high risk and this acceptance must be his.

## A. Decision

Accept with minor follow-up. The page delivers its contract, the technical content was spot-checked against the cited standards and holds, and no finding is critical or major. Five minor findings remain open: three on how the four Mermaid diagrams render (L1 to L3, mostly site-level), one overstatement in Section 7.2 (L4) and missing forward links to three later entries (L5).

**Library decision: retain.** This is the series' map: every later entry refers back to it, and it is also the only ACRR page that explains the structure, validation and lifecycle of access tokens (Sections 6 and 7) and enforcement at the resource server (Section 9); no later entry repeats that material. Its overlap with entries 2 to 7 is intended (a short overview of each layer) and each overlapping passage is brief. Its content does not need to change; the follow-ups are polish and navigation, so no rewrite, merge or reclassification is warranted.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a developer or reviewer of web applications and HTTP APIs who uses sessions, OAuth 2.0 or JSON Web Tokens through a framework and wants the model behind them.
- Problem: passwords, cookies, OAuth 2.0, OpenID Connect and JWTs look like unrelated technologies, and common defects (accepting ID tokens at an API, decoding instead of validating, missing object-level checks, treating 401 and 403 alike) come from confusing what each one answers.
- Outcome: separate identification, authentication, authorization and audit; compare reference and value tokens; explain what OAuth 2.0 delegates and what OpenID Connect adds; validate a JWT access token in the right order; place object-level authorization at the resource server; state how long each credential outlives a sign-out.
- Distinctive contribution: a top-down path from the reference monitor (Anderson 1972; Saltzer and Schroeder 1975) to current IETF practice (RFC 9068, RFC 9700), in which each protocol appears only after the problem it solves, with an ordered validation procedure, language-neutral pseudocode and a threats-and-controls table.
- Evidence: 23 references, mostly the IETF standards themselves, plus OpenID Connect Core, XACML 3.0, the OWASP API Security Top 10 (2023) and the two historical sources.
- Limitations: overview depth only (authenticators, sessions, authorization models, grants, sender-constrained tokens and service-to-service calls are left to entries 2 to 7); no particular framework or vendor; the cookie revision draft is cited as work in progress.

The benefit is delivered. Spot checks in this review: `iat` 1791795600 and `exp` 1791796200 are 2026-10-12 09:00 and 09:10 UTC; the JWT header prefix decodes to `{"alg":"RS256","typ":"at+jwt"}`; 401 must carry `WWW-Authenticate` (RFC 9110); the three RFC 6750 error codes and their status codes; Broken Object Level Authorization is item 1 of the OWASP API Security Top 10 2023; RFC 9700 deprecates the implicit and password grants; algorithm confusion, `exp` "at or after" and key rotation are stated correctly. Section 3.3's example session identifier decodes to the English text "Choose a random value" (audit C4, left unchanged; harmless).

Value density: at 33 minutes this is the longest entry of the series and twice the length of the others, but it is a map and a reference in one: the tables (Sections 1.2, 1.3, 3.5, 4.2, 5.5, 6.1, 6.3, 8, 10 and 11) let a reader return to it, and Sections 6.5, 9 and 10 are the most practically useful material in the series. The one section a reader with the stated prerequisite may skim is 3.1 (what an HTTP method, header and status code are); the series overview promises that HTTP is introduced where first used, so it is justified. Overlap within the series (by design): Section 2.1 with Authenticators: Passwords, One-Time Codes and Passkeys; 2.2 with Service-to-Service Authentication; 3.3 with Sessions and Cookies in Depth; 3.6 with Sender-Constrained Tokens; 4.2 with Authorization Models: RBAC, ABAC and Relationship-Based Access; 5.3 and 5.4 with OAuth 2.0 Grants and Client Types. No overlap outside the series was found. Value category: conceptual understanding, with reference value close behind. Format: explainer.

## C. Substantive findings

### L4. Section 7.2: refresh-token reuse is not always an attacker

- Location: Section 7.2, "Three practices make refresh tokens safer", the **Rotation** item.
- Problem: "If an old token is presented again, two parties hold copies, one of which must be an attacker" overstates the inference. A legitimate client that sent a refresh request and lost the response (a network failure, a crash, two tabs refreshing at once) also presents a rotated token again. RFC 9700 (Section 4.14.2) argues from a compromised token and says only that the authorization server cannot tell which party presented the invalidated token, and therefore revokes.
- Why it matters: the recommended response (revoke the chain) stays right, but a reader who implements rotation believing reuse proves an attack is surprised by spurious sign-outs and may not design for them.
- Required action: say that reuse means the token may have been copied, and that the server, unable to tell an attacker from a client retrying after a lost response, revokes the chain; optionally mention that some servers allow a short grace period for the immediately previous token.
- Priority: minor
- Acceptance condition: the Rotation item no longer says that one holder "must be an attacker" and names the benign case.

### L5. No links from the overview sections to entries 4, 5 and 7

- Location: Section 2.2 (users and workloads), Section 4.2 (authorization models), Sections 5.3 and 5.4 (client types and other grants).
- Problem: the page links forward to entries 2, 3 and 6 where it touches their topics, but not to Authorization Models (entry 4), OAuth 2.0 Grants and Client Types (entry 5) or Service-to-Service Authentication (entry 7), although Sections 4.2, 5.3–5.4 and 2.2 are short versions of exactly those entries. The opening says only that "later entries in the series take each layer further".
- Why it matters: a reader who needs depth on one layer (for example, how to choose between RBAC and ReBAC, or which grant a command-line tool should use) has no pointer at the point of need in a 33-minute article; standards 8.1 asks for the first mention of another entry to be linked.
- Required action: one linked sentence at the end of Section 2.2, 4.2 and 5.4 naming the entry that treats the topic in depth (as Sections 3.3 and 3.6 already do).
- Priority: minor
- Acceptance condition: Sections 2.2, 4.2 and 5.4 each link the corresponding later entry on the live page.

## D. Visual and structural findings

### L1. The four diagrams have no caption and no accessible name

- Location: Section 1.2 (request flowchart), Section 5.4 (PKCE sequence), Section 7.2 (refresh sequence), Section 9 (resource-server pipeline); `facts.json` reports four SVG figures without a title on every viewport.
- Problem: the diagrams are bare Mermaid figures: no caption tells the reader what to notice (standards 6.8), and a screen reader announces an unnamed graphic.
- Why it matters: the two sequence diagrams are the clearest statement of the PKCE and refresh flows on the page, and they are invisible to assistive technology; the Section 9 pipeline is the page's summary of enforcement.
- Required action: give each diagram an accessible title and description in its source (`accTitle:` and `accDescr:` lines, which Mermaid writes into the SVG), and a one-sentence caption, for example by placing the diagram in the `Figure` component or by a site-level caption syntax for Mermaid blocks.
- Priority: minor
- Acceptance condition: `facts.json` of new captures reports 0 SVG figures without a title, and each diagram has a caption that says what to notice.

### L2. Sequence diagrams: labels crossed by lifelines and broken mid-word

- Location: Section 5.4 (desktop-light-18 and 19) and Section 7.2 (desktop-light-27 and 28); the same diagrams at 360 px (mobile-light-34, 35, 49, 50).
- Problem: message labels are wrapped to a narrow width and drawn across the lifelines ("Request + a|ccess token", "Check token, cl|ient, revoc|ation, po|licy"), one label is hyphenated inside a parameter name ("grant_type=refresh_tok-en"), and the self-call notes ("Create code_verifier, derive code_challenge", "Check state matches the request") sit on the client lifeline. At 360 px the text is about 7 px high and the Resource server column of the PKCE diagram is off-screen.
- Why it matters: the diagrams remain readable on a wide screen with effort, but a protocol parameter broken as "refresh_tok-en" is the kind of detail a reader copies; on a phone the flows need zooming.
- Required action: site-level: give sequence diagrams wider message spacing (`sequence.messageMargin`/`actorMargin` in the Mermaid config) and a label background so lifelines do not cross text; article-level: shorten the longest labels (for example "refresh_token grant" on one line, "Check code, client, redirect_uri, PKCE" as a note) so nothing wraps inside a parameter name.
- Priority: minor
- Acceptance condition: at 1280 px no message label is crossed by a lifeline and no parameter name is hyphenated; at 360 px the labels are legible without zoom or the figure visibly scrolls.

### L3. Flowcharts cut at 360 px

- Location: Section 1.2 (mobile-light-07: the "Audit log" node is cut at the right edge) and Section 9 (mobile-light-55: the "yes" branch, "Business logic and data access" and "Response", is off-screen).
- Problem: figures keep at least 60 percent of their natural width (site design), so on a phone the right part of each flowchart is hidden without a cue.
- Why it matters: in Section 9 the hidden branch is the successful path, the one the pipeline leads to.
- Required action: the site-level scroll cue for wide figures already recorded in the DFT and FFT review (L2 there), or a top-to-bottom layout for the Section 9 pipeline with both outcomes below each test.
- Priority: minor (site-wide behavior)
- Acceptance condition: at 360 px every node of both flowcharts is visible, or a visible cue shows that the figure scrolls.

The eleven tables scroll inside their frames at 360 px with the site's scroll shadow; at 1280 px every table fits. Dark mode: the diagrams, tables and code blocks render correctly (mobile-dark-07, 19, 25, 29, 34, 35, 42, 46, 49, 50, 53, 55, 58, 62).

## E. Technical and source findings

No technical error beyond L4. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no element wider than the screen, 0 KaTeX errors, 0 broken images, 0 console errors. The references are in house format; the RFC numbers, authors and years were checked against the RFC Editor in the 13 October audit, and this review re-checked the subjects cited in the text. Not verified in this review: the volume, issue and pages of Saltzer and Schroeder (the audit took them from the MIT 6.033 reading list, IEEE Xplore being unreachable).

Maintenance note: the reference to draft-ietf-httpbis-rfc6265bis-22 ("work in progress") will need updating when the cookie revision is published as an RFC; it belongs in the maintenance register of adoption-plan Phase 7.

## F. Required changes

Mandatory:

- None.

Optional:

- [ ] L4: correct the refresh-token reuse sentence in Section 7.2.
- [ ] L5: link entries 4, 5 and 7 from Sections 4.2, 5.4 and 2.2.
- [ ] L1: accessible titles, descriptions and captions for the four diagrams.
- [ ] L2: sequence-diagram spacing (site level) and shorter labels.
- [ ] L3: scroll cue for wide figures (site level).
- [ ] Section 4.4, the `401 Unauthorized` example: at 1280 px the `WWW-Authenticate` line is cut at `error_description="The ac`, and at 360 px the `Set-Cookie` line of Section 3.3 loses its attributes; a shorter `error_description` would let the first fit.
- [ ] The URL slug (`token-based-authentication`) describes the page's earlier, narrower scope; keep it (external links may depend on it) unless the site gains redirects.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
| L4 | | | |
| L5 | | | |
