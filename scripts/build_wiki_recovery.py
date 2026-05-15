#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.wiki_recovery import build_recovery_package, write_recovery_record


def main() -> None:
    parser = argparse.ArgumentParser(description="Build wiki recovery package.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument(
        "--write-recovery-record",
        action="store_true",
        help="Write Markdown recovery record. Default behavior is stdout JSON only.",
    )
    parser.add_argument(
        "--recovery-record-dir",
        help="Directory for --write-recovery-record output. Defaults to wiki/ops/wiki-recovery-runs under --root.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    payload = build_recovery_package(root)
    if args.write_recovery_record:
        record_path = write_recovery_record(
            payload,
            root,
            output_dir=Path(args.recovery_record_dir).resolve() if args.recovery_record_dir else None,
        )
        payload["recovery_record_path"] = record_path.as_posix()
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

