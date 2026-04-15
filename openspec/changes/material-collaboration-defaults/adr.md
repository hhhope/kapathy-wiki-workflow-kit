# ADR Set: Material Collaboration Defaults

This file captures workflow-level decisions for the `material-collaboration-defaults` change. It is not a retro. It records decisions that future sessions should be able to inspect without replaying chat history.

## ADR-001: Treat repository-default collaboration changes as OpenSpec-level

- Status: accepted
- Date: 2026-04-15

### Context

The repository previously had workflow guidance scattered across wiki pages and conversation history, but no hard local rule saying that changes to default collaboration behavior must go through OpenSpec first. That made it too easy to patch `wiki/` or skill drafts directly and only later realize the change was actually repository-wide behavior.

### Decision

Changes to repository-default workflow, collaboration behavior, routing defaults, escalation boundaries, and default output rules are OpenSpec-level changes in this repository.

### Consequences

- Future sessions must create or select an active OpenSpec change before editing repository guidance for those topics.
- Temporary wiki-only fixes are no longer an acceptable first step for this class of changes.

## ADR-002: Decision visibility requires ADR plus interruption checkpoint

- Status: accepted
- Date: 2026-04-15

### Context

The user’s requirement is not only “make the right decision” but “make the decision process observable,” especially when the work is interrupted or later reviewed. A rule in `AGENTS.md` is not sufficient by itself because it explains what should happen, not what was actually decided in a specific change.

### Decision

Workflow-level changes in this repository must leave two visible traces:

- an ADR entry under the active OpenSpec change for the decision itself
- a checkpoint record when the work is interrupted or a decision branch is still open

### Consequences

- Future sessions can distinguish standing rules from change-specific decisions.
- Interrupted work becomes resumable without depending on memory or chat replay.

## ADR-003: Repository-specific first, global only with cross-repo proof

- Status: accepted
- Date: 2026-04-15

### Context

This repository has a wiki-first material-processing workflow with `inbox`, `source`, `ops`, and optional `html/preview` branches. Those constraints are not guaranteed to hold in every repository.

### Decision

Material-collaboration defaults are repository-specific unless repeated evidence across repositories shows the same decision boundary belongs in a global rule.

### Consequences

- The default place for this class of policy is repo `AGENTS.md` plus OpenSpec artifacts.
- Global promotion requires a separate decision, not silent copying upward.
