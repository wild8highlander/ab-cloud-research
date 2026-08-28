#!/bin/bash
# =============================================================================
# deploy.sh — Запушить AB-Cloud Verification Suite на GitHub
# =============================================================================
# Репозиторий: wild8highlander/research-papers
# СУЩЕСТВУЮЩИЕ ФАЙЛЫ НЕ УДАЛЯТСЯ — только ДОБАВЛЯЕМ новые!
# =============================================================================
# Использование:
#   chmod +x deploy.sh
#   ./deploy.sh                    # интерактивный (спросит PAT)
#   ./deploy.sh ghp_ВАШ_ТОКЕН     # с токеном сразу
# =============================================================================

set -euo pipefail

REPO="wild8highlander/research-papers"
BRANCH="main"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VERIFY_DIR="$SCRIPT_DIR"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'; NC='\033[0m'

echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  AB-Cloud Verification Suite → GitHub Deploy${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo ""

# ─── PAT из аргумента или ввода ───────────────────────────────────────
PAT="${1:-}"
if [ -z "$PAT" ]; then
    if [ -n "${GITHUB_TOKEN:-}" ]; then
        PAT="$GITHUB_TOKEN"
        echo -e "${GREEN}  ✓ GITHUB_TOKEN из окружения${NC}"
    else
        echo -e "${YELLOW}Нужен Personal Access Token (PAT):${NC}"
        echo "  Создайте: https://github.com/settings/tokens → Generate new token (classic) → scope: repo"
        echo ""
        read -rsp "Вставьте PAT: " PAT
        echo ""
        [ -z "$PAT" ] && { echo -e "${RED}PAT не введён. Выход.${NC}"; exit 1; }
    fi
fi

# ─── Клонировать ─────────────────────────────────────────────────────
echo -e "${YELLOW}[1/4] Клонирование $REPO ...${NC}"
WORK=$(mktemp -d)
trap "rm -rf '$WORK'" EXIT
git clone "https://${PAT}@github.com/$REPO.git" "$WORK/repo" 2>&1 | sed 's|'"$PAT"'|***|g'
cd "$WORK/repo"
EXISTING=$(find . -not -path './.git/*' -type f | wc -l)
echo -e "${GREEN}  ✓ Склонировано ($EXISTING файлов уже в репо)${NC}"

# ─── Копировать только ab-cloud-verification/ ────────────────────────
echo -e "${YELLOW}[2/4] Добавление ab-cloud-verification/ ...${NC}"
cp -r "$VERIFY_DIR" "$WORK/repo/ab-cloud-verification"
ADDED=$(find ./ab-cloud-verification -type f | wc -l)
echo -e "${GREEN}  ✓ $ADDED файлов добавлено (существующие не тронуты)${NC}"

# ─── Коммит ──────────────────────────────────────────────────────────
echo -e "${YELLOW}[3/4] Коммит ...${NC}"
git add -A
git config user.name "Isaev Iskhak Khamzatovich"
git config user.email "aslan08_05@mail.ru"
git commit -m "Add AB-Cloud Verification Suite: 10 languages, 3 objections, bilingual RU/EN

- Python, C++, Fortran, Julia, Rust, R, MATLAB, JavaScript, Go, Haskell
- Each: main bilingual + EN + RU + standalone runner
- load_zeros() with --zeros N, --source auto|50k|500k|2M|highT|zeros6
- 8 data files with Riemann zeta zeros (13K to 2M+)
- 3 reviewer objections: b(N) convergence, GUE spacing, large-T decay
- ORCID: 0009-0003-7299-0701 | DOI: 10.5281/zenodo.21825394"
echo -e "${GREEN}  ✓ Коммит создан${NC}"

# ─── Push ─────────────────────────────────────────────────────────────
echo -e "${YELLOW}[4/4] Push на GitHub ...${NC}"
git push origin "$BRANCH" 2>&1 | sed 's|'"$PAT"'|***|g'

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  ✓ ГОТОВО! Все файлы на GitHub!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  https://github.com/$REPO/tree/main/ab-cloud-verification${NC}"
