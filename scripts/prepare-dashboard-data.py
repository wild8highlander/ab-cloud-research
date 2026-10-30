#!/usr/bin/env python3
"""
prepare-dashboard-data.py — freeze repository artifacts into JSON the web
dashboard can fetch.

Sources (all already committed in the repository — no numerics re-run):
  results/RH_Sweep_Pro_Enrichment/data/assets.npz   → curve arrays
  results/RH_Sweep_Pro_Enrichment/data/metrics.csv  → per-config metric rows
  results/RH_Sweep_Pro_Enrichment/SUMMARY.json      → headline of the run
  results/RH_Sweep_Pro_Enrichment/data/gue_control.json → GUE error floor
  verification/data/abcloud_golden.json             → frozen golden values

Outputs (committed, so end users never need Python):
  apps/ab-cloud-dashboard/public/data/enrichment_curves.json
  apps/ab-cloud-dashboard/public/data/metrics_sweep.json
  apps/ab-cloud-dashboard/public/data/enrichment_summary.json
  apps/ab-cloud-dashboard/public/data/gue_control.json
  apps/ab-cloud-dashboard/public/data/golden_values.json

Requires: python3 + numpy (only for reading the .npz). Run once after the
Julia suite produces new artifacts; the generated JSON is what ships.
"""
import csv
import json
import math
import shutil
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "results" / "RH_Sweep_Pro_Enrichment"
DST = ROOT / "apps" / "ab-cloud-dashboard" / "public" / "data"


def clean(x):
    """NaN/Inf → None, round floats to 8 significant decimals."""
    if isinstance(x, (float, np.floating)):
        if math.isnan(x) or math.isinf(x):
            return None
        return round(float(x), 8)
    if isinstance(x, (int, np.integer)):
        return int(x)
    return x


def arr(name):
    return [clean(v) for v in npz[name].ravel()]


npz = np.load(SRC / "data" / "assets.npz", allow_pickle=True)

curves = {
    "_meta": {
        "source": "results/RH_Sweep_Pro_Enrichment/data/assets.npz",
        "run": "RH_Auto_5000_L64_s5",
        "generated": "2026-10-17",
        "what": "post-run enrichment curves: AB-cloud vs ζ zeros vs GUE vs Poisson",
        "note": "AB = file-union of 5 seeds (globally sorted); per-seed run metrics in results.json",
    },
    "R2": {
        "s": arr("s_grid"), "ab": arr("R2_ab"), "zz": arr("R2_zz"),
        "gue": arr("R2_gt"), "poi": arr("R2_pt"),
        "x": "s", "title": "R2(s) — two-level cluster function",
    },
    "K": {
        "t": arr("t_grid"), "ab": arr("K_ab"), "zz": arr("K_zz"),
        "gue": arr("K_gt"), "poi": arr("K_pt"),
        "x": "t", "title": "K(t) — spectral form factor",
    },
    "S2": {
        "L": arr("L_grid"), "ab": arr("S2_ab"), "zz": arr("S2_zz"),
        "gue": arr("S2_gt"), "poi": arr("S2_pt"),
        "x": "L", "title": "Σ²(L) — number variance",
    },
    "D3": {
        "L": arr("L_grid"), "ab": arr("D3_ab"), "zz": arr("D3_zz"),
        "x": "L", "title": "Δ₃(L) — spectral rigidity",
    },
    "ps": {
        "s": arr("c_s"), "ab": arr("p_ab"), "gue": arr("p_gue"),
        "poi": arr("p_poi"), "E": arr("E_ab"),
        "x": "s", "title": "p(s) — nearest-neighbour spacing + survival E(s)",
    },
    "ratio": {
        "r": arr("rb"), "hist": arr("h_ab"),
        "title": "histogram of r = min/max (file-union of 5 seeds)",
    },
    "superposition": {
        "m": arr("sup_m"), "r": arr("sup_r"), "rtilde": arr("sup_rt"),
        "title": "superposition of m independent GUE spectra",
    },
}

# metrics.csv: comment lines start with '#', then a single header row
rows = []
with open(SRC / "data" / "metrics.csv", newline="", encoding="utf-8") as fh:
    lines = [l for l in fh if not l.lstrip().startswith("#")]
reader = csv.DictReader(lines)
INT_COLS = {"L", "n_eigs", "tests_passed", "tests_total"}
for row in reader:
    out = {}
    for k, v in row.items():
        if k is None or v is None:
            continue
        v = v.strip().strip('"')
        key = k.strip()
        if key in INT_COLS:
            out[key] = int(v)
        elif key in ("label", "r_class"):
            out[key] = v
        elif key == "R2_match_GUE":
            out[key] = v == "TRUE"
        else:
            try:
                out[key] = float(v) if v not in ("", "-") else None
            except ValueError:
                out[key] = v
    rows.append(out)

metrics = {
    "_meta": {
        "source": "results/RH_Sweep_Pro_Enrichment/data/metrics.csv",
        "run": "RH_Auto_5000_L64_s5",
        "generated": "2026-10-16",
        "what": "RH_Unified sweep — per-config metrics of the AB-cloud operator",
        "n_configs": len(rows),
    },
    "rows": rows,
}

DST.mkdir(parents=True, exist_ok=True)

out_curves = DST / "enrichment_curves.json"
out_curves.write_text(json.dumps(curves, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
out_metrics = DST / "metrics_sweep.json"
out_metrics.write_text(json.dumps(metrics, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

shutil.copyfile(SRC / "SUMMARY.json", DST / "enrichment_summary.json")
shutil.copyfile(SRC / "data" / "gue_control.json", DST / "gue_control.json")
shutil.copyfile(ROOT / "verification" / "data" / "abcloud_golden.json", DST / "golden_values.json")

golden = json.loads((DST / "golden_values.json").read_text(encoding="utf-8"))
n_golden = sum(len(v) if isinstance(v, dict) else 1 for v in golden.values())

for p in (out_curves, out_metrics, DST / "enrichment_summary.json",
          DST / "gue_control.json", DST / "golden_values.json"):
    print(f"{p.name:28s} {p.stat().st_size / 1024:8.1f} KB")
print(f"golden values: {n_golden} entries in {len(golden)} groups")
print(f"metric rows:   {len(rows)} configs × {len(rows[0])} columns")
print("OK")
