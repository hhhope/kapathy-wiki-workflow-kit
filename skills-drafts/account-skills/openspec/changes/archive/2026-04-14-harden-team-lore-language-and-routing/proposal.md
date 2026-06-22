## Why

The first `team-lore` rollout slice proved the retrieval-first page contract and the Lore/Graphify routing boundary, but it intentionally stopped short of full mixed-language interpretation and automated routing checks.

Keeping those residual gaps inside the archived first-slice change would overstate completion and blur the acceptance boundary.

## What Changes

- harden mixed-language support beyond alias-only routing aids for the highest-value shared pages
- add stronger evaluation for Lore/OpenSpec/Graphify routing so the contract depends less on manual judgment
- define the smallest follow-up rollout needed to raise confidence without reopening broad historical backfill

## Capabilities

### New Capabilities
- `team-lore-language-and-routing-hardening`: harden mixed-language loading and routing verification after the first retrieval-first rollout slice

### Modified Capabilities

## Impact

- shared `team-lore` entry and reusable pages that still rely on alias-only language support
- Lore evaluation assets under `skills/lore/evals/`
- routing guidance that distinguishes OpenSpec, Lore, and Graphify use
