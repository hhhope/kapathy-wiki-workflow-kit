#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PRESSURE = ROOT / "pressure"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    oracle_rows = {row["id"]: row for row in load_json(PRESSURE / "weekly-review-logs.json")}
    blind_rows = {row["id"]: row for row in load_json(PRESSURE / "blind-weekly-review-decisions.json")}

    total = len(oracle_rows)
    decision_matches = 0
    type_matches = 0
    exact_matches = 0
    rows = []

    for log_id, oracle in oracle_rows.items():
        blind = blind_rows[log_id]
        oracle_decision = "absorb" if oracle["accepted"] else "discard"
        blind_decision = blind["decision"]
        decision_match = oracle_decision == blind_decision
        type_match = oracle["destination_type"] == blind["destination_type"]
        exact_match = oracle["destination_path"] == blind["destination_path"]
        if decision_match:
            decision_matches += 1
        if type_match:
            type_matches += 1
        if exact_match:
            exact_matches += 1
        rows.append(
            {
                "id": log_id,
                "oracle_decision": oracle_decision,
                "blind_decision": blind_decision,
                "oracle_type": oracle["destination_type"],
                "blind_type": blind["destination_type"],
                "oracle_path": oracle["destination_path"],
                "blind_path": blind["destination_path"],
                "decision_match": decision_match,
                "type_match": type_match,
                "exact_match": exact_match,
            }
        )

    lines = []
    lines.append("# Lore Blind Weekly Review")
    lines.append("")
    lines.append("Date: 2026-04-13")
    lines.append("Branch: `feat-lore-wiki-openspec`")
    lines.append("")
    lines.append("This file records a blind-style weekly-review run: destination decisions were written from the log text corpus first, then compared against the oracle mapping.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Result |")
    lines.append("|---|---:|")
    lines.append(f"| Decision accuracy | `{decision_matches}/{total} = {decision_matches/total:.0%}` |")
    lines.append(f"| Destination-type accuracy | `{type_matches}/{total} = {type_matches/total:.0%}` |")
    lines.append(f"| Exact destination accuracy | `{exact_matches}/{total} = {exact_matches/total:.0%}` |")
    lines.append("")
    lines.append("## Per-log comparison")
    lines.append("")
    lines.append("| Log | Oracle decision | Blind decision | Oracle type | Blind type | Exact destination match |")
    lines.append("|---|---|---|---|---|---|")
    for row in rows:
        lines.append(
            f"| `{row['id']}` | {row['oracle_decision']} | {row['blind_decision']} | {row['oracle_type']} | {row['blind_type']} | {'Pass' if row['exact_match'] else 'Fail'} |"
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- This is stronger than a pure scripted metrics pass because the weekly-review decisions were first written as blind judgments from log text.")
    lines.append("- It is still not a blind external evaluator or multi-session live-agent review with fresh context.")
    lines.append("")
    (ROOT / "BLIND-WEEKLY-REVIEW.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "decision_accuracy": decision_matches / total,
        "type_accuracy": type_matches / total,
        "exact_destination_accuracy": exact_matches / total,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
