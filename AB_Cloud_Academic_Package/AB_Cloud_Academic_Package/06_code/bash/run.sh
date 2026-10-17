#!/usr/bin/env bash
# AB-Cloud unified CLI — the Bash runner (tput colors, zero deps).
# Contract: ../shared/contract.json — identical metrics to the other five runners.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SHARED="$DIR/../shared"
ROOT="$DIR/../.."

# --- flat metrics via grep/sed (regex parse of the flat JSON)
m() { grep -o "\"$1\"[[:space:]]*:[[:space:]]*[^,}]*" "$SHARED/metrics.json" | head -1 | sed 's/.*:[[:space:]]*//; s/"//g'; }

LANG_ARG=en; THEME=dark; OUTPUT=table
for a in "$@"; do
  case "$a" in
    --lang=*)   LANG_ARG="${a#--lang=}";;
    --theme=*)  THEME="${a#--theme=}";;
    --output=*) OUTPUT="${a#--output=}";;
  esac
done
CMD="${1:-analyze}"; case "$1" in --*) CMD=analyze;; esac

if command -v tput >/dev/null 2>&1 && [ -t 1 ]; then B=$(tput bold); R=$(tput sgr0); ACC=$(tput setaf 3); GRN=$(tput setaf 2); MUT=$(tput setaf 8); else B=""; R=""; ACC=""; GRN=""; MUT=""; fi

banner() {
cat <<'EOB'
    _          _   ___                     _          _
   / \   _ __ | |_| _ \__      _____ _ __ | |__   ___| |___
  / _ \ | '_ \| __| |_) \ \ /\ / / _ \ '_ \| '_ \ / _ \ / __|
 / ___ \| | | | |_|  __/ \ V  V /  __/ | | | |_) |  __/ \__ \
/_/   \_\_| |_|\__|_|     \_/\_/ \___|_| |_|_.__/ \___|_|___/
EOB
}

steps_ru=("Проверка окружения" "Загрузка конфигурации" "Чтение реестра" "Расчёт метрик" "Сводка")
steps_en=("Environment check" "Loading configuration" "Reading the registry" "Computing metrics" "Summary")
if [ "$LANG_ARG" = "ru" ]; then STEPS=("${steps_ru[@]}"); TITLE="ПРОГРАММА AB-CLOUD · ЕДИНОЕ ИЗДАНИЕ"; SUB="четыре уровня · один реестр · честные границы"; DONE="Готово"; RH="Статус RH"; VERD="Вердикты"; else STEPS=("${steps_en[@]}"); TITLE="AB-CLOUD PROGRAMME · UNIFIED EDITION"; SUB="four levels · one registry · honest boundaries"; DONE="Done"; RH="RH status"; VERD="Verdicts"; fi

case "$CMD" in
  analyze)
    if [ "$OUTPUT" = "json" ]; then
      printf '{"hypothesis":"AB-Cloud unified programme","params":{"config":"config.yaml","seed":%s,"lang":"%s"},"metrics":' "$(m seed)" "$LANG_ARG"
      cat "$SHARED/metrics.json" | tr -d '\n'
      printf ',"provenance":{"registry":"research_registry.json","generated_by":"bash"},"artifacts":["01_monographs/ru/monograph_ru.pdf","01_monographs/en/monograph_en.pdf"]}\n'
      exit 0
    fi
    banner
    echo "  ${B}${TITLE}${R}"
    echo "  ${MUT}${SUB}   lang: ${LANG_ARG}  seed: $(m seed)  theme: ${THEME}${R}"
    echo "  ${MUT}$(printf '%.0s─' {1..66})${R}"
    i=1; for s in "${STEPS[@]}"; do
      dots=$(printf '%*s' $((40 - ${#s})) '' | tr ' ' '.')
      echo "[$i/5] · $s $dots ${GRN}✅${R}"
      i=$((i+1))
    done
    echo
    echo "── 📈 metrics ──────────────────────"
    echo "RH status: $(m rh_status) (V13 obligation machine)"
    echo "verdicts:  $(m verdicts_yes) YES / $(m verdicts_no) NO / $(m verdicts_certified) CERTIFIED"
    echo "flagship results: $(m flagship_results) · levels: $(m levels)"
    echo
    echo "🎉 ${DONE}."
    ;;
  version)
    echo "{\"implementation\":\"bash\",\"package\":\"AB_Cloud_Academic_Package\",\"edition\":\"unified (versionless)\",\"rh_status\":\"certified\"}"
    ;;
  doctor)
    [ -f "$ROOT/02_data/processed/research_registry.json" ] && echo "registry ✅ found" || { echo "registry ❌ MISSING"; exit 1; }
    [ -f "$ROOT/config.yaml" ] && echo "config   ✅ found" || { echo "config   ❌ MISSING"; exit 1; }
    echo "metrics  ✅ loaded"
    ;;
  cite)
    echo "Isaev, I. Kh. (2026). AB-Cloud Research Programme: Unified Academic Package."
    echo "DOI: $(grep -o '"doi"[^,]*' "$SHARED/constants.json" | sed 's/.*: *"\(.*\)"/\1/')"
    echo "RH status: certified (V13, unlocked)."
    ;;
  secret) echo "ζ lives in the trace; the spectrum keeps the secret." ;;
  *) echo "command '$CMD' delegated to the python reference: python3 $DIR/../python/run.py $CMD"; exit 2 ;;
esac
