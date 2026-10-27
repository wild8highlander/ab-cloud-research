"""tests/test_v2_campaigns.py — воспроизведение закоммиченных вердиктов v2.

Каждый тест перечитывает вердикт из computations/*/data/ и проверяет
ключевые пороги (то же правило, что в v1-тестах: вердикты коммитятся).
"""
import json
import os
import sys

import numpy as np
import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)


def _load(rel):
    with open(os.path.join(REPO, rel)) as f:
        return json.load(f)


def test_c9_nonlocal_primitive():
    d = _load("computations/C9_nonlocal_trace/data/results.json")
    r = d["results"]
    assert r["N1_Hxi"]["r_H7_matched"] > 0.999
    assert r["N2_DCT_twin"]["r_EF"]["r_fluct"] > 0.99
    assert r["N4_BerryKeating"]["r_H7"] < 0.2          # нулевая зона
    assert r["N1_Hxi"]["trace_check"]["max_abs_diff_K"] < 1e-4


def test_c10_hard_colocation():
    d = _load("computations/C10_phase_coded/data/results.json")
    worst = max(v["pairwise_max_resid"]
                for v in d["colocation_T12"].values())
    assert worst < 1e-12                                # T12 по построению
    assert max(abs(g["r_H7"]) for g in d["gates"]) < 0.15


def test_c11_counting_law():
    d = _load("computations/C11_alpha_third/data/results.json")
    assert d["law"]["holds_all_L"]
    assert d["law"]["index_holds"]
    assert d["law"]["decisive_L36_L48"] == {"36": 66, "48": 90}
    # T9-наблюдение v1 воспроизведено
    rows = {r["L"]: r["n_zero_torus"] for r in d["scan"]}
    assert rows[12] == 18 and rows[24] == 42


def test_c12_band5000():
    d = _load("computations/C12_band_5000/data/results.json")
    assert d["N_online_5000"] == 4520
    assert d["S_max"] <= 2.0
    assert all(s["match"] for s in d["strip_checks"])
    assert all(v["match"] for v in d["anchors"].values()
               if v.get("expected") is not None)


def test_c13_blind_null_zone():
    d = _load("computations/C13_blind_families/data/results.json")
    assert d["meta"]["pipeline_PC0p_r"] > 0.999
    assert max(abs(g["r_H7"]) for g in d["gates"]) < 0.15
    assert len(d["gates"]) == 20


def test_c14_no_rank_outliers():
    d = _load("computations/C14_anomaly_hunt/data/results.json")
    assert d["n_rH7_outliers_0p35"] == 0
    assert d["meta"]["n_configs"] >= 100
    classes = {r.get("class") for r in d["gates"]}
    assert {"gue", "integrable", "intermediate"} <= classes


def test_c15_dirichlet_pipeline():
    d = _load("computations/C15_dirichlet/data/results.json")
    for q in ("q5", "q7"):
        r = d["results"][q]
        assert r["max_abs_Im_Z"] < 1e-20                # вещественность
        assert abs(r["n_zeros_T120"] - r["n_bar_120"]) <= 1.0
        assert r["psi_chi_corr"] > 0.85                 # M2-аналог
        assert max(t["abs_diff"] for t in r["trace_formula"]) < 1e-4
    assert max(abs(g["r_H7"]) for g in d["gate_rank_projection"]) < 0.25


def test_c16_qinfo():
    d = _load("computations/C16_qinfo/data/results.json")
    assert d["Q1_gate_MI_max_z_vs_page"] > 10           # эхо локальности
    assert abs(d["Q2_MI_alignment"]["corr_MI_vs_zerowindow"]) < 0.3


def test_zeros_cache_deterministic():
    from hpbridge.zeros_mp import ensure_zeros
    g = ensure_zeros(100)
    assert abs(g[0] - 14.134725141734693) < 1e-6        # γ₁
    assert abs(g[99] - 236.524229665816) < 1e-4         # γ₁₀₀
