<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-verification-2EA043?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# ☕ verification/java — the Java port (spinor38)

> **The Java member of the ten-language suite: the spinor-38 experiment, JVM-stock only.**

The Java twin lives in [`spinor38/`](spinor38/): a stock-JVM implementation (no build systems, no external jars) of the spinor-38 experiment used by the suite's spinor section. Like every port in this folder it re-derives the same reference values from the same frozen datasets and must end with identical numbers — that is the cross-language contract documented in the [suite README](../README.md).

Compile and run with plain `javac`/`java`; the exact commands and the expected control block are listed in the [port README](spinor38/README.md).

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| `spinor38/` · [README](spinor38/README.md) | folder | 3 items | see inside |
| [`spinor38/Spinor38.java`](spinor38/Spinor38.java) | Java source | 7.0 KB | the Test-38 port — hand-written cyclic-Jacobi eigensolver over the frozen spinor classes |
| [`spinor38/run.sh`](spinor38/run.sh) | shell script | 199 B | compile-and-run wrapper (`javac` + `java`) |

## 🧭 Navigation

[⬅ verification/](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../LICENSE).*

</div>
