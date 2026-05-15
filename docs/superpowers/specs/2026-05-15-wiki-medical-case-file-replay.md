# Wiki Medical Case File Scenario Replay

> Supports OpenSpec change: `introduce-wiki-medical-case-file`.
> This replay is a post-hoc repair artifact for the skipped Superpowers gate.

## Scope

Manual replay against:

- `docs/superpowers/specs/2026-05-15-wiki-medical-case-file-design.md`
- `openspec/changes/introduce-wiki-medical-case-file/design.md`
- `wiki/ops/wiki-medical-case-file-drift-retro-2026-05-15.md`

## Results

| Case | Input / situation | Expected behavior | Pass | Notes |
|---|---|---|---|---|
| 1 | Doctor and confirm records exist, surgery is requested | Open or update one case file first | yes | Surgery is not a new source of truth. |
| 2 | Surgery script writes a generated surgery record | Link it as evidence attachment | yes | It cannot silently override `Confirmed Decisions`. |
| 3 | Human asks what to review | Review case `Confirmed Decisions` first | yes | Surgery plan is a fidelity check. |
| 4 | `relation_weak_evidence` appears in surgery candidates | Keep as manual relation evidence review | yes | No automatic relation write. |
| 5 | `drift_risk`, `adr_risk`, or `openspec_required` appears | Route to governance/OpenSpec review | yes | No direct rule or ADR mutation. |
| 6 | Recovery runs after treatment or surgery | Update case `Recovery` section and link evidence | yes | Recovery proves current state; it does not archive alone. |
| 7 | A later generated stage record disagrees with case decisions | Reject latest-record-wins behavior | yes | New finding must update case decisions or open successor case. |

## Verdict

The case-file model addresses the observed drift by making one durable case the
review surface and keeping generated stage records as evidence attachments.

## Proof Boundary

Replay is design evidence only. Implementation still requires the OpenSpec
tasks to be executed and verified.
