# Archive Review

Review date: 2026-05-06

Decision: **PASS AFTER REPAIR**

## Summary

This change was initially complete in the mechanical OpenSpec sense but not
archive-ready. The published `article-learning-capture` skill had been created
without the required skill-authoring gates and then proved weak in live use.

The repair pass chose the smallest path: keep the current skill and fix the
missing gates instead of creating a new framework or downgrading the asset.

## Findings

| Finding | Result | Evidence | Reason |
|---|---|---|---|
| `skill-creator` discovery/validation was not performed | resolved | `evaluation.md` records real trigger phrases and eight trigger/non-trigger validation cases | New skill authoring now has explicit discovery and validation evidence. |
| `writing-skills` / skill TDD was not performed | resolved | `evaluation.md` records four RED baseline commands and GREEN result checks | The repair now includes observed baseline failure and post-edit proof. |
| `simplicity-first` gate was skipped | resolved | `evaluation.md` records the chosen repair path: no new skill, page type, automation, tool, or OpenSpec change | The repair stayed within the existing asset instead of expanding scope. |
| Scorecard is not calibrated enough to guide work | resolved | `scorecard.md` now has an admission gate, source classes, anchored scoring, and hard caps | The scorecard now separates primary sources, secondary interpretations, structure references, and low-relevance material. |
| Source preservation is too weak | resolved | `SKILL.md`, `sop.md`, `scorecard.md`, and `wiki-template.md` require source grounding | Source preservation now includes extracted markdown, source map, bounded excerpts, or retrieval-failure note. |
| Current wiki rerun is not proof of skill correctness | resolved | `evaluation.md` records trigger validation and RED/GREEN commands separately from wiki output | Output production is no longer treated as the proof artifact. |

## Repair Path Chosen

Chosen path: **repair the skill**.

The downgrade and replacement paths were rejected because the live failure was
not that a skill was inappropriate; it was that the skill had been published
without its required gates.

## Minimum Acceptance For Repair

- At least five should-trigger and three should-not-trigger cases are run and
  recorded with results: satisfied in `evaluation.md`.
- A RED baseline shows the old behavior failing on source preservation,
  scoring, or skill/wikilayer routing: satisfied in `evaluation.md`.
- A GREEN result shows the revised skill preventing that failure: satisfied by
  post-repair `rg` checks and OpenSpec validation.
- The scorecard distinguishes primary source, secondary interpretation,
  structure reference, and low-relevance article: satisfied in `scorecard.md`.
- The SOP explicitly defines what source material is preserved without violating
  copyright: satisfied in `sop.md`.
- `openspec validate formalize-article-learning-capture --strict` passes after
  repair: satisfied on 2026-05-06.

## Archive Decision

Archive review now passes after repair. Remaining risk is explicit: validation
is static/manual and does not prove automatic runtime dispatch.
