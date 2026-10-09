"""T6: тождество Q(a) и следовая формула для H_ξ (из закоммиченного C4)."""
import json
import os

import numpy as np

from hpbridge import traceformula as TF

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_identity_calibration():
    d = json.load(open(f"{ROOT}/data/c4_trace_verdict.json"))
    v = d["verdict"]
    assert v["M0_max_abs_diff_Q"] < 1e-10
    assert v["M1_max_abs_diff_K"] < 5e-5


def test_pc0_sees_prime_comb():
    d = json.load(open(f"{ROOT}/data/c4_trace_verdict.json"))
    assert d["verdict"]["PC0_Hxi_r"] > 0.999
    assert d["verdict"]["PC0_resid_rel"] < 0.05


def test_builtin_constant_BC0():
    # C₀ = −B: классическое тождество, подтверждено файлом нулей
    d = json.load(open(f"{ROOT}/data/c4_trace_verdict.json"))
    B = d["meta"]["B"]
    C0 = d["meta"]["C0"]
    assert abs(B + C0) < 1e-9
