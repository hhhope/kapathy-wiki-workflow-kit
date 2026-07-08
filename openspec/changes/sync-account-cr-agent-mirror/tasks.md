# Tasks

- [x] 1. Add OpenSpec proposal, design, spec delta, and evaluation skeleton.
- [x] 2. Capture RED baseline for repo mirror drift and report-contract conflict.
- [x] 3. Sync installed `account-cr-agent` skill bundle into `skills-drafts/account-skills/` mirrors, excluding transient caches.
- [x] 4. Run replay and unit validation for the synced mirror.
- [x] 5. Run OpenSpec and behavior-asset validation, recording expected unrelated blockers.
- [x] 6. Commit scoped task-related files and stop at the OpenSpec completion boundary.
- [x] 7. Repair CR review finding: satisfied checker results now close linked diff units before gate re-evaluation.
- [x] 8. Sync repaired CR skill files back to external account-skills and local installed caches.

## Verification

- RED baseline recorded in `evaluation.md`.
- Bundle parity after sync:
  - `diff -qr --exclude='__pycache__' /home/yan/.codex/plugins/cache/account-skills/account-cr-agent/0.1.1/skills skills-drafts/account-skills/account-cr-agent/skills` -> exit 0, no output.
- Root mirror parity after sync:
  - `for skill in cr-agent cr-branch-governance cr-diff cr-evidence cr-gate cr-intake cr-issues cr-replay cr-report cr-scope cr-technical-review release-diff-cr; do diff -qr --exclude='__pycache__' "/home/yan/.codex/skills/$skill" "skills-drafts/account-skills/skills/$skill" || exit 1; done` -> exit 0, no output.
- CR coverage tests:
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills-drafts/account-skills/account-cr-agent/skills/cr-agent/tests` -> 22 tests passed.
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills-drafts/account-skills/skills/cr-agent/tests` -> 22 tests passed.
- CR replay:
  - `env PYTHONDONTWRITEBYTECODE=1 python3 skills-drafts/account-skills/account-cr-agent/skills/cr-agent/scripts/eval_cr_replay.py ...` -> validated 4 replay fixture(s).
- Release diff tests:
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest skills-drafts.account-skills.account-cr-agent.skills.release-diff-cr.tests.test_release_diff_report` -> 3 tests passed.
- External account-skills sync after CR repair:
  - `diff -qr --exclude='__pycache__' ... /mnt/d/skills/account-skills/...` for `cr-agent`, `cr-gate`, `cr-report`, and `release-diff-cr` in both layouts -> exit 0, no output.
  - `/mnt/d/skills/account-skills/skills/cr-agent/tests` -> 22 tests passed.
  - `/mnt/d/skills/account-skills/account-cr-agent/skills/cr-agent/tests` -> 22 tests passed.
  - `/mnt/d/skills/account-skills/account-cr-agent/skills/release-diff-cr/tests` -> 3 tests passed.
- OpenSpec:
  - `openspec validate sync-account-cr-agent-mirror --strict` -> valid, with non-blocking PostHog telemetry network flush errors after validation.
- Behavior asset checker:
  - `python3 scripts/check_behavior_assets.py` -> non-zero due to unrelated
    active changes: `enforce-named-skill-gate`,
    `initialize-llm-wiki-seed-repo`, `prefer-native-image-text-output`, and
    `realign-stripe-h5-redesign-sections`. It no longer reports
    `sync-account-cr-agent-mirror`.

## Completion Boundary

All scoped tasks are complete. Per repo OpenSpec boundary, stop implementation
after committing this change; default next action is archive review, not more
adjacent CR-agent repair.
