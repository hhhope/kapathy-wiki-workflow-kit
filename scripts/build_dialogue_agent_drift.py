#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.dialogue_agent_drift import build_dialogue_drift_report


def _load_candidates(path: str | None) -> list[dict[str, str]] | None:
    if not path:
        return None
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("--candidates-json must contain a list")
    candidates: list[dict[str, str]] = []
    for item in payload:
        if not isinstance(item, dict) or not item.get("path"):
            raise ValueError("each candidate must be an object with path")
        candidates.append(
            {
                "detail_ref": str(item.get("detail_ref") or ""),
                "path": str(item["path"]),
            }
        )
    return candidates


def main() -> None:
    parser = argparse.ArgumentParser(description="Build dialogue/agent drift review report.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--candidates-json", help="Optional JSON list of {detail_ref, path} candidates.")
    args = parser.parse_args()

    report = build_dialogue_drift_report(
        Path(args.root).resolve(),
        candidates=_load_candidates(args.candidates_json),
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
