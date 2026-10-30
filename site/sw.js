/**
 * AB-Cloud Research — service worker.
 *
 * Caching strategy (vanilla, zero dependencies):
 *   navigations              → network-first, cache fallback, then /offline.html
 *   /api/*                   → network-only (serverless functions manage their own s-maxage)
 *   /dashboard/assets/*,     → cache-first (content-hashed filenames, immutable)
 *   /lab3d/assets/*
 *   other same-origin GET    → stale-while-revalidate
 *
 * The precache list must stay root-relative: Pxxl serves the site from the
 * domain root, and scripts/serve.mjs (the local/fallback server) does too.
 */
const VERSION = 'ab-cloud-v4';
const PRECACHE = `${VERSION}-precache`;
const RUNTIME = `${VERSION}-runtime`;

const PRECACHE_URLS = [
  '/',
  '/offline.html',
  '/404.html',
  '/manifest.json',
  '/favicon.svg',
  '/icon-192.png',
  '/icon-512.png',
  '/icon-maskable-512.png',
  '/apple-touch-icon.png',
  '/og-cover.png',
  '/robots.txt',
  '/portal.js',
  '/particles.js',
  '/fonts/manrope-var.woff2',
  '/fonts/geist-mono-var.woff2',
];

// hashed, content-addressed build output — safe to keep forever
const IMMUTABLE_RE = /^\/(dashboard|lab3d)\/assets\//;

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches
      .open(PRECACHE)
      .then((cache) =>
        // addAll fails the whole install if ANY url 404s; add one-by-one so a
        // missing optional file can never brick the worker.
        Promise.allSettled(PRECACHE_URLS.map((u) => cache.add(new Request(u, { cache: 'reload' })))),
      )
      .then(() => self.skipWaiting()),
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(keys.filter((k) => !k.startsWith(VERSION)).map((k) => caches.delete(k))),
      )
      .then(() => self.clients.claim()),
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;

  // only same-origin GET without Range (media streaming must hit the network)
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (req.headers.has('range')) return;

  // 1. serverless API — never cached client-side
  if (url.pathname.startsWith('/api/')) return; // network-only

  // 2. app navigations (HTML documents)
  if (req.mode === 'navigate' || req.destination === 'document') {
    event.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(RUNTIME).then((c) => c.put(req, copy)).catch(() => {});
          return res;
        })
        .catch(() =>
          caches
            .match(req)
            .then(
              (hit) =>
                hit ??
                caches
                  .match('/offline.html')
                  .then((off) => off ?? new Response('Offline', { status: 503, headers: { 'Content-Type': 'text/plain' } })),
            ),
        ),
    );
    return;
  }

  // 3. immutable hashed assets — cache-first
  if (IMMUTABLE_RE.test(url.pathname)) {
    event.respondWith(
      caches.match(req).then(
        (hit) =>
          hit ??
          fetch(req).then((res) => {
            if (res.ok) caches.open(RUNTIME).then((c) => c.put(req, res.clone())).catch(() => {});
            return res;
          }),
      ),
    );
    return;
  }

  // 4. everything else — stale-while-revalidate
  event.respondWith(
    caches.match(req).then((hit) => {
      const network = fetch(req)
        .then((res) => {
          if (res.ok) caches.open(RUNTIME).then((c) => c.put(req, res.clone())).catch(() => {});
          return res;
        })
        .catch(() => hit);
      return hit ?? network;
    }),
  );
});
