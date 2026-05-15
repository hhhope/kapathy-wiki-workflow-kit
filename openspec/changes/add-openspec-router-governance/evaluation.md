# Evaluation

## Scope

This evaluation verifies project-level governance integration for
`openspec-router`. It intentionally distinguishes local skill replay from full
governance replay.

## Reference Adaptation

Source reference inspected:

- `/mnt/d/cloud/team-knowledge/team-knowledge/.codex/skills/openspec-router/SKILL.md`
- `/mnt/d/cloud/team-knowledge/team-knowledge/docs/superpowers/specs/2026-05-15-openspec-router-design.md`
- `/mnt/d/cloud/team-knowledge/team-knowledge/docs/superpowers/plans/2026-05-15-openspec-router.md`
- `/mnt/d/cloud/team-knowledge/team-knowledge/docs/superpowers/specs/2026-05-15-openspec-router-replay.md`
- `/mnt/d/cloud/team-knowledge/team-knowledge/openspec/changes/add-openspec-router-governance/*`
- `/mnt/d/cloud/team-knowledge/team-knowledge/AGENTS.md`
- `/mnt/d/cloud/team-knowledge/team-knowledge/PROJECT.md`

Reused:

- Small router shape: intent, gate, route line.
- Rule that `$superpowers:brainstorming` keeps OpenSpec read-only until written
  spec review passes.
- Governance replay distinction between skill-only replay and full
  project-level replay.

Modified:

- Scope adapted to `report-wiki-portfolio` and its existing workflow gates.
- Spec id uses `agent-workflow-routing`.
- AGENTS insertion is minimal and does not restructure repo governance.

Rejected:

- No product-code assumptions from team-knowledge.
- No Go/backend/frontend details.
- No global skill promotion.

## Prior-Art / Common-Rule Dedupe

Existing ownership checked:

- Scanned: `PROJECT.md`: OpenSpec owns lifecycle and implementation progress.
- Scanned: `AGENTS.md`: Workflow Change Gate, Behavior Replay Gate, Behavior Asset
  Prior-Art Gate, Skill Authoring Contract, and High-Frequency Skills table.
- Scanned: `openspec/specs/openspec-apply-change/spec.md`: Superpowers plans may be
  execution overlays, not a second progress ledger.
- Scanned: `wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md`: repeated
  Superpowers brainstorming drift must be repo-visible.
- Scanned: `wiki/ops/wiki-medical-case-file-drift-retro-2026-05-15.md`: current
  incident shows stage-output authority drift.

Ownership classification:

- Owns: `openspec-router` owns only the mixed-intent pre-action route.
- References: OpenSpec remains lifecycle authority.
- References: Superpowers remains method discipline.
- References: AGENTS remains repo discipline and discoverability.
- Rejects: team-knowledge product stack, Go/backend/frontend assumptions, and
  global skill promotion.

## Pressure Scenarios

Positive trigger scenario:

- Input or situation shape: user invokes `$superpowers:brainstorming` in this
  OpenSpec-governed repository and then says `可以继续做`.
- Trigger condition: explicit Superpowers method plus a possible OpenSpec or
  workflow action.
- Expected route or stop behavior: emit
  `Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.`
- Repo-visible artifact: `.codex/skills/openspec-router/SKILL.md`,
  `AGENTS.md`, `PROJECT.md`, this OpenSpec change, and
  `docs/superpowers/specs/2026-05-15-openspec-router-replay.md`.
- Expected output: one compact route line and no OpenSpec edit until the
  Superpowers written-spec review gate passes.
- Promotion or non-promotion boundary: Superpowers artifacts remain secondary
  working material; accepted lifecycle content must be copied into OpenSpec.

Negative or should-not-trigger scenario:

- Input or situation shape: user asks for a simple one-off file lookup that
  does not mention Superpowers, OpenSpec, workflow gates, implementation,
  verification, archive, or process repair.
- Trigger condition: none of the mixed workflow trigger conditions is present.
- Expected route or stop behavior: no `openspec-router` ceremony is required;
  normal repo health and file-reading discipline still applies.
- Repo-visible artifact: the router skill states its trigger conditions.
- Expected output: direct bounded answer or read-only lookup.
- Promotion or non-promotion boundary: no new OpenSpec or Superpowers artifact
  should be created for an ordinary lookup.

Parent-gate preservation scenario:

- Input or situation shape: user asks to implement a large workflow change after
  a Superpowers design discussion.
- Trigger condition: implementation request with OpenSpec source of truth.
- Expected route or stop behavior: route to OpenSpec apply only when an active
  change has proposal, design, specs, and tasks.
- Repo-visible artifact: `AGENTS.md` Workflow Routing and Workflow Change Gate,
  plus `openspec/changes/add-openspec-router-governance/specs/agent-workflow-routing/spec.md`.
- Expected output: OpenSpec lifecycle remains authoritative; Superpowers plan
  can assist but cannot replace tasks or validation.
- Promotion or non-promotion boundary: no implementation, completion, or
  archive claim from Superpowers checkboxes alone.

## RED Baseline

Observed failing behavior:

- `$superpowers:brainstorming` was active.
- The agent read the brainstorming skill but did not complete its design/spec
  review gate.
- A short approval was treated as permission to write OpenSpec artifacts and
  commit.
- The route line and mixed-gate decision were missing.

Why this is the right RED case:

- It is the exact failure the user challenged.
- It demonstrates that existing OpenSpec gates and Superpowers skills were both
  present but not ordered.

## GREEN Result

Expected behavior with the router:

- The route line is emitted before edits:

```text
Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.
```

- OpenSpec artifacts stay read-only until the Superpowers written spec review
  gate passes.
- Short approvals advance only the current gate.
- If the accepted result is a lifecycle change, it is then copied into
  OpenSpec and verified there.

Replay evidence:

- `docs/superpowers/specs/2026-05-15-openspec-router-replay.md`
- `openspec/changes/add-openspec-router-governance/specs/agent-workflow-routing/spec.md`
- `.codex/skills/openspec-router/SKILL.md`

## Original Incident Replay

Input:

```text
$superpowers:brainstorming
可以继续做
```

Expected route:

```text
Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.
```

Expected behavior:

- The router activates before edits.
- Superpowers brainstorming proceeds through exploration, options, design,
  written spec, self-review, and user review.
- OpenSpec remains read-only until Superpowers written spec review passes.
- Accepted lifecycle content may then be copied into OpenSpec.

Forbidden behavior:

- Direct `openspec/changes/*` edits before Superpowers review.
- Claiming full governance verification from skill-only replay.
- Treating short approvals such as `可以`, `继续`, or `做吧` as permission to
  cross into OpenSpec edit, implementation, commit, push, or archive.

## Validation

OpenSpec validation:

```text
openspec validate add-openspec-router-governance --strict
Change 'add-openspec-router-governance' is valid
```

Residual note: the CLI printed PostHog telemetry DNS flush errors after local
validation succeeded. Those network errors are non-blocking for local OpenSpec
validation.

Behavior asset validation:

```text
python3 scripts/check_behavior_assets.py
```

Initial result: failed because this evaluation was missing required pressure
scenario, RED/GREEN, residual risk, parent-gate preservation, replay, and
prior-art labels. The evaluation was updated to preserve those fields before
rerunning.

Rerun result:

```text
exit code: 0
```

The behavior-asset check passed after the evaluation evidence was expanded.

## Proof Boundary

This change adds routing governance. It does not apply wiki medical-loop
surgery, change product behavior, or archive any OpenSpec change.

## Residual Risks

- The router is still a skill, so it only helps when future sessions load it or
  read AGENTS.md.
- A future agent can still skip the route line under pressure; mitigation is
  the AGENTS trigger plus OpenSpec replay evidence.
- The router does not prove the downstream Superpowers design quality or
  OpenSpec implementation quality; it only orders the gates.
