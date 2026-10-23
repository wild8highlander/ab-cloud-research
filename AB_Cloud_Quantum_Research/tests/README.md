<!-- enriched 1.1.0 -->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/logo_abcloud_dark.png">
  <img src="../assets/logo_abcloud_light.png" width="92" alt="AB Cloud Quantum Research">
</picture>

### 🧪 Tests — smoke integrity

`AB Cloud Quantum Research` · v1.1.0 · part of one machine

![badge](https://img.shields.io/badge/program-AB_Cloud_Quantum_Research-C96F4A?style=flat-square)
![badge](https://img.shields.io/badge/verdicts-all%20PASS-3A6B4F?style=flat-square)
![badge](https://img.shields.io/badge/license-proprietary-6B6455?style=flat-square)

</div>

> 🧭 **Navigation:** [↑ main README](../README.md) · [📚 monographs](../MONOGRAPH_ARCHIVE/README.md) · [🧪 hypothesis lab](../HYPOTHESIS_LAB/README.md) · [🎞 animations](../VISUAL_ANIMATIONS/README.md)
# 🧪 tests/ — the integrity tests of the AB Cloud Quantum Research package

`test_unified.py` — the smoke tests of the package (run: `python3 tests/test_unified.py`
or `make test`). They check:

1. the structure (11 mandatory folders);
2. **12 theorem documents** (6 × RU/EN × PDF/DOCX) in `theorems_lemmas/`;
3. **12 tiled figures** in `figures_tiled/{ru,en}/`;
4. the verdicts of the Julia series: `verdicts_master.json` — **all 18 PASS**;
5. the core_rp obligation machine: the RH verdict — `certified` (0 assumptions);
6. the formal files: `sorry`/`Admitted` absent from RPTheorems;
7. the "Theorems" tab in both web labs + the portal of the three programs;
8. the full `scripts/validate_package.py` (40+ checks) finishing successfully.

Each component program carries its OWN tests: core_rp — 42 pytest tests
(`modules/core_spectrum/tests/`), QP — 19 (`test_v20_processor.py`),
Julia — its own self-tests inside the experiments + independent verification
(`independent_verification/RUN_ALL.sh` in core_rp and QP).

---

<div align="center">

<img src="../assets/avatars/avatar_author.svg" width="84" alt="author">

*Part of the discipline: pre-registration · blind protocols · replication ·
negative results published*

**AB Cloud Quantum Research** · v1.1.0 ·
[license](../../LICENSE) · © Isaev Iskhak Khamzatovich

</div>

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The integrity tests of the package: they check that the frozen data, the committed verdicts and the documents agree with each other — the plumbing that keeps the program honest.

## Folder contents

| File | Size | What it is |
|---|---|---|
| `test_unified.py` | 4.7 KB | Python source |
