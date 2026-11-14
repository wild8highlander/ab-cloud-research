<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:00e5ff,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ verification/](../README.md) · [🏠 Root README](../../README.md)**

</div>
<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-verification-2EA043?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# ☕ verification/java — the Java port

> **The Java member of the ten-language suite: the main three-objection verifier plus the spinor-38 experiment, JVM-stock only.**

## Main verifier — `ABCloudVerify.java` (CANON_SPEC v3.0)

A faithful port of the validated Python reference (`../python/ab_cloud_verify.py`):
Lambert W (Newton), Gram points (seed + exactly 8 Newton iterations), the b(N)
prefix kernel, normalized spacings, the GUE (β=2) CDF through the 32768-point
table (own erf/erfc — series + Lentz continued fraction, std-lib has none),
KS/Cramér–von Mises/Anderson–Darling/⟨r⟩, the three reviewer objections with
number-driven verdicts, the full §9 source registry — **including `2M_gz`,
decompressed natively via `java.util.zip.GZIPInputStream`** — and the 28 frozen
golden anchors. Bilingual (EN/RU): every conclusion is printed only in the
branch chosen by the computed numbers.

Run (JDK 8+):

    ./run_verify.sh --zeros 50000 --source 500k
    # or manually:
    javac -encoding UTF-8 ABCloudVerify.java ABCloudVerifyEn.java ABCloudVerifyRu.java
    java -Dfile.encoding=UTF-8 ABCloudVerify --zeros 50000 --source 500k

On JDK 11+ the single-file source launcher works without `javac`:

    java ABCloudVerify.java --zeros 50000 --source 500k

The run must print `Self-check: 28 passed, 0 failed`; exit code 1 means an
anchor failed, 2 means a load/CLI error. `ABCloudVerifyEn` / `ABCloudVerifyRu`
are thin language pins (spec §10): they append `--lang en|ru` and delegate to
`ABCloudVerify.runMain` — zero duplicated math.

Validated run (frozen first 50 000 zeros, source `500k`): b(50000) =
1.2125526773, KS D = 0.021619, W² = 8.177703, A² = 61.492426, ⟨r⟩ = 0.611880,
decay slope −0.1685 (R² = 0.9888) — bit-close to the canon.

## Spinor-38 — [`spinor38/`](spinor38/)

A stock-JVM implementation (no build systems, no external jars) of the spinor-38 experiment used by the suite's spinor section. Like every port in this folder it re-derives the same reference values from the same frozen datasets and must end with identical numbers — that is the cross-language contract documented in the [suite README](../README.md).

Compile and run with plain `javac`/`java`; the exact commands and the expected control block are listed in the [port README](spinor38/README.md).

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`ABCloudVerify.java`](ABCloudVerify.java) | Java source | ~33 KB | the main CANON_SPEC v3.0 verifier — 28 golden anchors, three objections, bilingual output |
| [`ABCloudVerifyEn.java`](ABCloudVerifyEn.java) | Java source | <1 KB | thin language pin: English |
| [`ABCloudVerifyRu.java`](ABCloudVerifyRu.java) | Java source | <1 KB | thin language pin: Russian |
| [`run_verify.sh`](run_verify.sh) | shell script | ~0.4 KB | compile-and-run wrapper (`javac -encoding UTF-8` + `java -Dfile.encoding=UTF-8`) |
| `spinor38/` · [README](spinor38/README.md) | folder | 3 items | see inside |
| [`spinor38/Spinor38.java`](spinor38/Spinor38.java) | Java source | 7.0 KB | the Test-38 port — hand-written cyclic-Jacobi eigensolver over the frozen spinor classes |
| [`spinor38/run.sh`](spinor38/run.sh) | shell script | 199 B | compile-and-run wrapper (`javac` + `java`) |

## 🧭 Navigation

[⬅ verification/](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../LICENSE).*

</div>

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The Java port shelf: the folder hosts the main CANON_SPEC v3.0 verifier (`ABCloudVerify.java` + thin `En`/`Ru` pins + `run_verify.sh`) and the spinor38 Java port (see the `spinor38/` subfolder).

<div align="center">

<img src="../../assets/svg/divider-cyan.svg" alt="—" width="100%" height="12"/>
</div>
