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
 *
 * Works on Node >= 20.19 (no external dependencies).
 */
import { spawnSync } from 'node:child_process';
import { existsSync, cpSync, mkdirSync, rmSync } from 'node:fs';
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

function ensureDeps(appDir) {
  if (existsSync(join(appDir, 'node_modules'))) return;
  console.log('\n▶ installing workspace dependencies…');
  if (existsSync(join(root, 'package-lock.json'))) {
    const ci = spawnSync('npm', ['ci'], { cwd: root, stdio: 'inherit' });
    if (ci.status !== 0) run('npm', ['install'], root);
  } else {
    run('npm', ['install'], root);
  }
}

// 1. Build both apps
for (const app of apps) {
  ensureDeps(app.dir);
  run('npm', ['run', 'build', '-w', app.name], root);
}

// 2. Assemble the unified static site
console.log('\n▶ assembling dist/ …');
rmSync(dist, { recursive: true, force: true });
mkdirSync(dist, { recursive: true });

cpSync(join(apps[0].dir, 'dist'), join(dist, 'dashboard'), { recursive: true });
cpSync(join(apps[1].dir, 'dist'), join(dist, 'lab3d'), { recursive: true });

// 3. Portal landing (site/index.html + assets) at the site root
cpSync(site, dist, { recursive: true });

console.log('\n✅ AB-Cloud portal assembled:');
console.log('   dist/index.html          — portal landing');
console.log('   dist/dashboard/…         — verification dashboard (React 19 + Vite)');
console.log('   dist/lab3d/…             — 3D laboratory (React 19 + Three.js)');
