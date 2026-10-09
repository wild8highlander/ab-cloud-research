# Changelog

## [1.3.0] — 2026-10-10 — «CI green, Pages pinned, the formal layer»

### Fixed
- **CI is green again.** The `structure` job of `ci.yml` and both steps of
  `julia.yml` still referenced `code/ab_cloud_v19.jl`, deleted in the
  "Hilbert Polya" consolidation commit — every push failed. All workflows
  now target the canonical v23 suite (`--test 1` smoke + manual full run),
  the canonical-artifact list covers the formal layer, and the dependabot
  action bumps (`checkout@v7`, `markdownlint-cli2-action@v24`, `stale@v11`,
  `setup-julia@v3`, `release-drafter@v7`) are applied.
- **`code/julia/README.md` rewritten** — it documented the removed
  historical sources (v19/v19_v1/v20/v21) as if they were still present.
- **GitHub Pages reproducibility.** `deploy-docs.yml` pins the exact
  MkDocs stack (mkdocs 1.6.1 / material 9.7.7 / minify 0.8.0) the site is
  verified with, and `mkdocs build --strict` passes.

### Added
- **The formal verification layer** ([`formal/`](formal/README.md)):
  - `formal/lean4/` — a full Lean 4 project (toolchain v4.19.0, **zero
    external dependencies**, no Mathlib): machine-checked theorems over
    ℕ/ℤ (b(N) sum nonnegativity/monotonicity/additivity/triangle, Gram
    offset lattice, flux certificates, PSL(2,7/8/13) orders, Klein orbit
    decomposition, Tr(AB) = Tr(BA)) **plus the `abcloud-verify`
    executable** — a Float64 port of the Python reference pipeline that
    re-derives the frozen reference numbers from
    `verification/data/zeta_zeros_50000.txt`: **8/8 checks PASS,
    Δ = 0.000000** (b(100…5000), KS D = 0.0991866231, CvM W² =
    17.6048550189, slope −0.1831023444, R² 0.9946087105), exit-code-gated.
  - `formal/coq/` — the exact core over ℤ (`lia`/`nia`/`ring`).
  - `formal/agda/` — builtins-only development; positivity of b(N) is a
    typing fact.
  - `formal/isabelle/` — `Main`-only HOL session.
  - `formal/assets/` — the section banner and seal (SVG).
- **`formal.yml`** — four independent CI jobs (lean4 / coq / agda /
  isabelle) running on every push and PR.
- **`.yamllint.yaml` + `.markdownlint-cli2.jsonc`** — real linter configs;
  the `ci.yml` markdown job now lints a curated 61-file surface with a
  reviewed rule set and the YAML job enforces the project config.
- **Docs site**: new `formal.md` (formal verification) and `map.md`
  (repository map) pages, nav regrouped, `docs/index.md` cards updated.
- **Makefile**: `smoke` and `formal`/`formal-lean/coq/agda/isabelle`
  targets; `quick-test`/`test-all`/`menu` target the v23 suite.

### Changed
- **Root README redesigned** (EN): new banner (`assets/banner-v2.svg`),
  formal-verification badge row, a mermaid repository-architecture
  diagram, the formal verification section with the re-derivation ledger,
  LaTeX display math, updated quick start / Makefile reference / CI-CD
  table / repository map / glossary / roadmap; the Russian duplicate
  section was retired (EN is now the single source of truth; RU content
  remains in the subprojects and the git history).
- All canonical-suite references across the repo (README, docs/, code/,
  verification/, .github templates, Makefile) updated from v19 to v23;
  historical v18/v19 run-artifact references intentionally preserved.


## [1.2.1] — 2026-09-04 — «the front page, restored and tripled»

### Fixed
- **Landing-page hijack removed.** `.github/README.md` (added in v1.2.0)
  silently replaced the root README on the repository home page — GitHub
  resolves `.github/README.md` ahead of the root README — so the banner,
  the badge wall and all front-page content disappeared for visitors.
  The infra guide moved to `.github/WORKFLOWS.md` (content unchanged) and
  the full front page is the landing page again.

### Added
- **Root README tripled in size** (37 KB → 107 KB, 534 → 1,575 lines) with
  big data straight from the stored computations: a 24-row *Computation
  data at a glance* table; the **complete 38-test ledger** of the flagship
  run (test-by-test verdicts with artifact links); the **full spinor64
  data** (E1 orbit table 28/21/7/7/1, E2 four holonomy classes, ensemble
  ⟨r⟩ = 0.5984 ± 0.0035); **real per-test wall-clock timings** (9 s …
  1 h 06 m); the **ζ dataset inventory with real SHA-256 checksums** of
  all nine frozen files (2,001,058 zeros, 91 MB); flagship artifact
  inventory (453 files / 39 directories); a statistical deep-dive (⟨r⟩,
  finite-T story, Montgomery R₂, topology at machine precision, Dirac
  R² = 0.9997); the annotated gallery of all 19 monograph plates at
  600 dpi; a ten-language cross-verification matrix; monograph editions
  matrix; Makefile reference; CI/CD table; reading paths; FAQ; glossary;
  a verification-history timeline; eight extra badges (Release, Version,
  **strictly personal License**, Suite 37×2+38, 2,001,058 ζ zeros,
  Android/Termux, 453 artifacts, Spinor64 64/64); and a Russian section
  with the big-data table, the full 38-test registry, checksums and a
  mini-glossary.

## [1.2.0] — 2026-09-03 — «documentation deep dive»

### Added
- **Deep-dive README in every directory** (32 files): root README gains a
  Documentation map, a Branches & versions section and a corrected
  Highlights table; every folder of the repository now ships an English
  README ending with a short Russian summary (`Кратко по-русски`):
  `code/`, `code/julia/`, `verification/` + all 10 language folders +
  `data/`, `spinor64/`, `sections/`, `monographs/` + `ru/en/zh` +
  `original-v21/`, `lab-3d/` + `code/`, `outputs/`, `results/`, `apps/` +
  both applications, `docs/`, `termux/` (new English guide), `assets/`,
  `.github/`. Every README documents contents file-by-file, stored result
  values with their provenance, run commands and expected output.
- Root README: Highlights row for the spinor structures corrected to the
  gone); roadmap updated to v1.2.0.

## [1.1.0] — 2026-09-03 — «spinor64 verification + run artifacts + apps»

### Added
- **`verification/spinor64/`** — independent reference implementation and full
  run over all 64 spinor structures of the Klein quartic: PSL(2,7) orbits
  28/21/7/7/1 (28 odd Arf=1 — bitangents, transitivity confirmed), EXACT
  isospectrality within orbits (max|Δλ| ≈ 8.9e-15), gauge invariance
  7.1e-15, zero modes 2/3/3/3/7; AB-cloud Hofstadter statistics:
  **64/64 structures GUE-consistent** (⟨r⟩ = 0.5984 ± 0.0035, MC reference

- **Test 38 ports in 10 languages** — `verification/<lang>/spinor38/`
  (C++/JS compiled+run here: isospectrality 3.4e-14, ⟨r⟩ = 0.4515710793,
  VERDICT PASS; Java/Rust/Go/Fortran/Haskell/R/MATLAB sources with build
  docs) reading the frozen data files `verification/spinor64/data/`.
- **`code/julia/`** — full sources of the suite v19 / v19_v1 / v20 / v21
  (as supplied), plus the extracted 50,000-zero embedded dataset
  `verification/data/zeta_zeros_50000_embedded.txt`.
- **`results/run_20260902_134759/`** — the complete v19 two-pass run of
  2026-09-02 (37 tests, 72×72 → 96×96 HARDCORE, Julia 1.12.0): per-test
  reports (md/pdf/docx/html), computation logs, FINAL_REPORT, index.html —
  453 files (reports+logs; the run's PNG plots are excluded — they are
  regenerated by the suite).
- **`apps/`** — two React applications (React 18 + Vite, prebuilt `dist/`
  committed, GitHub Pages ready):
  - `ab-cloud-dashboard` — 37-test verdict dashboard + real-time ζ
    statistics (b(N), ⟨r⟩, KS vs GUE ratio law, Σ², Δ₃) in a Web Worker +
    in-browser 64-spinor Jacobi verification;
  - `ab-cloud-lab3d` — WebGL 3D laboratory: Hofstadter lattice with
    vortices, Dirac cone, ζ critical strip (self-anchored Euler–Maclaurin
    ζ evaluator).
- **Monograph v21.1 (RU+EN corrected editions)** — errata note, corrected
  sections 3.1/3.2/3.2.1, new section 3.2.5 with the spinor64 results;
  rebuilt as `*_corrected.docx/html/pdf`.
- **Monographs v22.1 (RU/EN/ZH)** — Appendix B updated to the
  `run_20260902_134759` two-pass artifacts; new Appendix D (spinor64);
  LaTeX sources committed (`*.tex`); rebuilt `*_v221.docx/html/pdf`.

### Changed
- README: new sections for spinor64, Test-38 ports, React apps, code/julia,
  and the run artifacts.
- `monographs/original-v21/README.md`: v21.1 corrections documented.

All notable changes to the **AB-Cloud Research** repository are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Android/Termux push kit** — `termux/install_and_push.sh` +
  `termux/README_RU.md` + root cheat-sheet `HOW_TO_PUSH_FROM_ANDROID.md`:
  one-command publication of this repository to GitHub straight from an
  Android phone. The script auto-installs missing packages (git/curl/gh),
  relocates the repo out of shared /sdcard storage into Termux home,
  offers two login modes — **PAT token** (hidden input, pre-verified via
  GitHub API incl. push-permission check) or **browser device-flow**
  (GitHub CLI one-time code at github.com/login/device) — then pushes
  `main` + tags, verifies the remote SHA via `ls-remote` and opens the
  repo in the browser. Token exists in process memory only. Also shipped
  as a standalone `termux-push-kit.zip` and inside the main archive.

### Planned
- Full 37-test suite as a scheduled nightly CI job
- Interactive browser dashboard for verification results
- Quantum Hadamard-walk & 2D e⁻/e⁺ jet hydrodynamics extensions

## [1.0.0] - 2026-08-28

### Added
- **Monographs (5 editions)**:
  - v22 monograph rewritten from scratch on the verified 37-test suite —
    Russian, English, Chinese (`monographs/{ru,en,zh}/`): markdown, interactive
    HTML, DOCX, vector PDF, 14-slide PPTX, arXiv-style preprint (tex+pdf),
    19 figures at 600 dpi per language;
  - Original author monograph v21 with verification (RU) and its full English
    edition (`monographs/original-v21/{ru,en}/`): docx + pdf + interactive html
    + md + 16-slide pptx presentations, shared figure media.
- **Canonical Julia suite** `code/ab_cloud_v19.jl`: 37 tests, two-pass protocol,
  report engine (md/html/pdf/docx/png 600dpi/svg/gif), interactive menu,
  Physics Lab (22 experiments), 3D laboratory (30 tests), `--quick` CI mode
  (16×16 → 32×32, ζ ≤ 5000).
- **10-language verification suite** `verification/`: C++, Fortran, Go, Haskell,
  JavaScript, Julia, MATLAB, Python, R, Rust; bilingual RU/EN interface;
  answers to 3 standard referee objections; ζ-zero datasets
  (13,661 / 50,000 / 500k / 2M zeros, Odlyzko).
- **3D lattice laboratory** `lab-3d/`: 3D non-Hermitian Hofstadter Hamiltonian
  with vortex lines, 36³ lattices, 5000 embedded zeros, full output reports.
- **Reference verification log** `results/verification_run_v18_37tests_2026-08-28.txt`.
- Documentation site (MkDocs Material, GitHub Pages), CI (markdownlint,
  link-checker, CodeQL, Julia quick-test), issue/PR templates, release
  automation (release-drafter, labeler, dependency-review, stale),
  Dependabot, funding config.

### Verified highlights
- ⟨r⟩ = 0.5848 ± 0.0260 vs GUE 0.5992 (deviation −2.4 %)
- Montgomery test: KS = 0.047, p = 0.27 (N = 500 certified zeros) — H₀ not rejected
- Byers–Yang flux defect 3.5·10⁻¹⁵; Connes self-duality (4 zero modes), C₁ = 2
- Montgomery correlation hole reproduced (d_GUE 0.140 < d_Pois 0.227)
- Dirac dynamics: E_min ∝ 1/L (R² = 0.9997), 20× DOS dip, skin effect

### License
- Custom Research License: all rights belong fully and exclusively to
  Isaev Iskhak Khamzatovich (see `LICENSE`).

[Unreleased]: https://github.com/wild8highlander/ab-cloud-research/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/wild8highlander/ab-cloud-research/releases/tag/v1.0.0
