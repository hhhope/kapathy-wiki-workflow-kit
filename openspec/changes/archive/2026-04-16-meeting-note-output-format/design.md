## Context

The repository now correctly treats meeting notes as source materials and can extract summaries, but the output quality problem has shifted from routing to formatting. The user expects meeting-note outputs to be directly usable as meeting minutes, especially when synced to Feishu documents.

The desired format is materially stronger than the current source-page pattern. It includes:

- meeting title, time, host, attendees
- core agenda
- decision-first body sections
- explicit treatment of options considered and rejected
- a structured action-item table
- a final summary and next-step block

This is not only a writing-style preference. It changes what completion means for meeting-note processing in this repository.

## Goals / Non-Goals

**Goals:**

- Define a fixed, reusable meeting-note output format.
- Make the format usable for both wiki `source` pages and Feishu meeting-note output.
- Distinguish note output from transcript output while keeping them linked.
- Provide a repo-local skill draft so future sessions can follow the format consistently.

**Non-Goals:**

- Turn every source type into the same format.
- Replace project-management weekly report structures.
- Introduce a globally installed skill outside the repository write boundary.

## Decisions

### Decision: Meeting-note output uses a fixed section contract

Meeting-note outputs will use a strong structure instead of generic summary blocks. The required sections are:

- 会议主题 / 时间 / 主持人 / 参会人员
- 核心议题
- numbered body sections by topic
- 明确决策 / 被否决方案 / 风险点
- 待办事项表
- 总结与后续步骤

Alternative considered:
- Keep the current summary-plus-bullets style.
  - Rejected because it is useful for internal extraction but weak as a meeting-minutes deliverable.

### Decision: Transcript remains supplementary, not the main deliverable

The meeting note is the authoritative readable output. The transcript remains supporting evidence for disputes, rationale, and raw dialogue.

Alternative considered:
- Merge transcript and note into one output.
  - Rejected because it makes the main note noisy and too long for normal consumption.

### Decision: Skill draft plus AGENTS constraint is the enforceable local mechanism

Because the writable repository path cannot host a formally installed `.codex/skills/*` skill in this environment, the fixed format will be enforced through:

- repo `AGENTS.md`
- a repo-local skill draft
- template files

Alternative considered:
- Wait for a writable formal skill location first.
  - Rejected because the formatting problem needs immediate correction.

## Risks / Trade-offs

- [Risk] The format may be too heavy for very small internal syncs. → Mitigation: allow concise wording inside the same section contract rather than changing the structure.
- [Risk] Users may expect every transcript to produce a full note automatically. → Mitigation: keep transcript as supporting material and note as the primary output.
- [Risk] Repo-local skill draft is not the same as a globally installed skill. → Mitigation: make AGENTS and template authoritative until installation path changes.

## Migration Plan

1. Create OpenSpec artifacts for the meeting-note output format change.
2. Add the new capability spec and delta spec.
3. Update repo guidance and meeting-note templates.
4. Add a repo-local meeting-note output skill draft with fixed structure and example.
5. Rewrite the current meeting-note sample to the new format.
