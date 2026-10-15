---
name: style-guide
description: Editorial Style Guide Manager - set up or update a publication's editorial configuration (eos.config.json), standards manual, glossary and rule severities for editorial-os; adapt the suite to a new website, brand, audience, English variant, citation policy or content model; add house terms. Use when installing editorial-os in a project, when the house style changes, or when a recurring problem needs a new rule.
---

# Style guide manager

The editorial suite is generic; everything specific to a publication lives in three files in the project, normally under `editorial/`:

| File | Holds | Read by |
|---|---|---|
| `eos.config.json` | Publication profile, content types and globs, routes, front-matter field names, language variant, thresholds, rule severities, review stages and score minimums, validation commands | `eos` and every skill |
| `standards.md` | The policy: roles, workflow, language, structure, integrity, consistency, readiness (rubric and thresholds explained) | Every review stage |
| `glossary.json` | House terms (preferred and avoided forms, with reasons), phrases to avoid, intensifiers | `eos lint`, `eos fix`, `eos vale-style`, the copy editor |

`eos` means `node <plugin-root>/scripts/eos.mjs`. The JSON schema of the config is `<plugin-root>/schema/eos.config.schema.json`.

## Set up a new publication

1. `eos init` creates the three files from templates (it never overwrites).
2. Discover the content model: the content directories and file types, how files map to routes, the front-matter field names, drafts and samples, series, translations. Set `content.types` (globs, route pattern, required fields and sections), `content.exclude`, `content.fields`.
3. Interview the user only for what the repository cannot tell you (audience, identity, English variant, citation style, whether autonomous publishing is allowed). Choose defaults from the existing content where possible: measure the dominant spelling variant and terminology (`eos lint` with `spelling-variant` set to `suggestion` shows both forms) and adopt the majority unless the user prefers otherwise.
4. Fill `standards.md` from the template: keep the structure (roles, workflow, policies A-E, rubric, records, governance) and replace the publication-specific parts.
5. Set `validation.commands` to the project's real build and check commands, and verify each one runs.
6. Run `eos lint` on everything, look at the most frequent rules, and tune severities so that `error` means "must never be published" and the warnings are worth reading. Do not silence a rule to make a number go down; fix the content or record an exception.
7. Optionally `eos vale-style` for writers who use Vale in their editor.

## Change the house style

Edit the three files together in one commit, bump the version and add a change-log line in `standards.md`. When a rule becomes stricter, run `eos lint` and either fix the content in the same change or set the rule to `warning` until it is fixed. Record new house terms with a `note` giving the reason, and an autofix `replace` only when the replacement is safe in every context.

## English variants

`language.variant` is `en-US` or `en-GB`. The spelling map (`<plugin-root>/data/spelling-variants.json`) converts in either direction, except for words whose reverse mapping is ambiguous (meter/metre as an instrument, license/licence as a verb, practice/practise as a noun), which convert only towards American English. Add pairs there, not in the project, so every publication benefits.
