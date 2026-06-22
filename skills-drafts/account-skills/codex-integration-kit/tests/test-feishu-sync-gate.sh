#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CHECK_SCRIPT="${ROOT}/codex-integration-kit/scripts/check-feishu-sync.sh"
TMP_ROOT="$(mktemp -d)"
trap 'rm -rf "${TMP_ROOT}"' EXIT

init_repo() {
  local repo="$1"
  mkdir -p "${repo}/codex-integration-kit/docs" "${repo}/codex-integration-kit/rules/common"
  cat > "${repo}/codex-integration-kit/docs/feishu-codex-governance-share.md" <<'EOF'
# share
EOF
  cat > "${repo}/codex-integration-kit/rules/common/testing.md" <<'EOF'
# testing
EOF
  git -C "${repo}" init -q
  git -C "${repo}" config user.name "Codex"
  git -C "${repo}" config user.email "codex@example.com"
  git -C "${repo}" add .
  git -C "${repo}" commit -qm "init"
}

assert_fails_without_feishu_sync() {
  local repo="${TMP_ROOT}/missing-feishu"
  init_repo "${repo}"
  echo "rule change" >> "${repo}/codex-integration-kit/rules/common/testing.md"
  git -C "${repo}" add codex-integration-kit/rules/common/testing.md

  if "${CHECK_SCRIPT}" --repo "${repo}" --staged >/tmp/feishu-gate-missing.out 2>&1; then
    echo "expected failure when governance files changed without Feishu source sync" >&2
    cat /tmp/feishu-gate-missing.out >&2
    return 1
  fi

  grep -q "Feishu source update required" /tmp/feishu-gate-missing.out
}

assert_passes_with_feishu_sync() {
  local repo="${TMP_ROOT}/with-feishu"
  init_repo "${repo}"
  echo "rule change" >> "${repo}/codex-integration-kit/rules/common/testing.md"
  echo "share change" >> "${repo}/codex-integration-kit/docs/feishu-codex-governance-share.md"
  git -C "${repo}" add \
    codex-integration-kit/rules/common/testing.md \
    codex-integration-kit/docs/feishu-codex-governance-share.md

  "${CHECK_SCRIPT}" --repo "${repo}" --staged >/tmp/feishu-gate-pass.out 2>&1
  grep -q "Feishu sync gate passed" /tmp/feishu-gate-pass.out
}

assert_fails_without_feishu_sync
assert_passes_with_feishu_sync

echo "PASS: feishu sync gate"
