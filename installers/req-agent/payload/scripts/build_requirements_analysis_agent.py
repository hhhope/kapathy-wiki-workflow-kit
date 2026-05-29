#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.requirements_analysis_agent import analyze_requirements_intake


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze requirements intent and domain.")
    parser.add_argument("material", nargs="?", default="")
    parser.add_argument("--material-file")
    parser.add_argument("--repo-root", default=str(ROOT))
    args = parser.parse_args()

    material = args.material
    if args.material_file:
        with open(args.material_file, encoding="utf-8") as handle:
            material = handle.read()
    print(
        json.dumps(
            analyze_requirements_intake(material, repo_root=args.repo_root),
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
