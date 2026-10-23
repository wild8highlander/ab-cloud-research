<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ Vortex_optimization/](../README.md) · [🏠 Root README](../../README.md)**

</div>
<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-labs-7FC8A8?style=flat-square)](../README.md)

</div>

# 📈 Vortex_optimization — curves (frozen NPZ)

> **The frozen curve archives of the T-34 vortex study: one .npz per configuration.**

Each `R2_L*_Nv*_q*_W*_a*_<protocol>.npz` file is one optimization curve of the T-34 study — lattice size, vortex count, flux q, W and α, plus the protocol tag (`open`, `torus`, `open_regular`) — exactly as recorded during the sweeps that produced [`../data/`](../data/) and [`../figures/`](../figures/). The archives are the deepest layer of the evidence chain: CSVs and figures summarize them, they summarize nothing.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`R2_L96_Nv16_q0.70_W1.00_a0.50_open_protocol.npz`](R2_L96_Nv16_q0.70_W1.00_a0.50_open_protocol.npz) | NumPy | 3.4 KB | — |
| [`R2_L96_Nv16_q1.00_W1.00_a0.50_torus_protocol.npz`](R2_L96_Nv16_q1.00_W1.00_a0.50_torus_protocol.npz) | NumPy | 3.4 KB | — |
| [`R2_L96_Nv2_q1.00_W1.00_a0.50_open_protocol.npz`](R2_L96_Nv2_q1.00_W1.00_a0.50_open_protocol.npz) | NumPy | 3.4 KB | — |
| [`R2_L96_Nv8_q1.00_W1.00_a0.60_open_regular.npz`](R2_L96_Nv8_q1.00_W1.00_a0.60_open_regular.npz) | NumPy | 3.4 KB | — |

## 🧭 Navigation

[⬅ Vortex_optimization/](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../LICENSE).*

</div>

---

<!-- enriched-r3 -->

This folder holds **frozen, committed data**: the byte-identical inputs that the verification pipeline reads. The discipline of the repository is that nothing downstream depends on a recomputation — every figure, test and document replays these committed files, so editing or regenerating them in place is forbidden by convention. Where a file also exists in another module's canon, the copies are byte-identical by design.

The frozen scan curves (NumPy archives): the measured D-statistic landscapes over the vortex-dial windows, as committed by the large-scale scan.

<div align="center">

<img src="../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
</div>
