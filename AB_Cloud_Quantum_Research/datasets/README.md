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

### 📊 Datasets — verdict-derived data

`AB Cloud Quantum Research` · v1.1.0 · part of one machine

![badge](https://img.shields.io/badge/program-AB_Cloud_Quantum_Research-C96F4A?style=flat-square)
![badge](https://img.shields.io/badge/verdicts-all%20PASS-3A6B4F?style=flat-square)
![badge](https://img.shields.io/badge/license-proprietary-6B6455?style=flat-square)

</div>

> 🧭 **Navigation:** [↑ main README](../README.md) · [📚 monographs](../MONOGRAPH_ARCHIVE/README.md) · [🧪 hypothesis lab](../HYPOTHESIS_LAB/README.md) · [🎞 animations](../VISUAL_ANIMATIONS/README.md)
# 📊 datasets/ — curated datasets

Every value in these files is taken **from a committed campaign verdict**
(no hand-typed numbers). The files are rebuilt by the script
`scripts/make_datasets.py`.

| File | Contents | Provenance |
|------|------------|---------------|
| `flagship_numbers.csv` | 15 flagship metrics of the program: metric · value · source verdict · module | v20_verdict, v07_verdict, e16/e17/e18_verdict, es1–es5_verdict |
| `campaign_timeline.csv` | 43 campaigns of the four levels: id · module · title · status · key result | verdicts v01–v19, v20, e01–e18, es1–es5 |
| `zeta_zeros_reference.csv` | reference ordinates of the ζ zeros, 0 < γ ≤ 1000 (660 rows) — the very blind E17 reference | `modules/verifier_multilang/results/e17_zetazero_reference.csv` (SHA256 pin) |


```mermaid
graph LR
    V["verdicts<br/>*_verdict.json"] --> D["datasets/<br/>3 curated CSV"]
    D --> F["figures · atlas · timeline"]
    D --> M["MONOGRAPH_ARCHIVE<br/>appendices A–B"]
```

## Example usage

```bash
# flagships in one line
python3 -c "import csv; [print(r['metric'], '=', r['value']) for r in csv.DictReader(open('datasets/flagship_numbers.csv'))]"

# rebuild from verdicts
python3 scripts/make_datasets.py
```

## Related artifacts

- the campaign timeline map: [`../timeline/`](../timeline/README.md);
- the flagship atlas (2×2 tile, 600 dpi): [`../atlas/`](../atlas/README.md).

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

The curated CSV datasets of the program — the quantitative layer that the web lab and the documentation quote. Schemas and provenance for these files are described in the program documentation.

## Folder contents

| File | Size | What it is |
|---|---|---|
| `campaign_timeline.csv` | 6.0 KB | CSV dataset |
| `flagship_numbers.csv` | 1.5 KB | CSV dataset |
| `zeta_zeros_reference.csv` | 23 KB | CSV dataset |

<div align="center">

<img src="../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
</div>
