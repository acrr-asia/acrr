# Live review: Networked Automation and Digital Twins

- URL: https://acrr.asia/blog/networked-automation-and-digital-twins
- Source: `src/content/blog/networked-automation-and-digital-twins.mdx` (Industrial Automation, entry 5 of 5)
- Commit deployed: `7e20c2c`
- Captures: `live-captures` branch, run https://github.com/acrr-asia/acrr/actions/runs/40129647345 (2026-10-24 20:29 UTC): 25 desktop-light, 47 mobile-light, 47 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-25. The reviewer did not write or revise this article.
- Risk: **high (proposed), safety-relevant guidance.** Section 4 and Exercise 3 recommend a security architecture for networks that control plant ("no connection passes directly from the enterprise to a controller"; "a production system should not accept `None`"; a DMZ with an aggregating server), and Sections 5.1, 5.2 and 5.7 set the authority of a digital twin over a running process (a twin "may propose setpoints; the control layer, its interlocks and its independent safety functions remain responsible"). The page itself says an incorrect action in OT "has physical consequences", which is why OT security advice counts as safety-relevant here. The advice is correct, high-level and framed against IEC 62443, but a reader could apply it to a real plant. Under standards 3 only San may accept it. If San judges that architecture-level security description is routine, the page can be accepted with follow-up on this report.

## A. Decision

Leave in review for San (high risk). No critical or major finding: the contract is delivered and the worked example was reproduced. Three minor findings. Recommendation to San: accept with follow-up.

**Library decision: retain.** The page closes the series by connecting the control layer to enterprise systems and by giving the site's only careful definition of a digital twin, with a worked example that shows both what a twin can detect and its limits. No other ACRR page covers ISA-95, OPC UA, IEC 62443 or digital twins. Its state-estimation passage overlaps `sensing-and-state-estimation` but links to it instead of repeating it.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who has followed the first four entries, or a practitioner who meets "OPC UA", "Purdue levels" and "digital twin" in projects and wants precise meanings.
- Problem: how plant control data reach higher-level systems with their meaning and status intact, how that connection is secured, and what a digital twin is and needs in order to be useful.
- Outcome: place functions on ISA-95 levels; explain OPC UA's address space, status codes, subscriptions and PubSub, and how MQTT differs; sketch a zones-and-conduits architecture; tell a digital twin from a shadow, a model or a visualization; predict and interpret a twin's fault residual and its gain trade-off.
- Distinctive contribution: an exact, testable definition of a digital twin with the Kritzinger classification and a reproducible leak-detection example whose residual is derived in closed form, set against the protocol and security layers it depends on.
- Evidence: one Python program with real output, re-run with 40 seeds; the residual formula derived from the code; IEC 62264-1, IEC 62443, IEC 62541, ISO 23247, ISO/IEC 20922:2016, Kritzinger et al. (2018), Mahnke et al. (2009).
- Limitations: architecture level only (no OPC UA programming, no IEC 62443 risk-assessment procedure); a linear tank with a fixed-gain observer, not a Kalman filter; the twin cannot distinguish a leak from other unmodeled flows (stated).

The benefit is delivered. The opening states the two subjects and why they meet at the control-layer boundary; Section 3's table answers "which protocol for which need"; the digital-twin half defines, delimits, classifies, then shows a twin working and its limits, ending with engineering requirements. Verified for this review: the program output (alarm at 941 s, mean residual −9.76 mm); the 40-seed ranges (36–49 s after the leak; 62–102 s for the 0.0005 m³/s leak); the recursion r = a(1 − L) r − d, derived from the observer equations; r̄ ≈ −9.29 mm; steady states 1.25 and 1.75 m and A/k = 250 s; Exercise 2 (100 against 5 000 values per second); Exercise 4 (−4.6 mm, L ≈ 0.027). Value category: conceptual understanding (it resolves a widely misused term and explains what OPC UA adds), with technical decision second. Format: explainer. Worth its 26-minute reading effort; the closing paragraph ties the five entries together.

Overlap: `sensing-and-state-estimation` (predict–update cycle; linked), `numerical-integration-notes` (linked), `fieldbuses-and-industrial-ethernet` (TSN, Modbus registers; linked both ways). No duplication that calls for a merge.

## C. Substantive findings

None.

## D. Visual and structural findings

### L1. Residual formula cut at 360 px

- Location: Section 5.6, the display equation for r̄ (mobile-light-35).
- Problem: at 360 px the equation ends at "0.5 mm / (1 − 0.996 …"; the result "≈ −9.3 mm" is off-screen with no scroll cue (site-level behavior). The next line reads "consistent with the −9.76 mm", so a phone reader is told the result agrees with a number they have not seen; −9.3 mm appears only later in the "limits" paragraph.
- Why it matters: the prediction is the point of the paragraph (the code's −9.76 mm confirms it). Minor, because the value is restated a paragraph later.
- Required action: break the equation after the symbolic form, with the numeric evaluation on its own line (`aligned` block).
- Priority: minor
- Acceptance condition: at 360 px the full equation including "≈ −9.3 mm" is visible.

### L2. ISA-95 diagram repeats the table that follows it

- Location: Section 1.1, the five-box flowchart and the level table directly below it (desktop-light-02 to 04).
- Problem: the flowchart is a vertical stack of the same five levels the table lists, and it takes more than a screen at 1280 px; its only content not in the table is the time scale of each level.
- Why it matters: repetition costs reading effort at the opening of the page (standards 6.8: a visual must add something the text or a table does not).
- Required action: add a "Time scale" column to the table and remove the flowchart, or turn the flowchart into something the table cannot show (for example the Purdue placement of the DMZ from Section 4.2).
- Priority: minor
- Acceptance condition: Section 1.1 presents the five levels once, with their time scales.

### L3. Diagrams without captions or accessible names

- Location: Section 1.1 flowchart and Section 5.4 state-estimation diagram (`facts.json`: 2 SVG figures without title on every viewport).
- Problem: no captions or accessible titles; in the Section 5.4 diagram the "state, parameters" and "prediction" edges cross between State estimation and Model.
- Why it matters: the Section 5.4 caption is where the reader would be told that the residual output is what the twin's diagnosis uses; screen-reader users get nothing.
- Required action: add `accTitle`/`accDescr` and a one-sentence caption to each diagram that remains (see L2).
- Priority: minor
- Acceptance condition: each remaining diagram has a visible caption, and `facts.json` reports 0 SVG figures without title.

Site-level behavior also seen here (already recorded): at 360 px the level, node-class, connection-choice and Kritzinger tables scroll under the 7rem cell minimum (the "Typical systems" and "Why" columns are cut); the address-space tree and the program's comments and output are cut at the code box edge. Dark mode: the state-estimation diagram is legible (mobile-dark-29, 30).

## E. Technical and source findings

No technical or source errors found; see Section B for what was recomputed. Not verified in this review: OPC UA and MQTT protocol constants (port numbers 4840, 1883, 8883; QoS levels) were checked against reviewer knowledge only, as in wave 2. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, 0 KaTeX errors, 0 broken images, 0 console errors.

## F. Required changes

Mandatory: none.

Optional (follow-up):

- [ ] L1: split the Section 5.6 residual equation.
- [ ] L2: fold the ISA-95 diagram's time scales into the table.
- [ ] L3: captions and accessible titles for the diagrams.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L2 | | | |
| L3 | | | |
