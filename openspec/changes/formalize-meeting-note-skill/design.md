## Context

The repository currently has two different patterns for skill-like behavior:

- formally published project-local skills under `.codex/skills/`
- draft guidance under `skills-drafts/`

Two existing changes already prove that `.codex/skills/` is the working project-local publication path:

- `project-management-weekly-skill`
- `migrate-weixin-reader-skill`

But `meeting-note-output-format` chose a weaker pattern and explicitly treated `skills-drafts/meeting-note-output/` plus `AGENTS.md` as the enforceable mechanism. In practice that created a false sense of completion: the workflow was documented, but not discoverable as a formal skill by new sessions.

At the same time, the environment also contains manual role templates under `~/.codex/agents/`. Those files are useful for explicit planner/reviewer roles, but they are not the same thing as project-local skills and should not be treated as the mechanism for repo-default auto-routing.

This change corrects the publication model rather than only rewriting content.

## Goals / Non-Goals

**Goals:**

- Publish the meeting-note workflow as a real project-local skill under `.codex/skills/`.
- Define a durable publication rule that distinguishes formal project-local skills from draft skill documents.
- Record the boundary that agent role templates are manual role assets, not substitutes for project-local skill routing.
- Add verification that catches "draft exists but formal skill does not" as a RED state.

**Non-Goals:**

- Introduce a new global skill outside this repository.
- Redesign the meeting-note content contract itself beyond what is needed for formal publication.
- Add automatic agent spawning or change the platform-level sub-agent mechanism.

## Decisions

### Decision: `.codex/skills/` is the only formal project-local skill publication path

Project-local skills are considered active only when they exist under `.codex/skills/<skill-name>/SKILL.md`.

Alternative considered:
- Continue treating `skills-drafts/` as an enforceable publication surface.
  - Rejected because it documents intent without making the skill formally discoverable.

### Decision: `skills-drafts/` remains design/staging space only

`skills-drafts/` may still hold draft content, examples, or pre-publication exploration, but it is not enough to satisfy a repository workflow that depends on the skill being available in future sessions.

Alternative considered:
- Delete `skills-drafts/` entirely.
  - Rejected because draft space still has value during exploration, but it must not be confused with released behavior.

### Decision: agent role templates are manual, not routing defaults

Manual role templates such as planner/reviewer files belong to agent-role tooling and explicit role invocation. They do not count as a replacement for project-local skill routing and must not be used to claim that a repo-default workflow is formally published.

Alternative considered:
- Encode repo-default workflow behavior as an agent template instead of a skill.
  - Rejected because the current environment proves skill discovery and agent-role invocation are different mechanisms with different purposes.

### Decision: verification must test discoverability, not only document existence

The RED condition for this change is not merely "missing markdown". It is "meeting-note workflow exists only as draft guidance and is absent from the formal local skill directory". GREEN requires the formal skill to exist under `.codex/skills/` and repo references to stop treating the draft path as authoritative.

Alternative considered:
- Reuse the old validation style that checks only template/example presence.
  - Rejected because that misses the runtime discovery failure that caused the bug.

## Risks / Trade-offs

- [Risk] Duplicate content may temporarily exist in both `skills-drafts/` and `.codex/skills/`. → Mitigation: make the formal path authoritative and update references accordingly.
- [Risk] Repo guidance may still mention the old draft path. → Mitigation: search and update all meeting-note routing references during implementation.
- [Risk] Future contributors may again confuse manual agent templates with auto-routed skills. → Mitigation: codify the boundary in repo-visible guidance and specs.

## Migration Plan

1. Add OpenSpec artifacts that formalize the publication rule and meeting-note skill correction.
2. Publish `meeting-note-output` under `.codex/skills/`.
3. Update repo guidance so the formal skill path is authoritative.
4. Run RED/GREEN verification for draft-only versus formally published states.
5. Record the stable decision in repo-visible guidance if needed by the final implementation shape.
