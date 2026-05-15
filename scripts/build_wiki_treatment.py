#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.wiki_content_adjudication import build_adjudication_package
from scripts.wiki_treatment import (
    apply_treatment_plan,
    build_treatment_plan,
    write_treatment_record,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build or apply wiki treatment plan.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--approved-domain", action="append", default=[])
    parser.add_argument("--approved-detail", action="append", default=[])
    parser.add_argument("--apply", action="store_true", help="Apply approved frontmatter treatment.")
    parser.add_argument(
        "--write-treatment-record",
        action="store_true",
        help="Write Markdown treatment record. Default behavior is stdout JSON only.",
    )
    parser.add_argument(
        "--treatment-record-dir",
        help="Directory for --write-treatment-record output. Defaults to wiki/ops/wiki-treatment-runs under --root.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    adjudication_package = build_adjudication_package(root)
    plan = build_treatment_plan(
        adjudication_package,
        approved_domains=set(args.approved_domain),
        approved_detail_refs=set(args.approved_detail),
    )
    result = apply_treatment_plan(root, plan, apply=args.apply)
    payload = {"applied": args.apply, "plan": plan, "result": result}

    if args.write_treatment_record:
        record_path = write_treatment_record(
            plan,
            result,
            root,
            output_dir=Path(args.treatment_record_dir).resolve() if args.treatment_record_dir else None,
        )
        payload["treatment_record_path"] = record_path.as_posix()

    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

