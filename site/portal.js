/**
 * portal.js — interaction & motion layer for the AB-Cloud portal landing.
 *
 * Zero dependencies, CSP-safe (external file, script-src 'self'), fully
 * progressive: every feature degrades gracefully and every init is wrapped
 * in try/catch so no single failure can blank the page.
 *
 * Features
 *   • floating navigation: scrollspy (aria-current) + mobile full-height
 *     menu with staggered link entrance (B7 navigation rules)
 *   • reveal-on-scroll via IntersectionObserver, once per section (B7)
 *   • tagline reveal: per-word color activation on a trigger line (B11)
 *   • evidence panel: spacing-ratio histogram of the ζ zeros vs the GUE
 *     ratio law, computed in the browser from the SAME frozen dataset the
 *     dashboard uses (fetch) with an embedded fallback of the first zeros
 *   • count-up animation for the numbers strip
 *   • "copy BibTeX" button for instant citation
 *   • live API status dot (probes /api/health)
 *   • Konami-code easter egg → dispatches 'ab:burst' (particles.js responds)
 */
(() => {
  'use strict';

  const doc = document;
  const root = doc.documentElement;
  root.classList.remove('no-js');
  root.classList.add('js');

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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

  /* ── 1. navigation: mobile menu + scrollspy ─────────────────────────── */
  function initMenu() {
    const btn = doc.getElementById('menuBtn');
    const menu = doc.getElementById('mobileMenu');
    if (!btn || !menu) return;
    const setState = (open) => {
      doc.body.classList.toggle('menu-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      doc.body.style.overflow = open ? 'hidden' : '';
    };
    btn.addEventListener('click', () => setState(!doc.body.classList.contains('menu-open')));
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) setState(false); });
    doc.addEventListener('keydown', (e) => { if (e.key === 'Escape') setState(false); });
  }

  function initScrollSpy() {
    const links = Array.from(doc.querySelectorAll('.nav a.link[data-spy]'));
    if (!links.length || !('IntersectionObserver' in window)) return;
    const byId = new Map(links.map((a) => [a.getAttribute('href').slice(1), a]));
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) {
        const link = byId.get(e.target.id);
        if (!link) continue;
        if (e.isIntersecting) {
          links.forEach((a) => a.removeAttribute('aria-current'));
          link.setAttribute('aria-current', 'true');
        }
      }
    }, { rootMargin: '-40% 0px -55% 0px' });
    byId.forEach((_, id) => {
      const sec = doc.getElementById(id);
      if (sec) io.observe(sec);
    });
  }

  /* ── 2. reveal on scroll (once, B7) ─────────────────────────────────── */
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

  /* ── 3. tagline reveal: word by word on a trigger line (B11) ────────── */
  function initTaglineReveal() {
    const el = doc.getElementById('taglineReveal');
    if (!el) return;
    const words = el.textContent.trim().split(/\s+/);
    el.textContent = '';
    const spans = words.map((w) => {
      const s = doc.createElement('span');
      s.className = 'w';
      s.textContent = w;
      el.appendChild(s);
      el.appendChild(doc.createTextNode(' '));
      return s;
    });
    if (reduceMotion || !('IntersectionObserver' in window)) {
      spans.forEach((s) => s.classList.add('on'));
      return;
    }
    // each word activates individually as it crosses a trigger line
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) {
        if (e.isIntersecting) {
          e.target.classList.add('on');
          io.unobserve(e.target);
        }
      }
    }, { rootMargin: '-35% 0px -35% 0px', threshold: 0 });
    spans.forEach((s) => io.observe(s));
  }

  /* ── 4. evidence panel: spacing ratios vs GUE ratio law ─────────────── */
  // First 300 zeros, embedded as an offline fallback. The live path fetches
  // the full 50,000-zero dataset the dashboard itself ships.
  const FALLBACK_ZEROS = [
  14.134725141734695,
  21.022039638771556,
  25.01085758014569,
  30.424876125859512,
  32.93506158773919,
  37.586178158825675,
  40.9187190121475,
  43.327073280915,
  48.00515088116716,
  49.7738324776723,
  52.970321477714464,
  56.44624769706339,
  59.34704400260235,
  60.83177852460981,
  65.1125440480816,
  67.07981052949417,
  69.54640171117398,
  72.0671576744819,
  75.70469069908393,
  77.1448400688748,
  79.33737502024937,
  82.91038085408603,
  84.73549298051705,
  87.42527461312523,
  88.80911120763446,
  92.49189927055849,
  94.65134404051989,
  95.87063422824531,
  98.83119421819369,
  101.31785100573138,
  103.72553804047834,
  105.44662305232609,
  107.1686111842764,
  111.02953554316967,
  111.87465917699264,
  114.32022091545271,
  116.22668032085755,
  118.79078286597621,
  121.37012500242065,
  122.94682929355258,
  124.25681855434577,
  127.5166838795965,
  129.57870419995606,
  131.08768853093267,
  133.4977372029976,
  134.75650975337388,
  138.11604205453344,
  139.7362089521214,
  141.12370740402113,
  143.11184580762063,
  146.0009824867655,
  147.42276534255961,
  150.05352042078488,
  150.92525761224147,
  153.0246938111989,
  156.11290929423788,
  157.59759181759406,
  158.8499881714205,
  161.18896413759603,
  163.030709687182,
  165.5370691879004,
  167.1844399781745,
  169.09451541556882,
  169.9119764794117,
  173.41153651959155,
  174.75419152336573,
  176.44143429771043,
  178.37740777609997,
  179.916484020257,
  182.20707848436646,
  184.8744678483875,
  185.59878367770747,
  187.22892258350186,
  189.41615865601693,
  192.0266563607138,
  193.0797266038457,
  195.26539667952923,
  196.87648184095832,
  198.01530967625192,
  201.2647519437038,
  202.49359451414054,
  204.18967180310455,
  205.3946972021633,
  207.90625888780622,
  209.57650971685626,
  211.6908625953653,
  213.34791935971268,
  214.54704478349143,
  216.1695385082637,
  219.0675963490214,
  220.714918839314,
  221.43070555469333,
  224.00700025460432,
  224.9833246695823,
  227.4214442796793,
  229.33741330552536,
  231.25018870049917,
  231.98723525318024,
  233.6934041789083,
  236.5242296658162,
  237.7698204809252,
  239.55547757332764,
  241.04915779621658,
  242.8232719342226,
  244.07089849707816,
  247.1369900748975,
  248.10199006014847,
  249.5736896447072,
  251.014947795016,
  253.06998674799948,
  255.30625645491403,
  256.38071369443446,
  258.6104394915314,
  259.874406989678,
  260.8050845045969,
  263.57389390487015,
  265.55785183887633,
  266.6149737815011,
  267.92191508282406,
  269.9704490239976,
  271.494055641645,
  273.4596091884033,
  275.58749264934386,
  276.4520495031329,
  278.25074352984194,
  279.22925092774517,
  282.4651147650521,
  283.2111857332339,
  284.83596398090475,
  286.6674453630029,
  287.9119205014222,
  289.5798549292188,
  291.8462913290674,
  293.5584341393563,
  294.9653696192655,
  295.57325487895827,
  297.97927706194344,
  299.8403260537213,
  301.64932546219416,
  302.6967495896069,
  304.8643713408573,
  305.7289126020368,
  307.2194961281701,
  310.1094631467019,
  311.165141530356,
  312.4278011806009,
  313.9852857311589,
  315.47561608947575,
  317.7348059423702,
  318.8531042563166,
  321.1601343091136,
  322.14455867248296,
  323.4669695575121,
  324.8628660517396,
  327.44390126190547,
  329.03307168048093,
  329.9532397282339,
  331.4744675826634,
  333.64537852486984,
  334.2113548332444,
  336.84185042839067,
  338.3399928508066,
  339.85821672536355,
  341.04226111104657,
  342.0548775103636,
  344.6617029402523,
  346.34787056600993,
  347.2726775844205,
  349.31626087069617,
  350.4084193491921,
  351.87864902535927,
  353.4889004887188,
  356.0175749772649,
  357.1513022520396,
  357.95268510163226,
  359.74375495311443,
  361.28936169580464,
  363.33133057897385,
  364.736024114089,
  366.2127102883313,
  367.9935754817403,
  368.96843809573437,
  370.050919212106,
  373.06192837211285,
  373.86487391090856,
  375.82591276673935,
  376.32409223066804,
  378.4366802499655,
  379.87297534653237,
  381.4844686171865,
  383.44352944953647,
  384.95611681486366,
  385.86130084597426,
  387.222890222388,
  388.84612835423223,
  391.45608356363806,
  392.2450833395191,
  393.427743844434,
  395.5828700109937,
  396.3818542225922,
  397.9187362096142,
  399.9851198761949,
  401.8392286005332,
  402.86191776388614,
  404.236441800208,
  405.13438745990993,
  407.5814603868962,
  408.9472455023511,
  410.51386919336665,
  411.9722678042788,
  413.26273607018504,
  415.01880975515513,
  415.4552149962946,
  418.3877057895348,
  419.8613648181523,
  420.6438276250418,
  422.07671005882673,
  423.7165796274818,
  425.06988249446135,
  427.2088250840746,
  428.12791407661666,
  430.3287454309386,
  431.3013069307036,
  432.1386417345886,
  433.88921848092724,
  436.16100643264696,
  437.5816981676686,
  438.6217386562722,
  439.91844221437066,
  441.68319920118904,
  442.90454630260945,
  444.31933627755916,
  446.8606226964295,
  447.4417041944933,
  449.1485456850233,
  450.1269457803135,
  451.4033084453888,
  453.9867378066779,
  454.9746837686168,
  456.32842668924604,
  457.903893064103,
  459.513415281106,
  460.08794442217584,
  462.06536727488253,
  464.05728691054827,
  465.6715392113711,
  466.5702869308262,
  467.43904621026167,
  469.53600455911203,
  470.77365547810166,
  472.7991746619088,
  473.8352323451397,
  475.6003393693758,
  476.7690152374845,
  478.07526376667096,
  478.9421815346348,
  481.8303393762866,
  482.8347827909824,
  483.8514272124825,
  485.539148129356,
  486.52871826165125,
  488.38056709001745,
  489.66176157795616,
  491.398821593663,
  493.3144415817853,
  493.9579978053695,
  495.3588288221313,
  496.4296962157591,
  498.58078242968656,
  500.3090849416905,
  501.6044469651455,
  502.27627032711825,
  504.49977331342774,
  505.41523174224443,
  506.46415270952355,
  508.8007003364678,
  510.26422794367284,
  511.5622897003746,
  512.6231445314074,
  513.6689855554737,
  515.4350571672994,
  517.5896685724674,
  518.2342231475501,
  520.1063104117233,
  521.525193449492,
  522.4566961777302,
  523.9605308920159,
  525.0773856872796,
  527.9036416012724,
  528.4062138522927,
  529.8062263187069,
  530.866917883961,
  532.6881830282937,
  533.7796307537687,
  535.6643140758732,
  537.0697590831223,
  538.4285261762479,
  540.2131663762282,
  540.6313902472951,
  541.8474371212013,
];

  const GUE_PDF = (r) => (27 / 8) * Math.pow(r + r * r, 2) / Math.pow(1 + r + r * r, 5);

  async function loadZeros() {
    try {
      const ctrl = typeof AbortController !== 'undefined' ? new AbortController() : null;
      const timer = setTimeout(() => ctrl && ctrl.abort(), 8000);
      const res = await fetch('/dashboard/data/zeta_zeros_50000_embedded.txt', {
        cache: 'force-cache',
        signal: ctrl ? ctrl.signal : undefined,
      });
      clearTimeout(timer);
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const text = await res.text();
      const zeros = text.split('\n')
        .filter((l) => l && !l.startsWith('#'))
        .map(Number)
        .filter(Number.isFinite);
      if (zeros.length < 1000) throw new Error('dataset too short');
      return { zeros, live: true };
    } catch {
      return { zeros: FALLBACK_ZEROS, live: false };
    }
  }

  function spacingRatios(zeros, count) {
    const lam = zeros.slice(0, count).map(Math.abs).sort((a, b) => a - b);
    const d = [];
    for (let i = 1; i < lam.length; i++) d.push(lam[i] - lam[i - 1]);
    const r = [];
    for (let i = 0; i + 1 < d.length; i++) {
      const mn = Math.min(d[i], d[i + 1]), mx = Math.max(d[i], d[i + 1]);
      if (mx > 0) r.push(mn / mx);
    }
    return r;
  }

  function initEvidence() {
    const svg = doc.getElementById('ratioChart');
    const cap = doc.getElementById('evidenceCap');
    const note = doc.getElementById('evidenceNote');
    if (!svg || !cap) return;
    const NS = 'http://www.w3.org/2000/svg';
    const W = 640, H = 280, pad = { l: 44, r: 12, t: 12, b: 28 };
    const plotW = W - pad.l - pad.r, plotH = H - pad.t - pad.b;
    const BINS = 40;

    const el = (name, attrs) => {
      const n = doc.createElementNS(NS, name);
      for (const k in attrs) n.setAttribute(k, attrs[k]);
      return n;
    };

    const draw = (zeros, live) => {
      const ratios = spacingRatios(zeros, Math.min(5000, zeros.length));
      if (ratios.length < 50) {
        cap.textContent = 'The spacing histogram needs at least a few hundred zeros — none available offline.';
        return;
      }
      const bins = new Array(BINS).fill(0);
      for (const r of ratios) bins[Math.min(BINS - 1, Math.floor(r * BINS))]++;
      const maxBin = Math.max(...bins);

      // axes
      svg.appendChild(el('line', { x1: pad.l, y1: H - pad.b, x2: W - pad.r, y2: H - pad.b, class: 'axis' }));
      svg.appendChild(el('line', { x1: pad.l, y1: pad.t, x2: pad.l, y2: H - pad.b, class: 'axis' }));
      for (let i = 0; i <= 4; i++) {
        const x = pad.l + (plotW * i) / 4;
        svg.appendChild(el('line', { x1: x, y1: H - pad.b, x2: x, y2: H - pad.b + 4, class: 'axis' }));
        const t = el('text', { x, y: H - pad.b + 16, 'text-anchor': 'middle' });
        t.textContent = (i / 4).toFixed(2);
        svg.appendChild(t);
      }
      for (let i = 0; i <= 2; i++) {
        const v = Math.round((maxBin * i) / 2);
        const y = H - pad.b - (plotH * i) / 2;
        const t = el('text', { x: pad.l - 6, y: y + 3, 'text-anchor': 'end' });
        t.textContent = String(v);
        svg.appendChild(t);
      }

      // bars
      const bw = plotW / BINS;
      bins.forEach((c, i) => {
        if (!c) return;
        const h = (c / maxBin) * plotH;
        svg.appendChild(el('rect', {
          x: pad.l + i * bw + 0.5, y: H - pad.b - h,
          width: Math.max(1, bw - 1.5), height: h, class: 'bar',
        }));
      });

      // GUE ratio-law curve: pdf normalized to its own max, stretched to the plot height
      const steps = 160;
      let maxPdf = 0;
      const pdf = [];
      for (let i = 0; i <= steps; i++) {
        const r = i / steps;
        const p = GUE_PDF(r);
        pdf.push(p);
        if (p > maxPdf) maxPdf = p;
      }
      const curve = pdf.map((p, i) => [
        pad.l + (i / steps) * plotW,
        H - pad.b - (p / maxPdf) * plotH,
      ]);
      svg.appendChild(el('polyline', {
        points: curve.map(([x, y]) => `${x.toFixed(1)},${y.toFixed(1)}`).join(' '),
        class: 'gue',
      }));

      cap.textContent = `r = min/max of consecutive spacings, first ${ratios.length.toLocaleString('en-US')} zeros` +
        ` · curve: GUE ratio law 27/8·(r+r²)²/(1+r+r²)⁵ · ⟨r⟩ = ` +
        (ratios.reduce((a, b) => a + b, 0) / ratios.length).toFixed(4) +
        (live ? ' · dataset: frozen Odlyzko table, fetched from dashboard/data/' :
                ' · embedded fallback (first 300 zeros)');
      if (!live && note) {
        note.hidden = false;
        note.textContent = 'The live dataset was not reachable, so this panel used the embedded first 300 zeros. Open the dashboard for the full 50,000-zero computation.';
      }
    };

    loadZeros().then(({ zeros, live }) => draw(zeros, live));
  }

  /* ── 5. count-up stats ──────────────────────────────────────────────── */
  function initCountUp() {
    const nums = Array.from(doc.querySelectorAll('.stat-card .v[data-count]'));
    if (!nums.length || reduceMotion || !('IntersectionObserver' in window)) return;
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) {
        if (!e.isIntersecting) continue;
        io.unobserve(e.target);
        const el = e.target;
        const target = Number(el.getAttribute('data-count')) || 0;
        const t0 = performance.now();
        const DUR = 1400;
        const tick = (t) => {
          const k = Math.min(1, (t - t0) / DUR);
          const eased = 1 - Math.pow(1 - k, 3);
          el.textContent = String(Math.round(target * eased));
          if (k < 1) requestAnimationFrame(tick);
          else el.textContent = String(target);
        };
        requestAnimationFrame(tick);
      }
    }, { threshold: 0.5 });
    nums.forEach((el) => io.observe(el));
  }

  /* ── 6. share + BibTeX ──────────────────────────────────────────────── */
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
    const ta = doc.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    doc.body.appendChild(ta);
    ta.select();
    try { doc.execCommand('copy'); } finally { ta.remove(); }
  }

  function initCite() {
    const cite = doc.getElementById('btnCite');
    if (!cite) return;
    cite.addEventListener('click', async () => {
      try {
        await copyText(BIBTEX);
        toast('BibTeX copied — cite the zeros');
      } catch {
        toast('clipboard unavailable in this browser');
      }
    });
  }

  /* ── 7. API status dot ──────────────────────────────────────────────── */
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

  /* ── 8. Konami easter egg → γ-burst ─────────────────────────────────── */
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
  [initMenu, initScrollSpy, initReveal, initTaglineReveal, initEvidence, initCountUp, initCite, initApiStatus, initKonami]
    .forEach((fn) => { try { fn(); } catch (err) { /* one feature must never break the page */ } });
})();
