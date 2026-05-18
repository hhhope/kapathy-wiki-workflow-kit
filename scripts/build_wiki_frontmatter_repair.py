#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.wiki_frontmatter_repair import apply_frontmatter_batch, build_repair_batch


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan or apply bounded wiki frontmatter repairs.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--path", action="append", default=[], help="Explicit target path to include.")
    parser.add_argument(
        "--approved-frontmatter-json",
        help="JSON object mapping target paths to approved frontmatter fields.",
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    batch = build_repair_batch(root, limit=args.limit, paths=args.path or None)
    payload = {"batch": batch}
    if args.approved_frontmatter_json:
        approved = json.loads(args.approved_frontmatter_json)
        if not isinstance(approved, dict):
            parser.error("--approved-frontmatter-json must be a JSON object")
        payload["apply_result"] = apply_frontmatter_batch(
            root,
            batch,
            approved_frontmatter=approved,
            apply=args.apply,
        )
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
