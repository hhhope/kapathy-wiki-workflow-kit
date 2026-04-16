## 1. Change Setup

- [x] 1.1 Create and validate OpenSpec artifacts for formal meeting-note skill publication

## 2. Specification

- [x] 2.1 Add a new `project-local-skill-publication` capability spec
- [x] 2.2 Add a delta spec for `meeting-note-output-format` so formal skill publication is required

## 3. Implementation

- [x] 3.1 Add `.codex/skills/meeting-note-output/SKILL.md`
- [x] 3.2 Add any bundled references needed by the formal meeting-note skill
- [x] 3.3 Update repo guidance so meeting-note routing points to the formal skill path and not the draft-only path
- [x] 3.4 Record the boundary between project-local skills and manual agent role templates in repo-visible guidance

## 4. Verification

- [x] 4.1 Record RED evidence that the old state had only `skills-drafts/meeting-note-output/` and no formal `.codex/skills/meeting-note-output/`
- [x] 4.2 Record GREEN evidence that the formal meeting-note skill now exists under `.codex/skills/`
- [x] 4.3 Record GREEN evidence that repo references no longer treat the draft path as authoritative publication
