## Why

The repository already has several local replay mechanisms:

- skill changes require `evaluation.md`;
- local skill pressure tests require RED/GREEN-style evidence;
- disagreement and re-anchor gates have dedicated replay harnesses;
- link learning now has a `Link Trigger Replay` matrix.

Those mechanisms prove the same larger point: when the repository claims that a
runtime behavior will trigger next time, the claim must be replayable from
repo-visible evidence. Today that rule exists only as scattered special cases.

## What Changes

- Introduce a generic `behavior-replay-gate` specification.
- Add a repo `AGENTS.md` section that names the gate and its minimum evidence.
- Keep existing specialized replay mechanisms as examples or subcases rather
  than replacing them.
- Record RED/GREEN evidence showing the gate was missing and is now
  discoverable.

## Scope

In scope:

- new `behavior-replay-gate` spec
- repo `AGENTS.md` behavior gate wording
- wiki explanation page for the gate
- evaluation evidence for the change

Out of scope:

- changing root `~/.codex/AGENTS.md`
- editing root/global skills
- replacing existing disagreement / re-anchor / skill evaluation specs
- adding executable automation
- archiving existing completed changes

## Success Criteria

- Future agents can distinguish local replay examples from the generic replay
  gate.
- Any claim that a runtime behavior will trigger next time has a required
  evidence shape.
- The gate applies to skill triggers, AGENTS runtime triggers, OpenSpec hard
  stops, and future-behavior claims.
- The gate does not fire for one-off analysis, candidate learning notes, or
  ordinary source summaries that do not claim future behavior.
