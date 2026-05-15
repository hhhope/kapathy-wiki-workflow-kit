# Evaluation: wiki medical agent state machine

## Behavior Asset Change

This change creates `.codex/skills/wiki-medical-agent/SKILL.md` and changes
old stage skills to redirect ordinary usage to the medical agent.

## Routing Ownership

`wiki-medical-agent` is a high-level router/gate for ordinary user-facing
medical-loop intent. The existing stage skills remain module/debug evidence
helpers and do not own normal user entry.

## Prior-Art / Common-Rule Dedupe

- Scanned: repo `AGENTS.md`, `PROJECT.md`, active OpenSpec proposal/design/tasks,
  `openspec/specs/skill-authoring-contract/spec.md`,
  `openspec/specs/skill-evaluation-evidence/spec.md`,
  `openspec/specs/local-skill-pressure-tests/spec.md`,
  `openspec/specs/behavior-replay-gate/spec.md`,
  `wiki/ops/llm-wiki-self-evolution-medical-loop.md`,
  `wiki/ops/wiki-medical-case-file-drift-retro-2026-05-15.md`,
  `wiki/adr/0006-formal-project-local-skills-over-drafts.md`,
  `wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md`,
  and the five existing stage skills.
- Owns: repo-specific medical-loop entry, case-file authority, and redirect
  wording for `wiki-doctor`, `wiki-confirm`, `wiki-treatment`, `wiki-surgery`,
  and `wiki-recovery`.
- References: existing global/repo behavior-asset gates, TDD workflow,
  OpenSpec lifecycle authority, and the repo medical-loop case-file model.
- Rejects: duplicating generic git discipline, test thresholds, or full
  behavior-asset evaluation rules inside the skill body.

## Pressure Scenarios

- User invokes `wiki-treatment apply 已确认的 10 个`.
- User invokes `wiki-recovery` after treatment.
- User invokes `wiki-doctor` for ordinary diagnosis.
- User explicitly asks for legacy/debug stage evidence.

Positive trigger scenario:

- Input or situation shape: ordinary user asks for diagnosis, treatment apply,
  surgery planning, recovery, status, or archive check in the wiki medical
  loop.
- Trigger condition: the request is a normal user-facing medical-loop request,
  not an explicit legacy/debug evidence request.
- Expected route: route through `.codex/skills/wiki-medical-agent/SKILL.md`,
  then the medical agent resolves the active case and delegates to the bounded
  worker.
- Repo-visible artifact: `.codex/skills/wiki-medical-agent/SKILL.md` and the
  active case file under `wiki/ops/wiki-medical-cases/`.
- Expected output: response shows Intent, Case, State, Allowed action, any
  Blocked action, and Next Action.
- Promotion or non-promotion boundary: `Confirmed Decisions` may be executed
  when all approvals and state checks pass; `Proposed Decisions` and stage
  records are not executable.
- Proof boundary: local skill tests prove routing text and required surfaces;
  runtime CLI/state-machine tests remain the stronger enforcement proof.

Negative should-not-trigger scenario:

- Input or situation shape: user explicitly asks for legacy/debug evidence
  from `wiki-doctor`, `wiki-confirm`, `wiki-treatment`, `wiki-surgery`, or
  `wiki-recovery`.
- Trigger condition: the request names direct stage evidence and does not ask
  the agent to mutate case state.
- Expected route: direct stage skill usage is allowed only as legacy/debug
  evidence.
- Repo-visible artifact: the relevant stage skill under `.codex/skills/`.
- Expected output: stage output is described as evidence only and not as case
  authority.
- Promotion or non-promotion boundary: direct stage output must not become
  authoritative and must not update case state unless routed through the
  medical agent and written back to the active case file.
- Proof boundary: local skill tests verify every downgraded stage skill carries
  the redirect and legacy/debug boundary.

Parent gate preservation:

- The new user-facing skill preserves the OpenSpec lifecycle parent gate by
  forbidding mutation of OpenSpec lifecycle state unless a separate approved
  workflow scopes it.
- The stage skills preserve the medical-agent parent gate for ordinary use and
  remain direct-entry helpers only for legacy/debug evidence.

## RED Baseline

Before this change, `tests/test_wiki_medical_loop_skills.py` did not find a
normal `wiki-medical-agent` entry or redirect wording in stage skills.

Command:

```bash
python3 -m unittest tests.test_wiki_medical_loop_skills -v
```

Result: failed with 6 expected failures: missing
`.codex/skills/wiki-medical-agent/SKILL.md` and missing ordinary-use redirect
wording in `wiki-doctor`, `wiki-confirm`, `wiki-treatment`, `wiki-surgery`, and
`wiki-recovery`.

## GREEN Result

After this change, skill tests verify the new entry and redirect boundary.

- `python3 -m unittest tests.test_wiki_medical_loop_skills -v` passed, 5 tests.
- `python3 scripts/check_behavior_assets.py` passed.

## Residual Risks

Local skill text cannot prove every future agent will comply. Runtime CLI
guards and state-machine tests provide the stronger enforcement layer.

## Verification Commands

```text
python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_medical_case tests.test_wiki_treatment tests.test_wiki_recovery tests.test_wiki_medical_loop_skills -v
openspec validate introduce-wiki-medical-agent-state-machine --strict
python3 scripts/check_behavior_assets.py
```

## Replay Results

- Status request reports intent, case, state, allowed action, and next action.
- Apply request with matching confirmed count applies treatment, runs recovery,
  attaches records, and updates the case next action.
- Apply request with mismatched count is blocked.
- Multiple active cases block write actions.
- Old stage skills redirect ordinary usage to `wiki-medical-agent`.

Actual command results:

- `python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_medical_case tests.test_wiki_treatment tests.test_wiki_recovery tests.test_wiki_medical_loop_skills -v`: PASS, 52 tests ran in 9.059s, `OK`.
- `openspec validate introduce-wiki-medical-agent-state-machine --strict`: PASS, reported `Change 'introduce-wiki-medical-agent-state-machine' is valid`.
- OpenSpec telemetry warning: validation printed PostHog network flush warnings for `edge.openspec.dev` with `getaddrinfo EAI_AGAIN`; the command still exited 0 after reporting the change valid.
- `python3 scripts/check_behavior_assets.py`: PASS, exited 0 with no output.
- Frontmatter taxonomy check: not run; Task 10 added no repository wiki case outputs, only temporary test fixtures.
