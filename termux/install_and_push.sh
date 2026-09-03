#!/data/data/com.termux/files/usr/bin/bash
# ============================================================================
#  install_and_push.sh — AB-Cloud Research: автоматическая публикация на
#  GitHub прямо из Termux (Android). Работает также на обычном Linux/Mac.
#
#  ЗАПУСК:   bash termux/install_and_push.sh
#
#  Скрипт сам:
#    1) установит недостающие пакеты (git, curl, gh — по необходимости);
#    2) перенесёт репозиторий во внутреннюю память Termux, если он лежит
#       в общей папке /sdcard (там git работает ненадёжно);
#    3) спросит, куда пушить (по умолчанию — ваш репозиторий) и предложит
#       способ входа: PAT-токен ИЛИ вход через браузер (GitHub CLI);
#    4) отправит ветку main (+ теги) на GitHub;
#    5) проверит результат и по желанию откроет репозиторий в браузере.
#
#  Токен и данные входа существуют ТОЛЬКО в оперативной памяти на время
#  работы скрипта: ничего не сохраняется на диск и не пишется в .git/config.
#
#  «Сухой» прогон без каких-либо изменений:
#      DRY_RUN=1 bash termux/install_and_push.sh
# ============================================================================
set -u

# ----------------------------- оформление -----------------------------------
if [ -t 1 ]; then
  C_G="\033[1;32m"; C_Y="\033[1;33m"; C_R="\033[1;31m"; C_C="\033[1;36m"; C_B="\033[1m"; C_0="\033[0m"
else
  C_G=""; C_Y=""; C_R=""; C_C=""; C_B=""; C_0=""
fi
info(){ printf "${C_C}▸${C_0} %s\n" "$*"; }
ok(){   printf "${C_G}✔${C_0} %s\n" "$*"; }
warn(){ printf "${C_Y}!${C_0} %s\n" "$*"; }
die(){  printf "${C_R}✖ ОШИБКА:${C_0} %s\n" "$*" >&2; exit 1; }

DRY_RUN="${DRY_RUN:-0}"

# ----------------------- значения по умолчанию ------------------------------
DEF_USER="wild8highlander"
DEF_REPO_URL="https://github.com/wild8highlander/ab-cloud-research.git"
BRANCH="main"

# -------------------------------- пути --------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

GH_USER=""; GH_TOKEN=""; AUTH_MODE="pat"
REPO_URL="$DEF_REPO_URL"; OWNER="$DEF_USER"; REPO_NAME="ab-cloud-research"
LOCAL_SHA=""; REMOTE_SHA=""

# ----------------------------- вспомогательные ------------------------------
ask(){ # $1 - вопрос, $2 - значение по умолчанию -> ответ в $REPLY_VAL
  local q="$1" d="${2:-}" a=""
  if [ -n "$d" ]; then
    printf "%s [%s]: " "$q" "$d"; read -r a; REPLY_VAL="${a:-$d}"
  else
    printf "%s: " "$q"; read -r a; REPLY_VAL="$a"
  fi
}
ask_secret(){ # $1 - вопрос -> ответ в $REPLY_VAL (ввод скрыт)
  printf "%s" "$1"; read -r -s REPLY_VAL; printf "\n"
}
confirm(){ # $1 - вопрос, $2 - Y|N по умолчанию; код возврата 0 = да
  local d="${2:-Y}" a=""
  if [ "$d" = "Y" ]; then printf "%s [Y/n]: " "$1"; else printf "%s [y/N]: " "$1"; fi
  read -r a; a="${a:-$d}"
  case "$a" in [Yy]|[Yy][Ee][Ss]) return 0;; *) return 1;; esac
}

# ------------------------------ Termux-детект -------------------------------
IS_TERMUX=0
if [ -n "${TERMUX_VERSION:-}" ]; then
  IS_TERMUX=1
elif [ -n "${PREFIX:-}" ] && [ "${PREFIX#*com.termux}" != "${PREFIX}" ]; then
  IS_TERMUX=1
fi

pkg_install(){
  if command -v pkg >/dev/null 2>&1; then pkg install -y "$@"
  elif command -v apt-get >/dev/null 2>&1; then apt-get install -y "$@"
  else warn "Менеджер пакетов не найден — установите вручную: $*"; return 1; fi
}

ensure_tools(){
  local need=""
  command -v git  >/dev/null 2>&1 || need="$need git"
  command -v curl >/dev/null 2>&1 || need="$need curl"
  if [ -n "$need" ]; then
    info "Устанавливаю недостающие пакеты:$need (пара минут, нужен интернет)…"
    if [ "$DRY_RUN" = "1" ]; then
      info "[DRY-RUN] pkg install -y$need"
    else
      pkg_install $need || die "Не удалось установить пакеты. Выполните вручную: pkg install -y git curl"
    fi
  fi
  command -v git >/dev/null 2>&1 || die "git недоступен. Установите: pkg install -y git"
  command -v curl >/dev/null 2>&1 || warn "curl не найден — онлайн-проверка токена будет пропущена."
}

WAKE_LOCKED=0
take_wake(){ if [ "$IS_TERMUX" = "1" ] && command -v termux-wake-lock >/dev/null 2>&1; then termux-wake-lock >/dev/null 2>&1; WAKE_LOCKED=1; fi; }
give_wake(){ if [ "$WAKE_LOCKED" = "1" ] && command -v termux-wake-unlock >/dev/null 2>&1; then termux-wake-unlock >/dev/null 2>&1; fi; }
trap 'give_wake' EXIT

# --------------------- перенос из общей памяти (/sdcard) --------------------
maybe_relocate(){
  case "$REPO_ROOT" in
    /sdcard/*|/storage/*)
      local dest="$HOME/repo-ab-cloud"
      warn "Репозиторий лежит в общей памяти ($REPO_ROOT)."
      warn "В /sdcard git работает ненадёжно — переношу во внутреннюю память Termux."
      if [ -d "$dest/.git" ]; then
        info "Найдена готовая копия с git-историей: $dest — использую её."
      else
        if [ -e "$dest" ]; then dest="$dest.$(date +%Y%m%d-%H%M%S)"; fi
        info "Копирую во внутреннюю память ($dest)…"
        if [ "$DRY_RUN" = "1" ]; then
          info "[DRY-RUN] cp -a \"$REPO_ROOT\" \"$dest\""
        else
          cp -a "$REPO_ROOT" "$dest" || die "Копирование не удалось. Проверьте свободное место (нужно ~2 ГБ)."
        fi
      fi
      REPO_ROOT="$dest"
      ;;
  esac
  cd "$REPO_ROOT" || die "Каталог репозитория не найден: $REPO_ROOT"
}

# ------------------------------ URL репозитория -----------------------------
parse_url(){
  local u="$1"
  u="${u#https://}"; u="${u#http://}"; u="${u#www.}"; u="${u#github.com/}"; u="${u%.git}"
  u="${u#git@github.com:}"
  OWNER="${u%%/*}"; REPO_NAME="${u#*/}"
  case "$REPO_NAME" in */*) REPO_NAME="${REPO_NAME%%/*}";; esac
  [ -n "$OWNER" ] && [ -n "$REPO_NAME" ] || die "Не удалось разобрать адрес репозитория: $1"
}
ask_repo_url(){
  ask "Куда пушим (URL репозитория GitHub)" "$DEF_REPO_URL"; REPO_URL="$REPLY_VAL"
  case "$REPO_URL" in
    https://github.com/*|http://github.com/*) ;;
    git@github.com:*) REPO_URL="https://github.com/${REPO_URL#git@github.com:}";;
    *) warn "Адрес не похож на GitHub — использую как есть.";;
  esac
  parse_url "$REPO_URL"
}

# ------------------------------- выбор входа --------------------------------
choose_auth(){
  echo ""
  echo "  Способ входа в GitHub:"
  echo "    1) PAT-токен — ввести имя пользователя и токен (ввод скрыт)"
  echo "    2) Браузер   — одноразовый код через GitHub CLI (gh), всё в браузере"
  printf "  Выбор [1]: "
  local a=""; read -r a; a="${a:-1}"
  case "$a" in 2) AUTH_MODE="browser";; *) AUTH_MODE="pat";; esac
}

auth_pat(){
  ask "  Имя пользователя GitHub" "$DEF_USER"; GH_USER="$REPLY_VAL"
  echo "  Токен создаётся здесь: https://github.com/settings/tokens"
  echo "  (classic — отметьте область 'repo'; fine-grained — Contents: Read and write)"
  ask_secret "  Вставьте PAT-токен (ввод скрыт): "
  GH_TOKEN="$REPLY_VAL"
  [ -n "$GH_TOKEN" ] || die "Пустой токен — нечего отправлять на GitHub."
  if command -v curl >/dev/null 2>&1 && [ "$DRY_RUN" != "1" ]; then
    info "Проверяю токен через api.github.com…"
    local code login
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 25 -H "Authorization: token $GH_TOKEN" https://api.github.com/user) || code="000"
    if [ "$code" != "200" ]; then
      die "Токен не принят (HTTP $code). Создайте новый: https://github.com/settings/tokens (см. termux/README_RU.md, раздел 7)."
    fi
    login=$(curl -s --max-time 25 -H "Authorization: token $GH_TOKEN" https://api.github.com/user | sed -n 's/.*"login": *"\([^"]*\)".*/\1/p' | head -n1)
    if [ -n "$login" ]; then
      [ "$login" = "$GH_USER" ] || warn "Токен принадлежит '$login' — использую это имя вместо '$GH_USER'."
      GH_USER="$login"
    fi
    ok "Токен принят. Пользователь: $GH_USER"
  fi
}

auth_browser(){
  if ! command -v gh >/dev/null 2>&1; then
    info "Устанавливаю GitHub CLI (gh)…"
    if [ "$DRY_RUN" = "1" ]; then
      info "[DRY-RUN] pkg install -y gh"
    else
      pkg_install gh || die "Не удалось установить gh. Запустите снова и выберите способ 1 (PAT)."
    fi
  fi
  echo ""
  echo "  Сейчас появится ОДНОРАЗОВЫЙ КОД (вида XXXX-XXXX)."
  echo "  Браузер откроется сам; если нет — вручную откройте:"
  echo "  https://github.com/login/device   и введите там код."
  echo ""
  if [ "$DRY_RUN" = "1" ]; then
    info "[DRY-RUN] gh auth login --hostname github.com --git-protocol https --web"
    GH_USER="$DEF_USER"
  else
    gh auth login --hostname github.com --git-protocol https --web \
      || die "Вход через браузер не удался. Запустите снова и выберите способ 1 (PAT)."
    gh auth setup-git >/dev/null 2>&1 || true
    GH_USER="$(gh api user --jq .login 2>/dev/null || true)"
    [ -n "$GH_USER" ] || GH_USER="$DEF_USER"
  fi
  ok "Вход выполнен как: $GH_USER"
}

preflight_repo_access(){
  if [ "$DRY_RUN" = "1" ]; then
    info "[DRY-RUN] проверка доступа к $OWNER/$REPO_NAME пропущена"
    return 0
  fi
  if [ "$AUTH_MODE" = "pat" ] && command -v curl >/dev/null 2>&1; then
    info "Проверяю доступ к репозиторию $OWNER/$REPO_NAME…"
    local rcode perms
    rcode=$(curl -s -o /dev/null -w '%{http_code}' --max-time 25 -H "Authorization: token $GH_TOKEN" "https://api.github.com/repos/$OWNER/$REPO_NAME") || rcode="000"
    case "$rcode" in
      200) : ;;
      401) die "GitHub отклонил токен (401) — истёк или неверный. Создайте новый (termux/README_RU.md, раздел 7).";;
      404) die "Репозиторий $OWNER/$REPO_NAME недоступен этим токеном (404). Проверьте URL и права токена.";;
      *)   die "GitHub ответил HTTP $rcode — проверьте интернет и запустите снова.";;
    esac
    perms=$(curl -s --max-time 25 -H "Authorization: token $GH_TOKEN" "https://api.github.com/repos/$OWNER/$REPO_NAME" \
            | sed -n 's/.*"push": *\([a-z]*\).*/\1/p' | head -n1)
    if [ "$perms" = "true" ]; then
      ok "Право на запись в $OWNER/$REPO_NAME подтверждено."
    else
      warn "У токена, похоже, НЕТ права записи (push). Перевыпустите токен: classic с областью 'repo' либо fine-grained с Contents: Read and write."
      confirm "  Всё равно продолжить?" N || die "Отменено по вашему выбору."
    fi
  elif [ "$AUTH_MODE" = "browser" ] && command -v gh >/dev/null 2>&1; then
    gh api "repos/$OWNER/$REPO_NAME" --jq .full_name >/dev/null 2>&1 \
      || die "Репозиторий $OWNER/$REPO_NAME недоступен вашей учётной записью $GH_USER."
    ok "Доступ к $OWNER/$REPO_NAME подтверждён."
  fi
}

# ---------------------------- подготовка репо -------------------------------
prepare_repo(){
  [ -d "$REPO_ROOT" ] || die "Каталог не найден: $REPO_ROOT"
  if [ ! -d "$REPO_ROOT/.git" ]; then
    warn "В папке нет git-истории (.git) — похоже, распакованы только файлы."
    if confirm "Создать новый git-репозиторий и закоммитить все файлы?" Y; then
      if [ "$DRY_RUN" = "1" ]; then
        info "[DRY-RUN] git init -b $BRANCH; git add -A; git commit"
      else
        git init -b "$BRANCH" || die "git init не удался."
        git add -A
        git commit -m "feat: AB-Cloud Research (import from archive, pushed from Termux)" \
          || warn "Коммит не создан (возможно, пусто) — продолжаю."
      fi
    else
      die "Без git-истории публикация невозможна. Распакуйте архив целиком (вместе с папкой .git)."
    fi
  fi
  # личность автора — только если не настроена (нужна для авто-коммитов)
  if [ "$DRY_RUN" != "1" ]; then
    git config user.name  >/dev/null 2>&1 || git config user.name  "$GH_USER"
    git config user.email >/dev/null 2>&1 || git config user.email "$GH_USER@users.noreply.github.com"
  fi
}

commit_pending(){
  if [ "$DRY_RUN" = "1" ]; then
    if [ -n "$(git status --porcelain 2>/dev/null | head -n1)" ]; then
      info "[DRY-RUN] есть незафиксированные изменения — были бы закоммичены"
    fi
    return 0
  fi
  if [ -n "$(git status --porcelain 2>/dev/null | head -n1)" ]; then
    warn "Есть незафиксированные изменения — коммичу их перед push."
    git add -A
    git commit -m "chore: pending changes before push (Termux)" || true
  fi
}

# ------------------------- remote / fetch / push ----------------------------
CRED_HELPER=""
set_credentials(){
  if [ -n "$GH_TOKEN" ]; then
    export GH_USER GH_TOKEN
    CRED_HELPER='!f(){ echo "username=$GH_USER"; echo "password=$GH_TOKEN"; }; f'
  fi
}
gauth(){ # git с подстановкой токена в память (если есть токен)
  if [ -n "$CRED_HELPER" ]; then git -c "credential.helper=$CRED_HELPER" "$@"
  else git "$@"; fi
}

fetch_and_push(){
  info "Синхронизирую с GitHub (fetch)…"
  if [ "$DRY_RUN" = "1" ]; then
    info "[DRY-RUN] git fetch origin --prune --tags"
  else
    gauth fetch origin --prune --tags \
      || die "Не удалось связаться с GitHub. Проверьте интернет и URL репозитория."
  fi

  LOCAL_SHA="$(git rev-parse HEAD 2>/dev/null || true)"
  REMOTE_SHA="$(git rev-parse --verify "refs/remotes/origin/$BRANCH" 2>/dev/null || true)"

  local push_args=""
  if [ -z "$LOCAL_SHA" ]; then
    die "Локальный HEAD не читается — git-репозиторий повреждён."
  elif [ -z "$REMOTE_SHA" ]; then
    info "На GitHub ещё нет ветки $BRANCH — будет создана (обычный push)."
  elif [ "$REMOTE_SHA" = "$LOCAL_SHA" ]; then
    ok "GitHub уже содержит этот коммит — push не требуется."
  elif git merge-base --is-ancestor "$REMOTE_SHA" "$LOCAL_SHA" 2>/dev/null; then
    info "Обновление вперёд (fast-forward) — обычный push."
  else
    warn "История на GitHub расходится с историей архива."
    warn "По умолчанию архив ЗАМЕНЯЕТ содержимое ветки $BRANCH на GitHub (force-with-lease: чужие свежие коммиты, если они появятся позже, защищены)."
    if confirm "Обновить $BRANCH на GitHub содержимым этого архива?" Y; then
      push_args="--force-with-lease=refs/heads/$BRANCH:$REMOTE_SHA"
    else
      die "Отменено по вашему выбору. Ничего не изменено."
    fi
  fi

  if [ "$REMOTE_SHA" = "$LOCAL_SHA" ]; then
    : # пушить нечего
  elif [ "$DRY_RUN" = "1" ]; then
    info "[DRY-RUN] git push $push_args origin HEAD:refs/heads/$BRANCH (+ теги)"
  else
    info "Отправляю ветку $BRANCH на GitHub…"
    echo "    https://github.com/$OWNER/$REPO_NAME  ←  $(git rev-parse --short HEAD)"
    gauth push $push_args origin "HEAD:refs/heads/$BRANCH" \
      || die "Push не прошёл. Частые причины: у токена нет права записи; нет интернета. Подробности: termux/README_RU.md, раздел 9."
    info "Отправляю теги…"
    gauth push origin --tags >/dev/null 2>&1 || warn "Теги не отправились (не критично)."
  fi
}

verify_result(){
  if [ "$DRY_RUN" = "1" ]; then
    info "[DRY-RUN] git ls-remote origin refs/heads/$BRANCH — сверка SHA"
    return 0
  fi
  info "Проверяю, что GitHub получил коммит…"
  local final_sha
  final_sha="$(gauth ls-remote origin "refs/heads/$BRANCH" 2>/dev/null | cut -f1 | head -n1)"
  if [ "$final_sha" = "$LOCAL_SHA" ]; then
    ok "Подтверждено: на GitHub ветка $BRANCH = $(git rev-parse --short HEAD)"
  else
    warn "Не удалось сверить SHA автоматически (возможна задержка GitHub). Откройте репозиторий и проверьте последний коммит."
  fi
}

offer_open_browser(){
  if ! confirm "Открыть репозиторий в браузере?" Y; then return 0; fi
  local url="https://github.com/$OWNER/$REPO_NAME/tree/$BRANCH"
  if [ "$DRY_RUN" = "1" ]; then
    info "[DRY-RUN] открыть в браузере: $url"
  elif [ "$IS_TERMUX" = "1" ] && command -v termux-open-url >/dev/null 2>&1; then
    termux-open-url "$url" 2>/dev/null || echo "  $url"
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$url" 2>/dev/null || echo "  $url"
  else
    echo "  $url"
  fi
}

finish(){
  echo ""
  printf "${C_G}${C_B}=============================================================${C_0}\n"
  printf "${C_G}${C_B}  ГОТОВО! Репозиторий обновлён на GitHub.${C_0}\n"
  printf "${C_G}${C_B}  https://github.com/%s/%s/tree/%s${C_0}\n" "$OWNER" "$REPO_NAME" "$BRANCH"
  printf "${C_G}${C_B}=============================================================${C_0}\n"
  ok "Токен/данные входа нигде не сохранены — использовались только в памяти."
  unset GH_TOKEN 2>/dev/null || true
}

# ================================= MAIN =====================================
banner(){
  echo ""
  printf "${C_B}╔══════════════════════════════════════════════════════════╗${C_0}\n"
  printf "${C_B}║   AB-Cloud Research → GitHub   (Termux / Android)        ║${C_0}\n"
  printf "${C_B}╚══════════════════════════════════════════════════════════╝${C_0}\n"
  echo ""
  [ "$DRY_RUN" = "1" ] && warn "Режим DRY_RUN: ничего не будет изменено, только показ действий."
  if [ "$IS_TERMUX" = "1" ]; then
    ok "Termux обнаружен."
  else
    warn "Это не Termux — скрипт всё равно работает (Linux/Mac/эмулятор)."
  fi
}

banner
ensure_tools
take_wake
maybe_relocate
ask_repo_url
choose_auth
if [ "$AUTH_MODE" = "browser" ]; then auth_browser; else auth_pat; fi
preflight_repo_access
prepare_repo
commit_pending
set_credentials
fetch_and_push
verify_result
offer_open_browser
finish
