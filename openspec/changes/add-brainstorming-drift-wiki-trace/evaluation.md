# Evaluation: brainstorming drift wiki trace

## Implementation Decision

Selected implementation: update repo `AGENTS.md` hard stops only.

Rejected for this change:

- adding a new repo-local skill
- modifying `$superpowers:brainstorming`
- creating a new ADR
- changing runtime scripts or eval logic

Reason: the failure was a repo-local continuation gate gap. The smallest
effective runtime-visible hook is the existing `AGENTS.md` hard-stop table,
adjacent to `$openspec-explore` trace and live re-anchor gates.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: owns repo-local workflow gates and hard stops.
- `PROJECT.md`: defines OpenSpec and wiki as source-of-truth layers; no
  brainstorming drift rule.
- `openspec/specs/openspec-explore-wiki-trace/spec.md`: owns
  `$openspec-explore` trace before continuation.
- `openspec/specs/live-conversation-reanchor-gate/spec.md`: owns broad live
  conversation drift re-anchor.
- `wiki/adr/0003-retros-stay-separate-from-adrs.md`: requires retro evidence
  to remain distinct from stable ADR decisions.
- `wiki/adr/0009-explore-trace-before-openspec-explore.md`: prior art for
  trace-before-continuation.
- `wiki/adr/0024-live-conversation-reanchor-before-continued-implementation.md`:
  prior art for stopping when drift is signaled.
- `wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md`: incident
  evidence and cause analysis.

Classification:

- Owns: repo `AGENTS.md` owns the hard stop for this repository.
- References: existing OpenSpec-explore and live re-anchor gates provide the
  pattern.
- Rejects: the 2026-05-14 chat incident is not promoted directly to ADR or
  skill hard rule in this change.

## Pressure Scenarios

Positive trigger scenario:

- Input or situation shape: `$superpowers:brainstorming` is active, the user
  says this is the third drift, and the conversation has crossed wiki runtime,
  skill, eval, OpenSpec, ADR, and repair-route layers.
- Trigger condition: the user explicitly flags repeated drift during
  brainstorming.
- Expected route or stop behavior: stop brainstorming continuation, create or
  update a repo-visible `wiki/ops` drift trace, then re-anchor design before
  continuing.
- Expected output: a concise acknowledgement plus a repo-visible trace such as
  `wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md`.

Negative should-not-trigger scenario:

- Input or situation shape: `$superpowers:brainstorming` is active and the user
  gives a single factual correction without saying the discussion has drifted
  repeatedly.
- Expected route or stop behavior: continue the brainstorming clarification
  flow; do not force a new wiki drift trace.
- Expected output: acknowledge the correction and continue with the current
  design question.

Parent gate preservation:

- `$openspec-explore` trace remains governed by its own trace-before-explore
  gate.
- Live conversation re-anchor remains governed by the existing re-anchor gate.
- Semantic skill edits still require skill authoring/evaluation evidence.
- OpenSpec remains the lifecycle for behavior changes.

## RED Baseline

Before this change, repo `AGENTS.md` had hard stops for `$openspec-explore` and
live conversation drift, but no hard stop for repeated drift during
`$superpowers:brainstorming`.

Observed failure:

- The agent continued the wiki runtime repair-route chain after the user
  invoked `$superpowers:brainstorming`.
- The repeated drift was not recorded in `wiki/ops` until the user explicitly
  requested it.
- The failure stayed in chat history rather than becoming repo-visible
  evidence.

## GREEN Result

After this change:

- `AGENTS.md` contains a hard stop for repeated drift during
  `$superpowers:brainstorming`.
- `wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md` records the
  incident, rejected framing, corrected framing, cause analysis, ADR boundary,
  and next action.
- `openspec/changes/add-brainstorming-drift-wiki-trace/specs/brainstorming-drift-wiki-trace/spec.md`
  defines the expected route and non-output boundaries.

## Behavior Replay Evidence

Input shape:

```text
$superpowers:brainstorming is active.
User says repeated drift occurred, such as "third drift".
The conversation has crossed between design, runtime, skill, OpenSpec, ADR,
or repair-execution layers.
```

Trigger condition:

```text
The user explicitly flags repeated drift during brainstorming.
```

Expected route:

```text
Stop brainstorming continuation.
Create or update a repo-visible wiki/ops drift trace.
Re-anchor the design question before continuing.
```

Repo-visible artifact future agents should read:

```text
wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md
openspec/changes/add-brainstorming-drift-wiki-trace/specs/brainstorming-drift-wiki-trace/spec.md
```

Expected non-output:

- Do not continue the latest technical chain before trace creation.
- Do not create an ADR from the incident by default.
- Do not modify skills, runtime scripts, or completed OpenSpec changes.

Promotion or non-promotion boundary:

The incident remains retro evidence. ADR promotion requires a later explicit
decision path.

Proof boundary:

This evaluation proves the repo-visible hard stop and replay evidence exist. It
does not prove that the upstream Superpowers skill will enforce the behavior
outside this repository.

## Residual Risks

The rule depends on agents reading repo `AGENTS.md`. It does not modify the
upstream Superpowers brainstorming skill, so agents outside this repository may
not inherit the behavior.

## Verification Commands

Run:

```bash
openspec validate add-brainstorming-drift-wiki-trace --strict
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md
python3 scripts/check_behavior_assets.py
```

Expected:

- OpenSpec validation passes.
- Frontmatter precheck may report existing global wiki debt, but the new target
  has `target.entry_count: 0`.
- Behavior asset checker result is recorded before completion.

Observed on 2026-05-14:

- `openspec validate add-brainstorming-drift-wiki-trace --strict`: passed with
  `Change 'add-brainstorming-drift-wiki-trace' is valid`. The command also
  printed non-blocking PostHog network flush errors.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md`:
  exited non-zero because of existing whole-wiki frontmatter debt, with
  `blocking_count: 767`; the new target reported `target.entry_count: 0`.
- `python3 scripts/check_behavior_assets.py`: passed with exit code 0.
