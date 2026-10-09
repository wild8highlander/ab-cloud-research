"""Бит-в-бит воспроизведение протокола C3 (эталонный затвор Nv=0)."""
import csv
import os

from engine.solver import gate_spectrum

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_reference_gate_bits():
    rows = list(csv.DictReader(open(f"{ROOT}/data/c3_gates_table.csv")))
    ref = float(rows[0]["mean_spacing"])  # Nv=0, W=0.5, alpha=0.5
    _, dbar, _ = gate_spectrum(0, 0.0, 0.5, 0.5)
    assert abs(dbar - ref) / ref < 1e-10
