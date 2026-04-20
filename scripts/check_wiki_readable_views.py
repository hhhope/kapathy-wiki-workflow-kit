#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_STRING_FIELDS = [
    "bundle_label",
    "timeline_view",
    "artifact_grouping_view",
    "relation_reading_view",
]

REQUIRED_LIST_FIELDS = [
    "required_indexes",
    "red_baseline",
    "green_result",
    "residual_risk",
]

REQUIRED_CHECKS = [
    "timeline_view_present",
    "artifact_grouping_present",
    "relation_reading_present",
    "index_links_present",
    "no_openspec_explore_mutation_claim",
]


def load_record(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("top-level JSON value must be an object")
    return data


def validate_shape(data: dict) -> list[str]:
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


def validate_paths(repo_root: Path, data: dict) -> list[str]:
    errors: list[str] = []

    file_fields = [
        "timeline_view",
        "artifact_grouping_view",
        "relation_reading_view",
    ]
    for field in file_fields:
        path = repo_root / data[field]
        if not path.exists():
            errors.append(f"missing required file: {data[field]}")

    for index_path in data["required_indexes"]:
        path = repo_root / index_path
        if not path.exists():
            errors.append(f"missing required index file: {index_path}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the bounded wiki-readable-views bundle.",
    )
    parser.add_argument("record", help="Path to a JSON validation record.")
    args = parser.parse_args()

    record_path = Path(args.record).resolve()
    if not record_path.exists():
        print(f"FAIL: record not found: {record_path}")
        return 1

    repo_root = Path(__file__).resolve().parent.parent

    try:
        data = load_record(record_path)
    except Exception as exc:
        print(f"FAIL: could not load validation record: {exc}")
        return 1

    errors = validate_shape(data)
    errors.extend(validate_paths(repo_root, data))

    if errors:
        print("FAIL: wiki readable views bundle is invalid:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: wiki readable views bundle satisfies the executable contract.")
    print(f"bundle_label: {data['bundle_label']}")
    print(f"timeline_view: {data['timeline_view']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
