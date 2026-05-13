from __future__ import annotations

from pathlib import Path

from scripts.check_wiki_frontmatter import load_taxonomy


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_load_taxonomy_reads_contract(tmp_path: Path) -> None:
    write(
        tmp_path / "wiki/config/frontmatter-taxonomy.yaml",
        """
version: 1
fields:
  domain:
    forbidden:
      - personal-ops
    known:
      - none
      - unclassified
  ops_area:
    allowed:
      - source-intake
path_rules:
  wiki/ops:
    required:
      - layer
      - domain
      - ops_area
    layer: ops
severity:
  forbidden_domain: error
producer_paths:
  templates:
    - wiki/templates/*.md
  scripts:
    - scripts/inbox_intake.py
sample_migration_paths:
  - wiki/ops/example-intake.md
""".lstrip(),
    )

    config = load_taxonomy(tmp_path)

    assert config["version"] == 1
    assert config["fields"]["domain"]["forbidden"] == ["personal-ops"]
    assert config["producer_paths"]["scripts"] == ["scripts/inbox_intake.py"]
