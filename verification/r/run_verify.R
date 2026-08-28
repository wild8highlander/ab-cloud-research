#!/usr/bin/env Rscript
# ==============================================================================
# AB-Cloud Verification Suite — R Runner Script
# ==============================================================================
# Usage:
#   Rscript run_verify.R [options]
#   Options:
#     --zeros N         Number of zeros to use (0 = all)
#     --source NAME     Data source: auto|zeta_zeros_50000|zeta_zeros_500k|
#                         zeta_zeros_2M|zeta_zeros_highT|zeros6|zeta_zeros_50000_csv
#     --objection 1|2|3|all   Which objection to verify
#     --lang en|ru      Language
#     --data-dir DIR    Data directory (default: ../data)
#     --help            Show this help
# ==============================================================================

# --- Parse command-line arguments --------------------------------------------

args <- commandArgs(trailingOnly = TRUE)

opts <- list(
  zeros     = 0,
  source    = "auto",
  objection = "all",
  lang      = "en",
  dataDir   = "../data"
)

i <- 1
while (i <= length(args)) {
  flag <- args[i]
  if (flag == "--zeros" && i + 1 <= length(args)) {
    opts$zeros <- as.integer(args[i + 1]); i <- i + 2
  } else if (flag == "--source" && i + 1 <= length(args)) {
    opts$source <- args[i + 1]; i <- i + 2
  } else if (flag == "--objection" && i + 1 <= length(args)) {
    opts$objection <- args[i + 1]; i <- i + 2
  } else if (flag == "--lang" && i + 1 <= length(args)) {
    opts$lang <- args[i + 1]; i <- i + 2
  } else if (flag == "--data-dir" && i + 1 <= length(args)) {
    opts$dataDir <- args[i + 1]; i <- i + 2
  } else if (flag == "--help") {
    cat("
AB-Cloud Verification Suite — R Runner

Usage: Rscript run_verify.R [options]

Options:
  --zeros N           Number of zeros to use (0 = all)
  --source NAME       Data source (auto, zeta_zeros_50000, zeta_zeros_500k,
                        zeta_zeros_2M, zeta_zeros_highT, zeros6,
                        zeta_zeros_50000_csv)
  --objection 1|2|3|all   Which objection(s) to verify
  --lang en|ru        Output language
  --data-dir DIR      Path to data directory (default: ../data)
  --help              Show this help message

Examples:
  Rscript run_verify.R --zeros 50000 --objection 1 --lang en
  Rscript run_verify.R --source zeta_zeros_500k --objection all --lang ru
  Rscript run_verify.R --data-dir /path/to/data --zeros 100000
\n")
    quit(save = "no")
  } else {
    cat("Unknown option:", flag, "\n")
    quit(save = "no", status = 1)
  }
}

# --- Resolve script directory and load main module ---------------------------

scriptDir <- dirname(normalizePath(sys.frame(1)$ofile, mustStart = FALSE))
if (!nzchar(scriptDir) || !dir.exists(scriptDir)) {
  scriptDir <- getwd()
}

# Source the main bilingual module
mainFile <- file.path(scriptDir, "ab_cloud_verify.R")
if (!file.exists(mainFile)) {
  cat("ERROR: Cannot find ab_cloud_verify.R in:", scriptDir, "\n")
  quit(save = "no", status = 1)
}
source(mainFile)

# --- Resolve data directory --------------------------------------------------

dataDir <- opts$dataDir
if (!dir.exists(dataDir)) {
  # Try relative to script directory
  dataDir <- file.path(scriptDir, opts$dataDir)
}
if (!dir.exists(dataDir)) {
  cat("ERROR: Data directory not found:", opts$dataDir, "\n")
  quit(save = "no", status = 1)
}

# --- Run verification --------------------------------------------------------

cat("AB-Cloud R Runner\n")
cat("  Data dir:   ", normalizePath(dataDir), "\n")
cat("  Zeros:      ", if (opts$zeros > 0) opts$zeros else "all", "\n")
cat("  Source:     ", opts$source, "\n")
cat("  Objection:  ", opts$objection, "\n")
cat("  Language:   ", opts$lang, "\n\n")

results <- ab_cloud_verify(
  dataDir   = dataDir,
  zeros     = opts$zeros,
  source    = opts$source,
  objection = opts$objection,
  lang      = opts$lang
)

# Return exit code based on results
if (is.null(results)) {
  quit(save = "no", status = 1)
} else {
  quit(save = "no", status = 0)
}
