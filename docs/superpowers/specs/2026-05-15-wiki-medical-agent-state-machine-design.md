# Wiki Medical Agent State Machine Design

> Follow-up to `2026-05-15-wiki-medical-case-file-design.md`.
> This design addresses the remaining closure failure: the case file exists,
> but the workflow is not yet forced through one intent-aware state machine.

## Context

The wiki medical-loop workflow has stage records for doctor, confirm,
treatment, surgery, and recovery. A later repair introduced a canonical medical
case file so those records can be treated as evidence attachments instead of
independent sources of truth.

That repair is not yet a closed loop. The current failure modes are:

- `wiki-doctor` and `wiki-recovery` can still behave like stage-centric entry
  points.
- Existing skills can still invite users to run stage workflows directly.
- There is no explicit intent diagnosis step before script execution.
- There is no single active-case resolver.
- Treatment apply does not, by itself, guarantee case update plus recovery plus
  next-action classification.
- Newly discovered candidates can still look executable unless the case file
  explicitly routes them through confirmation.

The user selected the strict direction: one normal user entry point, one human
confirmation surface, no automatic execution of newly discovered candidates, and
automatic recovery after treatment apply.

## Design Goal

Introduce `wiki-medical-agent` as the normal user-facing skill and lifecycle
controller for wiki medical-loop work.

The agent owns:

- user intent diagnosis
- active medical case resolution
- case-state validation
- routing to internal stage workers
- case file updates
- recovery after apply
- final `Next Action` reporting

The existing doctor, confirm, treatment, surgery, and recovery skills and
scripts become internal workers or explicit legacy/debug tools. They do not own
authority.

## User Entry

The normal entry is:

```text
$report-wiki-portfolio:wiki-medical-agent <user intent>
```

Examples:

```text
$report-wiki-portfolio:wiki-medical-agent 看下 wiki 现在什么状态
$report-wiki-portfolio:wiki-medical-agent 诊断需要处理的问题
$report-wiki-portfolio:wiki-medical-agent 我确认病例里的 Confirmed Decisions，继续治疗
$report-wiki-portfolio:wiki-medical-agent apply 已确认的 10 个 treatment candidates
$report-wiki-portfolio:wiki-medical-agent 做 recovery，告诉我是否闭环
```

The old stage skills are not normal user entry points:

```text
wiki-doctor
wiki-confirm
wiki-treatment
wiki-surgery
wiki-recovery
```

On ordinary invocation they should redirect to `wiki-medical-agent`. They may
run only when the user explicitly asks for `legacy`, `debug`, or a non-authority
stage preview.

## Architecture

```text
user request
  -> wiki-medical-agent skill
  -> intent diagnosis
  -> active case resolver
  -> case state machine
  -> internal worker execution
  -> same case file update
  -> recovery / next_action
```

### Intent Diagnosis

The agent must classify the user request before executing anything. Expected
intent values include:

- `status`
- `diagnose`
- `confirm_decisions`
- `treatment_preview`
- `treatment_apply`
- `surgery_plan`
- `recovery`
- `archive_check`
- `legacy_debug`

Each run should show the selected intent in the user-visible result.

### Active Case Resolver

The resolver finds the one authoritative active case file under:

```text
wiki/ops/wiki-medical-cases/
```

Rules:

- No active case: `status` can report `no_case`; `diagnose` may create a new
  case; treatment, surgery, and recovery are blocked.
- One active case: use it.
- Multiple active cases: block write actions and ask the user to choose or
  explicitly allow old cases to be marked inactive.

### Case State Machine

The state machine decides which action is allowed. Stage records cannot change
state directly. Only updates to the case file change authority.

### Worker Adapter

Existing scripts remain useful as workers:

- doctor worker creates diagnosis evidence
- confirm worker creates or updates review decisions
- treatment worker previews or applies confirmed decisions
- surgery worker plans governance-sensitive work
- recovery worker verifies the result and identifies blockers

Worker output is attached back to the same case file as evidence.

## Case File Structure

Each case file should have stable frontmatter-like state:

```yaml
case_id: 2026-05-15-064427
status: diagnosis_ready | awaiting_confirmation | ready_for_treatment | treatment_previewed | treatment_applied | recovery_required | surgery_required | surgery_planned | blocked | archive_ready | followup_required
active: true
source_record: wiki/ops/wiki-doctor-runs/...
confirm_record: wiki/ops/wiki-review-decisions/...
current_intent:
  value: treatment_apply
  decided_at: 2026-05-15T...
  reason: user requested applying confirmed treatment candidates
```

Required body sections:

- `Case Summary`
- `Diagnosis Evidence`
- `Proposed Decisions`
- `Confirmed Decisions`
- `Treatment`
- `Surgery Plan`
- `Recovery`
- `Next Action`
- `Evidence Attachments`
- `Proof Boundary`

Authority rules:

- `Confirmed Decisions` is the only executable decision surface.
- `Proposed Decisions` is not executable.
- `Treatment` records execution results; it does not create new authority.
- `Recovery` can create proposed decisions or blockers, but cannot auto-treat
  new findings.
- `Next Action` is the only trustworthy next-step surface for users.

## State Transitions

Allowed transitions:

```text
no_case
  -> diagnosis_ready

diagnosis_ready
  -> awaiting_confirmation

awaiting_confirmation
  -> ready_for_treatment
  -> surgery_required
  -> blocked

ready_for_treatment
  -> treatment_previewed
  -> treatment_applied

treatment_previewed
  -> treatment_applied
  -> awaiting_confirmation

treatment_applied
  -> recovery_required

recovery_required
  -> archive_ready
  -> awaiting_confirmation
  -> surgery_required
  -> blocked
  -> followup_required

surgery_required
  -> surgery_planned
  -> awaiting_confirmation
  -> blocked

surgery_planned
  -> awaiting_confirmation
  -> blocked
```

Hard rules:

- Without `Confirmed Decisions`, treatment apply is blocked.
- After treatment apply, recovery is mandatory.
- Recovery findings become proposed decisions unless they are blockers or
  surgery candidates.
- Relation weak evidence, governance, OpenSpec, and ADR issues cannot be
  auto-treated.
- Multiple active cases block write actions.
- Legacy stage records are evidence only.

## Treatment Apply Flow

For:

```text
$report-wiki-portfolio:wiki-medical-agent apply 已确认的 10 个 treatment candidates
```

Expected flow:

```text
resolve active case
-> classify intent as treatment_apply
-> verify state allows treatment
-> verify exactly 10 executable confirmed decisions
-> apply treatment
-> attach treatment record
-> mark treatment_applied
-> run recovery
-> attach recovery record
-> set next_action
```

Expected successful output:

```text
Intent: treatment_apply
Case: wiki/ops/wiki-medical-cases/...
State before: ready_for_treatment
Applied: 10
Recovery: completed
State after: archive_ready | awaiting_confirmation | surgery_required | blocked
Next Action: ...
Evidence:
- treatment_record: ...
- recovery_record: ...
```

Expected blocked output:

```text
Intent: treatment_apply
Case: wiki/ops/wiki-medical-cases/...
Blocked: confirmed_decision_count_mismatch
Expected by user: 10
Executable in case: 0
Next Action: awaiting_confirmation
```

## Legacy And Debug Boundary

Old stage skills and scripts may remain available for low-level evidence or
debugging, but they must not produce authoritative workflow state.

Required script-level direction:

- `build_wiki_treatment.py`: `--apply` requires `--case-file`; no case file is
  legacy preview only.
- `build_wiki_surgery.py`: authoritative surgery planning requires
  `--case-file`.
- `build_wiki_recovery.py`: authoritative recovery requires `--case-file` and
  writes back to the same case.
- `build_wiki_review_decisions.py`: review output must be synchronized into the
  case file before it can authorize treatment.
- `build_wiki_content_adjudication.py`: doctor output is diagnosis evidence
  only.

## Error Handling

Every run should show:

```text
Intent: ...
Case: ...
State: ...
Allowed action: ...
Blocked action: ...
Next Action: ...
```

Blocking conditions:

- no active case for treatment, surgery, or recovery
- multiple active cases for any write action
- diagnosis exists but no confirmed decisions
- user-requested candidate count does not match executable confirmed decisions
- recovery discovers new candidates
- relation/governance/OpenSpec/ADR work needs surgery or human confirmation

## Verification Plan

Verification must cover more than "the script runs".

### Intent Routing

Replay natural-language requests for status, diagnosis, confirmation, treatment
apply, and recovery. Each should produce `Intent`, `Case`, `State`, allowed or
blocked action, and `Next Action`.

### State Machine

Cover these cases:

- `no_case` allows diagnosis but blocks treatment.
- `awaiting_confirmation` blocks treatment.
- `ready_for_treatment` allows treatment preview and apply.
- `treatment_applied` requires recovery.
- recovery with new candidates returns to `awaiting_confirmation`.
- clean recovery reaches `archive_ready`.
- multiple active cases block write actions.

### Drift Prevention

Verify ordinary invocation of old stage skills does not create authority.

Script-level checks:

- treatment apply without case file fails
- authoritative recovery without case file fails
- authoritative surgery without case file fails

### Real Replay

Replay the current 10 treatment candidates through `wiki-medical-agent`.

Completion requires the case file to show:

- `Treatment: applied`
- `Recovery: completed`
- `Next Action: archive_ready | awaiting_confirmation | surgery_required | blocked`
- treatment and recovery evidence attachments

## Residual Risks

- Historical case files may lack newer fields and need migration or legacy
  marking.
- Historical stage records remain useful evidence but are not authoritative.
- Multiple active cases may block the first real run until the user selects the
  active case.
- Governance and relation issues remain non-automatic by design.

## Approval State

The user approved the strict approach in chat:

- one normal user entry: `wiki-medical-agent`
- old stage skills downgraded to internal or legacy/debug entry points
- human confirmation only through case-file `Confirmed Decisions`
- treatment apply automatically followed by recovery
- newly discovered candidates never auto-execute
