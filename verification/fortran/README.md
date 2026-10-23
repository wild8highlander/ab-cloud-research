# AB-Cloud Verification Suite — Fortran port (canonical spec v3.0)

> **🧭 Navigation:** [verification/](../README.md) · [Root README](../../README.md) · [CANON_SPEC](../CANON_SPEC.md)

Fortran implementation of the unified AB-Cloud numerical kernel, ported to the
binding specification `verification/CANON_SPEC.md` (v3.0). Single source of
truth, bilingual EN/RU catalog, frozen-anchor self-check, honest
number-driven verdicts. No external dependencies: only intrinsic modules
(`iso_fortran_env`, `ieee_arithmetic`) plus the `erf` intrinsic.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.f90` | **The complete kernel** — math, loader, bilingual catalog, self-check, CLI |
| `ab_cloud_verify_en.f90` | THIN wrapper: `#define FORCE_LANG_EN` + `#include` (§10) |
| `ab_cloud_verify_ru.f90` | THIN wrapper: `#define FORCE_LANG_RU` + `#include` (§10) |
| `run_verify.sh` | builds all three binaries (one kernel, three language pins) and runs |
| `spinor38/` | Test 38 port (see below, untouched by the canon port) |

Per CANON_SPEC §10 the `*_en` / `*_ru` files contain **no duplicated math** —
they are two-line preprocessor wrappers around the same source text. The main
binary selects the language at runtime (`--lang en|ru`, default auto-detect
from `$LANG`); the wrapper binaries pin it at compile time.

## Requirements

- `gfortran >= 9` (or any Fortran 2008 compiler). The preprocessor is
  **required** (`-cpp`): the wrappers are `#define` + `#include` of the main
  source. No external libraries.

## Build & run

```bash
cd verification/fortran
./run_verify.sh                          # builds and runs with canon defaults
./run_verify.sh --zeros 50000 --source 50k_full --objection all --lang ru

# or manually:
gfortran -cpp -O2 -std=f2008 -Wall -o ab_cloud_verify    ab_cloud_verify.f90
gfortran -cpp -O2 -std=f2008 -Wall -o ab_cloud_verify_en ab_cloud_verify_en.f90
gfortran -cpp -O2 -std=f2008 -Wall -o ab_cloud_verify_ru ab_cloud_verify_ru.f90
./ab_cloud_verify --zeros 50000 --objection all
```

## CLI (CANON_SPEC §9)

| Flag | Meaning |
|---|---|
| `--zeros N` | zeros to load, default `50000`; `0` = load the whole source file |
| `--source NAME` | `auto`, `50k`, `50k_full`, `500k`, `2M`, `highT`, `2M_gz`, `csv`, `zeros6`; `auto` = smallest source with count ≥ N |
| `--objection X` | `1`, `2`, `3` or `all` (default) |
| `--lang L` | `en` / `ru`; default auto-detect from `$LANG` (RU if it contains `ru`) |
| `--data-dir D` | path to `data/`, default `../data` (relative to CWD) |
| `--no-selfcheck` | skip the frozen-anchor self-check |
| `--help` | usage |

Source registry: `50k` → `zeta_zeros_50000.txt` (13661), `50k_full` →
`zeta_zeros_50000_embedded.txt` (50000), `500k` →
`zeta_zeros_500k_odlyzko.txt` (500000), `2M` → `zeta_zeros_2M_odlyzko.txt`
(2001052), `highT` → `zeta_zeros_highT_blocks.txt` (30000, `#BLOCK
index=… offset=…` format), `2M_gz` → gzip of the 2M table (decompressed via
the `gzip` binary into a temp file), `csv` → `zeta_zeros_50000.csv` (column 2
= t), `zeros6` → `zeros6.txt`. Loading sorts ascending, then truncates to N.

## What the kernel computes (spec §1–§8)

- **§1 Lambert W** — principal branch, Newton, tol `1e-14·(1+|w|)`-style
  stopping per the canonical Python reference (`fp` guard + small-`x` seed;
  the naive seed `log(x)` hits `w = −1` exactly for `x = 1/e` where the
  denominator vanishes).
- **§2 Gram point (canon)** — seed `t = 2πk / W(k/e)`, then **exactly 8 Newton
  iterations** on the 5-term Riemann–Siegel theta expansion
  `θ(t) = (t/2)·ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³)`.
  The old port's formula `2π·W(k/e)` was mathematically wrong and is gone.
- **§3 b(N), b(N;offset)** — sequential accumulation `Σ|γ_k − γ̃_k|` in the
  exact canon order; the prefix-sum table `pref(N)/N` used by objections 1/3
  is bit-identical to the direct sum.
- **§4 Normalized spacings** — `s_k = (γ_{k+1} − γ_k)·log(γ_k/2π)/(2π)`,
  `γ_k > 0` filter, original order preserved.
- **§5 GUE CDF** — Wigner–Dyson β=2 surmise `F(s) = erf(2s/√π) − (4s/π)e^{−4s²/π}`
  through a lazily built 32768-point interpolation table, `SMAX = 5`; outside
  the table the exact closed form.
- **§6 Statistics** — two-sided KS `D` with λ-corrected asymptotic p
  (`λ = (√n + 0.12 + 0.11/√n)·D`, two branches with the 1e-18 term cutoffs,
  clamped to [0,1]); Cramér–von Mises `W²`; Anderson–Darling `A²` with
  `1e-300 / 1−1e-16` clamps; `<r>` adjacent-gap ratio (skipping all-zero gap
  pairs); mean / sample variance (n−1). All on the sorted spacings, mean/var
  summed in the original spacing order for bit-parity with the reference.
- **§7 Objections** — obj1 grid `{100,500,1000,5000,10000,50000}` filtered to
  N ≤ n, honest monotone-decrease verdict + clearly-labelled EMPIRICAL
  power-law fit (never "O(1/√N)" claims from obj1); obj2 statistics on all
  loaded zeros, `p < 0.05 → H₀ REJECTED` with the honest finite-T note, and
  `NOT REJECTED` otherwise — printed only in the branch the numbers chose;
  obj3 grid `50·2^k` plus n itself, OLS log–log with slope stderr, 95% CI
  (±1.96·se), verdict `|slope−(−0.5)| ≤ 0.1` → CONSISTENT / INCONSISTENT.
- **§8 selfcheck** — all frozen anchors embedded as literals (6 `lambert_w`,
  8 `gram_point`, 6 `bN`, `bN_off(1000,500)`, spacing mean/var, `ks.D/p`,
  CvM, AD, `<r>`). Printed as a PASS/FAIL/SKIP + Δ table with the spec
  tolerances (`lambert_w` 1e-12 rel; `gram_point`/`bN` 1e-6 abs; stats 1e-9,
  `ks.p` 1e-6 rel); stats anchors run on the FIRST 50000 zeros and print
  SKIP rows otherwise. **The program exits with code 1 if any anchor fails.**

There are **no canned verdict strings**: every conclusion line is inside the
branch selected by the computed numbers.

## Validation status

No gfortran in the authoring environment — the port was verified two ways:
1. Static: block balance, declaration audit, and a format/argument audit of
   every `WRITE` statement (descriptor count vs output-item count) pass.
2. Numerical: a Python mirror with the *exact same operation order* run on
   `zeta_zeros_50000_embedded.txt` reproduces **28/28 frozen anchors**
   (gram_point and bN_off bit-exact; statistics at libm-ULP distance,
   ≤ 1.4e-12 rel — tolerances are 1e-6…1e-9).

## spinor38/ — Test 38 port (unchanged)

`spinor38/spinor38.f90` reads the frozen classes from `../spinor64/data/`
(plain CSV parsing) and rebuilds the 28 odd-orbit spectra with a hand-written
cyclic-Jacobi eigensolver:

```bash
cd verification/fortran/spinor38
gfortran -O2 -std=f2008 -o spinor38 spinor38.f90 && ./spinor38
```

Details: `spinor38/README.md`.

## Documented deviations

- `--zeros 0` loads the entire source file (in the canonical Python CLI it
  means "0 zeros"; the semantics are aligned with the MATLAB port and
  documented here).
- `2M_gz` shells out to an external `gzip` binary (the Python kernel uses
  its built-in `gzip` module).
- RU catalog messages are printed in UTF-8 as-is (no transliteration).
- The PASS/FAIL field width in the selfcheck table is widened to 16
  columns so the Russian «ПРОЙДЕНО/ПРОПУСК» strings are not byte-truncated.

## Troubleshooting

- **`#ifdef` / `#include` treated as errors** — you forgot `-cpp`.
- **`gfortran: command not found`** — Debian/Ubuntu `apt install gfortran`;
  Fedora `dnf install gcc-gfortran`; macOS `brew install gfortran`;
  Termux `pkg install gfortran`.
- **2M_gz fails** — the `gzip` binary must be on `$PATH` (the program shells
  out `gzip -dc` into a temp file under `/tmp`).
- **Cyrillic looks garbled** — the RU catalog is UTF-8; run in a UTF-8
  terminal (`LANG=ru_RU.UTF-8`).
