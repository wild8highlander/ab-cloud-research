#!/usr/bin/env python3
"""Section 6 — Riemann-zeros / Gram-point canon.

REAL check (stdlib only, independent path):
  the suite's Gram points solve theta(t) = pi*k with the 5-term asymptotic
    theta(t) = t/2*ln(t/2pi) - t/2 - pi/8 + 1/(48t) + 7/(5760 t^3).
  The suite finds the root via Lambert-W seed + 8 Newton steps. Here we
  re-derive the SAME root by pure BISECTION (no Lambert W, no Newton) and
  verify it matches the frozen golden constants:
    gram_point(1) = 23.17028270133466
    gram_point(2) = 27.670182217848343
    gram_point(3) = 31.71797995477886
  to < 1e-9 absolute. This independently validates the whole Gram-point
  canon (and would have caught the old seed-only / 2*pi*W(n/e) bugs).
Exit code 1 on any failure.
"""
import math

GOLDEN = {1: 23.17028270133466, 2: 27.670182217848343, 3: 31.71797995477886}


def theta(t: float) -> float:
    """5-term Riemann–Siegel theta asymptotics."""
    arg = t / (2.0 * math.pi)
    return (t / 2.0) * math.log(arg) - t / 2.0 - math.pi / 8.0 \
        + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t ** 3)


def gram_bisection(k: int, lo: float = 5.0, hi: float = 100000.0,
                   iters: int = 200) -> float:
    """Root of theta(t) = pi*k by bisection (theta is monotone for t > ~6)."""
    target = math.pi * k
    flo, fhi = theta(lo) - target, theta(hi) - target
    assert flo < 0 < fhi, "bracket failure"
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if theta(mid) - target < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> int:
    print("=== Section 6: Riemann zeros / Gram-point canon (bisection cross-check) ===")
    all_ok = True
    for k, expected in GOLDEN.items():
        root = gram_bisection(k)
        d = abs(root - expected)
        ok = d < 1e-9
        all_ok = all_ok and ok
        print(f"  gram_point({k}): bisection = {root:.12f}  golden = {expected:.12f}"
              f"  Δ = {d:.3e}  -> {'PASS' if ok else 'FAIL'}")
    print("PASS" if all_ok else "FAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
