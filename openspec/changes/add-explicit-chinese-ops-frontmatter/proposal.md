# Change: Add Explicit Chinese Ops Frontmatter

## Why

The graph runtime now reports only three unresolved identities, all Chinese
`wiki/ops` pages that do not match the supported filename conventions. These
should be resolved with explicit frontmatter rather than another broad path
resolver.

## What Changes

- Add `canonical_object` and `artifact_type` to the three remaining unresolved
  ops pages.
- Keep the graph extractor unchanged.
- Add verification that live extraction reaches zero unresolved warnings.

## Impact

- Affected pages:
  - `wiki/ops/ai-chat-一键安装-skill-探索-2026-04-17.md`
  - `wiki/ops/宝财通分账开通与迁移边界提醒-2026-04-16.md`
  - `wiki/ops/宝财通分账开通迁移场景对照表-2026-04-16.md`
- Affected spec: `wiki-graph-extraction`
