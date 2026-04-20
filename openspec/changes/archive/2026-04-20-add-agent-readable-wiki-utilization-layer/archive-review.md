# Archive Review: Agent-Readable Wiki Utilization Layer

## Review Result

- archive review status: pass

## Completion Check

- `tasks.md` is fully checked
- `verification.md` records the utilization banding model, current-state summary, and residual risks
- `openspec validate add-agent-readable-wiki-utilization-layer` passed

## Scope Check

- the change stayed inside bounded utilization guidance
- it added:
  - repo-visible guidance
  - a utilization script
  - a sample utilization artifact
- it did not expand into:
  - retrieval infrastructure
  - runtime automation
  - unresolved page interpretation
  - autonomous routing

## Governance Check

- the change introduces a stable repo-default downstream layer after semantic scoring
- that decision should survive across future changes
- therefore the decision is promoted to ADR and synced to formal spec

## Disagreement Preservation Check

- no additional governance-heavy disagreement material required separate preservation in this change
- proof boundaries and residual risks are already preserved in `verification.md`

## Archive Decision

- sync the finalized spec into `openspec/specs/wiki-utilization-layer/spec.md`
- archive the active change directory
