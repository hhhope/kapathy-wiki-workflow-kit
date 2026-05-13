#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = Path("wiki/config/frontmatter-taxonomy.yaml")


@dataclass(frozen=True)
class DriftEntry:
    kind: str
    severity: str
    path: str
    message: str
    field: str | None = None
    value: str | None = None


def load_taxonomy(root: Path | str = ROOT) -> dict[str, Any]:
    root_path = Path(root)
    config_file = root_path / CONFIG_PATH
    with config_file.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"taxonomy config must be a mapping: {config_file}")
    return data


def build_report(root: Path | str = ROOT) -> dict[str, Any]:
    root_path = Path(root)
    config = load_taxonomy(root_path)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": root_path.resolve().as_posix(),
        "config_path": CONFIG_PATH.as_posix(),
        "summary": {"error": 0, "warn": 0, "info": 0, "total": 0},
        "entries": [],
        "taxonomy_version": config.get("version"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check wiki frontmatter taxonomy drift.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--json-output", default="/tmp/wiki-frontmatter-taxonomy-report.json")
    parser.add_argument("--markdown-output", default="/tmp/wiki-frontmatter-taxonomy-report.md")
    args = parser.parse_args()

    report = build_report(Path(args.root))
    Path(args.json_output).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    Path(args.markdown_output).write_text("# Wiki Frontmatter Taxonomy Report\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
