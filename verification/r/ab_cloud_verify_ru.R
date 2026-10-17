# ==============================================================================
# AB-Cloud Verification Suite — R, THIN Russian wrapper (CANON_SPEC §10)
# ==============================================================================
# Закрепляет русский язык вывода и делегирует ВСЮ математику единственному
# каноническому ядру в ab_cloud_verify.R. Дублирования математики здесь нет —
# дублированные ядра и были причиной расползания старого комплекта.
#
# Usage:
#   source("ab_cloud_verify_ru.R")
#   ab_cloud_verify_ru()                                  # ../data, 50000 нулей
#   ab_cloud_verify_ru("../data", 50000, "auto", "all")   # позиционно ok
# Для командной строки используйте раннер:  Rscript run_verify.R --lang ru ...
# (обёртка только определяет точку входа с закреплённым языком).
# ==============================================================================

.abv_wrapper_dir <- local({
  fa <- commandArgs(trailingOnly = FALSE)
  fi <- fa[grepl("^--file=", fa)]
  d <- ""
  if (length(fi) > 0L) {
    p <- sub("^--file=", "", fi[1])
    if (nzchar(p)) d <- dirname(suppressWarnings(normalizePath(p, mustWork = FALSE)))
  }
  d
})

.abv_main_file <- if (nzchar(.abv_wrapper_dir)) {
  file.path(.abv_wrapper_dir, "ab_cloud_verify.R")
} else {
  "ab_cloud_verify.R"   # интерактивный source() — ищем в текущем каталоге
}
if (!file.exists(.abv_main_file)) {
  stop("ab_cloud_verify_ru.R: \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d ab_cloud_verify.R \u0440\u044f\u0434\u043e\u043c \u0441 \u044d\u0442\u0438\u043c \u0444\u0430\u0439\u043b\u043e\u043c",
       if (nzchar(.abv_wrapper_dir))
         paste0(" (\u0438\u0441\u043a\u0430\u043b \u0432: ", .abv_wrapper_dir, ")")
       else " (\u0438\u0441\u043a\u0430\u043b \u0432 \u0442\u0435\u043a\u0443\u0449\u0435\u043c \u0440\u0430\u0431\u043e\u0447\u0435\u043c \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0435)",
       ". \u0417\u0430\u043f\u0443\u0441\u043a\u0430\u0439\u0442\u0435 \u0438\u0437 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430 verification/r/ \u0438\u043b\u0438 \u0447\u0435\u0440\u0435\u0437 Rscript.")
}
source(.abv_main_file)

# Точка входа с закреплённым языком: параметр 'lang' сознательно отсутствует —
# обёртка принудительно передаёт lang = "ru" в каноническое ядро.
ab_cloud_verify_ru <- function(dataDir = NULL, zeros = 50000, source = "auto",
                               objection = "all", selfcheck = TRUE) {
  ab_cloud_verify(dataDir = dataDir, zeros = zeros, source = source,
                  objection = objection, lang = "ru", selfcheck = selfcheck)
}
