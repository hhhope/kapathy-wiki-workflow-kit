## Baseline Evidence

- Date: 2026-05-07
- Target: repo `AGENTS.md`
- Baseline count: 510 lines / 3430 words / 23578 bytes
- Command: `wc -l -w -c AGENTS.md`

## Section Classification

| Current section | Lines | Classification | Keep inline / proxy target |
|---|---:|---|---|
| OpenSpec Trigger | 5-10 | inline repo-only hard stop | Keep concise trigger wording inline; proxy stable rationale to `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`. |
| Decision Observability | 12-21 | inline repo-only hard stop | Keep checkpoint and ADR routing inline; proxy rationale to `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md` and `wiki/adr/0003-retros-stay-separate-from-adrs.md`. |
| Repo AGENTS Governance Phase Gate | 23-33 | inline repo-only hard stop | Keep Phase 0/Phase 1 gate inline; proxy accepted decisions to `wiki/adr/0027-repo-phase0-before-repo-agents-migration.md` and `wiki/adr/0030-no-repo-local-commit-hook-default.md`. |
| High-Frequency Principles | 35-43 | stable proxy | Keep skill trigger list inline; proxy behavior details to the published `.codex/skills/*/SKILL.md` files. |
| Skill Authoring Contract | 45-53 | inline repo-only hard stop | Keep semantic skill edit gates inline; proxy source requirements to `openspec/specs/skill-authoring-contract/spec.md`, `openspec/specs/skill-evaluation-evidence/spec.md`, and `openspec/specs/local-skill-pressure-tests/spec.md`. |
| Archive Review Default | 55-65 | inline repo-only hard stop | Keep complete/archive stop inline; proxy rationale to `wiki/adr/0007-archive-review-before-archive.md` and `openspec/specs/archive-review-defaults/spec.md`. |
| Explore Trace Default | 67-73 | inline repo-only hard stop | Keep every-explore trace requirement inline; proxy details to `wiki/adr/0009-explore-trace-before-openspec-explore.md` and `openspec/specs/openspec-explore-wiki-trace/spec.md`. |
| Conversation Handoff Default | 75-98 | stable proxy | Keep trigger and durable routing summary inline; proxy method to `openspec/specs/conversation-north-star-handoff/spec.md` and `wiki/ops/conversation-handoff-mode.md`. |
| Example-Driven Capture Default | 100-120 | stable proxy | Keep extracted-learning routing inline; proxy details to `openspec/specs/example-driven-wiki-capture/spec.md`, `openspec/specs/article-learning-capture/spec.md`, and `openspec/specs/learning-capture-routing/spec.md`. |
| Evidence-Backed Best Practice Gate | 122-131 | inline repo-only hard stop | Keep promotion gate inline because it blocks AGENTS/spec/skill hard-rule promotion. |
| Disagreement Management Default | 133-153 | stable proxy | Keep anti-compression trigger inline; proxy method to `openspec/specs/disagreement-management-method/spec.md` and `wiki/ops/disagreement-management-method.md`. |
| Live Conversation Re-Anchor Gate | 155-176 | inline repo-only hard stop | Keep drift stop and unblock conditions inline; proxy details to `openspec/specs/live-conversation-reanchor-gate/spec.md` and `wiki/adr/0024-live-conversation-reanchor-before-continued-implementation.md`. |
| Wiki Naming Model through Wiki Self-Directed Execution | 178-485 | stable proxy | Replace the long runtime chain with a compact "Wiki Runtime Stack" table pointing to specs and wiki ops sources. |
| Scope Of Policy | 487-490 | inline repo-only hard stop | Keep repo-first/global-promotion boundary inline. |
| Material Processing Default | 492-499 | delivery-sensitive inline | Keep user-facing source/ops output boundary inline; proxy formal workflow to `.codex/skills/material-collaboration-defaults/SKILL.md`. |
| Meeting Note Output | 501-510 | delivery-sensitive inline | Keep review/final publication boundary inline; proxy formal workflow to `.codex/skills/meeting-note-output/SKILL.md`. |

## Proxy Acceptance Checks

- Each proxy must point to an existing repo-visible ADR, OpenSpec spec, wiki ops page, or published repo skill.
- Each shortened block must still tell a future agent where to read, how to verify, and when to stop.
- A proxy cannot replace a runtime stop condition unless the stop condition remains visible inline.
- Delivery-sensitive material and meeting-note behavior must keep final output and publication boundaries inline.

## Hard-Stop Preservation Checks

- OpenSpec-level workflow changes still require an active OpenSpec change before edits.
- Completed OpenSpec changes still stop at archive review before archive.
- Every `$openspec-explore` run still leaves a repo-visible trace before continuing.
- Live drift signals still stop implementation until re-anchored.
- Unsupported external learning still cannot become AGENTS/spec/skill hard rules.
- Material and meeting-note outputs still require readable/review output before final publication.

## Implementation Evidence

- Date: 2026-05-07
- Updated file: `AGENTS.md`
- After implementation count: 215 lines / 1609 words / 14908 bytes
- Reduction from baseline: 295 lines / 1821 words / 8670 bytes
- Proxy existence check: all explicit ADR, OpenSpec spec, wiki ops, and
  published repo skill paths referenced by `AGENTS.md` exist locally.
- Delivery boundary check: material processing still requires readable
  `wiki/sources` output before linked `wiki/ops`; meeting-note output still
  requires a review version and blocks final publication while confirmation
  items remain unresolved.
- Agent-legibility check embedded in `AGENTS.md`:
  - where to read: each compact rule points to source paths in the same section
  - how to verify: Hard Stops and Wiki Runtime Stack name the verification
    surface instead of restating full source text
  - when to stop: OpenSpec completion, archive review, `$openspec-explore`,
    live drift, unsupported learning promotion, and delivery publication stops
    remain visible inline

## Final Evaluation

### Before / After Counts

| File | Before | After | Delta |
|---|---:|---:|---:|
| `AGENTS.md` lines | 510 | 215 | -295 |
| `AGENTS.md` words | 3430 | 1609 | -1821 |
| `AGENTS.md` bytes | 23578 | 14908 | -8670 |

### Proxy Coverage

| Surface | Result |
|---|---|
| Section classification | All baseline sections classified before rewrite. |
| Hard-stop preservation | Preserved inline through `AGENTS.md` Hard Stops and delivery workflow sections. |
| Stable proxy targets | ADR, OpenSpec spec, wiki ops, and published repo skill proxies exist locally. |
| Long wiki runtime chain | Replaced by the `Wiki Runtime Stack` table with one row per governed layer. |
| Delivery-sensitive workflows | Kept inline instead of relying on skill proxy alone. |
| Deferred candidates | None in this implementation; all baseline sections were either kept inline, proxied, or kept delivery-sensitive inline. |

### Agent Legibility Result

- Where to read: compact sections list the governing ADR/spec/wiki/skill paths
  immediately next to the rule surface.
- How to verify: OpenSpec validation plus local proxy-existence checks cover the
  structural side; hard-stop text covers behavioral stop conditions.
- When to stop: active-change completion, archive review, explore trace,
  live-reanchor, unsupported-learning promotion, and delivery publication stops
  are still visible without opening secondary files.

### Residual Risks

- The compact `Wiki Runtime Stack` depends on agents following proxy links when
  they need details; `AGENTS.md` no longer repeats full model text.
- The public-facing artifact routing line is a boundary clarification, not a
  full public-workflow design.
- Delivery workflow details still depend on the two published repo skills for
  format depth.
