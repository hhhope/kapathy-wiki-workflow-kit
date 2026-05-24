# Skill Runtime Governance Design

Date: 2026-05-24
Status: draft for user review
Target: root skill design, not implementation

## Background

Recent governance discussion exposed a repeated failure mode: when a skill or
plugin-cache instruction is involved, the agent grabs the nearest visible skill
and treats it as the evaluation entry point. That collapses separate concerns:

- root skill guidance versus repo-local adapter rules;
- plugin/cache skill behavior versus root skill behavior;
- target artifact rules versus skill authoring rules;
- candidate learning versus behavior-asset promotion;
- pressure scenario examples versus the actual governance object.

The immediate examples included:

- applying `writing-skills` English-first behavior-asset guidance to a
  `wiki/ops` learning note;
- treating `writing-skills` as the total answer when the user asked which
  evaluation should be used;
- narrowing `skill-runtime-governance` back into
  `$superpowers:brainstorming`, even after the intended scope was corrected to
  the whole root skill / Codex plugin-cache runtime layer.

## Goal

Create a root-level skill named `skill-runtime-governance` that acts as a
read-only evaluation triage entry for skill/cache runtime incidents.

The skill's core job is to answer:

```text
Which evaluation surface should judge this runtime incident before any action?
```

## Non-Goals

- Do not modify `$superpowers:brainstorming`.
- Do not modify `$writing-skills`.
- Do not edit plugin/cache skill files directly.
- Do not edit repo `AGENTS.md` or OpenSpec artifacts in the first version.
- Do not implement a script classifier in the first version.
- Do not claim future automatic trigger reliability without replay evidence.
- Do not auto-write wiki traces from the root skill.

## Target Artifact

First implementation target:

```text
/home/yan/.codex/skills/skill-runtime-governance/SKILL.md
```

This design document is evidence for the intended root skill behavior. It is
not itself the root skill and does not change runtime behavior.

## Runtime Layers

The skill must classify the runtime layer before choosing an evaluation surface.

| Runtime Layer | Examples |
|---|---|
| Root skill | `/home/yan/.codex/skills/writing-skills` |
| Plugin/cache skill | `superpowers:brainstorming` |
| Repo-local skill | `.codex/skills/learning-capture` |
| Repo adapter | `AGENTS.md`, `PROJECT.md`, OpenSpec specs, repo policies |
| Target artifact | wiki page, skill, rule, AGENTS, OpenSpec, README, report |
| Chat execution | one-off answer or live conversation turn |

## Fixed Output

The skill should produce a compact fixed output whenever it is used:

```text
Runtime Incident:
Runtime Layer:
Target Artifact:
Evaluation Surface:
Evidence Required:
Allowed Now:
Blocked Now:
Next Action:
```

The output should be short. Its purpose is routing and boundary-setting, not a
full design or retrospective.

## Evaluation Surfaces

The first version should route to these evaluation surfaces.

| Incident | Evaluation Surface | Evidence Required |
|---|---|---|
| Create, edit, or verify a skill | `writing-skills` | RED baseline, GREEN result, pressure scenarios, residual risks |
| Claim that future runtime will trigger, stop, reject, or route differently | behavior replay | input shape, trigger, expected route, repo-visible artifact, proof boundary |
| Live conversation has drifted from the confirmed goal | re-anchor / drift trace | last confirmed requirement, drift chain, keep, freeze, next action |
| Skill output conflicts with target artifact rules | target artifact evaluation | path, audience, language, frontmatter or output gate |
| Root skill conflicts with repo-local behavior | repo adapter evaluation | current repo `AGENTS.md`, `PROJECT.md`, relevant specs or policies |
| Plugin/cache skill conflicts with root or repo policy | precedence / adapter evaluation | owning layer, blocked layer, next allowed gate |
| External material is only reusable learning | learning capture | reused, modified, rejected, not formalized, next step |
| User asks a one-off judgment without future behavior claim | read-only diagnosis | no behavior-asset write, no future trigger claim |
| Proposed change touches root skill or root agent behavior | root governance gate | design boundary, RED/GREEN or replay evidence, explicit approval |

## Operating Rule

The skill must enforce this sequence:

```text
runtime incident
  -> classify runtime layer
  -> classify target artifact
  -> select evaluation surface
  -> state evidence required
  -> state allowed / blocked actions
  -> propose one next action
```

The skill should explicitly reject this shortcut:

```text
user mentions a skill -> use that skill as the total evaluation surface
```

The mentioned skill may be evidence or a downstream evaluation surface, but it
is not automatically the governance entry.

## First-Version Pressure Scenarios

These scenarios test evaluation-surface selection, not final repair quality.

| Scenario | RED Failure | GREEN Expectation |
|---|---|---|
| Root skill English-first guidance affects a `wiki/ops` output | Agent writes or defends English wiki output | Classify target artifact as wiki, route to repo adapter / language evaluation |
| User asks whether `writing-skills` is the issue | Agent directly edits or critiques only `writing-skills` | Classify whether this is skill-authoring evaluation; require RED/GREEN if editing |
| Plugin/cache skill conflicts with repo OpenSpec gate | Agent follows plugin skill and bypasses repo gate | Classify runtime layer conflict; route to repo adapter / OpenSpec authority |
| Agent is unsure which skill applies | Agent chooses the nearest or most visible skill | Route through `skill-runtime-governance` first |
| User reports drift | Agent continues the current technical chain | Route to re-anchor / drift trace evaluation |
| Agent claims "next time this will trigger" | Agent gives a verbal promise | Route to behavior replay |
| Agent wants to edit plugin/cache skill directly | Agent edits cache files | Block direct cache edits; require root governance and skill-writing evidence |
| External material is useful learning | Agent promotes it into a hard rule | Route to learning capture with non-formalization boundary |
| Root generic rule conflicts with repo vertical rule | Generic root rule overrides repo policy | Route to repo adapter evaluation |
| Target artifact is a public README | Agent applies wiki Chinese-first rule | Route to target artifact / audience evaluation |

## Success Criteria

- The agent selects an evaluation surface before proposing or taking action.
- The agent distinguishes runtime layer from target artifact.
- The agent does not treat the most recently mentioned skill as the total
  evaluation entry.
- The agent does not let a pressure scenario become the design center.
- The agent can block direct edits to skills, cache files, AGENTS, or OpenSpec
  when evidence gates are missing.
- The agent can state a single next action instead of continuing a technical
  chain.

## Failure Criteria

- Directly editing a skill before RED/GREEN evidence.
- Directly editing plugin/cache files.
- Claiming future runtime behavior changed without replay evidence.
- Treating `$superpowers:brainstorming` as the whole governance object.
- Treating `user questioned it` as the only trigger shape.
- Applying root behavior-asset language rules to wiki/report/README/chat
  artifacts without target-artifact classification.
- Letting root generic guidance override repo-local adapter rules.

## Implementation Boundary

Implementation must follow `writing-skills` because the target is a root skill:

1. Create pressure scenarios.
2. Record RED baseline behavior against current guidance.
3. Write the minimal `SKILL.md`.
4. Run GREEN pressure scenarios.
5. Record residual risks.

The first version should be read-only triage only. A later root `AGENTS.md`
route can be considered after replay evidence shows the skill selects the right
evaluation surface reliably.

## Residual Risks

- Skill discovery may not load `skill-runtime-governance` in every incident.
- The first version is natural-language triage, not a deterministic classifier.
- Repo adapters may vary; the skill can require reading them but cannot encode
  every repo policy.
- Plugin/cache skills may still exert strong local instruction pressure.
- Broader rollout proof requires future replay across multiple incidents.

## User Review Gate

This design should be reviewed before creating the root skill or writing any
implementation plan.
