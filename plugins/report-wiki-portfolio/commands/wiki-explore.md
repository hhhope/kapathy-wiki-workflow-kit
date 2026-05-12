---
description: Explore a wiki-backed topic with evidence-surface and enoughness checks.
argument-hint: topic, thread, or "not enough" correction
---

# /wiki:explore

Explore a wiki-backed topic, thread, report, source set, or governance question
with an explicit evidence-depth contract.

Use this command when the user explicitly asks for `wiki:explore`, or when an
ongoing wiki-backed exploration is rejected as shallow, incomplete, off-target,
or not enough.

## Workflow

1. Re-anchor the current object:
   - name the exact topic, thread, report, source set, or behavior object;
   - state nearby objects that are not the current target when confusion is
     plausible.
2. Build bounded wiki context:

```bash
python3 scripts/build_wiki_status.py
python3 scripts/derive_runtime_auto_routing.py > /tmp/wiki-runtime-auto-routing.json
python3 scripts/build_runtime_context_injection.py > /tmp/wiki-context-injection.json
```

3. Search explicit terms across repo-visible knowledge:

```bash
rg -n "<topic terms>" wiki openspec/specs openspec/changes/archive .codex/skills plugins README.md
```

4. Open relevant evidence layers:
   - `wiki/ops`
   - `wiki/sources`
   - `wiki/reports`
   - OpenSpec specs or archived changes
   - relevant repo-local skills and command contracts
5. Return an exploration-depth answer with:
   - current object
   - opened evidence
   - evidence surface
   - enoughness judgment
   - next boundary

## Evidence Surface

Check which layers exist and which are missing:

- source map
- broad scan or public source pool
- timeline
- podcast/video/interview pool
- evidence matrix
- gate review
- output draft
- residual risks or blockers

When public material is involved, distinguish primary sources, secondary/media
sources, candidate leads, transcript/upstream-capture gaps, and internal
synthesis.

## Boundaries

- This command explores and judges depth; it does not implement.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not treat a source pool as publication-ready proof by itself.
- Recommend a new OpenSpec change only when a default behavior or durable
  workflow should change.
