#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GRAPH_EXTRACTOR = ROOT / "scripts" / "extract_wiki_graph.py"
RELATION_ANALYZER = ROOT / "scripts" / "analyze_wiki_relations.py"
DEFAULT_LIMIT = 10


def run_json(command: list[str]) -> dict:
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    return json.loads(completed.stdout)


def load_payload(path: str | None, fallback_command: list[str]) -> dict:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    return run_json(fallback_command)


def relation_analysis_for(graph_path: str | None, graph: dict) -> dict:
    if graph_path:
        return run_json([sys.executable, str(RELATION_ANALYZER), graph_path])

    # Avoid depending on temp files when the caller lets this script run live.
    import tempfile

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json") as handle:
        json.dump(graph, handle, ensure_ascii=False)
        handle.flush()
        return run_json([sys.executable, str(RELATION_ANALYZER), handle.name])


def warning_layer(warning: str) -> str:
    _prefix, _sep, path = warning.partition(":")
    if path.startswith("wiki/ops/"):
        return "wiki/ops"
    if path.startswith("wiki/adr/"):
        return "wiki/adr"
    if path.startswith("wiki/examples/"):
        return "wiki/examples"
    if path.startswith("openspec/specs/"):
        return "openspec/specs"
    return "other"


def normalize_focus(value: str | None) -> str | None:
    return value.strip().lower() if value and value.strip() else None


def matches_focus(value: str, focus: str | None) -> bool:
    return focus is None or focus in value.lower()


def build_object_view(graph: dict, relation_analysis: dict, focus: str | None, limit: int) -> list[dict]:
    nodes_by_object: dict[str, list[dict]] = defaultdict(list)
    relation_types_by_object: dict[str, Counter[str]] = defaultdict(Counter)
    path_to_object: dict[str, str] = {}

    for node in graph.get("nodes", []):
        canonical_object = node["canonical_object"]
        nodes_by_object[canonical_object].append(node)
        path_to_object[node["page_path"]] = canonical_object

    for edge in graph.get("edges", []):
        source_object = path_to_object.get(edge["source_page_path"])
        if source_object:
            relation_types_by_object[source_object][edge["relation_type"]] += 1

    coverage_by_object = {
        item["canonical_object"]: item
        for item in relation_analysis.get("object_coverage", [])
    }

    object_view = []
    for canonical_object, nodes in sorted(nodes_by_object.items()):
        if not matches_focus(canonical_object, focus):
            continue
        coverage = coverage_by_object.get(canonical_object, {})
        representative_pages = [
            {
                "page_path": node["page_path"],
                "artifact_type": node["artifact_type"],
                "source_layer": node["source_layer"],
            }
            for node in sorted(nodes, key=lambda item: item["page_path"])[:5]
        ]
        object_view.append(
            {
                "canonical_object": canonical_object,
                "node_count": len(nodes),
                "source_layers": coverage.get(
                    "source_layers",
                    sorted({node["source_layer"] for node in nodes}),
                ),
                "artifact_types": coverage.get(
                    "artifact_types",
                    sorted({node["artifact_type"] for node in nodes}),
                ),
                "relation_count": coverage.get(
                    "relation_count",
                    sum(relation_types_by_object[canonical_object].values()),
                ),
                "cross_layer": coverage.get(
                    "cross_layer",
                    len({node["source_layer"] for node in nodes}) > 1,
                ),
                "relation_types": dict(
                    sorted(relation_types_by_object[canonical_object].items())
                ),
                "representative_pages": representative_pages,
            }
        )

    object_view.sort(
        key=lambda item: (
            not item["cross_layer"],
            -item["node_count"],
            -item["relation_count"],
            item["canonical_object"],
        )
    )
    return object_view[:limit]


def summarize_graph(graph: dict, relation_analysis: dict, focus: str | None = None, limit: int = DEFAULT_LIMIT) -> dict:
    normalized_focus = normalize_focus(focus)
    warnings = graph.get("warnings", [])
    warning_by_layer = Counter(warning_layer(warning) for warning in warnings)
    object_view = build_object_view(graph, relation_analysis, normalized_focus, limit)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "focus": focus or None,
        "source_graph_summary": graph.get("summary", {}),
        "source_relation_summary": relation_analysis.get("summary", {}),
        "summary": {
            "displayed_object_count": len(object_view),
            "node_count": graph.get("summary", {}).get("node_count", 0),
            "edge_count": graph.get("summary", {}).get("edge_count", 0),
            "warning_count": graph.get("summary", {}).get("warning_count", len(warnings)),
            "canonical_object_count": relation_analysis.get("summary", {}).get(
                "canonical_object_count", 0
            ),
            "cross_layer_object_count": relation_analysis.get("summary", {}).get(
                "cross_layer_object_count", 0
            ),
        },
        "object_view": object_view,
        "warning_view": {
            "total": len(warnings),
            "by_layer": dict(sorted(warning_by_layer.items())),
            "samples": warnings[:10],
        },
        "proof_boundary_notes": [
            "This is structural graph evidence only.",
            "It does not infer semantic identity for unresolved pages.",
            "It does not prove retrieval quality or rollout readiness.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("focus", nargs="?", help="optional canonical object focus")
    parser.add_argument("--graph", help="path to a graph JSON artifact")
    parser.add_argument("--relation-analysis", help="path to a relation-analysis JSON artifact")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    args = parser.parse_args()

    graph = load_payload(args.graph, [sys.executable, str(GRAPH_EXTRACTOR)])
    relation_analysis = (
        load_payload(args.relation_analysis, [sys.executable, str(RELATION_ANALYZER)])
        if args.relation_analysis
        else relation_analysis_for(args.graph, graph)
    )
    print(
        json.dumps(
            summarize_graph(graph, relation_analysis, args.focus, args.limit),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
