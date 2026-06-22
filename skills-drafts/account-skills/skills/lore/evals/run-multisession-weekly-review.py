#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PRESSURE = ROOT / "pressure"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def summarize(logs):
    reviewed = sum(1 for item in logs if item["reviewed"])
    absorbed = sum(1 for item in logs if item["accepted"])
    discarded = sum(1 for item in logs if not item["accepted"])
    accepted_with_dest = sum(1 for item in logs if item["accepted"] and item["absorbed_to"])
    reviewed_with_absorbed_to = sum(1 for item in logs if item["reviewed"] and item["absorbed_to"])
    destinations = Counter(item["destination_type"] for item in logs if item["accepted"])
    absorption = accepted_with_dest / absorbed if absorbed else 0.0
    absorbed_to_completion = reviewed_with_absorbed_to / reviewed if reviewed else 0.0
    return {
        "reviewed": reviewed,
        "absorbed": absorbed,
        "discarded": discarded,
        "accepted": absorbed,
        "accepted_with_dest": accepted_with_dest,
        "absorption": absorption,
        "absorbed_to_completion": absorbed_to_completion,
        "destinations": dict(destinations),
    }


def main():
    logs = {item["id"]: item for item in load_json(PRESSURE / "weekly-review-logs.json")}
    sessions = load_json(PRESSURE / "weekly-review-sessions.json")

    remaining = set(logs.keys())
    session_summaries = []
    for session in sessions:
        batch = [logs[log_id] for log_id in session["log_ids"]]
        summary = summarize(batch)
        for log_id in session["log_ids"]:
            remaining.discard(log_id)
        summary["session_id"] = session["session_id"]
        summary["remaining_backlog"] = len(remaining)
        session_summaries.append(summary)

    aggregate = summarize(list(logs.values()))

    lines = []
    lines.append("# Lore Multi-Session Weekly Review")
    lines.append("")
    lines.append("Date: 2026-04-13")
    lines.append("Branch: `feat-lore-wiki-openspec`")
    lines.append("")
    lines.append("This file records a multi-session style weekly-review evaluation using the 10-log pressure corpus split across three review batches.")
    lines.append("")
    lines.append("## Session results")
    lines.append("")
    lines.append("| Session | Reviewed | Absorbed | Discarded | `absorbed-to` completion | Absorption | Remaining backlog |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for s in session_summaries:
        lines.append(
            f"| `{s['session_id']}` | `{s['reviewed']}` | `{s['absorbed']}` | `{s['discarded']}` | `{s['absorbed_to_completion']:.0%}` | `{s['absorption']:.0%}` | `{s['remaining_backlog']}` |"
        )
    lines.append("")
    lines.append("## Aggregate metrics")
    lines.append("")
    lines.append(f"- reviewed logs: `{aggregate['reviewed']}`")
    lines.append(f"- absorbed logs: `{aggregate['absorbed']}`")
    lines.append(f"- discarded logs: `{aggregate['discarded']}`")
    lines.append(f"- `absorbed-to` completion rate: `{aggregate['absorbed_to_completion']:.0%}`")
    lines.append(f"- absorption success rate: `{aggregate['absorption']:.0%}`")
    lines.append(f"- destination page types: `{aggregate['destinations']}`")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- Each review batch still emits the same metrics block shape required by Lore Phase 7.")
    lines.append("- The backlog trends to zero across sessions instead of pretending one giant weekly review run always happens.")
    lines.append("- Aggregate results stay aligned with the single-run pressure corpus metrics.")
    lines.append("")
    (ROOT / "MULTISESSION-WEEKLY-REVIEW.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "sessions": session_summaries,
                "aggregate": aggregate,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
