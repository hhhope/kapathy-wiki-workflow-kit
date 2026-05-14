#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.wiki_content_adjudication import build_adjudication_package
from scripts.wiki_doctor_review_records import write_review_record


def main() -> None:
    parser = argparse.ArgumentParser(description="Build wiki content adjudication review package.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument(
        "--write-review-record",
        action="store_true",
        help="Write a wiki-doctor Markdown review record. Default behavior is stdout JSON only.",
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
    payload["candidate_set"] = payload["candidate_set"][:limit]
    payload["full_detail_set"] = payload["full_detail_set"][:limit]
    payload["agent_judgment_set"] = payload["agent_judgment_set"][:limit]
    payload["review_focus_set"] = payload["review_focus_set"][:limit]
    payload["drift_trace_set"] = payload["drift_trace_set"][:limit]
    if args.write_review_record:
        record_path = write_review_record(
            payload,
            root,
            output_dir=Path(args.review_record_dir).resolve() if args.review_record_dir else None,
            limit=limit,
        )
        payload["review_record_path"] = record_path.as_posix()
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
