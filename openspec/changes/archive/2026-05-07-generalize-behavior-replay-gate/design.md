## Context

`skill-evaluation-evidence` is useful but narrow: it requires `evaluation.md`
when active changes publish or semantically edit `.codex/skills/*`.

The new need is broader. The user identified that the real governance pattern
is not only "skill changes need evidence"; it is "future runtime behavior
claims need replay." A future-behavior claim includes statements such as:

- next time a bare link appears in this context, `learning-capture` will run;
- archive-complete means implementation stops and archive review runs next;
- `$openspec-explore` creates or updates a trace before exploration continues;
- a skill description will trigger for the intended request and reject the
  wrong request.

## Decision

Create `Behavior Replay Gate` as a generic repository gate.

The gate fires when a change or completion claim says a runtime behavior will
trigger, stop, route, reject, or persist differently in future sessions.

Minimum replay evidence:

1. input or situation shape;
2. trigger condition;
3. expected route or stop behavior;
4. repo-visible artifact the future agent would read;
5. expected output, non-output, or refusal;
6. promotion / boundary rule;
7. residual risk or proof boundary.

## Layering

Specialized mechanisms remain valid:

- `skill-evaluation-evidence` is the skill-specific evidence gate.
- `local-skill-pressure-tests` is the skill-specific RED/GREEN pressure format.
- disagreement and re-anchor replay specs are specialized executable harnesses.
- `Link Trigger Replay` is the first learning-capture instance.

`Behavior Replay Gate` is the umbrella rule that says when these evidence
shapes are required.

## Non-Goals

- It does not require executable scripts for every replay.
- It does not claim replay proof is rollout telemetry.
- It does not force every wiki learning note to produce replay evidence.
- It does not automatically promote candidate learning into rules.

## Evidence Plan

Use documentation-level RED/GREEN replay:

- RED: search shows no generic `Behavior Replay Gate`; only local/specialized
  replay references exist.
- GREEN: `AGENTS.md`, the new spec, and wiki page expose the generic gate and
  its minimum evidence.
- Boundary: prove candidate learning and one-off analysis are excluded.
