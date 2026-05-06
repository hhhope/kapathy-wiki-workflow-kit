# Archive Review

Review date: 2026-05-06

Decision: **BLOCKED**

## Summary

This change is complete in the mechanical OpenSpec sense, but it is not
archive-ready. The published `article-learning-capture` skill was created
without the required skill-authoring gates and then proved weak in live use.

The issue is not only wording quality. The change skipped behavior proof before
publishing a behavior asset.

## Findings

| Finding | Result | Evidence | Reason |
|---|---|---|---|
| `skill-creator` discovery/validation was not performed | blocker | `.codex/skills/article-learning-capture/` exists; `evaluation.md` contains no trigger validation results | New skill authoring requires real triggers, should-not-trigger cases, and validation before shipping. |
| `writing-skills` / skill TDD was not performed | blocker | `evaluation.md` has narrative RED/GREEN sections, but no observed baseline failure or post-skill pass evidence | The repo requires semantic skill changes to include baseline fail and before/after evidence. |
| `simplicity-first` gate was skipped | blocker | One article-learning need became OpenSpec + skill + four references + spec delta + wiki rewrite | This was exactly the "small change drifting toward framework building" case. |
| Scorecard is not calibrated enough to guide work | blocker | `scorecard.md` uses broad criteria and does not separate primary sources from secondary interpretations | The user found the scoring naive; live use mixed primary official sources and a secondary WeChat interpretation too easily. |
| Source preservation is too weak | blocker | SOP requires URL/metadata and paraphrased notes, but no source snapshot / extracted markdown / bounded source map | The user expected original source grounding before translation and learning. |
| Current wiki rerun is not proof of skill correctness | blocker | `ae523e9` applies the new format to articles but does not show the skill preventing the original failures | Output production is not the same as trigger and behavior validation. |

## Required Repair Before Archive

The next work must choose one path and record the choice in this change before
archive:

1. **Repair the skill**: run `skill-creator`, `writing-skills`,
   `test-driven-development`, and `simplicity-first`; add real RED/GREEN
   evidence; revise source preservation and scorecard.
2. **Downgrade the asset**: remove the repo-local skill publication and keep the
   method as wiki SOP only.
3. **Replace with a smaller route**: reuse existing `weixin-reference-wiki-capture`
   / `readme-learning-capture` plus a lightweight article-learning wiki method.

## Minimum Acceptance For Repair

- At least five should-trigger and three should-not-trigger cases are run and
  recorded with results.
- A RED baseline shows the old behavior failing on source preservation,
  scoring, or skill/wikilayer routing.
- A GREEN result shows the revised skill preventing that failure.
- The scorecard distinguishes primary source, secondary interpretation,
  structure reference, and low-relevance article.
- The SOP explicitly defines what source material is preserved without violating
  copyright.
- `openspec validate formalize-article-learning-capture --strict` passes after
  repair.

## Archive Decision

Do not archive this change yet. Treat `complete` as a stop signal and this
archive review as the current blocker record.
