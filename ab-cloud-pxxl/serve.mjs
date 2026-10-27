#!/usr/bin/env node
/**
 * serve.mjs — zero-dependency static server for the assembled AB-Cloud portal.
 *
 * Used as the Web Service fallback start command (`npm start`):
 * serves ./dist on 0.0.0.0:$PORT (default 3000) and answers the
 * platform health check on / (GET and HEAD).
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
  '.txt': 'text/plain; charset=utf-8',
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

// Security headers applied to every response — mirrors the [[headers]]
// rules in pxxl.toml, so the Web-Service fallback behaves exactly like
// the Pxxl static edge (identical hardening on both deployment targets).
const SECURITY = {
  'x-content-type-options': 'nosniff',
  'referrer-policy': 'strict-origin-when-cross-origin',
  'x-frame-options': 'SAMEORIGIN',
  'permissions-policy': 'camera=(), microphone=(), geolocation=()',
};
const hdr = (extra) => ({ ...SECURITY, ...extra });

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
    const base = join(root, safePath);
    if (!base.startsWith(root)) {
      res.writeHead(403, hdr()).end('Forbidden');
      return;
    }

    // resolution order:
    //   1. exact file            (/dashboard/data/run_summary.json)
    //   2. directory index       (/dashboard/ → /dashboard/index.html)
    //   3. implicit index        (/dashboard  → 301 → /dashboard/)
    //   4. everything else       → styled 404 (dist/404.html)
    const st = await stat(base).catch(() => null);

    // CRITICAL: a directory requested WITHOUT the trailing slash must 301
    // to the slash form. Serving index.html directly from "/dashboard"
    // would resolve the page's RELATIVE asset URLs ("./assets/…",
    // fetch("data/…")) against "/" instead of "/dashboard/" → 404s and a
    // blank page. (Same convention as nginx/Netlify/GitHub Pages.)
    if (st?.isDirectory() && !urlPath.endsWith('/')) {
      const search = reqUrl.search || '';
      res.writeHead(301, hdr({ location: encodeURI(urlPath) + '/' + search }));
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
      // Serve the styled 404 page when it exists (status stays 404 so
      // crawlers and monitors still see the real code).
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
    const headers = {
      'content-type': MIME[extname(file).toLowerCase()] ?? 'application/octet-stream',
      'content-length': data.length,
      'cache-control': file.startsWith(join(root, 'dashboard', 'assets')) ||
        file.startsWith(join(root, 'lab3d', 'assets'))
        ? 'public, max-age=31536000, immutable'
        : 'no-cache',
    };
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
