#!/usr/bin/env python3
import json
import sys
import tempfile
from pathlib import Path

from coverage_config import DEFAULT_SETTINGS
from coverage_model import analyze_diff_text
from coverage_results import apply_checker_results, render_formal_report, run_money_unit_checker

REQUIRED_TOP_LEVEL = {
    "id",
    "input_situation",
    "triggered_workers",
    "expected_issues",
    "expected_gate",
    "proof_boundary",
    "residual_risk",
}

COVERAGE_TOP_LEVEL = {
    "input_diff_text",
    "expected_checks",
}


def validate(path: Path) -> list[str]:
    errors = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        return [f"{path}: cannot read fixture: {exc}"]
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return [f"{path}: fixture root must be an object"]
    missing = sorted(REQUIRED_TOP_LEVEL - set(data))
    if missing:
        errors.append(f"{path}: missing top-level fields: {', '.join(missing)}")
    if not isinstance(data.get("triggered_workers"), list) or not data.get("triggered_workers"):
        errors.append(f"{path}: triggered_workers must be a non-empty list")
    if data.get("expected_gate") not in {"allow", "conditional", "blocked"}:
        errors.append(f"{path}: expected_gate must be allow, conditional, or blocked")
    if not isinstance(data.get("expected_issues"), list):
        errors.append(f"{path}: expected_issues must be a list")
    elif data.get("expected_gate") != "allow" and not data.get("expected_issues"):
        errors.append(f"{path}: expected_issues must be non-empty unless expected_gate is allow")
    for index, issue in enumerate(data.get("expected_issues", []), 1):
        if not isinstance(issue, dict):
            errors.append(f"{path}: expected_issues[{index}] must be an object")
            continue
        for key in ["source_worker", "title", "blocking"]:
            if key not in issue:
                errors.append(f"{path}: expected_issues[{index}] missing {key}")
        if "blocking" in issue and not isinstance(issue["blocking"], bool):
            errors.append(f"{path}: expected_issues[{index}] blocking must be boolean")
    if COVERAGE_TOP_LEVEL <= set(data):
        errors.extend(validate_coverage_fixture(path, data))
    return errors


def validate_coverage_fixture(path: Path, data: dict) -> list[str]:
    errors = []
    config = data.get("coverage_config") or {}
    if "rules" not in config:
        errors.append(f"{path}: coverage_config.rules is required for executable coverage replay")
        return errors
    config.setdefault("settings", dict(DEFAULT_SETTINGS))
    result = analyze_diff_text(
        data["input_diff_text"],
        config,
        {
            "cr_type": "merge_cr",
            "base": "fixture-base",
            "head": "fixture-head",
            "merge_base": "fixture-base",
            "range_hash": "fixture-range",
            "config_hash": "fixture-config",
            "agent_version": "fixture",
        },
    )
    if result["gate"]["decision"] != data["expected_gate"]:
        errors.append(
            f"{path}: expected_gate {data['expected_gate']} but coverage gate returned {result['gate']['decision']}"
        )
    actual_titles = {check["title"] for check in result["checks"]}
    for expected in data.get("expected_checks", []):
        if expected not in actual_titles:
            errors.append(f"{path}: expected check not created: {expected}")
    if "expected_money_checker_status" in data:
        checker_results = run_money_unit_checker(
            result,
            data.get("money_checker_consumer_evidence", []),
        )
        if not checker_results:
            errors.append(f"{path}: money checker did not produce results")
        for checker_result in checker_results:
            if checker_result.get("status") != data["expected_money_checker_status"]:
                errors.append(
                    f"{path}: expected money checker status {data['expected_money_checker_status']} "
                    f"but got {checker_result.get('status')}"
                )
        question_term = data.get("expected_money_checker_question_contains")
        if question_term and not any(
            question_term in question
            for checker_result in checker_results
            for question in checker_result.get("unresolved_questions", [])
        ):
            errors.append(f"{path}: money checker unresolved questions did not mention {question_term}")
        updated = apply_checker_results(result, checker_results)
        issue_titles = {issue.get("title") for issue in updated.get("issues", [])}
        for expected_issue in data.get("expected_issues", []):
            if expected_issue.get("source_worker") == "coverage_gate" and expected_issue.get("title") not in issue_titles:
                errors.append(f"{path}: expected coverage issue not created: {expected_issue.get('title')}")
    if "formal_report" in data:
        errors.extend(validate_formal_report_fixture(path, data["formal_report"], result))
    return errors


def validate_formal_report_fixture(path: Path, formal_report: dict, result: dict) -> list[str]:
    errors = []
    if not isinstance(formal_report, dict):
        return [f"{path}: formal_report must be an object"]
    required = {"project", "report_target", "report_profile"}
    missing = sorted(required - set(formal_report))
    if missing:
        return [f"{path}: formal_report missing fields: {', '.join(missing)}"]

    reference_report_path = None
    with tempfile.TemporaryDirectory() as raw:
        if "reference_report_text" in formal_report:
            reference = Path(raw) / "reference-report.md"
            reference.write_text(formal_report["reference_report_text"], encoding="utf-8")
            reference_report_path = str(reference)
        report = render_formal_report(
            result,
            project=formal_report["project"],
            report_target=formal_report["report_target"],
            report_profile=formal_report["report_profile"],
            case_report_path=formal_report.get("case_report_path"),
            reference_report_path=reference_report_path,
        )

    expected_start = formal_report.get("expected_starts_with")
    if expected_start and not report.startswith(expected_start):
        errors.append(f"{path}: formal report did not start with expected text")
    for expected in formal_report.get("expected_contains", []):
        if expected not in report:
            errors.append(f"{path}: expected formal report text not found: {expected}")
    for forbidden in formal_report.get("expected_not_contains", []):
        if forbidden in report:
            errors.append(f"{path}: forbidden formal report text found: {forbidden}")
    return errors


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: eval_cr_replay.py <fixture.json> [...]", file=sys.stderr)
        return 2
    errors = []
    for raw in argv:
        errors.extend(validate(Path(raw)))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"validated {len(argv)} replay fixture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
