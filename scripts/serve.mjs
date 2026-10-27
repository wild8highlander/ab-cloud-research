#!/usr/bin/env node
/**
 * serve.mjs — zero-dependency static server for the assembled AB-Cloud portal.
 *
 * Used as the Web Service fallback start command (`npm start`):
 * serves ./dist on 0.0.0.0:$PORT (default 3000) and answers the
 * platform health check on / (GET and HEAD).
 */
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, join, resolve, dirname, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..', 'dist');
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

const server = createServer(async (req, res) => {
  const method = req.method || 'GET';
  if (method !== 'GET' && method !== 'HEAD') {
    res.writeHead(405, { allow: 'GET, HEAD' }).end('Method Not Allowed');
    return;
  }
  try {
    const urlPath = safeDecode(new URL(req.url, 'http://localhost').pathname);
    const safePath = normalize(urlPath).replace(/^(\.\.[/\\])+/, '');
    const base = join(root, safePath);
    if (!base.startsWith(root)) {
      res.writeHead(403).end('Forbidden');
      return;
    }

    // resolution order:
    //   1. exact file            (/dashboard/data/run_summary.json)
    //   2. directory index       (/dashboard/ → /dashboard/index.html)
    //   3. implicit index        (/dashboard  → /dashboard/index.html)
    //   4. extensionless → portal landing (soft fallback), else 404
    const st = await stat(base).catch(() => null);
    let file = null;
    if (st?.isFile()) {
      file = base;
    } else if (st?.isDirectory() || !extname(urlPath)) {
      file =
        (await isFile(join(base, 'index.html'))) ??
        (await isFile(join(base, 'index.htm'))) ??
        (extname(urlPath) ? null : join(root, 'index.html'));
    }

    if (!file) {
      res.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' }).end('404 Not Found');
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
    res.writeHead(200, headers);
    res.end(method === 'HEAD' ? undefined : data);
  } catch (err) {
    res.writeHead(500, { 'content-type': 'text/plain; charset=utf-8' }).end(`500: ${err.message}`);
  }
});

server.listen(port, '0.0.0.0', () => {
  console.log(`AB-Cloud portal serving dist/ at http://0.0.0.0:${port}`);
});
