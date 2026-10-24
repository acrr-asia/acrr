# Live review: What Is a Robot? Components and the Sensing-Acting Loop

- URL: https://acrr.asia/blog/what-is-a-robot
- Source: `src/content/blog/what-is-a-robot.mdx` (Introduction to Robotics, entry 1)
- Commit deployed: `1eb85d4`
- Captures: run https://github.com/acrr-asia/acrr/actions/runs/39980397404 (2026-10-23 15:43 UTC): 17 desktop-light, 31 mobile-light, 31 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review; Phase 3 library audit), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical explainer; no reporting, named-party claims, safety guidance or commercial relationship; Section 3 mentions torque limits and emergency stops only as examples of design structure, not as guidance)

## A. Decision

Accept. The page delivers its contract, the numbers on it were recomputed in this review, and no critical, major or minor finding is open. The two Mermaid figures and three tables fit the column at 1280 and at 360 px, in light and dark mode.

**Library decision: retain.** This is the vocabulary entry of the robotics series: entries 2 to 4 rely on its subsystems, its degree-of-freedom terms and its loop hierarchy, and the motion-planning series (Configuration Space and the Motion Planning Problem; Following a Plan: Path Tracking and Reactive Obstacle Avoidance) uses the same terms. The 13 October audit's blocking reference problem (ISO 8373 editions) and its structural findings (prose table of contents, no exercises) were fixed in wave 1 and are visible on the live page. Nothing on the page is redundant with another ACRR article; a rewrite, merge or reclassification would gain nothing.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: a student or engineer with no robotics background (feedback from the control series, torque and inertia assumed) starting the robotics series.
- Problem: "robot" is used loosely; the reader needs a precise working definition and a shared vocabulary for the parts of a robot and how they interact before kinematics and estimation.
- Outcome: state what makes a machine a robot and place a machine on the autonomy spectrum; name the four subsystems; count degrees of freedom and mobility (Chebychev–Grübler–Kutzbach) and use the terms redundant, underactuated and nonholonomic; compute transmission torque, speed, reflected inertia and encoder resolution; explain the energy and information paths, the loop hierarchy and the three software architectures.
- Distinctive contribution: one structural picture (subsystems, two flows, loops within loops, software layers) that ties hardware to control timing, with worked numbers and exercises; the point that a motor encoder's resolution does not describe the link.
- Evidence: worked formulas and three exercises with answers; ISO 8373:2012 and :2021; Brooks (1986); Gat (1998); Nilsson, Ed. (1984).
- Limitations: no kinematics, dynamics or estimation (deferred to entries 2 to 4); loop rates are orders of magnitude only; software architectures are described historically, not compared in depth.

The benefit is delivered. The opening states what is assumed and the order of the argument; each section adds one layer (definition, parts, flows, loops, software, difficulties) and the Summary table works as a review sheet. Spot checks recomputed in this review: serial-arm mobility $6(n + 1 - 1 - n) + n = n$; four-bar $3(4 - 1 - 4) + 4 = 1$; $\tau_j = 0.8 \times 50 \times 0.5 = 20$ N·m, $3000/50 = 60$ rpm, $2500 \times 2 \times 10^{-5} = 0.05$ kg·m²; $360°/(4096 \times 100) = 0.000879°$; $360°/(2048 \times 50) = 0.00352°$. Value density: no section is padding; Section 3 (energy and information paths) is the passage least likely to be found in an introductory chapter elsewhere and the most useful for design thinking. Overlap with other ACRR articles is by design and handled with links: degrees of freedom reappear in Configuration Space and the Motion Planning Problem (as the dimension of C-space), sensor types in Sensing and State Estimation and in the Sensor Systems series, the loop hierarchy in Following a Plan. Value category: conceptual understanding. Format: explainer.

## C. Substantive findings

None.

## D. Visual and structural findings

None requiring action. Both Mermaid diagrams (Section 2 subsystems, Section 4 loop hierarchy) fit the column at 360 px and are correct in dark mode (mobile-dark-07, 19); their labels are small at 360 px (about 9 px) but legible on the captures. The autonomy table (Section 1.2) wraps into narrow columns at 360 px and remains readable (mobile-light-05). All three display equations fit at 360 px.

## E. Technical and source findings

None. `facts.json`: HTTP 200 on all three viewports, no horizontal page scroll, no overflowing elements, 0 KaTeX errors, 0 broken images, 0 console errors.

Not verified in this review: the paraphrase of ISO 8373:2021 in Section 1.1 ("rephrases it around locomotion, manipulation and positioning") against the standard's text (the standard was not available; the audit flagged the same point), and the page numbers of the Gat chapter (not given on the page).

## F. Required changes

Mandatory: none.

Optional:

- [ ] Section 4 figure: a top-to-bottom layout with fewer crossing return edges, or a slightly larger label size, would make the loop hierarchy easier to read on a phone.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| (none) | | | |
