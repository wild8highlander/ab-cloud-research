/**
 * api/version.ts — GET /api/version
 *
 * Deployment introspection endpoint: what am I talking to, how long has it
 * been up, and which Pxxl environment variables are visible to this
 * generation (keys only — values are never echoed, secrets stay secret).
 *
 * Handy for:
 *   • verifying a Redeploy actually replaced the running generation
 *   • debugging deploys straight from the browser address bar
 *   • dashboards that display the current release
 *
 * Web-API handler style: zero imports, standard Request/Response globals.
 */

const SERVICE = 'ab-cloud-research';
const VERSION = '2.0.0'; // keep in sync with api/health.ts

function pickEnvKeys(): string[] {
  const names: string[] = [];
  try {
    // eslint-disable-next-line no-undef
    const env = (globalThis as Record<string, unknown>).process &&
      (globalThis as { process?: { env?: Record<string, string> } }).process?.env;
    if (env) names.push(...Object.keys(env).filter((k) => /^(PXXL|SITE_URL|NODE_VERSION|PORT)/.test(k)).sort());
  } catch {
    // env access is best-effort only
  }
  return names;
}

export async function GET(_request: Request): Promise<Response> {
  const startedNanos =
    typeof performance !== 'undefined' && performance.timeOrigin ? performance.timeOrigin : Date.now() - 0;

  const body = {
    service: SERVICE,
    version: VERSION,
    release: 'x15-plus',
    time: new Date().toISOString(),
    uptimeSeconds: Math.max(0, Math.round((Date.now() - startedNanos) / 1000)),
    runtime: {
      engine: 'pxxl-function (gVisor-isolated Web API)',
      ts: 'TypeScript, zero imports',
    },
    features: {
      staticApp: ['redirects', 'bot-social-cards', 'security-headers', 'cache-tiers', 'spa=false'],
      pwa: ['manifest', 'service-worker', 'offline-fallback', 'shortcuts'],
      api: ['/api/health', '/api/version', '/api/zeta', '/api/og'],
    },
    visibleEnvKeys: pickEnvKeys(),
    links: {
      repository: 'https://github.com/wild8highlander/ab-cloud-research',
      doi: 'https://doi.org/10.5281/zenodo.21825394',
    },
  };

  return new Response(JSON.stringify(body, null, 2) + '\n', {
    status: 200,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*',
      // introspection data is per-generation and time-sensitive
      'Cache-Control': 'no-store',
    },
  });
}
