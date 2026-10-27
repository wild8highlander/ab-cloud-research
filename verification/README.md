<!-- AB-ENRICHED:v1 · section=verification -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=90&color=0:05060f,50:00e5ff,100:05060f&section=header&text=VERIFICATION%20SUITE&fontSize=26&fontColor=e5e7eb&fontAlignY=55&animation=fadeIn" alt="VERIFICATION SUITE" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=15&duration=2800&pause=1100&color=00e5ff&center=true&vCenter=true&width=760&lines=Ten+languages+%C2%B7+one+number+each;Same+frozen+%CE%B6-data+%C2%B7+same+verdicts;Cross-language+agreement+%7E1e-12" alt="Typing: section tagline"/>

<img src="../assets/svg/progress-verification.svg" alt="progress-verification" width="420"/>

</div>

<!-- AB-ENRICHED:v2 · motion strip -->
<div align="center">

<img src="../assets/svg/progress-spinor64.svg" alt="progress bar: spinor structures GUE-consistent 64/64" width="420"/><br/>
<img src="../projects/quantum-research/VISUAL_ANIMATIONS/gif/spinor_cycles.gif" alt="Animated GIF: the 64 spinor structures cycling through their holonomy classes" width="560"/><br/>
<img src="../projects/quantum-research/VISUAL_ANIMATIONS/svg/spinor_ring_pi2.svg" alt="Animated SMIL ring: spinor holonomy phase pi/2 rotating in step" width="170"/> <img src="../projects/quantum-research/VISUAL_ANIMATIONS/svg/spinor_ring_pi3.svg" alt="Animated SMIL ring: spinor holonomy phase pi/3 rotating in step" width="170"/> <img src="../projects/quantum-research/VISUAL_ANIMATIONS/svg/spinor_ring_pi7.svg" alt="Animated SMIL ring: spinor holonomy phase pi/7 — the AB phase — rotating in step" width="170"/>

<sub>🎞️ <em>Ten ports, one verdict — the 64 spinor structures in motion, regenerated from the package's own data.</em></sub>

<img src="../assets/svg/divider-animated.svg" alt="—" width="100%" height="14"/>

</div>
<details>
<summary><strong>🗺️ How <code>verification/</code> connects to the repository (click)</strong></summary>

```mermaid
flowchart LR
    ROOT["🏠 Root README"] --> SEC["Verification Suite (10 languages)"]
    DATA["🧊 Frozen data<br/>verification/data/"] -.-> SEC
    SEC --> OUT["10 independent ports — identical headline numbers"]
    SEC <-.-> SIB["code · formal"]
```

</details>

<div align="center">

<img src="assets/banner.svg" alt="Verification — animated banner: the ring of ten language chips (Python, Julia, C++, Fortran, Go, JavaScript, Haskell, Rust, MATLAB, R) pulsing in turn around the ζ-core, with the frozen data and spinor blocks" width="100%"/>

# 🌐 Verification Suite — the AB-Cloud Hypothesis on 10 Languages

> **🧭 Navigation:** [Root README](../README.md) · [code/](../code/README.md) · [spinor64/](spinor64/README.md)

**The independent cross-language verification package: the same numerical program implemented
ten times — in C++, Fortran, Go, Haskell, JavaScript, Julia, MATLAB, Python, R and Rust — so
that any reviewer can re-derive every headline number in the language they trust, on any OS,
with no hidden dependencies.**

[![Languages](https://img.shields.io/badge/languages-10-9558B2?style=flat-square)](#-directory-layout-what-lives-where)
[![Objections](https://img.shields.io/badge/reviewer%20objections-3-0E7C86?style=flat-square)](#-what-is-verified--the-three-reviewer-objections)
[![Frozen data](https://img.shields.io/badge/frozen%20data-2%20000%000%20zeros-4FB3BE?style=flat-square)](#-frozen-data--automatic-file-selection)
[![Agreement](https://img.shields.io/badge/inter--language%20agreement-~1e--12-2EA043?style=flat-square)](#-expected-output-and-tolerances)
[![spinor64](https://img.shields.io/badge/spinor64-64%2F64%20GUE--consistent-3A6B4F?style=flat-square)](spinor64/README.md)
[![spinor38](https://img.shields.io/badge/Test--38%20ports-%C3%9710-C96F4A?style=flat-square)](#-spinor64-and-the-test-38-ports-added-in-v110)
[![Files](https://img.shields.io/badge/files-112%20%C2%B7%2093.7%20MB-3E515B?style=flat-square)](#-complete-file-inventory)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-3E515B?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

[Objections](#-what-is-verified--the-three-reviewer-objections) · [Layout](#-directory-layout-what-lives-where) · [How to run](#-how-to-run-every-language-copy-paste) · [Frozen data](#-frozen-data--automatic-file-selection) · [spinor64 / Test-38](#-spinor64-and-the-test-38-ports-added-in-v110) · [Tolerances](#-expected-output-and-tolerances) · [Summary](#-summary)

</div>

---

> Author of all codes and research: **Isaev, Iskhak Khamzatovich** ·
> ORCID [0009-0003-7299-0701](https://orcid.org/0009-0003-7299-0701) ·
> DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394)

All implementations read the same frozen ζ-zero datasets from [`data/`](data) and must agree
to numerical tolerance. Besides the classic "three reviewer objections" checks, this
directory also hosts two newer blocks added in v1.1.0:

- [`spinor64/`](spinor64) — the reference verification of **all 64 spinor structures** of the
  Klein quartic (it corrects the v21 monograph claim)
- `<lang>/spinor38/` — **Test 38 ports in 10 folders** (exact isospectrality inside a
  PSL(2,7) orbit + ⟨r⟩ via a hand-written Jacobi eigensolver)

## 🗂 Table of contents

<details open>
<summary><strong>Expand / collapse</strong></summary>

1. [🧪 What is verified — the three reviewer objections](#-what-is-verified--the-three-reviewer-objections)
2. [🗺 Directory layout (what lives where)](#-directory-layout-what-lives-where)
3. [🚀 How to run (every language, copy-paste)](#-how-to-run-every-language-copy-paste)
4. [❄️ Frozen data — automatic file selection](#-frozen-data--automatic-file-selection)
5. [🧬 spinor64 and the Test-38 ports (added in v1.1.0)](#-spinor64-and-the-test-38-ports-added-in-v110)
6. [📏 Expected output and tolerances](#-expected-output-and-tolerances)
7. [📖 Citing](#-citing)
8. [🔬 Deep dive — the ten-implementation parity matrix](#-deep-dive--the-ten-implementation-parity-matrix)
9. [📁 Complete file inventory](#-complete-file-inventory)
10. [📌 Summary](#-summary)

</details>

---

## 🧪 What is verified — the three reviewer objections

<div align="center">

<img src="assets/avatars.svg" alt="The verification cast: the ten languages, the frozen data, the spinor64 experiment and the spinor38 ports" width="680"/>

</div>

### Objection 1 — numerical stability / convergence of b(N)

**Claim:** the AB correction
`b(N) = (1/N) · Σₖ |γₖ − γ̃ₖ|`
(the mean distance between Gram-point approximations and true zeta zeros)
converges as N → ∞.

**Check:** compute b(N) for N = 100, 500, 1000, 5000, 10 000, 50 000 … and print a convergence
table with a log-log plot. The canonical Julia run gives b(50000) = 1.2126 (HARDCORE pass 2)
and an empirical law b(N) ≈ 7.0312 · N^(−0.1685), R² = 0.9895 (an alternative 1/log N fit
gives R² = 0.9994). The exponent is **empirical**: the monograph's α = 1/2 refers to the
Hofstadter AB-flux per plaquette, *not* to this convergence rate.

The v3.0 suite reproduces the canon bit-close: b(50000) = 1.2125526772588608 (Δ ≲ 8e-15
across languages), and on the regression grid N = 50·2^k (plus the last point) measures
b(N) ≈ 7.051 · N^(−0.1685), R² = 0.9888 — matching the canonical exponent −0.1685.

### Objection 2 — statistical significance (GUE)

**Claim:** the normalised spacings of zeta zeros follow GUE (Wigner–Dyson).

**Check:** the unfolded spacings
`sₖ = (γₖ₊₁ − γₖ) · log(γₖ / 2π) / (2π)`
are tested against the GUE (β=2) Wigner surmise
`p(s) = (32/π²)·s²·exp(−4s²/π)`, CDF `F(s) = erf(2s/√π) − (4s/π)·exp(−4s²/π)`,
with a Kolmogorov–Smirnov test and a Cramér–von Mises test. Criterion: p-value > 0.05
(H₀ "the zeros are GUE-spaced" is not rejected). The reference run reports
KS = 0.047 with p = 0.27 on 500 mpmath-certified zeros (Montgomery test), and
⟨r⟩ = 0.5848 ± 0.0260 against the GUE reference 0.5992.

> **v2.0.3 correction.** All ten language folders shipped the reference law as
> `1 − exp(−πs²/4)` — the **GOE (β=1)** surmise — while labeling it GUE. The v23 Julia
> reference suite already used the correct β=2 law, so its pinned numbers stand; the folder
> verifiers now match it. On the frozen first 500 zeros of `data/zeta_zeros_50000.txt` the
> corrected law gives KS D = 0.0495 (p = 0.168), where the old GOE-as-GUE law gave
> D = 0.1165 (p ≈ 0) — a false rejection of the true hypothesis.

> **v3.0 correction — the honest large-n outcome.** v2.x still printed "GUE not
> rejected" as an unconditional verdict. With the canonical kernel (Gram points
> solved from θ(t) = πk, GUE CDF via the 32768-point table) the suite now reports
> the raw statistics on all 50 000 zeros: mean spacing 0.999976 (unfolding
> validated), D = 0.021619, p ≈ 9.6e-21, W² = 8.178, A² = 61.49, ⟨r⟩ = 0.6119 vs
> the GUE surmise 0.5992. **The exact Wigner–Dyson surmise IS formally rejected at
> n = 50 000** — the known finite-T corrections of the zeta zeros, not a data
> artifact — while at n ≈ 500 it is not rejected (p ≈ 0.17). Both statements are
> now printed with their numbers; no canned verdicts remain. Additionally, the
> v2.x Gram points were the bare Lambert-W seed `2πk/W(k/e)` (three languages even
> had `2π·W(n/e)` — a factor n lost — and two hardcoded `17.44` for k = 0), so
> language implementations disagreed with each other by O(1) — far from the
> advertised ~1e-12. All ten now implement the identical Newton-refined canon
> and self-check 28 frozen anchors before printing any verdict (see
> `CANON_SPEC.md`).

The 50,000-zero distribution behind this objection, computed directly from
the frozen dataset:

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/visuals/charts/zeros_pair_correlation.dark.svg">
  <img src="../assets/visuals/charts/zeros_pair_correlation.light.svg" alt="Nearest-neighbour spacing histogram of the 50,000 frozen zeta zeros against the GUE and GOE Wigner surmises" width="780">
</picture>
</p>

> **How this chart relates to the verdicts above.** The histogram (n = 50,000,
> Riemann–von Mangoldt unfolding) shows the overall GUE-shaped level
> repulsion, and the ratio statistic ⟨r⟩ = 0.6119 stays GUE-class — but the
> honest v3.0 outcome stands: at n = 50,000 the *exact* Wigner–Dyson surmise
> is formally rejected by KS (known finite-T corrections of the zeros), while
> at n ≈ 500 it is not rejected. Both regimes are visible in the tail.

### Objection 3 — decay rate at large T

**Claim:** b(N) = O(1/√N), i.e. the log-log slope ≈ −0.5.

**Check:** linear regression of log b(N) vs log N with a 95% CI. The measured slope is
**not** −0.5; the honest verdict of the suite is that the convergence exponent is empirical
(see Objection 1). This is documented rather than hidden — every verdict in the suite is
printed with its raw numbers so a referee can disagree with the interpretation but not with
the arithmetic.

---

## 🗺 Directory layout (what lives where)

```
verification/
├── data/          # frozen ζ-zero datasets (up to 2,000,000 zeros)
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
├── java/          # JDK 8+         — Test-38 spinor38 port only
└── README.md      # this file
```

Every language folder contains the **same four files** (plus, since v1.1.0, a `spinor38/`
subfolder — see §5). The one exception is `java/`, which hosts only the Test-38
`spinor38/` port (no three-objection suite):

| File | Role |
|---|---|
| `ab_cloud_verify.<ext>` | bilingual module (auto-selects RU/EN at runtime) |
| `ab_cloud_verify_en.<ext>` | English-only version |
| `ab_cloud_verify_ru.<ext>` | Russian-only version |
| `run_verify.<ext>` (or `run_verify.sh`) | standalone CLI runner — one command, no library knowledge needed |

All files embed the function `load_zeros(data_dir, count, source)` which reads [`data/`](data)
with automatic file selection (§4).

---

## 🚀 How to run (every language, copy-paste)

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

# Java — Test-38 spinor port only: see verification/java/spinor38/
```

Each runner prints the three objection verdicts with raw statistics, writes a timestamped
report and saves plots next to the executable.

### CLI parameters (identical in all languages)

| Parameter | Default | Meaning |
|---|---|---|
| `--zeros N` | 5000 | how many ζ zeros to load |
| `--source NAME` | auto | `50k`, `500k`, `2M`, `highT`, `zeros6`, `csv`, `2M_gz`, `auto` |
| `--objection 1/2/3/all` | all | which objection to verify |
| `--lang en/ru` | auto | output language (auto = follow `LANG`) |
| `--data-dir PATH` | ../data | where the zero files live |

---

## ❄️ Frozen data — automatic file selection

| Requested zeros | File chosen |
|---|---|
| ≤ 13 661 | `data/zeta_zeros_50000.txt` |
| ≤ 500 000 | `data/zeta_zeros_500k_odlyzko.txt` |
| ≤ 2 000 000 | `data/zeta_zeros_2M_odlyzko.txt` |
| > 2 000 000 | `data/zeros6.txt` |

Full provenance, formats and column layout: [`data/README.md`](data/README.md).

---

## 🧬 spinor64 and the Test-38 ports (added in v1.1.0)

The experiment behind the ports, in one picture — all four holonomy classes
sit inside the GUE ensemble band:

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/visuals/charts/spinor64_classes.dark.svg">
  <img src="../assets/visuals/charts/spinor64_classes.light.svg" alt="Dot chart of the four spinor holonomy classes against the analytic GUE line and the ensemble confidence band" width="720">
</picture>
</p>

> **Data:** the per-class table of E2 (`spinor64/output/spinor64_table.csv`):
> ⟨r⟩ = 0.5935–0.6027 across classes, 64-structure mean 0.5984 ± 0.0035,
> min p_mc = 0.36 — no structure is statistically special.

`spinor64/` is the **reference Python implementation** that settled the spinor-uniqueness
question: **all 64 spinor structures of the Klein quartic give GUE-consistent statistics**.
PSL(2,7) splits them into orbits of sizes **28 / 21 / 7 / 7 / 1**; operators inside an orbit
are exactly isospectral (max\|Δλ\| ≈ 8.9·10⁻¹⁵); in the AB-cloud Hofstadter model (L = 44,
α = 1/2, Nv = 54 vortices, `:monumental` gauge) all 64 structures pass the MC GUE consistency
test, ⟨r⟩ = 0.5984 ± 0.0035, min p = 0.36. Details, data files and reproduction:
[`spinor64/README.md`](spinor64/README.md).

`<lang>/spinor38/` ports **Test 38** of that experiment to each language: it reads the frozen
classes from `spinor64/data/`, rebuilds the odd-orbit spectra with its **own hand-written
Jacobi eigensolver** (no LAPACK/BLAS), and checks exact isospectrality + ⟨r⟩. The C++ and
JavaScript builds were compiled and executed during v1.1.0 preparation: isospectrality
3.4·10⁻¹⁴, ⟨r⟩ = 0.4515710793 — **VERDICT PASS**. Each subfolder has its own README with exact
build/run commands. The Python reference folder has no separate `spinor38/` port —
`spinor64/` itself is the Python implementation — and the `java/` folder hosts only this
spinor38 port.

```mermaid
flowchart TD
    D["data/ — frozen ζ-zero datasets<br/>50k · 500k · 2M · highT · zeros6"] --> P["python/ (reference)"]
    D --> J["julia/ · cpp/ · fortran/"]
    D --> G["go/ · javascript/ · haskell/"]
    D --> RS["rust/ · matlab/ · r/"]
    P --> O["three objection verdicts<br/>with raw statistics"]
    J --> O
    G --> O
    RS --> O
    O -->|"must agree to ~1e-12"| V["one truth"]
    S["spinor64/ — 64 structures<br/>PSL(2,7) orbits 28/21/7/7/1"] --> S38["&lt;lang&gt;/spinor38/<br/>hand-written Jacobi eigensolver"]
    S38 -->|"isospectrality 3.4e-14 · PASS"| V
```

---

## 📏 Expected output and tolerances

A typical full run prints, per objection:

1. **Objection 1** — the b(N) table (N from 100 up to the dataset size) with the fitted power
   law, R², and the PASS/WARN/FAIL verdict against `bN_pass_threshold = 2.0`;
2. **Objection 2** — KS and CvM statistics with p-values, ⟨r⟩ with bootstrap error
   (n_bootstrap = 1000), the GUE ratio-law reference 0.5992(3);
3. **Objection 3** — log-log slope with 95% CI (tolerance band ±0.15 around the empirical
   exponent, `slope_ci_tolerance = 0.1` for CI width).

Numerical agreement between languages is expected at the level of double-precision round-off:
identical input zeros → identical b(N) tables to ~1e-12, identical KS statistics to ~1e-9.
Any larger deviation means the loader picked a different file — check `--source`.

**Measured v3.0 parity (6 machine-verified implementations on this repo's frozen data):**
`bN(50000) = 1.2125526772588608` — C++/Go/Rust/Julia/JS all within 8e-15 of the golden
and of each other (most anchors bit-identical, Δ = 0); `KS D = 0.0216193370329823` within
4e-16; slope −0.168466, CI [−0.1802, −0.1568] identical in C++/Go/Rust/Julia/JS.
Fortran/R/MATLAB/Haskell implement the same `CANON_SPEC.md` kernel with the same embedded
anchors and self-check at runtime wherever those toolchains are available.

**Self-check.** Every implementation starts with 28 frozen anchors
(lambert_w 6 · gram_point 8 · bN 7 · statistics 7, tolerances 1e-12…1e-6) from
`data/abcloud_golden.json` and exits non-zero if any anchor fails — the suite now
verifies *itself* before verifying anything else.

---

## 📖 Citing

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

## 🔬 Deep dive — the ten-implementation parity matrix

Ten independent implementations of the same suite live here: Python, Julia, C++, Fortran, Go,
JavaScript, Haskell, Rust, MATLAB and R. Each folder follows the same shape: the core
verifier, its `_en` and `_ru` reporting variants, a `run_verify` entry point, and (for the
compiled and research languages) a `spinor38/` subfolder with the Test-38 port. Parity means
something strict: all ten read the **same frozen data** from `data/`, run the **same 37
tests**, and must reproduce the **same reference statistics** — pair-correlation KS = 0.047
(p = 0.27), Byers–Yang flux defect 3.5e-15, ⟨r⟩ = 0.5848 ± 0.0260 against the GUE value
0.5992. A language that drifts from these numbers has a bug, not an opinion. (v2.0.3: the
spacing reference law itself was corrected in all ten folders — it was the GOE β=1 surmise
labeled as GUE; see the Objection 2 note above.)

Every entry point speaks the same flag language: `--zeros N` (number of zeros to use, 0 =
all; default 10 000), `--source NAME` (choose a dataset from `data/`: `auto`,
`zeta_zeros_50000`, `zeta_zeros_500k`, `zeta_zeros_2M`, `zeta_zeros_highT`, `zeros6`,
`zeta_zeros_50000_csv`), `--objection all|1|2|3` (run everything or a single objection test)
and `--lang en|ru` (report language). This uniformity is what makes the matrix testable: the
same command line can be replayed across all ten folders, which is exactly what CI does on
the interpreted subset.

Beyond the ten suites, this directory hosts the three specialized checkers: `spinor64/` (the
experiment that corrected the v21 monograph — all 64 Klein-quartic spinor structures
GUE-consistent, PSL(2,7) orbits 28/21/7/7/1), `spinor38/` ports inside the language folders
(Test 38 of the suite) and `sections/` (one-screen closed-form micro-verifications for
individual monograph sections). The data contract lives in `data/README.md`: nothing there is
generated at runtime, so every rerun of every program in every language sees byte-identical
input.

---

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `cpp/` | 7 files, 58.2 KB | directory |
| `data/` | 11 files, 91.0 MB | directory |
| `fortran/` | 7 files, 82.4 KB | directory |
| `go/` | 12 files, 41.8 KB | directory |
| `haskell/` | 8 files, 44.6 KB | directory |
| `java/` | 4 files, 12.4 KB | directory |
| `javascript/` | 7 files, 39.4 KB | directory |
| `julia/` | 8 files, 2.1 MB | directory |
| `matlab/` | 7 files, 58.6 KB | directory |
| `python/` | 5 files, 49.4 KB | directory |
| `r/` | 7 files, 64.3 KB | directory |
| `rust/` | 9 files, 48.0 KB | directory |
| `sections/` | 5 files, 9.6 KB | directory |
| `spinor64/` | 13 files, 114.9 KB | directory |
| `.gitignore` | 141 B | file |
| `README.md` | 19.0 KB | file |
| **Total (recursive)** | **112 files, 93.7 MB** | |

---

## 📌 Summary

Ten independent implementations of one numerical program share the same frozen data, the
same CLI and the same reference numbers; every verdict is printed with its raw statistics.
Besides the three-objection suites, the folder hosts `spinor64/` (all 64 Klein-quartic
spinor structures GUE-consistent), the Test-38 `spinor38/` ports (isospectrality 3.4e-14,
⟨r⟩ = 0.4515710793 — PASS) and the closed-form `sections/` micro-verifications. Expected
cross-language agreement is double-precision level (~1e-12 for b(N)); a drift from the
reference statistics is treated as a bug in the port, not an opinion.

---

<p align="center">
  <sub><em>Ten languages, one frozen dataset, one truth — a drift is a bug, not an opinion.</em></sub>
</p>

<div align="center">
<img src="../assets/svg/divider-cyan.svg" alt="—" width="100%" height="14"/>

<!-- AI end-cap — prompt P-02, registry: assets/prompts/AI_PROMPTS.md -->
<img src="../assets/banners/banner-verification.webp" alt="AI-rendered section art (prompt P-02)" width="100%"/>

<sub>🖼️ Section art: <a href="../assets/prompts/AI_PROMPTS.md">P-02</a> · palette <code>#05060f · #00e5ff · #ff2ec4 · #a78bfa · #ffd60a</code></sub>

<sub>⚡ Part of <a href="../README.md">AB-Cloud Research</a> — phase resonator for the zeros of the Riemann zeta function · <a href="../README.md">🏠 Root README</a></sub>
</div>

<!-- AB-ENRICHED:v2 · footer wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&height=85&color=0:00e5ff,55:0e1a4a,100:05060f&section=footer&animation=fadeIn" alt="" width="100%"/>
