#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml

CONFIG_PATH = Path("wiki/config/behavior-asset-evaluation.yaml")
REPORT_JSON = Path("/tmp/behavior-asset-evaluation-report.json")
REPORT_MD = Path("/tmp/behavior-asset-evaluation-report.md")


@dataclass(frozen=True)
class BehaviorAssetEntry:
    kind: str
    severity: str
    path: str
    message: str


def load_config(repo_root: Path) -> dict[str, Any]:
    with (repo_root / CONFIG_PATH).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"config must be a mapping: {CONFIG_PATH}")
    return data


def severity(config: dict[str, Any], kind: str, default: str = "warn") -> str:
    return str(config.get("severity", {}).get(kind, default))


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def active_change_dirs(repo_root: Path) -> list[Path]:
    root = repo_root / "openspec/changes"
    if not root.exists():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir() and path.name != "archive")


def change_text(change_dir: Path) -> str:
    parts = []
    for path in sorted(change_dir.rglob("*.md")):
        if path.name == "evaluation.md":
            continue
        parts.append(read_text(path))
    return "\n".join(parts)


def change_is_behavior_asset_change(change_dir: Path, config: dict[str, Any]) -> bool:
    text = change_text(change_dir)
    markers = [str(value) for value in config.get("covered_change_markers", [])]
    return any(marker in text for marker in markers)


def change_is_grandfathered(change_dir: Path, repo_root: Path, config: dict[str, Any]) -> bool:
    change_rel = rel(change_dir, repo_root)
    grandfathered = {str(value).rstrip("/") for value in config.get("grandfathered_changes", [])}
    return change_rel in grandfathered


def check_evaluation(change_dir: Path, repo_root: Path, config: dict[str, Any]) -> list[BehaviorAssetEntry]:
    evaluation = change_dir / "evaluation.md"
    change_rel = rel(change_dir, repo_root)
    if not evaluation.exists():
        return [
            BehaviorAssetEntry(
                kind="missing_evaluation",
                severity=severity(config, "missing_evaluation", "error"),
                path=change_rel,
                message="Behavior-asset change requires evaluation.md.",
            )
        ]

    content = read_text(evaluation)
    entries: list[BehaviorAssetEntry] = []
    for section in config.get("required_sections", []):
        if str(section) not in content:
            entries.append(
                BehaviorAssetEntry(
                    kind="missing_required_section",
                    severity=severity(config, "missing_required_section", "error"),
                    path=rel(evaluation, repo_root),
                    message=f"Missing required evaluation section: {section}",
                )
            )

    lower = content.lower()
    if not any(str(marker).lower() in lower for marker in config.get("positive_markers", [])):
        entries.append(
            BehaviorAssetEntry(
                kind="missing_positive_scenario",
                severity=severity(config, "missing_positive_scenario", "error"),
                path=rel(evaluation, repo_root),
                message="Evaluation requires a positive trigger scenario.",
            )
        )

    if not any(str(marker).lower() in lower for marker in config.get("negative_markers", [])):
        entries.append(
            BehaviorAssetEntry(
                kind="missing_negative_scenario",
                severity=severity(config, "missing_negative_scenario", "error"),
                path=rel(evaluation, repo_root),
                message="Evaluation requires a negative or should-not-trigger scenario.",
            )
        )

    change_lower = change_text(change_dir).lower()
    parent_sensitive = any(
        marker in change_lower
        for marker in [
            "parent gate",
            "route",
            "publish",
            "sync",
            "reader-facing",
            "lightweight path",
            "full path",
        ]
    )
    if parent_sensitive and not any(str(marker).lower() in lower for marker in config.get("parent_gate_markers", [])):
        entries.append(
            BehaviorAssetEntry(
                kind="missing_parent_gate_preservation",
                severity=severity(config, "missing_parent_gate_preservation", "error"),
                path=rel(evaluation, repo_root),
                message="Parent-gate-sensitive behavior requires preservation evidence.",
            )
        )

    for field in config.get("required_replay_fields", []):
        if str(field).lower() not in lower:
            entries.append(
                BehaviorAssetEntry(
                    kind="weak_replay_evidence",
                    severity=severity(config, "weak_replay_evidence", "warn"),
                    path=rel(evaluation, repo_root),
                    message=f"Replay evidence does not mention: {field}",
                )
            )

    for marker in config.get("shallow_evidence_markers", []):
        if str(marker).lower() in lower:
            entries.append(
                BehaviorAssetEntry(
                    kind="shallow_text_evidence",
                    severity=severity(config, "shallow_text_evidence", "error"),
                    path=rel(evaluation, repo_root),
                    message=f"Evaluation relies on shallow evidence marker: {marker}",
                )
            )
    return entries


def section_between(text: str, start_heading: str, next_heading_prefix: str = "## ") -> str:
    start = text.find(start_heading)
    if start == -1:
        return ""
    next_start = text.find(next_heading_prefix, start + len(start_heading))
    if next_start == -1:
        return text[start:]
    return text[start:next_start]


def check_agent_intent_ownership(repo_root: Path, config: dict[str, Any]) -> list[BehaviorAssetEntry]:
    agents = repo_root / "AGENTS.md"
    if not agents.exists():
        return []
    text = read_text(agents)
    rules = config.get("ownership_rules", {}).get("agent_intent_routing", {})
    owner = str(rules.get("owner_section", "High-Frequency Skills"))
    section_name = str(rules.get("classification_section", "Agent Intent Routing"))
    if f"## {owner}" not in text or f"## {section_name}" not in text:
        return []

    section = section_between(text, f"## {section_name}")
    entries = []
    for marker in [str(value) for value in rules.get("forbidden_markers", [])]:
        if marker in section:
            entries.append(
                BehaviorAssetEntry(
                    kind="route_table_ownership_drift",
                    severity=severity(config, "route_table_ownership_drift", "error"),
                    path="AGENTS.md",
                    message=f"`{section_name}` duplicates route-table ownership via `{marker}`.",
                )
            )
    return entries


def check_behavior_assets(repo_root: Path | str) -> list[BehaviorAssetEntry]:
    root = Path(repo_root)
    config = load_config(root)
    entries: list[BehaviorAssetEntry] = []
    for change_dir in active_change_dirs(root):
        if change_is_grandfathered(change_dir, root, config):
            continue
        if change_is_behavior_asset_change(change_dir, config):
            entries.extend(check_evaluation(change_dir, root, config))
    entries.extend(check_agent_intent_ownership(root, config))
    return entries


def write_reports(entries: list[BehaviorAssetEntry]) -> None:
    REPORT_JSON.write_text(
        json.dumps([asdict(entry) for entry in entries], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    lines = ["# Behavior Asset Evaluation Report", ""]
    if not entries:
        lines.append("No behavior asset evaluation drift found.")
    else:
        for entry in entries:
            lines.append(f"- `{entry.severity}` `{entry.kind}` `{entry.path}`: {entry.message}")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check behavior asset evaluation evidence.")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    entries = check_behavior_assets(Path(args.repo_root).resolve())
    write_reports(entries)
    for entry in entries:
        print(f"{entry.severity.upper()} {entry.kind} {entry.path}: {entry.message}")
    return 1 if any(entry.severity == "error" for entry in entries) else 0


if __name__ == "__main__":
    sys.exit(main())
