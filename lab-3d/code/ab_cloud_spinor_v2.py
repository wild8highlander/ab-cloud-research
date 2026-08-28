"""
ab_cloud_spinor.py
==================
Spinor classification and Arf invariant for AB-Cloud vortex configurations.

Implements the 64-spinor classification on the L x L lattice with bipartite
structure (alpha = 1/2) and computes the Arf invariant under three conventions.

Monograph prediction: idx=38 spinor is in the odd-Arf sector.
"""
import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Spinor:
    """A spinor = binary vector in F_2^6 (64 elements) or F_2^{2k}."""
    bits: np.ndarray  # 0/1 array
    label: int

    @property
    def weight(self) -> int:
        return int(np.sum(self.bits))


def generate_spinors(n_bits: int = 6) -> List[Spinor]:
    """Generate all 2^n_bits spinors as binary vectors in F_2^n."""
    n_total = 2 ** n_bits
    spinors = []
    for k in range(n_total):
        bits = np.array([(k >> i) & 1 for i in range(n_bits)], dtype=int)
        spinors.append(Spinor(bits=bits, label=k))
    return spinors


def quadratic_form_Q(bits: np.ndarray, convention: str = "A") -> int:
    """
    Quadratic form Q: F_2^{2k} -> F_2 used in Arf invariant computation.
    Three conventions:
        A: Q(x) = sum_i x_{2i} x_{2i+1}                    (symplectic)
        B: Q(x) = sum_i x_{2i} x_{2i+1} + x_0              (shifted)
        C: Q(x) = sum_i x_i x_{i+1} (mod n)                (cyclic)
    """
    n = len(bits)
    if convention == "A":
        s = 0
        for i in range(0, n - 1, 2):
            s += bits[i] * bits[i + 1]
        return s % 2
    elif convention == "B":
        s = 0
        for i in range(0, n - 1, 2):
            s += bits[i] * bits[i + 1]
        s += bits[0]
        return s % 2
    elif convention == "C":
        s = 0
        for i in range(n):
            s += bits[i] * bits[(i + 1) % n]
        return s % 2
    else:
        raise ValueError(f"Unknown convention: {convention}")


def arf_invariant(spinors: List[Spinor], convention: str = "A") -> Dict:
    """
    Compute Arf invariant for the spinor set.
    Arf = 0 if #even-Q spinors > #odd-Q spinors, else Arf = 1.

    Returns dict with:
        n_even, n_odd, arf, convention
    """
    n_even = 0
    n_odd = 0
    for sp in spinors:
        q = quadratic_form_Q(sp.bits, convention=convention)
        if q == 0:
            n_even += 1
        else:
            n_odd += 1
    arf = 0 if n_even > n_odd else 1
    return {
        "n_even": n_even,
        "n_odd": n_odd,
        "arf": arf,
        "convention": convention,
    }


def spinor_classification(n_bits: int = 6) -> Dict:
    """
    Full 64-spinor classification with all three Arf conventions.
    Monograph prediction: idx=38 spinor is odd-Arf.
    """
    spinors = generate_spinors(n_bits)
    n_total = len(spinors)

    # Convention A
    res_A = arf_invariant(spinors, "A")
    # Convention B
    res_B = arf_invariant(spinors, "B")
    # Convention C
    res_C = arf_invariant(spinors, "C")

    # Check idx=38 (label 38)
    target = 38
    target_sp = next((s for s in spinors if s.label == target), None)
    target_Q = {}
    if target_sp is not None:
        for conv in ["A", "B", "C"]:
            target_Q[conv] = quadratic_form_Q(target_sp.bits, conv)

    return {
        "n_total": n_total,
        "n_bits": n_bits,
        "n_even": res_A["n_even"],
        "n_odd": res_A["n_odd"],
        "conventions": {
            "A": res_A["arf"],
            "B": res_B["arf"],
            "C": res_C["arf"],
        },
        "convention_counts": {
            "A": {"even": res_A["n_even"], "odd": res_A["n_odd"]},
            "B": {"even": res_B["n_even"], "odd": res_B["n_odd"]},
            "C": {"even": res_C["n_even"], "odd": res_C["n_odd"]},
        },
        "idx_38_Q": target_Q,
        "idx_38_parity_A": "odd" if target_Q.get("A") == 1 else "even",
    }


if __name__ == "__main__":
    r = spinor_classification(6)
    print(f"Total spinors: {r['n_total']}")
    print(f"Convention A: even={r['convention_counts']['A']['even']}, odd={r['convention_counts']['A']['odd']}")
    print(f"Convention B: even={r['convention_counts']['B']['even']}, odd={r['convention_counts']['B']['odd']}")
    print(f"Convention C: even={r['convention_counts']['C']['even']}, odd={r['convention_counts']['C']['odd']}")
    print(f"idx=38 Q values: {r['idx_38_Q']}")
