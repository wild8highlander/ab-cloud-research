# ==============================================================================
# AB-Cloud Verification Suite — R, THIN English wrapper (CANON_SPEC §10)
# ==============================================================================
# Pins the output language to English and delegates ALL math to the single
# canonical kernel in ab_cloud_verify.R. No duplicated math here — duplicated
# kernels are how the old suite drifted apart.
#
# Usage:
#   source("ab_cloud_verify_en.R")
#   ab_cloud_verify_en()                                  # ../data, 50000 zeros
#   ab_cloud_verify_en("../data", 50000, "auto", "all")   # positional ok
# For the command line use the runner:  Rscript run_verify.R --lang en ...
# (the wrapper itself only defines the language-pinned entry point).
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
  "ab_cloud_verify.R"   # sourced interactively — resolve against the CWD
}
if (!file.exists(.abv_main_file)) {
  stop("ab_cloud_verify_en.R: cannot find ab_cloud_verify.R next to this file",
       if (nzchar(.abv_wrapper_dir))
         paste0(" (looked in: ", .abv_wrapper_dir, ")")
       else " (looked in the current working directory)",
       ". Run from the verification/r/ directory or via Rscript.")
}
source(.abv_main_file)

# Language-pinned entry point: 'lang' is deliberately NOT a parameter — the
# wrapper forces lang = "en" inside the canonical kernel.
ab_cloud_verify_en <- function(dataDir = NULL, zeros = 50000, source = "auto",
                               objection = "all", selfcheck = TRUE) {
  ab_cloud_verify(dataDir = dataDir, zeros = zeros, source = source,
                  objection = objection, lang = "en", selfcheck = selfcheck)
}
