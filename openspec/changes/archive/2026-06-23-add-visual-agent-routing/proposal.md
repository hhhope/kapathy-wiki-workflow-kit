# Add visual-agent routing

## Why

Visual production requests in this repo now span SVG diagrams, H5 pages,
article visuals, one-page infographics, direct image generation, and hybrid
workflows. The available skills already cover parts of this surface, but there
is no single user-facing controller that first decides whether the work should
be SVG, H5/HTML, image-model output, or a hybrid route.

Recent conversation showed the failure mode directly: `svg-flow-diagram` and
`architecture-diagram` both produce SVG, while `knowledge-article-visual` and
`infographic-onepager` differ by material shape rather than rendering engine.
Without an explicit router, agents can jump to the wrong worker or bypass the
human preference fork.

## What Changes

- Add a repo-local `.codex/skills/visual-agent/SKILL.md` as the normal
  user-facing controller for visual or drawing requests.
- Define a compact routing model for SVG, H5/HTML, image-model, and hybrid
  modes.
- Preserve existing worker ownership instead of copying their detailed
  execution rules into the controller.
- Register the route in `AGENTS.md` so future visual requests can discover the
  controller before choosing a worker.
- Add behavior evaluation evidence for positive and negative routing scenarios.

## Out of Scope

- Rewriting existing global visual skills.
- Creating a full rendering engine inside `visual-agent`.
- Automatically inserting generated images into Feishu or whiteboards.
- Changing OpenSpec lifecycle, public-report gates, or wiki frontmatter rules.

## Impact

Users get a consistent first step for visual work: classify the content, expose
the mode choice when needed, and route to the correct specialized worker while
keeping reader-facing quality gates intact.
