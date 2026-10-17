# ==============================================================================
# AB-Cloud Verification Suite — R kernel (bilingual EN/RU)
# ==============================================================================
# Canon: verification/CANON_SPEC.md (v3.0). Bit-compatible with the frozen
# golden reference data/abcloud_golden.json (meridian-spectral-observatory,
# selftest 199/199, Julia 1.10.9, first 50 000 Odlyzko zeros).
#
# Verifies three reviewer objections against actual Riemann zeta zeros:
#   1. Numerical stability of b(N) convergence
#   2. GUE spacing statistical significance (KS + Cramer-von Mises + AD + <r>)
#   3. Large-T decay rate O(1/sqrt(N))
#
# A frozen-anchor self-check (CANON_SPEC §8) runs FIRST; every verdict below
# is printed only in the branch chosen by the computed numbers — no canned
# verdict strings. The CLI runner run_verify.R exits with status 1 if any
# anchor fails.
#
# Base R only (no CRAN packages). The Lambert-W / theta-Newton kernels are
# vectorized across the k vector; the per-element operation order is IDENTICAL
# to the scalar pseudocode of CANON_SPEC §1–§2, so results are bit-compatible
# and the 50000-zero self-check finishes in seconds instead of minutes.
#
# Usage:
#   source("ab_cloud_verify.R")
#   results <- ab_cloud_verify()                                # ../data, 50000 zeros
#   results <- ab_cloud_verify(dataDir = "../data", zeros = 50000,
#                              source = "auto", objection = "all",
#                              lang = "en", selfcheck = TRUE)
# ==============================================================================

# ------------------------------------------------------------------------------
# Module state: script directory + lazily-built GUE interpolation table cache
# ------------------------------------------------------------------------------

.ABV <- new.env(parent = emptyenv())
.ABV$gue_tbl <- NULL   # 32768-point table, built once on first gue_cdf() call

.ABV$script_dir <- local({
  fa <- commandArgs(trailingOnly = FALSE)
  fi <- fa[grepl("^--file=", fa)]
  d <- ""
  if (length(fi) > 0L) {
    p <- sub("^--file=", "", fi[1])
    if (nzchar(p)) d <- dirname(suppressWarnings(normalizePath(p, mustWork = FALSE)))
  }
  d
})

# ------------------------------------------------------------------------------
# Bilingual message catalogs (sprintf format strings; %% escapes a literal %)
# ------------------------------------------------------------------------------

.msg_en <- function() list(
  loading         = "Loading %d zeros from '%s' ...\n",
  loaded          = "Loaded %d zeros from '%s'  |  T \u2208 [%.4f, %.4f]\n",
  auto_select     = "Auto-selected '%s' (needs \u2265%d zeros, file has %d)\n",
  file_not_found  = "ERROR: Data file not found: '%s'\n",
  no_source       = "ERROR: No data source available for %d zeros\n",
  obj1_title      = "Objection 1: Numerical Stability of b(N)",
  obj1_converge   = "Convergence table \u2014 b(N) = (1/N) \u03a3|\u03b3_k \u2212 \u03b3\u0303_k|",
  obj1_fit        = "Empirical law:  b(N) \u2248 %.4f \u00b7 N^(\u2212%.4f)   (R\u00b2 = %.4f)\n",
  obj1_honest     = "  b(N) decreases monotonically over the table \u2014 convergence confirmed\n  on the accessible range. The decay is EMPIRICAL, not O(1/\u221aN) (see Objection 3).\n",
  obj1_notmono    = "  b(N) is NOT monotonically decreasing over this table \u2014 convergence NOT\n  confirmed on the accessible range (honest verdict).\n",
  obj2_title      = "Objection 2: GUE Spacing Statistical Significance",
  obj2_mean       = "  Spacing mean: %.9f  var: %.9f  (n = %d)\n",
  obj2_ks         = "  Kolmogorov-Smirnov:  D = %.6f,  p-value = %.6f\n",
  obj2_cvm        = "  Cram\u00e9r-von Mises:    W\u00b2 = %.6f\n",
  obj2_ad         = "  Anderson-Darling:   A\u00b2 = %.6f\n",
  obj2_rmean      = "  \u27e8r\u27e9 (adjacent-ratio): %.6f  (n = %d, GUE surmise \u2248 0.5992)\n",
  obj2_result     = "  H\u2080 (GUE distribution): %s  (\u03b1 = 0.05)\n",
  obj2_reject     = "REJECTED",
  obj2_not_reject = "NOT REJECTED",
  obj2_note       = "  Note: at large n the exact GUE surmise is formally rejected \u2014 the\n  known finite-T corrections of the zeta zeros, not a data artifact\n  (mean \u2248 1 validates the unfolding; golden-anchored).\n",
  obj3_title      = "Objection 3: Large-T Decay Rate",
  obj3_fit        = "  Linear fit  log(b(N)) = %.4f \u00b7 log(N) + %.4f\n",
  obj3_expected   = "  Expected slope \u2248 \u22120.5  (b(N) = O(1/\u221aN))\n",
  obj3_ci         = "  95%% CI for slope: [%.4f, %.4f]\n",
  obj3_verdict    = "  Slope %.4f is %s \u22120.5 \u00b1 0.1 \u2192 %s\n",
  obj3_consistent    = "CONSISTENT with O(1/\u221aN)",
  obj3_inconsistent  = "INCONSISTENT with O(1/\u221aN)",
  obj3_within     = "within",
  obj3_outside    = "outside",
  selfcheck_title = "Golden self-check \u2014 frozen anchors (canon: meridian-spectral-observatory, selftest 199/199)",
  selfcheck_line  = "  %-24s %s  computed = %.12g, expected = %.12g, \u0394 = %.3e\n",
  selfcheck_ok    = "PASS",
  selfcheck_bad   = "FAIL",
  selfcheck_skip  = "  %-24s SKIP  (needs %d zeros, have %d)\n",
  selfcheck_result = "  Self-check: %d passed, %d failed\n",
  summary         = "Verification Summary",
  summary_line    = "  Objection %s: %s\n",
  pass_           = "PASS",
  fail            = "FAIL",
  warn            = "WARN"
)

.msg_ru <- function() list(
  loading         = "\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 %d \u043d\u0443\u043b\u0435\u0439 \u0438\u0437 '%s' ...\n",
  loaded          = "\u0417\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043e %d \u043d\u0443\u043b\u0435\u0439 \u0438\u0437 '%s'  |  T \u2208 [%.4f, %.4f]\n",
  auto_select     = "\u0410\u0432\u0442\u043e-\u0432\u044b\u0431\u043e\u0440 '%s' (\u043d\u0443\u0436\u043d\u043e \u2265%d \u043d\u0443\u043b\u0435\u0439, \u0444\u0430\u0439\u043b \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 %d)\n",
  file_not_found  = "\u041e\u0428\u0418\u0411\u041a\u0410: \u0424\u0430\u0439\u043b \u0434\u0430\u043d\u043d\u044b\u0445 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d: '%s'\n",
  no_source       = "\u041e\u0428\u0418\u0411\u041a\u0410: \u041d\u0435\u0442 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f %d \u043d\u0443\u043b\u0435\u0439\n",
  obj1_title      = "\u0412\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u0435 1: \u0427\u0438\u0441\u043b\u0435\u043d\u043d\u0430\u044f \u0443\u0441\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0441\u0442\u044c b(N)",
  obj1_converge   = "\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0441\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438 \u2014 b(N) = (1/N) \u03a3|\u03b3_k \u2212 \u03b3\u0303_k|",
  obj1_fit        = "\u042d\u043c\u043f\u0438\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0437\u0430\u043a\u043e\u043d:  b(N) \u2248 %.4f \u00b7 N^(\u2212%.4f)   (R\u00b2 = %.4f)\n",
  obj1_honest     = "  b(N) \u043c\u043e\u043d\u043e\u0442\u043e\u043d\u043d\u043e \u0443\u0431\u044b\u0432\u0430\u0435\u0442 \u043f\u043e \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u2014 \u0441\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0430\n  \u043d\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u043c \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0435. \u0423\u0431\u044b\u0432\u0430\u043d\u0438\u0435 \u042d\u041c\u041f\u0418\u0420\u0418\u0427\u0415\u0421\u041a\u041e\u0415, \u044d\u0442\u043e \u043d\u0435 O(1/\u221aN) (\u0441\u043c. \u0412\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u0435 3).\n",
  obj1_notmono    = "  b(N) \u041d\u0415 \u043c\u043e\u043d\u043e\u0442\u043e\u043d\u043d\u043e \u0443\u0431\u044b\u0432\u0430\u0435\u0442 \u043f\u043e \u044d\u0442\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u2014 \u0441\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u044c \u041d\u0415 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0430\n  \u043d\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u043c \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0435 (\u0447\u0435\u0441\u0442\u043d\u044b\u0439 \u0432\u0435\u0440\u0434\u0438\u043a\u0442).\n",
  obj2_title      = "\u0412\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u0435 2: \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u044c GUE-\u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f",
  obj2_mean       = "  \u0421\u0440\u0435\u0434\u043d\u0438\u0439 \u0441\u043f\u0435\u0439\u0441\u0438\u043d\u0433: %.9f  \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u044f: %.9f  (n = %d)\n",
  obj2_ks         = "  \u041a\u043e\u043b\u043c\u043e\u0433\u043e\u0440\u043e\u0432-\u0421\u043c\u0438\u0440\u043d\u043e\u0432:  D = %.6f,  p-\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 = %.6f\n",
  obj2_cvm        = "  \u041a\u0440\u0430\u043c\u0435\u0440-\u0444\u043e\u043d \u041c\u0438\u0437\u0435\u0441:    W\u00b2 = %.6f\n",
  obj2_ad         = "  \u0410\u043d\u0434\u0435\u0440\u0441\u043e\u043d-\u0414\u0430\u0440\u043b\u0438\u043d\u0433:     A\u00b2 = %.6f\n",
  obj2_rmean      = "  \u27e8r\u27e9 (\u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u0441\u043e\u0441\u0435\u0434\u043d\u0438\u0445): %.6f  (n = %d, GUE \u2248 0.5992)\n",
  obj2_result     = "  H\u2080 (GUE-\u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435): %s  (\u03b1 = 0.05)\n",
  obj2_reject     = "\u041e\u0422\u0412\u0415\u0420\u0413\u041d\u0423\u0422\u0410",
  obj2_not_reject = "\u041d\u0415 \u041e\u0422\u0412\u0415\u0420\u0413\u041d\u0423\u0422\u0410",
  obj2_note       = "  \u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435: \u043f\u0440\u0438 \u0431\u043e\u043b\u044c\u0448\u0438\u0445 n \u0442\u043e\u0447\u043d\u0430\u044f GUE-\u0441\u0443\u0440\u044c\u043c\u0438\u0434\u0430 \u0444\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e \u043e\u0442\u0432\u0435\u0440\u0433\u0430\u0435\u0442\u0441\u044f \u2014 \u044d\u0442\u043e\n  \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0435 \u043f\u043e\u043f\u0440\u0430\u0432\u043a\u0438 \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0445 T \u0443 \u043d\u0443\u043b\u0435\u0439 \u03b6, \u0430 \u043d\u0435 \u0434\u0435\u0444\u0435\u043a\u0442 \u0434\u0430\u043d\u043d\u044b\u0445\n  (\u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u2248 1 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u0435\u0442 \u0440\u0430\u0437\u0432\u0451\u0440\u0442\u043a\u0443; \u044f\u043a\u043e\u0440\u044f golden).\n",
  obj3_title      = "\u0412\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u0435 3: \u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044f \u043f\u0440\u0438 \u0431\u043e\u043b\u044c\u0448\u0438\u0445 T",
  obj3_fit        = "  \u041b\u0438\u043d\u0435\u0439\u043d\u0430\u044f \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f  log(b(N)) = %.4f \u00b7 log(N) + %.4f\n",
  obj3_expected   = "  \u041e\u0436\u0438\u0434\u0430\u0435\u043c\u044b\u0439 \u043d\u0430\u043a\u043b\u043e\u043d \u2248 \u22120.5  (b(N) = O(1/\u221aN))\n",
  obj3_ci         = "  95%% \u0414\u0418 \u0434\u043b\u044f \u043d\u0430\u043a\u043b\u043e\u043d\u0430: [%.4f, %.4f]\n",
  obj3_verdict    = "  \u041d\u0430\u043a\u043b\u043e\u043d %.4f %s \u22120.5 \u00b1 0.1 \u2192 %s\n",
  obj3_consistent    = "\u0421\u041e\u0413\u041b\u0410\u0421\u0423\u0415\u0422\u0421\u042f \u0441 O(1/\u221aN)",
  obj3_inconsistent  = "\u041d\u0415 \u0421\u041e\u0413\u041b\u0410\u0421\u0423\u0415\u0422\u0421\u042f \u0441 O(1/\u221aN)",
  obj3_within     = "\u0432\u043d\u0443\u0442\u0440\u0438",
  obj3_outside    = "\u0432\u043d\u0435",
  selfcheck_title = "\u0421\u0430\u043c\u043e-\u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 golden \u2014 \u0437\u0430\u043c\u043e\u0440\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u044f\u043a\u043e\u0440\u044f (\u043a\u0430\u043d\u043e\u043d: meridian-spectral-observatory, selftest 199/199)",
  selfcheck_line  = "  %-24s %s  \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043e = %.12g, \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0435 = %.12g, \u0394 = %.3e\n",
  selfcheck_ok    = "\u041f\u0420\u041e\u0419\u0414\u0415\u041d\u041e",
  selfcheck_bad   = "\u0421\u0411\u041e\u0419",
  selfcheck_skip  = "  %-24s \u041f\u0420\u041e\u041f\u0423\u0421\u041a  (\u043d\u0443\u0436\u043d\u043e %d \u043d\u0443\u043b\u0435\u0439, \u0435\u0441\u0442\u044c %d)\n",
  selfcheck_result = "  \u0421\u0430\u043c\u043e-\u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430: %d \u043f\u0440\u043e\u0439\u0434\u0435\u043d\u043e, %d \u043f\u0440\u043e\u0432\u0430\u043b\u0435\u043d\u043e\n",
  summary         = "\u0418\u0442\u043e\u0433\u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438",
  summary_line    = "  \u0412\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u0435 %s: %s\n",
  pass_           = "\u041f\u0420\u041e\u0419\u0414\u0415\u041d\u041e",
  fail            = "\u0421\u0411\u041e\u0419",
  warn            = "\u041f\u0420\u0415\u0414\u0423\u041f\u0420."
)

.get_msg <- function(lang) if (identical(lang, "ru")) .msg_ru() else .msg_en()

.detect_lang <- function() {
  l <- tolower(Sys.getenv("LANG"))
  if (grepl("ru", l, fixed = TRUE)) "ru" else "en"
}

# ------------------------------------------------------------------------------
# CANON_SPEC §1 — Lambert W, principal branch (Newton, up to 50 iterations,
# stop when |delta| < 1e-14*(1+|w|)).  Vectorized over x; per-element operation
# order is identical to the scalar pseudocode.
# Seed: w = log(x); w -= log(w) when w > 0.  Documented guard (matches the
# canonical Python kernel): when log(x) < 0 (0 < x < 1) the seed is w = x —
# the log seed sits exactly on the fp = 0 degeneracy at x = 1/e, which
# gram_point(1) hits.
# ------------------------------------------------------------------------------

.lambert_w_vec <- function(x) {
  x <- as.numeric(x)
  w <- rep(0.0, length(x))
  pos <- x > 0
  if (!any(pos)) return(w)
  xp <- x[pos]
  wp <- log(xp)
  neg <- wp < 0
  if (any(neg)) wp[neg] <- xp[neg]
  posw <- wp > 0
  if (any(posw)) wp[posw] <- wp[posw] - log(wp[posw])
  act <- rep(TRUE, length(xp))
  for (iter in seq_len(50L)) {
    idx <- which(act)
    if (length(idx) == 0L) break
    xi <- xp[idx]
    wi <- wp[idx]
    ew <- exp(wi)
    f  <- wi * ew - xi
    fp <- ew * (wi + 1.0)
    ok <- abs(fp) >= 1e-30
    delta <- rep(0.0, length(idx))
    delta[ok] <- f[ok] / fp[ok]
    wi[ok] <- wi[ok] - delta[ok]
    conv <- abs(delta) < 1e-14 * (1.0 + abs(wi))
    wp[idx] <- wi
    act[idx[conv]] <- FALSE
  }
  w[pos] <- wp
  w
}

# Scalar accessor (canon name).
lambert_w <- function(x) .lambert_w_vec(x)[1]

# ------------------------------------------------------------------------------
# CANON_SPEC §2 — Gram point. Seed t = 2*pi*k / W(k/e), then EXACTLY 8 Newton
# iterations on the 5-term Riemann–Siegel theta:
#   theta(t)  = (t/2)*ln(t/2pi) - t/2 - pi/8 + 1/(48t) + 7/(5760 t^3)
#   dtheta(t) = 0.5*ln(t/2pi) - 1/(48 t^2) - 21/(5760 t^4)
# Vectorized across k (8 passes over whole vectors; per-element arithmetic and
# per-element guard breaks are identical to the scalar canon).
# ------------------------------------------------------------------------------

.gram_points_vec <- function(k) {
  k <- as.numeric(k)
  t <- rep(0.0, length(k))
  pos <- k > 0
  if (!any(pos)) return(t)
  kp <- k[pos]
  tp <- 2.0 * pi * kp / .lambert_w_vec(kp / exp(1))
  for (iter in seq_len(8L)) {
    arg <- tp / (2.0 * pi)
    ok <- arg > 0
    if (!any(ok)) break
    idx <- which(ok)
    lg <- log(arg[idx])          # log applied only to positive args
    to <- tp[idx]
    theta  <- (to / 2.0) * lg - to / 2.0 - pi / 8.0 +
              1.0 / (48.0 * to) + 7.0 / (5760.0 * to * to * to)
    dtheta <- 0.5 * lg - 1.0 / (48.0 * to * to) -
              21.0 / (5760.0 * to * to * to * to)
    upd <- abs(dtheta) >= 1e-30
    tu  <- to[upd]
    tp[idx[upd]] <- tu - (theta[upd] - pi * kp[idx[upd]]) / dtheta[upd]
  }
  t[pos] <- tp
  t
}

# Scalar accessor (canon name).
gram_point <- function(k) .gram_points_vec(k)[1]

# ------------------------------------------------------------------------------
# CANON_SPEC §3 — b(N) with the exact sequential summation order.
# bn_prefix accumulates left-to-right; b(N) = pref[N+1]/N is bit-identical to
# the direct sum (CANON_SPEC §7 allows reusing the prefix for obj1/obj3).
# ------------------------------------------------------------------------------

.ssum <- function(v) {
  s <- 0.0
  for (x in v) s <- s + x
  s
}

bn_prefix <- function(z) {
  n <- length(z)
  pref <- numeric(n + 1L)
  pref[1L] <- 0.0
  if (n == 0L) return(pref)
  g <- .gram_points_vec(seq_len(n))
  acc <- 0.0
  for (kk in seq_len(n)) {
    acc <- acc + abs(z[kk] - g[kk])
    pref[kk + 1L] <- acc
  }
  pref
}

compute_bN <- function(z, N) {
  N <- as.integer(N)
  if (is.na(N) || N <= 0L || N > length(z)) return(NaN)
  g <- .gram_points_vec(seq_len(N))
  .ssum(abs(z[seq_len(N)] - g)) / N
}

compute_bN_offset <- function(z, N, offset) {
  N <- as.integer(N); offset <- as.integer(offset)
  if (is.na(N) || N <= 0L || offset + N > length(z)) return(NaN)
  g <- .gram_points_vec((offset + 1L):(offset + N))
  .ssum(abs(z[seq_len(N)] - g)) / N
}

# ------------------------------------------------------------------------------
# CANON_SPEC §4 — normalized spacings, in k order, only where z_k > 0.
# ------------------------------------------------------------------------------

spacings_of <- function(z) {
  n <- length(z)
  if (n < 2L) return(numeric(0))
  zk  <- z[seq_len(n - 1L)]
  zk1 <- z[2L:n]
  m <- zk > 0
  (zk1[m] - zk[m]) * log(zk[m] / (2.0 * pi)) / (2.0 * pi)
}

# ------------------------------------------------------------------------------
# CANON_SPEC §5 — GUE CDF (Wigner–Dyson beta=2 surmise) via the 32768-point
# interpolation table (SMAX = 5), built lazily once and cached in .ABV$gue_tbl.
#   exact(s) = erf(2s/sqrt(pi)) - (4s/pi)*exp(-4s^2/pi)
# R has no base erf: erf(x) = 2*pnorm(x*sqrt(2)) - 1 (documented deviation).
# R is 1-indexed: table[i] (0-based canon) is tbl[i+1], so the interpolation
# reads (1-t)*tbl[i+1] + t*tbl[i+2].
# ------------------------------------------------------------------------------

erf <- function(x) 2.0 * pnorm(x * sqrt(2.0)) - 1.0

.gue_exact <- function(s) {
  erf(2.0 * s / sqrt(pi)) - (4.0 * s / pi) * exp(-4.0 * s * s / pi)
}

gue_cdf <- function(s) {
  TN <- 32768L
  SMAX <- 5.0
  s <- as.numeric(s)
  out <- numeric(length(s))
  hi <- s >= SMAX
  if (any(hi)) out[hi] <- .gue_exact(s[hi])
  mid <- s > 0 & s < SMAX
  if (any(mid)) {
    if (is.null(.ABV$gue_tbl)) {
      .ABV$gue_tbl <- .gue_exact((0:(TN - 1L)) * SMAX / (TN - 1L))
    }
    tbl <- .ABV$gue_tbl
    sm <- s[mid]
    x  <- sm * (TN - 1L) / SMAX
    ii <- floor(x)
    bad <- ii < 0 | ii >= (TN - 1L)
    res <- rep(NA_real_, length(sm))
    if (any(bad)) res[bad] <- .gue_exact(sm[bad])
    good <- !bad
    ig <- ii[good]
    tg <- x[good] - ig
    res[good] <- (1.0 - tg) * tbl[ig + 1L] + tg * tbl[ig + 2L]
    out[mid] <- res
  }
  out
}

# ------------------------------------------------------------------------------
# CANON_SPEC §6 — statistics.
# ------------------------------------------------------------------------------

.ks_pvalue <- function(lam) {
  if (is.na(lam) || lam <= 0.0) return(1.0)
  if (lam < 0.6) {
    s2 <- 0.0
    for (kk in seq_len(1000L)) {
      term <- exp(-(((2.0 * kk - 1.0)^2) * (pi * pi)) / (8.0 * lam * lam))
      s2 <- s2 + term
      if (term < 1e-18) break
    }
    v <- 1.0 - sqrt(2.0 * pi) / lam * s2
  } else {
    ss <- 0.0
    sgn <- 1.0
    for (kk in seq_len(100L)) {
      term <- sgn * exp(-2.0 * kk * kk * lam * lam)
      ss <- ss + term
      sgn <- -sgn
      if (abs(term) < 1e-18) break
    }
    v <- 2.0 * ss
  }
  min(1.0, max(0.0, v))
}

ks_test <- function(sp) {
  n <- length(sp)
  if (n == 0L) return(list(D = 0.0, p = 1.0))
  ss <- sort(sp)
  Fv <- gue_cdf(ss)
  ii <- as.numeric(seq_len(n))
  d1 <- abs(ii / n - Fv)
  d2 <- abs((ii - 1.0) / n - Fv)
  D <- max(d1, d2)
  lam <- (sqrt(n) + 0.12 + 0.11 / sqrt(n)) * D
  list(D = D, p = .ks_pvalue(lam))
}

cvm_stat <- function(sp) {
  n <- length(sp)
  if (n == 0L) return(0.0)
  ss <- sort(sp)
  Fv <- gue_cdf(ss)
  W2 <- 1.0 / (12.0 * n)
  for (i in seq_len(n)) {
    W2 <- W2 + ((2.0 * i - 1.0) / (2.0 * n) - Fv[i])^2
  }
  W2
}

ad_stat <- function(sp) {
  n <- length(sp)
  if (n < 2L) return(NaN)
  ss <- sort(sp)
  Fv <- gue_cdf(ss)
  acc <- 0.0
  for (i in seq_len(n)) {
    Fi  <- min(max(Fv[i], 1e-300), 1.0 - 1e-16)
    Fni <- min(max(Fv[n + 1L - i], 1e-300), 1.0 - 1e-16)
    acc <- acc + (2.0 * i - 1.0) * (log(Fi) + log(1.0 - Fni))
  }
  -n - acc / n
}

adjacent_ratio <- function(z) {
  n <- length(z)
  if (n < 3L) return(list(r = NaN, n_r = 0L))
  d <- z[2L:n] - z[seq_len(n - 1L)]
  m <- n - 2L
  a <- d[seq_len(m)]
  b <- d[2L:(m + 1L)]
  keep <- !(a == 0.0 & b == 0.0)
  ak <- a[keep]
  bk <- b[keep]
  terms <- pmin(ak, bk) / pmax(ak, bk)
  cnt <- length(terms)
  if (cnt == 0L) return(list(r = NaN, n_r = 0L))
  list(r = .ssum(terms) / cnt, n_r = cnt)
}

.mean_var_s <- function(sp) {
  n <- length(sp)
  if (n == 0L) return(list(mean = NaN, var = NaN))
  mn <- .ssum(sp) / n
  vr <- if (n > 1L) .ssum((sp - mn)^2) / (n - 1L) else NaN
  list(mean = mn, var = vr)
}

# OLS with slope stderr se^2 = (SSres/(m-2)) * m / (m*Sxx - Sx^2) (spec §7).
.linreg <- function(x, y) {
  slope <- 0.0; intercept <- 0.0; se <- 0.0; r2 <- 0.0
  n <- length(x)
  if (n < 2L || length(y) != n) {
    return(list(slope = slope, intercept = intercept, se = se, r2 = r2))
  }
  sx <- 0.0; sy <- 0.0; sxx <- 0.0; sxy <- 0.0
  for (i in seq_len(n)) {
    sx  <- sx + x[i]
    sy  <- sy + y[i]
    sxx <- sxx + x[i] * x[i]
    sxy <- sxy + x[i] * y[i]
  }
  denom <- n * sxx - sx * sx
  if (abs(denom) < 1e-30) {
    return(list(slope = slope, intercept = intercept, se = se, r2 = r2))
  }
  slope     <- (n * sxy - sx * sy) / denom
  intercept <- (sy - slope * sx) / n
  ymean  <- sy / n
  ss_tot <- 0.0
  ss_res <- 0.0
  for (i in seq_len(n)) {
    ss_tot <- ss_tot + (y[i] - ymean)^2
    ss_res <- ss_res + (y[i] - (slope * x[i] + intercept))^2
  }
  r2  <- if (ss_tot > 0) 1.0 - ss_res / ss_tot else 0.0
  mse <- if (n > 2L) ss_res / (n - 2L) else 0.0
  se  <- if (denom > 0) sqrt(mse * n / denom) else 0.0
  list(slope = slope, intercept = intercept, se = se, r2 = r2)
}

# ------------------------------------------------------------------------------
# CANON_SPEC §9 — zero loader (source registry, auto = smallest file with
# avail >= count; sort ascending FIRST, then truncate).
# ------------------------------------------------------------------------------

.ABV$registry <- data.frame(
  name  = c("50k", "50k_full", "500k", "2M", "highT", "2M_gz", "csv", "zeros6"),
  file  = c("zeta_zeros_50000.txt", "zeta_zeros_50000_embedded.txt",
            "zeta_zeros_500k_odlyzko.txt", "zeta_zeros_2M_odlyzko.txt",
            "zeta_zeros_highT_blocks.txt", "zeta_zeros_2M_odlyzko.txt.gz",
            "zeta_zeros_50000.csv", "zeros6.txt"),
  avail = c(13661L, 50000L, 500000L, 2001052L, 30000L, 2001052L, 13661L, 2001052L),
  stringsAsFactors = FALSE
)

.parse_plain_lines <- function(lines) {
  s <- trimws(lines)
  keep <- nzchar(s) & !startsWith(s, "#")
  v <- suppressWarnings(as.numeric(s[keep]))
  v[!is.na(v)]
}

.parse_highT_lines <- function(lines) {
  # BLOCK-offset format: '# BLOCK index=... offset=BASE' headers set the base;
  # each value line is an offset from the current base.
  buf <- numeric(length(lines))
  cnt <- 0L
  base <- 0.0
  for (ln in lines) {
    s <- trimws(ln)
    if (!nzchar(s)) next
    if (startsWith(s, "#")) {
      if (grepl("BLOCK", s, fixed = TRUE)) {
        m <- regmatches(s, regexec("^#\\s*BLOCK\\s+index=\\S+\\s+offset=(\\S+)", s))
        if (length(m) == 1L && length(m[[1]]) >= 2L) {
          bb <- suppressWarnings(as.numeric(m[[1]][2]))
          if (!is.na(bb)) base <- bb
        }
      }
      next
    }
    v <- suppressWarnings(as.numeric(s))
    if (is.na(v)) next
    cnt <- cnt + 1L
    buf[cnt] <- base + v
  }
  if (cnt == 0L) numeric(0) else buf[seq_len(cnt)]
}

.parse_csv_lines <- function(lines) {
  # CSV columns: index,t,s_real,s_imag,zero_number — column 2 is t.
  buf <- numeric(length(lines))
  cnt <- 0L
  for (ln in lines) {
    s <- trimws(ln)
    if (!nzchar(s) || startsWith(s, "#")) next
    parts <- strsplit(s, ",", fixed = TRUE)[[1]]
    if (length(parts) < 2L) next
    v <- suppressWarnings(as.numeric(trimws(parts[2])))
    if (is.na(v)) next
    cnt <- cnt + 1L
    buf[cnt] <- v
  }
  if (cnt == 0L) numeric(0) else buf[seq_len(cnt)]
}

load_zeros <- function(dataDir, count = 50000, source = "auto", msg = NULL) {
  if (is.null(msg)) msg <- .get_msg(.detect_lang())
  count <- as.integer(count)
  reg <- .ABV$registry
  srcUsed <- ""

  if (identical(source, "auto")) {
    cand <- reg[reg$avail >= count, , drop = FALSE]
    if (nrow(cand) == 0L) {
      cat(sprintf(msg$no_source, count), file = stderr())
      return(list(zeros = numeric(0), source = ""))
    }
    k <- which.min(cand$avail)   # smallest avail; ties keep registry order
    srcUsed <- cand$name[k]
    fname   <- cand$file[k]
    cat(sprintf(msg$auto_select, srcUsed, count, cand$avail[k]))
  } else {
    k <- match(source, reg$name)
    if (is.na(k)) {
      cat(sprintf(msg$no_source, count), file = stderr())
      return(list(zeros = numeric(0), source = ""))
    }
    srcUsed <- reg$name[k]
    fname   <- reg$file[k]
  }

  filepath <- file.path(dataDir, fname)
  cat(sprintf(msg$loading, count, fname))

  if (!file.exists(filepath)) {
    cat(sprintf(msg$file_not_found, filepath), file = stderr())
    return(list(zeros = numeric(0), source = ""))
  }

  if (grepl("\\.gz$", fname)) {
    # gzipped plain table — read through a gzfile connection (base R).
    con <- gzfile(filepath, "rt")
    lines <- readLines(con, warn = FALSE)
    close(con)
    gammas <- .parse_plain_lines(lines)
  } else if (identical(source, "highT")) {
    gammas <- .parse_highT_lines(readLines(filepath, warn = FALSE))
  } else if (identical(source, "csv")) {
    gammas <- .parse_csv_lines(readLines(filepath, warn = FALSE))
  } else {
    gammas <- .parse_plain_lines(readLines(filepath, warn = FALSE))
  }

  gammas <- sort(gammas)
  if (count > 0L && count < length(gammas)) gammas <- gammas[seq_len(count)]

  if (length(gammas) > 0L) {
    cat(sprintf(msg$loaded, length(gammas), fname, gammas[1], gammas[length(gammas)]))
  }
  list(zeros = gammas, source = srcUsed)
}

# ------------------------------------------------------------------------------
# CANON_SPEC §7 — Objection 1: b(N) convergence table (prefix-based, the
# prefix/N values are bit-identical to the direct sums), empirical power-law
# fit, and the honest monotone-decrease verdict.
# ------------------------------------------------------------------------------

objection_1 <- function(z, pref, msg) {
  # Canon print order (CANON_SPEC §7 / canonical Python): '=', title, caption,
  # column header, then the '----' separator.
  cat(sprintf("\n%s\n%s\n%s\n", strrep("=", 60), msg$obj1_title,
              msg$obj1_converge))
  cat(sprintf("%10s  %20s  %20s\n", "N", "b(N)", "\u0394b = b(N)\u2212b(N/2)"))
  cat(sprintf("%s\n", strrep("-", 60)))

  n <- length(z)
  G <- c(100, 500, 1000, 5000, 10000, 50000)
  G <- G[G <= n]
  if (length(G) == 0L) G <- min(n, 100)

  bv <- numeric(length(G))
  prev <- NA_real_
  for (ci in seq_along(G)) {
    N <- G[ci]
    bN <- pref[N + 1L] / N
    bv[ci] <- bN
    ds <- if (is.na(prev)) "\u2014" else sprintf("%+.10f", bN - prev)
    cat(sprintf("%10d  %20.10f  %20s\n", as.integer(N), bN, ds))
    prev <- bN
  }

  # Optional empirical power-law fit on the printed grid (log-log OLS).
  slope <- NaN
  r2 <- 0.0
  keepG <- (G > 1) & (bv > 0)
  if (sum(keepG) >= 3L) {
    lr <- .linreg(log(G[keepG]), log(bv[keepG]))
    slope <- lr$slope
    r2 <- lr$r2
    cat(sprintf(msg$obj1_fit, exp(lr$intercept), -slope, r2))
  }

  # Honest convergence verdict: monotone decrease across the table.
  mono <- all(diff(bv) < 0)
  converged <- mono && length(bv) >= 3L
  if (converged) cat(msg$obj1_honest) else cat(msg$obj1_notmono)

  list(N_values = G, bN_values = bv, converged = converged,
       slope = slope, r2 = r2)
}

# ------------------------------------------------------------------------------
# CANON_SPEC §7 — Objection 2: GUE spacing statistical significance.
# Verdict: p < 0.05 -> H0 REJECTED (with the honest finite-T note printed only
# in that branch). NEVER prints "GUE confirmed" unconditionally.
# ------------------------------------------------------------------------------

objection_2 <- function(z, msg) {
  cat(sprintf("\n%s\n%s\n", strrep("=", 60), msg$obj2_title))

  sp <- spacings_of(z)
  cat(sprintf("  Computed %d normalized spacings\n", length(sp)))

  mv <- .mean_var_s(sp)
  cat(sprintf(msg$obj2_mean, mv$mean, mv$var, length(sp)))

  ks <- ks_test(sp)
  cat(sprintf(msg$obj2_ks, ks$D, ks$p))

  W2 <- cvm_stat(sp)
  cat(sprintf(msg$obj2_cvm, W2))

  A2 <- ad_stat(sp)
  cat(sprintf(msg$obj2_ad, A2))

  ar <- adjacent_ratio(z)
  cat(sprintf(msg$obj2_rmean, ar$r, ar$n_r))

  rejected <- ks$p < 0.05
  verdict <- if (rejected) msg$obj2_reject else msg$obj2_not_reject
  cat(sprintf(msg$obj2_result, verdict))
  if (rejected) cat(msg$obj2_note)

  list(D = ks$D, p_value = ks$p, W2 = W2, A2 = A2, r_mean = ar$r,
       n_r = ar$n_r, mean = mv$mean, var = mv$var, rejected = rejected,
       n_spacings = length(sp))
}

# ------------------------------------------------------------------------------
# CANON_SPEC §7 — Objection 3: large-T decay rate O(1/sqrt(N)).
# Grid N = 50*2^k while <= n, plus n itself if not already there; OLS of
# log b(N) vs log N; 95% CI = ±1.96*se; verdict |slope-(-0.5)| <= 0.1.
# ------------------------------------------------------------------------------

objection_3 <- function(z, pref, msg) {
  cat(sprintf("\n%s\n%s\n", strrep("=", 60), msg$obj3_title))

  n <- length(z)
  Nvals <- numeric(0)
  v <- 50
  while (v <= n) {
    Nvals <- c(Nvals, v)
    v <- v * 2
  }
  if (length(Nvals) > 0L && Nvals[length(Nvals)] != n && n > 100) {
    Nvals <- c(Nvals, n)
  }

  cat("  Computing b(N) at multiple N values ...\n")
  logN <- numeric(0)
  logB <- numeric(0)
  for (N in Nvals) {
    bN <- pref[N + 1L] / N
    if (is.na(bN) || bN <= 0) next
    logN <- c(logN, log(N))
    logB <- c(logB, log(bN))
    cat(sprintf("    N = %8d  b(N) = %.10f  log(b) = %.6f\n",
                as.integer(N), bN, log(bN)))
  }

  if (length(logN) < 3L) {
    cat("  WARNING: Not enough data points for regression\n")
    return(list(slope = NaN, intercept = NaN, se = NaN, ci_lo = NaN,
                ci_hi = NaN, consistent = FALSE, r2 = 0.0,
                N_values = Nvals, bN_values = numeric(0)))
  }

  lr <- .linreg(logN, logB)
  ci_lo <- lr$slope - 1.96 * lr$se
  ci_hi <- lr$slope + 1.96 * lr$se

  cat(sprintf(msg$obj3_fit, lr$slope, lr$intercept))
  cat(sprintf("  R\u00b2 = %.6f\n", lr$r2))
  cat(msg$obj3_expected)
  cat(sprintf(msg$obj3_ci, ci_lo, ci_hi))

  consistent <- abs(lr$slope - (-0.5)) <= 0.1
  rel <- if (consistent) msg$obj3_within else msg$obj3_outside
  vd  <- if (consistent) msg$obj3_consistent else msg$obj3_inconsistent
  cat(sprintf(msg$obj3_verdict, lr$slope, rel, vd))

  list(slope = lr$slope, intercept = lr$intercept, se = lr$se,
       ci_lo = ci_lo, ci_hi = ci_hi, consistent = consistent, r2 = lr$r2,
       N_values = Nvals, bN_values = exp(logB))
}

# ------------------------------------------------------------------------------
# CANON_SPEC §8 — golden self-check: frozen anchors embedded as literals.
# Tolerances: lambert_w 1e-12 rel; gram_point/bN 1e-6 abs; spacings.mean/var,
# ks.D, cvm, ad, rmean 1e-9 (ks.p 1e-6 rel). Stats anchors are computed on the
# FIRST 50000 zeros only (printed SKIP if fewer are loaded).
# Returns list(pass = , fail = , skip = ).
# ------------------------------------------------------------------------------

selfcheck <- function(z, pref, msg) {
  cat(sprintf("\n%s\n%s\n", strrep("=", 60), msg$selfcheck_title))
  rows <- list()
  nskip <- 0L
  n <- length(z)

  sc_add <- function(name, got, exp, tol, rel) {
    bad <- is.na(got)
    d <- if (bad) Inf else if (rel) abs(got - exp) / abs(exp) else abs(got - exp)
    ok <- !bad && d <= tol
    rows[[length(rows) + 1L]] <<- list(name = name, ok = ok,
                                       got = got, exp = exp, d = d)
    invisible(NULL)
  }
  sc_skip <- function(name, need, have) {
    cat(sprintf(msg$selfcheck_skip, name, as.integer(need), as.integer(have)))
    nskip <<- nskip + 1L
    invisible(NULL)
  }

  # --- lambert_w anchors (tolerance 1e-12 relative) ---------------------------
  lw <- list(
    list("0.5",     0.5,     0.35173371124919584),
    list("1.0",     1.0,     0.5671432904097838),
    list("3.7",     3.7,     1.1599531786120223),
    list("10.0",    10.0,    1.7455280027406992),
    list("271.8",   271.8,   4.17576816800275),
    list("12345.6", 12345.6, 7.417247034540566)
  )
  for (a in lw) {
    sc_add(sprintf("lambert_w(%s)", a[[1]]), lambert_w(a[[2]]), a[[3]], 1e-12, TRUE)
  }

  # --- gram_point anchors (tolerance 1e-6 absolute) ---------------------------
  gp_k <- c(1L, 2L, 3L, 10L, 100L, 1000L, 10000L, 50000L)
  gp_v <- c(23.17028270133466, 27.670182217848343, 31.71797995477886,
            54.67523744685398, 238.58259051450293, 1421.25638903275,
            9878.910118894457, 40434.6952780045)
  gvals <- .gram_points_vec(gp_k)
  for (i in seq_along(gp_k)) {
    sc_add(sprintf("gram_point(n=%d)", gp_k[i]), gvals[i], gp_v[i], 1e-6, FALSE)
  }

  # --- bN anchors (tolerance 1e-6 absolute; need N <= n) ----------------------
  bn_N <- c(100L, 500L, 1000L, 5000L, 10000L, 50000L)
  bn_v <- c(3.3321638710140165, 2.3912304957476382, 2.1072522951855435,
            1.6299485869022874, 1.4794053414584762, 1.2125526772588608)
  for (i in seq_along(bn_N)) {
    N <- bn_N[i]
    if (N <= n) {
      sc_add(sprintf("bN(N=%d)", N), pref[N + 1L] / N, bn_v[i], 1e-6, FALSE)
    } else {
      sc_skip(sprintf("bN(N=%d)", N), N, n)
    }
  }

  # --- bN_off anchor (needs n >= 1500) ----------------------------------------
  if (n >= 1500) {
    sc_add("bN(N=1000,off=500)", compute_bN_offset(z, 1000, 500),
           624.6201618180231, 1e-6, FALSE)
  } else {
    sc_skip("bN(N=1000,off=500)", 1500L, n)
  }

  # --- statistics anchors: FIRST 50000 zeros only -----------------------------
  if (n >= 50000) {
    z5 <- z[seq_len(50000)]
    sp <- spacings_of(z5)
    mv <- .mean_var_s(sp)
    ks <- ks_test(sp)
    W2 <- cvm_stat(sp)
    A2 <- ad_stat(sp)
    ar <- adjacent_ratio(z5)
    sc_add("spacings.mean", mv$mean, 0.999976001221201, 1e-9, FALSE)
    sc_add("spacings.var",  mv$var,  0.1590654827835423, 1e-9, FALSE)
    sc_add("ks_zeros.D",    ks$D,  0.021619337032982328, 1e-9, FALSE)
    sc_add("ks_zeros.p",    ks$p,  9.567870399361496e-21, 1e-6, TRUE)
    sc_add("cvm_zeros.W2",  W2,    8.177703317829403, 1e-9, TRUE)
    sc_add("ad_zeros.A2",   A2,    61.49242624209728, 1e-9, TRUE)
    sc_add("rmean_zeros.r", ar$r,  0.6118798907208398, 1e-9, FALSE)
  } else {
    for (nm in c("spacings.mean/var", "ks_zeros.D/p", "cvm_zeros.W2",
                 "ad_zeros.A2", "rmean_zeros.r")) {
      sc_skip(nm, 50000L, n)
    }
  }

  # --- PASS/FAIL table with deltas --------------------------------------------
  npass <- 0L
  nfail <- 0L
  for (r in rows) {
    status <- if (r$ok) msg$selfcheck_ok else msg$selfcheck_bad
    cat(sprintf(msg$selfcheck_line, r$name, status, r$got, r$exp, r$d))
    if (r$ok) npass <- npass + 1L else nfail <- nfail + 1L
  }
  cat(sprintf(msg$selfcheck_result, npass, nfail))
  list(pass = npass, fail = nfail, skip = nskip)
}

# ------------------------------------------------------------------------------
# Main entry — runs selfcheck, then the selected objections, then the summary
# (selfcheck n/n first, then per-objection status; CANON_SPEC §7).
# ------------------------------------------------------------------------------

ab_cloud_verify <- function(dataDir = NULL, zeros = 50000, source = "auto",
                            objection = "all", lang = NULL, selfcheck = TRUE) {
  if (is.null(dataDir) || !nzchar(dataDir)) {
    here <- .ABV$script_dir
    dataDir <- if (nzchar(here)) file.path(here, "..", "data") else "../data"
  }
  if (is.null(lang) || !nzchar(lang)) lang <- .detect_lang()
  if (!identical(lang, "ru")) lang <- "en"
  msg <- .get_msg(lang)

  zeros <- suppressWarnings(as.numeric(zeros))[1]
  if (is.na(zeros) || zeros < 0) {
    stop("ab_cloud_verify: zeros must be a non-negative number")
  }
  if (!identical(objection, "all") && !objection %in% c("1", "2", "3")) {
    stop("ab_cloud_verify: objection must be 1|2|3|all, got: ", objection)
  }

  loaded <- load_zeros(dataDir, as.integer(zeros), source, msg)
  z <- loaded$zeros
  if (length(z) == 0L) return(invisible(NULL))

  results <- list(lang = lang, n = length(z), source = loaded$source)

  # Shared sequential b(N) prefix — reused by selfcheck/obj1/obj3 (bit-identical
  # to the direct sums, CANON_SPEC §7).
  needPref <- isTRUE(selfcheck) || identical(objection, "all") ||
              identical(objection, "1") || identical(objection, "3")
  pref <- if (needPref) bn_prefix(z) else numeric(0)

  scPass <- -1L
  scFail <- -1L
  if (isTRUE(selfcheck)) {
    sc <- selfcheck(z, pref, msg)
    scPass <- sc$pass
    scFail <- sc$fail
    results$selfcheck <- sc
  }

  ran <- character(0)
  if (identical(objection, "all") || identical(objection, "1")) {
    results$obj1 <- objection_1(z, pref, msg)
    ran <- c(ran, "1")
  }
  if (identical(objection, "all") || identical(objection, "2")) {
    results$obj2 <- objection_2(z, msg)
    ran <- c(ran, "2")
  }
  if (identical(objection, "all") || identical(objection, "3")) {
    results$obj3 <- objection_3(z, pref, msg)
    ran <- c(ran, "3")
  }

  # Summary: self-check n/n first, then per-objection status.
  cat(sprintf("\n%s\n%s\n", strrep("=", 60), msg$summary))
  if (isTRUE(selfcheck)) cat(sprintf(msg$selfcheck_result, scPass, scFail))
  for (k in ran) {
    if (identical(k, "1")) {
      st <- if (isTRUE(results$obj1$converged)) msg$pass_ else msg$warn
    } else if (identical(k, "2")) {
      st <- if (!isTRUE(results$obj2$rejected)) msg$pass_ else msg$fail
    } else {
      st <- if (isTRUE(results$obj3$consistent)) msg$pass_ else msg$fail
    }
    cat(sprintf(msg$summary_line, k, st))
  }
  cat(sprintf("%s\n", strrep("=", 60)))

  invisible(results)
}
