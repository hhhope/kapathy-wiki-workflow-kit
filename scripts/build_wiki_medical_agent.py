#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.wiki_medical_agent import build_status_payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the wiki medical agent state controller.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--intent-text", required=True, help="Natural-language user intent to route.")
    args = parser.parse_args()

    payload = build_status_payload(Path(args.root).resolve(), args.intent_text)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
