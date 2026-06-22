#!/usr/bin/env python3
import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = {
    "id",
    "input_situation",
    "triggered_workers",
    "expected_issues",
    "expected_gate",
    "proof_boundary",
    "residual_risk",
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
    if not isinstance(data.get("expected_issues"), list) or not data.get("expected_issues"):
        errors.append(f"{path}: expected_issues must be a non-empty list")
    if data.get("expected_gate") not in {"allow", "conditional", "blocked"}:
        errors.append(f"{path}: expected_gate must be allow, conditional, or blocked")
    for index, issue in enumerate(data.get("expected_issues", []), 1):
        if not isinstance(issue, dict):
            errors.append(f"{path}: expected_issues[{index}] must be an object")
            continue
        for key in ["source_worker", "title", "blocking"]:
            if key not in issue:
                errors.append(f"{path}: expected_issues[{index}] missing {key}")
        if "blocking" in issue and not isinstance(issue["blocking"], bool):
            errors.append(f"{path}: expected_issues[{index}] blocking must be boolean")
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
