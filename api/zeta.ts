/**
 * api/zeta.ts — GET /api/zeta?n=<1..30>
 *
 * A tiny open-data API: the first N nontrivial zeros of the Riemann zeta
 * function on the critical line Re(s) = 1/2 (standard published values,
 * Odlyzko's tables; 15 significant digits).
 *
 * Examples:
 *   /api/zeta        → first 10 zeros + metadata
 *   /api/zeta?n=30   → first 30 zeros
 *   /api/zeta?n=7    → exactly the 7th zero
 *
 * Companion to the 50,000-zero dataset embedded in the verification
 * dashboard (dist/dashboard/data/zeta_zeros_50000_embedded.txt).
 */

const ZEROS: readonly number[] = [
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

function json(body: unknown, status = 200, cacheControl = 'public, s-maxage=86400'): Response {
  return new Response(JSON.stringify(body, null, 2) + '\n', {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': cacheControl,
      // open data: notebooks and tools may fetch it cross-origin
      'Access-Control-Allow-Origin': '*',
    },
  });
}

export async function GET(request: Request): Promise<Response> {
  const url = new URL(request.url);
  const raw = url.searchParams.get('n');

  if (raw === null || raw === '') {
    return json({
      hypothesis: 'Re(s) = 1/2 for every nontrivial zero of zeta(s)',
      zero: { ordinal: 1, realPart: 0.5, imaginaryPart: ZEROS[0] },
      zeros: ZEROS.slice(0, 10).map((imag, i) => ({
        ordinal: i + 1,
        s: { re: 0.5, im: imag },
      })),
      count: Math.min(10, MAX_N),
      meta: {
        source: 'first nontrivial zeros on the critical line (Odlyzko tables)',
        usage: '/api/zeta?n=<1..' + MAX_N + '> — a single zero, or /api/zeta?n=<2..' + MAX_N + '> — the first n zeros',
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
    return json(
      {
        error: 'invalid n',
        message: `n must be an integer in [1, ${MAX_N}]`,
        received: raw,
      },
      400,
      'no-store',
    );
  }

  if (n === 1) {
    return json({
      ordinal: 1,
      s: { re: 0.5, im: ZEROS[0] },
    });
  }

  return json({
    count: n,
    zeros: ZEROS.slice(0, n).map((imag, i) => ({ ordinal: i + 1, s: { re: 0.5, im: imag } })),
  });
}
