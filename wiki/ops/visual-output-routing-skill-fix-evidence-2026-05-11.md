---
layer: ops
domain: wiki
ops_area: wiki-runtime
title: visual-output-routing / skill-fix-evidence
canonical_object: visual-output-routing
artifact_type: skill_fix_evidence
status: active
source_path: chat://visual-output-routing/skill-fix/2026-05-11
updated: 2026-05-11
---

# Visual Output Routing Skill Fix Evidence

## Trigger

The live conversation exposed repeated routing drift:

- The user asked for visual assets and later explicitly challenged why the
  result was still H5/SVG-like.
- The user asked that drawing mode be selectable: simple H5, deterministic
  SVG/HTML, image model, or hybrid.
- The prior skills allowed dense Chinese/formal/editable requirements to become
  a silent deterministic SVG/HTML fallback, even after `图片模型`, `跑图`, or
  `生图` language appeared.

## Changed Files

Global skill files changed outside this repository:

- `/home/yan/.codex/skills/knowledge-article-visual/SKILL.md`
- `/home/yan/.codex/skills/knowledge-article-visual/evaluation.md`
- `/home/yan/.codex/skills/infographic-onepager/SKILL.md`
- `/home/yan/.codex/skills/infographic-onepager/evaluation.md`

This repo page records the behavior proof because the global skill files are not
archived inside this repository.

## RED Baseline

Old behavior language allowed these failures:

- `knowledge-article-visual` said `图片模型` requests should use image generation
  unless dense Chinese required deterministic fallback.
- `knowledge-article-visual` said dense Chinese, formal review, or exact wording
  should use deterministic SVG/HTML first.
- `infographic-onepager` said direct image requests could still fall back when
  dense Chinese made deterministic layout safer.
- The unclear fork covered image model vs H5/HTML, but not the full decision
  between H5/HTML, SVG/HTML, direct image model, and hybrid.

## GREEN Result

Updated behavior language now requires:

- Visual output mode is user-owned.
- If H5/HTML, deterministic SVG/HTML, direct image model, and hybrid could all
  satisfy part of the request, ask the four-mode fork before implementation.
- If the user already says `图片模型`, `跑图`, `生图`, or complains about H5/SVG,
  route to direct image generation or hybrid mode.
- Dense Chinese and formal review are risk notes or delivery constraints, not
  permission to silently override an explicit image-model request.
- PNG exported from HTML/SVG must be labeled deterministic rendering, not
  image-model output.

## Behavior Replay

| Field | Expected behavior |
|---|---|
| Input shape | User asks for visual assets, says `图片模型` / `跑图` / `生图`, or rejects H5/SVG quality. |
| Trigger condition | The same request could be fulfilled by H5/HTML, SVG/HTML, direct image model, or hybrid. |
| Required route | Ask the four-mode fork when unclear; if image model was already selected, use direct image model or hybrid. |
| Required non-output | Do not produce H5/SVG screenshots and describe them as image-model output. |
| Repo-visible artifact | This `wiki/ops` evidence page plus the global skill evaluation files. |
| Promotion boundary | This is a skill-routing fix, not proof that any specific generated visual is high quality. |

## Verification

Commands run after the edit:

```text
rg -n "Visual output mode|Output Mode Fork|four-mode|图片模型|H5/SVG|Dense Chinese is a risk note|user-owned|deterministic rendering" /home/yan/.codex/skills/knowledge-article-visual /home/yan/.codex/skills/infographic-onepager
nl -ba /home/yan/.codex/skills/knowledge-article-visual/SKILL.md | sed -n '1,140p'
nl -ba /home/yan/.codex/skills/infographic-onepager/SKILL.md | sed -n '1,115p'
tail -120 /home/yan/.codex/skills/knowledge-article-visual/evaluation.md
tail -120 /home/yan/.codex/skills/infographic-onepager/evaluation.md
```

Verified findings:

- Both skills now contain the four-mode fork.
- Both skills now state that dense Chinese is not a silent override for an
  explicit image-model request.
- Both evaluation files now include RED baseline, GREEN result, and behavior
  replay evidence for this routing failure.

## Residual Risk

This repair fixes the route selection language. It does not guarantee final
image quality. Pure image generation can still distort Chinese text, and hybrid
output still needs visual QA so deterministic overlays do not look like ordinary
H5 cards.
