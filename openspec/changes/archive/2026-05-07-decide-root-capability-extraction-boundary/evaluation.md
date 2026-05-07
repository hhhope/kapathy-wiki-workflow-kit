## RED Baseline

Date: 2026-05-07

| Scenario | Current Evidence | RED Result |
|---|---|---|
| Repo High-Frequency Skills distinguishes runtime trigger from ownership | `AGENTS.md` lists skill triggers but does not state ownership status per row. | FAIL |
| Generic principle skills are marked as root candidates | `clarify-before-acting`, `simplicity-first`, `surgical-changes`, and `verify-before-claiming` are repo-local rows without root-candidate labeling. | FAIL |
| Repo-owned workflow skills are distinguishable from root candidates | `material-collaboration-defaults` and `meeting-note-output` sit in the same table shape as generic principle skills. | FAIL |
| Root candidates are blocked from direct root promotion | Existing root-governance specs block unsupported promotion, but repo runtime map does not expose candidate status at the trigger row. | FAIL |

## GREEN Result

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Repo High-Frequency Skills distinguishes runtime trigger from ownership | repo `AGENTS.md` states the table is a runtime routing map, not an ownership map, and adds an Ownership column. | PASS |
| Generic principle skills are marked as root candidates | `clarify-before-acting`, `simplicity-first`, `surgical-changes`, and `verify-before-claiming` are marked `root-candidate`. | PASS |
| Repo-owned workflow skills are distinguishable from root candidates | `material-collaboration-defaults` and `meeting-note-output` are marked `repo-owned`. | PASS |
| Shared skills keep local repo detail visible | OpenSpec skills and `learning-capture` are marked `shared` with repo-local detail called out. | PASS |
| Root candidates are blocked from direct root promotion | ADR-0031 states root candidates require a root-focused OpenSpec change and evaluation evidence before promotion. | PASS |
| Gap root cause is durable outside chat | `wiki/ops/root-capability-extraction-retro.md` records runtime availability being misread as behavior ownership. | PASS |

## Residual Risks

- Ownership labels are documentation-level guidance, not automated enforcement.
- Root-candidate skills still live physically under repo `.codex/skills/` until
  a successor root-focused change decides whether to migrate or duplicate them.
- The change does not edit root `~/.codex/AGENTS.md`, so cross-repo runtime
  behavior is not changed yet.
- Existing agents may still load the repo skill by trigger; this change only
  prevents ownership confusion in repo-visible governance.
