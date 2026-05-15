#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.wiki_content_adjudication import build_adjudication_package
from scripts.wiki_doctor_review_records import write_review_record


def _apply_limit(payload: dict, limit: int) -> None:
    bounded = max(0, limit)
    payload["candidate_set"] = payload["candidate_set"][:bounded]
    payload["full_detail_set"] = payload["full_detail_set"][:bounded]
    payload["agent_judgment_set"] = payload["agent_judgment_set"][:bounded]
    payload["review_focus_set"] = payload["review_focus_set"][:bounded]
    payload["drift_trace_set"] = payload["drift_trace_set"][:bounded]


def _summary_payload(payload: dict, record_path: Path, limit: int) -> dict:
    eval_result = payload.get("eval_result", {})
    if not isinstance(eval_result, dict):
        eval_result = {}
    return {
        "generated_at": payload.get("generated_at"),
        "mode": "review_package_summary",
        "review_record_path": record_path.as_posix(),
        "preview_limit": max(0, limit),
        "summary": payload.get("summary", {}),
        "eval_result": {
            "passed": eval_result.get("passed"),
            "error_count": len(eval_result.get("errors", [])) if isinstance(eval_result.get("errors", []), list) else 0,
            "warning_count": len(eval_result.get("warnings", [])) if isinstance(eval_result.get("warnings", []), list) else 0,
        },
        "proof_boundary_notes": payload.get("proof_boundary_notes", []),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build wiki content adjudication review package.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument(
        "--write-review-record",
        action="store_true",
        help="Compatibility flag. Default behavior already writes a wiki-doctor Markdown diagnosis record.",
    )
    parser.add_argument(
        "--stdout-json-only",
        action="store_true",
        help="Emit the JSON review package only and do not write a diagnosis record.",
    )
    parser.add_argument(
        "--review-record-dir",
        help="Directory for --write-review-record output. Defaults to wiki/ops/wiki-doctor-runs under --root.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    payload = build_adjudication_package(root)
    payload["generated_at"] = datetime.now(timezone.utc).isoformat()
    payload["mode"] = "review_package"
    limit = max(0, args.limit)
    if args.stdout_json_only:
        preview_payload = copy.deepcopy(payload)
        _apply_limit(preview_payload, limit)
        print(json.dumps(preview_payload, ensure_ascii=False, indent=2))
        return

    record_path = write_review_record(
        payload,
        root,
        output_dir=Path(args.review_record_dir).resolve() if args.review_record_dir else None,
        limit=None,
    )
    print(json.dumps(_summary_payload(payload, record_path, limit), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
