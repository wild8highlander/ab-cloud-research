#!/usr/bin/env bash
# ============================================================================
# push_to_github.sh — AB-Cloud Research
# Push the prepared repository to GitHub in one command.
#
# Usage:
#   ./push_to_github.sh
#
# You will be asked for:
#   1. GitHub username   (default: wild8highlander)
#   2. Personal Access Token (PAT) with "repo" scope
#      Create one at: https://github.com/settings/tokens/new?scopes=repo
#      (classic token) or use a fine-grained token with Contents: read/write
#      on the target repository.
#
# The token is used ONLY to build the push URL in memory; it is not stored
# on disk, not echoed, and not written to .git/config (the remote keeps the
# original https URL).
# ============================================================================
set -euo pipefail

REPO_NAME="${REPO_NAME:-ab-cloud-research}"
BRANCH="${BRANCH:-main}"

echo "=============================================="
echo " AB-Cloud Research — GitHub push"
echo "=============================================="

read -r -p "GitHub username [wild8highlander]: " GH_USER
GH_USER="${GH_USER:-wild8highlander}"
read -rs -p "Personal Access Token (input hidden): " GH_TOKEN
echo ""

if [[ -z "${GH_TOKEN}" ]]; then
  echo "ERROR: empty token."; exit 1
fi

if [[ ! -d .git ]]; then
  echo "Initializing git repository…"
  git init -b "${BRANCH}"
  git add -A
  git commit -m "feat: AB-Cloud Research v1.1.0 (spinor64 + run artifacts + apps)"
fi

git config user.name  >/dev/null 2>&1 || git config user.name  "${GH_USER}"
git config user.email >/dev/null 2>&1 || git config user.email "${GH_USER}@users.noreply.github.com"

# make sure everything is committed
if ! git diff-index --quiet HEAD -- 2>/dev/null; then
  echo "There are uncommitted changes — committing them first."
  git add -A
  git commit -m "chore: pending changes before push"
fi

# do NOT print the token
echo ""
echo "Pushing https://github.com/${GH_USER}/${REPO_NAME}.git  (branch: ${BRANCH})…"
git push "https://x-access-token:${GH_TOKEN}@github.com/${GH_USER}/${REPO_NAME}.git" \
  "HEAD:refs/heads/${BRANCH}"

echo ""
echo "✔ Done. Your repository: https://github.com/${GH_USER}/${REPO_NAME}"
echo "  (the token was used in memory only and is NOT stored anywhere)"
