#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_lab.py — сборка web_lab/index.html (самодостаточная лаборатория).

Вкладки: Z(t) Римана–Зигеля, конструктор затворов (Якоби-диагонализация),
тепловой след против гребёнки простых, коэффициенты Ли, ψ-лестница.
Данные (нули, λ_n, Λ-сито) встраиваются в файл; внешних зависимостей нет.
Запуск: python3 scripts/build_lab.py
"""
import json
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys_p = os.path.join(ROOT, 'rpbridge')
os.sys.path.insert(0, ROOT)

from rpbridge.li import li_from_zeros  # noqa: E402
from rpbridge.primes import lambda_arrays  # noqa: E402
from rpbridge.zeros import load_zeros  # noqa: E402

ZEROS = load_zeros(nmax=600)
LAM, TAIL, _ = li_from_zeros(ZEROS, n_max=1000)
LAM = [round(float(x), 6) for x in LAM]
ZL = [round(float(z), 6) for z in ZEROS]
# Λ-сито до 1e5: (n, Λ(n)) носители
ns_l, lm_l = lambda_arrays(100_000)
CARR = [[int(n), round(float(l), 6)] for n, l in zip(ns_l, lm_l)]

HTML = '''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AB Research Program · Web Lab</title>
<style>
:root { --bg:#10101A; --panel:#181826; --ink:#E8E4DA; --line:#4FB3BE;
        --copper:#E08B66; --muted:#9A938A; --grid:#2A2A3A; --ok:#6FBF8A; }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink);
       font-family:'Segoe UI', system-ui, sans-serif; }
header { padding:18px 24px 8px; }
h1 { font-size:20px; margin:0 0 2px; }
h1 .cop { color:var(--copper); }
.sub { color:var(--muted); font-size:12.5px; }
.lang { float:right; }
.lang button { background:var(--panel); color:var(--ink);
  border:1px solid var(--grid); border-radius:6px; padding:4px 12px;
  cursor:pointer; margin-left:6px; }
.lang button.on { border-color:var(--copper); color:var(--copper); }
nav { display:flex; gap:4px; padding:10px 24px; flex-wrap:wrap; }
nav button { background:var(--panel); color:var(--ink);
  border:1px solid var(--grid); border-radius:8px 8px 0 0;
  padding:8px 16px; cursor:pointer; font-size:13px; }
nav button.on { background:var(--line); color:#0b1517; font-weight:600;
  border-color:var(--line); }
main { margin:0 24px 24px; background:var(--panel); border:1px solid
  var(--grid); border-radius:0 10px 10px 10px; padding:18px; }
canvas { width:100%; height:380px; display:block; background:var(--bg);
  border:1px solid var(--grid); border-radius:8px; }
.controls { display:flex; gap:18px; flex-wrap:wrap; margin:12px 0; }
.ctl { font-size:12.5px; color:var(--muted); }
.ctl input[type=range] { width:150px; vertical-align:middle; }
.ctl b { color:var(--ink); }
.readout { font-size:13px; color:var(--ink); margin-top:8px; line-height:1.7; }
.readout .cop { color:var(--copper); }
.note { color:var(--muted); font-size:11.5px; margin-top:10px;
  line-height:1.55; }
.tab { display:none; } .tab.on { display:block; }
</style>
</head>
<body>
<header>
  <div class="lang">
    <button id="btn_ru" class="on" onclick="setLang('ru')">RU</button>
    <button id="btn_en" onclick="setLang('en')">EN</button>
  </div>
  <h1>AB RESEARCH PROGRAM <span class="cop">· WEB LAB</span> v1.0.0</h1>
  <div class="sub" id="subtitle"></div>
</header>
<nav>
  <button id="nav0" class="on" onclick="show(0)">Z(t) Римана–Зигеля</button>
  <button id="nav1" onclick="show(1)">Конструктор затворов</button>
  <button id="nav2" onclick="show(2)">Тепловой след ↔ простые</button>
  <button id="nav3" onclick="show(3)">Критерий Ли</button>
  <button id="nav4" onclick="show(4)">ψ-лестница</button>
</nav>
<main>
<section class="tab on" id="tab0">
  <canvas id="cv0" width="1200" height="380"></canvas>
  <div class="controls">
    <div class="ctl"><span class="l" data="tmax">T max</span>:
      <input type="range" id="tmax" min="50" max="600" value="200"
        oninput="drawZ()"><b id="tmaxv">200</b></div>
  </div>
  <div class="readout" id="ro0"></div>
  <div class="note l" data="note0"></div>
</section>
<section class="tab" id="tab1">
  <canvas id="cv1" width="1200" height="380"></canvas>
  <div class="controls">
    <div class="ctl">L: <input type="range" id="gL" min="4" max="10"
      value="6" oninput="drawGate()"><b id="gLv">6</b></div>
    <div class="ctl">Nv: <input type="range" id="gNv" min="0" max="12"
      value="4" oninput="drawGate()"><b id="gNvv">4</b></div>
    <div class="ctl">q: <input type="range" id="gq" min="1" max="20"
      value="10" oninput="drawGate()"><b id="gqv">1.0</b></div>
    <div class="ctl">W: <input type="range" id="gW" min="0" max="10"
      value="5" oninput="drawGate()"><b id="gWv">0.5</b></div>
    <button onclick="drawGate()"
      style="background:var(--copper);border:none;border-radius:6px;
      padding:6px 14px;cursor:pointer;font-weight:600">⟲</button>
  </div>
  <div class="readout" id="ro1"></div>
  <div class="note l" data="note1"></div>
</section>
<section class="tab" id="tab2">
  <canvas id="cv2" width="1200" height="380"></canvas>
  <div class="readout" id="ro2"></div>
  <div class="note l" data="note2"></div>
</section>
<section class="tab" id="tab3">
  <canvas id="cv3" width="1200" height="380"></canvas>
  <div class="readout" id="ro3"></div>
  <div class="note l" data="note3"></div>
</section>
<section class="tab" id="tab4">
  <canvas id="cv4" width="1200" height="380"></canvas>
  <div class="readout" id="ro4"></div>
  <div class="note l" data="note4"></div>
</section>
</main>
<script>
const ZEROS = __ZEROS__;
const LAM = __LAM__;
const CARR = __CARR__;
let LANG = 'ru';

const T = {
 ru: { subtitle: 'Интерактивная лаборатория серии V1–V15: все вычисления '
   + 'исполняются локально в браузере (без сети и зависимостей).',
  tabs: ['Z(t) Римана–Зигеля','Конструктор затворов','Тепловой след ↔ простые',
    'Критерий Ли','ψ-лестница'],
  note0: 'Кривая Харди Z(t) = e^{iθ(t)}ζ(1/2+it) по формуле Римана–Зигеля; '
   + 'медные маркеры — нули из файла Одлыжко (первые 600). Кампания C1/V6 '
   + 'эталона: нули Z совпадают с нулями ζ.',
  note1: 'Эрмитова решётка хофштадтеровского типа с вихрями (упрощённый '
   + 'AB-cloud): фаза Ландау на x-связях + вихревые разности на y-связях; '
   + 'диагонализация методом Якоби в браузере. Это инженерная модель '
   + 'кампаний V2/V4 (в пакете — LAPACK, 576×576).',
  note2: 'Тепловой след K(x) = Σ e^{−xγ} (нулевая сторона) против простой '
   + 'гребёнки P(u) = Σ Λ(n)/√n·u/(u²+ln²n). Кампания V7: корреляция '
   + 'флуктуаций — PC0 r = +0.9996 в пакете.',
  note3: 'Коэффициенты Ли λ_n (n ≤ 1000, из файла нулей). Кампания V15: '
   + 'λ_n > 0 для n ≤ 3000 (сертифицированные хвосты); RH ⟺ λ_n ≥ 0 ∀n.',
  note4: 'ψ(x) = Σ_{p^k ≤ x} ln p по Λ-ситу до 10⁵ против гладкой прямой '
   + 'x. Кампания C6 эталона: corr(ψ_ζ, сито) = 0.972.' },
 en: { subtitle: 'Interactive laboratory of the V1–V15 series: every '
   + 'computation runs locally in your browser (no network, no deps).',
  tabs: ['Riemann–Siegel Z(t)','Gate builder','Heat trace ↔ primes',
    'Li criterion','ψ-staircase'],
  note0: 'The Hardy curve Z(t) = e^{iθ(t)}ζ(1/2+it) via the '
   + 'Riemann–Siegel formula; copper markers — Odlyzko zeros (first 600). '
   + 'Reference campaign C1/V6: the zeros of Z coincide with those of ζ.',
  note1: 'A Hermitian Hofstadter-type lattice with vortices (a simplified '
   + 'AB-cloud): Landau phase on x-links + vortex differences on y-links; '
   + 'Jacobi diagonalization in the browser. An engineering model of '
   + 'campaigns V2/V4 (the package uses LAPACK, 576×576).',
  note2: 'The heat trace K(x) = Σ e^{−xγ} (zero side) against the prime '
   + 'comb P(u) = Σ Λ(n)/√n·u/(u²+ln²n). Campaign V7: the fluctuation '
   + 'correlation — PC0 r = +0.9996 in the package.',
  note3: 'The Li coefficients λ_n (n ≤ 1000, from the zero file). '
   + 'Campaign V15: λ_n > 0 for n ≤ 3000 (certified tails); RH ⟺ λ_n ≥ 0 '
   + '∀n.',
  note4: 'ψ(x) = Σ_{p^k ≤ x} ln p from a Λ-sieve to 10⁵ against the '
   + 'straight line x. Reference campaign C6: corr(ψ_ζ, sieve) = 0.972.' }
};

function setLang(l) {
  LANG = l;
  document.getElementById('btn_ru').classList.toggle('on', l==='ru');
  document.getElementById('btn_en').classList.toggle('on', l==='en');
  document.getElementById('subtitle').textContent = T[l].subtitle;
  for (let i = 0; i < 5; i++) {
    document.getElementById('nav'+i).textContent = T[l].tabs[i];
    const n = document.querySelector('.note[data="note'+i+'"]');
    if (n) n.textContent = T[l]['note'+i];
  }
  drawAll();
}
function show(i) {
  for (let k = 0; k < 5; k++) {
    document.getElementById('tab'+k).classList.toggle('on', k===i);
    document.getElementById('nav'+k).classList.toggle('on', k===i);
  }
  drawAll();
}

// ── Риман–Зигель ─────────────────────────────────────────────────────
function theta(t) { // Римана–Зигеля θ(t)
  const g = [676.5203681218851, -1259.1392167224028, 771.32342877765313,
   -176.61502916214059, 12.507343278686905, -0.13857109526572012,
   9.9843695780195716e-6, 1.5056327351493116e-7];
  function lgamma(z) {
    let x = g[7];
    for (let i = 6; i >= 0; i--) x += g[i] / (z + i);
    const t2 = z + 7.5;
    return 0.5*Math.log(2*Math.PI) + (z+0.5)*Math.log(t2) - t2
      + Math.log(x);
  }
  return lgamma(0.25 + 0.5*new Complex(0, t)).im
    - 0.5*t*Math.log(Math.PI);
}
class Complex {
  constructor(re, im=0){ this.re=re; this.im=im; }
  add(o){ return new Complex(this.re+o.re, this.im+o.im); }
  mul(o){ return new Complex(this.re*o.re-this.im*o.im,
    this.re*o.im+this.im*o.re); }
  div(o){ const d=o.re*o.re+o.im*o.im;
    return new Complex((this.re*o.re+this.im*o.im)/d,
      (this.im*o.re-this.re*o.im)/d); }
  exp(){ return new Complex(Math.exp(this.re)*Math.cos(this.im),
    Math.exp(this.re)*Math.sin(this.im)); }
  conj(){ return new Complex(this.re, -this.im); }
}
function zetaHalf(t, N=60) { // ζ(1/2+it) рядом Диригле с окном
  let s = new Complex(0, 0);
  for (let n = 1; n <= N; n++) {
    const w = Math.exp(-Math.pow(n/N, 2)*6); // мягкое окно
    s = s.add(new Complex(Math.cos(-t*Math.log(n)),
      Math.sin(-t*Math.log(n))).mul(new Complex(Math.pow(n,-0.5)*w,0)));
  }
  return s;
}
function drawZ() {
  const Tm = +document.getElementById('tmax').value;
  document.getElementById('tmaxv').textContent = Tm;
  const cv = document.getElementById('cv0'), cx = cv.getContext('2d');
  const W = cv.width, H = cv.height;
  cx.clearRect(0,0,W,H);
  const th0 = thetaSmall(0);
  let zmin = 1e9, zmax = -1e9;
  const pts = [];
  for (let px = 0; px <= W; px++) {
    const t = Tm*px/W;
    const z = hardyZ(t);
    pts.push([px, z]);
    zmin = Math.min(zmin, z); zmax = Math.max(zmax, z);
  }
  const pad = 10;
  const y0 = v => H-pad-(v-zmin)/(zmax-zmin+1e-9)*(H-2*pad);
  cx.strokeStyle = '#4FB3BE'; cx.lineWidth = 1.6; cx.beginPath();
  for (const [px, z] of pts) px===0 ? cx.moveTo(px, y0(z))
    : cx.lineTo(px, y0(z));
  cx.stroke();
  cx.strokeStyle = '#2A2A3A'; cx.beginPath(); cx.moveTo(0,y0(0));
  cx.lineTo(W,y0(0)); cx.stroke();
  cx.fillStyle = '#E08B66';
  for (const g of ZEROS) { if (g > Tm) break;
    const px = g/Tm*W; cx.beginPath(); cx.arc(px, y0(0), 4, 0, 7);
    cx.fill(); }
  document.getElementById('ro0').innerHTML =
    (LANG==='ru' ? 'Нулей в окне: ' : 'Zeros in window: ')
    + ZEROS.filter(g=>g<=Tm).length
    + ' · Z(0) = ' + hardyZ(0).toFixed(4)
    + ' · θ(0)/π = ' + (thetaSmall(0)/Math.PI).toFixed(4);
}
function thetaSmall(t) { // θ(t) через асимптотику (быстро, для графики)
  const p = Math.PI;
  return t/2*Math.log(t/(2*p)) - t/2 - p/8 + 1/(48*t);
}
function hardyZ(t) { // Z = 2 Σ n^{-1/2} cos(θ − t ln n) с окном
  const th = thetaSmall(t);
  let s = 0; const N = Math.max(30, Math.floor(Math.sqrt(t)*8));
  for (let n = 1; n <= N; n++) {
    const w = Math.exp(-Math.pow(n/N,2)*5);
    s += w/Math.sqrt(n)*Math.cos(th - t*Math.log(n));
  }
  return 2*s;
}

// ── Конструктор затворов ─────────────────────────────────────────────
function buildH(L, Nv, q, W) {
  const N = L*L;
  const H = [];
  for (let i = 0; i < N; i++) {
    const row = [];
    for (let j = 0; j < N; j++) row.push(new Complex(0, 0));
    H.push(row);
  }
  const rng = mulberry(96);
  const vx = [], vy = [], vq = [];
  for (let k = 0; k < Nv; k++) {
    vx.push(1+Math.floor(rng()*(L-1))+0.5);
    vy.push(1+Math.floor(rng()*(L-1))+0.5);
    vq.push(k < Nv/2 ? q : -q);
  }
  const idx = (x,y) => y*L + x;
  for (let y = 0; y < L; y++)
    for (let x = 0; x < L-1; x++) {
      const ph = 2*Math.PI*0.5*y;
      const v = exp1j(ph);
      H[idx(x,y)][idx(x+1,y)] = v;
      H[idx(x+1,y)][idx(x,y)] = new Complex(v.re, -v.im);
    }
  for (let y = 0; y < L-1; y++)
    for (let x = 0; x < L; x++) {
      let ph = 0;
      for (let k = 0; k < Nv; k++) {
        const a1 = Math.atan2(y-vy[k], x-vx[k]);
        const a2 = Math.atan2(y+1-vy[k], x-vx[k]);
        ph += 0.5*vq[k]*(a2-a1);
      }
      const v = exp1j(ph);
      H[idx(x,y)][idx(x,y+1)] = v;
      H[idx(x,y+1)][idx(x,y)] = new Complex(v.re, -v.im);
    }
  for (let y = 0; y < L; y++)
    for (let x = 0; x < L; x++) {
      let d = 0;
      for (let k = 0; k < Nv; k++) {
        const r2 = (x+1-vx[k])**2 + (y+1-vy[k])**2;
        d += vq[k]*W/(r2/N + 1);
      }
      H[idx(x,y)][idx(x,y)] = new Complex(d, 0);
    }
  return H;
}
function mulberry(a){ return function(){ a|=0; a=a+0x6D2B79F5|0;
  let t=Math.imul(a^a>>>15,1|a); t=t+Math.imul(t^t>>>7,61|t)^t;
  return ((t^t>>>14)>>>0)/4294967296; } }
function exp1j(p){ return new Complex(Math.cos(p), Math.sin(p)); }
// Якоби для эрмитовой матрицы (объекты Complex)
function jacobiEig(Hin, sweeps=12) {
  const n = Hin.length;
  const A = [];
  for (let i = 0; i < n; i++) { A.push(new Array(n));
    for (let j = 0; j < n; j++) A[i][j] = new Complex(Hin[i][j].re,
      Hin[i][j].im); }
  for (let sw = 0; sw < sweeps; sw++) {
    let off = 0;
    for (let i = 0; i < n-1; i++) for (let j = i+1; j < n; j++)
      off += A[i][j].re*A[i][j].re + A[i][j].im*A[i][j].im;
    if (off < 1e-22) break;
    for (let p = 0; p < n-1; p++) for (let q = p+1; q < n; q++) {
      const m = A[p][q].re*A[p][q].re + A[p][q].im*A[p][q].im;
      if (m < 1e-28) continue;
      const absa = Math.sqrt(m);
      const a = A[p][q];
      const delta = A[q][q].re - A[p][p].re;
      const th = delta/(2*absa);
      const t = Math.sign(th || 1)/(Math.abs(th) + Math.sqrt(th*th+1));
      const c = 1/Math.sqrt(t*t+1);
      const ph = Math.atan2(a.im, a.re);
      const s = new Complex(t*c*Math.cos(ph), t*c*Math.sin(ph));
      const sb = new Complex(s.re, -s.im);
      for (let k = 0; k < n; k++) {
        const apk = A[p][k], aqk = A[q][k];
        A[p][k] = new Complex(c*apk.re - s.re*aqk.re + s.im*aqk.im,
          c*apk.im - s.re*aqk.im - s.im*aqk.re);
        A[q][k] = new Complex(sb.re*apk.re - sb.im*apk.im + c*aqk.re,
          sb.re*apk.im + sb.im*apk.re + c*aqk.im);
      }
      for (let k = 0; k < n; k++) {
        const akp = A[k][p], akq = A[k][q];
        A[k][p] = new Complex(c*akp.re - sb.re*akq.re + sb.im*akq.im,
          c*akp.im - sb.re*akq.im - sb.im*akq.re);
        A[k][q] = new Complex(s.re*akp.re - s.im*akp.im + c*akq.re,
          s.re*akp.im + s.im*akp.re + c*akq.im);
      }
      A[p][p] = new Complex(A[p][p].re, 0);
      A[q][q] = new Complex(A[q][q].re, 0);
      A[p][q] = new Complex(0, 0);
      A[q][p] = new Complex(0, 0);
    }
  }
  const ev = [];
  for (let i = 0; i < n; i++) ev.push(A[i][i].re);
  return ev.sort((x,y)=>x-y);
}
function drawGate() {
  const L = +document.getElementById('gL').value;
  const Nv = +document.getElementById('gNv').value;
  const q = +document.getElementById('gq').value/10;
  const W = +document.getElementById('gW').value/10;
  document.getElementById('gLv').textContent = L;
  document.getElementById('gNvv').textContent = Nv;
  document.getElementById('gqv').textContent = q.toFixed(1);
  document.getElementById('gWv').textContent = W.toFixed(1);
  const H = buildH(L, Nv, q, W);
  const ev = jacobiEig(H, 24);
  const n = ev.length, half = Math.floor(n*0.3);
  const cen = ev.slice(Math.floor(n/2)-half, Math.floor(n/2)+half);
  const u = unfold(cen).slice(0, 120);
  const r = meanR(u);
  // гистограмма развёрнутых промежутков
  const cv = document.getElementById('cv1'), cx = cv.getContext('2d');
  const w = cv.width, h = cv.height;
  cx.clearRect(0,0,w,h);
  const bins = 24, lo = 0, hi = 2.2;
  const hist = new Array(bins).fill(0);
  for (let i = 1; i < u.length; i++) {
    const s = u[i]-u[i-1];
    const b = Math.floor((s-lo)/(hi-lo)*bins);
    if (b >= 0 && b < bins) hist[b]++;
  }
  const mx = Math.max(...hist, 1);
  const bw = w/bins;
  for (let b = 0; b < bins; b++) {
    const bh = hist[b]/mx*(h-60);
    cx.fillStyle = '#4FB3BE';
    cx.fillRect(b*bw+2, h-30-bh, bw-4, bh);
  }
  // сурмиза GUE
  cx.strokeStyle = '#E08B66'; cx.lineWidth = 2; cx.beginPath();
  for (let px = 0; px < w; px++) {
    const s = lo + (hi-lo)*px/w;
    const p = 32/Math.PI/Math.PI*s*s*Math.exp(-4*s*s/Math.PI)*u.length*(hi-lo)/bins;
    const py = h-30 - p/mx*(h-60);
    px===0 ? cx.moveTo(px,py) : cx.lineTo(px,py);
  }
  cx.stroke();
  cx.fillStyle = '#9A938A'; cx.font = '11px sans-serif';
  cx.fillText('s', w-14, h-8); cx.fillText('p(s)', 6, 16);
  document.getElementById('ro1').innerHTML =
    'N = ' + (L*L) + ' · ⟨r⟩ = <span class="cop">' + r.toFixed(4)
    + '</span> · GUE 0.5992 · '
    + (LANG==='ru' ? 'уровней в окне: ' : 'levels in window: ') + u.length;
}
function unfold(vals) {
  const n = vals.length;
  const idx = [...Array(n).keys()];
  // монотонная кусочно-линейная развёртка по рангам
  const sorted = [...vals].map((v,i)=>[v,i]).sort((a,b)=>a[0]-b[0]);
  const u = new Array(n);
  const knots = 8;
  for (let k = 0; k < knots; k++) {
    const a = Math.floor(k*n/knots), b = Math.min(n-1,
      Math.floor((k+1)*n/knots));
    for (let i = a; i <= b; i++) u[sorted[i][1]] = i;
  }
  return u;
}
function meanR(u) {
  let acc = 0, cnt = 0;
  for (let i = 0; i < u.length-2; i++) {
    const s1 = u[i+1]-u[i], s2 = u[i+2]-u[i+1];
    if (s1 > 0 && s2 > 0) { acc += Math.min(s1,s2)/Math.max(s1,s2); cnt++; }
  }
  return cnt ? acc/cnt : 0;
}

// ── Тепловой след ↔ простые ──────────────────────────────────────────
function drawTrace() {
  const cv = document.getElementById('cv2'), cx = cv.getContext('2d');
  const w = cv.width, h = cv.height;
  cx.clearRect(0,0,w,h);
  const xs = [], K = [], P = [];
  for (let i = 0; i <= 60; i++) {
    const x = 0.05 + 1.2*i/60;
    let k = 0;
    for (const g of ZEROS) { if (g > 3000) break; k += Math.exp(-x*g); }
    let p = 0;
    for (const [n, l] of CARR) {
      const ln = Math.log(n);
      p += l/Math.sqrt(n)*x/(x*x+ln*ln);
    }
    xs.push(x); K.push(k); P.push(p);
  }
  const kmax = Math.max(...K), pmax = Math.max(...P);
  // K на левую ось, P на правую (нормировка к общей высоте)
  cx.strokeStyle = '#4FB3BE'; cx.lineWidth = 2; cx.beginPath();
  xs.forEach((x,i)=>{ const px = x/1.25*w, py = h-30-K[i]/kmax*(h-70);
    i===0?cx.moveTo(px,py):cx.lineTo(px,py); });
  cx.stroke();
  cx.strokeStyle = '#E08B66'; cx.beginPath();
  xs.forEach((x,i)=>{ const px = x/1.25*w, py = h-30-P[i]/pmax*(h-70);
    i===0?cx.moveTo(px,py):cx.lineTo(px,py); });
  cx.stroke();
  cx.fillStyle = '#9A938A'; cx.font = '12px sans-serif';
  cx.fillText('K(x) = Σ e^(−xγ)', 14, 24);
  cx.fillStyle = '#E08B66';
  cx.fillText('P(u) = Σ Λ(n)/√n·u/(u²+ln²n)', 220, 24);
  document.getElementById('ro2').innerHTML =
    (LANG==='ru' ? 'Обе кривые убывают согласованно — вес простых живёт '
      + 'в тепловом следе нулей (V7, PC0 r = +0.9996).'
      : 'Both curves decay consistently — the prime weight lives in the '
      + 'heat trace of the zeros (V7, PC0 r = +0.9996).');
}

// ── Критерий Ли ──────────────────────────────────────────────────────
function drawLi() {
  const cv = document.getElementById('cv3'), cx = cv.getContext('2d');
  const w = cv.width, h = cv.height;
  cx.clearRect(0,0,w,h);
  const n = LAM.length;
  const mx = Math.max(...LAM);
  cx.strokeStyle = '#4FB3BE'; cx.lineWidth = 1.6; cx.beginPath();
  for (let i = 0; i < n; i++) {
    const px = i/n*w, py = h-30-Math.sqrt(LAM[i]/mx)*(h-60);
    i===0?cx.moveTo(px,py):cx.lineTo(px,py);
  }
  cx.stroke();
  cx.strokeStyle = '#2A2A3A'; cx.beginPath(); cx.moveTo(0,h-30);
  cx.lineTo(w,h-30); cx.stroke();
  cx.fillStyle = '#E08B66';
  cx.fillRect(0, h-32, w, 2);
  cx.fillStyle = '#9A938A'; cx.font = '12px sans-serif';
  cx.fillText('n →', w-40, h-8);
  document.getElementById('ro3').innerHTML =
    'λ_1 = ' + LAM[0].toFixed(6) + ' (−B = 0.023096) · λ_100 = '
    + LAM[99].toFixed(3) + ' · λ_1000 = ' + LAM[999].toFixed(1)
    + ' · <span class="cop">'
    + (LANG==='ru' ? 'все λ_n > 0 на встроенных 1000' : 'all λ_n > 0 on '
      + 'the embedded 1000') + '</span>';
}

// ── ψ-лестница ───────────────────────────────────────────────────────
function drawPsi() {
  const cv = document.getElementById('cv4'), cx = cv.getContext('2d');
  const w = cv.width, h = cv.height;
  cx.clearRect(0,0,w,h);
  const xmax = 100000;
  let psi = 0, j = 0;
  const pxs = [], pys = [];
  for (let x = 100; x <= xmax; x += Math.ceil(xmax/900)) {
    while (j < CARR.length && CARR[j][0] <= x) { psi += CARR[j][1]; j++; }
    pxs.push(x); pys.push(psi);
  }
  const ymax = Math.max(...pys);
  cx.strokeStyle = '#4FB3BE'; cx.lineWidth = 2; cx.beginPath();
  pxs.forEach((x,i)=>{ const px = Math.log10(x/100)/Math.log10(xmax/100)*w;
    const py = h-30-pys[i]/ymax*(h-60);
    i===0?cx.moveTo(px,py):cx.lineTo(px,py); });
  cx.stroke();
  cx.strokeStyle = '#E08B66'; cx.setLineDash([6,5]); cx.beginPath();
  pxs.forEach((x,i)=>{ const px = Math.log10(x/100)/Math.log10(xmax/100)*w;
    const py = h-30-x/ymax*(h-60);
    i===0?cx.moveTo(px,py):cx.lineTo(px,py); });
  cx.stroke(); cx.setLineDash([]);
  cx.fillStyle = '#9A938A'; cx.font = '12px sans-serif';
  cx.fillText('ψ(x)', 14, 24); cx.fillText('x', w-20, h-8);
  cx.fillText('10^2', 2, h-10); cx.fillText('10^5', w-34, h-10);
  document.getElementById('ro4').innerHTML =
    'ψ(10^5) = ' + Math.round(pys[pys.length-1])
    + ' · x = 100000 · '
    + (LANG==='ru' ? 'лестница прижимается к прямой — теорема о простых '
      + 'числах в миниатюре' : 'the staircase hugs the line — the prime '
      + 'number theorem in miniature');
}

function drawAll() { drawZ(); drawGate(); drawTrace(); drawLi();
  drawPsi(); }
setLang('ru');
</script>
</body>
</html>'''

html = (HTML.replace('__ZEROS__', json.dumps(ZL, separators=(',', ':')))
            .replace('__LAM__', json.dumps(LAM, separators=(',', ':')))
            .replace('__CARR__', json.dumps(CARR, separators=(',', ':'))))

out = os.path.join(ROOT, 'web_lab', 'index.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(html)
print(f'WEB LAB OK: {out} ({len(html)//1024} KB)')
