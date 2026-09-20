#!/usr/bin/env bash
# ============================================================================
#  upload_to_github.sh — AB-Cloud v23 Academic Package (v34)
#  One-command uploader: copies the prepared package folder into your GitHub
#  repository and pushes it. Designed for Termux on Android, also works on
#  Linux and macOS.
#
#  Usage (interactive):
#      bash upload_to_github.sh
#
#  Usage (non-interactive / advanced):
#      GH_USER=yourname GH_TOKEN=ghp_xxx GH_REPO=ab-cloud-research \
#          bash upload_to_github.sh
#
#  What it does:
#    1. Installs git if missing (Termux: pkg; Debian/Ubuntu: apt; macOS: brew).
#    2. Locates repo_content/AB_Cloud_v23_Academic_Package next to this script.
#    3. Asks for your GitHub username, repository and Personal Access Token.
#    4. Clones your repository, replaces the package folder with the prepared
#       one, commits and pushes.
#    5. Cleans the token out of the remote URL when finished.
#
#  The token is read with hidden input (read -s) and is never written to disk.
# ============================================================================

set -uo pipefail

# never hang on credential prompts; keep the phone awake during the upload
export GIT_TERMINAL_PROMPT=0
command -v termux-wake-lock >/dev/null 2>&1 && termux-wake-lock 2>/dev/null
trap 'command -v termux-wake-unlock >/dev/null 2>&1 && termux-wake-unlock 2>/dev/null' EXIT

# ------------------------------------------------------------------ settings
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Если рядом есть repo_content/AB_Cloud_v23_Academic_Package — берём её,
# иначе считаем пакетом саму папку, где лежит скрипт.
if [ -d "${SCRIPT_DIR}/repo_content/AB_Cloud_v23_Academic_Package" ]; then
  PKG_SRC="${SCRIPT_DIR}/repo_content/AB_Cloud_v23_Academic_Package"
else
  PKG_SRC="${SCRIPT_DIR}"
fi
DEFAULT_REPO="ab-cloud-research"
DEFAULT_TARGET="AB_Cloud_v23_Academic_Package"
# Рабочая папка — в домашней директории, чтобы не копировать её в саму себя
WORKROOT="${HOME}/_ab_cloud_upload_work"

# ------------------------------------------------------------------ UI helpers
if [ -t 1 ]; then
  C_G="\033[1;32m"; C_Y="\033[1;33m"; C_R="\033[1;31m"; C_B="\033[1;36m"; C_0="\033[0m"
else
  C_G=""; C_Y=""; C_R=""; C_B=""; C_0=""
fi
say()  { printf "%b\n" "${C_B}==>${C_0} $*"; }
ok()   { printf "%b\n" "${C_G} ✔ ${C_0} $*"; }
warn() { printf "%b\n" "${C_Y} ⚠ ${C_0} $*"; }
die()  { printf "%b\n" "${C_R} ✖ ERROR: $*${C_0}" >&2; exit 1; }

# ------------------------------------------------------------------ 0. preflight
say "AB-Cloud v23 Academic Package (v34) — GitHub uploader"
echo    "------------------------------------------------------"

command -v git >/dev/null 2>&1 || {
  warn "git is not installed. Trying to install it…"
  if command -v pkg >/dev/null 2>&1; then
    yes | pkg install git >/dev/null 2>&1 || pkg install git -y || die "Could not install git via pkg. Run: pkg install git"
  elif command -v apt-get >/dev/null 2>&1; then
    sudo apt-get update -y && sudo apt-get install -y git || die "Could not install git via apt. Run: sudo apt install git"
  elif command -v brew >/dev/null 2>&1; then
    brew install git || die "Could not install git via brew. Run: brew install git"
  else
    die "git is missing and no known package manager found. Install git manually."
  fi
}
ok "git: $(git --version)"

[ -d "${PKG_SRC}" ] || die "Package folder not found: ${PKG_SRC}
Make sure the folder 'repo_content/AB_Cloud_v23_Academic_Package' sits next to this script."
FILES_COUNT="$(find "${PKG_SRC}" -type f | wc -l | tr -d ' ')"
SIZE_HUMAN="$(du -sh "${PKG_SRC}" 2>/dev/null | cut -f1)"
ok "Package found: ${FILES_COUNT} files, ${SIZE_HUMAN}"

# ------------------------------------------------------------------ 1. questions
GH_USER="${GH_USER:-}"
GH_TOKEN="${GH_TOKEN:-}"
GH_REPO="${GH_REPO:-}"
TARGET_DIR="${TARGET_DIR:-}"
COMMIT_MSG="${COMMIT_MSG:-}"

if [ -z "${GH_USER}" ]; then
  printf "%b" " 1/4  GitHub username (ваш логин на GitHub): "
  read -r GH_USER
  [ -n "${GH_USER}" ] || die "Username is required."
fi

if [ -z "${GH_REPO}" ]; then
  printf "%b" " 2/4  Repository name [${DEFAULT_REPO}]: "
  read -r GH_REPO
  GH_REPO="${GH_REPO:-${DEFAULT_REPO}}"
fi

if [ -z "${GH_TOKEN}" ]; then
  printf "%b" " 3/4  Personal Access Token (скрытый ввод; как получить — см. INSTALL_GUIDE): "
  read -rs GH_TOKEN
  echo
  [ -n "${GH_TOKEN}" ] || die "Token is required. Create one: GitHub → Settings → Developer settings → Personal access tokens."
fi

if [ -z "${TARGET_DIR}" ]; then
  printf "%b" " 4/4  Folder name inside the repo [${DEFAULT_TARGET}]: "
  read -r TARGET_DIR
  TARGET_DIR="${TARGET_DIR:-${DEFAULT_TARGET}}"
fi

[ -n "${COMMIT_MSG}" ] || COMMIT_MSG="Add AB-Cloud v23 Academic Package (v34): monograph, preprints, labs, run data; folder READMEs with unique file naming"

GIT_NAME="${GIT_NAME:-${GH_USER}}"
GIT_EMAIL="${GIT_EMAIL:-${GH_USER}@users.noreply.github.com}"

REPO_URL_CLEAN="https://github.com/${GH_USER}/${GH_REPO}.git"
REPO_URL_AUTH="https://${GH_USER}:${GH_TOKEN}@github.com/${GH_USER}/${GH_REPO}.git"

# ------------------------------------------------------------------ 2. token check
say "Checking the token and repository access…"
if ! git ls-remote "${REPO_URL_AUTH}" HEAD >/dev/null 2>&1; then
  die "Cannot access https://github.com/${GH_USER}/${GH_REPO}.git with this token.
Possible causes:
  • the token is wrong or truncated (paste it again);
  • the token lacks write access — for a fine-grained token select the repo
    and set 'Contents: Read and write'; for a classic token enable 'repo' scope;
  • the repository name/username has a typo.
Then run this script again."
fi
ok "Token accepted — repository is reachable."

# ------------------------------------------------------------------ 3. clone / update
WORK="${WORKROOT}/${GH_REPO}"
mkdir -p "${WORKROOT}"
if [ -d "${WORK}/.git" ]; then
  say "Reusing existing clone at ${WORK}"
  git -C "${WORK}" remote set-url origin "${REPO_URL_AUTH}"
  git -C "${WORK}" fetch origin --prune || die "git fetch failed (network?). Run the script again."
else
  say "Cloning ${REPO_URL_CLEAN} …"
  rm -rf "${WORK}"
  git clone "${REPO_URL_AUTH}" "${WORK}" || die "git clone failed (network?). Run the script again."
fi
ok "Repository is at the latest state."

DEFAULT_BRANCH="$(git -C "${WORK}" symbolic-ref --short HEAD)"
ok "Default branch: ${DEFAULT_BRANCH}"

# ------------------------------------------------------------------ 4. copy package
say "Copying the package into the repository as '${TARGET_DIR}/' …"
if [ -d "${WORK}/${TARGET_DIR}" ]; then
  warn "'${TARGET_DIR}' already exists in the repo — it will be REPLACED by the prepared package."
  rm -rf "${WORK}/${TARGET_DIR}"
fi
mkdir -p "${WORK}/$(dirname "${TARGET_DIR}")"
cp -R "${PKG_SRC}" "${WORK}/${TARGET_DIR}" || die "Copying failed (not enough free space?)."
ok "Copied: $(find "${WORK}/${TARGET_DIR}" -type f | wc -l | tr -d ' ') files."

# ------------------------------------------------------------------ 5. commit & push
cd "${WORK}"
git config user.name  "${GIT_NAME}"
git config user.email "${GIT_EMAIL}"

git add -A "${TARGET_DIR}"
if git diff --cached --quiet; then
  warn "Nothing changed since the last upload — nothing to commit."
else
  say "Committing…"
  git commit -m "${COMMIT_MSG}" || die "git commit failed."
  say "Pushing to ${GH_USER}/${GH_REPO} (${DEFAULT_BRANCH}) — this can take a while, keep the screen on…"
  if ! git push origin "${DEFAULT_BRANCH}"; then
    die "git push failed. Most often this is:
  • the token is invalid/expired or lacks WRITE access — for a classic token the
    'repo' scope must be ticked; for a fine-grained token set 'Contents: Read and write';
    create a fresh token and run this script again;
  • no internet / unstable connection — retry;
  • the branch is protected — allow pushes in the repo settings."
  fi
fi

# ------------------------------------------------------------------ 6. cleanup
git remote set-url origin "${REPO_URL_CLEAN}"
ok "Token removed from the repository's remote URL."

echo
printf "%b\n" "${C_G}=============================================================${C_0}"
printf "%b\n" "${C_G}  DONE! The package is on GitHub.${C_0}"
printf "%b\n" "${C_G}  → https://github.com/${GH_USER}/${GH_REPO}/tree/${DEFAULT_BRANCH}/${TARGET_DIR}${C_0}"
printf "%b\n" "${C_G}=============================================================${C_0}"
echo
echo "  Tips:"
echo "   • Open the link above in a browser and check the rendered READMEs."
echo "   • The local clone stays at: ${WORK}"
echo "     (delete it any time:  rm -rf \"${WORK}\")"
echo "   • For security you may now delete/revoke the token you created:"
echo "     GitHub → Settings → Developer settings → Personal access tokens."
echo
