<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-hilbert-polya-FFB74D?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 🧱 monograph/content — source modules

> **The book as code: Python content modules from which every monograph volume is generated.**

This is the *source* layer of the monograph machine: Python content modules (`ru_part*.py`, `en_part*.py`, `canon_*.py`, `parts_theorems_v2.py`) that carry the book's text as structured data, so the DOCX/PDF volumes next door are **generated**, not hand-assembled. Editing the text means editing a module here and re-running the build — the compiled volumes in the sibling folders are never edited directly.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`canon_en.py`](canon_en.py) | Python | 28.6 KB | EN canonical volume content module |
| [`canon_ru.py`](canon_ru.py) | Python | 41.3 KB | RU canonical volume content module |
| [`en_part1.py`](en_part1.py) | Python | 24.3 KB | — |
| [`en_part2.py`](en_part2.py) | Python | 17.3 KB | — |
| [`en_part3.py`](en_part3.py) | Python | 11.8 KB | — |
| [`en_part4.py`](en_part4.py) | Python | 17.9 KB | — |
| [`parts_theorems_v2.py`](parts_theorems_v2.py) | Python | 7.2 KB | theorems-v2 volume content (T1–T18 statements and commentary) |
| [`ru_part1.py`](ru_part1.py) | Python | 37.4 KB | — |
| [`ru_part2.py`](ru_part2.py) | Python | 25.6 KB | — |
| [`ru_part3.py`](ru_part3.py) | Python | 16.9 KB | — |
| [`ru_part4.py`](ru_part4.py) | Python | 26.7 KB | — |

## 🧭 Navigation

[⬅ monograph/](../README.md) · [🏠 Repo root](../../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>

---

<!-- enriched-r3 -->

This folder holds the **pipeline scripts** of its module: the deterministic code paths that turn frozen inputs into reports, figures and verdicts. The scripts follow the repository's seed discipline — same input, same seed, same bytes out — so a re-run on the pinned platform reproduces the committed artifacts. Nothing here is executed at import time by other modules; they are entry points, documented in the module README.

The single source of content: the Python source modules from which every volume, in both languages and both formats, is rendered. This is the anti-drift mechanism of the monograph layer.
