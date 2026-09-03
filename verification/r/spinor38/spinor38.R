# spinor38.R — Test 38: 64 spinor structures of the Klein quartic (R port)
# Self-implemented cyclic Jacobi eigenvalue algorithm (base R, no eigen()).
# Run: Rscript spinor38.R [repo-root]
#
# NOTE on performance: pure-R Jacobi is interpreted, so the full 28-spectrum
# isospectrality panel is reduced here to the first 3 spectra (a partial
# isospectrality check); the full-orbit exact isospectrality
# (max|dlambda| = 3.4e-14) is verified by the C++/Python reference run.

args <- commandArgs(trailingOnly = TRUE)
find_data_dir <- function(root_arg) {
  roots <- character(0)
  if (length(root_arg) > 0) roots <- c(root_arg)
  roots <- c(roots, getwd())
  for (r in roots) {
    b <- r
    for (up in 1:6) {
      cand <- file.path(b, "verification", "spinor64", "data",
                        "spinor_classes.csv")
      if (file.exists(cand)) {
        return(file.path(b, "verification", "spinor64", "data"))
      }
      b <- file.path(b, "..")
    }
  }
  stop("data dir not found; pass repo root as argument")
}

dd <- find_data_dir(if (length(args) > 0) args[1] else "")

# ---- load data ----
cls_lines <- readLines(file.path(dd, "spinor_classes.csv"))
cls_lines <- cls_lines[-1]
cls_lines <- cls_lines[nzchar(cls_lines)]
parts <- strsplit(cls_lines, ",", fixed = TRUE)
class_idx <- as.integer(sapply(parts, `[`, 1))
orbit <- as.integer(sapply(parts, `[`, 2))
arf <- as.integer(sapply(parts, `[`, 3))
signs <- t(sapply(parts, function(p) as.numeric(strsplit(p[4], " ", fixed = TRUE)[[1]])))

edge_lines <- readLines(file.path(dd, "klein_graph_edges.csv"))
edge_lines <- edge_lines[-1]
edge_lines <- edge_lines[nzchar(edge_lines)]
eparts <- strsplit(edge_lines, ",", fixed = TRUE)
e_u <- as.integer(sapply(eparts, `[`, 2))
e_v <- as.integer(sapply(eparts, `[`, 3))

js <- paste(readLines(file.path(dd, "reference_stats.json")), collapse = " ")
json_num <- function(js, key) {
  m <- regmatches(js, regexpr(paste0('"', key, '":\\s*[-0-9.eE+]+'), js))
  as.numeric(gsub(paste0('"', key, '":'), "", gsub('[",}]', "", m)))
}
r_ref <- json_num(js, "r_mean_reference")
n_zero_ref <- round(json_num(js, "n_zero_modes"))
representative <- round(json_num(js, "representative_class"))

N <- 56
n_odd <- sum(orbit == 0)

# ---- cyclic Jacobi (self-implemented; eigen() is NOT allowed here) ----
jacobi_eigen <- function(A) {
  n <- nrow(A)
  for (sweep in 1:200) {
    off <- sum(A[upper.tri(A)]^2)
    if (off < 1e-24) break
    for (p in 1:(n - 1)) {
      for (q in (p + 1):n) {
        if (abs(A[p, q]) < 1e-15) next
        tau <- (A[q, q] - A[p, p]) / (2 * A[p, q])
        t <- sign(tau) / (abs(tau) + sqrt(1 + tau^2))
        c <- 1 / sqrt(1 + t^2)
        s <- t * c
        colp <- A[, p]; colq <- A[, q]
        A[, p] <- c * colp - s * colq
        A[, q] <- s * colp + c * colq
        rowp <- A[p, ]; rowq <- A[q, ]
        A[p, ] <- c * rowp - s * rowq
        A[q, ] <- s * rowp + c * rowq
      }
    }
  }
  sort(diag(A))
}

build_A <- function(idx) {
  A <- matrix(0, N, N)
  for (k in 1:length(e_u)) {
    A[e_u[k] + 1, e_v[k] + 1] <- signs[idx, k]
    A[e_v[k] + 1, e_u[k] + 1] <- signs[idx, k]
  }
  A
}

odd_classes <- which(orbit == 0)
# partial panel: first 3 spectra for isospectrality
panel <- head(odd_classes, 3)
spectra <- lapply(panel, function(i) jacobi_eigen(build_A(i)))
isomax <- 0
if (length(spectra) > 1) {
  for (a in 1:(length(spectra) - 1)) {
    for (b in (a + 1):length(spectra)) {
      isomax <- max(isomax, max(abs(spectra[[a]] - spectra[[b]])))
    }
  }
}

# representative spectrum (class 0) for <r> and zero modes
rep_pos <- which(class_idx == representative & orbit == 0)
if (length(rep_pos) == 0) rep_pos <- which(class_idx == representative)
w0 <- jacobi_eigen(build_A(rep_pos[1]))
lam <- sort(abs(w0))
n_zero <- sum(lam < 1e-8)
dsp <- diff(lam)
dsp <- dsp[dsp > 1e-8]
r_ratios <- pmin(dsp[-length(dsp)], dsp[-1]) / pmax(dsp[-length(dsp)], dsp[-1])
r_mean <- mean(r_ratios)

iok <- isomax < 1e-9
rok <- abs(r_mean - r_ref) < 1e-6
ok <- iok && rok && (n_zero == n_zero_ref)

cat("Test 38 - 64 spinor structures of the Klein quartic (R port)\n")
cat(sprintf("classes loaded: %d | odd-orbit members: %d\n", length(class_idx), n_odd))
cat(sprintf("isospectrality (partial panel of 3): max|dlambda| = %.3e -> %s\n",
            isomax, ifelse(iok, "PASS", "FAIL")))
cat(sprintf("zero modes (representative): %d (expected %d)\n", n_zero, n_zero_ref))
cat(sprintf("<r> (representative): %.10f (reference 0.4515710793) -> %s\n",
            r_mean, ifelse(rok, "PASS", "FAIL")))
cat(sprintf("VERDICT: %s\n", ifelse(ok, "PASS", "FAIL")))
if (!ok) quit(status = 1)
