/**
 * api/health.ts — GET /api/health
 *
 * Platform-agnostic health endpoint for uptime monitors (Pxxl Cron Jobs,
 * UptimeRobot, …) and CI smoke tests. Returns structured JSON describing
 * the deployed portal generation.
 *
 * Web-API handler style: zero imports, runs on the standard Request/Response
 * globals inside Pxxl's gVisor-isolated Node runtime.
 */

const SERVICE = 'ab-cloud-research';
const VERSION = '2.0.0'; // keep in sync with api/version.ts

export async function GET(_request: Request): Promise<Response> {
  const body = {
    status: 'ok',
    service: SERVICE,
    version: VERSION,
    time: new Date().toISOString(),
    uptimeSeconds: Math.round(process.uptime?.() ?? 0),
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
  };

  return new Response(JSON.stringify(body, null, 2) + '\n', {
    status: 200,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      // monitors poll frequently; never cache a health probe
      'Cache-Control': 'no-store',
    },
  });
}
