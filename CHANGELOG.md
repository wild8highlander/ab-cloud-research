# Changelog

All notable changes to the **AB-Cloud Research** repository are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
