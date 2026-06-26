#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

COMMON_REQUIRED = (
    "learning_level",
    "learning_type",
    "methods_used",
    "input_inventory",
    "evidence_matrix",
    "value_judgment",
    "proof_boundary",
)

L3_REQUIRED = (
    "research_reconstruction_model",
    "output_transformation_plan",
)


def load_record(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return {}
    return data


def check_learning_record(path: Path) -> list[str]:
    record = load_record(path)
    messages: list[str] = []

    for field in COMMON_REQUIRED:
        if not record.get(field):
            messages.append(f"missing required field: {field}")

    level = str(record.get("learning_level", "")).upper()
    if level == "L3":
        for field in L3_REQUIRED:
            if not record.get(field):
                messages.append(f"missing required field: {field}")

    evidence = record.get("evidence_matrix")
    if evidence is not None and not isinstance(evidence, list):
        messages.append("evidence_matrix must be a list")

    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a structured L2/L3 learning record.")
    parser.add_argument("path", help="YAML learning record path")
    args = parser.parse_args()

    messages = check_learning_record(Path(args.path))
    for message in messages:
        print(message)
    return 1 if messages else 0


if __name__ == "__main__":
    sys.exit(main())
