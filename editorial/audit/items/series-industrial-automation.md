<!-- audit: {"slug":"industrial-automation","type":"series","series":"industrial-automation","priority":"P1","before":{"purpose":3,"structure":2,"accuracy":4,"evidence":4,"language":2,"consistency":2,"publishing":2},"findings":{"blocking":0,"shouldFix":4,"optional":1}} -->
# Audit: Industrial Automation (series overview)

- Path: `src/content/series/industrial-automation.md` · Route: `/series/industrial-automation` · Type: series overview · 5 entries, status published · Words: 144 (`eos status`)
- Audited at commit `e21dcc8`, 2026-10-13

## Provisional scores (before revision)

- purpose 3: reader and prerequisites are stated ("basic electrical engineering (voltage, current, switches and relays)"), but the page does not say what a reader will be able to do at the end beyond the objectives list.
- structure 2: everything after the prerequisites is one 86-word sentence (line 13) listing the five entries; there is no sequence rationale beyond "from the bottom of a plant upward", no statement of how the entries connect, and the conventions shared by all entries (IEC 61131-3 edition, signals in percent of span, Python 3) are not stated.
- accuracy 4: nothing incorrect.
- evidence 4: an overview; no claims needing sources.
- language 2: the 86-word list sentence is hard to read; "PID" not expanded.
- consistency 2: the four `objectives` cover entries 1-4 only; the fifth entry (ISA-95, OPC UA, IEC 62443, digital twins), a quarter of the series, has no objective, so the objectives and the entries disagree (standards 6.5: "each covered by an entry", and the converse is implied by "what each entry contributes").
- publishing 2: description 219 characters (limit 165).

## Priority

P1: the series front door; its objectives are the yardstick the series review and the last entry's closing paragraph measure against, and one entry is missing from them.

## Findings

| ID | Severity | Location | Dimension | Finding |
|---|---|---|---|---|
| D1 | Should fix | `:7-11` (`objectives`) | consistency | No objective for the fifth entry |
| D2 | Should fix | `:13` | structure | Body is one paragraph whose second half is a single 86-word list sentence; no sequence rationale, no account of how entries connect |
| D3 | Should fix | `:13` | purpose | Shared conventions not stated (IEC 61131-3:2013 as the edition followed, signals in percent of span, Python 3 standard library) |
| P1 | Should fix | `:3` | publishing | Description 219 characters, a list of topics |
| C1 | Optional | `:13` | language | "PID" not expanded |

### D1. Fifth entry has no objective
- **Where:** `src/content/series/industrial-automation.md:7-11`
- **Text:** the four objectives end with "Tune PID loops for typical process variables such as temperature, level, flow and pressure."
- **Problem:** `networked-automation-and-digital-twins.mdx` (ISA-95 levels, OPC UA, MQTT, IEC 62443 zones and conduits, digital twins with a worked residual-based leak detector and five exercises) is not represented. A reader of the overview cannot tell what the last entry is for, and the series review cannot check it against an objective.
- **Correction:** add "Explain how plant data reach higher-level systems through the ISA-95 levels and OPC UA, and how a digital twin uses residuals to detect faults." (verb-first, checkable; delivered by Sections 1-2 and 5.4-5.6 of entry 5). The `objectives` field is not one of the fields the Vietnamese file must copy, so the build is unaffected; the translation needs the new objective.

### D2. One-sentence body
- **Where:** `:13`
- **Text:** "It moves from the bottom of a plant upward: Boolean logic, latches, timers and state machines; the programmable logic controller, ...; and finally the connection of automation systems to higher-level systems through ISA-95 and OPC UA, and digital twins that run alongside the plant."
- **Problem:** 86 words; the order is asserted, not explained (each layer uses the one below: the PLC executes the logic of entry 1, networks extend the PLC's I/O timing, PID loops run on PLC cyclic tasks over those networks, entry 5 exposes all of it upward).
- **Correction:** three short paragraphs: reader and prerequisites; the sequence and why each entry depends on the previous one; shared conventions.

### D3. Shared conventions
- **Where:** `:13`
- **Problem:** every entry states Python 3; entries 1-2 follow IEC 61131-3:2013 while noting the 2025 edition; entry 4 uses percent of span. The overview should state these once.
- **Correction:** add a conventions paragraph.

### P1. Description length
- **Text:** "A series on automating physical processes: logic and sequential control, programmable logic controllers, fieldbuses and industrial Ethernet, PID control of process variables, and networked automation with digital twins." (219 characters)
- **Correction:** "A five-entry series on automating physical processes, from Boolean logic and PLCs through fieldbuses and PID loops to OPC UA and digital twins." (143)

### C1. PID
- **Correction:** expand "proportional–integral–derivative (PID)".

## Revision log (wave 1)
- Structure: body rewritten as three paragraphs: reader and prerequisites; the sequence and how each entry depends on the one before (logic → the PLC that executes it → networks that extend its I/O timing → feedback loops closed through that I/O → the systems above and digital twins); shared conventions (IEC 61131-3:2013 with the 2025 edition noted in entry 2, percent of span in entry 4, Python 3 standard library with real output). (D2, D3)
- Objectives: added a fifth, "Explain how plant data reach higher-level systems through the ISA-95 levels and OPC UA, and how a digital twin uses residuals to detect faults.", delivered by entry 5, Sections 1-2 and 5.4-5.6 and Exercises 1, 2 and 4. The other four objectives unchanged. (D1)
- Metadata: description 219 → 143 characters, one sentence. (P1)
- Terminology: PID expanded at first use. (C1)
- Remaining lint: 3 suggestions (ISA, OPC, UA "not expanded"): ISA-95 and OPC UA are standard names; expanding OPC (Open Platform Communications) on the overview adds nothing for the reader and entry 5 explains both.
- Flags for independent review: Series Editor: confirm the new objective is the right summary of entry 5 and that the overview promises nothing the entries do not deliver. The series file changed, so `reviews/industrial-automation.md`'s content-hash stamp is now stale (series gate); a new series review and `series-pipeline stamp` are needed.
- Vietnamese translation affected: yes. `src/content/series/vi/industrial-automation.md` needs the fifth objective, the new description, and the restructured body (meaning of the existing text unchanged; added: the dependency of each entry on the previous one and the conventions paragraph). No copied field changed (`status`, `category`, `example`, `plannedEntries` untouched), so the build is unaffected.
