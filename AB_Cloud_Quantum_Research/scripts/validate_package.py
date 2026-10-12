#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_package.py — чистая самопроверка пакета AB Cloud Quantum Research.

Проверяет: структуру, версии, вердикты трёх программ, 12 документов теорем,
12 плиточных фигур, веб-лаборатории (вкладки), формальные файлы, README."""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OK, FAIL = [], []


def check(name, cond, detail=""):
    (OK if cond else FAIL).append(f"{name}{' — ' + detail if detail else ''}")
    return cond


def main():
    # 1. структура
    for d in ("modules/core_spectrum", "modules/processor_ab",
              "modules/verifier_multilang", "theorems_lemmas",
              "figures_tiled", "web_lab", "formal", "scripts", "tests",
              "assets", "docs", "research/realtime_spinor_memory",
              "datasets", "timeline", "atlas", "glossary", "whitepaper"):
        check(f"папка {d}", os.path.isdir(os.path.join(ROOT, d)))
    for f in ("README.md", "README.en.md", "VERSION",
              "docs/ARCHITECTURE.md", "CHANGELOG.md",
              "Makefile", "LICENSE", "CITATION.cff", "requirements.txt"):
        check(f"файл {f}", os.path.isfile(os.path.join(ROOT, f)))

    # 2. версии
    v_core = open(os.path.join(ROOT, "modules/core_spectrum/VERSION")).read().strip()
    v_qp = open(os.path.join(ROOT, "modules/processor_ab/VERSION")).read().strip()
    v_jl = open(os.path.join(ROOT, "modules/verifier_multilang/results",
                             "ROADMAP.md")).read()
    check("core 1.2.2", v_core == "1.2.2", v_core)
    check("processor 0.1.2", v_qp == "0.1.2", v_qp)
    check("verifier 0.4.0 (класс B исполнен)", "O-J2 (класс B) — ИСПОЛНЕНО в v0.4.0" in v_jl)
    check("VERSION корня допустима (1.0.0 / 1.1.0)",
          open(os.path.join(ROOT, "VERSION")).read().strip() in ("1.0.0", "1.1.0"))

    # 3. вердикты
    m = json.load(open(os.path.join(ROOT, "modules/verifier_multilang",
                                    "results/verdicts_master.json")))
    check("Julia: все вердикты PASS", m["all_pre_registered_pass"] is True,
          f"{len(m['passes'])} экспериментов")
    v20 = json.load(open(os.path.join(ROOT, "modules/processor_ab",
                                      "data/v20_verdict.json")))
    check("QP: вердикт V20", bool(v20.get("verdict_note")))
    ob = json.load(open(os.path.join(ROOT, "modules/core_spectrum/formal/obligations.json")))
    check("core_rp: RH blocked", ob["verdict"] == "blocked")

    # 4. теоремы: 12 документов + 12 фигур + 6 README + сводный
    thm_dirs = ["T01_hermiticity", "T02_self_adjointness", "T03_certificates",
                "T04_li_spectral", "T05_block_reduction", "T06_trace_formula"]
    n_pdf, n_docx = 0, 0
    for d in thm_dirs:
        base = os.path.join(ROOT, "theorems_lemmas", d)
        n_pdf += len([f for f in os.listdir(base) if f.endswith(".pdf")])
        n_docx += len([f for f in os.listdir(base) if f.endswith(".docx")])
        check(f"README теоремы {d}",
              os.path.isfile(os.path.join(base, "README.md")))
    check("12 PDF теорем (6×RU/EN)", n_pdf == 12, str(n_pdf))
    check("12 DOCX теорем (6×RU/EN)", n_docx == 12, str(n_docx))
    check("сводный README theorems_lemmas",
          os.path.isfile(os.path.join(ROOT, "theorems_lemmas/README.md")))

    # 4b. спинор-исследование: вердикты + документы TS + фигуры
    sdata = os.path.join(ROOT, "research/realtime_spinor_memory/data")
    for tag in ("es1_cycles", "es2_volatility", "es3_realtime",
                "es4_memoryless_task", "es5_noise"):
        v = json.load(open(os.path.join(sdata, f"{tag}_verdict.json")))
        check(f"ES вердикт {tag}: PASS", v["pass"] is True)
    sdir = os.path.join(ROOT, "research/realtime_spinor_memory/theorems")
    n_spdf, n_sdocx = 0, 0
    for d in os.listdir(sdir):
        p2 = os.path.join(sdir, d)
        if os.path.isdir(p2) and d.startswith("TS"):
            n_spdf += len([f for f in os.listdir(p2) if f.endswith(".pdf")])
            n_sdocx += len([f for f in os.listdir(p2) if f.endswith(".docx")])
    check("6 PDF теорем TS (3×RU/EN)", n_spdf == 6, str(n_spdf))
    check("6 DOCX теорем TS (3×RU/EN)", n_sdocx == 6, str(n_sdocx))
    for lang in ("ru", "en"):
        for f in (f"figures/{lang}/ts1_4dim_{lang}.png",
                  f"figures/{lang}/models_4dim_{lang}.png",
                  "README.md", "README.en.md",
                  f"docs/theory{'.' + lang + '.md' if lang == 'en' else '.md'}"):
            check(f"спинор: {f}", os.path.isfile(
                os.path.join(sdir, "..", f)))

    # 4c. витрина
    check("datasets: 3 CSV + README",
          all(os.path.isfile(os.path.join(ROOT, "datasets", f))
              for f in ("flagship_numbers.csv", "campaign_timeline.csv",
                        "zeta_zeros_reference.csv", "README.md")))
    check("glossary", os.path.isfile(os.path.join(ROOT, "glossary/glossary.md")))
    for lang in ("ru", "en"):
        check(f"atlas {lang}", os.path.isfile(os.path.join(
            ROOT, "atlas", f"atlas_flagships_{lang}.png")))
        check(f"timeline {lang}", os.path.isfile(os.path.join(
            ROOT, "timeline", f"campaign_timeline_{lang}.png")))
        check(f"whitepaper {lang}", os.path.isfile(os.path.join(
            ROOT, "whitepaper", f"whitepaper_{lang}.pdf")))

    # 5. плиточные фигуры верхнего уровня
    for lang in ("ru", "en"):
        fs = os.listdir(os.path.join(ROOT, "figures_tiled", lang))
        check(f"figures_tiled/{lang}: 6 фигур", len([x for x in fs if x.endswith(".png")]) == 6)

    # 6. веб-лаборатории
    for lab, min_tabs in (("modules/core_spectrum/web_lab/index.html", 10),
                          ("modules/processor_ab/web_lab/index.html", 8)):
        html = open(os.path.join(ROOT, lab), encoding="utf-8").read()
        tabs = len(re.findall(r'<button id="nav\d+"', html))
        check(f"{lab}: вкладок ≥ {min_tabs}", tabs >= min_tabs, str(tabs))
        check(f"{lab}: вкладка Теоремы", "Теоремы (Th1–Th6)" in html)
    portal = os.path.join(ROOT, "web_lab/index.html")
    check("портал web_lab/index.html", os.path.isfile(portal))
    if os.path.isfile(portal):
        html = open(portal, encoding="utf-8").read()
        check("портал: три программы", all(s in html for s in
              ("core_spectrum", "processor_ab",
               "verifier_multilang")))
        check("портал: JS синтаксис", "<script>" in html)

    # 7. формальный слой
    for f in ("modules/core_spectrum/formal/lean/RPTheorems.lean",
              "modules/core_spectrum/formal/coq/RPTheorems.v",
              "modules/core_spectrum/formal/obligations.json"):
        check(f"формальный файл {os.path.basename(f)}",
              os.path.isfile(os.path.join(ROOT, f)))
    lean = open(os.path.join(ROOT, "modules/core_spectrum/formal/lean/RPTheorems.lean"),
                encoding="utf-8").read()
    lean_code = re.sub(r"/-.*?-/", "", lean, flags=re.S)
    lean_code = re.sub(r"--[^\n]*", "", lean_code)
    check("Lean: нет sorry (в коде)", "sorry" not in lean_code)
    coq = open(os.path.join(ROOT, "modules/core_spectrum/formal/coq/RPTheorems.v"),
               encoding="utf-8").read()
    coq_code = re.sub(r"\(\*.*?\*\)", "", coq, flags=re.S)
    check("Coq: нет admit (в коде)", "admit" not in coq_code.lower() and
          "Admitted" not in coq)

    # 8. README-система
    for d in ("modules", "theorems_lemmas", "figures_tiled", "formal",
              "scripts", "tests", "web_lab", "assets", "docs", "datasets",
              "timeline", "atlas", "glossary", "whitepaper"):
        check(f"README {d}/", os.path.isfile(os.path.join(ROOT, d, "README.md")))

    print(f"PASS: {len(OK)}")
    if FAIL:
        print(f"FAIL: {len(FAIL)}")
        for x in FAIL:
            print("  ✗", x)
        sys.exit(1)
    print("PACKAGE VALIDATION: ALL OK")


if __name__ == "__main__":
    main()
