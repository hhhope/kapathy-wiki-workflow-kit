# Hermes Agent Self-Evolution Review

## 1. Source Trace

### External inputs

- Weixin article mirror: [一文搞懂 Hermes：新顶流 Agent 如何从经验中自我进化](https://tool.lu/index.php/ja_JP/article/7Mb/detail)
  - The mirrored page explicitly states the original source is `mp.weixin.qq.com`.
  - This review treats it as the article input requested by the change because the original Weixin page is not directly retrievable from the current environment.
- Repository: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Skills workflow references:
  - [Hermes Agent 中文社区: 使用技能](https://hermesagent.org.cn/docs/guides/work-with-skills)
  - [Hermes Agent docs: Updating & Uninstalling](https://nousresearch.github.io/hermes-agent/docs/getting-started/updating/)

### Why these sources matter

- The article gives the high-level framing for Hermes as an agent that learns from experience rather than only executing prompts.
- The GitHub repository anchors the implementation reference instead of leaving the comparison at article-summary level.
- The skills pages expose the mechanics behind discovery, progressive disclosure, and lifecycle actions such as search, install, create, update, and uninstall.

## 2. Repository Baseline Review

### Current strengths already present in this repository

1. OpenSpec boundary enforcement is already strong.
   - The global `AGENTS.md` now makes `all_done` a hard stop and routes completed changes into archive review instead of silent follow-on implementation.
2. Local skill publication is already being formalized.
   - The repository has moved from draft-only workflow pages toward `.codex/skills/` as the formal publication surface.
3. Skill and behavior changes already have TDD-style evaluation pressure.
   - Skill-edit and behavior-asset rules require baseline/after evidence instead of accepting prompt edits as self-justifying.
4. Retro capture is already separated from stable decisions.
   - The repo distinguishes ADRs from retros such as `scope-drift-retro`, which is a strong governance baseline.

### Main gaps relative to Hermes-style self-evolution

1. No explicit experience-extraction trigger layer.
   - The repository has good review discipline after a problem is noticed, but it still depends on a person noticing that the experience should become reusable governance.
2. No candidate-memory layer between raw event and stable reusable method.
   - Today the jump is often too direct: chat or incident -> ADR / rule / skill.
   - Hermes-style self-evolution suggests an intermediate layer where candidate knowledge can exist before becoming durable policy.
3. Incremental refresh is still only directionally defined.
   - `ADR-0005` exists, but the repository still lacks an operational state model that distinguishes already-structured material from not-yet-structured material.
4. Human governance is present in practice but not yet formalized as a first-class layer.
   - The repo already behaves cautiously, but it still needs a visible rule that self-evolution outputs are reviewed and promoted intentionally instead of mutating the operating surface by default.

### Incremental-refresh gap, stated explicitly

The repository does not yet have a complete state model for:

- new raw material
- already-structured material
- material that is structured but stale
- material that is structured but contradicted by newer evidence

That means it has the right direction, but not yet the refresh semantics required to safely avoid full reprocessing while also avoiding stale knowledge.

## 3. ADR And Follow-up Boundary

### ADR-level decisions surfaced by this review

- [ADR-0004 Agent Self-Evolution Over Skill Governance](../../../wiki/adr/0004-agent-self-evolution-over-skill-governance.md)
- [ADR-0005 Incremental Refresh Over Full Reprocessing](../../../wiki/adr/0005-incremental-refresh-over-full-reprocessing.md)
- [ADR-0008 Human Governance Before Self-Evolution Promotion](../../../wiki/adr/0008-human-governance-before-self-evolution-promotion.md)

### Follow-up change candidates

1. `candidate-memory-layer-for-agent-learning`
   - Add a repository-visible staging layer between raw retros/chat discoveries and stable skills / rules / ADR promotion.
2. `incremental-refresh-state-model`
   - Convert `ADR-0005` from proposed direction into an explicit state model and workflow.
3. `experience-extraction-triggers`
   - Define when incidents, repeated clarifications, or repeated manual fixes must be examined for reuse promotion.

### Non-goal boundary

This review does not modify current skill behavior, routing, or archive logic beyond documenting the comparison and the follow-up implications.

## 4. Validation

- Review artifact exists in the current change directory as `review.md`.
- The change now leaves a repo-visible trace that links external reference inputs, current strengths, current gaps, ADR-level outcomes, and bounded follow-up candidates.
- The review remains documentary: it does not silently rewrite `.codex/skills/`, repo `AGENTS.md`, or other live behavior assets.
