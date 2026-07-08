# Evaluation

## Pressure Scenarios

### Positive full mirror sync

Input or situation shape: user asks whether account-skills was really synced
and points out that no full `account-skills` commit is visible.

Trigger condition: external `/mnt/d/skills/account-skills` differs from
`skills-drafts/account-skills` outside the previously synced CR subset.

Expected route: create a scoped OpenSpec change, refresh the repo mirror under
`skills-drafts/account-skills/`, preserve no-plugin README boundary files, and
verify source/target parity with documented exclusions.

Repo-visible artifact: this OpenSpec change plus the refreshed
`skills-drafts/account-skills/` tree.

Expected output: a commit that clearly records the full mirror refresh.

Promotion or non-promotion boundary: the mirror remains draft/reference content
and does not become active `.codex/skills` runtime registration.

Proof boundary: file parity and representative tests prove this local mirror
sync, not plugin publication or future runtime reload.

### Negative should-not-trigger runtime install

Input or situation shape: user asks about syncing the account-skills mirror, not
installing skills into active runtime.

Trigger condition: the target path is repo mirror content, not
`$CODEX_HOME/skills`.

Expected route: do not add new active `.codex/skills` registrations and do not
claim plugin publication.

Repo-visible artifact: absence of `.codex/skills` edits for this change.

Expected output: repository mirror update only.

Promotion or non-promotion boundary: future promotion of individual skills
requires separate evaluation.

Proof boundary: scoped git diff and path checks.

## RED Baseline

- Full mirror diff before sync had 58 effective differences after excluding
  local/plugin/generated state and the two repo-specific README files.
- Drift included `codex-integration-kit`, `req-agent-kit`, root `skills/*`,
  visual/diagram skills, source tests, and documentation.
- Source included plugin marketplace test coverage that depends on
  `.claude-plugin` manifests. Keeping that test while excluding plugin
  manifests produced failing mirror tests, proving it belongs to the excluded
  plugin packaging surface.

## GREEN Result

- Refreshed `skills-drafts/account-skills/` from
  `/mnt/d/skills/account-skills/` with the mirror copy policy.
- Preserved repo-specific no-plugin README files:
  `skills-drafts/account-skills/README.md` and
  `skills-drafts/account-skills/account-cr-agent/README.md`.
- Excluded plugin/local/generated state:
  `.git/`, `.claude-plugin/`, `.codex-plugin/`, `.idea/`, `.agents/`,
  `graphify-out/`, `__pycache__/`, and
  `tests/test_cr_agent_plugin_marketplace.py`.
- Mirror parity command with those documented exclusions returned exit 0 with
  no output.
- Exclusion-path check returned no paths after removing generated `__pycache__`.
- Representative tests:
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills-drafts/account-skills/tests`
    -> 13 tests passed.
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills-drafts/account-skills/account-cr-agent/skills/cr-agent/tests`
    -> 22 tests passed.
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills-drafts/account-skills/account-cr-agent/skills/release-diff-cr/tests`
    -> 3 tests passed.
- `openspec validate sync-account-skills-full-mirror --strict` returned valid.
  PostHog telemetry DNS flush failed after validation, without changing the
  validation result.
- `git diff --check -- skills-drafts/account-skills openspec/changes/sync-account-skills-full-mirror`
  returned exit 0 with no output.
- `python3 scripts/check_behavior_assets.py` returned non-zero only for
  unrelated active changes: `enforce-named-skill-gate`,
  `initialize-llm-wiki-seed-repo`, `prefer-native-image-text-output`, and
  `realign-stripe-h5-redesign-sections`. It did not report this change.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md` workflow and behavior-asset gates.
- `PROJECT.md` OpenSpec source-of-truth declaration.
- `openspec/changes/mirror-account-skills-no-plugin/*`.
- `openspec/changes/sync-account-cr-agent-mirror/*`.
- `skills-drafts/account-skills/README.md`.
- `/home/yan/.codex/skills/migrating-skills/SKILL.md`.
- `/home/yan/.codex/skills/.system/skill-installer/SKILL.md`.

Owns:

- Refreshing repo-visible account-skills mirror content.
- Preserving no-plugin mirror boundary and validation evidence.

References:

- Existing account-skills mirror policy.
- External `/mnt/d/skills/account-skills` source.

Rejects:

- Creating `skills/account-skills/`.
- Copying plugin/local/generated state.
- Treating the mirror sync as active installation or plugin publication.

## Residual Risks

- This proves source-to-repo mirror parity with documented no-plugin
  exclusions; it does not publish a plugin or activate the imported skills in
  the current Codex runtime.
- The preserved repo-specific README files intentionally differ from the source
  package README files.
- Source plugin marketplace tests are excluded because their required manifests
  are also excluded from this no-plugin mirror.
