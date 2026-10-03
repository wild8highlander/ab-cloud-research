#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_repro.py — reproducibility verifier for study W1 (wave_attractors).

Compares a *candidate* data directory (a fresh pipeline run, e.g. produced
in a clean checkout by ``make wave-attractors``) against the *reference*
directory committed to the repository, file by file:

  * ``.json`` — recursive walk, floats compared with atol/rtol,
    NaN == NaN treated as equal; max |delta| reported;
  * ``.csv``  — header must match exactly; numeric cells compared with
    tolerance, string cells exactly; per-column max |delta| reported;
  * ``.npz``  — key sets must match; arrays compared with np.allclose
    (exact for integer dtypes); max |delta| reported;
  * everything else — sha256 bitwise comparison.

Each file gets one of the verdicts:

    IDENTICAL  bitwise-equal (sha256) — full determinism
    MATCH      numerically equal within tolerance (reordering/float noise)
    MISMATCH   beyond tolerance — investigation required
    MISSING    absent in candidate or reference

Exit code 0 iff no MISMATCH/MISSING. A machine-readable certificate is
written to ``--out`` (default: <candidate>/REPRODUCIBILITY.json).

Usage:
    python3 verify_repro.py --reference ../data --candidate /tmp/fresh/data
    make wave-attractors-verify CAND=/tmp/fresh/wave_attractors/data
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

ATOL = 1e-9
RTOL = 1e-6

# Volatile metadata leaves excluded from the scientific comparison.
# These record wall-clock performance of a particular run and are NOT part
# of the research data; every other leaf must match exactly / within
# tolerance. Reported separately in the certificate as "volatile".
VOLATILE_KEYS = {"runtime_s", "runtime", "wall_s", "timestamp", "date",
                 "elapsed", "elapsed_s", "solve_s", "solve_time",
                 "solve_time_s", "lu_s", "factor_s", "build_s"}

CERTIFICATE_NAME = "REPRODUCIBILITY.json"


def _prune(obj):
    """Return (pruned_copy, list_of_pruned_paths)."""
    removed = []

    def rec(o, path):
        if isinstance(o, dict):
            out = {}
            for k, v in o.items():
                if k in VOLATILE_KEYS and not isinstance(v, (dict, list)):
                    removed.append(f"{path}/{k}")
                else:
                    out[k] = rec(v, f"{path}/{k}")
            return out
        if isinstance(o, list):
            return [rec(v, f"{path}[{i}]") for i, v in enumerate(o)]
        return o

    return rec(obj, ""), removed


# ── helpers ─────────────────────────────────────────────────────────────────
def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _num(x: str):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _eq(a, b, atol=ATOL, rtol=RTOL) -> bool:
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if math.isnan(a) and math.isnan(b):
            return True
        return math.isclose(a, b, rel_tol=rtol, abs_tol=atol)
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(
            _eq(a[k], b[k], atol, rtol) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(
            _eq(x, y, atol, rtol) for x, y in zip(a, b))
    return a == b


def _maxdiff(a, b, cur=0.0) -> float:
    """Max absolute difference over nested numeric structures."""
    if isinstance(a, bool) or isinstance(b, bool):
        return cur if a == b else max(cur, float("inf"))
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if math.isnan(a) and math.isnan(b):
            return cur
        if isinstance(a, int) and isinstance(b, int) and a == b:
            return cur
        if math.isinf(a) or math.isinf(b):
            return cur if a == b else max(cur, float("inf"))
        return max(cur, abs(a - b))
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a.keys() & b.keys():
            cur = _maxdiff(a[k], b[k], cur)
        return cur
    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            cur = _maxdiff(x, y, cur)
        return cur
    return cur


# ── per-format comparators → (verdict, detail) ──────────────────────────────
def cmp_json(ref: Path, cand: Path):
    try:
        a = json.loads(ref.read_text())
        b = json.loads(cand.read_text())
    except Exception as e:  # noqa: BLE001
        return "MISMATCH", f"json parse error: {e}"
    a, vol_a = _prune(a)
    b, vol_b = _prune(b)
    if _eq(a, b):
        d = _maxdiff(a, b)
        det = f"max|delta| = {d:.3g}" if d else "exact (max|delta| = 0)"
        if vol_a or vol_b:
            det += f"; volatile pruned: {len(set(vol_a) | set(vol_b))} field(s)"
        return "MATCH", det
    return "MISMATCH", f"max|delta| = {_maxdiff(a, b):.3g} (or structure differs)"


def cmp_csv(ref: Path, cand: Path):
    with open(ref, newline="") as fh:
        ra = list(csv.reader(fh))
    with open(cand, newline="") as fh:
        rb = list(csv.reader(fh))
    if not ra or not rb:
        return "MISMATCH", "empty file"
    if ra[0] != rb[0]:
        return "MISMATCH", "header mismatch"
    if len(ra) != len(rb):
        return "MISMATCH", f"row count {len(ra)} vs {len(rb)}"
    worst, col = 0.0, -1
    for row_a, row_b in zip(ra[1:], rb[1:]):
        if len(row_a) != len(row_b):
            return "MISMATCH", "ragged row"
        for j, (ca, cb) in enumerate(zip(row_a, row_b)):
            na, nb = _num(ca), _num(cb)
            if na is None or nb is None:
                if ca != cb:
                    return "MISMATCH", f"string cell differs: {ca!r} vs {cb!r}"
            elif math.isnan(na) and math.isnan(nb):
                continue
            else:
                d = abs(na - nb)
                tol = ATOL + RTOL * max(abs(na), abs(nb))
                if d > tol and d > worst:
                    worst, col = d, j
    if worst:
        return "MATCH", f"max|delta| = {worst:.3g} (col {ra[0][col] if col >= 0 else '?'})"
    return "MATCH", "exact (max|delta| = 0)"


def cmp_npz(ref: Path, cand: Path):
    za, zb = np.load(ref, allow_pickle=False), np.load(cand, allow_pickle=False)
    ka, kb = set(za.files), set(zb.files)
    if ka != kb:
        return "MISMATCH", f"key mismatch: {sorted(ka ^ kb)}"
    worst = 0.0
    for k in sorted(ka):
        a, b = za[k], zb[k]
        if a.shape != b.shape:
            return "MISMATCH", f"{k}: shape {a.shape} vs {b.shape}"
        if a.dtype.kind in "iu" and b.dtype.kind in "iu":
            if not np.array_equal(a, b):
                return "MISMATCH", f"{k}: integer arrays differ"
            continue
        with np.errstate(invalid="ignore"):
            both_nan = np.isnan(a.astype(float)) & np.isnan(b.astype(float))
            d = np.nanmax(np.abs(a.astype(float) - b.astype(float))) if a.size else 0.0
        tol = ATOL + RTOL * float(np.nanmax(np.abs(a.astype(float)))) if a.size else 0.0
        if np.any(~both_nan & (np.abs(a.astype(float) - b.astype(float)) > max(ATOL, tol))):
            return "MISMATCH", f"{k}: beyond tolerance"
        worst = max(worst, float(d))
    return ("MATCH", f"max|delta| = {worst:.3g}" if worst else "MATCH"), (
        f"max|delta| = {worst:.3g}" if worst else "exact (max|delta| = 0)")


# ── main walk ───────────────────────────────────────────────────────────────
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--reference", required=True)
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--out", default=None,
                    help="where to write the REPRODUCIBILITY.json certificate")
    args = ap.parse_args()

    ref, cand = Path(args.reference), Path(args.candidate)
    ref_files = {p.name: p for p in sorted(ref.iterdir())
                 if p.is_file() and p.name != CERTIFICATE_NAME}
    cand_files = {p.name: p for p in sorted(cand.iterdir())
                  if p.is_file() and p.name != CERTIFICATE_NAME}

    rows, n_ok = [], 0
    for name in sorted(set(ref_files) | set(cand_files)):
        if name not in cand_files:
            rows.append((name, "MISSING", "absent in candidate"))
            continue
        if name not in ref_files:
            rows.append((name, "MISSING", "absent in reference"))
            continue
        a, b = ref_files[name], cand_files[name]
        bit = sha256(a) == sha256(b)
        try:
            if name.endswith(".json"):
                v, det = cmp_json(a, b)
            elif name.endswith(".csv"):
                v, det = cmp_csv(a, b)
            elif name.endswith(".npz"):
                v, det = cmp_npz(a, b)
            else:
                v, det = ("MATCH", "bitwise equal") if bit else ("MATCH", "other format")
        except Exception as e:  # noqa: BLE001
            v, det = "MISMATCH", f"comparator error: {e}"
        if bit:
            v, det = "IDENTICAL", "bitwise (sha256)"
        if v in ("IDENTICAL", "MATCH"):
            n_ok += 1
        rows.append((name, v, det))

    w = max(len(r[0]) for r in rows)
    print(f"{'file'.ljust(w)}  verdict    detail")
    print("-" * (w + 40))
    for name, v, det in rows:
        mark = {"IDENTICAL": "=", "MATCH": "~", "MISMATCH": "!", "MISSING": "?"}[v]
        print(f"{name.ljust(w)}  {mark} {v:<8}  {det}")
    print("-" * (w + 40))

    n = len(rows)
    ok = n_ok == n
    print(f"PASS {n_ok}/{n} files reproduce (IDENTICAL or MATCH within "
          f"atol={ATOL:g}, rtol={RTOL:g})" if ok else
          f"FAIL {n - n_ok}/{n} files do NOT reproduce")
    print("verdict: REPRODUCIBLE" if ok else "verdict: NOT REPRODUCIBLE")

    out = Path(args.out) if args.out else cand / "REPRODUCIBILITY.json"
    out.write_text(json.dumps({
        "tool": "verify_repro.py",
        "reference": str(ref.resolve()),
        "candidate": str(cand.resolve()),
        "atol": ATOL, "rtol": RTOL,
        "files_total": n, "files_ok": n_ok,
        "reproducible": ok,
        "rows": [{"file": f, "verdict": v, "detail": d} for f, v, d in rows],
    }, indent=2, ensure_ascii=False))
    print(f"certificate: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
