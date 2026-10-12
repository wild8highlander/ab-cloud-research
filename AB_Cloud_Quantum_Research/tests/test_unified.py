#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_unified.py — smoke-тесты целостности пакета AB Cloud Quantum
Research v1.0.0 (структура, вердикты, документы, фигуры, формальный слой)."""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_structure():
    for d in ("modules", "theorems_lemmas", "figures_tiled", "formal",
              "web_lab", "scripts", "tests", "assets", "docs",
              "research", "datasets", "timeline", "atlas", "glossary",
              "whitepaper"):
        assert os.path.isdir(os.path.join(ROOT, d)), d


def test_theorem_docs_12_pairs():
    n_pdf, n_docx = 0, 0
    for d in os.listdir(os.path.join(ROOT, "theorems_lemmas")):
        p = os.path.join(ROOT, "theorems_lemmas", d)
        if os.path.isdir(p) and d.startswith("T0"):
            n_pdf += len([f for f in os.listdir(p) if f.endswith(".pdf")])
            n_docx += len([f for f in os.listdir(p) if f.endswith(".docx")])
    assert n_pdf == 12 and n_docx == 12, (n_pdf, n_docx)


def test_spinor_theorem_docs_12():
    base = os.path.join(ROOT, "research", "realtime_spinor_memory",
                        "theorems")
    n_pdf, n_docx = 0, 0
    for d in os.listdir(base):
        p = os.path.join(base, d)
        if os.path.isdir(p) and d.startswith("TS"):
            n_pdf += len([f for f in os.listdir(p) if f.endswith(".pdf")])
            n_docx += len([f for f in os.listdir(p) if f.endswith(".docx")])
    assert n_pdf == 6 and n_docx == 6, (n_pdf, n_docx)


def test_spinor_verdicts_all_pass():
    base = os.path.join(ROOT, "research", "realtime_spinor_memory", "data")
    for tag in ("es1_cycles", "es2_volatility", "es3_realtime",
                "es4_memoryless_task", "es5_noise"):
        v = json.load(open(os.path.join(base, f"{tag}_verdict.json")))
        assert v["pass"] is True, tag


def test_showcase_folders():
    assert len(os.listdir(os.path.join(ROOT, "datasets"))) >= 4
    assert os.path.isfile(os.path.join(ROOT, "glossary", "glossary.md"))
    for lang in ("ru", "en"):
        assert os.path.isfile(os.path.join(
            ROOT, "atlas", f"atlas_flagships_{lang}.png"))
        assert os.path.isfile(os.path.join(
            ROOT, "timeline", f"campaign_timeline_{lang}.png"))
        assert os.path.isfile(os.path.join(
            ROOT, "whitepaper", f"whitepaper_{lang}.pdf"))


def test_tiled_figures_12():
    n = 0
    for lang in ("ru", "en"):
        p = os.path.join(ROOT, "figures_tiled", lang)
        n += len([f for f in os.listdir(p) if f.endswith(".png")])
    assert n == 12, n


def test_verdicts():
    m = json.load(open(os.path.join(
        ROOT, "modules/verifier_multilang/results/verdicts_master.json")))
    assert m["all_pre_registered_pass"] is True
    assert len(m["passes"]) == 18


def test_obligations_blocked():
    ob = json.load(open(os.path.join(
        ROOT, "modules/core_spectrum/formal/obligations.json")))
    assert ob["verdict"] == "blocked"


def test_formal_no_sorry():
    import re
    lean = open(os.path.join(ROOT,
                "modules/core_spectrum/formal/lean/RPTheorems.lean")).read()
    lean_code = re.sub(r"/-.*?-/", "", lean, flags=re.S)
    lean_code = re.sub(r"--[^\n]*", "", lean_code)
    assert "sorry" not in lean_code
    coq = open(os.path.join(ROOT,
               "modules/core_spectrum/formal/coq/RPTheorems.v")).read()
    coq_code = re.sub(r"\(\*.*?\*\)", "", coq, flags=re.S)
    assert "Admitted" not in coq and "admit" not in coq_code.lower()


def test_web_labs_tabs():
    core = open(os.path.join(ROOT,
                "modules/core_spectrum/web_lab/index.html")).read()
    assert "Теоремы (Th1–Th6)" in core
    qp = open(os.path.join(ROOT,
              "modules/processor_ab/web_lab/index.html")).read()
    assert "Теоремы (Th1–Th6)" in qp
    portal = open(os.path.join(ROOT, "web_lab/index.html")).read()
    assert "verifier_multilang" in portal


def test_validate_package_passes():
    r = subprocess.run([sys.executable,
                        os.path.join(ROOT, "scripts/validate_package.py")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted({k: v for k, v in globals().items()
                            if k.startswith("test_")}.items()):
        try:
            fn()
            print(f"  ✓ {name}")
        except AssertionError as e:
            print(f"  ✗ {name}: {e}")
            fails += 1
    print("PASS" if fails == 0 else f"FAIL: {fails}")
    sys.exit(1 if fails else 0)
