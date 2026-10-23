# Live review: Spectra: The DFT and the FFT

- URL: https://acrr.asia/blog/dft-and-fft
- Source: `src/content/blog/dft-and-fft.mdx` (Digital Signal Processing for Engineers, entry 3)
- Commit deployed: `b768495` (master after PR #48)
- Captures: `live-captures` branch, run https://github.com/acrr-asia/acrr/actions/runs/39932244075 (2026-10-23 09:30 UTC): 20 desktop-light, 37 mobile-light, 37 mobile-dark tiles
- Reviewed by, date: Claude (chief editor, live review), 2026-10-23. The reviewer did not write or revise this article.
- Risk: routine (a technical tutorial; no reporting, named-party claims, safety guidance or commercial relationship)

## A. Decision

Request revision. One major presentation finding (L1): two key equations of Section 3.2 are cut off on every screen size. Everything else is minor.

## B. Reader-value assessment

Reconstructed contract (inferred from the page, not the author's stated intent):

- Reader: an engineer or student who can use `numpy.fft` but cannot yet say what a measured spectrum shows or why it looks as it does.
- Problem: reading amplitudes, frequencies and noise from an FFT correctly; choosing record length and window.
- Outcome: compute bin frequencies and resolution, explain leakage and the FFT's cost, choose and correct for a window, read amplitudes and noise levels.
- Distinctive contribution: one derivation-to-practice path (definition, periodicity, FFT, leakage, windows, scaling) with every number reproduced by runnable code and a final recipe table.
- Evidence: derivations in the text; three scripts with their real output; Cooley and Tukey (1965), Harris (1978), Heideman et al. (1984), Oppenheim and Schafer (2010), Welch (1967).
- Limitations: radix-2 only in detail; multitaper and parametric methods out of scope.

The benefit is delivered. The opening states the question and the conventions; each section answers part of it; the worked numbers are right (spot-checked: the four-point DFT, the bin spacing and bin offsets of Section 5.2, 5120 against 1 048 576 multiplications, the window table against the standard values). The recipe table (5.4) and the summary table (7) turn the article into something a reader can reuse. The page is worth its reading effort; no section is padding. Value category: conceptual understanding, with practical implementation close behind. Format: explainer.

## C. Substantive findings

### L1. Section 3.2 equations cut off at the right edge

- Location: Section 3.2, the display equation after "the DFT becomes" and the butterfly pair after "costs nothing extra"; desktop-light-07, mobile-light-13.
- Problem: both equations are wider than the text column at 1280 px and at 360 px. On desktop the first ends at "= E[k] + W_N^k" with O[k] hidden, and the second shows "k =" with the range hidden; on a phone even less is visible. They scroll sideways inside their box, but nothing on the page tells the reader so.
- Why it matters: these two equations are the result of the section (the split into E and O, and the butterfly). A reader who does not discover the hidden scroll reads an incomplete formula at the point the argument depends on it.
- Required action: break each equation over lines (for example an `aligned` block: the split on two lines, then "= E[k] + W_N^k O[k]"; the butterfly pair one equation per line with the index range on its own line).
- Priority: major
- Acceptance condition: on new captures, both equations are fully visible without sideways scrolling at 1280 px, and at 360 px no line of either is cut.

### L3. Window table: last column hidden at desktop width

- Location: Section 5.1, the table of window properties; desktop-light-12.
- Problem: the sixth column ("Equivalent noise bandwidth (bins)") is cut under the scroll shadow at 1280 px; its header reads "Equivalen... bandwidt...".
- Why it matters: the ENBW values are needed in Section 5.3; at desktop width a reader expects the table to fit.
- Required action: shorten the header to "ENBW (bins)" (the term is defined, with its abbreviation, in the list that follows the table) so that all six columns fit at 1280 px.
- Priority: minor
- Acceptance condition: all six columns, headers included, visible at 1280 px.

## D. Visual and structural findings

### L2. FFT structure diagram: final node off-screen at 360 px

- Location: Section 3.2, the Mermaid flowchart; mobile-light-13.
- Problem: at 360 px the diagram is wider than the screen (by design, figures keep at least 60 percent of their natural width), and its last node, "butterflies", is hidden to the right.
- Why it matters: the node the diagram leads to is the one a phone reader does not see; there is no visible scroll cue.
- Required action: a site-level scroll cue for wide figures (as tables already have), or a top-to-bottom layout for this diagram.
- Priority: minor (site-wide behavior, not specific to this article; to be taken up with the site's figure styling)
- Acceptance condition: at 360 px the "butterflies" node is visible, or a visible cue shows that the figure scrolls.

The page already uses the right representations: equations with intermediate steps, a process diagram for the FFT split, comparison and recipe tables, and code with real output. No further visual is needed.

## E. Technical and source findings

### L4. Printed output lines cut in Section 5.2

- Location: Section 5.2, the output block (and the last line of the script above it); desktop-light-14.
- Problem: the printed lines are longer than the code box; "200-300 Hz floor -52.8" loses its unit at the edge.
- Why it matters: small; the values are repeated in the prose below.
- Required action: optional; shorter labels in the `print` call would let the output fit. Changing the code means re-running it.
- Priority: minor
- Acceptance condition: output lines fully visible at 1280 px, or the finding is accepted as a limitation of wide code output.

No technical or source errors found on the page. KaTeX rendered without errors, all images loaded, and there was no console error and no page-level horizontal scroll at 360 px (`facts.json`).

## F. Required changes

Mandatory:

- [ ] L1: split the two Section 3.2 equations so that they fit.

Optional:

- [ ] L3: shorten the ENBW column header.
- [ ] L2: scroll cue for wide figures (site-level).
- [ ] L4: shorter output labels in the Section 5.2 script.
- [ ] Section 1.2: "whose columns are orthogonal ($W^H W = NI$ ...)" breaks after the opening parenthesis on desktop; a colon instead of the parenthesis would avoid the orphaned bracket.

## G. Re-review

| Finding | Re-checked on (URL, commit, date) | Acceptance condition met? | Closed |
|---|---|---|---|
| L1 | | | |
| L3 | | | |
| L2 | | | |
| L4 | | | |
