<!-- audit: {"slug":"introduction-to-robotics","type":"series","series":"introduction-to-robotics","priority":"P2","before":{"purpose":3,"structure":2,"accuracy":4,"evidence":4,"language":3,"consistency":3,"publishing":4},"findings":{"blocking":0,"shouldFix":3,"optional":1}} -->
# Audit: Introduction to Robotics (series overview)

- Path: `src/content/series/introduction-to-robotics.md` · Route: `/series/introduction-to-robotics` · Type: series · 4 entries, status published · Words: 58
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: reader and prerequisites are stated; what the series is for is one clause.
- structure 2: no sequence rationale beyond "works down to"; does not say what each entry contributes or how the entries connect; shared conventions (right-handed frames, radians in computation, SI units) not stated (standards 6.5).
- accuracy 4: nothing to compute; nothing promised that the entries do not deliver.
- evidence 4: n/a (no claims needing sources).
- language 3: "works down to the geometry, kinematics and estimation that every robot depends on" is vague ("down to").
- consistency 3: description uses a serial comma ("structure, actuation, sensing, and computation"), against house style 5.1; objectives also use serial commas.
- publishing 4: description 116 characters, title fine; lint clean.

Objectives: five, each starting with an assessable verb (describe, represent, explain, outline, explain); each covered (previous review's coverage table, re-checked against the current entries). Objectives are left unchanged because the Vietnamese translation mirrors them.

## Priority

P2: the front door of the series falls short of standards 6.5.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | body | structure | No sequence rationale or per-entry contribution. |
| D2 | Should fix | body | consistency | Shared conventions not stated. |
| C1 | Should fix | `:6` | language | Serial comma in description. |
| C2 | Optional | objectives | language | Serial commas in objectives 1 and 4 (left: changing them touches the translation's mirror of the objectives for no gain in meaning). |

## Revision log (wave 1)
- Structure: body rewritten to meet standards 6.5: prerequisites (kept), where the probability is introduced, the link to the control-systems series, a numbered sequence rationale with what each entry contributes and how it depends on the previous ones, and the shared conventions (SI units, right-handed frames, column vectors, radians in computation).
- Metadata: description rewritten without the serial comma (146 characters).
- Objectives unchanged (C2 left; the translation mirrors them).
- Remaining warnings: none.
- Flags for independent review: series editor to confirm the overview does not promise more than the entries deliver (it describes only what the entries contain).
- Vietnamese translation affected: yes: body (three new paragraphs and a list) and description.
