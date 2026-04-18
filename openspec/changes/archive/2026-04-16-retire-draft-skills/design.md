## Context

The repository already adopted a stable publication boundary:

- formal project-local skills live in `.codex/skills/`
- `skills-drafts/` is draft space only
- manual agent role templates do not replace skill routing

That boundary was formalized to fix the meeting-note workflow, but the repo still carries draft `SKILL.md` files under `skills-drafts/`. As long as those files remain present, contributors can still misread draft space as a runtime-discoverable skill surface.

The remaining operational gap is therefore not conceptual. It is publication hygiene:

- one workflow (`material-collaboration-defaults`) is still only drafted
- one workflow (`meeting-note-output`) already has a formal skill but still leaves a draft `SKILL.md` behind
- repo guidance does not yet state a hard completion rule that draft skills must be promoted or removed

## Goals / Non-Goals

**Goals:**

- Publish the remaining draft workflow as a real project-local skill.
- Ensure `skills-drafts/` no longer contains active `SKILL.md` files that can be mistaken for published capabilities.
- Make draft retirement/promotion a hard repository rule and a spec-level acceptance condition.

**Non-Goals:**

- Introduce a new publication mechanism beyond `.codex/skills/`.
- Replace OpenSpec or ADR as the workflow-governance mechanism.
- Delete historical OpenSpec changes that originally created the draft skills.

## Decisions

### Decision: `skills-drafts/` cannot carry live `SKILL.md` files after publication

If a workflow is important enough to survive across future sessions, it must be formally published. Once a formal copy exists, the repo should not keep a live-looking draft `SKILL.md` in `skills-drafts/`, because that recreates ambiguity about the true runtime surface.

Alternatives considered:
- Keep duplicate `SKILL.md` files in both locations.
  - Rejected because duplicate skill bodies create drift and false confidence.
- Keep draft `SKILL.md` files forever but rely on AGENTS wording.
  - Rejected because the failure mode is operational discoverability, not just documentation precision.

### Decision: change completion requires promotion or explicit retirement

A workflow-level change that creates or updates a project-local skill is not complete if the workflow remains only in `skills-drafts/`. The change must either:

- publish the skill under `.codex/skills/`, or
- explicitly retire the draft without claiming runtime availability

Alternatives considered:
- Allow draft-only completion when the wording is strong enough.
  - Rejected because draft-only completion already produced a real process miss.

### Decision: material-processing defaults get the same formal publication treatment as meeting-note output

The repository's default material-processing behavior is a repo-level workflow, not a one-off note. It should therefore be discoverable through the same formal local-skill path as meeting-note output.

Alternatives considered:
- Leave the behavior only in AGENTS and OpenSpec docs.
  - Rejected because repo-default reusable behavior should not depend on contributors remembering to read multiple guidance layers manually.

## Risks / Trade-offs

- [Risk] Removing draft `SKILL.md` files may reduce discoverability for contributors browsing historical changes. -> Mitigation: keep the OpenSpec artifacts and ADR trail, and point repo guidance to the formal skill path.
- [Risk] Future experiments may still want a staging area. -> Mitigation: keep `skills-drafts/` as a draft directory, but do not allow active `SKILL.md` files to represent published behavior.
- [Risk] Publishing too early could harden weak wording. -> Mitigation: require OpenSpec plus verification before promotion and allow explicit retirement when a draft is not ready.

## Migration Plan

1. Add a new OpenSpec change covering draft-skill retirement.
2. Publish `material-collaboration-defaults` under `.codex/skills/`.
3. Remove draft `SKILL.md` files from `skills-drafts/`.
4. Tighten AGENTS and ADR wording so future changes cannot stop at draft publication.
5. Record RED/GREEN verification showing the previous draft-only state and the new no-draft-skill state.

## Open Questions

- Whether the repository should keep a placeholder README or `.gitkeep` under `skills-drafts/` once it no longer stores active skills.
