## Behavior Replay Gate Evaluation

Date: 2026-05-07

## RED Baseline

Command:

```sh
rg -n "Behavior Replay Gate|runtime behavior will trigger|future behavior|next time|replay evidence" AGENTS.md openspec/specs wiki/ops .codex/skills
```

Result before this change:

- No generic `Behavior Replay Gate` existed in repo `AGENTS.md`, `openspec/specs`,
  or `wiki/ops`.
- Matches were specialized or local examples only, including link-trigger replay,
  skill-evaluation evidence, disagreement replay, and re-anchor replay.
- Therefore a future behavior claim could pass by copying one local example
  without a repo-wide rule saying when replay evidence is mandatory.

## GREEN Result

Repo-visible artifacts now expose the generic gate:

| Artifact | Evidence |
|---|---|
| `openspec/changes/generalize-behavior-replay-gate/specs/behavior-replay-gate/spec.md` | Adds the normative requirement that future runtime behavior claims SHALL include replay evidence. |
| `AGENTS.md` | Adds `Behavior Replay Gate` with trigger conditions, minimum evidence, exclusions, and relationship to specialized gates. |
| `wiki/ops/behavior-replay-gate.md` | Explains the gate in Chinese and distinguishes learning capture from future runtime behavior claims. |
| `wiki/ops/index.md` | Adds the method page to the ops entry path. |

## Replay Matrix

| Case | Expected gate behavior | Covered by |
|---|---|---|
| Skill description claims a link or request will trigger next time | Replay evidence required | `AGENTS.md`, behavior replay spec, specialized skill-evaluation gates |
| Repo `AGENTS.md` says the agent should stop, route, or reject in future sessions | Replay evidence required | `AGENTS.md`, behavior replay spec |
| OpenSpec archive / re-anchor / explore hard stop is changed | Replay evidence required | `AGENTS.md`, behavior replay spec, specialized gate if present |
| Article learning produces only candidate observations | Replay evidence not required by default | behavior replay spec narrowness scenario, wiki boundary |
| Candidate learning is promoted into a skill hard rule, AGENTS rule, or spec `SHALL` | Replay evidence required | behavior replay spec promotion scenario |

## Proof Boundary

- This is documentation-level replay proof, not multi-session telemetry.
- No executable automation was added.
- Existing specialized replay specs were not renamed or migrated.
- Root `~/.codex/AGENTS.md` and root/global skills remain out of scope.
- The gate only applies when a future runtime behavior claim is made; ordinary
  source summaries and candidate learning notes stay lightweight.
