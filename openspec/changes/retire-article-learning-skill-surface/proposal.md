# Retire Article Learning Skill Surface

## Why

`learning-capture` is the intended runtime router for learning requests, but
`.codex/skills/article-learning-capture/SKILL.md` still exposes a directly
triggerable description for article, WeChat, deep-reading, and learning
extraction requests. That creates two runtime entry signals for the same
learning workflow.

Durable learning templates also set `language: zh-CN` while retaining English
reading-note headings, which can still steer wiki learning output toward
English.

## What Changes

- Make `learning-capture` the only active learning runtime skill.
- Migrate useful article-specific workflow rules into `learning-capture`
  references.
- Remove the active `article-learning-capture` skill trigger surface.
- Make durable wiki learning notes Chinese-first by default.
- Preserve English-first authoring for behavior assets such as `SKILL.md`.

## Out Of Scope

- Reprocessing historical wiki learning notes.
- Changing external source fetching behavior.
- Changing README/repo or example learning semantics except where routing
  pressure scenarios prove they are not captured by the article module.
- Promoting article takeaways into `AGENTS.md`, specs, or hard skill rules
  without evidence.
