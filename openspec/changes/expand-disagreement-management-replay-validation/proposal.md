## Why

The repository has already formalized the disagreement-management method, published it to `wiki/ops`, promoted the stable policy to `AGENTS.md`, and archived the first formalization change.

But the current proof is still narrow:

- replay evidence is concentrated in the design and evaluation artifacts of one change
- the method has only been pressure-tested against a small number of real threads
- there is no lightweight repo-visible harness that future validations can reuse

The user explicitly asked to continue with more replay / harness validation before moving into runtime behavior.

## What Changes

- Add a lightweight replay-validation harness for disagreement management.
- Record additional replay evidence against at least one more disagreement shape beyond the initial formalization runs.
- Make the validation boundary explicit: replay / harness proof is stronger than narrative design evidence, but still not rollout proof.

## Capabilities

### Modified Capabilities

- `disagreement-management-method`

## Impact

- Adds a new OpenSpec change under `openspec/changes/expand-disagreement-management-replay-validation/`.
- Publishes a reusable replay harness under `wiki/ops/`.
- Publishes additional replay evidence under `wiki/ops/`.
