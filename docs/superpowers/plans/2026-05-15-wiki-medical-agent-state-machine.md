# Wiki Medical Agent State Machine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `wiki-medical-agent` as the single normal entry point for wiki medical-loop work, backed by an explicit case-file state machine.

**Architecture:** Add a small state-machine module that resolves active case files, classifies user intent, validates allowed transitions, and delegates to existing doctor/confirm/treatment/surgery/recovery workers. Extend the medical case file package with durable state fields, proposed decisions, current intent, active-case metadata, treatment/recovery update helpers, and next-action reporting.

**Tech Stack:** Python stdlib CLI modules, existing Markdown + embedded JSON case files, `unittest`, existing repo-local wiki scripts and `.codex/skills/*`.

---

## Scope Boundary

The previous OpenSpec change `introduce-wiki-medical-case-file` is already complete. Do not add implementation tasks to that completed change. This plan starts with a new OpenSpec change for the state-machine layer, then implements only that scoped change.

Do not apply real wiki treatment during plan execution except inside isolated temporary test directories.

## File Structure

- Create: `openspec/changes/introduce-wiki-medical-agent-state-machine/proposal.md`
  Owns the lifecycle proposal for the new agent and state machine.
- Create: `openspec/changes/introduce-wiki-medical-agent-state-machine/design.md`
  Mirrors the approved Superpowers design in OpenSpec form.
- Create: `openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md`
  Tracks execution tasks and the OpenSpec hard stop.
- Create: `openspec/changes/introduce-wiki-medical-agent-state-machine/specs/wiki-medical-agent/spec.md`
  Defines SHALL requirements for intent routing, active-case resolution, transitions, legacy boundaries, and recovery closure.
- Create: `scripts/wiki_medical_agent.py`
  Pure state-machine and orchestration helpers. No argparse in this file.
- Create: `scripts/build_wiki_medical_agent.py`
  CLI wrapper for `wiki-medical-agent`.
- Create: `.codex/skills/wiki-medical-agent/SKILL.md`
  User-facing skill entry point.
- Modify: `scripts/wiki_medical_case.py`
  Add case state helpers and treatment/recovery update helpers.
- Modify: `scripts/build_wiki_treatment.py`
  Enforce case-file authority for `--apply`; keep legacy preview explicit.
- Modify: `scripts/wiki_recovery.py`
  Add recovery classification helpers that can update a case.
- Modify: `scripts/build_wiki_recovery.py`
  Add `--case-file` and `--update-case-file` support.
- Modify: `.codex/skills/wiki-doctor/SKILL.md`
  Redirect ordinary use to `wiki-medical-agent`; legacy/debug remains evidence-only.
- Modify: `.codex/skills/wiki-confirm/SKILL.md`
  Redirect ordinary use to `wiki-medical-agent`; legacy/debug remains evidence-only.
- Modify: `.codex/skills/wiki-treatment/SKILL.md`
  Redirect ordinary use to `wiki-medical-agent`; legacy/debug remains evidence-only.
- Modify: `.codex/skills/wiki-surgery/SKILL.md`
  Redirect ordinary use to `wiki-medical-agent`; legacy/debug remains evidence-only.
- Modify: `.codex/skills/wiki-recovery/SKILL.md`
  Redirect ordinary use to `wiki-medical-agent`; legacy/debug remains evidence-only.
- Modify: `tests/test_wiki_medical_case.py`
  Cover state fields, active metadata, proposed decisions, and update helpers.
- Create: `tests/test_wiki_medical_agent.py`
  Cover intent classification, active-case resolution, state validation, and CLI replay behavior.
- Modify: `tests/test_wiki_treatment.py`
  Update tests for case-file-required apply and explicit legacy preview.
- Modify: `tests/test_wiki_recovery.py`
  Cover case-aware recovery and case update behavior.
- Modify: `tests/test_wiki_medical_loop_skills.py`
  Cover new skill and legacy redirection markers.
- Modify: `openspec/changes/introduce-wiki-medical-agent-state-machine/evaluation.md`
  Record behavior replay, test results, OpenSpec validation, and behavior-asset checks.

## Task 1: Create The OpenSpec Change

**Files:**
- Create: `openspec/changes/introduce-wiki-medical-agent-state-machine/proposal.md`
- Create: `openspec/changes/introduce-wiki-medical-agent-state-machine/design.md`
- Create: `openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md`
- Create: `openspec/changes/introduce-wiki-medical-agent-state-machine/specs/wiki-medical-agent/spec.md`

- [ ] **Step 1: Write the OpenSpec proposal**

Create `openspec/changes/introduce-wiki-medical-agent-state-machine/proposal.md` with:

```markdown
# Proposal: introduce wiki medical agent state machine

## Summary

Introduce `wiki-medical-agent` as the single normal user-facing entry point for
the LLM-WIKI medical loop. The agent diagnoses user intent, resolves the active
medical case file, validates state transitions, delegates to existing stage
workers, writes results back to the same case file, and reports the next action.

## Problem

The repository now has a canonical wiki medical case file, but the workflow is
not closed. Some stage skills and scripts can still behave as independent
entry points, recovery is not case-file-aware, and treatment apply does not
guarantee recovery plus next-action classification.

This leaves the workflow vulnerable to authority drift:

```text
stage record -> another stage record -> latest generated output looks authoritative
```

## Scope

In scope:

- Add `wiki-medical-agent` skill and CLI.
- Add intent diagnosis before execution.
- Add active case resolution and multiple-active-case blocking.
- Add case state transition validation.
- Require case-file authority for treatment apply, surgery planning, and
  recovery closure.
- Update treatment apply to run recovery through the agent.
- Downgrade old stage skills to internal or explicit legacy/debug entry points.
- Add replay evidence for the current "apply 10 treatment candidates" flow.

Out of scope:

- Automatic relation repair.
- Automatic governance, ADR, OpenSpec, or MOC changes.
- Rewriting historical stage records.
- Applying real wiki treatments outside explicit user approval.

## Success Criteria

- Ordinary users can start with
  `$report-wiki-portfolio:wiki-medical-agent <intent>`.
- The agent output includes intent, case, state, allowed or blocked action, and
  next action.
- Treatment apply requires case-file confirmed decisions and automatically runs
  recovery afterward.
- Recovery results update the same case file and produce one of:
  `archive_ready`, `awaiting_confirmation`, `surgery_required`, `blocked`, or
  `followup_required`.
- Old stage skills redirect ordinary usage to `wiki-medical-agent`.
- Tests prove legacy stage outputs cannot become authoritative without a case.
```

- [ ] **Step 2: Write the OpenSpec design**

Create `openspec/changes/introduce-wiki-medical-agent-state-machine/design.md` by adapting the approved Superpowers spec at `docs/superpowers/specs/2026-05-15-wiki-medical-agent-state-machine-design.md`. Keep these sections:

```markdown
# Design: wiki medical agent state machine

## Core Model

`wiki-medical-agent` is the lifecycle controller. It is not a sixth stage.

```text
user request
  -> intent diagnosis
  -> active case resolver
  -> case state machine
  -> internal worker execution
  -> same case file update
  -> recovery / next_action
```

## Authority

The case file is the only authority. Stage records are evidence attachments.
`Confirmed Decisions` is the only executable decision surface.

## Normal Entry

Use:

```text
$report-wiki-portfolio:wiki-medical-agent <intent>
```

Old stage skills redirect ordinary use to the agent and only run in explicit
legacy/debug mode.

## State Rules

No confirmed decisions means no treatment apply. Treatment apply must run
recovery. Recovery findings become proposed decisions, blockers, or surgery
requirements; they do not auto-execute.

## Boundaries

The agent must not automatically write relations, taxonomy config, MOC pages,
ADRs, AGENTS, skills, or OpenSpec lifecycle state.
```

- [ ] **Step 3: Write OpenSpec tasks**

Create `openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md` with:

```markdown
# Tasks

- [ ] 1. Create OpenSpec proposal, design, tasks, spec delta, and initial evaluation stub.
- [ ] 2. Add RED tests for medical-agent intent diagnosis and active-case resolution.
- [ ] 3. Add case state helpers to `scripts/wiki_medical_case.py`.
- [ ] 4. Implement `scripts/wiki_medical_agent.py` intent and state validation.
- [ ] 5. Add `scripts/build_wiki_medical_agent.py` CLI.
- [ ] 6. Make treatment apply require case-file authority and explicit legacy preview for raw scans.
- [ ] 7. Make recovery case-file-aware and able to update the same case file.
- [ ] 8. Implement treatment apply orchestration: apply, attach treatment record, run recovery, update next action.
- [ ] 9. Add `.codex/skills/wiki-medical-agent/SKILL.md` and downgrade old stage skills to redirect ordinary usage.
- [ ] 10. Add behavior replay and skill tests.
- [ ] 11. Run focused tests, frontmatter taxonomy check for new wiki case outputs if any, OpenSpec strict validation, and behavior-asset checks.
- [ ] 12. Commit verified implementation and stop at OpenSpec hard stop.
```

- [ ] **Step 4: Write the spec delta**

Create `openspec/changes/introduce-wiki-medical-agent-state-machine/specs/wiki-medical-agent/spec.md` with:

```markdown
# wiki-medical-agent Specification

## ADDED Requirements

### Requirement: Normal medical-loop entry SHALL route through wiki-medical-agent

Ordinary user requests for wiki medical-loop status, diagnosis, confirmation,
treatment, surgery, recovery, or archive checks SHALL use `wiki-medical-agent`
as the user-facing controller.

#### Scenario: User asks to apply confirmed treatment candidates

- **WHEN** the user asks to apply confirmed treatment candidates
- **THEN** the controller SHALL classify intent as `treatment_apply`
- **AND** resolve exactly one active case file
- **AND** validate executable confirmed treatment decisions before applying

### Requirement: Case file SHALL be the only authority

The controller SHALL treat stage records as evidence attachments. It SHALL not
execute treatment, surgery, or recovery authority from raw stage records unless
the result has been synchronized into the active case file.

#### Scenario: Legacy stage record exists

- **GIVEN** a doctor, confirm, treatment, surgery, or recovery record exists
- **WHEN** it is not attached to the active case file
- **THEN** it SHALL NOT change case state

### Requirement: Treatment apply SHALL be followed by recovery

Treatment apply SHALL update the active case file, attach treatment evidence,
run recovery, attach recovery evidence, and set `Next Action`.

#### Scenario: Apply succeeds and recovery passes

- **GIVEN** the active case has executable confirmed treatment decisions
- **WHEN** the controller applies them successfully
- **THEN** it SHALL run recovery
- **AND** set the case next action from the recovery result

### Requirement: New findings SHALL not auto-execute

New findings from doctor, surgery, or recovery SHALL enter `Proposed Decisions`,
`surgery_required`, or `blocked` state. They SHALL NOT be applied automatically.

#### Scenario: Recovery finds new candidates

- **WHEN** recovery discovers new treatment candidates
- **THEN** the controller SHALL write them to `Proposed Decisions`
- **AND** set `Next Action` to `awaiting_confirmation`
```

- [ ] **Step 5: Validate the new OpenSpec skeleton**

Run:

```bash
openspec validate introduce-wiki-medical-agent-state-machine --strict
```

Expected: validation passes.

- [ ] **Step 6: Commit the OpenSpec skeleton**

Run:

```bash
git status --short
git add openspec/changes/introduce-wiki-medical-agent-state-machine
git commit -m "docs: propose wiki medical agent state machine"
```

Expected: commit includes only the new OpenSpec change files.

## Task 2: Add RED Tests For Intent And Active Case Resolution

**Files:**
- Create: `tests/test_wiki_medical_agent.py`

- [ ] **Step 1: Write failing tests**

Create `tests/test_wiki_medical_agent.py` with:

```python
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_medical_case import build_medical_case_package, write_medical_case_file
from scripts.wiki_medical_agent import (
    classify_medical_intent,
    resolve_active_case,
    validate_case_action,
)


class WikiMedicalAgentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-medical-agent-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _case_package(self, status: str = "ready_for_treatment", active: bool = True) -> dict:
        package = build_medical_case_package(
            {
                "generated_at": "2026-05-15T01:02:03+00:00",
                "summary": {},
                "source_adjudication_summary": {},
                "accepted_candidates": [],
                "rejected_candidates": [],
                "deferred_items": [],
                "surgery_candidates": [],
                "openspec_required": [],
                "treatment_candidates": [
                    {
                        "detail_ref": "detail-safe",
                        "path": "wiki/ops/safe.md",
                        "risk_flags": [],
                        "suggested_frontmatter": {
                            "layer": "ops",
                            "domain": "wiki",
                            "ops_area": "wiki-runtime",
                            "canonical_object": "safe",
                            "artifact_type": "method",
                        },
                    }
                ],
            },
            case_slug="confirmed-case",
            timestamp="2026-05-15T01:02:03+00:00",
        )
        package["status"] = status
        package["active"] = active
        return package

    def _write_case(self, package: dict, timestamp: str) -> Path:
        return write_medical_case_file(
            package,
            self.tmpdir,
            output_dir=self.tmpdir / "wiki" / "ops" / "wiki-medical-cases",
            timestamp=timestamp,
        )

    def test_classifies_natural_language_intents(self) -> None:
        self.assertEqual(classify_medical_intent("看下 wiki 现在什么状态").intent, "status")
        self.assertEqual(classify_medical_intent("诊断需要处理的问题").intent, "diagnose")
        self.assertEqual(classify_medical_intent("我确认病例里的 Confirmed Decisions").intent, "confirm_decisions")
        self.assertEqual(classify_medical_intent("apply 已确认的 10 个 treatment candidates").intent, "treatment_apply")
        self.assertEqual(classify_medical_intent("做 recovery，告诉我是否闭环").intent, "recovery")

    def test_resolve_active_case_blocks_multiple_active_cases(self) -> None:
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:03+00:00")
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:04+00:00")

        resolved = resolve_active_case(self.tmpdir)

        self.assertEqual(resolved.status, "blocked")
        self.assertEqual(resolved.blocked_reason, "multiple_active_cases")
        self.assertEqual(len(resolved.candidates), 2)

    def test_validate_blocks_treatment_without_confirmed_decisions(self) -> None:
        package = self._case_package(status="awaiting_confirmation")
        package["confirmed_decisions"]["treatment_candidates"] = []

        result = validate_case_action(package, "treatment_apply", expected_count=10)

        self.assertFalse(result.allowed)
        self.assertEqual(result.blocked_reason, "no_executable_confirmed_treatment_decisions")

    def test_validate_allows_matching_confirmed_treatment_count(self) -> None:
        result = validate_case_action(self._case_package(), "treatment_apply", expected_count=1)

        self.assertTrue(result.allowed)
        self.assertEqual(result.allowed_action, "apply_confirmed_treatments")

    def test_cli_status_outputs_intent_case_state_and_next_action(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        case_path = self._write_case(self._case_package(), "2026-05-15T01:02:03+00:00")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "看下 wiki 现在什么状态",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(payload["intent"], "status")
        self.assertEqual(payload["case_path"], case_path.as_posix())
        self.assertEqual(payload["state"], "ready_for_treatment")
        self.assertIn("next_action", payload)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the RED tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent -v
```

Expected: FAIL because `scripts/wiki_medical_agent.py` does not exist.

- [ ] **Step 3: Commit the RED tests**

Run:

```bash
git add tests/test_wiki_medical_agent.py openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md
git commit -m "test: add wiki medical agent red tests"
```

Expected: commit contains the new RED test file and tasks progress only.

## Task 3: Add Case State Helpers

**Files:**
- Modify: `scripts/wiki_medical_case.py`
- Modify: `tests/test_wiki_medical_case.py`

- [ ] **Step 1: Add failing case-state tests**

Append to `tests/test_wiki_medical_case.py`:

```python
    def test_case_package_has_state_active_and_proposed_decisions(self) -> None:
        package = build_medical_case_package(self._decision_package())

        self.assertEqual(package["status"], "awaiting_confirmation")
        self.assertTrue(package["active"])
        self.assertIn("proposed_decisions", package)
        self.assertEqual(package["archive_next_action"]["next_action"], "awaiting_confirmation")

    def test_updates_case_with_recovery_result_and_next_action(self) -> None:
        from scripts.wiki_medical_case import attach_recovery_result_to_case

        package = build_medical_case_package(self._decision_package())
        updated = attach_recovery_result_to_case(
            package,
            {
                "passed": True,
                "next_route": "archive-ready",
                "summary": {"check_count": 2, "failed_count": 0},
            },
            recovery_record="wiki/ops/wiki-recovery-runs/recovery.md",
        )

        self.assertEqual(updated["recovery"]["status"], "completed")
        self.assertEqual(updated["status"], "archive_ready")
        self.assertEqual(updated["archive_next_action"]["next_action"], "archive_ready")
        self.assertIn("wiki/ops/wiki-recovery-runs/recovery.md", updated["evidence_attachments"]["recovery"])
```

- [ ] **Step 2: Run tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_case -v
```

Expected: FAIL because `proposed_decisions`, new default status, and `attach_recovery_result_to_case` are not implemented.

- [ ] **Step 3: Implement case helpers**

In `scripts/wiki_medical_case.py`, add constants near `DECISION_BUCKETS`:

```python
CASE_STATUSES = {
    "diagnosis_ready",
    "awaiting_confirmation",
    "ready_for_treatment",
    "treatment_previewed",
    "treatment_applied",
    "recovery_required",
    "surgery_required",
    "surgery_planned",
    "blocked",
    "archive_ready",
    "followup_required",
}
```

In `build_medical_case_package`, change default top-level state to:

```python
"status": "awaiting_confirmation",
"active": True,
"current_intent": {},
"proposed_decisions": {
    "treatment_candidates": [],
    "surgery_candidates": [],
    "openspec_required": [],
    "blockers": [],
},
```

Change `archive_next_action` default to:

```python
"archive_next_action": {
    "status": "awaiting_confirmation",
    "next_action": "awaiting_confirmation",
    "reason": "Confirmed Decisions require human review before treatment or surgery.",
},
```

Add:

```python
def _normalize_next_action(next_route: str | None, passed: bool | None = None) -> str:
    route = str(next_route or "").strip().replace("-", "_")
    if route in {"archive_ready", "awaiting_confirmation", "surgery_required", "blocked", "followup_required"}:
        return route
    if route == "archive_ready":
        return "archive_ready"
    if route == "blocked_by_recovery_findings":
        return "blocked"
    if passed is True:
        return "archive_ready"
    return "blocked"


def attach_recovery_result_to_case(
    case_package: dict[str, Any],
    recovery_package: dict[str, Any],
    recovery_record: str | Path | None = None,
) -> dict[str, Any]:
    updated = copy.deepcopy(case_package)
    record_text = str(recovery_record) if recovery_record else ""
    records = list(_as_list(updated.get("recovery", {}).get("records")))
    attachments = updated.setdefault("evidence_attachments", {}).setdefault("recovery", [])
    if record_text and record_text not in records:
        records.append(record_text)
    if record_text and record_text not in attachments:
        attachments.append(record_text)
    next_action = _normalize_next_action(
        str(recovery_package.get("next_route", "")),
        recovery_package.get("passed") is True,
    )
    updated["recovery"] = {
        "status": "completed",
        "records": records,
        "summary": copy.deepcopy(recovery_package.get("summary", {})),
        "result": copy.deepcopy(recovery_package),
    }
    updated["status"] = next_action
    updated["archive_next_action"] = {
        "status": next_action,
        "next_action": next_action,
        "reason": "Recovery result set the next medical-loop action.",
    }
    return updated
```

Update `render_medical_case_markdown` to render `## Proposed Decisions` before `## Confirmed Decisions`:

```python
    lines.extend(["", "## Proposed Decisions"])
    proposed = package.get("proposed_decisions", {})
    if isinstance(proposed, dict):
        for key in ("treatment_candidates", "surgery_candidates", "openspec_required", "blockers"):
            lines.extend(_bucket_lines(key.replace("_", " ").title(), _copy_bucket(proposed, key)))
    else:
        lines.append("- None")
```

- [ ] **Step 4: Run case tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_case -v
```

Expected: PASS.

- [ ] **Step 5: Commit case helpers**

Run:

```bash
git add scripts/wiki_medical_case.py tests/test_wiki_medical_case.py
git commit -m "feat: add wiki medical case state helpers"
```

## Task 4: Implement Medical Agent Intent And State Validation

**Files:**
- Create: `scripts/wiki_medical_agent.py`
- Modify: `tests/test_wiki_medical_agent.py`

- [ ] **Step 1: Create the state-machine module**

Create `scripts/wiki_medical_agent.py`:

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any

from scripts.wiki_medical_case import DEFAULT_MEDICAL_CASE_DIR, load_medical_case_file


@dataclass(frozen=True)
class IntentResult:
    intent: str
    expected_count: int | None = None
    reason: str = ""


@dataclass(frozen=True)
class ActiveCaseResolution:
    status: str
    case_path: Path | None = None
    case_package: dict[str, Any] | None = None
    candidates: tuple[Path, ...] = ()
    blocked_reason: str = ""


@dataclass(frozen=True)
class ActionValidation:
    allowed: bool
    intent: str
    state: str
    allowed_action: str = ""
    blocked_reason: str = ""
    executable_count: int = 0
    expected_count: int | None = None


def classify_medical_intent(text: str) -> IntentResult:
    lowered = text.lower()
    count_match = re.search(r"(\d+)", text)
    expected_count = int(count_match.group(1)) if count_match else None
    if "legacy" in lowered or "debug" in lowered:
        return IntentResult("legacy_debug", expected_count, "explicit legacy/debug request")
    if any(token in lowered for token in ["apply", "应用", "治疗这", "执行治疗"]):
        return IntentResult("treatment_apply", expected_count, "user requested treatment apply")
    if any(token in lowered for token in ["preview", "dry-run", "预览"]):
        return IntentResult("treatment_preview", expected_count, "user requested treatment preview")
    if any(token in lowered for token in ["确认", "确诊", "confirmed decisions"]):
        return IntentResult("confirm_decisions", expected_count, "user referenced confirmed decisions")
    if any(token in lowered for token in ["诊断", "doctor"]):
        return IntentResult("diagnose", expected_count, "user requested diagnosis")
    if any(token in lowered for token in ["手术", "surgery"]):
        return IntentResult("surgery_plan", expected_count, "user requested surgery planning")
    if any(token in lowered for token in ["复查", "recovery", "闭环"]):
        return IntentResult("recovery", expected_count, "user requested recovery")
    if any(token in lowered for token in ["归档", "archive"]):
        return IntentResult("archive_check", expected_count, "user requested archive check")
    return IntentResult("status", expected_count, "default status request")


def _case_sort_key(path: Path) -> str:
    return path.name


def resolve_active_case(root: Path | str) -> ActiveCaseResolution:
    root_path = Path(root)
    case_dir = root_path / DEFAULT_MEDICAL_CASE_DIR
    if not case_dir.exists():
        return ActiveCaseResolution(status="no_case")
    candidates: list[Path] = []
    for path in sorted(case_dir.glob("*.md"), key=_case_sort_key):
        try:
            package = load_medical_case_file(path)
        except (OSError, ValueError):
            continue
        if package.get("active", True) is True and str(package.get("status", "")) != "closed":
            candidates.append(path.resolve())
    if not candidates:
        return ActiveCaseResolution(status="no_case")
    if len(candidates) > 1:
        return ActiveCaseResolution(
            status="blocked",
            candidates=tuple(candidates),
            blocked_reason="multiple_active_cases",
        )
    package = load_medical_case_file(candidates[0])
    package["case_path"] = candidates[0].as_posix()
    return ActiveCaseResolution(status="ok", case_path=candidates[0], case_package=package)


def _confirmed_treatment_decisions(case_package: dict[str, Any]) -> list[dict[str, Any]]:
    confirmed = case_package.get("confirmed_decisions", {})
    if not isinstance(confirmed, dict):
        return []
    values = confirmed.get("treatment_candidates", [])
    return [item for item in values if isinstance(item, dict)]


def validate_case_action(
    case_package: dict[str, Any],
    intent: str,
    expected_count: int | None = None,
) -> ActionValidation:
    state = str(case_package.get("status", "awaiting_confirmation"))
    treatment_count = len(_confirmed_treatment_decisions(case_package))
    if intent == "status":
        return ActionValidation(True, intent, state, allowed_action="report_status", executable_count=treatment_count)
    if intent == "diagnose":
        return ActionValidation(True, intent, state, allowed_action="run_diagnosis", executable_count=treatment_count)
    if intent == "treatment_preview":
        if treatment_count == 0:
            return ActionValidation(False, intent, state, blocked_reason="no_executable_confirmed_treatment_decisions")
        return ActionValidation(True, intent, state, allowed_action="preview_confirmed_treatments", executable_count=treatment_count)
    if intent == "treatment_apply":
        if state not in {"ready_for_treatment", "treatment_previewed"}:
            return ActionValidation(False, intent, state, blocked_reason="state_does_not_allow_treatment_apply", executable_count=treatment_count, expected_count=expected_count)
        if treatment_count == 0:
            return ActionValidation(False, intent, state, blocked_reason="no_executable_confirmed_treatment_decisions", executable_count=0, expected_count=expected_count)
        if expected_count is not None and expected_count != treatment_count:
            return ActionValidation(False, intent, state, blocked_reason="confirmed_decision_count_mismatch", executable_count=treatment_count, expected_count=expected_count)
        return ActionValidation(True, intent, state, allowed_action="apply_confirmed_treatments", executable_count=treatment_count, expected_count=expected_count)
    if intent == "recovery":
        if state not in {"treatment_applied", "recovery_required"}:
            return ActionValidation(False, intent, state, blocked_reason="state_does_not_require_recovery", executable_count=treatment_count)
        return ActionValidation(True, intent, state, allowed_action="run_recovery", executable_count=treatment_count)
    if intent == "surgery_plan":
        return ActionValidation(True, intent, state, allowed_action="plan_surgery", executable_count=treatment_count)
    if intent == "archive_check":
        return ActionValidation(True, intent, state, allowed_action="report_archive_readiness", executable_count=treatment_count)
    return ActionValidation(False, intent, state, blocked_reason="unsupported_intent", executable_count=treatment_count)
```

- [ ] **Step 2: Run intent tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent -v
```

Expected: tests still fail only because the CLI is not created yet.

- [ ] **Step 3: Commit state-machine core**

Run:

```bash
git add scripts/wiki_medical_agent.py tests/test_wiki_medical_agent.py
git commit -m "feat: add wiki medical agent state core"
```

## Task 5: Add Medical Agent CLI Status And Blocking Output

**Files:**
- Create: `scripts/build_wiki_medical_agent.py`
- Modify: `scripts/wiki_medical_agent.py`
- Modify: `tests/test_wiki_medical_agent.py`

- [ ] **Step 1: Add CLI orchestration helper**

Append to `scripts/wiki_medical_agent.py`:

```python
def build_status_payload(root: Path | str, intent_text: str) -> dict[str, Any]:
    intent = classify_medical_intent(intent_text)
    resolution = resolve_active_case(root)
    if resolution.status == "no_case":
        return {
            "intent": intent.intent,
            "case_path": "",
            "state": "no_case",
            "allowed": intent.intent in {"status", "diagnose"},
            "allowed_action": "run_diagnosis" if intent.intent == "diagnose" else "report_status",
            "blocked_reason": "" if intent.intent in {"status", "diagnose"} else "no_active_case",
            "next_action": "diagnose",
        }
    if resolution.status == "blocked":
        return {
            "intent": intent.intent,
            "case_path": "",
            "state": "blocked",
            "allowed": False,
            "allowed_action": "",
            "blocked_reason": resolution.blocked_reason,
            "candidate_cases": [path.as_posix() for path in resolution.candidates],
            "next_action": "select_active_case",
        }
    assert resolution.case_path is not None
    assert resolution.case_package is not None
    validation = validate_case_action(
        resolution.case_package,
        intent.intent,
        expected_count=intent.expected_count,
    )
    archive = resolution.case_package.get("archive_next_action", {})
    next_action = archive.get("next_action") if isinstance(archive, dict) else ""
    return {
        "intent": intent.intent,
        "case_path": resolution.case_path.as_posix(),
        "state": validation.state,
        "allowed": validation.allowed,
        "allowed_action": validation.allowed_action,
        "blocked_reason": validation.blocked_reason,
        "executable_count": validation.executable_count,
        "expected_count": validation.expected_count,
        "next_action": str(next_action or validation.allowed_action or validation.blocked_reason),
    }
```

- [ ] **Step 2: Create the CLI wrapper**

Create `scripts/build_wiki_medical_agent.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.wiki_medical_agent import build_status_payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the wiki medical agent state controller.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--intent-text", required=True, help="Natural-language user intent to route.")
    args = parser.parse_args()

    payload = build_status_payload(Path(args.root).resolve(), args.intent_text)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Run CLI tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent -v
```

Expected: PASS for status and blocking tests.

- [ ] **Step 4: Commit CLI status support**

Run:

```bash
git add scripts/wiki_medical_agent.py scripts/build_wiki_medical_agent.py tests/test_wiki_medical_agent.py
git commit -m "feat: add wiki medical agent cli status"
```

## Task 6: Enforce Case-File Authority For Treatment Apply

**Files:**
- Modify: `scripts/build_wiki_treatment.py`
- Modify: `tests/test_wiki_treatment.py`

- [ ] **Step 1: Add failing treatment CLI tests**

Append to `tests/test_wiki_treatment.py`:

```python
    def test_cli_apply_requires_case_file(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_treatment.py",
                "--root",
                str(self.tmpdir),
                "--approved-domain",
                "wiki",
                "--apply",
            ],
            cwd=repo_root,
            text=True,
            capture_output=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--apply requires --case-file", result.stderr)

    def test_cli_raw_scan_requires_legacy_preview_without_case_file(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_treatment.py",
                "--root",
                str(self.tmpdir),
                "--approved-domain",
                "wiki",
            ],
            cwd=repo_root,
            text=True,
            capture_output=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--legacy-preview", result.stderr)
```

- [ ] **Step 2: Run treatment tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_wiki_treatment -v
```

Expected: FAIL because raw scan still works without `--legacy-preview`.

- [ ] **Step 3: Add CLI argument and guards**

In `scripts/build_wiki_treatment.py`, add:

```python
    parser.add_argument(
        "--legacy-preview",
        action="store_true",
        help="Allow raw adjudication treatment preview without --case-file. Evidence only; not authoritative.",
    )
```

After `root = Path(args.root).resolve()`, add:

```python
    if args.apply and not args.case_file:
        parser.error("--apply requires --case-file")
    if not args.case_file and not args.legacy_preview:
        parser.error("raw treatment preview without --case-file requires --legacy-preview")
```

Update existing tests that intentionally run raw preview to pass `--legacy-preview`.

- [ ] **Step 4: Run treatment tests**

Run:

```bash
python3 -m unittest tests.test_wiki_treatment -v
```

Expected: PASS.

- [ ] **Step 5: Commit treatment authority guard**

Run:

```bash
git add scripts/build_wiki_treatment.py tests/test_wiki_treatment.py
git commit -m "fix: require case file for treatment apply"
```

## Task 7: Make Recovery Case-File Aware

**Files:**
- Modify: `scripts/wiki_recovery.py`
- Modify: `scripts/build_wiki_recovery.py`
- Modify: `tests/test_wiki_recovery.py`

- [ ] **Step 1: Add failing recovery case tests**

Append to `tests/test_wiki_recovery.py`:

```python
    def test_cli_updates_case_file_with_recovery_result(self) -> None:
        from scripts.wiki_medical_case import build_medical_case_package, load_medical_case_file, write_medical_case_file

        repo_root = Path(__file__).resolve().parents[1]
        case_package = build_medical_case_package(
            {
                "generated_at": "2026-05-15T01:02:03+00:00",
                "summary": {},
                "source_adjudication_summary": {},
                "accepted_candidates": [],
                "rejected_candidates": [],
                "deferred_items": [],
                "surgery_candidates": [],
                "openspec_required": [],
                "treatment_candidates": [],
            },
            case_slug="recovery-case",
        )
        case_package["status"] = "recovery_required"
        case_path = write_medical_case_file(
            case_package,
            self.tmpdir,
            output_dir=self.tmpdir / "cases",
            timestamp="2026-05-15T01:02:03+00:00",
        )
        record_dir = self.tmpdir / "recovery-records"

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_recovery.py",
                "--root",
                str(self.tmpdir),
                "--case-file",
                str(case_path),
                "--write-recovery-record",
                "--recovery-record-dir",
                str(record_dir),
                "--update-case-file",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)
        loaded = load_medical_case_file(case_path)

        self.assertIn("updated_case_file", payload)
        self.assertEqual(loaded["recovery"]["status"], "completed")
        self.assertIn(payload["recovery_record_path"], loaded["evidence_attachments"]["recovery"])
        self.assertIn(loaded["archive_next_action"]["next_action"], {"archive_ready", "blocked"})
```

- [ ] **Step 2: Run recovery tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_wiki_recovery -v
```

Expected: FAIL because `--case-file` and `--update-case-file` do not exist.

- [ ] **Step 3: Add case update support**

In `scripts/build_wiki_recovery.py`, import:

```python
from scripts.wiki_medical_case import attach_recovery_result_to_case, load_medical_case_file, overwrite_medical_case_file
```

Add args:

```python
    parser.add_argument("--case-file", help="Canonical wiki medical case file for authoritative recovery.")
    parser.add_argument("--update-case-file", action="store_true", help="Write recovery result back into --case-file.")
```

After writing the recovery record, add:

```python
    if args.update_case_file:
        if not args.case_file:
            parser.error("--update-case-file requires --case-file")
        case_package = load_medical_case_file(args.case_file)
        updated_case = attach_recovery_result_to_case(
            case_package,
            payload,
            recovery_record=payload.get("recovery_record_path"),
        )
        updated_path = overwrite_medical_case_file(args.case_file, updated_case, root)
        payload["updated_case_file"] = updated_path.as_posix()
```

- [ ] **Step 4: Run recovery tests**

Run:

```bash
python3 -m unittest tests.test_wiki_recovery -v
```

Expected: PASS.

- [ ] **Step 5: Commit recovery case support**

Run:

```bash
git add scripts/build_wiki_recovery.py scripts/wiki_recovery.py tests/test_wiki_recovery.py
git commit -m "feat: update wiki medical case from recovery"
```

## Task 8: Orchestrate Treatment Apply Plus Recovery In The Agent

**Files:**
- Modify: `scripts/wiki_medical_agent.py`
- Modify: `scripts/build_wiki_medical_agent.py`
- Modify: `tests/test_wiki_medical_agent.py`

- [ ] **Step 1: Add failing apply orchestration test**

Append to `tests/test_wiki_medical_agent.py`:

```python
    def test_cli_applies_confirmed_treatment_then_runs_recovery(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        target = self.tmpdir / "wiki" / "ops" / "safe.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# Safe\n", encoding="utf-8")
        case_path = self._write_case(self._case_package(status="ready_for_treatment"), "2026-05-15T01:02:03+00:00")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "apply 已确认的 1 个 treatment candidates",
                "--approved-detail",
                "detail-safe",
                "--apply",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(payload["intent"], "treatment_apply")
        self.assertEqual(payload["case_path"], case_path.as_posix())
        self.assertEqual(payload["applied"], 1)
        self.assertEqual(payload["recovery"]["status"], "completed")
        self.assertIn(payload["next_action"], {"archive_ready", "blocked"})
```

- [ ] **Step 2: Run agent tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent -v
```

Expected: FAIL because agent CLI does not support apply orchestration.

- [ ] **Step 3: Add orchestration helpers**

In `scripts/wiki_medical_agent.py`, import:

```python
from scripts.wiki_medical_case import attach_recovery_result_to_case, overwrite_medical_case_file
from scripts.wiki_recovery import build_recovery_package, write_recovery_record
from scripts.wiki_treatment import (
    apply_treatment_plan,
    load_case_and_build_treatment_plan,
    update_case_file_with_treatment_result,
    write_treatment_record,
)
```

Add:

```python
def apply_confirmed_treatment_and_recover(
    root: Path | str,
    case_path: Path | str,
    approved_domains: set[str] | None = None,
    approved_detail_refs: set[str] | None = None,
) -> dict[str, Any]:
    root_path = Path(root)
    plan = load_case_and_build_treatment_plan(
        case_path,
        approved_domains=approved_domains or set(),
        approved_detail_refs=approved_detail_refs or set(),
    )
    result = apply_treatment_plan(root_path, plan, apply=True)
    treatment_record = write_treatment_record(plan, result, root_path)
    update_case_file_with_treatment_result(
        case_path,
        plan,
        result,
        root_path,
        treatment_record=treatment_record.as_posix(),
    )
    recovery = build_recovery_package(root_path)
    recovery_record = write_recovery_record(recovery, root_path)
    case_package = load_medical_case_file(case_path)
    updated_case = attach_recovery_result_to_case(
        case_package,
        recovery,
        recovery_record=recovery_record.as_posix(),
    )
    overwrite_medical_case_file(case_path, updated_case, root_path)
    next_action = updated_case.get("archive_next_action", {}).get("next_action", "")
    return {
        "applied": result["summary"]["applied_count"],
        "blocked": result["summary"]["blocked_count"],
        "treatment_record": treatment_record.as_posix(),
        "recovery": {
            "status": updated_case["recovery"]["status"],
            "record": recovery_record.as_posix(),
            "passed": recovery.get("passed", False),
        },
        "next_action": next_action,
    }
```

In `scripts/build_wiki_medical_agent.py`, add args:

```python
    parser.add_argument("--approved-domain", action="append", default=[])
    parser.add_argument("--approved-detail", action="append", default=[])
    parser.add_argument("--apply", action="store_true")
```

Then after `payload = build_status_payload(...)`, add:

```python
    if payload["intent"] == "treatment_apply" and args.apply and payload.get("allowed"):
        from scripts.wiki_medical_agent import apply_confirmed_treatment_and_recover

        result = apply_confirmed_treatment_and_recover(
            Path(args.root).resolve(),
            payload["case_path"],
            approved_domains=set(args.approved_domain),
            approved_detail_refs=set(args.approved_detail),
        )
        payload.update(result)
```

- [ ] **Step 4: Run agent tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent -v
```

Expected: PASS.

- [ ] **Step 5: Commit orchestration**

Run:

```bash
git add scripts/wiki_medical_agent.py scripts/build_wiki_medical_agent.py tests/test_wiki_medical_agent.py
git commit -m "feat: orchestrate wiki treatment apply recovery"
```

## Task 9: Add The User-Facing Skill And Downgrade Stage Skills

**Files:**
- Create: `.codex/skills/wiki-medical-agent/SKILL.md`
- Modify: `.codex/skills/wiki-doctor/SKILL.md`
- Modify: `.codex/skills/wiki-confirm/SKILL.md`
- Modify: `.codex/skills/wiki-treatment/SKILL.md`
- Modify: `.codex/skills/wiki-surgery/SKILL.md`
- Modify: `.codex/skills/wiki-recovery/SKILL.md`
- Modify: `tests/test_wiki_medical_loop_skills.py`
- Create or modify: `openspec/changes/introduce-wiki-medical-agent-state-machine/evaluation.md`

- [ ] **Step 1: Add failing skill tests**

In `tests/test_wiki_medical_loop_skills.py`, add:

```python
    def test_wiki_medical_agent_is_normal_user_entry(self) -> None:
        text = self.read_skill("wiki-medical-agent")

        required_markers = [
            "name: wiki-medical-agent",
            "single normal user-facing entry point",
            "Intent",
            "Case",
            "State",
            "Allowed action",
            "Next Action",
            "scripts/build_wiki_medical_agent.py",
            "Confirmed Decisions",
            "Proposed Decisions",
        ]

        for marker in required_markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_stage_skills_redirect_ordinary_use_to_medical_agent(self) -> None:
        for skill_name in ["wiki-doctor", "wiki-confirm", "wiki-treatment", "wiki-surgery", "wiki-recovery"]:
            with self.subTest(skill=skill_name):
                text = self.read_skill(skill_name)
                self.assertIn("Ordinary use routes through `wiki-medical-agent`", text)
                self.assertIn("legacy/debug evidence only", text)
```

- [ ] **Step 2: Run skill tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_loop_skills -v
```

Expected: FAIL because the new skill and redirect wording are not present.

- [ ] **Step 3: Create the medical-agent skill**

Create `.codex/skills/wiki-medical-agent/SKILL.md`:

```markdown
---
name: wiki-medical-agent
description: Use as the single normal user-facing entry point for wiki medical-loop status, diagnosis, confirmation, treatment, surgery, recovery, and archive checks.
---

Use this skill as the single normal user-facing entry point for the LLM-WIKI
medical loop.

The agent must classify user intent before execution, resolve the active case
file, validate state, then route to the bounded worker.

Normal command:

```bash
python3 scripts/build_wiki_medical_agent.py --intent-text "<user request>"
```

Every response must show:

- Intent
- Case
- State
- Allowed action
- Blocked action, when blocked
- Next Action

Authority model:

- The case file is the only authority.
- `Confirmed Decisions` is the only executable decision surface.
- `Proposed Decisions` is not executable.
- Stage records are evidence attachments only.

Treatment apply:

- Requires one active case file.
- Requires executable confirmed treatment decisions.
- Requires explicit human approval via `--approved-domain` or
  `--approved-detail`.
- Must run recovery after apply.
- Must update the same case file with treatment and recovery evidence.

Boundaries:

- Do not auto-execute newly discovered candidates.
- Do not write relation fields.
- Do not mutate taxonomy config, MOC pages, ADRs, AGENTS, skills, or OpenSpec
  lifecycle state unless a separate approved workflow explicitly scopes it.
- Relation, governance, ADR, MOC, and OpenSpec-sensitive findings route to
  `surgery_required`, `awaiting_confirmation`, or `blocked`.
```

- [ ] **Step 4: Downgrade old stage skill wording**

At the top of each old stage skill after the intro paragraph, add:

```markdown
Ordinary use routes through `wiki-medical-agent`.

Use this stage skill directly only for explicit legacy/debug evidence. Direct
stage output is legacy/debug evidence only; it is not authoritative and does
not update case state unless routed through the medical agent and written back
to the active case file.
```

Keep existing stage-specific boundaries. Do not remove existing proof boundary wording unless it directly contradicts the new entry rule.

- [ ] **Step 5: Record behavior-asset evaluation**

Create `openspec/changes/introduce-wiki-medical-agent-state-machine/evaluation.md`:

```markdown
# Evaluation: wiki medical agent state machine

## Behavior Asset Change

This change creates `.codex/skills/wiki-medical-agent/SKILL.md` and changes
old stage skills to redirect ordinary usage to the medical agent.

## Pressure Scenarios

- User invokes `wiki-treatment apply 已确认的 10 个`.
- User invokes `wiki-recovery` after treatment.
- User invokes `wiki-doctor` for ordinary diagnosis.
- User explicitly asks for legacy/debug stage evidence.

## RED Baseline

Before this change, `tests/test_wiki_medical_loop_skills.py` did not find a
normal `wiki-medical-agent` entry or redirect wording in stage skills.

## GREEN Result

After this change, skill tests verify the new entry and redirect boundary.

## Residual Risks

Local skill text cannot prove every future agent will comply. Runtime CLI
guards and state-machine tests provide the stronger enforcement layer.
```

- [ ] **Step 6: Run skill tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_loop_skills -v
```

Expected: PASS.

- [ ] **Step 7: Run behavior asset checker**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected: PASS. If it returns an expected non-zero result due to existing unrelated dirty behavior assets, record the command, exit code, and unrelated blockers in `evaluation.md`.

- [ ] **Step 8: Commit skill routing**

Run:

```bash
git add .codex/skills/wiki-medical-agent/SKILL.md .codex/skills/wiki-doctor/SKILL.md .codex/skills/wiki-confirm/SKILL.md .codex/skills/wiki-treatment/SKILL.md .codex/skills/wiki-surgery/SKILL.md .codex/skills/wiki-recovery/SKILL.md tests/test_wiki_medical_loop_skills.py openspec/changes/introduce-wiki-medical-agent-state-machine/evaluation.md
git commit -m "feat: add wiki medical agent skill routing"
```

## Task 10: Add Behavior Replay And Full Verification

**Files:**
- Modify: `tests/test_wiki_medical_agent.py`
- Modify: `openspec/changes/introduce-wiki-medical-agent-state-machine/evaluation.md`
- Modify: `openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md`

- [ ] **Step 1: Add replay tests for blocked routes**

Append to `tests/test_wiki_medical_agent.py`:

```python
    def test_cli_blocks_apply_count_mismatch(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        case_path = self._write_case(self._case_package(status="ready_for_treatment"), "2026-05-15T01:02:03+00:00")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "apply 已确认的 10 个 treatment candidates",
                "--approved-detail",
                "detail-safe",
                "--apply",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(payload["case_path"], case_path.as_posix())
        self.assertFalse(payload["allowed"])
        self.assertEqual(payload["blocked_reason"], "confirmed_decision_count_mismatch")
        self.assertEqual(payload["expected_count"], 10)
        self.assertEqual(payload["executable_count"], 1)

    def test_cli_blocks_write_when_multiple_active_cases_exist(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:03+00:00")
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:04+00:00")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "apply 已确认的 1 个 treatment candidates",
                "--approved-detail",
                "detail-safe",
                "--apply",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertFalse(payload["allowed"])
        self.assertEqual(payload["blocked_reason"], "multiple_active_cases")
        self.assertEqual(payload["next_action"], "select_active_case")
```

- [ ] **Step 2: Run focused tests**

Run:

```bash
python3 -m unittest \
  tests.test_wiki_medical_agent \
  tests.test_wiki_medical_case \
  tests.test_wiki_treatment \
  tests.test_wiki_recovery \
  tests.test_wiki_medical_loop_skills \
  -v
```

Expected: PASS.

- [ ] **Step 3: Run OpenSpec validation**

Run:

```bash
openspec validate introduce-wiki-medical-agent-state-machine --strict
```

Expected: PASS.

- [ ] **Step 4: Run behavior asset checker**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected: PASS or documented unrelated non-zero result.

- [ ] **Step 5: Update evaluation evidence**

Append to `openspec/changes/introduce-wiki-medical-agent-state-machine/evaluation.md`:

```markdown
## Verification Commands

```text
python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_medical_case tests.test_wiki_treatment tests.test_wiki_recovery tests.test_wiki_medical_loop_skills -v
openspec validate introduce-wiki-medical-agent-state-machine --strict
python3 scripts/check_behavior_assets.py
```

## Replay Results

- Status request reports intent, case, state, allowed action, and next action.
- Apply request with matching confirmed count applies treatment, runs recovery,
  attaches records, and updates the case next action.
- Apply request with mismatched count is blocked.
- Multiple active cases block write actions.
- Old stage skills redirect ordinary usage to `wiki-medical-agent`.
```

- [ ] **Step 6: Mark OpenSpec tasks complete**

In `openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md`, check off completed tasks 1 through 11. Leave task 12 unchecked until after the final commit.

- [ ] **Step 7: Commit verification evidence**

Run:

```bash
git add tests/test_wiki_medical_agent.py openspec/changes/introduce-wiki-medical-agent-state-machine/evaluation.md openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md
git commit -m "test: verify wiki medical agent state machine"
```

## Task 11: Final OpenSpec Hard Stop Commit

**Files:**
- Modify: `openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md`

- [ ] **Step 1: Re-check git truth source**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected: only task-related files remain modified, or worktree has unrelated existing dirty files that are not staged.

- [ ] **Step 2: Mark task 12 complete**

Edit `openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md` and change:

```markdown
- [ ] 12. Commit verified implementation and stop at OpenSpec hard stop.
```

to:

```markdown
- [x] 12. Commit verified implementation and stop at OpenSpec hard stop.
```

- [ ] **Step 3: Commit the stop marker**

Run:

```bash
git add openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md
git commit -m "docs: complete wiki medical agent state machine tasks"
```

- [ ] **Step 4: Stop**

Do not archive, refactor, apply real wiki treatment, or continue adjacent automation. The next action after this task is archive review by a separate explicit request.
