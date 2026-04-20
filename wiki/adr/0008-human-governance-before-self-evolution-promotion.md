# ADR-0008 Human Governance Before Self-Evolution Promotion

- Status: accepted
- Date: 2026-04-16

## Context

The repository is moving from narrow skill-file governance toward broader agent self-evolution governance. That shift increases the risk that useful experience gets promoted too quickly from chat history or incident notes into durable operating behavior.

The repo already shows cautious practice:

- retros are separate from ADRs
- behavior-asset edits require evaluation
- OpenSpec changes define scope before implementation

What was still missing was an explicit stable rule that human governance remains the promotion gate between raw experience and durable reusable behavior.

## Decision

Before a self-evolution insight becomes a durable behavior asset, the repository keeps a human-governed promotion boundary:

- raw experience may exist in chat, retros, or review notes
- candidate insights may be summarized in review artifacts or follow-up proposals
- stable operating behavior is promoted only through explicit repo-visible artifacts such as ADRs, skills, rules, or AGENTS updates

This means self-evolution is encouraged, but silent mutation of the operating surface is not.

## Consequences

- The repository can keep learning loops without pretending that every useful observation should immediately become live policy
- Review changes can benchmark outside systems without silently rewriting current agent behavior
- Future self-evolution automation must still preserve a visible human-governance checkpoint
