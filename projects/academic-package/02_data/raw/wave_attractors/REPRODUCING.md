# REPRODUCING — how to rebuild study W1 from this repository alone

This study is designed to be reproducible **without any external knowledge or
data**: every number, figure and document in `wave_attractors/` can be
regenerated from the sources committed here. The original popular-science
article that motivated the study is **not needed** — the README and the
monographs state the physics, the models, all parameters and all published
observables, and the code encodes every constant (seeds, chamber geometry,
protocols) explicitly.

## Tiers

| Tier | Contents | Requires | How |
|------|----------|----------|-----|
| 1. Research data | E1–E7, AB companion, reference dumps (`data/`) | Python ≥ 3.12 + `requirements.txt` (numpy, scipy, matplotlib) | `make wave-attractors` |
| 2. Julia cross-verification | `rays_julia.csv`, `julia_td_*`, `cross_verification.json`, `td_cross_verification.json` | Julia ≥ 1.10 (stdlib only) | `make wave-attractors-julia JULIA=julia` |
| 3. Figures | `figures/*.png` (12, 300 dpi) | tier 1 (+ tier 2 for fig 09) | `make wave-attractors` |
| 4. Documents | report PDF, RU/EN monograph DOCX | tier 1–3 + `reportlab`, `pypdf`, Node + `docx@9.7.1`, LibreOffice (PDF), `python-docx` | `make wave-attractors-docs` |

## Verification protocol

After a fresh run, compare the regenerated `data/` against the committed
reference with the built-in verifier:

```bash
make wave-attractors CAND=...            # or run steps manually
make wave-attractors-verify CAND=/path/to/fresh/wave_attractors/data
```

`verify_repro.py` compares every file on three levels and prints a per-file
verdict:

* `IDENTICAL` — bitwise (sha256) equal;
* `MATCH` — numerically equal within `atol=1e-9, rtol=1e-6` (JSON/CSV/NPZ);
* `MISMATCH` / `MISSING` — reproduction failed.

Volatile wall-clock metadata (`runtime_s`, `solve_s`, …) is excluded from the
scientific comparison and reported as pruned. The verifier writes a
machine-readable certificate to `data/REPRODUCIBILITY.json`.

## Blind cold-start audit (2026-10-01)

Protocol: the working tree was copied to a clean directory and **every
derived artifact was deleted** (all of `data/`, all 12 figures, the report
PDF, both monographs and their per-language figure sets) — 113 MB reduced to
560 KB of pure sources. The full pipeline was then re-run from the Makefile
only, on the same machine (Python 3.12, numpy 2.1.3, scipy 1.14.1,
matplotlib 3.9.2, Julia 1.10.4, docx 9.7.1), and compared against the
committed reference.

| Tier | Result |
|------|--------|
| Data (`data/`) | **31/31 files reproduce** — 22 bitwise identical, 9 JSON files exact (max delta = 0) after pruning volatile timing fields |
| Figures | **12/12 PNG bitwise identical** (sha256) |
| Julia cross-verification | short-horizon identity + TD kernel: `all_ok = true`, max rel. dev 2.4e-15 |
| Report PDF | 14 pages, extracted text **identical** (bytes differ only by the embedded PDF creation timestamp) |
| Monograph DOCX (RU + EN) | `word/document.xml` **bitwise identical** for both languages |
| Overall | **REPRODUCIBLE** — certificate: `data/REPRODUCIBILITY.json` |

The audit surfaced and fixed three latent reproducibility defects:

1. fig 09 hard-depended on the optional Julia tier → now skipped with a
   warning when `cross_verification.json` is absent;
2. `make_figures.py --out` was CWD-dependent → the Makefile now passes
   explicit `../figures` paths;
3. the document chain omitted two post-steps (footer patch + TOC
   placeholders) and the `docx` npm version was unpinned → the chain is now
   `build → postprocess → add_toc_placeholders` with `docx` pinned to 9.7.1
   in `scripts/monograph/package.json`.

## Determinism notes

* Every stochastic entry point uses a fixed seed (`np.random.default_rng(seed)`;
  chamber seed 7), so ray experiments are fully deterministic — the raw CSV
  and NPZ outputs are byte-for-byte reproducible on the same
  numpy/scipy/matplotlib versions.
* The Julia port is stdlib-only and reproduces the Python trajectories to
  3.45e-15 (short horizon; long horizons diverge chaotically by design, which
  is why verification is short-horizon + statistical).
* Documents embed build metadata (PDF creation time, DOCX zip timestamps);
  their *content* streams are what the verifier-level checks treat as the
  reproducibility contract.
* Software versions used for the reference artifacts are pinned in
  `requirements.txt` (Python) and `scripts/monograph/package.json` (Node).
