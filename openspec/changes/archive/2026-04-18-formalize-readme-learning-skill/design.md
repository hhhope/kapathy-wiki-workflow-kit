## Context

The repository already knows how to:

- capture repeated in-session topics through `handoff mode`
- turn extracted example learnings into wiki records

What it still lacks is a dedicated entry point for one recurring source type:

- GitHub and GitLab repository READMEs

This source type is different from ordinary material processing because the useful output is usually not a full source digest. The practical value is the adaptation boundary:

- what should be copied
- what should be adapted
- what should not be copied
- what follow-up asset should be created

## Goals / Non-Goals

**Goals**

- Create a dedicated repo-local skill for GitHub / GitLab README learning
- Make the trigger explicit so future requests load the right workflow
- Preserve adaptation boundaries instead of generic source summary
- Keep the skill compact and repo-boundary aware

**Non-Goals**

- Do not create a full web-fetching implementation in this change
- Do not require every GitHub / GitLab link to become a wiki page
- Do not replace `example-driven wiki capture`; this skill should feed that workflow
- Do not create a generic skill for all possible websites

## Decisions

### Decision: Trigger on GitHub / GitLab repo or README analysis requests

The skill should trigger when the user:

- provides a GitHub or GitLab repo / README
- asks what is reusable, worth copying, or worth learning
- wants the result written into repo assets

Alternative considered:

- keep using generic example-driven capture only
  - Rejected because the trigger is common and specific enough to deserve a dedicated skill.

### Decision: Preserve adaptation boundary as the core output

The skill should not optimize for generic summary.

It should preserve at least:

- source
- what was reused
- what was modified
- what was rejected or not yet formalized
- repo target

Alternative considered:

- treat the README as a normal article summary task
  - Rejected because it loses the repository-specific value.

### Decision: Reuse existing wiki routing rather than invent a new output layer

The skill should route its durable outputs through the already-published repository layers:

- `wiki/ops`
- `wiki/examples`
- `wiki/team-lore-candidates.md`
- `OpenSpec change` when the learning becomes a scoped workflow change

Alternative considered:

- create a new dedicated README-learning page type
  - Rejected because existing routing is already sufficient.

## Skill Shape

The skill should stay compact and English-first.

It should include:

- trigger conditions
- hard rules
- a short output checklist
- routing guidance
- anti-patterns

It may reference repo policy pages instead of restating them.

## Evaluation Plan

### RED baseline

Without a dedicated skill:

- README analysis may stop at a generic summary
- adaptation boundaries may be partial or absent
- wiki capture may rely on follow-up clarification

### GREEN expectation

With the skill present:

- GitHub / GitLab README analysis routes through a dedicated workflow
- the result extracts repository learning instead of just source summary
- the output preserves reuse / modify / not-formalized boundaries

## Open Questions

- Should a later change add a fetch helper or MCP integration specialized for README retrieval?
- Should GitHub / GitLab README learning later split into separate source and adaptation skills?
