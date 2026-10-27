<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ff2ec4,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ lab-3d/](../README.md) · [🏠 Root README](../../README.md)**

</div>
# lab-3d/outputs — Committed Verification Runs (2026-07-31)

> **🧭 Navigation:** [lab-3d/](../README.md) · [Root README](../../README.md)

Four complete, timestamped output folders produced by the 3D laboratory on
2026-07-31 and committed verbatim so the figures and numbers can be inspected
without re-running the simulations. Every folder follows the same report
convention: `<mode>.json` (machine dump) + `<mode>.md` / `.txt` / `.html`
(human reports) + `<mode>_summary.csv` (flat table) + all figures in both
PDF (vector) and PNG (600 dpi).

## Run inventory

| Folder | Mode | What it contains |
|---|---|---|
| `full_verification_2026-07-31_15-33-39/` | G — full verification | reviewer-point checks: ⟨r⟩ = 0.6159 vs GUE 0.5996, KS tests, FSS to N = 5000, Arf invariant 0 across N ∈ {16…4096}, Dirac cone β = 1.0, decay slope −0.967; figures 01–11 |
| `deep_zeros_2026-07-31_15-36-34/` | H — deep ζ analysis | 5000 embedded zeros: all on Re s = 1/2, NN spacing PDF, R₂(x), K(τ), S(T) statistics, decay times τₙ = ħ/γₙ |
| `3d_bridge_2026-07-31_15-36-37/` | I — AB↔Riemann bridge | 9 visualizations: spectral staircase, (α,σ) phase diagram, Dirac-cone family, form-factor surfaces, wavefunction density, decay-time manifold, pair-correlation landscape |
| `3d_advanced_2026-07-31_15-51-47/` | J — advanced 3D | Chern marker surface+heatmap, probability current, winding number W = 1 (11 points), Hofstadter butterfly, 121 exceptional-point candidates, edge-state localization |

## Headline numbers (recap)

| Metric | Value |
|---|---|
| ⟨r⟩ (ζ zeros / AB-Cloud) | 0.6159 / same within error (GUE 0.5996) |
| KS p (AB-Cloud vs ζ) | 0.27–0.88 — indistinguishable |
| Permutation test | Z = 14.10σ, p < 10⁻⁴⁴ |
| Arf invariant | 0 at every resolution |
| Winding number at RH | 1 (11 checkpoints) |

## How to regenerate

The folders are reproducible from `../code/` with fixed seeds (folder names
will carry the new timestamp):

```bash
cd ../code
python3 ab_cloud_3d_en.py    # choose mode G / H / I / J in the menu
```

## Reading the reports

Start with `<mode>.md` — it has the verdict table with raw numbers; the
`.json` holds the same data machine-readably; `<mode>_summary.csv` is
convenient for spreadsheets. Figure files are numbered to match the section
order of the `.md` report.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `3d_advanced_2026-07-31_15-51-47/` | directory, 21 files inside | folder |
| `3d_bridge_2026-07-31_15-36-37/` | directory, 29 files inside | folder |
| `deep_zeros_2026-07-31_15-36-34/` | directory, 15 files inside | folder |
| `full_verification_2026-07-31_15-33-39/` | directory, 27 files inside | folder |
| `README.md` | 2.9 KB | markdown guide |
| **Total (files)** | **2.9 KB** | 1 files + 4 subdirectories |

## 🔬 Deep dive — committed outputs with their producers

Nothing in this folder is "free art": each output names the script and the
parameter block that produced it, and the lab's README tables map every
file to its producer. The committed set includes the 36³ reference scene
renders, surface exports used by the preprint figures, and diagnostic
probes (hermiticity checks, flux bookkeeping) that let a reviewer verify
the *instrument* as well as the picture.

If you regenerate an output and it differs, the lab treats that as a
reportable event — check first for floating-point stack differences (BLAS
orderings), then for actual drift. The committed files are the archival
truth; local re-renders are for confidence, not for replacing evidence.

---

<!-- enriched-r3 -->

This folder is a **committed run artifact**: the outputs of one execution of the module's pipeline, frozen at the moment of generation. The run directories are named by their UTC timestamp and are never edited after the fact — the reports, figures and data tables inside are the evidence that the pipeline ran and what it produced. Regenerating them is always possible from the scripts; the committed copies exist so that no reader ever has to.

The committed verification runs of 2026-07-31: four timestamped run folders, each with its own PDF report, figure set and run manifest. The folders are never edited after the fact; regenerate from `code/` if needed.

## Folder contents

**Subfolders:** `3d_advanced_2026-07-31_15-51-47/` · `3d_bridge_2026-07-31_15-36-37/` · `deep_zeros_2026-07-31_15-36-34/` · `full_verification_2026-07-31_15-33-39/`


**Where next:** [outputs hub](../README.md)

<div align="center">

<img src="../../assets/svg/divider-magenta.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
