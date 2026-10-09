#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_infographics.py — инфографики проекта (Playwright + CSS).

5 инфографик × 2 языка × 2 темы → figures/{ru,en}/{light,dark}/info_*.png
(масштаб 3× ≈ 600 dpi для A4-landscape). Низкая насыщенность заливок,
один акцент на карточку, same-hue прогрессия фаз — по правилам charts.
Запуск: python3 scripts/make_infographics.py
"""
import asyncio
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = os.path.join(ROOT, "scripts", "_info_html")
OUT = os.path.join(ROOT, "figures")

PALETTE = {
    "light": {"bg": "#FAF7F0", "card": "#FFFFFF", "ink": "#1A1A24",
              "line": "#0E7C86", "copper": "#C96F4A", "slate": "#3E515B",
              "muted": "#6B6455", "grid": "#E3DCCB", "ok": "#3A6B4F",
              "bad": "#8C3A2F", "soft": "#F1EDE2"},
    "dark": {"bg": "#10101A", "card": "#171724", "ink": "#E8E2D0",
             "line": "#4FB3BE", "copper": "#E08B66", "slate": "#8FA8B5",
             "muted": "#8A8574", "grid": "#26263a", "ok": "#7FBF9A",
             "bad": "#D97B6C", "soft": "#1d1d2e"},
}

T = {
"ru": {
 "scorecard_title": "Табель Гильберта–Пойа: пять вопросов, пять вердиктов",
 "scorecard_sub": "Измерено в кампаниях C1–C8 · все величины воспроизводимы",
 "items": [
  ("Г1 · Самосопряжённость", "ДА", "ok",
   "Эрмитов гамильтониан решётки: вещественный спектр на машинной точности (декоя и GUE-контроли)"),
  ("Г2 · Спектральное тождество", "НЕТ", "bad",
   "Разрыв график↔оператор: r_H7 ≤ 0.226 (52 затвора), |r_H7| ≤ 0.043 (35 новых), разрыв ≈9–10 порядков, в тепловой проекции ≈0.5 порядка"),
  ("Г3 · Класс GUE", "ДА", "ok",
   "⟨r⟩ = 0.60 при вихрях Nv≥8; вся расширенная семья 0.498–0.505 на единичной развёртке"),
  ("Г4 · Дирак-динамика", "ДА", "ok",
   "Когерентный пакет, отражение, рассеяние на вихрях; энергия до 1e-15; ζ-облако прозрачнее случайного ×16"),
  ("Г5 · Простые в операторе", "НЕТ", "bad",
   "ψ-лестница: corr = 0.972 у нулей против нулевой зоны затворов; вес Λ(n)/√n верифицирован только для H_ξ (T6)"),
 ],
 "map_title": "Карта моста: от алгебраических тождеств к оператору",
 "map_sub": "Что доказано, что измерено, где проходит граница",
 "stages": [
  ("1 · Алгебра", "Γ-лестница: 3 замыкания · dps=40 · невязки ~1e-39", "Доказано (T1)"),
  ("2 · График", "Z_id = e^{iθ}ζ(½+it) · вещественность 5e-29 · 79 нулей", "Доказано (K2, K3)"),
  ("3 · Счёт", "Аргументный принцип до T=1000 · 649 = 649 · S(T) ≤ 1.8", "Верифицировано (K4, K5)"),
  ("4 · Оператор", "52+35 затворов · GUE-класс · ко-локация Φ_pq ≡ Φ_p+Φ_q (1.4e-14)", "Измерено (C3–C6)"),
  ("5 · След", "Tr e^{−xH_ξ} = (1/π)∫Q sin · |ΔK| ≤ 1.2e-5 · затворы: нулевая зона", "T6 доказана; Г2 — разрыв"),
 ],
 "trace_title": "Следовая формула C4: анатомия Tr e^{−xH_ξ}",
 "trace_sub": "Тождество Адамара → Q(a) → синус-преобразование → вес простых",
 "parts": [
  ("T1 · Γ-часть", "интеграл замкнутой формы на [0, 1.5] — «геометрия» Γ-фактора", "#3E515B"),
  ("T2 · Простая часть", "−ΣΛ(n)/√n·Im[e^{−A(ln n−ix)}/(ln n−ix)] — ВЕС ПРОСТЫХ", "#C96F4A"),
  ("T3 · Гладкая часть", "точные формы Si/Ci: полюс, ψ, константы B=−C₀", "#0E7C86"),
 ],
 "trace_note": "Калибровка тождества: |ΔQ| ≤ 1.7e-12 · следовая формула H_ξ: |ΔK| ≤ 1.2e-5 · PC0 r = +0.9998",
 "handles_title": "Расширенное семейство C5: шесть новых ручек",
 "handles_sub": "35 затворов + 2 декуя · вопрос: выведет ли хоть одна ручка из нулевой зоны? Ответ: нет",
 "handles": [
  ("Твисты (φx, φy)", "3 класса спин-структур", "|r_H7| ≤ 0.033"),
  ("Анизотропия t_x/t_y", "0.8 и 1.25", "|r_H7| ≤ 0.030"),
  ("Флакс-сдвиг δα", "±0.02 (±1/24 на торусе)", "|r_H7| ≤ 0.034"),
  ("Стэггерд-масса m", "0.15 и 0.35", "|r_H7| ≤ 0.032"),
  ("Профиль вихря", "site | midpoint", "|r_H7| ≤ 0.033"),
  ("Знаки и границы", "neutral | all_plus | random · open | torus", "|r_H7| ≤ 0.044"),
 ],
 "ladder_title": "Статистическая лестница C8: симметрия задаёт класс",
 "ladder_sub": "Тройственность Дайсона на решётке · GSE структурно недостижима (T²=+1)",
 "ladder": [
  ("Пуассон", "⟨r⟩ = 0.386", "чистая решётка · андерсоновская локализация"),
  ("GOE", "⟨r⟩ = 0.531", "вещественный беспорядок w = 1–4"),
  ("GUE", "⟨r⟩ = 0.602", "комплексные вихревые фазы Nv ≥ 8"),
  ("spinor64", "64 → 4", "спин-структуры квартики Кляйна: 4 гамильтониана"),
 ],
},
"en": {
 "scorecard_title": "Hilbert–Pólya scorecard: five questions, five verdicts",
 "scorecard_sub": "Measured in campaigns C1–C8 · every number reproducible",
 "items": [
  ("H1 · Self-adjointness", "YES", "ok",
   "Hermitian lattice Hamiltonian: real spectrum at machine precision (decoy and GUE controls)"),
  ("H2 · Spectral identity", "NO", "bad",
   "Graph↔operator gap: r_H7 ≤ 0.226 (52 gates), |r_H7| ≤ 0.043 (35 new), gap ≈9–10 orders, ≈0.5 order in the trace projection"),
  ("H3 · GUE class", "YES", "ok",
   "⟨r⟩ = 0.60 with vortices Nv≥8; the whole extended family 0.498–0.505 on the unit unfolding"),
  ("H4 · Dirac dynamics", "YES", "ok",
   "Coherent packet, reflection, vortex scattering; energy to 1e-15; ζ-cloud 16× more transparent than random"),
  ("H5 · Primes in the operator", "NO", "bad",
   "ψ-ladder: corr = 0.972 for zeros vs null zone of gates; the Λ(n)/√n weight verified only for H_ξ (T6)"),
 ],
 "map_title": "Bridge map: from algebraic identities to the operator",
 "map_sub": "What is proven, what is measured, where the boundary runs",
 "stages": [
  ("1 · Algebra", "Γ-ladder: 3 closures · dps=40 · residuals ~1e-39", "Proven (T1)"),
  ("2 · Graph", "Z_id = e^{iθ}ζ(½+it) · reality 5e-29 · 79 zeros", "Proven (K2, K3)"),
  ("3 · Counting", "Argument principle to T=1000 · 649 = 649 · S(T) ≤ 1.8", "Verified (K4, K5)"),
  ("4 · Operator", "52+35 gates · GUE class · co-location Φ_pq ≡ Φ_p+Φ_q (1.4e-14)", "Measured (C3–C6)"),
  ("5 · Trace", "Tr e^{−xH_ξ} = (1/π)∫Q sin · |ΔK| ≤ 1.2e-5 · gates: null zone", "T6 proven; H2 — gap"),
 ],
 "trace_title": "C4 trace formula: anatomy of Tr e^{−xH_ξ}",
 "trace_sub": "Hadamard product → Q(a) → sine transform → the weight of primes",
 "parts": [
  ("T1 · Γ-part", "integral of the closed form on [0, 1.5] — Γ-factor geometry", "#3E515B"),
  ("T2 · Prime part", "−ΣΛ(n)/√n·Im[e^{−A(ln n−ix)}/(ln n−ix)] — THE WEIGHT OF PRIMES", "#C96F4A"),
  ("T3 · Smooth part", "exact Si/Ci forms: pole, ψ, constants B=−C₀", "#0E7C86"),
 ],
 "trace_note": "Identity calibration: |ΔQ| ≤ 1.7e-12 · trace formula for H_ξ: |ΔK| ≤ 1.2e-5 · PC0 r = +0.9998",
 "handles_title": "C5 extended family: six new handles",
 "handles_sub": "35 gates + 2 decoys · question: does any handle exit the null zone? Answer: no",
 "handles": [
  ("Twists (φx, φy)", "3 spin-structure classes", "|r_H7| ≤ 0.033"),
  ("Anisotropy t_x/t_y", "0.8 and 1.25", "|r_H7| ≤ 0.030"),
  ("Flux shift δα", "±0.02 (±1/24 on the torus)", "|r_H7| ≤ 0.034"),
  ("Staggered mass m", "0.15 and 0.35", "|r_H7| ≤ 0.032"),
  ("Vortex profile", "site | midpoint", "|r_H7| ≤ 0.033"),
  ("Signs and boundaries", "neutral | all_plus | random · open | torus", "|r_H7| ≤ 0.044"),
 ],
 "ladder_title": "C8 statistics ladder: symmetry sets the class",
 "ladder_sub": "Dyson triplet on the lattice · GSE structurally unreachable (T²=+1)",
 "ladder": [
  ("Poisson", "⟨r⟩ = 0.386", "clean lattice · Anderson localization"),
  ("GOE", "⟨r⟩ = 0.531", "real disorder w = 1–4"),
  ("GUE", "⟨r⟩ = 0.602", "complex vortex phases Nv ≥ 8"),
  ("spinor64", "64 → 4", "Klein quartic spin structures: 4 Hamiltonians"),
 ],
},
}


def css(tok):
    return f"""
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ background:{tok['bg']}; font-family:'DejaVu Sans','Noto Sans',sans-serif; }}
    #root {{ width:1560px; padding:36px; background:{tok['bg']}; color:{tok['ink']}; }}
    .hd {{ margin-bottom:8px; }}
    .hd h1 {{ font-size:30px; font-weight:800; letter-spacing:-0.5px; }}
    .hd p {{ font-size:15px; color:{tok['muted']}; margin-top:6px; }}
    .rule {{ height:3px; background:{tok['line']}; width:72px; margin:14px 0 22px; border-radius:2px; }}
    .grid {{ display:grid; gap:16px; }}
    .card {{ background:{tok['card']}; border:1px solid {tok['grid']};
             border-radius:12px; padding:18px 20px; }}
    .row {{ display:flex; align-items:center; gap:16px; }}
    .verdict {{ font-size:26px; font-weight:900; padding:2px 16px;
                border-radius:10px; }}
    .ok  {{ color:{tok['ok']}; background:color-mix(in srgb,{tok['ok']} 12%, transparent); }}
    .bad {{ color:{tok['bad']}; background:color-mix(in srgb,{tok['bad']} 12%, transparent); }}
    .t   {{ font-size:17px; font-weight:700; }}
    .d   {{ font-size:13.5px; color:{tok['muted']}; margin-top:6px; line-height:1.5; }}
    .stage {{ display:flex; gap:14px; align-items:stretch; margin-bottom:12px; }}
    .num  {{ min-width:52px; display:flex; align-items:center; justify-content:center;
             font-size:20px; font-weight:900; color:{tok['line']}; }}
    .stage .card {{ flex:1; }}
    .chip {{ display:inline-block; font-size:12px; font-weight:700;
             padding:3px 10px; border-radius:99px; margin-left:10px;
             color:{tok['line']}; background:color-mix(in srgb,{tok['line']} 10%, transparent); }}
    .bar {{ height:10px; border-radius:5px; margin-top:10px; }}
    .foot {{ margin-top:22px; font-size:13px; color:{tok['muted']};
             border-top:1px solid {tok['grid']}; padding-top:12px; }}
    .mono {{ font-family:'DejaVu Sans Mono',monospace; font-size:13px; }}
    """


def html_scorecard(L, tok):
    cards = "".join(
        f'<div class="card"><div class="row"><div class="t" style="flex:1">{t}</div>'
        f'<div class="verdict {cls}">{v}</div></div><div class="d">{d}</div></div>'
        for t, v, cls, d in L["items"])
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css(tok)}</style></head>
<body><div id="root"><div class="hd"><h1>{L["scorecard_title"]}</h1><p>{L["scorecard_sub"]}</p></div>
<div class="rule"></div><div class="grid">{cards}</div>
<div class="foot">Hilbert Polya Bridge v1.0.0 · data/c*_verdict.json · independent_verification/IVP*</div></div></body></html>'''


def html_map(L, tok):
    stages = ""
    for i, (t, d, chip) in enumerate(L["stages"]):
        stages += (f'<div class="stage"><div class="num">{i+1}</div>'
                   f'<div class="card"><div class="t">{t}'
                   f'<span class="chip">{chip}</span></div>'
                   f'<div class="d mono">{d}</div></div></div>')
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css(tok)}</style></head>
<body><div id="root"><div class="hd"><h1>{L["map_title"]}</h1><p>{L["map_sub"]}</p></div>
<div class="rule"></div>{stages}
<div class="foot">T = theorem · K = criterion · Г/Н = Hilbert–Pólya scorecard item · C = campaign</div></div></body></html>'''


def html_trace(L, tok):
    parts = "".join(
        f'<div class="card"><div class="t" style="color:{col}">{t}</div>'
        f'<div class="d mono">{d}</div></div>'
        for t, d, col in L["parts"])
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css(tok)}</style></head>
<body><div id="root"><div class="hd"><h1>{L["trace_title"]}</h1><p>{L["trace_sub"]}</p></div>
<div class="rule"></div>
<div class="card mono" style="font-size:17px; margin-bottom:16px">
K(x) := Tr e<sup>−xH<sub>ξ</sub></sup> = Σ<sub>γ&gt;0</sub> e<sup>−xγ</sup>
&nbsp;=&nbsp; (1/π) ∫₀<sup>∞</sup> Q(a)·sin(ax) da</div>
<div class="grid" style="grid-template-columns:1fr 1fr 1fr">{parts}</div>
<div class="foot mono">{L["trace_note"]}</div></div></body></html>'''


def html_handles(L, tok):
    rows = "".join(
        f'<div class="card"><div class="row"><div class="t" style="flex:1">{t}</div>'
        f'<div class="mono" style="color:{tok["copper"]}; font-weight:700">{m}</div></div>'
        f'<div class="d">{d}</div></div>'
        for t, d, m in L["handles"])
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css(tok)}</style></head>
<body><div id="root"><div class="hd"><h1>{L["handles_title"]}</h1><p>{L["handles_sub"]}</p></div>
<div class="rule"></div><div class="grid" style="grid-template-columns:1fr 1fr">{rows}</div>
<div class="foot">data/c5_gates_ext_verdict.json · ⟨r⟩ = 0.500 ± 0.002 everywhere (GUE class) · |r_H7| max = 0.043</div></div></body></html>'''


def html_ladder(L, tok):
    cards = "".join(
        f'<div class="card"><div class="t">{t}</div>'
        f'<div class="mono" style="font-size:22px; color:{tok["line"]}; '
        f'font-weight:800; margin:8px 0">{v}</div>'
        f'<div class="d">{d}</div></div>'
        for t, v, d in L["ladder"])
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css(tok)}</style></head>
<body><div id="root"><div class="hd"><h1>{L["ladder_title"]}</h1><p>{L["ladder_sub"]}</p></div>
<div class="rule"></div><div class="grid" style="grid-template-columns:1fr 1fr 1fr 1fr">{cards}</div>
<div class="foot">data/computations/C8 · spinor64: isospectrality |Δλ| ≤ 1.1e-14 · orbits 28/21/7/7/1 (Arf 28/36)</div></div></body></html>'''


BUILDERS = [("info_scorecard", html_scorecard), ("info_map", html_map),
            ("info_trace", html_trace), ("info_handles", html_handles),
            ("info_ladder", html_ladder)]


async def render_all():
    from playwright.async_api import async_playwright
    os.makedirs(TMP, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1700, "height": 900},
                                      device_scale_factor=3)
        for name, builder in BUILDERS:
            for lang in ("ru", "en"):
                for theme in ("light", "dark"):
                    tok = PALETTE[theme]
                    html = builder(T[lang], tok)
                    path = os.path.join(TMP, f"{name}_{lang}_{theme}.html")
                    open(path, "w").write(html)
                    await page.goto(f"file://{path}")
                    await page.wait_for_timeout(120)
                    outd = os.path.join(OUT, lang, theme)
                    os.makedirs(outd, exist_ok=True)
                    el = page.locator("#root")
                    box = await el.bounding_box()
                    await page.set_viewport_size({"width": 1700,
                                                  "height": int(box["height"]) + 20})
                    await page.wait_for_timeout(60)
                    await el.screenshot(path=os.path.join(
                        outd, f"{name}_{lang}.png"))
        await browser.close()


if __name__ == "__main__":
    asyncio.run(render_all())
    n = sum(len(f) for _, _, f in os.walk(OUT) if "info_" in str(f))
    total = 0
    for root, _, files in os.walk(OUT):
        total += sum(1 for f in files if f.startswith("info_"))
    print(f"infographics done: {total} files")
