# Harden visual-agent entry route

## Why

Visual requests still have a bypass risk after the initial `visual-agent`
routing change. The repo has a controller skill, but the public-report gate and
worker references can still make a future agent jump directly to
`knowledge-article-visual`, `infographic-onepager`, SVG workers, or `imagegen`
without first exposing the visual mode fork.

The repeated failure mode is concrete: ambiguous requests such as 制图, 出图,
配图, 一图流, 知识卡, or section images were satisfied as H5/SVG work without
asking whether the user wanted SVG, H5/HTML, image-model, or hybrid output.

## What Changes

- Require visual work to visibly enter through `visual-agent` before child
  worker routing.
- Add a short entry marker so bypasses are observable in normal responses.
- Update public-report visual delegation references so reader-facing visual
  work routes through `visual-agent` before article/image worker skills.
- Add replay evidence for the H5/SVG defaulting failure and the corrected
  visual-agent-first route.

## Out of Scope

- Editing global visual worker skills under `/home/yan/.codex/skills`.
- Rewriting the visual rendering workers.
- Producing new visual assets.
- Archiving the earlier `add-visual-agent-routing` change.
