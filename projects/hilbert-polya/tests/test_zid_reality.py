"""T2: вещественность Z_id на критической линии."""
from hpbridge.identity import Z_id


def test_reality():
    for t in (1.0, 17.3, 48.0, 100.0):
        re, im = Z_id(t, dps=30)
        assert abs(im) < 1e-25
        assert isinstance(re, float)


def test_parity():
    a = Z_id(7.5, dps=30)
    b = Z_id(-7.5, dps=30)
    assert abs(a[0] - b[0]) < 1e-20
