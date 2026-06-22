# Evaluation: mirror account-skills without plugin mode

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: workflow change gate, behavior asset prior-art gate, output
  routing, and skill authoring/migration boundaries.
- `PROJECT.md`: OpenSpec source-of-truth model.
- `/home/yan/.codex/skills/migrating-skills/SKILL.md`: mirror/adapt/wrapper
  decision model and dependency review.
- `/home/yan/.codex/skills/.system/skill-installer/SKILL.md`: direct installer
  scope; not used because the source is a local path and the target is a repo
  mirror, not `$CODEX_HOME/skills`.
- `/home/yan/.codex/skills/writing-skills/SKILL.md` and
  `/home/yan/.codex/skills/test-driven-development/SKILL.md`: skill content
  gate. This change mirrors source skills without semantic edits to each
  `SKILL.md`; README wrapping is evaluated here.
- `.codex/skills/public-report-quality-gate/SKILL.md`: README as repo-public
  lightweight path.
- Source `/mnt/d/skills/account-skills/README.md` and `PROJECT.md`.

Classification:

- Owns: repo-local mirror location, no-plugin boundary, and mirror README.
- References: source account-skills package, source reusable kits, repo
  skill-draft boundary.
- Rejects: plugin marketplace installation, active `.codex/skills` runtime
  registration, semantic rewrites of imported skills, and copying local state.

## Pressure Scenarios

### Scenario 1: positive mirror request

- Input or situation shape: user asks to upload `D:\skills\account-skills` here
  and says not to use plugin mode.
- Trigger condition: local external skills package plus explicit no-plugin
  constraint.
- Expected route or stop behavior: mirror ordinary content under
  `skills-drafts/account-skills/`, exclude plugin/local/generated state, and
  write a direct-use README.
- Repo-visible artifact: `skills-drafts/account-skills/README.md` and this
  OpenSpec change.
- Expected output or non-output: no plugin marketplace install commands as the
  primary route.
- Promotion or non-promotion boundary: mirrored skills remain draft/reference
  until a later promotion change evaluates individual skills.
- Proof boundary: file presence/exclusion checks and README text checks, not
  source test-suite acceptance.

### Scenario 2: negative should-not-trigger active skill install

- Input or situation shape: user asks for upload/mirror, not runtime install.
- Trigger condition: target is the current repo, not `$CODEX_HOME/skills`.
- Expected route or stop behavior: do not install the package into
  `.codex/skills/` and do not update AGENTS routing.
- Repo-visible artifact: absence of new `.codex/skills/account-*` files and no
  AGENTS route changes.
- Expected output or non-output: no active runtime dependency claim.
- Promotion or non-promotion boundary: individual skill promotion is a separate
  OpenSpec change.
- Proof boundary: scoped `git diff --name-only` and path checks.

## RED Baseline

- `skills-drafts/account-skills/` did not exist.
- Source `/mnt/d/skills/account-skills` contains `.claude-plugin/`, `.git/`,
  `.idea/`, and `graphify-out/`, so a blind copy would violate the user's
  no-plugin/local-state boundary.
- Source README contains plugin marketplace instructions; using it unchanged
  would violate the user's "不用plugin模式" instruction.

## GREEN Result

Actual implementation evidence:

- `skills-drafts/account-skills/` exists with 315 mirrored files.
- Expected ordinary source paths are present:
  `skills/`, `account-cr-agent/`, `codex-integration-kit/`,
  `req-agent-kit/`, `openspec/`, `tests/`, `.codex/`, `.githooks/`,
  and `README.md`.
- Exclusion check returned no paths for `.claude-plugin`, `.codex-plugin`,
  `.git`, `.idea`, `graphify-out`, or `__pycache__` under the mirror.
- README command scan returned no plugin install/marketplace command hits in
  mirrored README files.
- `skills-drafts/account-skills/README.md` states this is a non-plugin mirror,
  is not installed as a Codex plugin, is not registered in AGENTS, and requires
  a separate promotion change before runtime use.
- `skills-drafts/account-skills/account-cr-agent/README.md` was rewritten to
  describe direct bundle usage instead of plugin installation.
- The preserved historical document
  `skills-drafts/account-skills/codex-integration-kit/docs/feishu-codex-governance-share.md`
  still contains source-era plugin workflow text; root README explicitly marks
  such mentions as source history, not the usage path for this mirror.
- `openspec validate mirror-account-skills-no-plugin --strict` passed. The CLI
  emitted PostHog DNS flush warnings after validation in the restricted network,
  but the change validation itself returned exit code 0.
- `git diff --check -- skills-drafts/account-skills openspec/changes/mirror-account-skills-no-plugin`
  passed.
- `python3 scripts/check_behavior_assets.py` returned non-zero only for
  pre-existing `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`
  missing required evaluation sections; no error referenced this change.

## Residual Risks

- This change mirrors source content but does not make each imported skill
  production-ready in this repo.
- Source test execution is out of scope; imported tests are preserved as source
  material.
- Future promotion into `.codex/skills` requires separate skill evaluation and
  local governance wiring.
