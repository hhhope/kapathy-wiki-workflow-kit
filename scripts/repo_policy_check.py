from __future__ import annotations

import argparse
import sys
from pathlib import Path


def find_draft_skill_violations(repo_root: Path) -> list[Path]:
    draft_root = repo_root / "skills-drafts"
    if not draft_root.exists():
        return []
    return sorted(path.relative_to(repo_root) for path in draft_root.rglob("SKILL.md"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check repository workflow publication boundaries.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root to inspect. Defaults to the current directory.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    violations = find_draft_skill_violations(repo_root)
    if not violations:
        print("OK: no active draft skill files under skills-drafts/")
        return 0

    print("FAIL: active draft skill files found under skills-drafts/:")
    for violation in violations:
        print(violation.as_posix())
    return 1


if __name__ == "__main__":
    sys.exit(main())
