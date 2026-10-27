#!/usr/bin/env node
/**
 * serve.mjs — zero-dependency static server for the assembled AB-Cloud portal.
 *
 * Used as the Web Service fallback start command (`npm start`):
 * serves ./dist on 0.0.0.0:$PORT (default 3000) and answers the
 * platform health check on /.
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

async function firstExisting(paths) {
  for (const p of paths) {
    const s = await stat(p).catch(() => null);
    if (s?.isFile()) return p;
  }
  return null;
}

const server = createServer(async (req, res) => {
  try {
    const urlPath = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    const safePath = normalize(urlPath).replace(/^(\.\.[/\\])+/, '');
    const base = join(root, safePath);
    if (!base.startsWith(root)) {
      res.writeHead(403).end('Forbidden');
      return;
    }

    const file =
      (await stat(base).then((s) => (s.isDirectory() ? join(base, 'index.html') : base)).catch(() => null)) ??
      (await firstExisting([join(base, 'index.html'), join(base, 'index.htm')])) ??
      (urlPath === '/' || !extname(urlPath) ? join(root, 'index.html') : null);

    if (!file) {
      res.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' }).end('404 Not Found');
      return;
    }

    const data = await readFile(file);
    res.writeHead(200, {
      'content-type': MIME[extname(file).toLowerCase()] ?? 'application/octet-stream',
      'cache-control': file.includes(`${root}/assets`) ? 'public, max-age=31536000, immutable' : 'no-cache',
    });
    res.end(data);
  } catch (err) {
    res.writeHead(500, { 'content-type': 'text/plain; charset=utf-8' }).end(`500: ${err.message}`);
  }
});

server.listen(port, '0.0.0.0', () => {
  console.log(`AB-Cloud portal serving dist/ at http://0.0.0.0:${port}`);
});
