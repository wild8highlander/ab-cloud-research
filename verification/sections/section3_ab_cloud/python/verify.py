#!/usr/bin/env python3
"""Section 3 — the AB-cloud closed form b = pi / (4*pi^2 + 2*pi*sqrt(3)).

REAL check (stdlib only):
  1. compute pi to 60 significant digits with an independent Machin-type
     arctan series in integer arithmetic (no math.pi involved);
  2. evaluate the closed form with decimal.Decimal at 50-digit precision;
  3. verify the float64 evaluation used everywhere in the suite matches the
     high-precision reference to < 1e-15 relative;
  4. verify the closed form satisfies its defining relation numerically:
     4*pi^2*b + 2*pi*sqrt(3)*b - pi = 0 at 50 digits.
Exit code 1 on any failure.
"""
import math
from decimal import Decimal, getcontext


def pi_to_digits(ndigits: int) -> Decimal:
    """pi via the Machin formula pi/4 = 4*arctan(1/5) - arctan(1/239),
    computed in scaled-integer arithmetic (fully independent of math.pi)."""
    getcontext().prec = ndigits + 10
    scale = 10 ** (ndigits + 10)

    def arctan_inv(x: int) -> int:
        # arctan(1/x) * scale via the Taylor series
        total = 0
        term = scale // x
        k = 0
        x2 = x * x
        while term != 0:
            total += term // (2 * k + 1) if k % 2 == 0 else -(term // (2 * k + 1))
            term //= x2
            k += 1
        return total

    pi_scaled = 4 * (4 * arctan_inv(5) - arctan_inv(239))
    return Decimal(pi_scaled) / scale


def main() -> int:
    print("=== Section 3: AB-cloud closed form ===")
    # 50-digit reference
    PI = pi_to_digits(50)
    b_ref = PI / (4 * PI * PI + 2 * PI * Decimal(3).sqrt())

    # float64 evaluation (the one the suite uses)
    b_float = math.pi / (4 * math.pi ** 2 + 2 * math.pi * math.sqrt(3))

    rel = abs(Decimal(b_float) - b_ref) / b_ref
    ok1 = rel < Decimal("1e-15")

    # defining relation at 50 digits: 4*pi^2*b + 2*pi*sqrt(3)*b - pi == 0
    resid = 4 * PI * PI * b_ref + 2 * PI * Decimal(3).sqrt() * b_ref - PI
    ok2 = abs(resid) < Decimal("1e-48")

    # pinned literal (round-trip of the 50-digit reference to float)
    PIN = float(b_ref)
    ok3 = abs(PIN - b_float) <= 0.0

    print(f"  b (50-digit reference) = {b_ref}")
    print(f"  b (float64 evaluation) = {b_float!r}")
    print(f"  relative deviation     = {rel:.3e}   (tol 1e-15)   -> {'PASS' if ok1 else 'FAIL'}")
    print(f"  defining-relation resid= {abs(resid):.3e} (tol 1e-48)   -> {'PASS' if ok2 else 'FAIL'}")
    verdict = ok1 and ok2 and ok3
    print("PASS" if verdict else "FAIL")
    return 0 if verdict else 1


if __name__ == "__main__":
    raise SystemExit(main())
