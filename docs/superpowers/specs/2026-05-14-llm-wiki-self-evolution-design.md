# Design: LLM-WIKI Self-Evolution Medical Loop

## Purpose

Define the first shared model for LLM-WIKI self-evolution as a reviewable
medical loop. The model gives the repository a common language for moving from
wiki health signals to diagnosis, human confirmation, repair, verification, and
durable memory.

This design does not authorize new write automation. It does not create a
`wiki-surgery` skill, modify wiki pages, apply frontmatter, accept relation
candidates, write MOC projections, or bypass OpenSpec. It is a conceptual design
for later scoped changes.

## Lifecycle

The LLM-WIKI self-evolution loop is:

```text
checkup -> doctor -> review -> treatment -> surgery -> recovery -> archive
```

- `checkup` performs periodic health checks on wiki structure, such as
  frontmatter, taxonomy, graph, runtime status, and MOC dry-run state.
- `doctor` produces diagnosis records. It does not write structure or approve
  repair.
- `review` is human confirmation of the diagnosis. It decides which findings are
  false positives, which can be treated, which require surgery, and which need
  OpenSpec.
- `treatment` handles low-risk, narrow, explicitly confirmed fixes.
- `surgery` handles large or structural repair, such as batch frontmatter work,
  relation rebuilding, MOC projection writes, governance drift, ADR-sensitive
  pages, or OpenSpec-required changes.
- `recovery` verifies the post-repair state with fresh evidence.
- `archive` links the diagnosis, review, repair, and recovery records into a
  durable case history for future agents.

The core boundary is:

```text
doctor diagnoses; review confirms; treatment or surgery writes; recovery proves;
archive preserves.
```

## Artifact Placement

Each lifecycle stage should leave a repo-visible artifact.

- `checkup` leaves health snapshots such as `wiki/status/*`, frontmatter checker
  reports, graph/status output, and MOC dry-run output.
- `doctor` leaves diagnosis records under
  `wiki/ops/wiki-doctor-runs/*-review.md`.
- `review` should later leave human decision records, for example
  `wiki/ops/wiki-review-decisions/YYYY-MM-DD-*.md`.
- `treatment` should leave narrow change commits, accepted-item lists, and
  verification commands.
- `surgery` should leave an OpenSpec change, batch plan, no-touch zones,
  rollback boundary, and per-batch recovery evidence.
- `recovery` should leave fresh checker, doctor, graph, status, and MOC dry-run
  evidence.
- `archive` should link the full case chain and promote stable decisions into
  ADR only when the decision has stabilized.

The artifact rule is: no important state should live only in stdout or chat.

## Boundary Rules

`treatment` is allowed only for low-risk, narrow, explicitly confirmed repairs.
Examples include a small set of frontmatter edits with clear evidence and no
workflow, skill, ADR, governance, OpenSpec, or relation-semantics change.

`surgery` is required when the repair is large, structural, or governance
sensitive. Triggers include:

- broad batch writes
- relation rebuilding
- MOC projection writes
- ADR or governance pages
- `openspec_required` diagnosis reasons
- high-volume `relation_weak_evidence` findings
- drift, retro, reanchor, or runtime behavior traces
- changes to workflow, skill, AGENTS, OpenSpec, or default repository behavior

`safe_to_apply_frontmatter=true` means a finding can enter treatment review. It
does not mean automatic approval.

`relation_weak_evidence` findings cannot be bulk accepted. They require human
review or a surgery plan with evidence policy.

`openspec_required` findings cannot be handled by treatment. They require a new
or selected OpenSpec change.

`drift/governance` findings cannot be treated as ordinary markdown cleanup. They
need governance review and may require ADR or OpenSpec.

`recovery` is not the same as `archive`. Passing checks proves the immediate
repair state; archive review decides whether the case history is complete enough
to close or promote.

## Current Diagnosis Interpretation

The current detailed wiki-doctor record shows:

- 153 candidates
- 144 review-focus items
- 71 drift/governance risks
- 112 relation evidence warnings
- 9 safe frontmatter candidates

Under this model, the whole case is a `surgery candidate` because the scope is
large and includes governance, relation, ADR, and OpenSpec-sensitive findings.
Inside that case, small confirmed subsets may become `treatment batches`, such
as the 9 safe frontmatter candidates.

The practical rule is:

```text
Treat small confirmed wounds; plan surgery for structural disease.
```

## Future OpenSpec Decomposition

This design should not be implemented as one large change. Later work should be
split into scoped OpenSpec changes:

1. `formalize-llm-wiki-medical-loop`
   - Stabilize the lifecycle vocabulary, artifact boundaries, and escalation
     rules.
   - Do not implement write capability.
2. `add-wiki-review-decisions`
   - Define the human confirmation record that consumes doctor output.
3. `add-wiki-treatment-workflow`
   - Define low-risk confirmed repair, verification, and record keeping.
4. `add-wiki-surgery-workflow`
   - Define structural repair planning, batching, no-touch zones, rollback, and
     OpenSpec-required routing.
5. `add-wiki-recovery-records`
   - Define post-repair evidence records that stitch together checker, doctor,
     graph, status, and MOC dry-run results.

Recommended sequence:

```text
formalize loop -> review decisions -> treatment -> surgery -> recovery
```

The reason is that doctor records now exist, but the repository still lacks a
confirmed diagnosis artifact. Without review decisions, treatment or surgery
would have a broken approval chain.

## Non-Goals

- No automatic wiki repair.
- No bulk relation acceptance.
- No MOC write approval.
- No new skill or command.
- No frontmatter, taxonomy, ADR, AGENTS, or OpenSpec mutation.
- No claim of unrestricted agent autonomy.

## Success Criteria

- Future agents can explain where doctor, treatment, surgery, recovery, and
  archive fit in the existing wiki runtime.
- The model preserves the current OpenSpec and human-confirmation boundaries.
- The next scoped change can start from a clear lifecycle vocabulary without
  re-litigating whether diagnosis, approval, write, verification, and archive are
  separate stages.
