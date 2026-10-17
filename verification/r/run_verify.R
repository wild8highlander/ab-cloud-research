#!/usr/bin/env Rscript
# ==============================================================================
# AB-Cloud Verification Suite — R CLI runner (THIN, CANON_SPEC §9/§10)
# ==============================================================================
# No math lives here: this only parses the flags, sources the single canonical
# kernel ab_cloud_verify.R, and maps the self-check result to the exit code
# (status 1 if any frozen anchor fails).
#
# Usage:
#   Rscript run_verify.R [options]
#     --zeros N          number of zeros to load   (default 50000; 0 = all)
#     --source NAME      auto|50k|50k_full|500k|2M|highT|2M_gz|csv|zeros6
#                        (default auto = smallest file with enough zeros;
#                         50k_full = zeta_zeros_50000_embedded.txt;
#                         highT = BLOCK-offset format)
#     --objection X      1|2|3|all                 (default all)
#     --lang L           en|ru                     (default: LANG auto-detect)
#     --data-dir D       data directory            (default ../data relative
#                                                    to the language folder)
#     --no-selfcheck     skip the frozen-anchor self-check
#     --help             show this help
#
# Examples:
#   Rscript run_verify.R --zeros 50000 --objection all --lang en
#   Rscript run_verify.R --source highT --objection 2 --lang ru
#   Rscript run_verify.R --data-dir /path/to/data --zeros 200000
# ==============================================================================

.parse_flags <- function(args) {
  opts <- list(zeros = 50000L, source = "auto", objection = "all",
               lang = NULL, dataDir = NULL, selfcheck = TRUE)
  i <- 1L
  n <- length(args)
  while (i <= n) {
    a <- args[i]
    if (a == "--zeros") {
      if (i + 1L > n) stop("missing value after --zeros")
      v <- suppressWarnings(as.integer(args[i + 1L]))
      if (is.na(v) || v < 0L) stop("--zeros must be a non-negative integer")
      opts$zeros <- v
      i <- i + 2L
    } else if (a == "--source") {
      if (i + 1L > n) stop("missing value after --source")
      opts$source <- args[i + 1L]
      i <- i + 2L
    } else if (a == "--objection") {
      if (i + 1L > n) stop("missing value after --objection")
      opts$objection <- args[i + 1L]
      i <- i + 2L
    } else if (a == "--lang") {
      if (i + 1L > n) stop("missing value after --lang")
      opts$lang <- args[i + 1L]
      i <- i + 2L
    } else if (a == "--data-dir") {
      if (i + 1L > n) stop("missing value after --data-dir")
      opts$dataDir <- args[i + 1L]
      i <- i + 2L
    } else if (a == "--no-selfcheck") {
      opts$selfcheck <- FALSE
      i <- i + 1L
    } else if (a == "--help" || a == "-h") {
      opts$help <- TRUE
      i <- i + 1L
    } else {
      stop("unknown option: ", a)
    }
  }
  opts
}

.usage <- function() {
  cat("AB-Cloud Verification Suite \u2014 R runner (CANON_SPEC v3.0)\n\n")
  cat("Usage: Rscript run_verify.R [options]\n\n")
  cat("Options:\n")
  cat("  --zeros N          zeros to load (default 50000; 0 = all)\n")
  cat("  --source NAME      auto|50k|50k_full|500k|2M|highT|2M_gz|csv|zeros6\n")
  cat("  --objection X      1|2|3|all (default all)\n")
  cat("  --lang L           en|ru (default: auto-detect from LANG)\n")
  cat("  --data-dir D       data directory (default ../data relative to r/)\n")
  cat("  --no-selfcheck     skip the frozen-anchor self-check\n")
  cat("  --help             show this help\n\n")
  cat("Exit status: 0 on success; 1 if any frozen self-check anchor fails\n")
  cat("or the data cannot be loaded.\n")
}

# --- flag parsing -------------------------------------------------------------
args <- commandArgs(trailingOnly = TRUE)
opts <- tryCatch(.parse_flags(args), error = function(e) {
  cat("ERROR:", conditionMessage(e), "\n")
  cat("Run with --help for usage.\n")
  NULL
})
if (is.null(opts)) quit(save = "no", status = 1)
if (isTRUE(opts$help)) {
  .usage()
  quit(save = "no", status = 0)
}

# --- locate and source the single canonical kernel (no math here) -------------
fa <- commandArgs(trailingOnly = FALSE)
fi <- fa[grepl("^--file=", fa)]
scriptDir <- getwd()
if (length(fi) > 0L) {
  p <- sub("^--file=", "", fi[1])
  if (nzchar(p)) scriptDir <- dirname(suppressWarnings(normalizePath(p, mustWork = FALSE)))
}
mainFile <- file.path(scriptDir, "ab_cloud_verify.R")
if (!file.exists(mainFile)) {
  cat("ERROR: cannot find ab_cloud_verify.R in: ", scriptDir, "\n", sep = "")
  quit(save = "no", status = 1)
}
source(mainFile)

# --- resolve data directory (default ../data relative to the language folder) -
if (!is.null(opts$dataDir) && !dir.exists(opts$dataDir)) {
  cand <- file.path(scriptDir, opts$dataDir)
  if (dir.exists(cand)) opts$dataDir <- cand
}

# --- run ------------------------------------------------------------------------
res <- tryCatch(
  ab_cloud_verify(dataDir = opts$dataDir, zeros = opts$zeros,
                  source = opts$source, objection = opts$objection,
                  lang = opts$lang, selfcheck = opts$selfcheck),
  error = function(e) {
    cat("ERROR:", conditionMessage(e), "\n", file = stderr())
    NULL
  }
)

if (is.null(res)) quit(save = "no", status = 1)
if (isTRUE(opts$selfcheck) && !is.null(res$selfcheck) &&
    isTRUE(res$selfcheck$fail > 0L)) {
  quit(save = "no", status = 1)
}
quit(save = "no", status = 0)
