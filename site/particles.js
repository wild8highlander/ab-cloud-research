/**
 * particles.js — ambient "zero field" for the AB-Cloud portal landing.
 *
 * A lightweight canvas behind the content: drifting points (the nontrivial
 * zeros rising off the critical line), faint constellation links between
 * close neighbours, an occasional italic γ glyph, and a radial "γ-burst"
 * triggered by the Konami easter egg (portal.js dispatches 'ab:burst').
 *
 * Design constraints:
 *   • CSP-safe external file, zero dependencies
 *   • honors prefers-reduced-motion (renders nothing; CSS handles ambience)
 *   • pauses when the tab is hidden, caps DPR at 2, caps particle count
 *     by viewport area — negligible cost on phones and 4K alike
 *   • theme-aware: reads --accent from CSS, re-reads on 'ab:theme'
 */
(() => {
  'use strict';

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const canvas = document.getElementById('zeroField');
  if (!canvas || !canvas.getContext) return;
  const ctx = canvas.getContext('2d', { alpha: true });
  if (!ctx) return;

  const root = document.documentElement;

  let W = 0;
  let H = 0;
  let accent = [79, 195, 247]; // default --accent (#4fc3f7)
  let parts = [];
  let running = true;
  let rafId = 0;
  let lastT = 0;

  const MAX_PARTS = 90;
  const MAX_BURST = 170;
  const LINK_DIST2 = 12100; // 110 px squared

  function readAccent() {
    const raw = getComputedStyle(root).getPropertyValue('--accent').trim();
    const m = /^#?([0-9a-f]{6})$/i.exec(raw);
    if (m) {
      const n = parseInt(m[1], 16);
      accent = [(n >> 16) & 255, (n >> 8) & 255, n & 255];
    }
  }

  function rgba(alpha) {
    return `rgba(${accent[0]},${accent[1]},${accent[2]},${alpha})`;
  }

  function resize() {
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = Math.round(W * dpr);
    canvas.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    seed();
  }

  function seed() {
    const n = Math.min(MAX_PARTS, Math.max(24, Math.round((W * H) / 26000)));
    parts = [];
    for (let i = 0; i < n; i++) {
      parts.push({
        x: Math.random() * W,
        y: Math.random() * H,
        r: 0.6 + Math.random() * 1.7,
        v: -(6 + Math.random() * 16),          // px/s, upward drift
        drift: (Math.random() - 0.5) * 7,      // px/s, lateral wander
        a: 0.14 + Math.random() * 0.42,
        glyph: i % 17 === 0,                   // every 17th renders as γ
        burst: false,
        life: 1,
      });
    }
  }

  function burst() {
    const cx = W / 2;
    const cy = H * 0.38;
    const n = 70;
    for (let i = 0; i < n && parts.length < MAX_BURST; i++) {
      const ang = (Math.PI * 2 * i) / n + Math.random() * 0.4;
      const speed = 90 + Math.random() * 190;
      parts.push({
        x: cx,
        y: cy,
        r: 1 + Math.random() * 2.4,
        v: 0,
        drift: 0,
        a: 0.9,
        glyph: i % 6 === 0,
        burst: true,
        life: 1,
        vx: Math.cos(ang) * speed,
        vy: Math.sin(ang) * speed,
      });
    }
  }

  function frame(t) {
    if (!running) return;
    const dt = Math.min(50, t - lastT) / 1000 || 0.016;
    lastT = t;
    ctx.clearRect(0, 0, W, H);

    // links between close ambient particles (constellation lines)
    ctx.lineWidth = 1;
    for (let i = 0; i < parts.length; i++) {
      const p = parts[i];
      if (p.burst) continue;
      for (let j = i + 1; j < parts.length; j++) {
        const q = parts[j];
        if (q.burst) continue;
        const dx = p.x - q.x;
        const dy = p.y - q.y;
        const d2 = dx * dx + dy * dy;
        if (d2 < LINK_DIST2) {
          ctx.strokeStyle = rgba((1 - d2 / LINK_DIST2) * 0.10);
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.stroke();
        }
      }
    }

    // particles
    for (let i = parts.length - 1; i >= 0; i--) {
      const p = parts[i];

      if (p.burst) {
        p.life -= dt / 1.5;
        if (p.life <= 0) { parts.splice(i, 1); continue; }
        p.x += p.vx * dt;
        p.y += p.vy * dt;
        p.vy += 70 * dt; // gentle gravity
        draw(p, p.life * 0.9);
        continue;
      }

      p.y += p.v * dt;
      p.x += p.drift * dt;
      if (p.y < -14) { p.y = H + 12; p.x = Math.random() * W; }
      if (p.x < -14) p.x = W + 12;
      if (p.x > W + 14) p.x = -12;
      draw(p, p.a);
    }

    rafId = requestAnimationFrame(frame);
  }

  function draw(p, alpha) {
    if (p.glyph) {
      ctx.fillStyle = rgba(alpha);
      ctx.font = `italic ${Math.round(9 + p.r * 3.4)}px Georgia, serif`;
      ctx.fillText('γ', p.x, p.y);
      return;
    }
    ctx.fillStyle = rgba(alpha);
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fill();
  }

  function start() {
    if (!running) return;
    lastT = performance.now();
    rafId = requestAnimationFrame(frame);
  }

  readAccent();
  resize();
  start();

  root.addEventListener('ab:theme', () => {
    readAccent();
  });
  root.addEventListener('ab:burst', burst);

  window.addEventListener('resize', resize, { passive: true });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      running = false;
      cancelAnimationFrame(rafId);
    } else if (!running) {
      running = true;
      start();
    }
  });
})();
