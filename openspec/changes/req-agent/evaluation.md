# Evaluation

## Pressure Scenarios

Positive controller trigger:

- Input: `看这个需求能不能进开发`
- Expected: load `req-agent`, report Intent, Case, State, Allowed Action,
  Blocked Action when blocked, Next Action, and Evidence.
- Expected route: controller first; internal scripts may collect evidence but
  the user is not asked to run Python as the normal path.

Positive worker routing trigger:

- Input: `req-agent 已判断下一步需要补验收映射`
- Expected: `req-agent` may route to `req-acceptance`; the worker stays inside
  observable acceptance functions and bidirectional story mappings.

Negative / should-not-trigger:

- Input: ordinary wiki frontmatter repair.
- Expected: use the wiki frontmatter taxonomy path, not `req-agent`.

Parent gate preservation:

- Input: a generated OpenSpec draft is created by `req-handoff`.
- Expected: preserve the OpenSpec lifecycle parent gate; draft creation stops
  the requirements flow and does not approve implementation.

## RED Baseline

Command:

```bash
python3 -m unittest tests.test_req_agent_skills
```

Result before adding the `req-*` skills:

- Failed because `.codex/skills/req-agent/SKILL.md` did not exist.
- Failed because worker skill files did not exist.
- Failed because the superseded
  `openspec/changes/add-requirements-analysis-agent-skill-entry` artifacts were
  still present.

This captures both old failure modes: no Codex-facing `req-agent` route and
the narrower single-entry direction still occupying the workflow.

## GREEN Result

Command:

```bash
python3 -m unittest tests.test_req_agent_skills
```

Result after adding the six skills and retiring the narrow artifacts:

```text
Ran 3 tests in 0.072s

OK
```

The new skill surface is:

- `.codex/skills/req-agent/SKILL.md`
- `.codex/skills/req-intake/SKILL.md`
- `.codex/skills/req-scope/SKILL.md`
- `.codex/skills/req-stories/SKILL.md`
- `.codex/skills/req-acceptance/SKILL.md`
- `.codex/skills/req-handoff/SKILL.md`

Focused regression command:

```bash
python3 -m unittest tests.test_req_agent_skills tests.test_requirements_analysis_agent
```

Result:

```text
Ran 14 tests in 0.346s

OK
```

OpenSpec validation:

```bash
openspec validate req-agent --strict
```

Result: `Change 'req-agent' is valid`. The command exited 0. OpenSpec printed
PostHog telemetry DNS errors after validation; those did not affect the
validation result.

Behavior-asset checks:

```bash
python3 scripts/check_behavior_assets.py
```

Result: non-zero due to unrelated pre-existing active change
`openspec/changes/initialize-llm-wiki-seed-repo`. The output did not report
`openspec/changes/req-agent`.

Targeted req-agent evaluation check:

```bash
python3 -c "from pathlib import Path; from scripts.check_behavior_assets import load_config, check_evaluation; root=Path('.').resolve(); entries=check_evaluation(root/'openspec/changes/req-agent', root, load_config(root)); [print(f'{e.severity} {e.kind} {e.path}: {e.message}') for e in entries]; raise SystemExit(1 if any(e.severity == 'error' for e in entries) else 0)"
```

Result: exit 0 with no entries.

## Behavior Replay

Input or situation shape: user asks for requirement intake, readiness,
requirement gate, user stories, acceptance functions, or OpenSpec draft
handoff.

Trigger condition: ordinary requirements work before development.

Expected route: load `req-agent` as the single normal Codex-facing controller.

Repo-visible artifact: `.codex/skills/req-agent/SKILL.md` plus worker skills
under `.codex/skills/req-*`.

Expected output: Intent, Case, State, Allowed Action, Blocked Action when
blocked, Next Action, and Evidence.

Promotion or non-promotion boundary: Python scripts remain internal evidence
tools; worker skills do not become ordinary entry points; generated OpenSpec
drafts do not authorize implementation.

Proof boundary: this verifies the repo-local skill surface and routing
contract. It does not prove semantic extraction quality beyond existing
requirements scripts and future live usage.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `openspec/changes/req-agent`
- `openspec/changes/add-requirements-analysis-agent`
- `wiki/ops/requirements-agent-skill-isolation-explore-2026-05-29.md`
- `wiki/ops/moc-medical-agent-review-process-2026-05-19.md`
- `.codex/skills/wiki-medical-agent/SKILL.md`
- `/home/yan/.codex/rules/common/development-workflow.md`
- `/home/yan/.codex/rules/common/testing.md`

Owns:

- `req-agent` as the normal requirements controller.
- Worker boundaries for `req-intake`, `req-scope`, `req-stories`,
  `req-acceptance`, and `req-handoff`.
- Retirement of the narrow single `requirements-analysis-agent` skill-entry
  direction.

References:

- OpenSpec lifecycle and hard stops remain governed by repo `AGENTS.md`.
- Requirements taxonomy authority remains
  `requirements/config/requirements-taxonomy.yaml`.
- Existing Python helper behavior remains under
  `openspec/changes/add-requirements-analysis-agent`.
- Skill authoring/evaluation gates remain governed by repo `AGENTS.md` and
  common behavior-asset rules.

Rejects:

- Duplicating requirements taxonomy vocabulary inside skills.
- Asking users to run Python as the normal requirements path.
- Treating worker skills as normal entry points.
- Treating generated OpenSpec drafts as implementation approval.

## Residual Risks

- The skill files constrain routing behavior; they do not add new extraction
  intelligence.
- The first implementation intentionally keeps worker bodies compact. If a
  worker becomes complex, add references or a follow-up OpenSpec change instead
  of bloating `SKILL.md`.
- The full behavior-asset checker is currently blocked by unrelated
  `initialize-llm-wiki-seed-repo` evaluation debt. This change has targeted
  `req-agent` evaluation proof, but the repository-wide checker remains
  non-zero until that separate change is fixed or archived.
- The old narrow artifacts were untracked local files, so retirement is visible
  as their absence from the worktree rather than a tracked deletion diff.
