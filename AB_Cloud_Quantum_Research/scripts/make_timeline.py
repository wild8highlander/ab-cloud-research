#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_timeline.py — хронологическая карта кампаний программы.

Одна фигура (600 dpi, RU/EN) из ЗАКОММИЧЕННОГО
datasets/campaign_timeline.csv: 43 кампании четырёх уровней исследования
(ядро V01–V19 · процессор V20 · верификация E01–E18 · спинор ES1–ES5)
на единой временной ленте с маркерами статуса.
Выход: timeline/campaign_timeline_{lang}.png."""
import csv
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm

for _f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
    if os.path.exists(_f):
        fm.fontManager.addfont(_f)
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "timeline")
os.makedirs(OUT, exist_ok=True)

T = dict(bg="#FAF7F0", panel="#FFFFFF", ink="#1A1A24", line="#0E7C86",
         copper="#C96F4A", slate="#3E515B", muted="#6B6455",
         grid="#DDD6C8", ok="#3A6B4F", bad="#8C3A2F", gold="#8C6D1F")

MODCOL = {"core_spectrum": T["line"],
          "processor_ab": T["copper"],
          "verifier_multilang": T["slate"],
          "realtime_spinor_memory": T["gold"]}

L = {
    "ru": dict(t="Хронология кампаний AB Cloud Quantum Research — 43 кампании",
               lanes={"core_spectrum": "Ядро V01–V19",
                      "processor_ab": "Процессор V20",
                      "verifier_multilang": "Верификация E01–E18",
                      "realtime_spinor_memory": "Спинор ES1–ES5"},
               cap=("Источник: datasets/campaign_timeline.csv — статусы из "
                    "закоммиченных вердиктов. Предрегистрированные пороги, "
                    "слепые протоколы, публикация отрицательных результатов."),
               x="порядковый номер кампании"),
    "en": dict(t="AB Cloud Quantum Research campaign timeline — 43 campaigns",
               lanes={"core_spectrum": "Core V01–V19",
                      "processor_ab": "Processor V20",
                      "verifier_multilang": "Verification E01–E18",
                      "realtime_spinor_memory": "Spinor ES1–ES5"},
               cap=("Source: datasets/campaign_timeline.csv — statuses from "
                    "committed verdicts. Pre-registered thresholds, blind "
                    "protocols, published negative results."),
               x="campaign ordinal"),
}


def fig(lang):
    P = L[lang]
    rows = list(csv.DictReader(open(os.path.join(ROOT, "datasets",
                                                 "campaign_timeline.csv"),
                                    encoding="utf-8")))
    lanes = ["core_spectrum", "processor_ab", "verifier_multilang",
             "realtime_spinor_memory"]
    fig, ax = plt.subplots(figsize=(13, 5.6), dpi=100,
                           constrained_layout=True)
    fig.patch.set_facecolor(T["bg"])
    ax.set_facecolor(T["panel"])

    counters = {m: 0 for m in lanes}
    maxn = 0
    for r in rows:
        m = r["module"]
        counters[m] += 1
        x = counters[m]
        maxn = max(maxn, x)
        y = lanes.index(m)
        passed = "PASS" in r["status"] or r["status"] == "исполнена"
        ax.scatter([x], [y], s=210 if x % 5 == 0 or x == 1 else 110,
                   color=MODCOL[m] if passed else T["bad"],
                   edgecolors=T["ink"], linewidths=0.6, zorder=3)
        ax.text(x, y + 0.30, r["campaign"], ha="center", va="bottom",
                fontsize=7, color=T["ink"], rotation=0, zorder=4)

    for y, m in enumerate(lanes):
        ax.axhline(y, color=T["grid"], lw=1.0, zorder=1)
        ax.text(-0.7, y, P["lanes"][m], ha="right", va="center",
                fontsize=9.5, color=MODCOL[m], fontweight="bold")

    ax.set_xlim(-14, maxn + 1.5)
    ax.set_ylim(-0.7, 3.7)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlabel(P["x"], fontsize=9, color=T["muted"])
    for s in ax.spines.values():
        s.set_visible(False)

    fig.suptitle(P["t"], fontsize=13.5, fontweight="bold", color=T["ink"])
    fig.supxlabel(P["cap"], fontsize=8.6, color=T["muted"], style="italic")
    out = os.path.join(OUT, f"campaign_timeline_{lang}.png")
    fig.savefig(out, dpi=600, facecolor=T["bg"])
    plt.close(fig)
    print("OK:", out, f"({os.path.getsize(out) // 1024} KB)")


if __name__ == "__main__":
    for lang in ("ru", "en"):
        fig(lang)
