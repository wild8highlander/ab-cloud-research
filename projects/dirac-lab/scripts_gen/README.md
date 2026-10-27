<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:00e5ff,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ dirac-lab/](../README.md) · [🏠 Root README](../../README.md)**

</div>
<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-labs-7FC8A8?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# ⚙️ dirac-lab — generation scripts

> **The document machine of dirac-lab: bilingual content JSON, the DOCX builder and the benchmark.**

Everything that assembles dirac-lab's documents lives here: [`monograph_en.json`](monograph_en.json) and [`monograph_ru.json`](monograph_ru.json) are the full bilingual content blocks of the monograph, [`make_docx.js`](make_docx.js) turns a JSON block into the DOCX editions, and [`benchmark.py`](benchmark.py) runs the lab's performance benchmark. This folder is the top of dirac-lab's document dependency chain: JSON → tex → pdf/docx.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`benchmark.py`](benchmark.py) | Python | 6.0 KB | — |
| [`make_docx.js`](make_docx.js) | JavaScript | 12.5 KB | — |
| [`monograph_en.json`](monograph_en.json) | JSON | 72.5 KB | — |
| [`monograph_ru.json`](monograph_ru.json) | JSON | 119.0 KB | — |

## 🧭 Navigation

[⬅ dirac-lab/](../README.md) · [→ tex intermediates](../monographs/tex/) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>

---

<!-- enriched-r3 -->

This folder holds the **pipeline scripts** of its module: the deterministic code paths that turn frozen inputs into reports, figures and verdicts. The scripts follow the repository's seed discipline — same input, same seed, same bytes out — so a re-run on the pinned platform reproduces the committed artifacts. Nothing here is executed at import time by other modules; they are entry points, documented in the module README.

The generation scripts of the laboratory: the drivers that produce the test folders, figures and ledgers from the shared core.

<div align="center">

<img src="../../assets/svg/divider-cyan.svg" alt="—" width="100%" height="12"/>
</div>
