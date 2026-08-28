# ==============================================================================
# AB-Cloud Verification Suite — R Implementation (Bilingual: EN/RU)
# ==============================================================================
# Verifies three key objections against Riemann zeta zero data:
#   Objection 1: b(N) convergence  (Gram-point deviation via Lambert W)
#   Objection 2: GUE spacing KS test
#   Objection 3: Large-T decay slope ≈ -0.5
# ==============================================================================

# --- Bilingual message tables ------------------------------------------------

MSG <- list(
  en = list(
    header       = "AB-Cloud Verification Suite — R",
    separator    = "──────────────────────────────────────────────────────",
    loading      = "Loading zeros from: %s",
    loaded       = "Loaded %d zeros from %s",
    obj1_title   = "Objection 1: b(N) Convergence",
    obj1_desc    = "b(N) = (1/N) * Σ|γ_k - γ̃_k|, Gram points via Lambert W",
    obj1_n       = "N",
    obj1_bN      = "b(N)",
    obj1_status  = "Status",
    obj1_converge = "CONVERGING — b(N) → 0 supports AB-Cloud",
    obj1_stable  = "STABLE — b(N) near zero, AB-Cloud consistent",
    obj1_diverge = "DIVERGING — b(N) not → 0, objection upheld",
    obj2_title   = "Objection 2: GUE Spacing KS Test",
    obj2_desc    = "s_k = (γ_{k+1}-γ_k)·log(γ_k/2π)/(2π), vs p(s)=(πs/2)·exp(-πs²/4)",
    obj2_stat    = "D-statistic",
    obj2_pval    = "p-value",
    obj2_result  = "Result",
    obj2_pass    = "PASS — GUE spacing confirmed (p > 0.05)",
    obj2_fail    = "FAIL — GUE spacing rejected (p ≤ 0.05)",
    obj3_title   = "Objection 3: Large-T Decay Slope",
    obj3_desc    = "Linear regression of log|γ_k - γ̃_k| vs log(γ_k), expect slope ≈ -0.5",
    obj3_slope   = "Slope",
    obj3_stderr  = "Std Error",
    obj3_target  = "Target",
    obj3_result  = "Result",
    obj3_pass    = "PASS — Slope ≈ -0.5, AB-Cloud decay confirmed",
    obj3_fail    = "FAIL — Slope deviates from -0.5",
    no_data      = "ERROR: No zeros loaded. Check data directory.",
    done         = "Verification complete.",
    usage        = "Usage: source('ab_cloud_verify.R'); ab_cloud_verify(dataDir, zeros, source, objection, lang)"
  ),
  ru = list(
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
    done         = "Проверка завершена.",
    usage        = "Использование: source('ab_cloud_verify.R'); ab_cloud_verify(dataDir, zeros, source, objection, lang)"
  )
)

# --- Lambert W (principal branch) via Newton iteration -----------------------

lambert_W0 <- function(x, tol = 1e-12, max_iter = 50) {
  # Compute W_0(x) using Halley's method
  if (x == 0) return(0)
  w <- if (x > 1) log(x) - log(log(x)) else x  # initial guess
  for (i in seq_len(max_iter)) {
    ew  <- exp(w)
    f   <- w * ew - x
    fp  <- ew * (1 + w)
    fpp <- ew * (2 + w)
    # Halley step
    w <- w - (2 * f * fp) / (2 * fp * fp - f * fpp)
    if (abs(f) < tol * abs(x + 1)) break
  }
  return(w)
}

# --- Gram point computation via Lambert W ------------------------------------

gram_point <- function(n) {
  # γ̃_n ≈ 2πn / W(n/e)
  if (n <= 0) return(0)
  val <- 2 * pi * n / lambert_W0(n / exp(1))
  # One Newton refinement using exact θ(t)
  for (iter in 1:3) {
    theta <- 0.5 * val * log(val / (2 * pi)) - 0.5 * val - pi / 8
    dtheta <- 0.5 * log(val / (2 * pi))
    val <- val + (pi * n - theta) / dtheta
  }
  return(val)
}

gram_points_vec <- function(n_vec) {
  sapply(n_vec, gram_point)
}

# --- GUE spacing distribution (Wigner surmise) -------------------------------

gue_cdf <- function(s) {
  # CDF of p(s) = (πs/2)·exp(-πs²/4)
  1 - exp(-pi * s^2 / 4)
}

# --- Load zeros from data files ----------------------------------------------

load_zeros <- function(dataDir, count = 0, source = "auto") {
  # File selection priority
  files <- list(
    zeta_zeros_50000      = file.path(dataDir, "zeta_zeros_50000.txt"),
    zeta_zeros_500k       = file.path(dataDir, "zeta_zeros_500k_odlyzko.txt"),
    zeta_zeros_2M         = file.path(dataDir, "zeta_zeros_2M_odlyzko.txt"),
    zeta_zeros_highT      = file.path(dataDir, "zeta_zeros_highT_blocks.txt"),
    zeros6                = file.path(dataDir, "zeros6.txt"),
    zeta_zeros_50000_csv  = file.path(dataDir, "zeta_zeros_50000.csv")
  )

  # Source override
  if (source != "auto" && source %in% names(files)) {
    selected <- files[[source]]
  } else {
    # Auto-select: largest available file that makes sense for count
    selected <- NULL
    for (nm in names(files)) {
      if (file.exists(files[[nm]])) {
        selected <- files[[nm]]
        src_name <- nm
        if (count > 0 && count <= 50000 && nm == "zeta_zeros_50000") break
      }
    }
  }
  if (is.null(selected) || !file.exists(selected)) {
    stop("No data file found in: ", dataDir)
  }

  cat(sprintf(MSG$en$loading, selected), "\n")

  # Read based on extension
  ext <- tools::file_ext(selected)
  zeros <- if (ext == "csv") {
    df <- read.csv(selected, comment.char = "#", header = FALSE)
    as.numeric(df[[1]])
  } else {
    # .txt files: skip comment lines (#), parse floats
    lines <- readLines(selected, warn = FALSE)
    lines <- lines[!grepl("^\\s*#", lines) & nzchar(trimws(lines))]
    vals <- as.numeric(trimws(lines))
    vals[!is.na(vals)]
  }

  if (count > 0 && count < length(zeros)) {
    zeros <- zeros[1:count]
  }

  cat(sprintf(MSG$en$loaded, length(zeros), basename(selected)), "\n")
  return(zeros)
}

# --- Objection 1: b(N) Convergence ------------------------------------------

objection_1 <- function(zeros, lang = "en") {
  M <- MSG[[lang]]
  N <- length(zeros)
  cat("\n", M$separator, "\n")
  cat(M$obj1_title, "\n")
  cat(M$obj1_desc, "\n")
  cat(M$separator, "\n\n")

  # Compute b(N) at several checkpoints
  checkpoints <- c(100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000)
  checkpoints <- checkpoints[checkpoints <= N]

  results <- data.frame(N = integer(), bN = numeric(), Status = character(),
                        stringsAsFactors = FALSE)

  prev_bN <- NA
  for (cp in checkpoints) {
    idx    <- 1:cp
    gram   <- gram_points_vec(idx)
    diffs  <- abs(zeros[idx] - gram)
    bN     <- mean(diffs)

    status <- if (is.na(prev_bN)) {
      "—"
    } else if (bN < prev_bN * 1.05) {
      "↓"
    } else {
      "↑"
    }
    results <- rbind(results, data.frame(N = cp, bN = bN, Status = status,
                                         stringsAsFactors = FALSE))
    prev_bN <- bN
  }

  # Print table
  cat(sprintf("%10s  %14s  %8s\n", M$obj1_n, M$obj1_bN, M$obj1_status))
  cat(sprintf("%10s  %14s  %8s\n", "──────────", "──────────────", "────────"))
  for (i in seq_len(nrow(results))) {
    cat(sprintf("%10d  %14.8f  %8s\n", results$N[i], results$bN[i], results$Status[i]))
  }

  # Final verdict
  final_bN <- results$bN[nrow(results)]
  verdict <- if (final_bN < 0.01) {
    M$obj1_converge
  } else if (final_bN < 0.5) {
    M$obj1_stable
  } else {
    M$obj1_diverge
  }
  cat("\n", verdict, "\n")
  return(results)
}

# --- Objection 2: GUE Spacing KS Test ----------------------------------------

objection_2 <- function(zeros, lang = "en") {
  M <- MSG[[lang]]
  N <- length(zeros)
  cat("\n", M$separator, "\n")
  cat(M$obj2_title, "\n")
  cat(M$obj2_desc, "\n")
  cat(M$separator, "\n\n")

  # Compute normalized spacings
  gammas <- zeros[1:(N - 1)]
  deltas <- zeros[2:N] - zeros[1:(N - 1)]
  log_fac <- log(gammas / (2 * pi)) / (2 * pi)
  s <- deltas * log_fac

  # Filter positive, finite spacings
  s <- s[is.finite(s) & s > 0]

  # Use R built-in ks.test against GUE CDF
  ks_result <- ks.test(s, gue_cdf)

  cat(sprintf("%18s: %.8f\n", M$obj2_stat, ks_result$statistic))
  cat(sprintf("%18s: %.6e\n", M$obj2_pval, ks_result$p.value))

  verdict <- if (ks_result$p.value > 0.05) M$obj2_pass else M$obj2_fail
  cat("\n", verdict, "\n")

  return(list(D = ks_result$statistic, p.value = ks_result$p.value))
}

# --- Objection 3: Large-T Decay Slope ----------------------------------------

objection_3 <- function(zeros, lang = "en") {
  M <- MSG[[lang]]
  N <- length(zeros)
  cat("\n", M$separator, "\n")
  cat(M$obj3_title, "\n")
  cat(M$obj3_desc, "\n")
  cat(M$separator, "\n\n")

  # Compute deviations |γ_k - γ̃_k| for upper half of data (large T)
  start <- max(1, floor(N * 0.5))
  idx   <- start:N
  gram  <- gram_points_vec(idx)
  dev   <- abs(zeros[idx] - gram)

  # Filter valid points
  valid <- is.finite(dev) & dev > 0
  log_gamma <- log(zeros[idx][valid])
  log_dev   <- log(dev[valid])

  # Linear regression: log|dev| ~ log(gamma)
  fit <- lm(log_dev ~ log_gamma)

  slope  <- coef(fit)[2]
  stderr <- summary(fit)$coefficients[2, 2]

  cat(sprintf("%18s: %.6f\n", M$obj3_slope, slope))
  cat(sprintf("%18s: %.6f\n", M$obj3_stderr, stderr))
  cat(sprintf("%18s: -0.5\n", M$obj3_target))

  verdict <- if (abs(slope - (-0.5)) < 0.15) M$obj3_pass else M$obj3_fail
  cat("\n", verdict, "\n")

  return(list(slope = slope, stderr = stderr))
}

# --- Main verification function ----------------------------------------------

ab_cloud_verify <- function(dataDir = "../data", zeros = 0, source = "auto",
                             objection = "all", lang = "en") {
  M <- MSG[[lang]]
  cat("\n", M$separator, "\n")
  cat(M$header, "\n")
  cat(M$separator, "\n")

  # Load zeros
  gammas <- load_zeros(dataDir, count = zeros, source = source)
  if (length(gammas) == 0) {
    cat(M$no_data, "\n")
    return(invisible(NULL))
  }

  # Run selected objections
  results <- list()
  if (objection %in% c("all", "1")) results$obj1 <- objection_1(gammas, lang)
  if (objection %in% c("all", "2")) results$obj2 <- objection_2(gammas, lang)
  if (objection %in% c("all", "3")) results$obj3 <- objection_3(gammas, lang)

  cat("\n", M$separator, "\n")
  cat(M$done, "\n\n")
  return(invisible(results))
}
