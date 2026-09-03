# Verification Suite — the AB-Cloud Hypothesis on 10 Languages

This directory is the **independent cross-language verification package** of the
AB-Cloud hypothesis (Isaev I. Kh., ORCID [0009-0003-7299-0701](https://orcid.org/0009-0003-7299-0701),
DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394)).
The same numerical program is implemented **ten times** — in C++, Fortran, Go,
Haskell, JavaScript, Julia, MATLAB, Python, R and Rust — so that any reviewer
can re-derive every headline number in the language they trust, on any OS,
with no hidden dependencies. All implementations read the same frozen
ζ-zero datasets from [`data/`](data) and must agree to numerical tolerance.

Besides the classic "three reviewer objections" checks, this directory also
hosts two newer blocks added in v1.1.0:

- [`spinor64/`](spinor64) — the reference verification of **all 64 spinor
  structures** of the Klein quartic (it corrects the v21 monograph claim that
  "only idx=38 gives GUE agreement"; the claim is withdrawn as a computational
  artifact);
- `<lang>/spinor38/` — **Test 38 ports in 10 languages** (exact isospectrality
  inside a PSL(2,7) orbit + ⟨r⟩ via a hand-written Jacobi eigensolver).

---

## 1. What is verified — the three reviewer objections

### Objection 1 — numerical stability / convergence of b(N)

**Claim:** the AB correction
`b(N) = (1/N) · Σₖ |γₖ − γ̃ₖ|`
(the mean distance between Gram-point approximations and true zeta zeros)
converges as N → ∞.

**Check:** compute b(N) for N = 100, 500, 1000, 5000, 10 000, 50 000 …
and print a convergence table with a log-log plot. The canonical Julia run
gives b(50000) = 1.2126 (HARDCORE pass 2) and an empirical law
b(N) ≈ 7.0312 · N^(−0.1685), R² = 0.9895 (an alternative 1/log N fit gives
R² = 0.9994). The exponent is **empirical**: the monograph's α = 1/2 refers to
the Hofstadter AB-flux per plaquette, *not* to this convergence rate.

### Objection 2 — statistical significance (GUE)

**Claim:** the normalised spacings of zeta zeros follow GUE (Wigner–Dyson).

**Check:** the unfolded spacings
`sₖ = (γₖ₊₁ − γₖ) · log(γₖ / 2π) / (2π)`
are tested against the Wigner surmise `p(s) = (πs/2)·exp(−πs²/4)` with a
Kolmogorov–Smirnov test and a Cramér–von Mises test. Criterion: p-value > 0.05
(H₀ "the zeros are GUE-spaced" is not rejected). The reference run reports
KS = 0.047 with p = 0.27 on 500 mpmath-certified zeros (Montgomery test), and
⟨r⟩ = 0.5848 ± 0.0260 against the GUE reference 0.5992.

### Objection 3 — decay rate at large T

**Claim:** b(N) = O(1/√N), i.e. the log-log slope ≈ −0.5.

**Check:** linear regression of log b(N) vs log N with a 95% CI. The measured
slope is **not** −0.5; the honest verdict of the suite is that the convergence
exponent is empirical (see Objection 1). This is documented rather than
hidden — every verdict in the suite is printed with its raw numbers so a
referee can disagree with the interpretation but not with the arithmetic.

---

## 2. Directory layout (what lives where)

```
verification/
├── data/          # frozen ζ-zero datasets (8 files, up to 2,000,000 zeros)
├── spinor64/      # reference Python verification of all 64 spin structures
├── sections/      # per-monograph-section micro-verifications (section 3, 6)
├── python/        # Python 3.10+   — reference implementation
├── cpp/           # C++17          — g++/clang++, no external libs
├── fortran/       # Fortran 2018   — gfortran
├── julia/         # Julia 1.9+     — stdlib only
├── rust/          # Rust 1.70+     — cargo, std only
├── r/             # R 4.3+         — base R
├── matlab/        # MATLAB R2021b+ — base MATLAB
├── javascript/    # Node.js 18+    — no npm deps
├── go/            # Go 1.21+       — stdlib only
├── haskell/       # GHC 9+         — base + containers
├── deploy.sh      # helper used to upload fresh reports to results/
└── README.md      # this file
```

Every language folder contains the **same four files** (plus, since v1.1.0,
a `spinor38/` subfolder — see §5):

| File | Role |
|---|---|
| `ab_cloud_verify.<ext>` | bilingual module (auto-selects RU/EN at runtime) |
| `ab_cloud_verify_en.<ext>` | English-only version |
| `ab_cloud_verify_ru.<ext>` | Russian-only version |
| `run_verify.<ext>` (or `run_verify.sh`) | standalone CLI runner — one command, no library knowledge needed |

All files embed the function `load_zeros(data_dir, count, source)` which reads
[`data/`](data) with automatic file selection (§4).

---

## 3. How to run (every language, copy-paste)

```bash
# Python 3.10+  (reference implementation)
cd verification/python && python3 run_verify.py --zeros 5000 --objection all --lang ru

# C++17
cd verification/cpp && chmod +x run_verify.sh && ./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en

# Fortran 2018
cd verification/fortran && chmod +x run_verify.sh && ./run_verify.sh --zeros 10000 --source 50k --objection all

# Julia 1.9+
cd verification/julia && julia run_verify.jl --zeros 500000 --source 500k --objection all --lang en

# Rust 1.70+
cd verification/rust && chmod +x run_verify.sh && ./run_verify.sh --zeros 50000 --source 500k --objection 1 --lang ru

# R 4.3+
cd verification/r && Rscript run_verify.R --zeros 50000 --source 50k --objection all --lang en

# MATLAB R2021b+
cd verification/matlab && run_verify('--zeros', 50000, '--source', '50k', '--objection', 'all')

# Node.js 18+
cd verification/javascript && node run_verify.js --zeros 50000 --source 50k --objection all --lang en

# Go 1.21+
cd verification/go && chmod +x run_verify.sh && ./run_verify.sh --zeros 50000 --source 500k --objection all --lang ru

# Haskell (GHC 9+)
cd verification/haskell && chmod +x run_verify.sh && ./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en
```

Each runner prints the three objection verdicts with raw statistics, writes a
timestamped report and saves plots next to the executable.

### CLI parameters (identical in all languages)

| Parameter | Default | Meaning |
|---|---|---|
| `--zeros N` | 5000 | how many ζ zeros to load |
| `--source NAME` | auto | `50k`, `500k`, `2M`, `highT`, `zeros6`, `csv`, `2M_gz`, `auto` |
| `--objection 1/2/3/all` | all | which objection to verify |
| `--lang en/ru` | auto | output language (auto = follow `LANG`) |
| `--data-dir PATH` | ../data | where the zero files live |

---

## 4. Frozen data — automatic file selection

| Requested zeros | File chosen |
|---|---|
| ≤ 13 661 | `data/zeta_zeros_50000.txt` |
| ≤ 500 000 | `data/zeta_zeros_500k_odlyzko.txt` |
| ≤ 2 000 000 | `data/zeta_zeros_2M_odlyzko.txt` |
| > 2 000 000 | `data/zeros6.txt` |

Full provenance, formats and column layout: [`data/README.md`](data/README.md).

---

## 5. spinor64 and the Test-38 ports (added in v1.1.0)

`spinor64/` is the **reference Python implementation** that settled the
"idx=38 uniqueness" question: **all 64 spinor structures of the Klein quartic
give GUE-consistent statistics**. PSL(2,7) splits them into orbits of sizes
**28 / 21 / 7 / 7 / 1**; operators inside an orbit are exactly isospectral
(max|Δλ| ≈ 8.9·10⁻¹⁵); in the AB-cloud Hofstadter model (L = 44, α = 1/2,
Nv = 54 vortices, `:monumental` gauge) all 64 structures pass the MC GUE
consistency test, ⟨r⟩ = 0.5984 ± 0.0035, min p = 0.36.
Details, data files and reproduction: [`spinor64/README.md`](spinor64/README.md).

`<lang>/spinor38/` ports **Test 38** of that experiment to each language: it
reads the frozen classes from `spinor64/data/`, rebuilds the odd-orbit spectra
with its **own hand-written Jacobi eigensolver** (no LAPACK/BLAS), and checks
exact isospectrality + ⟨r⟩. The C++ and JavaScript builds were compiled and
executed during v1.1.0 preparation: isospectrality 3.4·10⁻¹⁴,
⟨r⟩ = 0.4515710793 — **VERDICT PASS**. Each subfolder has its own README with
exact build/run commands.

---

## 6. Expected output and tolerances

A typical full run prints, per objection:

1. **Objection 1** — the b(N) table (N from 100 up to the dataset size) with
   the fitted power law, R², and the PASS/WARN/FAIL verdict against
   `bN_pass_threshold = 2.0`;
2. **Objection 2** — KS and CvM statistics with p-values, ⟨r⟩ with bootstrap
   error (n_bootstrap = 1000), the GUE ratio-law reference 0.5992(3);
3. **Objection 3** — log-log slope with 95% CI (tolerance band ±0.15 around
   the empirical exponent, `slope_ci_tolerance = 0.1` for CI width).

Numerical agreement between languages is expected at the level of
double-precision round-off: identical input zeros → identical b(N) tables to
~1e-12, identical KS statistics to ~1e-9. Any larger deviation means the
loader picked a different file — check `--source`.

---

## 7. Citing

Cite the monographs for the physics and this suite for the numbers:

```bibtex
@misc{isaev2026abcloud,
  title  = {AB-Cloud Research: a phase resonator for the zeros of the Riemann zeta function},
  author = {Iskhak Hamzatovich Isaev},
  year   = {2026},
  doi    = {10.5281/zenodo.21825394},
  url    = {https://github.com/wild8highlander/ab-cloud-research}
}
```

---

## Кратко (по-русски)

- Этот каталог — независимая кросс-языковая верификация AB-Cloud гипотезы:
  одна и та же программа на **10 языках** (C++, Fortran, Go, Haskell,
  JavaScript, Julia, MATLAB, Python, R, Rust), у всех одинаковый CLI и общие
  замороженные данные в `data/`.
- Проверяются три возражения рецензентов: сходимость b(N), GUE-статистика
  нулей (KS/CvM, p > 0.05), скорость убывания; вердикты печатаются с сырыми
  числами.
- Команды запуска для каждого языка — в §3; файл нулей выбирается
  автоматически по запросу `--zeros`.
- В v1.1.0 добавлены `spinor64/` (все 64 спинорные структуры GUE-согласованы,
  «уникальность idx=38» снята как артефакт) и порты Test 38
  `<язык>/spinor38/` (изоспектральность 3.4e-14, ⟨r⟩ = 0.4515710793 — PASS).
- Ожидаемое межъязыковое согласие — на уровне двойной точности; расхождения
  ~1e-12 для b(N) считаются нормой.
