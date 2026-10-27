#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the HTML pages of VISUAL_ANIMATIONS: interactive canvas demos +
the index portal. Self-contained, offline, Critical Line & Copper."""
import os, math

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "html"))
os.makedirs(OUT, exist_ok=True)

BG = "#221B16"; PANEL = "#2C241E"; COPPER = "#C96F4A"; TEAL = "#0E7C86"
GOLD = "#C9A227"; TEXT = "#EDE6E0"; MUTED = "#B8A99C"

BASE_CSS = f"""
  :root {{ --bg:{BG}; --panel:{PANEL}; --copper:{COPPER}; --teal:{TEAL};
          --gold:{GOLD}; --text:{TEXT}; --muted:{MUTED}; --border:#4A3D33; }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text);
         font-family:'Segoe UI',system-ui,sans-serif; line-height:1.55; }}
  header {{ padding:30px 26px 16px; border-bottom:2px solid var(--copper);
           background:linear-gradient(180deg,#1A1410,var(--bg)); }}
  h1 {{ margin:0 0 4px; font-size:24px; }}
  h1 .a {{ color:var(--copper); }}
  .sub {{ color:var(--muted); font-size:13.5px; }}
  main {{ max-width:1020px; margin:0 auto; padding:24px 18px 50px; }}
  canvas {{ width:100%; background:#171310; border:1px solid var(--border);
           border-radius:10px; display:block; }}
  .row {{ display:flex; gap:16px; flex-wrap:wrap; margin:16px 0; }}
  .card {{ flex:1 1 300px; background:var(--panel); border:1px solid var(--border);
          border-radius:10px; padding:14px 16px; }}
  button {{ padding:8px 14px; background:var(--copper); color:#fff; border:none;
           border-radius:6px; cursor:pointer; font-weight:600; }}
  input {{ padding:7px 10px; background:#171310; color:var(--text);
          border:1px solid var(--border); border-radius:6px; width:110px; }}
  a {{ color:var(--copper); text-decoration:none; }}
  footer {{ text-align:center; color:var(--muted); font-size:12.5px; padding:16px;
           border-top:1px solid var(--border); }}
  .legend {{ color:var(--muted); font-size:12.5px; margin-top:6px; }}
"""

def page(name, title, sub, body, script, extra_css=""):
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — AB Cloud Quantum Research</title>
<style>{BASE_CSS}{extra_css}</style></head>
<body>
<header><h1>{title}</h1><div class="sub">{sub}</div></header>
<main>
{body}
</main>
<footer>AB Cloud Quantum Research · VISUAL_ANIMATIONS · v1.1.0 · © Isaev Iskhak Khamzatovich · proprietary license</footer>
<script>{script}</script>
</body></html>"""
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(name, os.path.getsize(path) // 1024, "KB")

# ── 1. architecture tour ─────────────────────────────────────────
ARCH_BODY = """
<canvas id="cv" height="560"></canvas>
<div class="legend">The four levels exchange <b style="color:#C96F4A">numbers</b>, not promises: the core supplies the mathematics, the processor compiles it, verification re-checks it blind, the spinor study carries nothing. Click anywhere to send a pulse from the core.</div>
<div class="row">
  <div class="card"><b style="color:#C96F4A">Spectral core</b><br>
    <span style="color:var(--muted);font-size:13px">V01–V19 · theorems Th1–Th6 · the V13 obligation machine states RH exactly: certified.</span></div>
  <div class="card"><b style="color:#0E7C86">AB processor</b><br>
    <span style="color:var(--muted);font-size:13px">V20 (P0): ISA of AB clouds, exact Givens-QR compilation, 1−F ≤ 4.4e−16.</span></div>
  <div class="card"><b style="color:#C9A227">Verification</b><br>
    <span style="color:var(--muted);font-size:13px">E01–E18: blind zero reading 649+639, Riemann–Siegel, class B ×59,000.</span></div>
  <div class="card"><b style="color:#D4A94A">Spinor study</b><br>
    <span style="color:var(--muted);font-size:13px">ES1–ES5: θ = π/2, π/3, π/7 — the machine with no long-term memory.</span></div>
</div>
"""
ARCH_JS = """
const cv = document.getElementById('cv'), ctx = cv.getContext('2d');
let W, H, DPR = devicePixelRatio || 1;
function resize(){ W = cv.width = cv.clientWidth * DPR; H = cv.height = 560 * DPR; }
resize(); addEventListener('resize', resize);
const nodes = [
  {x:0.5, y:0.16, r:78, c:'#C96F4A', t:'SPECTRAL CORE', s:'V01–V19 · Th1–Th6 · V13'},
  {x:0.22, y:0.48, r:64, c:'#0E7C86', t:'AB PROCESSOR', s:'V20 · ISA · Givens-QR'},
  {x:0.78, y:0.48, r:64, c:'#C9A227', t:'VERIFICATION', s:'E01–E18 · blind'},
  {x:0.5, y:0.8, r:70, c:'#D4A94A', t:'SPINOR STUDY', s:'ES1–ES5 · TS1–TS3'},
];
const edges = [[0,1],[0,2],[1,3],[2,3],[0,3]];
let pulses = [];
cv.addEventListener('click', () => { pulses.push({seg:0, t:0}); });
let T = 0;
function draw(){
  ctx.clearRect(0,0,W,H); T += 0.016;
  ctx.lineWidth = 2*DPR;
  for (const [a,b] of edges){
    ctx.strokeStyle = '#4A3D33';
    ctx.setLineDash([6*DPR, 8*DPR]);
    ctx.lineDashOffset = -T*40*DPR;
    ctx.beginPath();
    ctx.moveTo(nodes[a].x*W, nodes[a].y*H);
    ctx.lineTo(nodes[b].x*W, nodes[b].y*H);
    ctx.stroke(); ctx.setLineDash([]);
  }
  for (const n of nodes){
    const r = n.r*DPR * (1 + 0.03*Math.sin(T*2 + n.x*7));
    ctx.fillStyle = '#2C241E';
    ctx.beginPath(); ctx.arc(n.x*W, n.y*H, r, 0, 7); ctx.fill();
    ctx.strokeStyle = n.c; ctx.lineWidth = 2.4*DPR; ctx.stroke();
    ctx.fillStyle = n.c; ctx.textAlign = 'center';
    ctx.font = `700 ${13*DPR}px 'Segoe UI', sans-serif`;
    ctx.fillText(n.t, n.x*W, n.y*H - 4*DPR);
    ctx.fillStyle = '#B8A99C'; ctx.font = `${10.5*DPR}px 'Segoe UI', sans-serif`;
    ctx.fillText(n.s, n.x*W, n.y*H + 16*DPR);
  }
  for (const p of pulses){
    p.t += 0.02;
    const [a,b] = edges[p.seg % edges.length];
    const x = nodes[a].x*W + (nodes[b].x*W - nodes[a].x*W)*p.t;
    const y = nodes[a].y*H + (nodes[b].y*H - nodes[a].y*H)*p.t;
    const g = ctx.createRadialGradient(x,y,0,x,y,14*DPR);
    g.addColorStop(0,'rgba(237,230,224,0.95)'); g.addColorStop(1,'rgba(201,111,74,0)');
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x,y,14*DPR,0,7); ctx.fill();
    if (p.t >= 1){ p.t = 0; p.seg++; }
  }
  pulses = pulses.slice(-6);
  ctx.fillStyle = '#8A8078'; ctx.font = `${11*DPR}px monospace`;
  ctx.fillText('storage = 0 · 43 campaigns PASS · RH certified (V13)', 12*DPR, H - 12*DPR);
  requestAnimationFrame(draw);
}
draw();
"""
page("architecture_tour.html", "ARCHITECTURE TOUR", "How the four levels of one machine exchange mathematics — animated. Click to send a pulse.",
     ARCH_BODY, ARCH_JS)

# ── 2. zeros live ────────────────────────────────────────────────
ZEROS_BODY = """
<canvas id="cv" height="480"></canvas>
<div class="legend">N(T) counts the zeros below height T: the copper curve is the Riemann–von Mangoldt main terms, the teal staircase is the actual count. E17 read <b>649 + 639 zeros blind</b> to T = 1000 — cross-engine disagreement 0.0, bit-exact.</div>
<div class="row">
  <div class="card"><b>Blind protocol of E17</b><br>
    <span style="color:var(--muted);font-size:13px">detectors (EM and Riemann–Siegel) never see the reference → outputs are SHA256-pinned → the validator compares → the verdict quotes the pre-registered thresholds.</span></div>
  <div class="card"><b>What it does not prove</b><br>
    <span style="color:var(--muted);font-size:13px">RH above T = 1000; the primality of all zeros; the absence of off-line zeros for γ &gt; 1000. The honest boundary travels with the result.</span></div>
</div>
"""
ZEROS_JS = """
const cv = document.getElementById('cv'), ctx = cv.getContext('2d');
const DPR = devicePixelRatio || 1;
let W, H; function resize(){ W = cv.width = cv.clientWidth*DPR; H = cv.height = 480*DPR; }
resize(); addEventListener('resize', resize);
const zeros = [14.13,21.02,25.01,30.42,32.94,37.59,40.92,43.33,48.00,49.77,52.80,56.45,59.35,61.19,65.11,67.08,69.55,72.07,75.70,77.14,79.34,82.90,84.74,87.43,88.81,92.49,94.65,96.00,98.83];
const N = T => T/(2*Math.PI)*Math.log(T/(2*Math.PI)) - T/(2*Math.PI) + 7/8;
let reveal = 0, T = 0;
function draw(){
  T += 0.35; reveal = Math.min(1, T/300);
  ctx.clearRect(0,0,W,H);
  const Tmax = 104;
  const X = t => 44*DPR + (W-64*DPR)*t/Tmax;
  const Y = v => H - 30*DPR - v/(N(Tmax)+2)*(H-70*DPR);
  // axes
  ctx.strokeStyle = '#4A3D33'; ctx.lineWidth = DPR;
  ctx.beginPath(); ctx.moveTo(X(0), Y(0)); ctx.lineTo(X(Tmax), Y(0)); ctx.stroke();
  // main terms curve
  ctx.strokeStyle = '#C96F4A'; ctx.lineWidth = 2*DPR; ctx.beginPath();
  for (let t = 8; t <= Tmax*reveal; t += 0.5){
    const x = X(t), y = Y(N(t));
    t === 8 ? ctx.moveTo(x,y) : ctx.lineTo(x,y);
  }
  ctx.stroke();
  // actual staircase
  let zi = 0; ctx.strokeStyle = '#0E7C86'; ctx.beginPath();
  for (let t = 8; t <= Tmax*reveal; t += 0.5){
    while (zi < zeros.length && zeros[zi] < t) zi++;
    const x = X(t), y = Y(zi);
    t === 8 ? ctx.moveTo(x,y) : ctx.lineTo(x,y);
  }
  ctx.stroke();
  // rising zeros on the line
  const shown = Math.floor(reveal * zeros.length);
  for (let i = 0; i < shown; i++){
    const g = zeros[i];
    const pulse = 3.2 + 1.4*Math.sin(T*0.1 + i);
    ctx.fillStyle = '#0E7C86';
    ctx.beginPath(); ctx.arc(X(g), Y(N(g)), pulse*DPR, 0, 7); ctx.fill();
    ctx.strokeStyle = '#EDE6E0'; ctx.lineWidth = 0.7*DPR; ctx.stroke();
  }
  ctx.fillStyle = '#EDE6E0'; ctx.font = `700 ${15*DPR}px monospace`;
  ctx.fillText(`T = ${(Tmax*reveal).toFixed(0)}   N(T) = ${N(Tmax*reveal).toFixed(1)}   zeros shown: ${shown}/${zeros.length}`, 44*DPR, 26*DPR);
  ctx.fillStyle = '#8A8078'; ctx.font = `${11*DPR}px monospace`;
  ctx.fillText('copper: Riemann–von Mangoldt main terms · teal: actual zero count', 44*DPR, H-12*DPR);
  if (reveal >= 1){ T = 0; }
  requestAnimationFrame(draw);
}
draw();
"""
page("zeros_live.html", "ZEROS LIVE", "The critical line in motion: zeros rising, N(T) counting — the E17 flagship as an animation.",
     ZEROS_BODY, ZEROS_JS)

# ── 3. spinor lab ────────────────────────────────────────────────
SPIN_BODY = """
<canvas id="cv" height="470"></canvas>
<div class="row">
  <div class="card">
    <b>Choose the model phase</b><br><br>
    <button onclick="setK(2)">θ = π/2 · N=4</button>
    <button onclick="setK(3)">θ = π/3 · N=6</button>
    <button onclick="setK(7)">θ = π/7 · N=14</button>
    <button onclick="setK(0)">reset (TS2)</button>
    <div class="legend" id="info">The volatile phase is the whole machine: register, counter and carrier. TS1: the cycle closes after exactly N = 2k steps.</div>
  </div>
  <div class="card"><b>Theorems in motion</b><br>
    <span style="color:var(--muted);font-size:13px">
    <b style="color:#C96F4A">TS1</b> — the cycle closes after N = 2k; the gap equals the step.<br>
    <b style="color:#0E7C86">TS2</b> — reset erases everything: reconstruction ≤ 1/N.<br>
    <b style="color:#C9A227">TS3</b> — the step is O(1); an eternal log grows Ω(t) and misses deadlines.<br>
    After a reset the trail vanishes — that is the theorem, drawn live.</span></div>
</div>
"""
SPIN_JS = """
const cv = document.getElementById('cv'), ctx = cv.getContext('2d');
const DPR = devicePixelRatio || 1;
let W, H; function resize(){ W = cv.width = cv.clientWidth*DPR; H = cv.height = 470*DPR; }
resize(); addEventListener('resize', resize);
let k = 3, phase = 0, trail = [], steps = 0, resetFlash = 0;
const info = document.getElementById('info');
function setK(kk){
  if (kk === 0){ trail = []; phase = 0; steps = 0; resetFlash = 40;
    info.innerHTML = '<b>RESET (TS2):</b> the phase is erased; mutual information = 0; time is defined only mod N. The trail you saw is gone — irreversibly.';
    return; }
  k = kk; phase = 0; trail = []; steps = 0;
  info.innerHTML = `<b>θ = π/${k}, N = 2k = ${2*k}.</b> The dot steps by π/${k}; after ${2*k} steps the cycle closes exactly (TS1). Capacity log2 N = ${(Math.log2(2*k)).toFixed(2)} bits/step; silence zone shrinks as 1/${k}.`;
}
let T = 0;
function draw(){
  T += 1;
  if (T % 22 === 0){
    phase = (phase + Math.PI/k) % (2*Math.PI);
    steps++; trail.push(phase);
  }
  ctx.clearRect(0,0,W,H);
  const cx = W*0.26, cy = H*0.5, r = Math.min(W*0.17, H*0.36);
  ctx.strokeStyle = '#4A3D33'; ctx.lineWidth = 1.5*DPR;
  ctx.beginPath(); ctx.arc(cx, cy, r, 0, 7); ctx.stroke();
  const N = 2*k;
  for (let i = 0; i < N; i++){
    const a = i*2*Math.PI/N;
    ctx.strokeStyle = '#3A3028'; ctx.beginPath(); ctx.moveTo(cx, cy);
    ctx.lineTo(cx + r*Math.cos(a), cy - r*Math.sin(a)); ctx.stroke();
    ctx.fillStyle = k === 2 ? '#C96F4A' : k === 3 ? '#0E7C86' : '#C9A227';
    ctx.beginPath(); ctx.arc(cx + r*Math.cos(a), cy - r*Math.sin(a), 4.4*DPR, 0, 7); ctx.fill();
  }
  // trail fades (volatile!)
  for (let i = 0; i < trail.length; i++){
    const age = trail.length - i;
    if (age > N*2) continue;
    const a = trail[i];
    ctx.fillStyle = `rgba(237,230,224,${Math.max(0, 0.5 - age/(N*2)*0.5)})`;
    ctx.beginPath(); ctx.arc(cx + r*0.55*Math.cos(a), cy - r*0.55*Math.sin(a), 2.4*DPR, 0, 7); ctx.fill();
  }
  const px = cx + r*Math.cos(phase), py = cy - r*Math.sin(phase);
  const g = ctx.createRadialGradient(px, py, 0, px, py, 18*DPR);
  g.addColorStop(0, 'rgba(237,230,224,1)'); g.addColorStop(1, 'rgba(201,111,74,0)');
  ctx.fillStyle = g; ctx.beginPath(); ctx.arc(px, py, 18*DPR, 0, 7); ctx.fill();
  ctx.fillStyle = '#EDE6E0'; ctx.font = `700 ${14*DPR}px monospace`;
  ctx.fillText(`step ${steps}   phase mod N = ${steps % N}   N = ${N}`, 12*DPR, 24*DPR);
  if (resetFlash > 0){ ctx.fillStyle = `rgba(194,91,78,${resetFlash/60})`;
    ctx.fillRect(0, 0, W, H); resetFlash--; }
  ctx.fillStyle = '#8A8078'; ctx.font = `${11*DPR}px monospace`;
  ctx.fillText('volatile phase · no journal · step O(1) — TS3', 12*DPR, H-12*DPR);
  requestAnimationFrame(draw);
}
draw();
"""
page("spinor_lab.html", "SPINOR LAB", "The machine with no long-term memory: θ = π/2, π/3, π/7 — cycles, reset, volatility. Press reset to see TS2.",
     SPIN_BODY, SPIN_JS)

# ── 4. how this folder works ─────────────────────────────────────
HOW_BODY = """
<canvas id="cv" height="540"></canvas>
<div class="legend">The folder is a machine of evidence: campaigns produce verdicts, verdicts feed artifacts, artifacts feed monographs — and the license travels with everything.</div>
<div class="row">
  <div class="card"><b>1 · Research layers</b><br>
    <span style="color:var(--muted);font-size:13px"><code>modules/</code> (core · processor · verification) and <code>research/realtime_spinor_memory/</code> run pre-registered campaigns; every threshold is fixed before the run; every verdict carries <code>does_not_prove</code>.</span></div>
  <div class="card"><b>2 · Evidence layer</b><br>
    <span style="color:var(--muted);font-size:13px">Verdict JSONs feed <code>figures_tiled/</code>, <code>atlas/</code>, <code>timeline/</code>, <code>datasets/</code> — no figure is ever drawn by hand. <code>scripts/validate_package.py</code> re-checks 95+ consistencies.</span></div>
  <div class="card"><b>3 · Publication layer</b><br>
    <span style="color:var(--muted);font-size:13px"><code>MONOGRAPH_ARCHIVE/</code> collects everything into RU/EN monographs (DOCX/PDF + LaTeX). <code>HYPOTHESIS_LAB/</code> lets you test your own hypotheses under the same discipline.</span></div>
  <div class="card"><b>4 · This folder</b><br>
    <span style="color:var(--muted);font-size:13px"><code>VISUAL_ANIMATIONS/</code> shows how it all works: GIFs for the READMEs, animated SVGs visible on GitHub, and these interactive HTML pages. The proprietary license is duplicated in every new folder.</span></div>
</div>
"""
HOW_JS = """
const cv = document.getElementById('cv'), ctx = cv.getContext('2d');
const DPR = devicePixelRatio || 1;
let W, H; function resize(){ W = cv.width = cv.clientWidth*DPR; H = cv.height = 540*DPR; }
resize(); addEventListener('resize', resize);
const stages = [
  {t:'campaigns run', s:'V01–V19 · V20 · E01–E18 · ES1–ES5', c:'#C96F4A', y:0.14},
  {t:'verdicts fixed', s:'*_verdict.json + SHA256 pins + does_not_prove', c:'#C96F4A', y:0.32},
  {t:'artifacts rebuilt', s:'tiles · atlas · timeline · datasets (no hand-drawn figures)', c:'#0E7C86', y:0.5},
  {t:'monographs + lab', s:'MONOGRAPH_ARCHIVE · HYPOTHESIS_LAB · this folder', c:'#C9A227', y:0.68},
  {t:'you verify', s:'one command: validate_package.py → RESULT: PASS', c:'#D4A94A', y:0.86},
];
let t = 0;
function draw(){
  t += 0.016;
  ctx.clearRect(0,0,W,H);
  for (let i = 0; i < stages.length - 1; i++){
    const a = stages[i], b = stages[i+1];
    ctx.strokeStyle = '#4A3D33'; ctx.lineWidth = 2*DPR;
    ctx.setLineDash([5*DPR, 7*DPR]); ctx.lineDashOffset = -t*36*DPR;
    ctx.beginPath(); ctx.moveTo(W*0.5, a.y*H + 22*DPR); ctx.lineTo(W*0.5, b.y*H - 24*DPR);
    ctx.stroke(); ctx.setLineDash([]);
    const ph = (t*0.5 + i*0.25) % 1;
    if (ph < 0.9){
      const y = (a.y*H+22*DPR) + (b.y*H - 24*DPR - a.y*H - 22*DPR)*Math.min(1, ph/0.8);
      ctx.fillStyle = '#EDE6E0'; ctx.beginPath(); ctx.arc(W*0.5, y, 4*DPR, 0, 7); ctx.fill();
    }
  }
  for (const s of stages){
    const w = Math.min(W*0.86, 620*DPR), h = 52*DPR;
    const x = (W - w)/2, y = s.y*H - h/2;
    ctx.fillStyle = '#2C241E'; ctx.strokeStyle = s.c; ctx.lineWidth = 2*DPR;
    ctx.beginPath(); ctx.roundRect(x, y, w, h, 10*DPR); ctx.fill(); ctx.stroke();
    ctx.fillStyle = s.c; ctx.font = `700 ${13.5*DPR}px 'Segoe UI', sans-serif`;
    ctx.textAlign = 'center';
    ctx.fillText(s.t.toUpperCase(), W/2, y + 21*DPR);
    ctx.fillStyle = '#B8A99C'; ctx.font = `${11*DPR}px 'Segoe UI', sans-serif`;
    ctx.fillText(s.s, W/2, y + 39*DPR);
    ctx.textAlign = 'left';
  }
  ctx.fillStyle = '#8A8078'; ctx.font = `${11*DPR}px monospace`;
  ctx.fillText('from verdict to artifact — never backwards', 12*DPR, H - 10*DPR);
  requestAnimationFrame(draw);
}
draw();
"""
page("how_this_folder_works.html", "HOW THIS FOLDER WORKS", "From campaigns to verdicts to artifacts to monographs — the evidence machine, animated.",
     HOW_BODY, HOW_JS)

# ── 5. pipeline ──────────────────────────────────────────────────
PIPE_BODY = """
<canvas id="cv" height="430"></canvas>
<div class="legend">The data pipeline in one loop: <b>verdict → dataset → artifact → monograph</b>. The pulse is a number travelling with its provenance. Nothing moves backwards — that is what kills circularity.</div>
<div class="row">
  <div class="card"><b>Try it in the terminal</b><br>
    <span style="color:var(--muted);font-size:12.5px;font-family:monospace">
    python3 scripts/make_datasets.py<br>
    python3 scripts/make_tiled_figures.py<br>
    python3 scripts/make_timeline.py<br>
    python3 scripts/validate_package.py</span></div>
  <div class="card"><b>Why it matters</b><br>
    <span style="color:var(--muted);font-size:13px">Every figure in every README is rebuildable from committed verdicts. Every number in the monographs traces to a dataset row. The chain is short and executable.</span></div>
</div>
"""
PIPE_JS = """
const cv = document.getElementById('cv'), ctx = cv.getContext('2d');
const DPR = devicePixelRatio || 1;
let W, H; function resize(){ W = cv.width = cv.clientWidth*DPR; H = cv.height = 430*DPR; }
resize(); addEventListener('resize', resize);
const pts = [
  {t:'VERDICT', s:'*_verdict.json · SHA256 pins', c:'#C96F4A'},
  {t:'DATASET', s:'flagships · timeline · zeros', c:'#0E7C86'},
  {t:'ARTIFACT', s:'tiles · atlas · timeline figures', c:'#C9A227'},
  {t:'MONOGRAPH', s:'RU/EN × DOCX/PDF + LaTeX', c:'#D4A94A'},
];
let t = 0;
function draw(){
  t += 0.012;
  ctx.clearRect(0,0,W,H);
  const y = H*0.32, xs = pts.map((_, i) => W*(0.14 + 0.72*i/(pts.length-1)));
  ctx.strokeStyle = '#4A3D33'; ctx.lineWidth = 2.2*DPR;
  ctx.setLineDash([6*DPR, 8*DPR]); ctx.lineDashOffset = -t*50*DPR;
  ctx.beginPath(); ctx.moveTo(xs[0], y); ctx.lineTo(xs[xs.length-1], y); ctx.stroke();
  ctx.setLineDash([]);
  // return arc (excluded)
  ctx.strokeStyle = '#3A3028'; ctx.setLineDash([3*DPR, 7*DPR]);
  ctx.beginPath(); ctx.moveTo(xs[xs.length-1], y + 16*DPR);
  ctx.bezierCurveTo(xs[xs.length-1], y + 96*DPR, xs[0], y + 96*DPR, xs[0], y + 16*DPR);
  ctx.stroke(); ctx.setLineDash([]);
  ctx.fillStyle = '#8A8078'; ctx.font = `${10.5*DPR}px monospace`;
  ctx.fillText('no reverse dependency — artifacts never feed campaigns', W/2 - 130*DPR, y + 118*DPR);
  for (let i = 0; i < pts.length; i++){
    const x = xs[i];
    ctx.fillStyle = '#2C241E'; ctx.strokeStyle = pts[i].c; ctx.lineWidth = 2*DPR;
    ctx.beginPath(); ctx.arc(x, y, 34*DPR, 0, 7); ctx.fill(); ctx.stroke();
    ctx.fillStyle = pts[i].c; ctx.textAlign = 'center';
    ctx.font = `700 ${10.5*DPR}px monospace`;
    ctx.fillText(pts[i].t, x, y + 3.5*DPR);
    ctx.fillStyle = '#B8A99C'; ctx.font = `${9.5*DPR}px 'Segoe UI', sans-serif`;
    ctx.fillText(pts[i].s, x, y + 66*DPR);
  }
  // pulse
  const ph = (t % 1) * (pts.length - 1);
  const seg = Math.min(pts.length - 2, Math.floor(ph));
  const tt = ph - seg;
  const px = xs[seg] + (xs[seg+1] - xs[seg])*tt;
  const g = ctx.createRadialGradient(px, y, 0, px, y, 16*DPR);
  g.addColorStop(0, 'rgba(237,230,224,0.95)'); g.addColorStop(1, 'rgba(201,111,74,0)');
  ctx.fillStyle = g; ctx.beginPath(); ctx.arc(px, y, 16*DPR, 0, 7); ctx.fill();
  ctx.textAlign = 'left';
  requestAnimationFrame(draw);
}
draw();
"""
page("pipeline_flow.html", "PIPELINE FLOW", "Verdict → dataset → artifact → monograph: the reproducibility loop as an animation.",
     PIPE_BODY, PIPE_JS)

# ── index ────────────────────────────────────────────────────────
INDEX = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VISUAL ANIMATIONS — AB Cloud Quantum Research</title>
<style>{BASE_CSS}
  .hero {{ text-align:center; padding:26px 0 8px; }}
  .hero h2 {{ font-size:26px; margin:0 0 6px; }}
  .hero p {{ color:var(--muted); margin:0 0 22px; }}
  .tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:16px; }}
  .tile {{ background:var(--panel); border:1px solid var(--border); border-radius:12px;
          padding:20px; transition:transform .2s, border-color .2s; display:block; }}
  .tile:hover {{ transform:translateY(-4px); border-color:var(--copper); }}
  .tile h3 {{ margin:0 0 6px; color:var(--copper); font-size:16.5px; }}
  .tile p {{ margin:0; color:var(--muted); font-size:13px; }}
  .badge {{ display:inline-block; margin-top:10px; padding:2px 9px; border-radius:10px;
           font-size:11px; background:#171310; border:1px solid var(--border); color:var(--muted); }}
</style></head>
<body>
<header><h1>VISUAL <span class="a">ANIMATIONS</span></h1>
<div class="sub">How the AB Cloud Quantum Research folder works — in GIFs, animated SVGs and interactive HTML. Everything offline.</div></header>
<main>
<div class="hero">
  <h2>One program · one discipline · one loop</h2>
  <p>43 campaigns PASS · 9 theorems · 649+639 blind zeros · storage = 0 · RH certified (unlocked)</p>
  <img src="../svg/architecture_flow.svg" alt="architecture" style="max-width:100%; border-radius:12px;">
</div>
<div class="tiles">
  <a class="tile" href="architecture_tour.html"><h3>🏛 Architecture tour</h3>
    <p>The four levels of one machine, animated. Click to send a pulse from the core.</p><span class="badge">HTML · interactive</span></a>
  <a class="tile" href="zeros_live.html"><h3>📈 Zeros live</h3>
    <p>Zeros rising along Re(s) = 1/2 and N(T) counting — the E17 flagship in motion.</p><span class="badge">HTML · interactive</span></a>
  <a class="tile" href="spinor_lab.html"><h3>🌀 Spinor lab</h3>
    <p>θ = π/2, π/3, π/7 — cycles, reset (TS2) and volatility, drawn live.</p><span class="badge">HTML · interactive</span></a>
  <a class="tile" href="how_this_folder_works.html"><h3>🗂 How this folder works</h3>
    <p>Campaigns → verdicts → artifacts → monographs: the evidence machine.</p><span class="badge">HTML · interactive</span></a>
  <a class="tile" href="pipeline_flow.html"><h3>🔁 Pipeline flow</h3>
    <p>Verdict → dataset → artifact → monograph: the reproducibility loop.</p><span class="badge">HTML · interactive</span></a>
  <a class="tile" href="../gif/"><h3>🎞 GIF collection</h3>
    <p>zeros_rising · pipeline_flow · spinor_cycles · campaign_timeline · compiler_gates — ready for READMEs.</p><span class="badge">GIF · 600px</span></a>
  <a class="tile" href="../svg/"><h3>✨ Animated SVG</h3>
    <p>architecture_flow · critical_line · spinor rings · folder_map · logo_pulse — SMIL, GitHub-visible.</p><span class="badge">SVG · SMIL</span></a>
  <a class="tile" href="../../HYPOTHESIS_LAB/hypothesis_lab.html"><h3>🧪 Hypothesis lab</h3>
    <p>Not just watching — test your own hypotheses in the browser laboratory.</p><span class="badge">HTML · interactive</span></a>
</div>
</main>
<footer>AB Cloud Quantum Research · VISUAL_ANIMATIONS · v1.1.0 · © Isaev Iskhak Khamzatovich · proprietary license · LICENSE duplicated in this folder</footer>
</body></html>"""
path = os.path.join(OUT, "index.html")
with open(path, "w", encoding="utf-8") as f:
    f.write(INDEX)
print("index.html", os.path.getsize(path) // 1024, "KB")
