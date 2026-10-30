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

  /* Frozen enrichment curves of RH_Auto_5000_L64_s5 (assets.npz →
     enrichment_curves.json), embedded rounded to 4 decimals so the panel
     also works offline. Full precision lives in the dashboard tabs. */
  const FROZEN_CURVES = {"meta":{"run":"RH_Auto_5000_L64_s5","generated":"2026-10-17","source":"results/RH_Sweep_Pro_Enrichment/data/assets.npz"},"r2":{"s":[0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95,2.0,2.05,2.1,2.15,2.2,2.25,2.3,2.35,2.4,2.45,2.5,2.55,2.6,2.65,2.7,2.75,2.8,2.85,2.9,2.95,3.0,3.05,3.1,3.15,3.2,3.25,3.3,3.35,3.4,3.45,3.5,3.55,3.6,3.65,3.7,3.75,3.8,3.85,3.9,3.95,4.0,4.05,4.1,4.15,4.2,4.25,4.3,4.35,4.4,4.45,4.5,4.55,4.6,4.65,4.7,4.75,4.8,4.85,4.9,4.95,5.0],"AB":[0.0,0.4922,0.583,0.6565,0.7108,0.7478,0.7719,0.7878,0.799,0.8073,0.8137,0.8183,0.821,0.8219,0.8207,0.8173,0.8121,0.8062,0.8016,0.8,0.8027,0.8092,0.8179,0.8267,0.8336,0.8376,0.8387,0.8375,0.835,0.8323,0.8303,0.8296,0.8305,0.8331,0.8369,0.8414,0.8459,0.8501,0.8538,0.8577,0.8628,0.8699,0.8794,0.8906,0.9017,0.9106,0.9154,0.9156,0.9119,0.9065,0.9022,0.9017,0.9061,0.9148,0.9256,0.9359,0.9437,0.9482,0.9496,0.9491,0.9478,0.947,0.9479,0.9509,0.9562,0.963,0.9702,0.9766,0.981,0.9826,0.9811,0.9769,0.9708,0.9639,0.9574,0.9527,0.9507,0.9522,0.9568,0.9635,0.9705,0.9767,0.9814,0.9848,0.9872,0.9889,0.9897,0.9891,0.987,0.9837,0.9796,0.9755,0.9717,0.9688,0.967,0.9667,0.9682,0.9717,0.9763,0.981,0.9844],"ZZ":[0.0,0.034,0.0544,0.083,0.1212,0.1698,0.2287,0.297,0.3732,0.455,0.54,0.6253,0.708,0.7849,0.853,0.9096,0.9532,0.9829,0.999,1.0028,0.9969,0.9846,0.9697,0.9555,0.9445,0.9382,0.9366,0.9391,0.945,0.9531,0.9627,0.9725,0.9816,0.9889,0.9934,0.995,0.9939,0.9907,0.986,0.9803,0.974,0.9675,0.9618,0.9579,0.9568,0.9591,0.9643,0.9712,0.9783,0.9843,0.9882,0.9897,0.989,0.9869,0.9845,0.9825,0.9814,0.9808,0.98,0.9786,0.9765,0.9739,0.9717,0.9703,0.97,0.9707,0.9722,0.9741,0.9763,0.9787,0.9813,0.9843,0.9878,0.9917,0.9954,0.9975,0.9966,0.9914,0.9821,0.9702,0.9584,0.9497,0.9465,0.9495,0.9581,0.9706,0.9847,0.9979,1.008,1.0134,1.0133,1.0082,0.9994,0.9884,0.9767,0.9654,0.9557,0.9489,0.9462,0.9483,0.955],"GUE":[0.0,0.0082,0.0325,0.0719,0.1249,0.1894,0.2632,0.3434,0.4272,0.5119,0.5947,0.6733,0.7454,0.8096,0.8647,0.9099,0.9453,0.9711,0.9881,0.9973,1.0,0.9978,0.992,0.9842,0.9757,0.9676,0.9608,0.9559,0.9532,0.953,0.955,0.9589,0.9642,0.9705,0.9771,0.9835,0.9892,0.9939,0.9973,0.9993,1.0,0.9994,0.9978,0.9955,0.9928,0.99,0.9875,0.9854,0.9841,0.9835,0.9838,0.9848,0.9864,0.9885,0.9909,0.9933,0.9955,0.9974,0.9988,0.9997,1.0,0.9997,0.999,0.9979,0.9966,0.9952,0.9939,0.9928,0.9921,0.9917,0.9917,0.9922,0.9929,0.994,0.9952,0.9964,0.9976,0.9986,0.9994,0.9998,1.0,0.9998,0.9994,0.9988,0.998,0.9972,0.9964,0.9957,0.9953,0.995,0.995,0.9952,0.9957,0.9963,0.997,0.9978,0.9985,0.9991,0.9996,0.9999,1.0],"POI":[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]},"k":{"t":[0.0,0.02,0.04,0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26,0.28,0.3,0.32,0.34,0.36,0.38,0.4,0.42,0.44,0.46,0.48,0.5,0.52,0.54,0.56,0.58,0.6,0.62,0.64,0.66,0.68,0.7,0.72,0.74,0.76,0.78,0.8,0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1.0,1.02,1.04,1.06,1.08,1.1,1.12,1.14,1.16,1.18,1.2,1.22,1.24,1.26,1.28,1.3,1.32,1.34,1.36,1.38,1.4,1.42,1.44,1.46,1.48,1.5,1.52,1.54,1.56,1.58,1.6,1.62,1.64,1.66,1.68,1.7,1.72,1.74,1.76,1.78,1.8,1.82,1.84,1.86,1.88,1.9,1.92,1.94,1.96,1.98,2.0],"AB":[0.0,0.1661,0.1829,0.2976,0.2913,0.5468,0.5612,0.74,0.8836,0.7035,0.9118,0.7358,0.934,1.4334,1.2386,0.8156,0.7507,0.7186,0.6759,0.7736,1.1224,0.752,0.827,0.9341,1.0481,0.9319,0.9146,0.9396,0.9351,0.9301,0.9771,0.9771,0.9769,1.0171,0.9851,0.988,0.9662,0.9844,0.965,0.973,0.9735,0.9355,0.9655,1.012,0.987,0.9889,0.9803,0.9983,0.9737,0.9948,1.0043,0.9911,0.9709,0.9314,0.8857,0.8766,0.8905,0.9172,0.9107,0.9101,0.8829,0.9124,0.9284,0.9455,0.9666,1.0181,1.0112,0.9928,1.0319,1.0494,1.0932,1.1005,1.0564,1.0705,1.071,1.0544,1.0026,1.0311,1.0632,1.0347,1.018,1.0051,1.0035,1.0205,1.0047,0.9731,0.9622,0.9733,0.9617,0.9735,0.9188,0.907,0.8882,0.9252,0.9404,0.9518,0.8586,0.9892,1.2146,1.1656,1.0217],"ZZ":[0.0,0.0008,0.0009,0.0012,0.0021,0.0241,0.1512,0.0409,0.046,0.1968,0.1593,0.1279,0.3981,0.2931,0.1276,0.3791,0.1666,0.2731,0.382,0.425,0.1643,0.3951,0.49,0.241,0.4905,0.4196,0.4417,0.4607,0.4705,0.5091,0.5223,0.5446,0.5461,0.5612,0.5914,0.5958,0.6128,0.6327,0.6718,0.6729,0.6741,0.6982,0.7428,0.758,0.7379,1.0974,1.0971,1.1024,1.1228,1.0845,1.1342,1.253,1.25,1.2013,1.2281,1.3018,0.9368,0.9843,1.0235,1.0332,1.1013,1.0776,0.9733,0.9718,1.0187,1.0548,1.0165,0.988,0.9604,0.9618,0.9769,0.9419,0.9686,0.9966,1.0264,1.0527,1.0505,1.0517,1.1035,1.0887,1.0601,1.0389,1.0387,0.9995,1.0107,0.9911,0.9415,0.8961,0.8867,0.8475,0.8538,0.9053,0.8999,0.9021,0.8983,0.8932,1.3122,0.8302,0.9988,0.7187,1.2107],"GUE":[0.0,0.02,0.04,0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26,0.28,0.3,0.32,0.34,0.36,0.38,0.4,0.42,0.44,0.46,0.48,0.5,0.52,0.54,0.56,0.58,0.6,0.62,0.64,0.66,0.68,0.7,0.72,0.74,0.76,0.78,0.8,0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],"POI":[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]},"s2":{"L":[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0,21.0,22.0,23.0,24.0,25.0,26.0,27.0,28.0,29.0,30.0,31.0,32.0,33.0,34.0,35.0,36.0,37.0,38.0,39.0,40.0,41.0,42.0,43.0,44.0,45.0,46.0,47.0,48.0,49.0,50.0,51.0,52.0,53.0,54.0,55.0,56.0,57.0,58.0,59.0,60.0,61.0,62.0,63.0,64.0,65.0,66.0,67.0,68.0,69.0,70.0,71.0,72.0,73.0,74.0,75.0,76.0,77.0,78.0,79.0,80.0,81.0,82.0,83.0,84.0,85.0,86.0,87.0,88.0,89.0,90.0,91.0,92.0,93.0,94.0,95.0,96.0,97.0,98.0,99.0,100.0],"AB":[0.6425,1.0502,1.3274,1.4939,1.6443,1.7053,1.7315,1.8141,1.8528,1.9052,1.995,2.0362,2.073,2.124,2.133,2.1537,2.1893,2.1746,2.1766,2.2143,2.2115,2.2402,2.2086,2.2704,2.2399,2.2394,2.2645,2.2386,2.2394,2.2314,2.2658,2.2725,2.2063,2.1872,2.214,2.2253,2.2129,2.1429,2.1487,2.2103,2.2033,2.1612,2.2193,2.1773,2.1888,2.1583,2.161,2.1737,2.1939,2.242,2.1818,2.1554,2.1377,2.1137,2.125,2.1165,2.1407,2.1616,2.1629,2.1234,2.0949,2.0456,2.0573,2.0204,2.0668,2.0256,1.9564,2.004,1.9776,1.997,1.9371,1.9334,1.9905,2.0035,1.9717,1.9683,1.916,1.9569,1.908,1.887,1.8699,1.9236,1.9193,1.8832,1.8701,1.8647,1.8536,1.8436,1.8626,1.8101,1.8054,1.776,1.8381,1.8039,1.8449,1.833,1.8396,1.8168,1.7858,1.8167],"ZZ":[0.2515,0.2816,0.2892,0.2779,0.2686,0.2637,0.2557,0.2544,0.2527,0.2534,0.2576,0.2664,0.2772,0.2998,0.2918,0.2599,0.2506,0.2543,0.2582,0.2665,0.2723,0.2812,0.2667,0.2646,0.2672,0.2734,0.266,0.2554,0.2581,0.2664,0.2744,0.2822,0.2765,0.2712,0.2621,0.255,0.2583,0.2603,0.2625,0.2677,0.2668,0.2693,0.2738,0.2678,0.2622,0.264,0.2554,0.2581,0.2647,0.2682,0.2755,0.2728,0.2659,0.2578,0.2585,0.2576,0.2538,0.2632,0.2623,0.2684,0.2685,0.2688,0.2686,0.2614,0.2529,0.2547,0.255,0.2574,0.2673,0.2718,0.2665,0.26,0.2536,0.2554,0.2529,0.2545,0.2607,0.2594,0.2633,0.2665,0.2579,0.2597,0.2545,0.2544,0.2577,0.2563,0.2619,0.2659,0.2644,0.2602,0.2545,0.2536,0.2574,0.258,0.2552,0.2563,0.2589,0.2573,0.2644,0.2554],"GUE":[0.0127,0.0829,0.124,0.1531,0.1757,0.1942,0.2098,0.2234,0.2353,0.246,0.2556,0.2644,0.2725,0.2801,0.287,0.2936,0.2997,0.3055,0.311,0.3162,0.3211,0.3259,0.3304,0.3347,0.3388,0.3428,0.3466,0.3503,0.3538,0.3573,0.3606,0.3638,0.3669,0.37,0.3729,0.3758,0.3785,0.3812,0.3839,0.3864,0.3889,0.3914,0.3938,0.3961,0.3984,0.4006,0.4028,0.4049,0.407,0.409,0.411,0.413,0.4149,0.4168,0.4187,0.4205,0.4223,0.4241,0.4258,0.4275,0.4292,0.4308,0.4325,0.434,0.4356,0.4372,0.4387,0.4402,0.4417,0.4431,0.4446,0.446,0.4474,0.4488,0.4501,0.4515,0.4528,0.4541,0.4554,0.4567,0.4579,0.4592,0.4604,0.4616,0.4628,0.464,0.4652,0.4663,0.4675,0.4686,0.4697,0.4708,0.4719,0.473,0.4741,0.4751,0.4762,0.4772,0.4782,0.4793],"POI":[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0,21.0,22.0,23.0,24.0,25.0,26.0,27.0,28.0,29.0,30.0,31.0,32.0,33.0,34.0,35.0,36.0,37.0,38.0,39.0,40.0,41.0,42.0,43.0,44.0,45.0,46.0,47.0,48.0,49.0,50.0,51.0,52.0,53.0,54.0,55.0,56.0,57.0,58.0,59.0,60.0,61.0,62.0,63.0,64.0,65.0,66.0,67.0,68.0,69.0,70.0,71.0,72.0,73.0,74.0,75.0,76.0,77.0,78.0,79.0,80.0,81.0,82.0,83.0,84.0,85.0,86.0,87.0,88.0,89.0,90.0,91.0,92.0,93.0,94.0,95.0,96.0,97.0,98.0,99.0,100.0]}};

  /* GUE (β=2) gap-ratio surmise, Atas–Bogomolny–Giraud–Roux Eq. (7):
     P(r) ∝ (r+r²)²/(1+r+r²)⁴ — mode (√5−1)/2 ≈ 0.618, ⟨r̃⟩_W = 0.60266,
     matching the suite's large-N reference 0.5996 to 0.5%. Drawn normalized
     to its own max, as before. */
  const GUE_PDF = (r) => Math.pow(r + r * r, 2) / Math.pow(1 + r + r * r, 4);

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
        ` · curve: GUE ratio surmise ∝ (r+r²)²/(1+r+r²)⁴ · ⟨r⟩ = ` +
        (ratios.reduce((a, b) => a + b, 0) / ratios.length).toFixed(4) +
        (live ? ' · dataset: frozen Odlyzko table, fetched from dashboard/data/' :
                ' · embedded fallback (first 300 zeros)');
      if (!live && note) {
        note.hidden = false;
        note.textContent = 'The live dataset was not reachable, so this panel used the embedded first 300 zeros. Open the dashboard for the full 50,000-zero computation.';
      }
    };

    /* ── view switcher: ratio histogram | R₂(s) | K(t) | Σ²(L) ──
       The three extra views draw the frozen enrichment curves of
       RH_Auto_5000_L64_s5 (results/RH_Sweep_Pro_Enrichment). Same axes
       discipline, same palette; nothing here recomputes the numerics. */
    const VIEWS = {
      ratio: {
        title: 'Spacing ratios of the ζ zeros vs the GUE law',
        legend: [['l1', 'zeros, live'], ['l2', 'GUE ratio law']],
        aria: 'Histogram of consecutive spacing ratios of the first five thousand zeta zeros against the GUE ratio law curve',
      },
      r2: {
        title: 'R₂(s) — two-level cluster function',
        aria: 'Two-level cluster function R2(s) of the AB-cloud, the zeta zeros, GUE and Poisson on a log-s axis',
      },
      k: {
        title: 'K(t) — spectral form factor',
        aria: 'Spectral form factor K(t) of the AB-cloud, the zeta zeros, GUE and Poisson on a log-t axis',
      },
      s2: {
        title: 'Σ²(L) — number variance',
        aria: 'Number variance Sigma2(L) of the AB-cloud, the zeta zeros, GUE and Poisson on a log-L axis',
      },
    };
    const SERIES_STYLE = [
      { stroke: '#00E5FF', name: 'AB-cloud' },
      { stroke: '#FF2EC4', name: 'ζ zeros' },
      { stroke: '#A78BFA', name: 'GUE' },
      { stroke: '#FFD60A', name: 'Poisson' },
    ];
    const tabs = Array.from(doc.querySelectorAll('.ev-tab'));
    const head = svg.closest('.evidence-card')?.querySelector('.evidence-title');
    const legend = svg.closest('.evidence-card')?.querySelector('.legend');
    if (!tabs.length) return;
    let active = 'ratio';

    const setLegend = (items) => {
      if (!legend) return;
      legend.innerHTML = '';
      for (const [cls, label] of items) {
        const span = doc.createElement('span');
        span.className = cls;
        const i = doc.createElement('i');
        span.appendChild(i);
        span.appendChild(doc.createTextNode(label));
        legend.appendChild(span);
      }
      // beyond l1/l2, recolor the markers to the 4-series palette
      const colors = ['#00E5FF', '#FF2EC4', '#A78BFA', '#FFD60A'];
      Array.from(legend.children).forEach((sp, idx) => {
        const dot = sp.querySelector('i');
        if (dot && !sp.className) dot.style.background = colors[idx % colors.length];
      });
    };

    const drawFrozen = (view) => {
      const c = FROZEN_CURVES[view];
      if (!c) return;
      const grid = c.s || c.t || c.L;
      if (!grid) return;
      const xs = grid.filter((v) => v != null);
      const logX = view === 's2'; // L = 1..100 — log reads better; s,t start at 0
      // Σ²(L) spans 0.25…100 with the Poisson line L — linear Y would crush
      // the physics into the floor; number variance is presented log-log.
      const logY = view === 's2';
      const xMin = logX ? Math.log10(Math.min(...xs)) : Math.min(...xs);
      const xMax = logX ? Math.log10(Math.max(...xs)) : Math.max(...xs);
      const series = ['AB', 'ZZ', 'GUE', 'POI']
        .map((k, i) => ({ k, i, pts: c[k] }))
        .filter((s) => Array.isArray(s.pts));
      const allVals = series.flatMap((s) => s.pts.filter((v) => v != null));
      const yMax0 = Math.max(...allVals);
      let yMin0 = 0, yMax = yMax0 * 1.06;
      if (logY) {
        yMin0 = Math.min(...allVals.filter((v) => v > 0)) * 0.7;
        yMax = yMax0 * 1.3;
      }
      const X = (v) => pad.l + ((logX ? Math.log10(v) : v) - xMin) / (xMax - xMin || 1) * plotW;
      const Y = (v) => {
        const a = logY ? Math.log10(Math.max(v, yMin0)) : v;
        return H - pad.b - (a - (logY ? Math.log10(yMin0) : 0))
          / ((logY ? Math.log10(yMax) : yMax) - (logY ? Math.log10(yMin0) : 0) || 1) * plotH;
      };
      const yTickVals = logY
        ? [0.001, 0.01, 0.1, 1, 10, 100, 1000].filter((v) => v >= yMin0 && v <= yMax)
        : [yMax, yMax / 2, 0];
      const xTickVals = [0, 1, 2, 3, 4].map((i) => {
        const v = xMin + ((xMax - xMin) * i) / 4;
        return { pos: pad.l + (plotW * i) / 4, label: (logX ? Math.pow(10, v) : v) };
      });

      svg.appendChild(el('line', { x1: pad.l, y1: H - pad.b, x2: W - pad.r, y2: H - pad.b, class: 'axis' }));
      svg.appendChild(el('line', { x1: pad.l, y1: pad.t, x2: pad.l, y2: H - pad.b, class: 'axis' }));
      for (const tk of xTickVals) {
        svg.appendChild(el('line', { x1: tk.pos, y1: H - pad.b, x2: tk.pos, y2: H - pad.b + 4, class: 'axis' }));
        const t = el('text', { x: tk.pos, y: H - pad.b + 16, 'text-anchor': 'middle' });
        t.textContent = Number(tk.label.toPrecision(3)).toString();
        svg.appendChild(t);
      }
      for (const v of yTickVals) {
        const t = el('text', { x: pad.l - 6, y: Y(v) + 3, 'text-anchor': 'end' });
        t.textContent = Number(v.toPrecision(3)).toString();
        svg.appendChild(t);
      }
      for (const s of series) {
        const style = SERIES_STYLE[s.i % SERIES_STYLE.length];
        const pts = [];
        for (let i = 0; i < grid.length; i++) {
          const xv = grid[i], yv = s.pts[i];
          if (xv == null || yv == null) continue;
          pts.push(`${X(xv).toFixed(1)},${Y(yv).toFixed(1)}`);
        }
        svg.appendChild(el('polyline', {
          points: pts.join(' '), fill: 'none',
          stroke: style.stroke, 'stroke-width': '1.6',
        }));
      }
      // in-chart series labels (left to right, staggered rows)
      series.forEach((s, i) => {
        const style = SERIES_STYLE[s.i % SERIES_STYLE.length];
        const t = el('text', {
          x: pad.l + 10 + (i % 2) * 150, y: pad.t + 14 + Math.floor(i / 2) * 16,
          fill: style.stroke,
        });
        t.textContent = style.name;
        svg.appendChild(t);
      });
      cap.textContent = 'Frozen curves of ' + FROZEN_CURVES.meta.run +
        ' (' + FROZEN_CURVES.meta.generated + '), source ' + FROZEN_CURVES.meta.source +
        ' · full precision and the Δ₃(L), p(s), E(s) views in the dashboard';
      if (note) note.hidden = true;
    };

    const show = (view) => {
      active = tabs.some((b) => b.dataset.view === view) ? view : 'ratio';
      tabs.forEach((b) => {
        const on = b.dataset.view === active;
        b.classList.toggle('active', on);
        b.setAttribute('aria-selected', String(on));
      });
      const v = VIEWS[active];
      if (head && v && v.title) head.textContent = v.title;
      if (v && v.legend) setLegend(v.legend);
      else if (legend) setLegend([['', 'AB-cloud'], ['', 'ζ zeros'], ['', 'GUE'], ['', 'Poisson']]);
      if (v && v.aria) svg.setAttribute('aria-label', v.aria);
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      if (active === 'ratio') {
        if (currentZeros) draw(currentZeros, currentLive);
        // else: keep the "Loading the frozen Odlyzko dataset…" caption
      } else {
        drawFrozen(active);
      }
    };

    let currentZeros = null, currentLive = false;
    tabs.forEach((b) => b.addEventListener('click', () => show(b.dataset.view)));
    show('ratio');
    loadZeros().then(({ zeros, live }) => {
      currentZeros = zeros; currentLive = live;
      if (active === 'ratio') {
        while (svg.firstChild) svg.removeChild(svg.firstChild);
        draw(zeros, live);
      }
    });
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
