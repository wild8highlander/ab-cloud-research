<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:00e5ff,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ verification/](../README.md) · [🏠 Root README](../../README.md)**

</div>
# R Verification — canonical port (CANON_SPEC v3.0)

> **🧭 Navigation:** [verification/](../README.md) · [Root README](../../README.md) · [CANON_SPEC](../CANON_SPEC.md)

Base-R implementation of the AB-Cloud Verification Suite kernel. No CRAN
packages; runs anywhere R ≥ 4.0 does. This port follows
[`../CANON_SPEC.md`](../CANON_SPEC.md) exactly: same frozen anchors, same
tolerances, same CLI flags, honest branch-selected verdicts only.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.R` | the single canonical kernel: Lambert W (§1), Gram points (§2), b(N) (§3), spacings (§4), GUE table CDF (§5), KS/CvM/AD/⟨r⟩ (§6), objections (§7), golden self-check (§8), loader (§9), bilingual EN/RU messages |
| `ab_cloud_verify_en.R` | THIN English wrapper — sources the kernel, pins `lang="en"` (§10) |
| `ab_cloud_verify_ru.R` | THIN Russian wrapper — sources the kernel, pins `lang="ru"` (§10) |
| `run_verify.R` | THIN CLI runner — parses flags, sources the kernel, exit-code mapping |
| `spinor38/` | Test 38 port (separate companion, see below) |

There is **no duplicated math**: the old per-language copies (`*_en`/`*_ru`)
are one-line-deep shims over the shared kernel, per CANON_SPEC §10.

## Requirements

- **R ≥ 4.0** — base only (`stats` for `pnorm`, `utils`/`base` otherwise).
  No `install.packages()`.

## Run

```bash
cd verification/r
Rscript run_verify.R --zeros 50000 --objection all --lang en
Rscript run_verify.R --source highT --objection 2 --lang ru
Rscript run_verify.R --zeros 0 --source zeros6 --objection 1
Rscript run_verify.R --help
```

CLI (CANON_SPEC §9):

| Flag | Values | Meaning |
|---|---|---|
| `--zeros N` | integer (default 50000; `0` = all loaded) | how many ordinates to use |
| `--source NAME` | `auto`, `50k`, `50k_full`, `500k`, `2M`, `highT`, `2M_gz`, `csv`, `zeros6` | `auto` = smallest registered file with enough zeros; `50k_full` = `zeta_zeros_50000_embedded.txt`; `highT` = BLOCK-offset format; `2M_gz` read through a `gzfile` connection |
| `--objection X` | `1`, `2`, `3`, `all` | run the full suite or one objection |
| `--lang L` | `en`, `ru` | report language (default: auto-detect from `LANG`) |
| `--data-dir D` | path (default `../data` relative to `r/`) | frozen Odlyzko tables |
| `--no-selfcheck` | flag | skip the frozen-anchor self-check |

Exit status: **0** on success, **1** if any frozen self-check anchor fails or
the data cannot be loaded.

Interactive use:

```r
source("ab_cloud_verify.R")
res <- ab_cloud_verify(zeros = 50000, lang = "en")       # ../data by default
res$selfcheck$pass; res$obj3$slope
source("ab_cloud_verify_ru.R")                           # thin wrapper
ab_cloud_verify_ru(objection = "2")
```

## What a run prints

1. **Golden self-check (§8) first** — all 28 frozen anchors as literals:
   6 `lambert_w` (tol 1e-12 rel), 8 `gram_point` (1e-6 abs), 6 `bN` (1e-6 abs),
   `bN_off(1000,500)` (1e-6 abs), and on the FIRST 50 000 zeros
   `spacings.mean/var`, `ks_zeros.D`, `ks_zeros.p` (1e-6 rel), `cvm_zeros.W2`,
   `ad_zeros.A2`, `rmean_zeros.r` (1e-9). PASS/FAIL lines carry the computed
   value, the frozen expectation and Δ; unavailable anchors print an explicit
   SKIP line (stats need ≥ 50 000 zeros, `bN_off` needs ≥ 1500, `bN(N)` needs
   N ≤ n).
2. **Objection 1** — b(N) convergence table on the grid {100, 500, 1000, 5000,
   10000, 50000} (prefix/N — bit-identical to the direct sums; canon print
   order: rule, title, caption, column header, `----`), optional
   empirical power-law fit, and the honest verdict: convergence is declared
   only when the table is monotonically decreasing (and explicitly labeled
   EMPIRICAL, not O(1/√N)).
3. **Objection 2** — mean/var of normalized spacings, two-sided KS D with the
   λ-corrected p-value, Cramér–von Mises W², Anderson–Darling A² (1e-300 /
   1−1e-16 clamps), ⟨r⟩ with n_r. Verdict: `p < 0.05` → H₀ REJECTED plus the
   honest finite-T note (printed only in that branch). The suite never prints
   an unconditional "GUE confirmed".
4. **Objection 3** — b(N) on the grid 50·2^k (+ n), OLS of log b(N) vs log N
   with slope stderr (`se² = (SSres/(m−2))·m/(m·Sxx−Sx²)`), 95% CI ±1.96·se;
   verdict `|slope−(−0.5)| ≤ 0.1` → CONSISTENT, else INCONSISTENT — as
   computed. (On the first 50 000 zeros the measured slope ≈ −0.17, so the
   honest printed verdict is INCONSISTENT with O(1/√N) — that is what the
   numbers say, not a canned string.)
5. **Summary** — self-check n/n first, then per-objection status.

## Canonical kernel notes

- **Lambert W (§1)**: Newton on `w·e^w = x`, up to 50 iterations, stop when
  `|delta| < 1e-14·(1+|w|)`; seed `w = log(x)`, `w -= log(w)` when `w > 0`.
- **Gram point (§2)**: seed `t = 2πk / W(k/e)`, then **exactly 8 Newton
  iterations** on the 5-term Riemann–Siegel theta
  `θ(t) = (t/2)ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³)`. The old port's
  3-iteration, 3-term variant is gone.
- **b(N) (§3)**: strictly sequential accumulation; the shared prefix table
  feeds selfcheck/obj1/obj3 (`b(N) = pref[N+1]/N` — bit-identical order).
- **GUE CDF (§5)**: Wigner–Dyson β=2 surmise through the lazily-built
  32768-point interpolation table (SMAX = 5) cached in a package environment;
  lookups use the exact canon arithmetic `x = s·(TN−1)/SMAX; i = floor(x);
  t = x−i; (1−t)·tbl[i+1] + t·tbl[i+2]` (1-based R). Outside [0, 5) the exact
  closed form is used.
- **Vectorization**: the Lambert-W and theta-Newton kernels run over whole k
  vectors (masked updates — per-element operation order is identical to the
  scalar pseudocode), so the 50 000-zero self-check takes seconds, not
  minutes. The algorithm is unchanged.
- **Loader (§9)**: registry `50k|50k_full|500k|2M|highT|2M_gz|csv|zeros6`;
  `auto` = smallest `avail ≥ zeros`; sort ascending FIRST, then truncate;
  plain/CSV/BLOCK-offset/gz parsers.

## Documented deviations (all tiny, all deliberate)

- **`erf` via `pnorm`**: R has no base `erf`, so `erf(x) = 2·pnorm(x√2) − 1`
  (mandated for this port). Effect on the GUE table ≈ 1e-14 relative — far
  below the 1e-9/1e-6 anchor tolerances.
- **`lambert_w` seed guard**: for `0 < x < 1` the seed is `w = x` (the log
  seed sits exactly on the `fp = 0` degeneracy at `x = 1/e`, which
  `gram_point(1)` hits). Same choice as the canonical Python kernel; the §1
  pseudocode does not describe this case.
- **`--zeros 0` = all loaded zeros** (the CLI default is 50000; 0 would
  otherwise be meaningless).
- **Objection 1 honest verdict**: when the b(N) table is NOT monotonically
  decreasing, the port prints an explicit "convergence NOT confirmed" line
  instead of the canon's unconditional confirm-note (which would be a canned
  string). Spec §7 requires verdicts chosen by the computed numbers.
- **`cvm_zeros.W2` / `ad_zeros.A2` anchors** use the 1e-9 tolerance relative
  (as the canonical Python self-check does).
- The obj2 one-line p-value is printed with `%.6f` (canon parity), so
  `p ≈ 9.6e-21` renders as `0.000000`; the self-check line prints the full
  `%.12g` value.
- gz input is read through a base-`gzfile` connection (no external `gunzip`).

## Validation status

No `Rscript` exists in the porting sandbox, so the port was validated by an
operation-order mirror — a Python script that reproduces
the R code element-for-element (masked vector Newton, sequential sums, table
interpolation, loader parsers) on the real `zeta_zeros_50000_embedded.txt`.
Re-confirmed in the final session — **28/28 frozen anchors PASS**
(`lambert_w ≤ 1.9e-16` rel; `gram_point`/`bN`/`bN_off` bit-exact to ≤ 8.9e-16;
`ks.p` rel 1.4e-12 vs 1e-6 tol; `W2/A2/mean/var/⟨r⟩` ≤ 1.2e-13 vs 1e-9;
`n_r = 49998`; parser counts 13661/50000/13661/30000; `auto(50000)=50k_full`,
`auto(2000)=50k`, `auto(20000)=highT`), plus a static checker (delimiter
balance, `sprintf` spec/arg audit, forbidden-token scan: all OK).
Final R-native runs happen centrally (`Rscript` machine).

## spinor38/ — Test 38 port

`spinor38/spinor38.R` reads the frozen classes from `../spinor64/data/` and
rebuilds the 28 odd-orbit spectra with an R-native Jacobi eigensolver:

```bash
cd verification/r/spinor38
Rscript spinor38.R
```

## Summary

- The base-R ≥ 4.0 port with no CRAN packages follows the canon of
  `verification/CANON_SPEC.md` (v3.0).
- One kernel: `ab_cloud_verify.R`; `ab_cloud_verify_en.R` / `ab_cloud_verify_ru.R` are thin
  language-pinning wrappers (§10) — no duplicated math anymore.
- Gram points: seed `2πk/W(k/e)` + exactly 8 Newton iterations on the 5-term theta (the
  old 3-iteration/3-term variant is gone). GUE via the 32768-point table (SMAX = 5),
  `erf` via `2·pnorm(x√2) − 1`.
- The §8 self-check prints all 28 frozen anchors as a PASS/FAIL/Δ table (+ SKIP) and the
  runner exits with status 1 on any failure.
- Honest verdicts: only the branch selected by the computed numbers is printed; there are
  no canned "GUE confirmed" strings.
- Run: `Rscript run_verify.R --zeros 50000 --objection all --lang en`
  (§9 flags; `--no-selfcheck`, `--data-dir`, `--help`).
- Sandbox validation used a Python mirror of the exact operation order: 28/28 anchors;
  the final R-native runs happen centrally.
- `spinor38/` — the Test 38 port, mirroring the validated reference.

<div align="center">

<img src="../../assets/svg/divider-cyan.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
