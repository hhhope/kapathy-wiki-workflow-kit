## RED Baseline

Date: 2026-05-12

| Scenario | Current Evidence | RED Result |
|---|---|---|
| User explicitly invokes `wiki:explore` | `rg "wiki-explore|wiki:explore|/wiki:explore" .codex/skills plugins openspec/specs README.md` has no existing skill, command contract, or spec before this change. | FAIL |
| User rejects a wiki-backed exploration as "not enough" | Existing `wiki-query` only builds bounded context; it does not require current object, evidence surface, or enoughness judgment. | FAIL |
| Agentic collaboration thread replay | The repo eventually reached source map, public timeline, podcast/video pool, evidence matrix, and gate review, but no skill requires future explorations to start with that evidence-surface check. | FAIL |

## GREEN Result

| Scenario | Expected Evidence | Result |
|---|---|---|
| `wiki:explore` trigger exists | `.codex/skills/wiki-explore/SKILL.md` and `plugins/report-wiki-portfolio/commands/wiki-explore.md` exist. | PASS |
| Required output sections are defined | `references/behavior-gate.md` defines Current Object, Opened Evidence, Evidence Surface, Enoughness Judgment, and Next Boundary. | PASS |
| Public-source depth is covered | Behavior gate distinguishes primary, secondary, candidate, transcript/upstream gaps, and internal synthesis. | PASS |
| Agentic collaboration replay passes | Evaluation records that the expected answer opens source map, public timeline, podcast/video pool, evidence matrix, and gate review before judging enoughness. | PASS |
| Skill body stays compact | `wc -l` reports 52 lines for `SKILL.md` and 126 lines for `references/behavior-gate.md`; detailed replay gates live in the reference. | PASS |
| Command surface is visible | `README.md` lists `$wiki-explore`, and `plugins/report-wiki-portfolio/commands/wiki-explore.md` defines `/wiki:explore`. | PASS |
| OpenSpec validation passes | `openspec validate add-wiki-explore-depth-contract --strict` reports `Change 'add-wiki-explore-depth-contract' is valid`. | PASS |

Validation note: the strict validation command emitted PostHog DNS flush errors
after the valid result because network access to `edge.openspec.dev` was not
available. The OpenSpec validation result itself passed.

## Agentic Collaboration GREEN Replay

Input shape:

```text
wiki:explore 看下昨天 agent 团队协作这个事情，我一直说不够
```

Expected behavior:

1. Identify current object as `agentic-product-engineering-collaboration`, not
   inbox cleanup, completion bridge, or a generic remaining-task list.
2. Open repo-visible evidence:
   - `wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md`
   - `wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md`
   - `wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md`
   - `wiki/ops/agentic-product-engineering-collaboration-article-evidence-matrix-2026-05-11.md`
   - `wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md`
3. Report evidence surface:
   - source map exists;
   - broad scan exists;
   - public timeline exists;
   - podcast/video pool exists;
   - evidence matrix exists;
   - gate review exists;
   - residual risks and publication blockers remain.
4. Judge enoughness:
   - enough for internal discussion;
   - not enough for public publication or hard quotation;
   - missing transcript/upstream capture and final role-change integration.

## Residual Risks

- This is behavior guidance, not automatic enforcement.
- The skill depends on future agents actually loading it when `wiki:explore` is
  invoked.
- The required evidence surface is a depth heuristic, not a fixed artifact
  checklist for every topic.
