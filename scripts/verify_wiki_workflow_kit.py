#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_PATHS = [
    "PROJECT.md",
    "AGENTS.md",
    "CLAUDE.md",
    "wiki/index.md",
    "wiki/ai-workflow.md",
    "wiki/ops/index.md",
    "wiki/reports/index.md",
    "wiki/sources/index.md",
    "wiki/adr/index.md",
    "wiki/templates",
    "wiki/examples/index.md",
    ".codex/skills/material-collaboration-defaults/SKILL.md",
    ".codex/skills/meeting-note-output/SKILL.md",
    ".codex/skills/openspec-explore/SKILL.md",
    ".codex/skills/weixin-reader/SKILL.md",
    "openspec/config.yaml",
    "openspec/changes/archive",
    ".obsidian/core-plugins.json",
]


def main() -> int:
    root = Path.cwd()
    missing = [path for path in REQUIRED_PATHS if not (root / path).exists()]
    if missing:
        print("Missing required kit paths:")
        for path in missing:
            print(f"- {path}")
        return 1
    print("Wiki workflow kit verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
