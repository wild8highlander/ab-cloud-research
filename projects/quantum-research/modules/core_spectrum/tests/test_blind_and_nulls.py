"""V1/V2: слепой нуль и GUE-класс (коммиченные вердикты)."""
import json
import os


def _v(name):
    p = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'data', name)
    return json.load(open(p))


def test_blind_in_null():
    d = _v('v01_verdict.json')
    assert abs(d['r_test'] - d['perm_null_mean']) < 2 * d['perm_null_sd']


def test_m0_gue_and_ladder():
    d = _v('v02_verdict.json')
    m = d['models']
    assert m['M0_ab_cloud']['KS_GUE'] < 0.15
    assert m['REF_POISSON']['KS_GUE'] > m['REF_GUE']['KS_GUE']
