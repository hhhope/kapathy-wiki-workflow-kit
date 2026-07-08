# Tasks

- [x] 1. Create OpenSpec proposal, design, spec delta, and evaluation record.
- [x] 2. Capture pre-sync drift between `/mnt/d/skills/account-skills` and `skills-drafts/account-skills`.
- [x] 3. Refresh `skills-drafts/account-skills/` from the external source using the mirror copy policy.
- [x] 4. Run mirror diff, exclusion checks, representative tests, OpenSpec validation, and behavior-asset validation.
- [x] 5. Commit scoped task-related files and stop at the OpenSpec completion boundary.

## Verification

- Pre-sync drift:
  - `diff -qr ... /mnt/d/skills/account-skills skills-drafts/account-skills | wc -l` -> 58 effective differences with mirror exclusions.
- Mirror parity:
  - `diff -qr --exclude='.git' --exclude='.claude-plugin' --exclude='.codex-plugin' --exclude='.idea' --exclude='.agents' --exclude='graphify-out' --exclude='__pycache__' --exclude='README.md' --exclude='account-cr-agent/README.md' --exclude='test_cr_agent_plugin_marketplace.py' /mnt/d/skills/account-skills skills-drafts/account-skills` -> exit 0, no output.
- Exclusion check:
  - `find skills-drafts/account-skills ...` for excluded paths -> no output after removing generated `__pycache__`.
- Representative tests:
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills-drafts/account-skills/tests` -> 13 tests passed.
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills-drafts/account-skills/account-cr-agent/skills/cr-agent/tests` -> 22 tests passed.
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills-drafts/account-skills/account-cr-agent/skills/release-diff-cr/tests` -> 3 tests passed.
- OpenSpec:
  - `openspec validate sync-account-skills-full-mirror --strict` -> valid, with non-blocking PostHog telemetry DNS errors after validation.
- Behavior asset checker:
  - `python3 scripts/check_behavior_assets.py` -> non-zero due to unrelated active changes: `enforce-named-skill-gate`, `initialize-llm-wiki-seed-repo`, `prefer-native-image-text-output`, and `realign-stripe-h5-redesign-sections`; no error referenced `sync-account-skills-full-mirror`.
- Whitespace:
  - `git diff --check -- skills-drafts/account-skills openspec/changes/sync-account-skills-full-mirror` -> exit 0, no output.
