#!/usr/bin/env node
/**
 * serve.mjs — zero-dependency server for the assembled AB-Cloud portal.
 *
 * This is the platform-agnostic fallback start command (`npm start`) used
 * when the portal runs as a Web Service instead of a Pxxl Static App. It
 * mirrors EVERY rule from pxxl.toml so both deployment targets behave
 * identically:
 *
 *   • redirect rules        (/dashboard → /dashboard/, /index.html → /, …)
 *   • security headers      (CSP, HSTS, COOP, COEP, CORP, Permissions-Policy, …)
 *   • cache tiers           (immutable assets / data / icons / no-cache SW)
 *   • bot rewrites          (crawler UAs → server-rendered social cards)
 *   • mini-API              (JS ports of the api/*.ts Pxxl Functions:
 *                            /api/health, /api/version, /api/zeta, /api/og)
 *   • styled 404, traversal guard, HEAD support
 */
import { createServer } from 'node:http';
import { readFile, stat, realpath } from 'node:fs/promises';
import { extname, join, resolve, dirname, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..', 'dist');
const rootReal = await realpath(root).catch(() => root); // realpath base for the symlink guard
const port = Number(process.env.PORT) || 3000;

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webmanifest': 'application/manifest+json',
  '.txt': 'text/plain; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.csv': 'text/csv; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.ico': 'image/x-icon',
  '.webp': 'image/webp',
  '.wasm': 'application/wasm',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.map': 'application/json',
};

// ── security headers — mirrors the universal [[headers]] rule ───────────
const CSP =
  "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; " +
  "img-src 'self' data: blob:; font-src 'self'; connect-src 'self'; " +
  "worker-src 'self' blob:; manifest-src 'self'; object-src 'none'; " +
  "base-uri 'self'; form-action 'self'; frame-ancestors 'self'; upgrade-insecure-requests";

const SECURITY = {
  'content-security-policy': CSP,
  'strict-transport-security': 'max-age=63072000; includeSubDomains',
  'x-content-type-options': 'nosniff',
  'x-frame-options': 'SAMEORIGIN',
  'referrer-policy': 'strict-origin-when-cross-origin',
  'cross-origin-opener-policy': 'same-origin',
  'cross-origin-resource-policy': 'same-origin',
  'cross-origin-embedder-policy': 'credentialless',
  'permissions-policy':
    'camera=(), microphone=(), geolocation=(), gyroscope=(), magnetometer=(), payment=(), usb=(), interest-cohort=()',
};
const hdr = (extra) => ({ ...SECURITY, ...extra });

// ── redirect rules — mirrors [[redirects]] in pxxl.toml ─────────────────
const REDIRECTS = [
  { source: '/dashboard', destination: '/dashboard/', status: 308 },
  { source: '/lab3d', destination: '/lab3d/', status: 308 },
  { source: '/index.html', destination: '/', status: 308 },
  { source: '/lab', destination: '/lab3d/', status: 308 },
  { source: '/d', destination: '/dashboard/', status: 308 },
  { source: '/l', destination: '/lab3d/', status: 308 },
  { source: '/health', destination: '/api/health', status: 307 },
  { source: '/zeta', destination: '/api/zeta', status: 307 },
  { source: '/orcid', destination: 'https://orcid.org/0009-0003-7299-0701', status: 307 },
  { source: '/github', destination: 'https://github.com/wild8highlander/ab-cloud-research', status: 307 },
  { source: '/doi', destination: 'https://doi.org/10.5281/zenodo.21825394', status: 307 },
];

// ── cache tiers — mirrors the per-class [[headers]] rules ────────────────
function cacheControlFor(pathname) {
  if (/^\/(dashboard|lab3d)\/assets\//.test(pathname)) return 'public, max-age=31536000, immutable';
  if (/^\/dashboard\/data\//.test(pathname)) return 'public, max-age=300, stale-while-revalidate=86400';
  if (pathname === '/og-cover.png' || /^\/icon-/.test(pathname) || pathname === '/apple-touch-icon.png' || pathname === '/favicon.svg')
    return 'public, max-age=604800';
  if (/^\/screenshots\//.test(pathname)) return 'public, max-age=604800';
  if (pathname === '/portal.js' || pathname === '/particles.js') return 'public, max-age=300, stale-while-revalidate=86400';
  if (pathname === '/manifest.json' || pathname === '/sitemap.xml') return 'public, max-age=3600';
  if (pathname === '/robots.txt') return 'public, max-age=86400';
  if (pathname === '/sw.js') return 'public, max-age=0, must-revalidate';
  return 'no-cache';
}

// ── bot-aware social previews — mirrors the [[rewrites]] rules ───────────
const BOT_RE =
  /(twitterbot|whatsapp|telegrambot|discordbot|facebookexternalhit|linkedinbot|slurp|bingbot|googlebot)/i;

const OG_CARDS = {
  '/': {
    title: 'AB-Cloud Research — Phase Resonator for the Riemann ζ Zeros',
    description:
      'A topological vortex on a Hofstadter lattice encoding Aharonov–Bohm phases from the zeros of the Riemann zeta function. Interactive verification dashboard and 3D laboratory.',
  },
  '/dashboard': {
    title: 'AB-Cloud — Verification Dashboard',
    description:
      'The two-pass verdict table for the Hilbert–Pólya program: 39 tests, Julia 1.12, 50 000 Odlyzko zeros, live ζ statistics (b(N), KS vs GUE, Σ²(L), Δ₃(L)) computed in a Web Worker.',
  },
  '/lab3d': {
    title: 'AB-Cloud — 3D Laboratory',
    description:
      'Interactive WebGL scenes of experiments 3D-1…3D-34: the Hofstadter lattice with vortex flux cones, the Dirac cone at α = 1/2, and the ζ critical strip with the embedded zeros γ₁…γ₁₅.',
  },
};

function escapeHtml(s) {
  return s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
}

function ogHtml(origin, route) {
  const card = OG_CARDS[route] ?? OG_CARDS['/'];
  const cover = `${origin}/og-cover.png`;
  const pageUrl = route === '/' ? `${origin}/` : `${origin}${route}/`;
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex,follow" />
  <title>${escapeHtml(card.title)}</title>
  <meta name="description" content="${escapeHtml(card.description)}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="AB-Cloud Research" />
  <meta property="og:url" content="${pageUrl}" />
  <meta property="og:title" content="${escapeHtml(card.title)}" />
  <meta property="og:description" content="${escapeHtml(card.description)}" />
  <meta property="og:image" content="${cover}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="${escapeHtml(card.title)}" />
  <meta name="twitter:description" content="${escapeHtml(card.description)}" />
  <meta name="twitter:image" content="${cover}" />
</head>
<body>
  <!-- Server-rendered social card for bots; humans: ${pageUrl} -->
  <noscript><a href="${pageUrl}">Open AB-Cloud Research</a></noscript>
</body>
</html>
`;
}

// ── mini-API — JS ports of the api/*.ts Pxxl Functions ───────────────────
const ZEROS = [
  14.1347251417347, 21.0220396387716, 25.0108575801457, 30.4248761258595,
  32.9350615877392, 37.5861781588257, 40.91840544983, 43.327073280915,
  48.0051508811672, 49.7738324776723, 52.9703214777145, 56.4462476970634,
  59.3470440026024, 60.8317785246098, 65.1125440480817, 67.0798105294942,
  69.546401711174, 72.0671576744853, 75.7046906990839, 77.1448400688748,
  79.3373750202494, 82.910380854086, 84.7354929805171, 87.4208845358898,
  88.8091112076345, 92.4918992713839, 94.65134404051, 95.8706342282453,
  98.8311942181937, 101.317851005731,
];
const MAX_N = ZEROS.length;

function jsonResponse(body, status = 200, cacheControl = 'public, s-maxage=86400') {
  return {
    status,
    cacheControl,
    cors: cacheControl !== 'no-store', // zeta: open data, ACAO:*; health/version: dynamic
    body: JSON.stringify(body, null, 2) + '\n',
  };
}

function apiResponse(pathname, searchParams) {
  if (pathname === '/api/health') {
    return jsonResponse({
      status: 'ok',
      service: 'ab-cloud-research',
      version: '2.0.0',
      time: new Date().toISOString(),
      uptimeSeconds: Math.round(process.uptime()),
      endpoints: {
        health: '/api/health',
        version: '/api/version',
        zetaZeros: '/api/zeta?n=1..30',
        socialPreview: '/api/og?path=/',
      },
      links: {
        repository: 'https://github.com/wild8highlander/ab-cloud-research',
        doi: 'https://doi.org/10.5281/zenodo.21825394',
      },
    }, 200, 'no-store');
  }

  if (pathname === '/api/version') {
    return jsonResponse({
      service: 'ab-cloud-research',
      version: '2.0.0',
      release: 'x15-plus',
      time: new Date().toISOString(),
      uptimeSeconds: Math.round(process.uptime()),
      runtime: {
        engine: `node ${process.version}`,
        ts: 'JS port of api/version.ts (serve.mjs parity)',
      },
      features: {
        staticApp: ['redirects', 'bot-social-cards', 'security-headers', 'cache-tiers', 'spa=false'],
        pwa: ['manifest', 'service-worker', 'offline-fallback', 'shortcuts'],
        api: ['/api/health', '/api/version', '/api/zeta', '/api/og'],
      },
      visibleEnvKeys: Object.keys(process.env)
        .filter((k) => /^(PXXL|SITE_URL|NODE_VERSION|PORT)/.test(k))
        .sort(),
      links: {
        repository: 'https://github.com/wild8highlander/ab-cloud-research',
        doi: 'https://doi.org/10.5281/zenodo.21825394',
      },
    }, 200, 'no-store');
  }

  if (pathname === '/api/zeta') {
    const raw = searchParams.get('n');
    if (raw === null || raw === '') {
      return jsonResponse({
        hypothesis: 'Re(s) = 1/2 for every nontrivial zero of zeta(s)',
        zero: { ordinal: 1, realPart: 0.5, imaginaryPart: ZEROS[0] },
        zeros: ZEROS.slice(0, 10).map((imag, i) => ({ ordinal: i + 1, s: { re: 0.5, im: imag } })),
        count: Math.min(10, MAX_N),
        meta: {
          source: 'first nontrivial zeros on the critical line (Odlyzko tables)',
          usage: `/api/zeta?n=<1..${MAX_N}> — a single zero, or /api/zeta?n=<2..${MAX_N}> — the first n zeros`,
          companionDataset: '/dashboard/data/zeta_zeros_50000_embedded.txt',
          links: {
            repository: 'https://github.com/wild8highlander/ab-cloud-research',
            doi: 'https://doi.org/10.5281/zenodo.21825394',
          },
        },
      });
    }
    const n = Number(raw);
    if (!Number.isInteger(n) || n < 1 || n > MAX_N) {
      return jsonResponse(
        { error: 'invalid n', message: `n must be an integer in [1, ${MAX_N}]`, received: raw },
        400,
        'no-store',
      );
    }
    if (n === 1) return jsonResponse({ ordinal: 1, s: { re: 0.5, im: ZEROS[0] } });
    return jsonResponse({
      count: n,
      zeros: ZEROS.slice(0, n).map((imag, i) => ({ ordinal: i + 1, s: { re: 0.5, im: imag } })),
    });
  }

  if (pathname === '/api/og') {
    const requested = searchParams.get('path') ?? '/';
    const route = Object.prototype.hasOwnProperty.call(OG_CARDS, requested) ? requested : '/';
    return {
      status: 200,
      cacheControl: 'public, s-maxage=300',
      html: ogHtml('https://localhost', route),
    };
  }

  return null;
}

async function isFile(p) {
  const s = await stat(p).catch(() => null);
  return s?.isFile() ? p : null;
}

function safeDecode(raw) {
  try {
    return decodeURIComponent(raw);
  } catch {
    return raw; // malformed percent-encoding → serve as-is (will 404/500 safely)
  }
}

// Custom 404 page (dist/404.html), resolved once at startup.
const notFoundHtml = await isFile(join(root, '404.html'));

const server = createServer(async (req, res) => {
  const method = req.method || 'GET';
  if (method !== 'GET' && method !== 'HEAD') {
    res.writeHead(405, hdr({ allow: 'GET, HEAD' })).end('Method Not Allowed');
    return;
  }
  try {
    const reqUrl = new URL(req.url, 'http://localhost');
    const urlPath = safeDecode(reqUrl.pathname);
    const safePath = normalize(urlPath).replace(/^(\.\.[/\\])+/, '');

    // 0a. redirect rules (exact path match, like [[redirects]])
    const redirect = REDIRECTS.find((r) => r.source === urlPath);
    if (redirect) {
      const loc = redirect.destination.startsWith('http')
        ? redirect.destination
        : redirect.destination + (reqUrl.search || '');
      res.writeHead(redirect.status, hdr({ location: loc }));
      res.end();
      return;
    }

    // 0b. bot rewrite → server-rendered social card (like [[rewrites]])
    const ua = String(req.headers['user-agent'] ?? '');
    const baseForRewrite =
      urlPath === '/' ? '/' : urlPath.endsWith('/') ? urlPath.slice(0, -1) : urlPath;
    if (BOT_RE.test(ua) && Object.prototype.hasOwnProperty.call(OG_CARDS, baseForRewrite)) {
      const origin = `http://${req.headers.host ?? 'localhost'}`;
      const html = ogHtml(origin, baseForRewrite);
      res.writeHead(200, hdr({ 'content-type': MIME['.html'], 'cache-control': 'public, s-maxage=300' }));
      res.end(method === 'HEAD' ? undefined : html);
      return;
    }

    // 0c. mini-API (parity with the Pxxl Functions under api/)
    if (urlPath.startsWith('/api/')) {
      const api = apiResponse(urlPath, reqUrl.searchParams);
      if (api) {
        const headers = hdr({ 'content-type': MIME['.json'], 'cache-control': api.cacheControl });
        if (api.cors) headers['access-control-allow-origin'] = '*';
        if (api.html) {
          headers['content-type'] = MIME['.html'];
          const body = Buffer.from(api.html);
          res.writeHead(api.status, { ...headers, 'content-length': body.length });
          res.end(method === 'HEAD' ? undefined : body);
        } else {
          const body = Buffer.from(api.body);
          res.writeHead(api.status, { ...headers, 'content-length': body.length });
          res.end(method === 'HEAD' ? undefined : body);
        }
      } else {
        res.writeHead(404, hdr({ 'content-type': MIME['.json'] })).end('{"error":"unknown endpoint"}');
      }
      return;
    }

    // 0d. open research data gets CORS (mirrors the ACAO header rule)
    const allowCors = /^\/dashboard\/data\//.test(urlPath);

    const base = join(root, safePath);
    if (!base.startsWith(root)) {
      res.writeHead(403, hdr()).end('Forbidden');
      return;
    }

    // resolution order:
    //   1. exact file            (/dashboard/data/run_summary.json)
    //   2. directory index       (/dashboard/ → /dashboard/index.html)
    //   3. implicit index        (/dashboard  → 308 → /dashboard/, rule 0a)
    //   4. everything else       → styled 404 (dist/404.html)
    const st = await stat(base).catch(() => null);

    // safety net for directories without a configured redirect
    if (st?.isDirectory() && !urlPath.endsWith('/')) {
      res.writeHead(308, hdr({ location: encodeURI(urlPath) + '/' + (reqUrl.search || '') }));
      res.end();
      return;
    }

    let file = null;
    if (st?.isFile()) {
      file = base;
    } else if (st?.isDirectory() || !extname(urlPath)) {
      // Directory index only. There is deliberately NO soft fallback to the
      // landing page for unknown extensionless paths: unknown URLs must
      // return a real 404 (styled via dist/404.html), matching the Pxxl
      // static edge where no [routing] spa fallback is configured.
      file =
        (await isFile(join(base, 'index.html'))) ??
        (await isFile(join(base, 'index.htm')));
    }

    if (!file) {
      const nf = notFoundHtml ? await readFile(notFoundHtml).catch(() => null) : null;
      if (nf) {
        res.writeHead(
          404,
          hdr({
            'content-type': MIME['.html'],
            'content-length': nf.length,
            'cache-control': 'no-cache',
          }),
        );
        res.end(method === 'HEAD' ? undefined : nf);
      } else {
        res.writeHead(404, hdr({ 'content-type': 'text/plain; charset=utf-8' })).end('404 Not Found');
      }
      return;
    }

    // realpath guard: a symlink inside dist/ must not escape the site root
    const real = await realpath(file).catch(() => null);
    if (!real || !real.startsWith(rootReal)) {
      res.writeHead(403, hdr()).end('Forbidden');
      return;
    }

    const data = await readFile(file);
    const rel = file.slice(root.length);
    const headers = {
      'content-type': MIME[extname(file).toLowerCase()] ?? 'application/octet-stream',
      'content-length': data.length,
      'cache-control': cacheControlFor(rel),
    };
    if (allowCors) headers['access-control-allow-origin'] = '*';
    res.writeHead(200, hdr(headers));
    res.end(method === 'HEAD' ? undefined : data);
  } catch (err) {
    res.writeHead(500, hdr({ 'content-type': 'text/plain; charset=utf-8' })).end(`500: ${err.message}`);
  }
});

// Friendly startup failure (EADDRINUSE etc.) instead of an unhandled error
server.on('error', (err) => {
  console.error(`✗ AB-Cloud portal server failed to start: ${err.message}`);
  if (err.code === 'EADDRINUSE') {
    console.error(`  Port ${port} is already in use — set a different PORT env value.`);
  }
  process.exit(1);
});

server.listen(port, '0.0.0.0', () => {
  console.log(`AB-Cloud portal serving dist/ at http://0.0.0.0:${port}`);
});
