#!/usr/bin/env node
/**
 * deploy-build.mjs — Pxxl build entry point with a ZERO-FAILURE guarantee.
 *
 * Why this exists
 * ---------------
 * The committed ./dist is always a complete, verified build (the maintainer
 * has no local Node toolchain, so every source change ships together with a
 * freshly rebuilt dist). A hosted builder, however, is an unpredictable
 * environment: npm registry hiccups, restricted postinstall scripts, a Node
 * runtime older than the lockfile expects, a dev-dependency-less install…
 * Any of those turned every Pxxl production deploy of this repository into
 * "Failed to deploy to production" — even though a perfectly good dist was
 * sitting right there in git.
 *
 * What it does
 * ------------
 *   1. Backs up the committed ./dist (if present) to .pxxl-dist-backup/.
 *   2. Runs the full rebuild (`node scripts/build-site.mjs`):
 *      npm ci → esbuild self-heal → vite build ×2 → assemble dist/.
 *   3. If the rebuild produced a complete site
 *      (dist/index.html + dist/dashboard/ + dist/lab3d/) — ship it.
 *   4. If ANYTHING failed — restore the committed dist and still exit 0:
 *      production always ships the last known-good build instead of
 *      failing the deploy. A loud ⚠ warning is printed for the build log.
 *
 * The script never exits non-zero unless there is NEITHER a fresh build
 * NOR a committed dist to fall back to — at which point no deploy could
 * possibly serve anything anyway.
 *
 * Works on Node >= 16.7 (cpSync) — deliberately more permissive than the
 * build itself, so the fallback path survives even an ancient builder.
 */
import { spawnSync } from 'node:child_process';
import { cpSync, existsSync, rmSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const dist = join(root, 'dist');
const backup = join(root, '.pxxl-dist-backup');

const REQUIRED = ['index.html', 'dashboard/index.html', 'lab3d/index.html'];

function completeSite(dir) {
  return REQUIRED.every((rel) => {
    try {
      return statSync(join(dir, rel)).isFile();
    } catch {
      return false;
    }
  });
}

const hadCommittedDist = completeSite(dist);

// 1. preserve the committed build before the rebuild wipes ./dist
if (hadCommittedDist) {
  rmSync(backup, { recursive: true, force: true });
  cpSync(dist, backup, { recursive: true });
  console.log('▶ committed dist/ backed up to .pxxl-dist-backup/');
}

// 2. full rebuild (npm ci + both Vite apps + assembly). A non-zero exit
//    or a crash is expected and handled — never fatal here.
console.log('\n▶ running the full rebuild (scripts/build-site.mjs)…');
const r = spawnSync(process.execPath, ['scripts/build-site.mjs'], {
  cwd: root,
  stdio: 'inherit',
  timeout: 15 * 60 * 1000,
});

let ok = false;
if (r.error) {
  console.error(`⚠ rebuild could not start: ${r.error.message}`);
} else if (r.status !== 0) {
  console.error(`⚠ rebuild exited with code ${r.status}`);
} else {
  ok = completeSite(dist);
  if (!ok) console.error('⚠ rebuild finished but dist/ is incomplete');
}

// 3/4. verdict
if (ok) {
  rmSync(backup, { recursive: true, force: true });
  console.log('\n✅ fresh build verified — shipping it.');
} else if (hadCommittedDist) {
  rmSync(dist, { recursive: true, force: true });
  cpSync(backup, dist, { recursive: true });
  rmSync(backup, { recursive: true, force: true });
  console.log('\n⚠⚠ REBUILD FAILED — restored the committed dist/ and shipping that.');
  console.log('    Production stays online with the last known-good build.');
  console.log('    Fix the builder environment (Node version, npm registry access,');
  console.log('    dev-dependencies) to get fresh builds again.');
} else {
  console.error('\n✗ no fresh build AND no committed dist/ — nothing to publish.');
  process.exit(1);
}
