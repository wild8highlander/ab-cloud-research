"""Th5: блочная редукция на торе (живой пересчёт, L=12)."""
from rpbridge.symmetry import part_a_exact_reduction


def test_commutators_exact():
    a = part_a_exact_reduction(12)
    assert a['eps_Ux'] < 1e-10
    assert a['eps_Uy'] < 1e-10


def test_block_union():
    a = part_a_exact_reduction(12)
    assert a['block_union_err'] < 1e-9
    assert a['offdiag_max'] < 1e-8
