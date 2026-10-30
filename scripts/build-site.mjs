#!/usr/bin/env node
/**
 * build-site.mjs — assembles the deployable AB-Cloud portal.
 *
 * 1. Installs workspace dependencies (if needed) and builds both Vite apps:
 *      apps/ab-cloud-dashboard  -> apps/ab-cloud-dashboard/dist
 *      apps/ab-cloud-lab3d      -> apps/ab-cloud-lab3d/dist
 * 2. Merges them into a single static site at ./dist:
 *      dist/index.html            (portal landing from ./site)
 *      dist/dashboard/...         (React verification dashboard)
 *      dist/lab3d/...             (React + Three.js 3D laboratory)
 * 3. If SITE_URL is set (e.g. in Pxxl Secrets), emits SEO artifacts:
 *      dist/sitemap.xml           (absolute URLs: /, /dashboard/, /lab3d/)
 *      dist/robots.txt            (+ "Sitemap:" line)
 *      canonical <link> + og:url + absolute og:image in dist/index.html
 *
 * Works on Node >= 18 (no external dependencies).
 */
import { spawnSync } from 'node:child_process';
import { existsSync, cpSync, mkdirSync, rmSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const dist = join(root, 'dist');
const site = join(root, 'site');

const apps = [
  { name: 'ab-cloud-dashboard', dir: join(root, 'apps', 'ab-cloud-dashboard') },
  { name: 'ab-cloud-lab3d', dir: join(root, 'apps', 'ab-cloud-lab3d') },
];

function run(cmd, args, cwd) {
  console.log(`\n▶ ${cmd} ${args.join(' ')}  (cwd: ${cwd})`);
  const r = spawnSync(cmd, args, { cwd, stdio: 'inherit', shell: process.platform === 'win32' });
  if (r.status !== 0) {
    console.error(`✗ Command failed: ${cmd} ${args.join(' ')} in ${cwd}`);
    process.exit(r.status ?? 1);
  }
}

// ---- esbuild self-heal -------------------------------------------------------
// Some CI environments (recent npm security policy, restricted containers)
// skip esbuild's postinstall validation script. The binary usually still
// works (it ships as an optionalDependency), but when the platform binary is
// missing the API throws. A rebuild re-runs the install script and fixes it;
// a plain `npm install` is the last-resort fallback. Doing this BEFORE the
// vite builds turns a confusing "esbuild: Failed to install correctly" (or
// "The service was stopped") build failure into an automatic repair.
function esbuildHealthy(appDir) {
  const probe = spawnSync(
    process.execPath,
    ['-e', "try{const e=require('esbuild');e.transformSync('const x=1');}catch(_){process.exit(1)}"],
    { cwd: appDir, timeout: 30000 },
  );
  return probe.status === 0;
}

function ensureEsbuild(appDir) {
  if (esbuildHealthy(appDir)) return;
  console.log('\n⚠ esbuild sanity check failed — attempting automatic repair…');
  spawnSync('npm', ['rebuild', 'esbuild'], { cwd: root, stdio: 'inherit', shell: process.platform === 'win32' });
  if (esbuildHealthy(appDir)) {
    console.log('✓ esbuild repaired via `npm rebuild esbuild`.');
    return;
  }
  console.log('⚠ still broken — falling back to a full `npm install`…');
  run('npm', ['install'], root);
  if (!esbuildHealthy(appDir)) {
    console.error('✗ esbuild is not usable after repair attempts — aborting with a clear message.');
    console.error('  Fix locally with: npm rebuild esbuild   (or npm install)');
    process.exit(1);
  }
}

function ensureDeps(appDir) {
  // npm workspaces hoist deps to the root node_modules; checking the app-level
  // dir alone would re-run `npm ci` on every build even right after install.
  if (existsSync(join(appDir, 'node_modules')) ||
      existsSync(join(root, 'node_modules'))) return;
  console.log('\n▶ installing workspace dependencies…');
  if (existsSync(join(root, 'package-lock.json'))) {
    const ci = spawnSync('npm', ['ci'], { cwd: root, stdio: 'inherit' });
    if (ci.status !== 0) run('npm', ['install'], root);
  } else {
    run('npm', ['install'], root);
  }
}

// 0. Fail early (and clearly) when an expected input directory is missing
//    instead of throwing a raw ENOENT stack from cpSync at the end.
if (!existsSync(site)) {
  console.error(`✗ Build input missing: ${site}`);
  console.error('  The portal landing lives in ./site — make sure it is committed.');
  process.exit(1);
}
for (const app of apps) {
  if (!existsSync(join(app.dir, 'package.json'))) {
    console.error(`✗ Build input missing: ${app.dir}/package.json`);
    console.error('  Workspace apps must live under ./apps — make sure they are committed.');
    process.exit(1);
  }
}

// 1. Build both apps
for (const app of apps) {
  ensureDeps(app.dir);
  ensureEsbuild(app.dir);
  run('npm', ['run', 'build', '-w', app.name], root);
}

// 2. Assemble the unified static site
console.log('\n▶ assembling dist/ …');
rmSync(dist, { recursive: true, force: true });
mkdirSync(dist, { recursive: true });

cpSync(join(apps[0].dir, 'dist'), join(dist, 'dashboard'), { recursive: true });
cpSync(join(apps[1].dir, 'dist'), join(dist, 'lab3d'), { recursive: true });

// 3. Portal landing (site/index.html + assets) at the site root
//    (cpSync copies dot-directories too — site/.well-known/security.txt lands at dist/.well-known/)
cpSync(site, dist, { recursive: true });

// 3.5. Static API snapshots — dist/api/*.json
//
//      Pxxl Functions are a paid-plan feature; on plans without them the
//      api/*.ts handlers are not deployed, yet the landing page's status
//      dot fetches /api/health and research notebooks use /api/zeta.
//      pxxl.toml therefore redirects /api/{health,version,zeta} onto these
//      frozen JSON snapshots (307), so a PURE STATIC deployment keeps a
//      working mini-API. Content mirrors scripts/serve.mjs and api/*.ts —
//      keep the three in sync. Dynamic fields (time/uptime) are frozen to
//      the build moment; the "mode" field makes that explicit.
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
const API_VERSION = '2.0.0'; // keep in sync with api/health.ts and api/version.ts
const BUILD_TIME = new Date().toISOString();
const REPO = 'https://github.com/wild8highlander/ab-cloud-research';
const DOI = 'https://doi.org/10.5281/zenodo.21825394';

const apiDir = join(dist, 'api');
mkdirSync(apiDir, { recursive: true });
const writeJson = (name, body) =>
  writeFileSync(join(apiDir, name), JSON.stringify(body, null, 2) + '\n');

writeJson('health.json', {
  status: 'ok',
  service: 'ab-cloud-research',
  version: API_VERSION,
  mode: 'static-snapshot',
  time: BUILD_TIME,
  uptimeSeconds: 0,
  endpoints: {
    health: '/api/health',
    version: '/api/version',
    zetaZeros: '/api/zeta?n=1..30',
  },
  links: { repository: REPO, doi: DOI },
});

writeJson('version.json', {
  service: 'ab-cloud-research',
  version: API_VERSION,
  release: 'x15-plus',
  mode: 'static-snapshot',
  time: BUILD_TIME,
  features: {
    staticApp: ['redirects', 'security-headers', 'cache-tiers', 'spa=false', 'static-api-snapshots'],
    pwa: ['manifest', 'service-worker', 'offline-fallback', 'shortcuts'],
    api: ['/api/health', '/api/version', '/api/zeta'],
  },
  links: { repository: REPO, doi: DOI },
});

writeJson('zeta.json', {
  hypothesis: 'Re(s) = 1/2 for every nontrivial zero of zeta(s)',
  zero: { ordinal: 1, realPart: 0.5, imaginaryPart: ZEROS[0] },
  zeros: ZEROS.slice(0, 10).map((imag, i) => ({ ordinal: i + 1, s: { re: 0.5, im: imag } })),
  count: 10,
  meta: {
    source: 'first nontrivial zeros on the critical line (Odlyzko tables)',
    usage: '/api/zeta.json serves the first 10 zeros; ?n=1..30 ranges need Pxxl Functions (api/zeta.ts)',
    fullFirst30: ZEROS.map((imag, i) => ({ ordinal: i + 1, s: { re: 0.5, im: imag } })),
    companionDataset: '/dashboard/data/zeta_zeros_50000_embedded.txt',
    links: { repository: REPO, doi: DOI },
  },
});

// 4. Optional SEO pass — only when the public URL is known.
//    Set SITE_URL in Pxxl Secrets ("https://<your-pxxl-domain>"), rebuild,
//    and the deploy gains a sitemap, robots Sitemap line, canonical link
//    and absolute OG image URLs. Without SITE_URL the site ships exactly
//    as before (relative og:image, no sitemap) — nothing breaks.
const SITE_URL = (process.env.SITE_URL || process.env.PXXL_PUBLIC_DOMAIN || '').replace(/\/+$/, '');
if (SITE_URL) {
  if (!/^https:\/\//.test(SITE_URL)) {
    console.error(`✗ SITE_URL must start with https:// (got "${SITE_URL}") — skipping SEO pass.`);
  } else {
    console.log(`\n▶ SEO pass for SITE_URL=${SITE_URL} …`);

    writeFileSync(
      join(dist, 'sitemap.xml'),
      `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>${SITE_URL}/</loc><changefreq>monthly</changefreq><priority>1.0</priority></url>
  <url><loc>${SITE_URL}/dashboard/</loc><changefreq>monthly</changefreq><priority>0.9</priority></url>
  <url><loc>${SITE_URL}/lab3d/</loc><changefreq>monthly</changefreq><priority>0.9</priority></url>
</urlset>
`,
    );

    const robotsPath = join(dist, 'robots.txt');
    let robots = readFileSync(robotsPath, 'utf8').replace(/\n*Sitemap:.*$/m, '').trimEnd();
    robots += `\nSitemap: ${SITE_URL}/sitemap.xml\n`;
    writeFileSync(robotsPath, robots);

    const landingPath = join(dist, 'index.html');
    let landing = readFileSync(landingPath, 'utf8');
    // absolute cover image for social scrapers that ignore relative URLs
    landing = landing
      .replaceAll('content="og-cover.png"', `content="${SITE_URL}/og-cover.png"`)
      .replace(
        /(\s*<meta name="twitter:image" content="[^"]*" \/>)/,
        `$1\n  <meta property="og:url" content="${SITE_URL}/" />\n  <link rel="canonical" href="${SITE_URL}/" />`,
      );
    writeFileSync(landingPath, landing);

    console.log('   dist/sitemap.xml         — generated from SITE_URL');
    console.log('   dist/robots.txt          — + Sitemap line');
    console.log('   dist/index.html          — canonical + og:url + absolute og:image');
  }
}

console.log('\n✅ AB-Cloud portal assembled:');
console.log('   dist/index.html          — portal landing');
console.log('   dist/dashboard/…         — verification dashboard (React 19 + Vite)');
console.log('   dist/lab3d/…             — 3D laboratory (React 19 + Three.js)');
console.log('   dist/api/*.json          — static mini-API snapshots (health/version/zeta)');
console.log('   dist/offline.html        — offline fallback (service worker)');
console.log('   dist/.well-known/        — security.txt (RFC 9116)');
