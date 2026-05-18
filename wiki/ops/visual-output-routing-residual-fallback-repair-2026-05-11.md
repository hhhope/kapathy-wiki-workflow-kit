---
layer: ops
domain: wiki
ops_area: wiki-runtime
title: visual-output-routing / residual fallback repair
canonical_object: visual-output-routing
artifact_type: skill_fix_evidence
status: active
source_path: chat://visual-output-routing/residual-fallback-repair/2026-05-11
updated: 2026-05-11
---

# Visual Output Routing Residual Fallback Repair

## Trigger

The fix recheck found that the previous visual output mode repair was
directionally correct but still had residual wording that could reopen a silent
fallback from image-model output to deterministic SVG/HTML when Chinese text was
dense or risky.

## Changed Files

Global skill files changed outside this repository:

- `/home/yan/.codex/skills/knowledge-article-visual/SKILL.md`
- `/home/yan/.codex/skills/knowledge-article-visual/evaluation.md`
- `/home/yan/.codex/skills/infographic-onepager/SKILL.md`
- `/home/yan/.codex/skills/infographic-onepager/evaluation.md`

## RED Pressure

Pressure script:

```text
/tmp/visual_output_routing_pressure.py
```

Initial RED result before the residual repair:

```text
forbidden residual text in /home/yan/.codex/skills/knowledge-article-visual/SKILL.md: unsafe for text accuracy
```

After the first wording patch, the same pressure script was expanded to require
new evaluation evidence. It then failed on missing replay evidence:

```text
missing expected text in /home/yan/.codex/skills/knowledge-article-visual/evaluation.md: ## 2026-05-11 Residual Fallback Tightening
```

## GREEN Result

The repaired skill wording now requires:

- direct image requests do not stop at prompts because text accuracy is risky;
- text-accuracy risk is reported before changing modes;
- broken Chinese prefers hybrid mode unless the user explicitly chose
  deterministic-only output;
- dense exact Chinese is a constraint to confirm, not an automatic SVG/HTML
  route.

Final pressure run:

```text
python3 /tmp/visual_output_routing_pressure.py
visual output routing pressure checks passed
```

## Behavior Replay

| Field | Expected behavior |
|---|---|
| Input shape | User asks for image-model visuals, asks why H5/SVG was used, or provides dense Chinese infographic content while wanting image-model quality. |
| Trigger condition | Chinese text may distort in pure image generation. |
| Required route | Report the risk, prefer hybrid, and only use deterministic-only output when the user chooses it or an external constraint requires it. |
| Required non-output | Do not silently stop at prompts or auto-route to SVG/HTML because text accuracy is risky or dense Chinese is present. |
| Repo-visible artifact | This evidence page plus the global skill evaluation files. |
| Proof boundary | This proves routing language and pressure checks only; final visual quality still requires generated-asset QA. |

## Verification Commands

```text
python3 /tmp/visual_output_routing_pressure.py
rg -n "unsafe for text accuracy|switch to deterministic or hybrid|Use SVG/HTML when the user chooses deterministic rendering|Residual Fallback Tightening|automatic deterministic fallback|automatic SVG/HTML route|text accuracy becomes risky|prefer hybrid mode" /home/yan/.codex/skills/knowledge-article-visual /home/yan/.codex/skills/infographic-onepager
nl -ba /home/yan/.codex/skills/knowledge-article-visual/SKILL.md | sed -n '268,292p'
nl -ba /home/yan/.codex/skills/infographic-onepager/SKILL.md | sed -n '276,286p'
tail -90 /home/yan/.codex/skills/knowledge-article-visual/evaluation.md
tail -90 /home/yan/.codex/skills/infographic-onepager/evaluation.md
```

## Residual Risk

This repair closes the documented routing loopholes. It does not prove pure
image-model Chinese typography is usable for final publication; dense final copy
still needs image QA and may require hybrid overlay.
