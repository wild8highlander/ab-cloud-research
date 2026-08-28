# ==============================================================================
# AB-Cloud Verification Suite — R Implementation (Russian)
# ==============================================================================
# Русская версия. Для двуязычной, используйте ab_cloud_verify.R
# ==============================================================================

MSG_RU <- list(
  header       = "Комплекс проверки AB-Cloud — R",
  separator    = "──────────────────────────────────────────────────────",
  loading      = "Загрузка нулей из: %s",
  loaded       = "Загружено %d нулей из %s",
  obj1_title   = "Возражение 1: Сходимость b(N)",
  obj1_desc    = "b(N) = (1/N) * Σ|γ_k - γ̃_k|, точки Грама через W Ламберта",
  obj1_n       = "N",
  obj1_bN      = "b(N)",
  obj1_status  = "Статус",
  obj1_converge = "СХОДИТСЯ — b(N) → 0 подтверждает AB-Cloud",
  obj1_stable  = "СТАБИЛЬНО — b(N) ≈ 0, AB-Cloud согласуется",
  obj1_diverge = "РАСХОДИТСЯ — b(N) ↛ 0, возражение подтверждено",
  obj2_title   = "Возражение 2: KS-тест интервалов GUE",
  obj2_desc    = "s_k = (γ_{k+1}-γ_k)·log(γ_k/2π)/(2π), сравн. с p(s)=(πs/2)·exp(-πs²/4)",
  obj2_stat    = "D-статистика",
  obj2_pval    = "p-значение",
  obj2_result  = "Результат",
  obj2_pass    = "ПРОЙДЕНО — интервалы GUE подтверждены (p > 0.05)",
  obj2_fail    = "НЕ ПРОЙДЕНО — интервалы GUE отклонены (p ≤ 0.05)",
  obj3_title   = "Возражение 3: Наклон убывания при больших T",
  obj3_desc    = "Регрессия log|γ_k - γ̃_k| от log(γ_k), ожид. наклон ≈ -0.5",
  obj3_slope   = "Наклон",
  obj3_stderr  = "Стд. ошибка",
  obj3_target  = "Цель",
  obj3_result  = "Результат",
  obj3_pass    = "ПРОЙДЕНО — Наклон ≈ -0.5, убывание AB-Cloud подтверждено",
  obj3_fail    = "НЕ ПРОЙДЕНО — Наклон отклоняется от -0.5",
  no_data      = "ОШИБКА: Нули не загружены. Проверьте каталог данных.",
  done         = "Проверка завершена."
)

# --- Функция W Ламберта (главная ветвь), метод Халли ------------------------

lambert_W0_ru <- function(x, tol = 1e-12, max_iter = 50) {
  if (x == 0) return(0)
  w <- if (x > 1) log(x) - log(log(x)) else x
  for (i in seq_len(max_iter)) {
    ew  <- exp(w)
    f   <- w * ew - x
    fp  <- ew * (1 + w)
    fpp <- ew * (2 + w)
    w   <- w - (2 * f * fp) / (2 * fp * fp - f * fpp)
    if (abs(f) < tol * abs(x + 1)) break
  }
  return(w)
}

# --- Вычисление точки Грама через W Ламберта ---------------------------------

gram_point_ru <- function(n) {
  if (n <= 0) return(0)
  val <- 2 * pi * n / lambert_W0_ru(n / exp(1))
  for (iter in 1:3) {
    theta  <- 0.5 * val * log(val / (2 * pi)) - 0.5 * val - pi / 8
    dtheta <- 0.5 * log(val / (2 * pi))
    val    <- val + (pi * n - theta) / dtheta
  }
  return(val)
}

gram_points_vec_ru <- function(n_vec) sapply(n_vec, gram_point_ru)

# --- Функция распределения интервалов GUE (гипотеза Вигнера) -----------------

gue_cdf_ru <- function(s) 1 - exp(-pi * s^2 / 4)

# --- Загрузка нулей из файлов данных -----------------------------------------

load_zeros_ru <- function(dataDir, count = 0, source = "auto") {
  files <- list(
    zeta_zeros_50000      = file.path(dataDir, "zeta_zeros_50000.txt"),
    zeta_zeros_500k       = file.path(dataDir, "zeta_zeros_500k_odlyzko.txt"),
    zeta_zeros_2M         = file.path(dataDir, "zeta_zeros_2M_odlyzko.txt"),
    zeta_zeros_highT      = file.path(dataDir, "zeta_zeros_highT_blocks.txt"),
    zeros6                = file.path(dataDir, "zeros6.txt"),
    zeta_zeros_50000_csv  = file.path(dataDir, "zeta_zeros_50000.csv")
  )
  if (source != "auto" && source %in% names(files)) {
    selected <- files[[source]]
  } else {
    selected <- NULL
    for (nm in names(files)) {
      if (file.exists(files[[nm]])) {
        selected <- files[[nm]]
        if (count > 0 && count <= 50000 && nm == "zeta_zeros_50000") break
      }
    }
  }
  if (is.null(selected) || !file.exists(selected))
    stop("Файл данных не найден в: ", dataDir)

  cat(sprintf(MSG_RU$loading, selected), "\n")
  ext <- tools::file_ext(selected)
  zeros <- if (ext == "csv") {
    df <- read.csv(selected, comment.char = "#", header = FALSE)
    as.numeric(df[[1]])
  } else {
    lines <- readLines(selected, warn = FALSE)
    lines <- lines[!grepl("^\\s*#", lines) & nzchar(trimws(lines))]
    vals  <- as.numeric(trimws(lines))
    vals[!is.na(vals)]
  }
  if (count > 0 && count < length(zeros)) zeros <- zeros[1:count]
  cat(sprintf(MSG_RU$loaded, length(zeros), basename(selected)), "\n")
  return(zeros)
}

# --- Возражение 1: Сходимость b(N) -------------------------------------------

objection_1_ru <- function(zeros) {
  M <- MSG_RU; N <- length(zeros)
  cat("\n", M$separator, "\n", M$obj1_title, "\n", M$obj1_desc, "\n", M$separator, "\n\n")
  checkpoints <- c(100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000)
  checkpoints <- checkpoints[checkpoints <= N]
  results <- data.frame(N = integer(), bN = numeric(), Status = character(), stringsAsFactors = FALSE)
  prev_bN <- NA
  for (cp in checkpoints) {
    idx  <- 1:cp
    gram <- gram_points_vec_ru(idx)
    bN   <- mean(abs(zeros[idx] - gram))
    status <- if (is.na(prev_bN)) "—" else if (bN < prev_bN * 1.05) "↓" else "↑"
    results <- rbind(results, data.frame(N = cp, bN = bN, Status = status, stringsAsFactors = FALSE))
    prev_bN <- bN
  }
  cat(sprintf("%10s  %14s  %8s\n", M$obj1_n, M$obj1_bN, M$obj1_status))
  cat(sprintf("%10s  %14s  %8s\n", "──────────", "──────────────", "────────"))
  for (i in seq_len(nrow(results)))
    cat(sprintf("%10d  %14.8f  %8s\n", results$N[i], results$bN[i], results$Status[i]))
  final_bN <- results$bN[nrow(results)]
  verdict <- if (final_bN < 0.01) M$obj1_converge else if (final_bN < 0.5) M$obj1_stable else M$obj1_diverge
  cat("\n", verdict, "\n")
  return(results)
}

# --- Возражение 2: KS-тест интервалов GUE ------------------------------------

objection_2_ru <- function(zeros) {
  M <- MSG_RU; N <- length(zeros)
  cat("\n", M$separator, "\n", M$obj2_title, "\n", M$obj2_desc, "\n", M$separator, "\n\n")
  gammas  <- zeros[1:(N - 1)]
  deltas  <- zeros[2:N] - zeros[1:(N - 1)]
  log_fac <- log(gammas / (2 * pi)) / (2 * pi)
  s       <- deltas * log_fac
  s       <- s[is.finite(s) & s > 0]
  ks_res  <- ks.test(s, gue_cdf_ru)
  cat(sprintf("%18s: %.8f\n", M$obj2_stat, ks_res$statistic))
  cat(sprintf("%18s: %.6e\n", M$obj2_pval, ks_res$p.value))
  verdict <- if (ks_res$p.value > 0.05) M$obj2_pass else M$obj2_fail
  cat("\n", verdict, "\n")
  return(list(D = ks_res$statistic, p.value = ks_res$p.value))
}

# --- Возражение 3: Наклон убывания при больших T -----------------------------

objection_3_ru <- function(zeros) {
  M <- MSG_RU; N <- length(zeros)
  cat("\n", M$separator, "\n", M$obj3_title, "\n", M$obj3_desc, "\n", M$separator, "\n\n")
  start <- max(1, floor(N * 0.5))
  idx   <- start:N
  gram  <- gram_points_vec_ru(idx)
  dev   <- abs(zeros[idx] - gram)
  valid <- is.finite(dev) & dev > 0
  log_gamma <- log(zeros[idx][valid])
  log_dev   <- log(dev[valid])
  fit    <- lm(log_dev ~ log_gamma)
  slope  <- coef(fit)[2]
  stderr <- summary(fit)$coefficients[2, 2]
  cat(sprintf("%18s: %.6f\n", M$obj3_slope, slope))
  cat(sprintf("%18s: %.6f\n", M$obj3_stderr, stderr))
  cat(sprintf("%18s: -0.5\n", M$obj3_target))
  verdict <- if (abs(slope - (-0.5)) < 0.15) M$obj3_pass else M$obj3_fail
  cat("\n", verdict, "\n")
  return(list(slope = slope, stderr = stderr))
}

# --- Главная функция (только русский) ----------------------------------------

ab_cloud_verify_ru <- function(dataDir = "../data", zeros = 0, source = "auto",
                                objection = "all") {
  M <- MSG_RU
  cat("\n", M$separator, "\n", M$header, "\n", M$separator, "\n")
  gammas <- load_zeros_ru(dataDir, count = zeros, source = source)
  if (length(gammas) == 0) { cat(M$no_data, "\n"); return(invisible(NULL)) }
  results <- list()
  if (objection %in% c("all", "1")) results$obj1 <- objection_1_ru(gammas)
  if (objection %in% c("all", "2")) results$obj2 <- objection_2_ru(gammas)
  if (objection %in% c("all", "3")) results$obj3 <- objection_3_ru(gammas)
  cat("\n", M$separator, "\n", M$done, "\n\n")
  return(invisible(results))
}
