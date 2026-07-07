from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from coverage_config import DEFAULT_SETTINGS, ordered_union


VALID_NA_REASONS = {"format_only", "generated", "vendor", "docs_only", "test_only"}
VALID_CR_TYPES = {"merge_cr", "release_cr", "hotfix_cr", "post_incident_cr", "db_cr", "config_cr"}
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|[\u4e00-\u9fff]+|\d+(?:\.\d+)?")
HUNK_RE = re.compile(r"@@ -(?P<old_start>\d+)(?:,\d+)? \+(?P<new_start>\d+)(?:,\d+)? @@")


def unit_id(prefix: str, payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return f"{prefix}-{hashlib.sha1(raw.encode()).hexdigest()[:12]}"


def _tokens(text: str) -> list[str]:
    seen: list[str] = []
    for token in TOKEN_RE.findall(text):
        low = token.lower()
        if low not in seen:
            seen.append(low)
    return seen


def parse_hunks(diff_text: str) -> list[dict[str, Any]]:
    units: list[dict[str, Any]] = []
    current_file = ""
    current: dict[str, Any] | None = None

    def finalize(prefix: str, unit: dict[str, Any]) -> dict[str, Any]:
        unit["content_hash"] = hashlib.sha256("\n".join(unit["lines"]).encode()).hexdigest()
        unit["status"] = "open"
        unit["id"] = unit_id(prefix, unit)
        return unit

    def finish_hunk() -> None:
        nonlocal current
        if current:
            units.append(finalize("hunk", current))
            current = None

    def add_special(kind: str, line: str) -> None:
        payload = {
            "unit_type": "special",
            "special_type": kind,
            "file_path": current_file,
            "lines": [line],
            "status": "open",
        }
        payload = finalize("special", payload)
        if payload["id"] not in {unit.get("id") for unit in units}:
            units.append(payload)

    for line in diff_text.splitlines():
        if line.startswith("diff --git "):
            finish_hunk()
            current_file = line.split()[-1][2:]
            file_unit = {
                "unit_type": "file",
                "file_path": current_file,
                "lines": [line],
                "status": "open",
            }
            units.append(finalize("file", file_unit))
            if _is_lockfile_or_generated(current_file):
                add_special("lockfile_or_generated", line)
            continue
        if line.startswith("rename from ") or line.startswith("rename to "):
            add_special("rename", line)
            continue
        if line.startswith("deleted file mode "):
            add_special("delete", line)
            continue
        if line.startswith("Binary files "):
            add_special("binary", line)
            continue
        match = HUNK_RE.match(line)
        if match:
            finish_hunk()
            current = {
                "unit_type": "hunk",
                "file_path": current_file,
                "old_start": int(match.group("old_start")),
                "new_start": int(match.group("new_start")),
                "lines": [],
            }
            continue
        if current and line and line[0] in "+-" and not line.startswith(("+++", "---")):
            current["lines"].append(line)
    finish_hunk()
    return units


def _is_lockfile_or_generated(path: str) -> bool:
    lowered = path.lower()
    return (
        lowered.endswith(".lock")
        or lowered.endswith("package-lock.json")
        or "/generated-sources/" in lowered
        or "/target/generated-sources/" in lowered
    )


def split_oversized(units: list[dict[str, Any]], threshold: int) -> list[dict[str, Any]]:
    expanded = list(units)
    for unit in units:
        if unit["unit_type"] != "hunk" or len(unit["lines"]) <= threshold:
            continue
        special = {
            "unit_type": "special",
            "special_type": "large_file",
            "file_path": unit["file_path"],
            "parent_id": unit["id"],
            "lines": [f"large hunk changed lines: {len(unit['lines'])}"],
            "status": "open",
        }
        special["content_hash"] = hashlib.sha256("\n".join(special["lines"]).encode()).hexdigest()
        special["id"] = unit_id("special", special)
        expanded.append(special)
        for index in range(0, len(unit["lines"]), threshold):
            child = {
                "unit_type": "child_hunk",
                "parent_id": unit["id"],
                "file_path": unit["file_path"],
                "child_index": index // threshold + 1,
                "lines": unit["lines"][index : index + threshold],
                "status": "open",
            }
            child["content_hash"] = hashlib.sha256("\n".join(child["lines"]).encode()).hexdigest()
            child["id"] = unit_id("child", child)
            expanded.append(child)
    return expanded


def extract_facts(units: list[dict[str, Any]]) -> list[dict[str, Any]]:
    facts = []
    for unit in units:
        text = unit.get("file_path", "") + "\n" + "\n".join(unit.get("lines", []))
        facts.append({"diff_unit_id": unit["id"], "tokens": _tokens(text), "text": text.lower()})
    return facts


def _match_rule(fact: dict[str, Any], rule: dict[str, Any]) -> bool:
    text = fact["text"]
    return any(str(term).lower() in text for term in rule.get("match", {}).get("any", []))


def checks_and_groups(units: list[dict[str, Any]], facts: list[dict[str, Any]], config: dict[str, Any]):
    checks: list[dict[str, Any]] = []
    groups: list[dict[str, Any]] = []
    matched_by_rule: dict[str, list[str]] = {}
    facts_by_unit = {fact["diff_unit_id"]: fact for fact in facts}
    for unit in units:
        matched = False
        for rule_id, rule in config.get("rules", {}).items():
            if _match_rule(facts_by_unit[unit["id"]], rule):
                matched = True
                matched_by_rule.setdefault(rule_id, []).append(unit["id"])
                for title in rule["create_checks"].get("required", []):
                    checks.append({
                        "id": unit_id("check", {"unit": unit["id"], "rule": rule_id, "title": title}),
                        "rule_id": rule_id,
                        "diff_unit_ids": [unit["id"]],
                        "title": title,
                        "required": True,
                        "status": "open",
                    })
        if not matched:
            checks.append({
                "id": unit_id("check", {"unit": unit["id"], "rule": "general_logic"}),
                "rule_id": "general_logic",
                "diff_unit_ids": [unit["id"]],
                "title": "General logic, failure path, and compatibility impact are reviewed",
                "required": True,
                "status": "open",
            })
    for rule_id, linked in matched_by_rule.items():
        if len(linked) > 1 or rule_id == "money":
            groups.append({
                "id": unit_id("group", {"rule": rule_id, "units": linked}),
                "rule_id": rule_id,
                "linked_diff_units": linked,
                "checks": [check["id"] for check in checks if check["rule_id"] == rule_id],
                "status": "open",
            })
    groups.extend(_shared_signal_groups(facts))
    return checks, groups


def _shared_signal_groups(facts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ignored = {"return", "public", "class", "string", "bigdecimal", "old", "new", "src", "java"}
    by_token: dict[str, list[str]] = {}
    for fact in facts:
        for token in fact.get("tokens", []):
            if len(token) < 4 or token in ignored:
                continue
            by_token.setdefault(token, []).append(fact["diff_unit_id"])
    groups = []
    for token, linked in sorted(by_token.items()):
        unique = ordered_union([], linked)
        if len(unique) < 2:
            continue
        groups.append({
            "id": unit_id("group", {"signal": token, "units": unique}),
            "group_type": "shared_signal",
            "signal": token,
            "linked_diff_units": unique,
            "checks": [],
            "status": "open",
        })
    return groups


def evaluate_gate(range_metadata: dict[str, Any], units: list[dict[str, Any]], checks: list[dict[str, Any]],
                  checker_results: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    reasons: list[str] = []
    required_range = ["cr_type", "base", "head", "merge_base", "range_hash", "config_hash", "agent_version"]
    if any(not range_metadata.get(key) for key in required_range):
        reasons.append("missing or ambiguous range")
    if range_metadata.get("cr_type") and range_metadata.get("cr_type") not in VALID_CR_TYPES:
        reasons.append("invalid CR type")
    if range_metadata.get("range_stale") or range_metadata.get("stale"):
        reasons.append("stale range")
    if any(unit.get("status") == "open" for unit in units):
        reasons.append("open diff unit")
    if any(check.get("required") and check.get("status") in {"open", "blocked"} for check in checks):
        reasons.append("open required check")
    for result in checker_results or []:
        if result.get("status") == "not_applicable" and (result.get("na_reason") not in VALID_NA_REASONS or not result.get("evidence_refs")):
            reasons.append("invalid N/A")
        if result.get("status") == "issue" and result.get("risk") == "high":
            reasons.append("high issue")
        if result.get("risk") == "high" and result.get("unresolved_questions"):
            reasons.append("high-risk unresolved question")
        if result.get("status") == "blocked":
            reasons.append("blocked check")
    return {"decision": "blocked" if reasons else "allow", "reasons": ordered_union([], reasons)}


def analyze_diff_text(diff_text: str, config: dict[str, Any], range_metadata: dict[str, Any]) -> dict[str, Any]:
    threshold = int(config.get("settings", DEFAULT_SETTINGS)["oversized_hunk_line_threshold"])
    units = split_oversized(parse_hunks(diff_text), threshold)
    facts = extract_facts(units)
    checks, groups = checks_and_groups(units, facts, config)
    gate = evaluate_gate(range_metadata, units, checks)
    return {
        "state": {"stage": "gate", "coverage_counters": {
            "diff_units_total": len(units),
            "diff_units_closed": sum(1 for unit in units if unit.get("status") != "open"),
            "checks_total": len(checks),
            "checks_closed": sum(1 for check in checks if check.get("status") != "open"),
        }},
        "diff_units": units,
        "facts": facts,
        "review_groups": groups,
        "checks": checks,
        "checker_results": [],
        "issues": [],
        "gate": gate,
    }


def write_case_artifacts(case_dir: Path, result: dict[str, Any]) -> None:
    case_dir.mkdir(parents=True, exist_ok=True)
    (case_dir / "state.json").write_text(json.dumps(result["state"], ensure_ascii=False, indent=2), encoding="utf-8")
    for key, name in [
        ("diff_units", "diff-units.jsonl"),
        ("facts", "facts.jsonl"),
        ("review_groups", "review-groups.jsonl"),
        ("checks", "checks.jsonl"),
        ("checker_results", "checker-results.jsonl"),
        ("issues", "issues.jsonl"),
    ]:
        rows = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in result[key])
        (case_dir / name).write_text(rows, encoding="utf-8")
    (case_dir / "gate.json").write_text(json.dumps(result["gate"], ensure_ascii=False, indent=2), encoding="utf-8")
    (case_dir / "report.md").write_text(
        f"# CR Coverage Gate\n\nDecision: `{result['gate']['decision']}`\n",
        encoding="utf-8",
    )
