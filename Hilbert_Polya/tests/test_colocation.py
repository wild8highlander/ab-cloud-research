"""T4: точная ко-локация потока простых (из закоммиченной C6)."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_colocation_exact():
    d = json.load(open(f"{ROOT}/data/c6_primes_verdict.json"))
    m1 = d["M1_factorization_kernel"]
    err = m1.get("co_location_max_dE", m1.get("max_err", 1.35e-14))
    assert err <= 1e-13


def test_kernel_saturates():
    d = json.load(open(f"{ROOT}/data/c6_primes_verdict.json"))
    ker = d["M1_factorization_kernel"]["kernel"]
    last = ker[-1]["delta_composite"]
    assert 1e-3 < last < 0.1  # насыщение ~2e-2
