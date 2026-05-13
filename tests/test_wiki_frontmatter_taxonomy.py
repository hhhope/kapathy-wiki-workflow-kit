from __future__ import annotations

from pathlib import Path

from scripts.check_wiki_frontmatter import load_taxonomy
from scripts.check_wiki_frontmatter import check_content_drift


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


def minimal_config() -> dict:
    return {
        "fields": {
            "domain": {
                "forbidden": ["personal-ops"],
                "known": ["none", "unclassified", "nirvana"],
            },
            "ops_area": {"allowed": ["agent-governance", "source-intake"]},
        },
        "path_rules": {
            "wiki/ops": {"required": ["layer", "domain", "ops_area"], "layer": "ops"},
        },
        "severity": {
            "forbidden_domain": "error",
            "missing_ops_area_on_ops_page": "error",
            "missing_domain_on_sample_ops_page": "error",
            "unclassified_without_flag": "error",
            "unknown_domain": "warn",
            "missing_layer_on_legacy_page": "warn",
        },
        "sample_migration_paths": ["wiki/ops/sample.md"],
    }


def test_content_drift_reports_forbidden_personal_ops(tmp_path: Path) -> None:
    write(
        tmp_path / "wiki/ops/sample.md",
        """
---
layer: ops
domain: personal-ops
ops_area: agent-governance
---
# Sample
""".lstrip(),
    )

    entries = check_content_drift(tmp_path, minimal_config())

    assert [(entry.kind, entry.severity, entry.value) for entry in entries] == [
        ("forbidden_domain", "error", "personal-ops")
    ]


def test_content_drift_requires_ops_area_for_sample_path(tmp_path: Path) -> None:
    write(
        tmp_path / "wiki/ops/sample.md",
        """
---
layer: ops
domain: none
---
# Sample
""".lstrip(),
    )

    entries = check_content_drift(tmp_path, minimal_config())

    assert any(entry.kind == "missing_ops_area_on_ops_page" for entry in entries)


def test_unclassified_domain_requires_classification_flag(tmp_path: Path) -> None:
    write(
        tmp_path / "wiki/ops/sample.md",
        """
---
layer: ops
domain: unclassified
ops_area: source-intake
---
# Sample
""".lstrip(),
    )

    entries = check_content_drift(tmp_path, minimal_config())

    assert any(entry.kind == "unclassified_without_flag" for entry in entries)
