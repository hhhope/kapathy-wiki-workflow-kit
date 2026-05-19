from __future__ import annotations

import fnmatch

from scripts import llm_wiki_seed_manifest as manifest


def test_seed_manifest_includes_real_wiki_skill_surface() -> None:
    required_skill_dirs = {
        ".codex/skills/learning-capture",
        ".codex/skills/readme-learning-capture",
        ".codex/skills/material-collaboration-defaults",
        ".codex/skills/public-report-quality-gate",
        ".codex/skills/wiki-status",
        ".codex/skills/wiki-manifest",
        ".codex/skills/wiki-query",
        ".codex/skills/wiki-react",
        ".codex/skills/wiki-apply",
        ".codex/skills/wiki-scorecard",
        ".codex/skills/wiki-frontmatter-taxonomy",
        ".codex/skills/wiki-medical-agent",
        ".codex/skills/wiki-doctor",
        ".codex/skills/wiki-review-decisions",
        ".codex/skills/wiki-confirm",
        ".codex/skills/wiki-treatment",
        ".codex/skills/wiki-surgery",
        ".codex/skills/wiki-recovery",
        ".codex/skills/openspec-router",
        ".codex/skills/openspec-apply-change",
    }

    copied_dirs = set(manifest.COPY_DIRS)

    assert required_skill_dirs <= copied_dirs


def test_seed_manifest_includes_config_and_runtime_scripts() -> None:
    required_files = {
        "wiki/config/frontmatter-taxonomy.yaml",
        "wiki/config/behavior-asset-evaluation.yaml",
        "scripts/check_wiki_frontmatter.py",
        "scripts/build_wiki_status.py",
        "scripts/extract_wiki_graph.py",
        "scripts/analyze_wiki_relations.py",
        "scripts/score_wiki_semantics.py",
        "scripts/derive_wiki_utilization.py",
        "scripts/build_wiki_runtime_context.py",
        "scripts/derive_runtime_auto_routing.py",
        "scripts/build_runtime_context_injection.py",
        "scripts/derive_self_directed_execution.py",
        "scripts/build_wiki_medical_agent.py",
        "scripts/build_wiki_medical_case.py",
        "scripts/build_wiki_review_decisions.py",
        "scripts/build_wiki_treatment.py",
        "scripts/build_wiki_surgery.py",
        "scripts/build_wiki_recovery.py",
        "scripts/wiki_medical_agent.py",
        "scripts/wiki_medical_case.py",
        "scripts/wiki_review_decisions.py",
        "scripts/wiki_treatment.py",
        "scripts/wiki_surgery.py",
        "scripts/wiki_recovery.py",
    }

    copied_files = set(manifest.COPY_FILES)

    assert required_files <= copied_files


def test_seed_manifest_generates_runtime_gitignore() -> None:
    gitignore = manifest.GENERATED_TEXT_FILES[".gitignore"]

    assert "__pycache__/" in gitignore
    assert "*.py[cod]" in gitignore


def test_seed_manifest_rejects_archive_dump_paths() -> None:
    forbidden_fragments = {
        "inbox/",
        "logs/",
        "wiki/.obsidian",
        "wiki/reports/reports.zip",
        "openspec/changes/archive",
    }
    forbidden_globs = {
        "wiki/reports/*.zip",
    }
    generated_text_paths = set(manifest.GENERATED_TEXT_FILES)
    generated_sample_paths = set(manifest.GENERATED_SAMPLE_FILES)
    manifest_paths = (
        list(manifest.COPY_FILES)
        + list(manifest.COPY_DIRS)
        + list(manifest.CREATE_DIRS)
        + list(generated_text_paths)
        + list(generated_sample_paths)
    )

    assert forbidden_fragments <= set(manifest.EXCLUDE_FRAGMENTS)
    assert forbidden_globs <= set(manifest.EXCLUDE_GLOBS)
    assert all("*" not in fragment for fragment in manifest.EXCLUDE_FRAGMENTS)
    assert "wiki/reports" in manifest.CREATE_DIRS
    assert "wiki/reports/index.md" in generated_sample_paths
    assert all(
        fragment not in path
        for path in manifest_paths
        for fragment in manifest.EXCLUDE_FRAGMENTS
    )
    assert all(
        not fnmatch.fnmatch(path, pattern)
        for path in manifest_paths
        for pattern in manifest.EXCLUDE_GLOBS
    )
    assert all("concepts" not in path for path in manifest.CREATE_DIRS)
    assert all("entities" not in path for path in manifest.CREATE_DIRS)
