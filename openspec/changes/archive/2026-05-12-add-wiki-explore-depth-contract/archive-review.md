## Archive Review

Date: 2026-05-12

Change: `add-wiki-explore-depth-contract`

## Decision

Archive review passes.

## Scope Check

- The change adds an independent `wiki-explore` skill and `/wiki:explore`
  command contract.
- The change updates README routing visibility.
- The change adds spec deltas for the command/skill behavior and runtime slash
  command surface.
- The change does not continue source hardening for the historical
  `agentic-product-engineering-collaboration` thread.
- The change does not modify `wiki-query` semantics.

## Evidence

- `tasks.md` has all tasks checked.
- `evaluation.md` records RED baseline, GREEN replay, compact skill-body check,
  command visibility, strict validation, and residual risks.
- `openspec validate add-wiki-explore-depth-contract --strict` reported:
  `Change 'add-wiki-explore-depth-contract' is valid`.
- `git diff --check` passed for the task-related paths before the
  implementation commit.

## Routine Closing Tail

None.

## Residual Risks

- This is behavior guidance, not automatic enforcement.
- Future correctness still depends on the agent loading the `wiki-explore` skill
  when the explicit command or rejection trigger appears.
- The evidence surface is a depth standard, not a fixed artifact checklist for
  every topic.
