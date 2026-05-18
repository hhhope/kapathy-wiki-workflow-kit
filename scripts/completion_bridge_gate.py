#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_STRING_FIELDS = [
    "thread_label",
    "delivery_result",
]

REQUIRED_LIST_FIELDS = [
    "red_baseline",
    "green_result",
    "residual_risk",
]

REQUIRED_CHECKS = [
    "delivery_result_present",
    "original_question_identified",
    "bridge_answer_present",
    "no_scope_continuation",
    "no_unearned_runtime_claim",
]

ALLOWED_NEXT_ACTIONS = {
    "archive_review",
    "new_openspec_proposal",
    "explicit_user_decision",
    "no_action",
    "report_status",
}


def load_record(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("top-level JSON value must be an object")
    return data


def _has_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_list_field(data: dict[str, Any], field: str, errors: list[str]) -> None:
    value = data.get(field)
    if not isinstance(value, list) or not value:
        errors.append(f"missing or empty list field: {field}")
        return
    if not all(_has_text(item) for item in value):
        errors.append(f"list field contains non-string or empty items: {field}")


def validate_record(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for field in REQUIRED_STRING_FIELDS:
        if not _has_text(data.get(field)):
            errors.append(f"missing or empty string field: {field}")

    for field in REQUIRED_LIST_FIELDS:
        _validate_list_field(data, field, errors)

    original_question_required = data.get("original_question_required")
    if not isinstance(original_question_required, bool):
        errors.append("missing boolean field: original_question_required")
    elif original_question_required:
        if not _has_text(data.get("original_question")):
            errors.append("missing original_question for required completion bridge")
        if not _has_text(data.get("bridge_answer")):
            errors.append("missing bridge_answer for required completion bridge")

    next_action = data.get("next_action")
    if not _has_text(next_action):
        errors.append("missing or empty string field: next_action")
    elif next_action not in ALLOWED_NEXT_ACTIONS:
        errors.append(f"invalid next_action: {next_action}")

    checks = data.get("checks")
    if not isinstance(checks, dict):
        errors.append("missing object field: checks")
        return errors

    for field in REQUIRED_CHECKS:
        value = checks.get(field)
        if not isinstance(value, bool):
            errors.append(f"missing boolean check: checks.{field}")
        elif value is not True:
            errors.append(f"required pass-condition failed: checks.{field}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a structured completion bridge replay record.",
    )
    parser.add_argument("record", help="Path to a JSON replay record.")
    args = parser.parse_args()

    path = Path(args.record).resolve()
    if not path.exists():
        print(f"FAIL: record not found: {path}")
        return 1

    try:
        data = load_record(path)
    except Exception as exc:
        print(f"FAIL: could not load replay record: {exc}")
        return 1

    errors = validate_record(data)
    if errors:
        print("FAIL: completion bridge replay record is invalid:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: completion bridge replay record satisfies the executable contract.")
    print(f"thread_label: {data['thread_label']}")
    print(f"next_action: {data['next_action']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
