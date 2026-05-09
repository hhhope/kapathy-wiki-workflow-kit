#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SELF_DIRECTED_EXECUTION_DERIVER = ROOT / "scripts" / "derive_self_directed_execution.py"


def run_json(command: list[str]) -> dict:
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    return json.loads(completed.stdout)


def load_execution(path: str | None) -> dict:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    return run_json([sys.executable, str(SELF_DIRECTED_EXECUTION_DERIVER)])


def source_paths(item: dict) -> list[str]:
    return [
        source["page_path"]
        for source in item.get("action_sources", [])
        if source.get("page_path")
    ]


def ready_item(item: dict) -> dict:
    return {
        "canonical_object": item["canonical_object"],
        "queue_state": "ready",
        "preview_action": item.get("action_type", "inspect_and_apply_context"),
        "source_paths": source_paths(item),
        "reasons": item.get("reasons", []),
        "caution_notes": [
            "Preview only; inspect sources before editing.",
            "No OpenSpec lifecycle mutation is allowed from this queue view.",
        ],
    }


def decision_item(item: dict) -> dict:
    return {
        "canonical_object": item["canonical_object"],
        "queue_state": "needs_user_decision",
        "preview_action": item.get("action_type", "inspect_before_followup"),
        "source_paths": source_paths(item),
        "reasons": item.get("reasons", []),
        "decision_needed": "Confirm whether this follow-up should become a separate OpenSpec change or remain deferred.",
    }


def blocked_item(item: dict) -> dict:
    return {
        "canonical_object": item["canonical_object"],
        "queue_state": "blocked",
        "preview_action": item.get("action_type", "blocked_from_first_pass_execution"),
        "source_paths": source_paths(item),
        "reasons": item.get("reasons", []),
        "blocker": "Do not execute from this object during first-pass wiki work.",
    }


def build_queue_preview(execution: dict) -> dict:
    ready = [ready_item(item) for item in execution.get("execute_now", [])]
    needs_user_decision = [
        decision_item(item) for item in execution.get("defer_for_followup", [])
    ]
    blocked = [blocked_item(item) for item in execution.get("do_not_execute", [])]
    source_summary = execution.get("summary", {})

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_execution_summary": source_summary,
        "summary": {
            "ready_count": len(ready),
            "needs_user_decision_count": len(needs_user_decision),
            "blocked_count": len(blocked),
            "caution_active": source_summary.get("caution_active", False),
            "direct_source_inspection_required": source_summary.get(
                "direct_source_inspection_required", True
            ),
        },
        "ready": ready,
        "needs_user_decision": needs_user_decision,
        "blocked": blocked,
        "proof_boundary_notes": [
            "This is a preview queue only.",
            "It does not create, modify, archive, or queue OpenSpec changes.",
            "It does not execute work or mark tasks complete.",
            "It does not replace direct source inspection.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execution", help="path to self-directed execution JSON")
    args = parser.parse_args()

    print(
        json.dumps(
            build_queue_preview(load_execution(args.execution)),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
