"""T1: Γ-замыкания при dps = 40 (порог 1e-35)."""
import numpy as np
from hpbridge.identity import gamma_ladder_closures


def test_three_closures_at_dps40():
    res = gamma_ladder_closures([0.5, 1.0, 2.0, 3.5])
    assert max(max(r) for r in res) < 1e-35


def test_residuals_match_committed():
    # порядок величин из вердикта C1
    res = gamma_ladder_closures([1.0])
    assert all(r < 1e-35 for r in res[0])
