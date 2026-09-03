# Canonical Julia Suite — `ab_cloud_v19.jl` (37 Tests, Two-Pass Protocol)

This folder holds the **canonical numerical program** of the project: a
single-file, dependency-free Julia suite that produces every number the
monographs quote. Language: Julia ≥ 1.10 (reference runs: Julia 1.12.0);
stdlib only — nothing to `Pkg.add()`.

## Files

| File | Size | What it is |
|---|---|---|
| `ab_cloud_v19.jl` | 16 110 lines | **canonical suite** — 37 tests, two-pass protocol, report engine (md/html/pdf/docx/png/svg/gif), interactive menu, Physics Lab (22 experiments), 3D lab (30 experiments) |
| `julia/` | 5 files, ~122 K lines | historical versions supplied by the author — see `julia/README.md` |

## The 37 tests, grouped

| Group | Tests | Verifies |
|---|---|---|
| Convergence | 1–3 | b(N) = (1/N)Σ|γₖ−γ̃ₖ| — table, monotonicity, rate; b(50000) = 1.2126, empirical law b(N) ≈ 7.0312·N^(−0.1685) (R² = 0.9895) |
| GUE statistics | 4–5, 9–17 | KS/CvM vs the GUE surmise, ⟨r⟩ = 0.5848 ± 0.0260 (GUE 0.5992), Σ²(L), Δ₃(L), K(τ), bootstrap CIs |
| Physics of the cloud | 6–8, 18–22 | Byers–Yang flux defect 3.5·10⁻¹⁵, Connes self-duality zero modes, AIII class, Dirac cone v_F ≈ 0.125 (R² = 0.9997), Berry R₂(0) |
| Spinor / topology | 23–28 | Arf invariant, PSL(2,7) orbit structure, zero-mode counts 2/3/3/3/7 |
| Robustness | 29–37 | chaos/decay rate, half-factorial γ, byte-level robustness, form factor K(τ), residual diagnostics |

(Verdict semantics: PASS / WARN / FAIL against thresholds printed with each
test; the WARN band is calibration, documented in the run reports.)

## Running

```bash
# fast CI check: 16×16 → 32×32, ζ ≤ 5000, both passes, ~3–5 min
julia code/ab_cloud_v19.jl --quick

# the full two-pass 37-test suite (30–60 min, 50 000 zeros, 72×72 → 96×96)
julia code/ab_cloud_v19.jl --test all

# one test only, single pass
julia code/ab_cloud_v19.jl --test 33 --no-two-pass

# interactive menu: 37 tests + Physics Lab (E-experiments) + 3D lab (30 tests)
julia code/ab_cloud_v19.jl
```

Useful flags: `--zeros N` (default 50000), `--source NAME`, `--matrix-size`,
`--quick`, `--test all|N`, `--no-two-pass`, `--lang en|ru`. `make quick-test`,
`make test-all`, `make menu` from the repository root do the same.

## What it writes

A timestamped run folder under `results/` (`run_YYYYMMDD_HHMMSS/`):
per-test subfolders with `report.{md,pdf,docx,html}`, `logs/` (computation
log + captured stdout), `plots/` (600 dpi PNG + SVG + PDF + GIF animations),
plus `FINAL_REPORT/` and an `index.html` cross-linking everything. The
committed example of such a run is `results/run_20260902_134759/` (plots
stripped for size — they regenerate).

## The two-pass protocol

Pass 1 runs every test on a moderate lattice; pass 2 ("HARDCORE") re-runs
the decisive checks at higher resolution (96×96) with the full 50 000-zero
sample. Only a test that passes **both** passes is reported PASS; this is
the anti-overfitting backbone of the monograph claims.

## Кратко (по-русски)

- `code/ab_cloud_v19.jl` — канонический набор: 37 тестов, двухпроходный
  протокол, генератор отчётов (md/html/pdf/docx/графика), интерактивное меню,
  Physics Lab и 3D-лаборатория; 16 тыс. строк, без внешних пакетов Julia.
- Запуск: `--quick` (быстрый CI), `--test all` (полный прогон 30–60 мин),
  `--test N`, меню без аргументов.
- Результаты пишутся в `results/run_<метка>/` с отчётами, логами и
  графиками; образец — `results/run_20260902_134759/`.
- `julia/` — авторские исторические версии (v19_v1, v20, v21) для прослеживания.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `julia/` | directory, 6 files inside | folder |
| `README.md` | 3.8 KB | markdown guide |
| `ab_cloud_v19.jl` | 1.2 MB | Julia source |
| `ab_cloud_v21.jl` | 1.7 MB | Julia source |
| **Total (files)** | **3.0 MB** | 3 files + 1 subdirectories |

## 🔬 Deep dive — the canonical suite and its supporting library

`code/` is the computational heart: **12 MB** of Julia sources whose
canonical entry point is `ab_cloud_v19.jl` — the two-pass, 37-test suite
behind every verdict on the front page. The suite structure is
deliberately old-fashioned: one file, numbered tests, explicit verdict
printing, no hidden framework. A reviewer reads it top to bottom and sees
every constant, every tolerance and every statistical decision — nothing
lives in a config file or an environment variable.

Run profiles (the same file serves all three):

| Profile | Command | Ladders | ζ zeros | Time |
|---------|---------|---------|---------|------|
| Quick | `julia ab_cloud_v19.jl --quick` | 16×16 → 32×32 | ≤ 5000 | ~3–5 min |
| Full (two-pass) | `make test-all` | 72×72 → 96×96 hardcore | 50 000 | 30–60 min / pass |
| Interactive | `make menu` | pick tests, Physics Lab, 3D lab | — | interactive |

The flagship run that produced the committed ledger took **≈ 9 h 46 min**
wall time with artifacts enabled — per-test durations are stamped in the
report log and reproduced in the root README ledger. Pass 2 ("hardcore")
re-runs each test with tightened tolerances and decomposed sub-checks;
selected tests add a series pass 3. A test only counts as green when every
tier agrees.

Version lineage lives in [code/julia/](julia/): the v19/v20/v21 sources
are kept as supplied, so a verdict quoted from an older monograph can be
re-run against the *exact* code revision that produced it — versioned
science, not vibes.
