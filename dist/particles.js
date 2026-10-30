/**
 * particles.js — ambient "zeros field" for the AB-Cloud portal landing.
 *
 * A quiet drift of glowing points (the ζ zeros) rising through the page.
 * Zero dependencies, CSP-safe, and polite:
 *   • honors prefers-reduced-motion (renders nothing at all)
 *   • pauses when the tab is hidden
 *   • caps devicePixelRatio at 2 to protect GPU memory
 *   • density scales with viewport area and never exceeds ~90 points
 *   • Konami easter egg: listens for 'ab:burst' and emits a radial pulse
 */
(() => {
  'use strict';

  const canvas = document.getElementById('zeroField');
  if (!canvas) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  const DPR = Math.min(window.devicePixelRatio || 1, 2);
  let W = 0, H = 0, dots = [], raf = 0, running = false;

  function resize() {
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = Math.round(W * DPR);
    canvas.height = Math.round(H * DPR);
    canvas.style.width = W + 'px';
    canvas.style.height = H + 'px';
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    seed();
  }

  function makeDot(burst) {
    const cyan = Math.random() < 0.8;
    return {
      x: Math.random() * W,
      y: burst ? H * 0.5 + (Math.random() - 0.5) * 40 : Math.random() * H,
      vx: burst ? (Math.random() - 0.5) * 3.2 : (Math.random() - 0.5) * 0.06,
      vy: burst ? (Math.random() - 0.5) * 3.2 : -(0.06 + Math.random() * 0.16),
      r: 0.8 + Math.random() * 1.4,
      a: 0.10 + Math.random() * 0.30,
      cyan,
    };
  }

  function seed() {
    const n = Math.min(90, Math.round((W * H) / 16000));
    dots = Array.from({ length: n }, () => makeDot(false));
  }

  function step() {
    ctx.clearRect(0, 0, W, H);
    for (const d of dots) {
      d.x += d.vx;
      d.y += d.vy;
      if (d.y < -8) { d.y = H + 8; d.x = Math.random() * W; }
      if (d.x < -8) d.x = W + 8;
      if (d.x > W + 8) d.x = -8;
      ctx.beginPath();
      ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
      ctx.fillStyle = d.cyan
        ? `rgba(0, 229, 255, ${d.a.toFixed(3)})`
        : `rgba(255, 255, 255, ${(d.a * 0.8).toFixed(3)})`;
      ctx.fill();
    }
    raf = requestAnimationFrame(step);
  }

  function start() {
    if (running || document.hidden) return;
    running = true;
    raf = requestAnimationFrame(step);
  }

  function stop() {
    running = false;
    if (raf) cancelAnimationFrame(raf);
    raf = 0;
  }

  document.addEventListener('visibilitychange', () => (document.hidden ? stop() : start()));
  window.addEventListener('resize', () => { resize(); });
  document.documentElement.addEventListener('ab:burst', () => {
    dots.push(...Array.from({ length: 36 }, () => makeDot(true)));
  });

  resize();
  start();
})();
