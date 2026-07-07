#!/usr/bin/env python3
"""CLI and compatibility API for the CR-agent coverage gate."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

from coverage_config import ConfigError, LoadedConfig, load_rule_config
from coverage_model import analyze_diff_text, evaluate_gate, write_case_artifacts as _write_case_artifacts
from coverage_results import (
    apply_confirmed_issues,
    apply_checker_results,
    blocked_case_result,
    invalidate_stale_checker_results,
    manual_checker_fallback,
    render_formal_report,
    render_report,
    run_money_unit_checker,
)

__all__ = [
    "ConfigError",
    "LoadedConfig",
    "analyze_diff_text",
    "evaluate_gate",
    "load_rule_config",
    "apply_checker_results",
    "apply_confirmed_issues",
    "blocked_case_result",
    "invalidate_stale_checker_results",
    "manual_checker_fallback",
    "render_formal_report",
    "render_report",
    "run_money_unit_checker",
    "read_case_artifacts",
    "write_case_artifacts",
]


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def read_case_artifacts(case_dir: Path) -> dict:
    return {
        "state": json.loads((case_dir / "state.json").read_text(encoding="utf-8")),
        "diff_units": _read_jsonl(case_dir / "diff-units.jsonl"),
        "facts": _read_jsonl(case_dir / "facts.jsonl"),
        "review_groups": _read_jsonl(case_dir / "review-groups.jsonl"),
        "checks": _read_jsonl(case_dir / "checks.jsonl"),
        "checker_results": _read_jsonl(case_dir / "checker-results.jsonl"),
        "issues": _read_jsonl(case_dir / "issues.jsonl"),
        "gate": json.loads((case_dir / "gate.json").read_text(encoding="utf-8")),
    }


def write_case_artifacts(case_dir: Path, result: dict) -> None:
    _write_case_artifacts(case_dir, result)
    (case_dir / "report.md").write_text(render_report(result), encoding="utf-8")


def _range_metadata(repo: Path, base: str, head: str, cr_type: str, config_hash: str, diff_text: str) -> dict[str, str]:
    merge_base = subprocess.check_output(
        ["git", "-C", str(repo), "merge-base", base, head],
        text=True,
    ).strip()
    return {
        "cr_type": cr_type,
        "base": base,
        "head": head,
        "merge_base": merge_base,
        "range_hash": hashlib.sha256(diff_text.encode()).hexdigest(),
        "config_hash": config_hash,
        "agent_version": "coverage-gate-v1",
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--cr-type", default="merge_cr")
    parser.add_argument("--skill-dir", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args(argv)

    repo = Path(args.repo)
    loaded = load_rule_config(Path(args.skill_dir), repo, args.project, args.case_id)
    diff_text = subprocess.check_output(["git", "-C", str(repo), "diff", f"{args.base}..{args.head}"], text=True)
    range_metadata = _range_metadata(repo, args.base, args.head, args.cr_type, loaded.config_hash, diff_text)
    result = analyze_diff_text(diff_text, loaded.config, range_metadata)
    result["state"].update({
        "stage": "gate",
        "current_diff_unit_cursor": None,
        "current_check_cursor": None,
        **range_metadata,
        "config_sources": loaded.sources,
        "diff_ledger_hash": hashlib.sha256(json.dumps(result["diff_units"], sort_keys=True).encode()).hexdigest(),
    })
    write_case_artifacts(repo / "CR" / args.project / "cases" / args.case_id, result)
    print(json.dumps(result["gate"], ensure_ascii=False))
    return 3 if result["gate"]["decision"] == "blocked" else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
