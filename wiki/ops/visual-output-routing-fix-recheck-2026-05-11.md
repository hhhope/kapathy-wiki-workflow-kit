---
layer: ops
domain: wiki
ops_area: wiki-runtime
title: visual-output-routing / fix recheck
canonical_object: visual-output-routing
artifact_type: explore_trace
status: active
source_path: chat://visual-output-routing/fix-recheck/2026-05-11
updated: 2026-05-11
---

# Visual Output Routing Fix Recheck

## Trigger

The user asked to continue fixing but explicitly requested an
`openspec-explore` pass first to check whether the previous visual output mode
routing fix is actually correct.

## Scope

This trace is for investigation before implementation. It covers:

- whether the current global `knowledge-article-visual` and
  `infographic-onepager` skill wording routes image-model requests correctly;
- whether the recorded behavior evidence matches the actual changed skill text;
- whether any follow-up should be an OpenSpec change, a skill patch, or no
  further change.

## Boundary

No implementation is authorized from this trace by itself. If the recheck finds
a real behavior gap, the next step must choose an appropriate change path before
editing behavior assets.

## Findings

### What is correct

The main runtime wording in both global skills now matches the intended route:

- `knowledge-article-visual` says visual output mode is user-owned, requires the
  four-mode fork when the user has not chosen, and treats dense Chinese as a
  risk note rather than permission to override an explicit image-model request.
- `infographic-onepager` says the same at the one-page/card layer and explicitly
  prevents treating HTML/SVG-exported PNGs as image-model output.
- Both evaluation files include RED/GREEN behavior replay for the H5/SVG versus
  image-model routing failure.

### Residual gaps

The previous fix is directionally right, but not fully closed:

- `knowledge-article-visual` still says direct image runs should not stop at
  prompts unless image generation is unavailable or unsafe for text accuracy.
  That can reopen the old silent fallback if "unsafe for text accuracy" is not
  paired with a user-visible mode decision.
- `knowledge-article-visual` still says to switch to deterministic or hybrid
  mode when image generation distorts Chinese. The current stronger rule should
  prefer reporting the issue and switching to hybrid unless the user explicitly
  chooses deterministic-only output.
- `infographic-onepager` says to use SVG/HTML when the user chooses
  deterministic rendering, needs dense exact Chinese text, formal accuracy, or
  editable output. The "needs dense exact Chinese" phrasing is still ambiguous
  because it can be read as an automatic route instead of a constraint presented
  at the output-mode fork.
- The older top section of `knowledge-article-visual/evaluation.md` still says
  dense Chinese or formal output must use deterministic SVG/HTML export or
  hybrid mode. That is stale relative to the later output-mode fork repair.

## Recheck Conclusion

The fix should be tightened before relying on it as final behavior. The likely
next patch should only change residual wording and evaluation evidence; it does
not need a broad rewrite of either skill.
