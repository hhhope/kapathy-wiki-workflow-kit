#!/usr/bin/env bash
set -euo pipefail

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
skill_dir=$(dirname "$script_dir")
repo_root=$(dirname "$(dirname "$skill_dir")")
templates_dir="$repo_root/skills/lore/references"

wiki_repo=""
codex_home="${HOME}/.codex"
project_dir=""
project_name=""
legacy_lore=""
member="yan"

usage() {
  cat <<'EOF'
Usage:
  bootstrap_lore_wiki.sh --project-dir <path> [options]

Options:
  --project-dir <path>   Project repo containing PROJECT.md
  --project-name <name>  Override project name
  --wiki-repo <path>     Shared lore repo root (default: /mnt/d/team-lore when available, else ~/team-lore)
  --codex-home <path>    Codex home for AGENTS.md (default: ~/.codex)
  --legacy-lore <path>   Optional flat lore file to snapshot for migration
  --member <name>        Member identifier for generated notes
EOF
}

die() {
  echo "ERROR: $*" >&2
  exit 1
}

render_template() {
  local src="$1"
  local dest="$2"
  local domain_name="$3"
  sed \
    -e "s/project-name/${project_name}/g" \
    -e "s/domain-name/${domain_name}/g" \
    -e "s/example-domain/${domain_name}/g" \
    -e "s/pitfall-name/bootstrap-entry/g" \
    -e "s/principle-name/wiki-in-git/g" \
    -e "s/project-a/${project_name}/g" \
    -e "s/project-b/${project_name}/g" \
    "$src" > "$dest"
}

default_wiki_repo() {
  if [ -n "${LORE_BOOTSTRAP_DEFAULT_REPO:-}" ]; then
    printf '%s\n' "$LORE_BOOTSTRAP_DEFAULT_REPO"
    return
  fi
  if [ -d /mnt/d ]; then
    printf '%s\n' "/mnt/d/team-lore"
    return
  fi
  printf '%s\n' "${HOME}/team-lore"
}

detect_project_name() {
  if [ -n "$project_name" ]; then
    return
  fi
  if [ -f "$project_dir/PROJECT.md" ]; then
    project_name=$(awk '
      BEGIN { in_frontmatter=0 }
      /^---$/ { if (in_frontmatter==0) { in_frontmatter=1; next } else { exit } }
      in_frontmatter && /^project:[[:space:]]*/ {
        sub(/^project:[[:space:]]*/, "", $0)
        print $0
        exit
      }
    ' "$project_dir/PROJECT.md")
  fi
  if [ -z "$project_name" ]; then
    project_name=$(basename "$project_dir")
  fi
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --project-dir)
      project_dir="$2"
      shift 2
      ;;
    --project-name)
      project_name="$2"
      shift 2
      ;;
    --wiki-repo)
      wiki_repo="$2"
      shift 2
      ;;
    --codex-home)
      codex_home="$2"
      shift 2
      ;;
    --legacy-lore)
      legacy_lore="$2"
      shift 2
      ;;
    --member)
      member="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
done

[ -n "$project_dir" ] || die "--project-dir is required"
[ -d "$project_dir" ] || die "project dir does not exist: $project_dir"
[ -f "$project_dir/PROJECT.md" ] || die "PROJECT.md not found in project dir: $project_dir"
[ -n "$wiki_repo" ] || wiki_repo=$(default_wiki_repo)

detect_project_name

mkdir -p "$wiki_repo"
if [ ! -d "$wiki_repo/.git" ]; then
  git -c init.defaultBranch=main init "$wiki_repo" >/dev/null
fi

wiki_root="$wiki_repo/wiki"
project_root="$wiki_root/projects/$project_name"
domain_name="entrypoint"

mkdir -p \
  "$wiki_root/projects/$project_name/domains" \
  "$wiki_root/pitfalls" \
  "$wiki_root/principles" \
  "$wiki_repo/templates" \
  "$codex_home"

if [ ! -f "$wiki_root/index.md" ]; then
  render_template "$templates_dir/INDEX-template.md" "$wiki_root/index.md" "$domain_name"
fi

if [ ! -f "$project_root/overview.md" ]; then
  render_template "$templates_dir/PROJECT-OVERVIEW-template.md" "$project_root/overview.md" "$domain_name"
fi

if [ ! -f "$project_root/domains/$domain_name.md" ]; then
  render_template "$templates_dir/DOMAIN-template.md" "$project_root/domains/$domain_name.md" "$domain_name"
fi

if [ ! -f "$wiki_root/pitfalls/bootstrap-entry.md" ]; then
  render_template "$templates_dir/PITFALL-template.md" "$wiki_root/pitfalls/bootstrap-entry.md" "$domain_name"
fi

if [ ! -f "$wiki_root/principles/wiki-in-git.md" ]; then
  render_template "$templates_dir/PRINCIPLE-template.md" "$wiki_root/principles/wiki-in-git.md" "$domain_name"
fi

cp "$templates_dir/INDEX-template.md" "$wiki_repo/templates/index.md"
cp "$templates_dir/PROJECT-OVERVIEW-template.md" "$wiki_repo/templates/project-overview.md"
cp "$templates_dir/DOMAIN-template.md" "$wiki_repo/templates/domain.md"
cp "$templates_dir/PITFALL-template.md" "$wiki_repo/templates/pitfall.md"
cp "$templates_dir/PRINCIPLE-template.md" "$wiki_repo/templates/principle.md"

agents_path="$codex_home/AGENTS.md"
team_lore_line="team-lore: ${wiki_root}"
if [ -f "$agents_path" ]; then
  if grep -q '^team-lore:' "$agents_path"; then
    awk -v repl="$team_lore_line" '
      /^team-lore:/ { print repl; next }
      { print }
    ' "$agents_path" > "$agents_path.tmp"
    mv "$agents_path.tmp" "$agents_path"
  else
    printf "%s\n\n%s\n" "# Lore bootstrap added path" "$team_lore_line" >> "$agents_path"
  fi
else
  cat > "$agents_path" <<EOF
# Lore bootstrap minimal AGENTS overlay

$team_lore_line
EOF
fi

if [ -n "$legacy_lore" ]; then
  [ -f "$legacy_lore" ] || die "legacy lore file does not exist: $legacy_lore"
  mkdir -p "$project_root/legacy"
  cp "$legacy_lore" "$project_root/legacy/LORE-legacy.md"
  cat > "$project_root/migration-notes.md" <<EOF
# Lore Migration Notes — ${project_name}

Date: $(date '+%Y-%m-%d %H:%M:%S')
Member: ${member}

## Source

- Legacy flat lore: \`${legacy_lore}\`

## Required split targets

- project overview updates
- domain pages under \`projects/${project_name}/domains/\`
- shared pitfall pages under \`pitfalls/\`
- shared principle pages under \`principles/\`

## Status

- Legacy file copied for traceability
- Semantic split still required before flat lore can be retired
EOF
fi

echo "MODE: $([ -n "$legacy_lore" ] && echo migration || echo bootstrap)"
if [ -n "${LORE_BOOTSTRAP_DEFAULT_REPO:-}" ] && [ "$wiki_repo" = "${LORE_BOOTSTRAP_DEFAULT_REPO}" ]; then
  echo "INSTALL_TARGET_SOURCE: env-default"
elif [ "$wiki_repo" = "$(default_wiki_repo)" ]; then
  echo "INSTALL_TARGET_SOURCE: auto-default"
else
  echo "INSTALL_TARGET_SOURCE: explicit"
fi
echo "WIKI_REPO: $wiki_repo"
echo "WIKI_ROOT: $wiki_root"
echo "PROJECT: $project_name"
echo "AGENTS_PATH: $agents_path"
