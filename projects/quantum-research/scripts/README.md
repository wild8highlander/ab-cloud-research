<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ AB_Cloud_Quantum_Research/](../README.md) · [🏠 Root README](../../README.md)**

</div>
<!-- enriched 1.1.0 -->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/logo_abcloud_dark.png">
  <img src="../assets/logo_abcloud_light.png" width="92" alt="AB Cloud Quantum Research">
</picture>

### 🔧 Scripts — reproducibility pipelines

`AB Cloud Quantum Research` · v1.1.0 · part of one machine

![badge](https://img.shields.io/badge/program-AB_Cloud_Quantum_Research-C96F4A?style=flat-square)
![badge](https://img.shields.io/badge/verdicts-all%20PASS-3A6B4F?style=flat-square)
![badge](https://img.shields.io/badge/license-proprietary-6B6455?style=flat-square)

</div>

> 🧭 **Navigation:** [↑ main README](../README.md) · [📚 monographs](../MONOGRAPH_ARCHIVE/README.md) · [🧪 hypothesis lab](../HYPOTHESIS_LAB/README.md) · [🎞 animations](../VISUAL_ANIMATIONS/README.md)
# 🔧 scripts/ — the pipelines of the AB Cloud Quantum Research package

| Script | What it does |
|--------|-----------|
| `make_tiled_figures.py` | 12 tiled 2×2 figures ("4 dimensions") @600 dpi for Th1–Th6 from committed verdicts → `figures_tiled/{ru,en}/` + `theorems_lemmas/T0K_*/figures/` |
| `make_theorem_docs.py` | 12 theorem documents (RU/EN × PDF/DOCX) with the embedded tiled figure; the renderers and the content come from `modules/core_spectrum` without duplication |
| `make_theorem_readmes.py` | 6 detailed READMEs of the theorem folders (derivation, 4 dimensions, boundaries, EN summary) |
| `make_banner.py` | the animated banner `assets/banner.gif` (the critical line + the ζ zeros) and the logos `assets/logo*.svg/png` |
| `make_release.py` | SHA256SUMS.txt + the release ZIP in `/home/z/my-project/download/` |
| `validate_package.py` | the clean check (95+): structure, versions, verdicts, 36 documents, 20 figures, the web labs, the formal layer, the showcase |
| `make_datasets.py` | curated data: flagship_numbers, campaign_timeline (43 campaigns), the 660-zero ζ reference → `datasets/` |
| `make_atlas.py` | the flagship atlas — a 2×2 tile (blind zeros · compiler · trace·primes · CHSH) @600 dpi → `atlas/` |
| `make_timeline.py` | the timeline map of the 43 campaigns @600 dpi → `timeline/` |
| `make_whitepaper.py` | the research white paper (RU/EN PDF, the numbers from verdicts) → `whitepaper/` |

The scripts of the supplementary study are in
`research/realtime_spinor_memory/` (`make_figures.py`,
`make_theorem_docs.py`, `experiments/run_all.py`).

## Quick start

```bash
python3 scripts/make_tiled_figures.py     # the figures
python3 scripts/make_theorem_docs.py      # 24 doc files (12 documents)
python3 scripts/make_theorem_readmes.py   # the theorem READMEs
python3 scripts/make_banner.py            # the assets
python3 scripts/validate_package.py       # the self-check
python3 scripts/make_release.py           # the release
```

## Dependencies

Python ≥ 3.10: `matplotlib`, `numpy`, `Pillow`, `reportlab`, `python-docx`,
`openpyxl`, `pypdf` (see `../requirements.txt`). The theorem renderers use
the system FreeSerif fonts. The Julia program is run by its own stack:
`julia modules/verifier_multilang/experiments/run_all.jl all`.

---

<div align="center">

<img src="../assets/avatars/avatar_author.svg" width="84" alt="author">

*Part of the discipline: pre-registration · blind protocols · replication ·
negative results published*

**AB Cloud Quantum Research** · v1.1.0 ·
[license](../../../LICENSE) · © Isaev Iskhak Khamzatovich

</div>

---

<!-- enriched-r3 -->

This folder holds the **pipeline scripts** of its module: the deterministic code paths that turn frozen inputs into reports, figures and verdicts. The scripts follow the repository's seed discipline — same input, same seed, same bytes out — so a re-run on the pinned platform reproduces the committed artifacts. Nothing here is executed at import time by other modules; they are entry points, documented in the module README.

The pipelines of the AB Cloud Quantum Research package: deterministic entry points that rebuild figures, documents and checks from the frozen data.

## Folder contents

| File | Size | What it is |
|---|---|---|
| `make_atlas.py` | 7.9 KB | Python source |
| `make_avatars.py` | 2.2 KB | Python source |
| `make_banner.py` | 7.5 KB | Python source |
| `make_datasets.py` | 8.5 KB | Python source |
| `make_release.py` | 1.8 KB | Python source |
| `make_theorem_docs.py` | 5.2 KB | Python source |
| `make_theorem_readmes.py` | 22 KB | Python source |
| `make_tiled_figures.py` | 22 KB | Python source |
| `make_timeline.py` | 4.8 KB | Python source |
| `make_whitepaper.py` | 21 KB | Python source |
| `validate_package.py` | 8.3 KB | Python source |

<div align="center">

<img src="../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
</div>
