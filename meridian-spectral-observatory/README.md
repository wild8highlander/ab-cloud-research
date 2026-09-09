# 🧭 MERIDIAN SPECTRAL OBSERVATORY

**Language / Язык:** [🇬🇧 English](README.md) · [🇷🇺 Русский](README.ru.md)

**A suite of verification codes for the "AB-Cloud" project — from the lattice Aharonov–Bohm model to the statistics of the zeros of the Riemann zeta function.**

> Author of all codes and research: **Isaev, Iskhak Khamzatovich**
> ORCID: [0009-0003-7299-0701](https://orcid.org/0009-0003-7299-0701) · DOI: [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394)
> Related repositories: [research-papers](https://github.com/wild8highlander/research-papers) · [ab-cloud-research](https://github.com/wild8highlander/ab-cloud-research)

---

## ⚡ What this is — in a nutshell

This is a **laboratory of 24 self-contained Julia codes and one Python code** that test one big idea — the **Hilbert–Pólya conjecture**: that the non-trivial zeros of the Riemann zeta function ζ(s) behave like the spectrum (the set of energy levels) of some quantum system. The folder name — *Spectral Observatory* — captures the spirit: we **watch spectra** — of lattice AB-cloud Hamiltonians and of the zeros of ζ(s) — and compare their fingerprints.

Technically, each file is a **standalone "supercombo" bench**: open one file in Julia and you get an interactive console menu with dozens of tests, plots, reports and a built-in self-check system. No project-external modules, no builds: copy the file — it works (or honestly tells you what is missing).

The three pillars of the project:

1. **The AB cloud** — a lattice quantum model: a Hamiltonian on an L×L lattice with **magnetic-flux vortices** (the Aharonov–Bohm effect, flux α per vortex). The spectrum of this Hamiltonian is our "experimental material".
2. **The zeros of ζ(s)** — 50 000 real zeta zeros (file `zeros50k.txt`, from 14.134725142 to 40433.687385) — the "reference standard" we compare against.
3. **GUE statistics** — random matrices of the Gaussian Unitary Ensemble (β=2): the reference nearest-neighbor level statistics (⟨r⟩ ≈ 0.5996, band [0.5772, 0.6212]). The zeros of ζ(s) are known to follow GUE — the question is: **at which parameters does the AB cloud reach GUE as well?**

---

## 🏆 Headline result (Gate H5, L=72, 2026-09-09)

40 dense eigensolves of 5184×5184 matrices, 4 regimes × 7 realizations + α-profile, 46 minutes on a smartphone:

| Regime | Vortex density | Flux α | ⟨r⟩ | in GUE band | individual KS pass | median KS_D | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| **A** baseline | Nv=4 (0.08%) | 0.5000 | 0.5898±0.0102 | 6/7 | 0/7 | 0.3531 | misses GUE |
| **B** monograph density | Nv=144=L²/36 (2.78%) | 0.5000 | 0.6000±0.0052 | 7/7 | 1/7 | 0.0559 | GUE reached — *OR-clause only* |
| **C** sharp flux | Nv=4 (0.08%) | 0.0278 | 0.5937±0.0041 | 7/7 | 0/7 | 0.0646 | GUE reached — *OR-clause only* |
| **D** combined | Nv=144=L²/36 (2.78%) | 0.0278 | 0.6003±0.0050 | 7/7 | **7/7** | **0.0148** | **GUE reached (clean)** |

**Reading:** GUE statistics recover in regimes B, C, D, but only the combination **[D] = monograph density + sharp flux α = 25/900 passes cleanly** (every single realization passes the KS test at p > 0.01; median KS_D is 2× below the critical value d_crit = 1.63/√n ≈ 0.031). The published baseline regime [A] is a systematic outlier (median D ≈ 0.35, worsening with L). Full interpretation: [docs/05](docs/05_gate_H5_regimy.md).

---

## 🗺️ Repository map

### 🔬 Main line: `ab_cloud_v*.jl` — Verification Suite

| File | Lines | What it is |
|---|---:|---|
| `ab_cloud_v19.jl` | 23 342 | v19.1 — 37 tests, Hilbert–Pólya focus + advanced RMT diagnostics |
| `ab_cloud_v19_v1.jl` | 23 956 | evolution of v19 |
| `ab_cloud_v20.jl` | 24 596 | intermediate evolution |
| `ab_cloud_v21.jl` | 25 519 | v21 — 38 tests + Physics Lab + 3D Lab (sparse engine) |
| `ab_cloud_v21_v1.jl` | 25 519 | v21 fixes |
| `ab_cloud_v22.jl` | 7 369 | v22.2 — journal-grade plotting engine (module `ABPlotV23`), THREE-PASS Test 38 |
| `ab_cloud_v23.jl` | 28 281 | start of the v23 line |
| `ab_cloud_v23_v1.jl` | 29 904 | evolution of v23 |
| **`ab_cloud_v23_v2.jl`** | **30 908** | ⭐ **SUPERCOMBO v23.6 — the most complete bench**: v21 core (38 tests + Physics Lab + 3D Lab) × v22 plotting engine × THREE-PASS Test 38 (38a+38b hardcore+38c ladder), H1 deepen-protocol, H5 α-profile, decoy controls, presets FAST L=16 / FULL L=56 |

Files with the **`_D`** suffix are the same versions with the **MERIDIAN DESIGN SYSTEM v1.0**: a unified console identity (double-frame banners, ◆-sections, ✓/✗/⚠ statuses, live ▰▰▰▱▱ progress bars, true-TTY colors). The physics and the numbers are bit-identical: only the console "clothing" changes.

### 🎯 HP·MERIDIAN: `hp_audit_standalone.jl` (v24.2-SA)

| File | Lines | What it is |
|---|---:|---|
| **`hp_audit_standalone.jl`** | **6 054** | ⭐ Compact standalone audit of **gates H1–H7 only** (the Hilbert–Pólya hypothesis). The core is lifted VERBATIM from v23_v2 — with equal seeds the numbers match bit-for-bit. Plus: H5 budget ≤ 40 diagonalizations (v24.1), the targeted **FOCUS-D** mode (`hp_regime_mode = :regime_d`, command `5d`, v24.2), a live progress bar during LAPACK calls, a 60 s heartbeat (v23.8), environment doctor, battery cost estimation |

The 7 gates: **H1** PRIME-TRACE (Bragg comb at ω = log p + composite decoy controls + regime-matched null models + deepen protocol P95) · **H2** WEYL-DOS (N(E) ladder, AICc showdown) · **H3** POWER-LAW (exponent ladder, dictionary falsification) · **H4** CRITICAL-Q (sharpness scan + domain guard) · **H5** REGIME-2×2 (4-regime ensemble showdown + α-profile: finetuning vs plateau) · **H6** HERMIT-STRESS (self-adjointness/stability) · **H7** SEQ-CORR (levels↔zeros correlation).

### 🌀 RH line: maximizing the correlation of the AB cloud with the zeros of ζ(s)

| File | Lines | What it is |
|---|---:|---|
| `RH_Unified.jl` | 1 885 | single self-contained file: 500 real ζ-zeros, 61 "magic" α-points, 6 vortices (hexagon), RHConfig (33 parameters), jitter, 4 vortex layouts, 9 presets |
| `RH_Unified_v5.jl` | 2 204 | evolution: extended presets and diagnostics |
| `RH_Sweep_Pro.jl` | 6 450 | ⭐ **professional parameter sweep**: 13 661 real ζ-zeros (mpmath.zetazero, 25 digits), dynamic sweep of 8 parameters over 10 key points, CSV/TXT(ASCII)/JSON reports, Plots.jl graphics, timing logs |

### 🏛️ Monumental line

| File | Lines | What it is |
|---|---:|---|
| `AB_Cloud_Monumental_v6_3.jl` | 7 759 | module `AB_Cloud_Monumental` — a Julia port of the Python code base: **V01–V112** verifications of the AB-Cloud monograph. `run_all()`, `run_all(quick=true)`, `run_only(["V11","V35"])`; clean CSV + JSON + PNG dashboard; optional Arpack.jl (large L) and Plots.jl |

### 🧰 Utilities and libraries

| File | Lines | What it is |
|---|---:|---|
| `Magic_Alpha_Points_v1.jl` | 131 | library of **61 "magic" α-points**: π/30…π×5, √2…√15, rationals, φ, e, ln(2), 1/e, 1/π and specials — from the original RMT study of the AB cloud |
| `test11_honest.jl` | 322 | honest recalibration of Test 11 (Anderson–Darling GOF of ζ-zero spacings vs the Wigner surmise GUE β=2): removes the bootstrap artifact of ties (49 999 draws from a pool of ~8 000), the null is built i.i.d. from `gue2_surmise_cdf` |
| `test11_honest.py` | 178 | the same protocol in Python (default input — `zeta_zeros_50k.txt`) |

### 📊 Data and configuration

| File | Size | What it is |
|---|---:|---|
| `zeros50k.txt` | 50 000 lines | **50 000 real zeros of ζ(s)**, one per line: 14.134725142 … 40433.687385462 |
| `zeta_zeros_50k.txt` | 5 000 lines | the same 50 000 zeros, 10 per line (format for `test11_honest.py` etc.) |
| `p_myset.cfg` | 37 lines | the "myset" configuration profile for HP·MERIDIAN: `hp_L=20`, ensemble 8, seed 2026, ladder lattice [16,20,24], showdown mode, etc. |

---

## 🚀 Quick start

Requires [Julia](https://julialang.org) ≥ 1.10 (tested on 1.12). The main benches use **only the standard library** — no packages to install.

```bash
# 1) Supercombo bench (38 tests, interactive menu)
julia -e 'include("ab_cloud_v23_v2.jl")'

# 2) Compact HP audit H1–H7 (7 gates, the meridian> console)
julia -e 'include("hp_audit_standalone.jl")'

# 3) Monumental verifications V01–V112
julia -e 'include("AB_Cloud_Monumental_v6_3.jl"); AB_Cloud_Monumental.run_all(quick=true)'

# 4) Honest test 11 (Python)
pip install mpmath numpy   # if not yet installed
python3 test11_honest.py
```

Important: **the zero data files sit next to the code on purpose** — the codes look for `zeros50k.txt` in the script directory (`@__DIR__`), in the working directory (`pwd()`), and via the `HP_ZEROS` environment variable / the console command `z`.

### Typical runtimes (mid-range smartphone, Termux)

| Run | Time |
|---|---|
| HP·MERIDIAN `:smoke` (L=20, validation) | ~ minutes |
| HP·MERIDIAN `f` FAST (L=72, H5 with the 40-solve budget) | **46 min** (measured 2026-09-09) |
| HP·MERIDIAN `F` FULL (L=56, deep) | hours |
| H5 single solve 64×64 (4096×4096 eigen) | ~ 49 s |
| H5 single solve 72×72 (5184×5184 eigen) | ~ 69 s |
| test11_honest | seconds–minutes |

> Each diagonalization is a dense L²×L² problem (e.g. L=72 → 5184×5184). Cost grows as ≈ L⁶, memory as ≈ L⁴.

---

## 📚 Full documentation (`docs/`)

The documentation is deliberately thorough — from "what is the AB cloud" to bit-level interpretation of verdicts (the documents are in Russian; the tables and formulas are universal):

| Document | Contents |
|---|---|
| [01 · Project overview](docs/01_obzor_proekta.md) | the science case, the Hilbert–Pólya hypothesis, project history |
| [02 · Code catalog](docs/02_katalog_kodov.md) | every file: what it computes, which tests, how to run |
| [03 · Launch guide](docs/03_rukovodstvo_zapuska.md) | installing Julia (Termux/Linux/Windows), all presets and menus, dependencies |
| [04 · Physics and mathematics](docs/04_fizika_matematika.md) | the AB cloud, vortices, flux α, GUE, ⟨r⟩, KS, Anderson–Darling, gates H1–H7 |
| [05 · Gate H5 and regimes](docs/05_gate_H5_regimy.md) | regimes A/B/C/D, the 40-solve budget, FOCUS-D, real-run walkthroughs 16×16, 64×64 and 72×72 |
| [06 · ζ-zero data](docs/06_dannye_zeta_nulej.md) | provenance, formats, GUE-check of the data themselves |
| [07 · Version chronology](docs/07_hronologiya_versij.md) | the full evolution: RH_Unified → Sweep → Monumental → v19…v23.6 → v24.2 |
| [08 · Reproducibility](docs/08_reproduciuemost.md) | seeds, profiles, honest verdicts, known caveats, checklist |

---

## 📖 How to cite

```bibtex
@misc{isaev2026abcloud,
  author       = {Isaev, Iskhak Khamzatovich},
  title        = {AB-Cloud Verification Suite: Meridian Spectral Observatory},
  year         = {2026},
  doi          = {10.5281/zenodo.21825394},
  orcid        = {0009-0003-7299-0701},
  url          = {https://github.com/wild8highlander/ab-cloud-research}
}
```

See also [CITATION.cff](CITATION.cff).

---

## ⚠️ Research status and honest caveats

The project is in an **active audit stage**: the codes follow the principle "an honest verdict matters more than a pretty one" — WARN is never disguised as PASS, null models are regime-matched, decoy controls must stay silent while the primes are heard, and the compute budget is declared before the run and never exceeded. The current results (72×72, Gate H5, 2026-09-09) point to **regime D (monograph density + sharp flux α = 25/900) as a clean GUE candidate: 7/7 individual KS passes, median KS_D = 0.0148 against the 0.031 threshold, ⟨r⟩ = 0.6003±0.0050 — right on the GUE asymptote**, while the baseline regime A is systematically off (median D ≈ 0.35). The gate verdict is PARAMETER-DEPENDENT: GUE recovers in B, C, D, but cleanly only in D. This is not yet a claim of proof — see the "Known caveats" section in [doc 08](docs/08_reproduciuemost.md) and the run walkthrough in [doc 05](docs/05_gate_H5_regimy.md).

All the code consists of self-contained research benches without project-external dependencies; the rights belong to the author (see CITATION.cff).
