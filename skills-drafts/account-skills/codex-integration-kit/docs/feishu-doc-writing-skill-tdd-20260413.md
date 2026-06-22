# Feishu Doc Writing Skill TDD

Date: `2026-04-13`

## Goal

Create a global-installable skill that prevents four recurring document failures:

- knowledge density stays overloaded in one page
- updates ignore surrounding document context
- published docs still contain unresolved TODOs or half-finished continuation text
- writing order is technically complete but hostile to readers

This round also expands the skill to prevent three more failures:

- one doc in the set gets reframed but sibling docs keep the old naming and style
- text gets updated but stale diagrams still show the previous model
- requests for Feishu visuals drift into ad-hoc output instead of routing to the right visual skill

This refinement round expands the skill further to prevent three more failures:

- the published page still reads like a cleaned-up conversation instead of a stable document
- comparison-heavy content stays as bullets or prose instead of being converted into tables
- the doc is “updated” but no post-update readback verifies the remote result

This final refinement round closes one more failure:

- system-level diagrams drift into command-order sequence charts and fail to show operator control, governance layers, truth sources, execution tools, and publishing outputs

This follow-up closes one more failure:

- once a page already has a clear job, new information still gets added as a brand-new section instead of being merged into the right place or moved to the right child doc

## RED Baseline

Without a dedicated skill, the agent can still rationalize all of these:

1. “信息都写全了，所以先不拆文档”
2. “只改目标页就行，父页和子页之后再补”
3. “先留 TODO，后面再继续”
4. “事实都对，行文体验以后再优化”
5. “先画个时序图顶一下，之后再讲体系怎么协作”
6. “这个信息也很重要，所以再加一节”

That baseline is exactly what caused prior Feishu updates to drift away from reader-facing quality.

## GREEN Contract

The new skill blocks those rationalizations by requiring:

- overview vs deep-dive classification before writing
- progressive first-screen structure
- explicit split rules for dense topics
- context-link checks across related docs
- no unresolved TODO in published updates
- document-set naming consistency across overview / child docs
- stale visual cleanup after reframing
- explicit routing to `xiaohongshu-retro-grid-content` or `lark-whiteboard` when a visual companion is needed
- dialogue-like wording to be rewritten into document language
- table-first formatting for list-shaped comparisons, metrics, steps, and boundaries
- post-update readback as part of the publish gate
- diagram routing by reader question instead of by habit
- layered system-map visuals for governance/lifecycle explanations that need to show control surfaces and truth-bearing artifacts
- section-addition discipline based on page role instead of additive dumping
- overview pages to stay on system model and reading-map duty while install/gate detail stays in install pages

## Evidence

Created assets:

- [SKILL.md](/mnt/d/skills/account-skills/codex-integration-kit/skills/feishu-doc-writing/SKILL.md)
- [template.md](/mnt/d/skills/account-skills/codex-integration-kit/skills/feishu-doc-writing/references/template.md)

Repository integration updates:

- [README.md](/mnt/d/skills/account-skills/codex-integration-kit/README.md)
- [feishu-codex-governance-share.md](/mnt/d/skills/account-skills/codex-integration-kit/docs/feishu-codex-governance-share.md)

## Acceptance

This skill is acceptable only if it makes these decisions explicit:

- when to split
- how to keep overview/deep-dive linkage intact
- how to prevent dangling TODOs
- how to write progressively for human readers
- how to keep a multi-doc set stylistically coherent
- when to generate a visual summary and which companion skill to pair with
- how to decide when prose should become a table
- how to reject “chat-like” published wording
- how to verify that the remote Feishu result actually matches the intended final shape
- how to keep a system-level visual from collapsing into a misleading sequence-only diagram
- how to stop new information from becoming a new section when the page job has not changed
