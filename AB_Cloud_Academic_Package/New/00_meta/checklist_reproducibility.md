# Reproducibility checklist

- [x] **Single global seed** (42) declared in `config.yaml`; runners inherit it.
- [x] **Arbitrary precision paths** pinned (dps 40 default; 256-bit for rational identities).
- [x] **Cross-language verification**: the three sources cross-verify Python ↔ Julia
  (dirac-lab: 4 independent Julia ports; E-series: Julia platform with Python
  cross-checks); the unified CLI keeps the contract identical in 6 languages.
- [x] **Pre-registered verdict windows** (`config.yaml: gue_windows`) — the
  statistics cannot be re-tuned to fit results.
- [x] **Data checksums**: `02_data/checksums.sha256`; verify with
  `python3 06_code/scripts/update_checksums.py --verify-only`.
- [x] **Provenance ledger**: `00_meta/provenance.jsonl` — one row per
  consolidation decision.
- [x] **Deterministic outputs**: figure generation is seed-pinned; report
  assembly reads the registry (no live computation of headline numbers).
- [x] **Environment description**: `06_code/requirements.txt`, `pyproject.toml`,
  `Dockerfile`, `environment.yml` for conda users.
- [ ] **Nightly automated re-run** (open item — see `ROADMAP.md`).
- [x] **Negative-result reproducibility**: the failures (null zones, locality
  wall) are as reproducible as the successes and documented in the registry.
