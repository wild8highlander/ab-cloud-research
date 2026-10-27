/**
 * portal.js — interaction & motion layer for the AB-Cloud portal landing.
 *
 * Zero dependencies, CSP-safe (external file, script-src 'self'), fully
 * progressive: every feature degrades gracefully and every init is wrapped
 * in try/catch so no single failure can blank the page.
 *
 * Features
 *   • light/dark theme toggle (persisted, syncs theme-color + particles)
 *   • scroll progress bar + back-to-top button with progress ring
 *   • reveal-on-scroll via IntersectionObserver (with no-JS fallback)
 *   • count-up animation for the stats strip
 *   • subtle 3D tilt on the app cards (pointer devices only)
 *   • hero mouse-parallax on the background glow
 *   • Web Share API button (fallback: copy URL + toast)
 *   • "copy BibTeX" button for instant citation
 *   • live API status dot (probes /api/health)
 *   • Konami-code easter egg → dispatches 'ab:burst' (particles.js responds)
 */
(() => {
  'use strict';

  const doc = document;
  const root = doc.documentElement;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* ── toast ──────────────────────────────────────────────────────────── */
  const toastEl = doc.getElementById('toast');
  let toastTimer = 0;
  function toast(message) {
    if (!toastEl) return;
    toastEl.textContent = message;
    toastEl.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove('show'), 2400);
  }

  /* ── 1. theme ───────────────────────────────────────────────────────── */
  const THEME_KEY = 'ab-theme';
  const THEME_COLORS = { dark: '#05060f', light: '#eef3f9' };

  function applyTheme(theme) {
    if (theme === 'light') root.setAttribute('data-theme', 'light');
    else root.removeAttribute('data-theme');
    const meta = doc.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', THEME_COLORS[theme] ?? THEME_COLORS.dark);
    const btn = doc.getElementById('themeToggle');
    if (btn) btn.setAttribute('aria-pressed', String(theme === 'light'));
    root.dispatchEvent(new CustomEvent('ab:theme', { detail: { theme } }));
  }

  function initTheme() {
    let stored = null;
    try { stored = localStorage.getItem(THEME_KEY); } catch { /* storage blocked */ }
    applyTheme(stored === 'light' ? 'light' : 'dark');

    const btn = doc.getElementById('themeToggle');
    if (!btn) return;
    btn.addEventListener('click', () => {
      const next = root.hasAttribute('data-theme') && root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      applyTheme(next);
      try { localStorage.setItem(THEME_KEY, next); } catch { /* ignore */ }
    });
  }

  /* ── 2. scroll progress + back-to-top ───────────────────────────────── */
  function initScrollWidgets() {
    const bar = doc.getElementById('progress');
    const toTop = doc.getElementById('toTop');
    const ring = toTop ? toTop.querySelector('.ring-fg') : null;
    let ticking = false;

    const update = () => {
      ticking = false;
      const max = root.scrollHeight - window.innerHeight;
      const p = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
      if (bar) bar.style.transform = `scaleX(${p})`;
      if (toTop) toTop.classList.toggle('show', window.scrollY > 480);
      if (ring) ring.style.strokeDashoffset = String(100 - p * 100);
    };
    const onScroll = () => {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    update();

    if (toTop) {
      toTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
      });
    }
  }

  /* ── 3. reveal on scroll ────────────────────────────────────────────── */
  function initReveal() {
    const items = Array.from(doc.querySelectorAll('[data-reveal]'));
    if (!items.length) return;
    if (reduceMotion || !('IntersectionObserver' in window)) {
      items.forEach((el) => el.classList.add('in'));
      return;
    }
    const io = new IntersectionObserver(
      (entries) => {
        for (const e of entries) {
          if (e.isIntersecting) {
            e.target.classList.add('in');
            io.unobserve(e.target);
          }
        }
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' },
    );
    items.forEach((el) => io.observe(el));
  }

  /* ── 4. count-up stats ──────────────────────────────────────────────── */
  function initCountUp() {
    const nums = Array.from(doc.querySelectorAll('.stat .n[data-count]'));
    if (!nums.length || reduceMotion || !('IntersectionObserver' in window)) return;

    const fmt = (value, format) => {
      if (format === 'space') {
        // 50000 → "50 000" (thin-friendly regular space, as designed)
        return String(Math.round(value)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
      }
      return String(Math.round(value));
    };

    const io = new IntersectionObserver(
      (entries) => {
        for (const e of entries) {
          if (!e.isIntersecting) continue;
          io.unobserve(e.target);
          const el = e.target;
          const target = Number(el.getAttribute('data-count')) || 0;
          const format = el.getAttribute('data-format');
          const t0 = performance.now();
          const DUR = 1400;
          const tick = (t) => {
            const k = Math.min(1, (t - t0) / DUR);
            const eased = 1 - Math.pow(1 - k, 3); // easeOutCubic
            el.textContent = fmt(target * eased, format);
            if (k < 1) requestAnimationFrame(tick);
            else el.textContent = fmt(target, format);
          };
          requestAnimationFrame(tick);
        }
      },
      { threshold: 0.5 },
    );
    nums.forEach((el) => io.observe(el));
  }

  /* ── 5. 3D tilt on cards ────────────────────────────────────────────── */
  function initTilt() {
    if (!canHover || reduceMotion) return;
    const MAX = 5; // degrees
    doc.querySelectorAll('.card').forEach((card) => {
      card.addEventListener('pointermove', (ev) => {
        const r = card.getBoundingClientRect();
        const px = (ev.clientX - r.left) / r.width - 0.5;
        const py = (ev.clientY - r.top) / r.height - 0.5;
        card.style.setProperty('--ry', `${(px * MAX * 2).toFixed(2)}deg`);
        card.style.setProperty('--rx', `${(-py * MAX * 2).toFixed(2)}deg`);
      });
      card.addEventListener('pointerleave', () => {
        card.style.setProperty('--rx', '0deg');
        card.style.setProperty('--ry', '0deg');
      });
    });
  }

  /* ── 6. hero mouse-parallax on the glow ─────────────────────────────── */
  function initParallax() {
    if (!canHover || reduceMotion) return;
    let raf = 0;
    window.addEventListener('pointermove', (ev) => {
      if (raf) return;
      raf = requestAnimationFrame(() => {
        raf = 0;
        const dx = (ev.clientX / window.innerWidth - 0.5) * 28;
        const dy = (ev.clientY / window.innerHeight - 0.5) * 18;
        root.style.setProperty('--mx', `${dx.toFixed(1)}px`);
        root.style.setProperty('--my', `${dy.toFixed(1)}px`);
      });
    }, { passive: true });
  }

  /* ── 7. share + BibTeX ──────────────────────────────────────────────── */
  const BIBTEX = `@misc{abcloud2026,
  author       = {Isaev, Iskhak Khamzatovich},
  title        = {{AB-Cloud Research}: A Phase Resonator for the {Riemann zeta} Zeros},
  year         = {2026},
  howpublished = {\\url{https://github.com/wild8highlander/ab-cloud-research}},
  doi          = {10.5281/zenodo.21825394},
  note         = {Hilbert-P\\'olya program on a Hofstadter lattice; GUE universality verified in-browser}
}`;

  async function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }
    // fallback for non-secure contexts
    const ta = doc.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    doc.body.appendChild(ta);
    ta.select();
    try { doc.execCommand('copy'); } finally { ta.remove(); }
  }

  function initActions() {
    const share = doc.getElementById('btnShare');
    if (share) {
      share.addEventListener('click', async () => {
        const data = {
          title: doc.title,
          text: 'AB-Cloud Research — a phase resonator for the Riemann ζ zeros',
          url: location.origin + '/',
        };
        try {
          if (navigator.share) {
            await navigator.share(data);
            return;
          }
          throw new Error('no-share');
        } catch (err) {
          if (err && err.name === 'AbortError') return; // user closed the sheet
          try {
            await copyText(data.url);
            toast('link copied to clipboard');
          } catch {
            toast('could not share — copy the URL from the address bar');
          }
        }
      });
    }

    const cite = doc.getElementById('btnCite');
    if (cite) {
      cite.addEventListener('click', async () => {
        try {
          await copyText(BIBTEX);
          toast('BibTeX copied — cite the zeros');
        } catch {
          toast('clipboard unavailable in this browser');
        }
      });
    }
  }

  /* ── 8. API status dot ──────────────────────────────────────────────── */
  function initApiStatus() {
    const el = doc.getElementById('apiStatus');
    if (!el) return;
    const setState = (state, label) => {
      el.setAttribute('data-state', state);
      const l = el.querySelector('.api-label');
      if (l) l.textContent = label;
    };
    const controller = typeof AbortController !== 'undefined' ? new AbortController() : null;
    const timer = setTimeout(() => controller && controller.abort(), 5000);
    fetch('/api/health', { cache: 'no-store', signal: controller ? controller.signal : undefined })
      .then((res) => {
        clearTimeout(timer);
        setState(res.ok ? 'ok' : 'down', res.ok ? 'api online' : 'api degraded');
      })
      .catch(() => {
        clearTimeout(timer);
        setState('down', 'api offline');
      });
  }

  /* ── 9. Konami easter egg → γ-burst ─────────────────────────────────── */
  function initKonami() {
    const SEQ = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
    let idx = 0;
    window.addEventListener('keydown', (ev) => {
      const key = ev.key.length === 1 ? ev.key.toLowerCase() : ev.key;
      idx = key === SEQ[idx] ? idx + 1 : key === SEQ[0] ? 1 : 0;
      if (idx === SEQ.length) {
        idx = 0;
        root.dispatchEvent(new CustomEvent('ab:burst'));
        toast('γ-burst — the zeros salute you');
      }
    });
  }

  /* ── boot (each feature isolated) ───────────────────────────────────── */
  [initTheme, initScrollWidgets, initReveal, initCountUp, initTilt, initParallax, initActions, initApiStatus, initKonami]
    .forEach((fn) => { try { fn(); } catch (err) { /* one feature must never break the page */ } });
})();
