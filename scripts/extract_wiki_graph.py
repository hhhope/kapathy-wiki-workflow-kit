#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COVERED_DIRS = [
    ROOT / "wiki" / "ops",
    ROOT / "wiki" / "adr",
    ROOT / "openspec" / "specs",
    ROOT / "wiki" / "examples",
]
RELATION_FIELDS = [
    "related_objects",
    "derived_from",
    "validates",
    "formalizes",
    "supersedes",
    "replaces",
]
RUNTIME_ADR_IDENTITIES = {
    "wiki/adr/0015-agent-readable-wiki-graph-extraction-after-structure.md": "wiki-graph-extraction",
    "wiki/adr/0016-agent-readable-wiki-relation-analysis-after-extraction.md": "wiki-relation-analysis",
    "wiki/adr/0017-agent-readable-wiki-semantic-scoring-after-relation-analysis.md": "wiki-semantic-scoring",
    "wiki/adr/0018-agent-readable-wiki-utilization-layer-after-semantic-scoring.md": "wiki-utilization-layer",
    "wiki/adr/0019-agent-readable-wiki-runtime-context-after-utilization.md": "wiki-runtime-context",
    "wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md": "wiki-runtime-context-source-integration",
    "wiki/adr/0021-agent-readable-wiki-runtime-auto-routing-after-source-integration.md": "wiki-runtime-auto-routing",
    "wiki/adr/0022-agent-readable-wiki-context-injection-after-runtime-auto-routing.md": "wiki-context-injection",
    "wiki/adr/0023-agent-readable-wiki-self-directed-execution-after-context-injection.md": "wiki-self-directed-execution",
}


@dataclass
class ParsedPage:
    path: str
    layer: str
    canonical_object: str | None
    artifact_type: str | None
    metadata: dict


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    raw_meta, body = parts
    lines = raw_meta.splitlines()[1:]
    meta: dict[str, object] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if re.match(r"^[A-Za-z0-9_-]+:\s*$", line):
            key = line.split(":", 1)[0].strip()
            items: list[str] = []
            i += 1
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:].strip().strip('"').strip("'"))
                i += 1
            meta[key] = items
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                meta[key] = [] if not inner else [
                    item.strip().strip('"').strip("'")
                    for item in inner.split(",")
                ]
            else:
                meta[key] = value
        i += 1
    return meta, body


def derive_layer(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("wiki/ops/"):
        return "wiki/ops"
    if rel.startswith("wiki/adr/"):
        return "wiki/adr"
    if rel.startswith("wiki/examples/"):
        return "wiki/examples"
    if rel.startswith("openspec/specs/"):
        return "openspec/specs"
    raise ValueError(f"unsupported layer for {rel}")


def derive_object_and_type(path: Path, meta: dict) -> tuple[str | None, str | None]:
    canonical_object = meta.get("canonical_object")
    artifact_type = meta.get("artifact_type")
    if isinstance(canonical_object, str) and isinstance(artifact_type, str):
        return canonical_object, artifact_type

    rel = path.relative_to(ROOT).as_posix()
    stem = path.stem

    if rel.startswith("openspec/specs/") and rel.endswith("/spec.md"):
        return rel.split("/")[2], "spec"

    if rel in RUNTIME_ADR_IDENTITIES:
        return RUNTIME_ADR_IDENTITIES[rel], "adr"

    # Stable object-family resolvers for current formalized pages.
    if stem == "agent-readable-wiki-naming-model":
        return "wiki-naming-model", "method"
    if stem == "agent-readable-wiki-frontmatter":
        return "wiki-frontmatter-model", "method"
    if rel == "openspec/specs/wiki-naming-model/spec.md":
        return "wiki-naming-model", "spec"
    if rel == "openspec/specs/wiki-frontmatter-model/spec.md":
        return "wiki-frontmatter-model", "spec"
    if rel == "wiki/adr/0013-agent-readable-wiki-naming-before-graph-growth.md":
        return "wiki-naming-model", "adr"
    if rel == "wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md":
        return "wiki-frontmatter-model", "adr"

    if "disagreement-management" in stem or "disagreement-management" in rel:
        if "replay-harness" in stem:
            return "disagreement-management", "replay-harness"
        if "replay-validation" in stem:
            return "disagreement-management", "replay-validation"
        if stem == "sample-disagreement-retro":
            return "disagreement-management", "sample"
        if rel == "openspec/specs/disagreement-management-method/spec.md":
            return "disagreement-management", "spec"
        if rel == "wiki/adr/0012-disagreement-management-before-conclusion-promotion.md":
            return "disagreement-management", "adr"
        return "disagreement-management", "method"

    if stem == "conversation-handoff-mode":
        return "conversation-handoff", "method"
    if stem == "sample-handoff-topic":
        return "conversation-handoff", "sample"
    if rel == "openspec/specs/conversation-north-star-handoff/spec.md":
        return "conversation-handoff", "spec"

    if stem == "example-driven-wiki-capture":
        return "example-driven-capture", "method"
    if "example-driven-capture-runtime-validation" in stem:
        return "example-driven-capture", "runtime-validation"
    if stem == "github-analysis-example":
        return "example-driven-capture", "example"
    if rel == "openspec/specs/example-driven-wiki-capture/spec.md":
        return "example-driven-capture", "spec"

    return None, None


def normalize_relation_value(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str):
        return [value] if value.strip() else []
    return [str(value)]


def collect_pages() -> tuple[list[dict], list[dict], list[str]]:
    nodes: list[dict] = []
    edges: list[dict] = []
    warnings: list[str] = []

    for base_dir in COVERED_DIRS:
        for path in sorted(base_dir.rglob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            if path.name == "index.md":
                continue
            text = path.read_text(encoding="utf-8")
            meta, _body = parse_frontmatter(text)
            canonical_object, artifact_type = derive_object_and_type(path, meta)
            layer = derive_layer(path)

            if not canonical_object or not artifact_type:
                warnings.append(f"unresolved_identity:{rel}")
                continue

            nodes.append(
                {
                    "page_path": rel,
                    "canonical_object": canonical_object,
                    "artifact_type": artifact_type,
                    "source_layer": layer,
                }
            )

            for relation_type in RELATION_FIELDS:
                for target in normalize_relation_value(meta.get(relation_type)):
                    edges.append(
                        {
                            "source_page_path": rel,
                            "relation_type": relation_type,
                            "target": target,
                        }
                    )

    return nodes, edges, warnings


def main() -> None:
    nodes, edges, warnings = collect_pages()
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "covered_layers": [p.relative_to(ROOT).as_posix() for p in COVERED_DIRS],
        "summary": {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "warning_count": len(warnings),
        },
        "nodes": nodes,
        "edges": edges,
        "warnings": warnings,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
