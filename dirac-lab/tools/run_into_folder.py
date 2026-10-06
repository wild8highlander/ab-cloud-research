#!/usr/bin/env python3
"""v1.4 documentation overhaul — regenerate canonical per-test artifacts
directly into tests/DXX_*/ folders using the ORIGINAL validated harness.

For every test D1..D14 the module-level test function runs in FULL mode with
  dl._FIG_DIR = tests/<folder>/figures
  dl._RES_DIR = tests/<folder>
so the canonical 600-dpi figure and the CSV land inside the test folder, and
a per-test results.json (checks ledger) is written next to them.

Usage: python3 run_per_test_folders.py <group>   group in {core, ext, ext2, ext3}
"""
import json
import os
import sys
import time
import traceback

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "code"))

import dirac_lab as dl  # noqa: E402
import dirac_lab_extensions as ext  # noqa: E402
import dirac_lab_extensions2 as ext2  # noqa: E402
import dirac_lab_extensions3 as ext3  # noqa: E402

FOLDERS = {
    "D1": "D01_bloch_continuum_limit",
    "D2": "D02_zero_mode_tower",
    "D3": "D03_berry_phase",
    "D4": "D04_relativistic_landau_levels",
    "D5": "D05_klein_tunneling",
    "D6": "D06_zitterbewegung",
    "D7": "D07_zeta_decoration",
    "D8": "D08_chiral_protection",
    "D9": "D09_jr_index_restoration",
    "D10": "D10_montgomery_transport",
    "D11": "D11_bk_connes_conjugation",
    "D12": "D12_bk_ladder_infinite_limit",
    "D13": "D13_wall_under_conjugation_drive",
    "D14": "D14_odlyzko_form_factor",
}

GROUPS = {
    "core": ("dirac_lab", "TESTS"),
    "ext": ("dirac_lab_extensions", "TESTS_EXT"),
    "ext2": ("dirac_lab_extensions2", "TESTS_EXT2"),
    "ext3": ("dirac_lab_extensions3", "TESTS_EXT3"),
}


def list_name(mod):
    for cand in ("TESTS", "TESTS_EXT", "TESTS_EXT2", "TESTS_EXT3"):
        if hasattr(mod, cand):
            return cand
    raise AttributeError("no TESTS list found")


def run_group(group: str):
    mod = {"core": dl, "ext": ext, "ext2": ext2, "ext3": ext3}[group]
    dl._QUICK = False
    dl._MAKE_FIGURES = True
    dl.SEED = 96

    zeros = dl.load_zeta_zeros(os.path.join(ROOT, "data",
                                            "zeta_zeros_2000.txt"), 2000)
    if group == "ext3":
        ext3.ZEROS_LOW = dl.load_zeta_zeros(os.path.join(
            ROOT, "data", "zeta_zeros_low_600.txt"), 600)
        ext3.ZEROS_BIG = dl.load_zeta_zeros(os.path.join(
            ROOT, "data", "zeta_zeros_high_2000.txt"), 2000)

    lname = list_name(mod)
    suite = getattr(mod, lname)
    for tid, title, fn in suite:
        folder = os.path.join(ROOT, "tests", FOLDERS[tid])
        figdir = os.path.join(folder, "figures")
        os.makedirs(figdir, exist_ok=True)
        dl._RES_DIR = folder
        dl._FIG_DIR = figdir
        res = dl.TestResult(tid=tid, title=title)
        dl.banner(tid, title)
        t0 = time.time()
        try:
            fn(res, zeros)
        except Exception as e:  # noqa: BLE001
            traceback.print_exc()
            res.check(f"{tid} crashed: {e}", False, "exception")
        n_ok = sum(1 for _, ok, _ in res.checks if ok)
        out = {
            "tid": res.tid,
            "title": res.title,
            "verdict": res.verdict,
            "checks": [[n, bool(ok), d] for n, ok, d in res.checks],
            "n_pass": n_ok,
            "n_total": len(res.checks),
            "elapsed_s": round(time.time() - t0, 2),
            "mode": "FULL",
            "seed": 96,
            "provenance": ("regenerated v1.4 into tests/ with the canonical "
                           "harness; ledger matches results/"
                           "run_20261006_full_v13"),
        }
        with open(os.path.join(folder, "results.json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
        print(f"  → {folder}  [{res.verdict} {n_ok}/{len(res.checks)}]  "
              f"({time.time() - t0:.1f}s)", flush=True)


if __name__ == "__main__":
    grp = sys.argv[1] if len(sys.argv) > 1 else "core"
    t0 = time.time()
    print(f"=== per-test folder regeneration: group {grp} ===", flush=True)
    run_group(grp)
    print(f"=== group {grp} done in {time.time() - t0:.1f}s ===", flush=True)
