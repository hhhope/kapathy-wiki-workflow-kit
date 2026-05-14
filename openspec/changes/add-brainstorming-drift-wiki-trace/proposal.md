# Proposal: add brainstorming drift wiki trace

## Summary

Add a repository rule that treats repeated drift during
`$superpowers:brainstorming` as a repo-visible trace event before continuation.

## Motivation

The repository already has durable trace gates for `$openspec-explore` and live
conversation re-anchor. A similar gap exists for brainstorming: when the user
explicitly invokes brainstorming and then repeatedly flags drift, the agent can
keep continuing the latest technical thread instead of recording the failure,
re-anchoring the design question, and preserving the correction pressure.

This happened during the wiki runtime discussion on 2026-05-14. The agent
blurred:

- `$wiki-react` as the explicit router and decision-trace entrypoint
- `eval_wiki_decision_trace.py` as trace validation
- `/wiki:apply` as bounded execution preview
- repair-route labels as design/contract language, not complete executable
  repair infrastructure

The repeated drift should not remain only in chat history.

## Scope

- Define the brainstorming drift trace rule.
- Record the 2026-05-14 three-drift incident as `wiki/ops` evidence.
- Keep the record as retro/trace evidence, not an ADR.
- Preserve the boundary that stable runtime, skill, AGENTS, or ADR changes
  require their own implementation steps after this proposal is accepted.

## Non-Goals

- Do not modify Superpowers upstream skills.
- Do not change repo-local `.codex/skills/*` behavior in this change proposal
  step.
- Do not create an ADR before the retro evidence is reviewed.
- Do not mark any completed OpenSpec change as reopened.
