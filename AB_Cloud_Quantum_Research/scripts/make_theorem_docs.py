#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_theorem_docs.py — папка theorems_lemmas единого пакета:
для каждой теоремы Th1–Th6 собирается монография (все секции с префиксом
ThK из тома теорем материнской серии), в раздел «Результаты» внедряется
плиточная фигура 4-измерений, документ рендерится в RU/EN × PDF/DOCX.

Выход: theorems_lemmas/T0K_*/theorem_thK_{lang}.{pdf,docx} (12 файлов).
Рендереры и контент переиспользуются из modules/core_spectrum (без
дублирования исходников)."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CORE = os.path.join(ROOT, "modules", "core_spectrum")
sys.path.insert(0, CORE)
sys.path.insert(0, os.path.join(CORE, "monograph"))
sys.path.insert(0, os.path.join(CORE, "monograph", "content"))

from content import ru_part1, ru_part2, ru_part3, ru_part4, ru_part5, \
    ru_part6  # noqa: E402
from content import en_part1, en_part2, en_part3, en_part4, en_part5, \
    en_part6  # noqa: E402

DOCS = {
    "ru": {**ru_part1.DOCS, **ru_part2.DOCS, **ru_part3.DOCS,
           **ru_part4.DOCS, **ru_part5.DOCS, **ru_part6.DOCS},
    "en": {**en_part1.DOCS, **en_part2.DOCS, **en_part3.DOCS,
           **en_part4.DOCS, **en_part5.DOCS, **en_part6.DOCS},
}

THM_DIRS = [
    ("Th1", "T01_hermiticity", "th1"),
    ("Th2", "T02_self_adjointness", "th2"),
    ("Th3", "T03_certificates", "th3"),
    ("Th4", "T04_li_spectral", "th4"),
    ("Th5", "T05_block_reduction", "th5"),
    ("Th6", "T06_trace_formula", "th6"),
]

NAME = {"Th1": "Эрмитовость", "Th2": "Самосопряжённость",
        "Th3": "Сертификаты", "Th4": "Формула Ли",
        "Th5": "Блочная редукция", "Th6": "Следовая формула"}
NAME_EN = {"Th1": "Hermiticity", "Th2": "Self-adjointness",
           "Th3": "Certificates", "Th4": "The Li formula",
           "Th5": "Block reduction", "Th6": "The trace formula"}

CAPTION = {
    "ru": ("Рис. 1. Теорема {k}: четыре измерения измерений — метрика, "
           "её поведение по затворам/инстансам, контроль и порог "
           "(плитка 2×2, 600 dpi, данные вердикта кампании)."),
    "en": ("Fig. 1. Theorem {k}: four measurement dimensions — the metric, "
           "its behaviour across gates/instances, the control and the "
           "threshold (2×2 tile, 600 dpi, campaign verdict data)."),
}


def thm_doc(base, thm_key, lang):
    """Все секции тома теорем с префиксом ключа (постановка + сертификат)."""
    secs = [s for s in base["sections"] if s["h1"].startswith(thm_key)]
    meta = dict(base["meta"])
    nm = NAME[thm_key] if lang == "ru" else NAME_EN[thm_key]
    meta["title"] = f"{thm_key}. {nm}"
    meta["volume"] = thm_key
    return {"meta": meta, "sections": secs}


def inject_figure(doc, rel_fig_path, lang, thm_key):
    fig = {"path": rel_fig_path,
           "caption": CAPTION[lang].format(k=thm_key)}
    for sec in doc["sections"]:
        h1 = sec["h1"]
        if h1.startswith(("Сертификат", "Certificate")) or \
           h1.startswith((f"{thm_key}.1", f"{thm_key}.2")):
            sec.setdefault("figure", fig)
            return doc
    doc["sections"][-1]["figure"] = fig
    return doc


def main():
    only = sys.argv[1:] or None
    tmp = os.path.join(ROOT, "theorems_lemmas", "_json")
    os.makedirs(tmp, exist_ok=True)
    n_docs = 0
    for lang in ("ru", "en"):
        base = DOCS[lang]["theorems"]
        for thm_key, dirname, figstem in THM_DIRS:
            if only and thm_key not in only and dirname not in only:
                continue
            d = thm_doc(base, thm_key, lang)
            rel_fig = os.path.join(
                "..", "..", "theorems_lemmas", dirname, "figures",
                f"{figstem}_4dim_" + "{lang}.png")
            d = inject_figure(d, rel_fig, lang, thm_key)
            jp = os.path.join(tmp, f"{thm_key}_{lang}.json")
            with open(jp, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, indent=1)
            out_dir = os.path.join(ROOT, "theorems_lemmas", dirname)
            os.makedirs(out_dir, exist_ok=True)
            out_pdf = os.path.join(out_dir, f"theorem_{thm_key.lower()}_{lang}.pdf")
            out_docx = os.path.join(out_dir,
                                    f"theorem_{thm_key.lower()}_{lang}.docx")
            print(f"--- {thm_key} [{lang}]")
            subprocess.run([sys.executable,
                            os.path.join(CORE, "scripts", "render_pdf.py"),
                            jp, out_pdf, lang], check=True)
            subprocess.run([sys.executable,
                            os.path.join(CORE, "scripts", "render_docx.py"),
                            jp, out_docx, lang], check=True)
            n_docs += 1
    print(f"THEOREM DOCS DONE: {n_docs} (12 = 6 теорем × RU/EN × PDF/DOCX)")


if __name__ == "__main__":
    main()
