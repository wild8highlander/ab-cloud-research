# AB-Cloud Multi-Language Ports

Full computational analogs of the **meridian-spectral-observatory** suite
(`ab_cloud_full.jl`, `hp_audit_standalone.jl`, `AB_Cloud_Monumental_v6_3.jl`)
in four languages: **Python, C++, Rust, Go** — with a golden selftest
verified against the **unmodified Julia originals**.

---

## Quick start

| Language | Build / run | Verification |
|----------|-------------|--------------|
| Python 3.8+ | `python3 -m abcloud …` (package `ports/python/abcloud/`) | `python3 -m abcloud selftest` |
| C++17 | `g++ -O2 -std=c++17 -o abcloud abcloud_port.cpp` | `./abcloud selftest` |
| Rust | `cargo build --release` | `./target/release/abcloud selftest` |
| Go | `go build -o abcloud .` | `./abcloud selftest` |

Every `selftest` recomputes **133 reference numbers** from
`ports/golden/abcloud_golden.json` — a file of anchors generated from the
original Julia code by `ports/golden/gen_golden.jl` — and prints a
PASS/FAIL verdict per check.

Verification status (golden selftest):

| Port | Golden selftest | Suite (25 tests) |
|------|-----------------|-------------------|
| Python | **133/133 PASS** | 19 PASS, 0 FAIL, 3 WARN, 3 INFO |
| C++ | **133/133 PASS** | 19 PASS, 0 FAIL, 3 WARN, 3 INFO |
| Rust | **133/133 PASS** | 19 PASS, 0 FAIL, 3 WARN, 3 INFO |
| Go | **133/133 PASS** | 20 PASS, 0 FAIL, 2 WARN, 3 INFO |

## CLI (identical across languages)

```
selftest                      — golden parity check against the Julia originals (133 checks)
zeros  [--data P] [--n N]     — full zero-analysis battery
                                (KS / CvM / A² / χ² / <r> / Σ² / Δ₃ / K(t) / H1-SNR)
suite  [--test N|all]         — portable subset of the 39-test suite
ham    (Python only)          — Hamiltonian scenarios + exact-theorem checks
bN     --N n… [--offset k]    — the b(N) statistic
gram   --n n…                 — Gram points
test11 --mc N --seed S        — honest Anderson–Darling test + MC null
hp     [--data P] [--n N]     — H1 primary detector (Bragg peaks at ω = log p)
sweep  --N n…                  — b(N) ladder sweep
```

## The golden system

* `ports/golden/gen_golden.jl` includes the **unmodified** originals
  (`ab_cloud_full.jl`), runs every section and writes JSON with `%.17g`.
* All Σ²/Δ₃ window sampling uses the **classic MT19937** (init_genrand),
  embedded identically in all five programs (including the generator) —
  window sampling is bit-identical across languages.
* The frequency grids ω (726 points) and t (30 points) are stored in the
  JSON — no dependence on language `colon`/`arange` semantics.
* Tolerances: 1e-9 rel on purely scalar sections; 1e-7 rel on special
  functions (cross-libm exp/log: openlibm vs glibc ~2e-8); 1e-8 abs on
  eigen-anchored sections (LAPACK zheevr vs the ports' Jacobi solver);
  1e-6 rel on the H1/K(t) Fourier sums.

## What is ported (computational kernel, 1:1 with the original)

* **Scalar math**: Lanczos lgamma, regularized incomplete gamma (series +
  Lentz continued fraction), exact χ² CDF (any df), asymptotic KS p-value
  (dual theta series with the correct −2k²λ² exponent), Wigner surmises
  GUE β=2 / GOE β=1, Lambert W₀ (Halley), Gram points (corrected theta
  asymptotics 1/(48t)+7/(5760t³)), the b(N) ladder.
* **RMT reference-law engine**: CDF interpolation table (32768 points,
  |ΔF|≤1e-9), inverse-CDF quantile grid (4096, 48 bisections) — the
  law-exact MC sampler of Test 11.
* **GOF statistics**: KS (Stephens correction), two-sample KS with full
  tie discipline, Cramér–von Mises W², Anderson–Darling A², χ² histogram
  (overflow bin, exp≥5 gate), ⟨r⟩ (0/0 degeneracy guard), smooth counting
  function N̄(T), unfolding, Σ²(L), Δ₃(L) (via linreg residuals, as in the
  original), two-level form factor K(t) with local unfolding and smoothing.
* **AB-cloud lattice**: Vortex, ABCloudConfig, the monumental smooth-gauge
  vertical-bond phase (atan2 differences ·0.5), the :dirac model (smooth
  part + explicit Dirac string: −2πq up-bond, +2πq down-bond, torus
  branch), vortex Coulomb potential + residual disorder ε (see below),
  Hermitian symmetrization (H+H†)/2, canonical plaquette_flux (CCW sum of
  angle(−H)), flux_circdist (circular distance — ±π branch phantom guard),
  central band extraction.
* **HP audit (H1)**: raw-position periodogram detector
  P(ω)=|Σwₖe^{−iωTₖ}|²/Σwₖ² (Hann window), SNR yardstick vs the band
  median over 0.3:0.004:3.2, PASS/STRONG verdicts (≥4 of 6 prime harmonics
  above SNR 10 / all above 100), GUE envelope K_box(t)=t(1−sinc(2πt)),
  AICc, Wald CI, Spearman (average ranks), fluctuation high-pass.

## Exact theorems (verified against the original)

| Theorem | Golden anchor |
|---------|--------------|
| Byers–Yang (q→q+1, neutral config, :dirac) | 2.66e-15 |
| Dirac-string flux (plaquette_flux, :dirac) | 1.78e-15 |
| Chiral AIII (α=1/2, W=0) | exactly 0 |
| Connes α↔1/α defect (open, W=0, boundary-spoiled) | 0.359127159… |
| b(50000) | 1.21255267725886… |
| A² (full zero set) | 61.4924262420973 |
| ⟨r⟩ of the zeros (n_r=49998) | 0.611879890720840 |

## Documented port deviations

1. **Disorder at W>0**: ε ~ U(−0.01,0.01) is drawn from the classic
   MT19937 (seed = disorder_seed). The original uses Julia's built-in
   dSFMT, which no other language reproduces. **All golden anchors use
   W=0**, where no ε is drawn at all.
2. **Eigenvalues**: cyclic Jacobi for Hermitian matrices (C++/Rust/Go)
   instead of LAPACK zheevr — agreement ~1e-12, inside the golden
   tolerances 1e-7/1e-8.
3. **Suite lattice sizes**: without LAPACK, statistical tests 12/16/34 in
   C++/Rust/Go use lattices 200²/24²/28² (Python uses 400²/32²/40² via
   numpy). These are STATISTICAL tests with finite-size-calibrated gates;
   the golden selftest uses the full sizes (64/100/144) and is verified
   everywhere.
4. **Suite coverage**: 25 of 39 tests are ported (the computational
   core); the other 14 print an honest `[SKIP]` with a reason (graphics,
   specialized protocols, dSFMT-dependent disorder).

## Layout

```
ports/
├── golden/
│   ├── gen_golden.jl           — reference generator from UNMODIFIED Julia
│   └── abcloud_golden.json     — 133 anchor numbers + ω/t grids
├── python/abcloud/             — canonical package (mt19937, special,
│                                 rmt_table, gof, lattice, unfold, hp_audit,
│                                 golden, suite, cli)
├── cpp/abcloud_port.cpp        — single-file C++17 port (same CLI)
├── rust/ (Cargo)               — single-file Rust port (std only)
├── go/main.go + go.mod         — single-file Go port (std only)
├── PORT_SPEC.md                — parity specification (golden format,
│                                 tolerances, MT19937, porting rules)
└── README.md / README.ru.md    — this file
```

## Regenerating the golden

```bash
julia ports/golden/gen_golden.jl <meridian_dir> <out.json>
# default: julia ports/golden/gen_golden.jl . ports/golden/abcloud_golden.json
```

Requires Julia 1.10+ with stdlib (LinearAlgebra, DelimitedFiles, Printf)
and the `zeros50k.txt` file in the meridian directory root.
