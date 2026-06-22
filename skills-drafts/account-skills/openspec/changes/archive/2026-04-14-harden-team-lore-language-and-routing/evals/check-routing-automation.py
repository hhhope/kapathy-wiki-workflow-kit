#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CHANGE_ROOT = ROOT.parent
REPO = CHANGE_ROOT.parents[2]


def run(cmd: list[str]) -> str:
    result = subprocess.run(
        cmd,
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def load_cases() -> list[dict]:
    return json.loads((ROOT / "routing-cases.json").read_text(encoding="utf-8"))


def check_case(case: dict) -> dict:
    route = case["expected_route"]
    surfaces = case["expected_surface"]
    passed = True
    details: dict[str, object] = {}

    if route[0] == "openspec":
        raw = run(["openspec", "status", "--change", "harden-team-lore-language-and-routing", "--json"])
        details["openspec_hit"] = "harden-team-lore-language-and-routing" in raw
        passed = passed and bool(details["openspec_hit"])

    if "lore" in route:
        for rel in surfaces.get("lore", []):
            exists = (CHANGE_ROOT / rel).exists()
            details[f"lore:{rel}"] = exists
            passed = passed and exists

    if "graphify" in route:
        query = case.get("graphify_query")
        raw = run(["graphify", "query", query]) if query else ""
        markers = case.get("graphify_markers", [])
        marker_ok = all(marker in raw for marker in markers)
        details["graphify_markers"] = marker_ok
        passed = passed and marker_ok

    return {
        "id": case["id"],
        "expected_route": route,
        "pass": passed,
        "details": details,
    }


def main() -> int:
    cases = load_cases()
    results = [check_case(case) for case in cases]
    summary = {"all_pass": all(item["pass"] for item in results), "results": results}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
