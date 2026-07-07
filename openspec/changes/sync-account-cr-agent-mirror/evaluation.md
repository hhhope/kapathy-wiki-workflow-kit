# Evaluation

## Pressure Scenarios

### Positive trigger scenario

Input or situation shape: user asks to sync the repo mirror after exploration
shows that `skills-drafts/account-skills/account-cr-agent/skills/cr-agent/`
contains only the old minimal skill files while the installed
`account-cr-agent` bundle contains coverage-gate source.

Trigger condition: the target is a non-runtime mirror under
`skills-drafts/account-skills/`, not `.codex/skills/` publication.

Expected route: create an active OpenSpec change, classify the work as
`mirror`, copy ordinary installed source files into the repo mirror, validate
the mirror, and keep runtime activation out of scope.

Repo-visible artifact: this OpenSpec change plus
`wiki/ops/cr-agent-issues-explore-2026-07-07.md`.

Expected output: the mirror includes `rules/global.yaml`,
`scripts/coverage_gate.py`, coverage support modules, 4 replay fixtures, and 21
coverage tests; validation commands pass against the mirrored files.

Promotion or non-promotion boundary: the copied mirror is source/reference
material only. It is not plugin publication, runtime cache upgrade, or active
repo `.codex/skills` registration.

Proof boundary: this proves local mirror parity with the selected installed
source on this machine. It does not prove future sessions use the mirror, and it
does not publish a new plugin version.

### Negative or should-not-trigger scenario

Input or situation shape: user asks whether `cr-agent` has problems or asks for
analysis without requesting a sync.

Trigger condition: read-only exploration or candidate learning should not mutate
behavior assets.

Expected route: create or update a `wiki/ops` explore trace and report findings
without copying files or editing skills.

Repo-visible artifact: `wiki/ops/cr-agent-issues-explore-2026-07-07.md`.

Expected output: no `skills-drafts/` files are changed; any sync or promotion
requires a follow-up OpenSpec implementation request.

Promotion or non-promotion boundary: candidate learning from
`open-code-review` remains candidate-only and is not promoted into CR agent hard
rules by this sync.

Proof boundary: this negative scenario is a routing boundary, not a test that
the runtime agent will refuse every future ambiguous edit request.

### Parent gate preservation

`cr-agent` remains the parent router/gate for CR lifecycle behavior.
`cr-report` remains a rendering module and must not recalculate `cr-gate`.
`release-diff-cr` remains a diff/evidence helper and must not replace
`cr-agent` gate decisions. The mirror sync preserves those installed
relationships; it does not make mirrored draft folders active runtime routes in
this repository.

## RED Baseline

- File inventory before sync:
  - `find skills-drafts/account-skills/account-cr-agent/skills/cr-agent -maxdepth 3 -type f | sort`
  - Result: only `SKILL.md`, `replay/mandao-customer-keytype.json`, and
    `scripts/eval_cr_replay.py` existed.
- Installed source inventory:
  - `find /home/yan/.codex/plugins/cache/account-skills/account-cr-agent/0.1.1/skills/cr-agent -maxdepth 3 -type f | sort | rg -v '__pycache__'`
  - Result: included `rules/global.yaml`, `rules/rule-schema.json`,
    `scripts/coverage_gate.py`, `scripts/coverage_model.py`,
    `scripts/coverage_results.py`, `scripts/coverage_config.py`, 4 replay
    fixtures, and 3 coverage test files.
- Contract drift scan:
  - `rg -n "Coverage gate|coverage_gate|global.yaml|Report State|plugin_plain|repo_existing|Include frontmatter|\\[!todo\\]" skills-drafts/account-skills/account-cr-agent/skills/...`
  - Result before sync: mirrored `cr-agent` did not contain the installed
    coverage-gate terms; `release-diff-cr` still had frontmatter and `[!todo]`
    evidence inherited from the selected installed source.
- Baseline conclusion: repo mirror was not a faithful copy of the currently
  installed CR agent source and could not be used as accurate promotion or
  diagnosis evidence.

## GREEN Result

- Synced bundle mirror:
  - Source:
    `/home/yan/.codex/plugins/cache/account-skills/account-cr-agent/0.1.1/skills/`
  - Target:
    `skills-drafts/account-skills/account-cr-agent/skills/`
  - Command shape: `rsync -a --exclude '__pycache__/' ...`
- Synced root skill mirror:
  - Source: `/home/yan/.codex/skills/{cr-*,release-diff-cr}/`
  - Target: `skills-drafts/account-skills/skills/{cr-*,release-diff-cr}/`
  - Command shape: `rsync -a --exclude '__pycache__/' ...`
- Bundle parity:
  - `diff -qr --exclude='__pycache__' /home/yan/.codex/plugins/cache/account-skills/account-cr-agent/0.1.1/skills skills-drafts/account-skills/account-cr-agent/skills`
  - Result: exit 0, no output.
- Root mirror parity:
  - `for skill in cr-agent cr-branch-governance cr-diff cr-evidence cr-gate cr-intake cr-issues cr-replay cr-report cr-scope cr-technical-review release-diff-cr; do diff -qr --exclude='__pycache__' "/home/yan/.codex/skills/$skill" "skills-drafts/account-skills/skills/$skill" || exit 1; done`
  - Result: exit 0, no output.
- Coverage tests:
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills-drafts/account-skills/account-cr-agent/skills/cr-agent/tests`
  - Result: 21 tests passed.
- Replay fixtures:
  - `env PYTHONDONTWRITEBYTECODE=1 python3 skills-drafts/account-skills/account-cr-agent/skills/cr-agent/scripts/eval_cr_replay.py ...`
  - Result: validated 4 replay fixture(s).
- Release diff tests:
  - `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest skills-drafts.account-skills.account-cr-agent.skills.release-diff-cr.tests.test_release_diff_report`
  - Result: 3 tests passed.
- Key mirrored terms:
  - `rg -n "Coverage gate is mandatory|Report State: stage_report|plugin_plain|repo_existing|rules/global.yaml|known-good-empty-range|webank-split-balance-unit|yqt-formal-report-repo-existing" skills-drafts/account-skills/account-cr-agent/skills/cr-agent skills-drafts/account-skills/account-cr-agent/skills/cr-report`
  - Result: expected installed coverage/profile/replay terms found.
- OpenSpec:
  - `openspec validate sync-account-cr-agent-mirror --strict`
  - Result: valid. PostHog telemetry flush printed a network error after the
    validation result; it did not change the OpenSpec validation status.
- Behavior asset checker:
  - `python3 scripts/check_behavior_assets.py`
  - Result after this evaluation update: non-zero due to unrelated active
    changes: `enforce-named-skill-gate`, `initialize-llm-wiki-seed-repo`,
    `prefer-native-image-text-output`, and
    `realign-stripe-h5-redesign-sections`. It no longer reports
    `sync-account-cr-agent-mirror`.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md` repo gates for behavior assets, skill authoring, OpenSpec boundary,
  named skills, and prior-art dedupe.
- `PROJECT.md` source-of-truth declaration.
- `openspec/changes/mirror-account-skills-no-plugin/*`, especially the completed
  mirror boundary.
- `openspec/specs/skill-authoring-contract/spec.md`.
- `openspec/specs/skill-evaluation-evidence/spec.md`.
- `openspec/specs/local-skill-pressure-tests/spec.md`.
- `openspec/specs/behavior-replay-gate/spec.md`.
- `openspec/changes/mirror-account-skills-no-plugin/specs/account-skills-mirror/spec.md`.
- `wiki/ops/cr-agent-issues-explore-2026-07-07.md`.
- Installed sources under `/home/yan/.codex/skills/` and
  `/home/yan/.codex/plugins/cache/account-skills/account-cr-agent/0.1.1/skills/`.

Owns:

- Repo-visible mirror parity for `account-cr-agent` skill source under
  `skills-drafts/account-skills/`.
- Evaluation evidence for this mirror sync.
- Non-runtime distinction between mirrored draft/reference source and active
  skill installation.

References:

- Skill authoring/TDD rules provide the evidence shape and pressure-test
  requirement.
- Behavior replay gate provides the future-behavior proof boundary vocabulary.
- Prior mirror change provides the non-plugin mirror boundary and target
  directory.
- Installed `account-cr-agent` source is the selected source of truth for this
  sync.

Rejects:

- Editing `/home/yan/.codex/plugins/cache/...` as a durable source repair.
- Claiming this repo mirror update is a plugin release, install, or runtime
  session refresh.
- Promoting `open-code-review` candidate learning into CR agent hard rules in
  this change.
- Reopening or modifying the completed `mirror-account-skills-no-plugin` change.

## Residual Risks

- `release-diff-cr` still contains installed-source behavior that may preserve
  frontmatter or `[!todo]` output in some paths. This sync mirrors the selected
  installed source; it does not semantically redesign release-diff output.
- The current Codex session may already have loaded skill metadata; this mirror
  update does not reload runtime skills.
- Multi-session rollout proof and plugin publication are out of scope.
- `python3 scripts/check_behavior_assets.py` has known unrelated active-change
  failures in this repository; this change can only clear its own evaluation
  findings.
