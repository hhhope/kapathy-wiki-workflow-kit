# Archive Review

Review date: 2026-05-06

Decision: **PASS**

## Summary

The change is complete and archive-ready. It adds a repo-default evidence gate
for promoting captured learning into behavior assets, while keeping source
capture, skills, root dotfiles, wiki method pages, and automation out of scope.

## Checks

| Check | Result | Evidence | Reason |
|---|---|---|---|
| OpenSpec artifacts complete | pass | `openspec status --change require-evidence-backed-best-practices --json` returned `isComplete: true` | The missing `design.md` lifecycle artifact has been added. |
| Validation passed | pass | `openspec validate require-evidence-backed-best-practices --strict` returned valid | PostHog DNS noise did not affect local validation. |
| Landing layer held | pass | `proposal.md`, `design.md`, `evaluation.md` | The gate lands in repo `AGENTS.md`, not root `AGENTS.md` or a skill. |
| Evidence shapes bounded | pass | `tasks.md` and spec delta | Accepted evidence shapes remain exactly external-document excerpt, local demo/fixture, or git-like project comparison. |
| Scope did not expand | pass | `design.md` Non-Goals and `evaluation.md` Self-Check | No skill, wiki method page, root dotfile rule, replay harness, or automation was added. |

## Residual Risk

The gate is prose-level and depends on future agents following repo
`AGENTS.md`. Mechanical enforcement remains out of scope unless a later change
shows repeated unsupported promotions.
