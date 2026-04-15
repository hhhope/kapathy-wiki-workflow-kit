## ADDED Requirements

### Requirement: System SHALL provide a local weixin-reader skill
The repository SHALL provide a local `weixin-reader` skill under `.codex/skills/` so Weixin article reading does not depend on an external skill path.

#### Scenario: User wants to read a Weixin article
- **WHEN** the user provides an `mp.weixin.qq.com` article URL and wants to analyze, summarize, or extract its content
- **THEN** the repository SHALL contain a local `weixin-reader` skill that defines how to fetch and read the article

### Requirement: Migrated skill SHALL use local references
The migrated `weixin-reader` skill SHALL reference its local script path instead of the external `~/.claude/skills/` path.

#### Scenario: User checks the migrated skill
- **WHEN** the local `weixin-reader` skill is inspected
- **THEN** its documentation SHALL point to local repo skill paths and not depend on the external source location
