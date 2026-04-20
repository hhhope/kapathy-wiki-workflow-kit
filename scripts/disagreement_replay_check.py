#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_LIST_FIELDS = [
    "rejected_framing",
    "correction_pressure",
    "red_baseline",
    "green_result",
    "residual_risk",
]

REQUIRED_STRING_FIELDS = [
    "thread_label",
    "disagreement_shape",
    "redirection_moment",
    "clarity_state",
    "protected_target",
]

REQUIRED_CHECKS = [
    "evolution_over_endpoint",
    "no_premature_abstraction",
    "unclear_state_allowed",
    "no_rollout_claim",
]


def load_record(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("top-level JSON value must be an object")
    return data


def validate_record(data: dict) -> list[str]:
    errors: list[str] = []

    for field in REQUIRED_STRING_FIELDS:
        value = data.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"missing or empty string field: {field}")

    for field in REQUIRED_LIST_FIELDS:
        value = data.get(field)
        if not isinstance(value, list) or not value:
            errors.append(f"missing or empty list field: {field}")
            continue
        if not all(isinstance(item, str) and item.strip() for item in value):
            errors.append(f"list field contains non-string or empty items: {field}")

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
        description="Validate a structured disagreement replay record.",
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
        print("FAIL: replay record is invalid:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: replay record satisfies the executable disagreement replay contract.")
    print(f"thread_label: {data['thread_label']}")
    print(f"disagreement_shape: {data['disagreement_shape']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
