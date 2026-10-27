/**
 * api/og.ts — GET /api/og?path=/<route>
 *
 * Server-side social-preview generator. The [[rewrites]] rules in pxxl.toml
 * send requests from social bots (twitterbot, whatsapp, telegrambot,
 * discordbot, …) here, so shared links unfurl with correct per-route cards
 * even though the Vite apps themselves ship no OG meta.
 *
 * The handler builds ABSOLUTE og:image/twitter:image URLs from the request
 * host — the one thing a static index.html cannot do for itself.
 * Humans never see this page: the rewrite matches bot user-agents only.
 */

interface RouteCard {
  title: string;
  description: string;
}

const CARDS: Record<string, RouteCard> = {
  '/': {
    title: 'AB-Cloud Research — Phase Resonator for the Riemann ζ Zeros',
    description:
      'A topological vortex on a Hofstadter lattice encoding Aharonov–Bohm phases from the zeros of the Riemann zeta function. Interactive verification dashboard and 3D laboratory.',
  },
  '/dashboard': {
    title: 'AB-Cloud — Verification Dashboard',
    description:
      'The two-pass verdict table for the Hilbert–Pólya program: 39 tests, Julia 1.12, 50 000 Odlyzko zeros, live ζ statistics (b(N), KS vs GUE, Σ²(L), Δ₃(L)) computed in a Web Worker.',
  },
  '/lab3d': {
    title: 'AB-Cloud — 3D Laboratory',
    description:
      'Interactive WebGL scenes of experiments 3D-1…3D-34: the Hofstadter lattice with vortex flux cones, the Dirac cone at α = 1/2, and the ζ critical strip with the embedded zeros γ₁…γ₁₅.',
  },
};

function escapeHtml(s: string): string {
  return s
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

function escapeAttr(s: string): string {
  return escapeHtml(s).replaceAll("'", '%27');
}

export async function GET(request: Request): Promise<Response> {
  const url = new URL(request.url);
  const routeParam = url.searchParams.get('path') ?? '/';
  // whitelist: only the three real routes are representable
  const route = Object.prototype.hasOwnProperty.call(CARDS, routeParam) ? routeParam : '/';
  const card = CARDS[route];

  // absolute URL of the cover image — resolved against the live host
  const cover = new URL('/og-cover.png', url.origin).toString();
  const pageUrl = new URL(route === '/' ? '/' : route + '/', url.origin).toString();

  const meta = [
    `<meta property="og:type" content="website" />`,
    `<meta property="og:site_name" content="AB-Cloud Research" />`,
    `<meta property="og:url" content="${escapeAttr(pageUrl)}" />`,
    `<meta property="og:title" content="${escapeHtml(card.title)}" />`,
    `<meta property="og:description" content="${escapeHtml(card.description)}" />`,
    `<meta property="og:image" content="${escapeAttr(cover)}" />`,
    `<meta property="og:image:width" content="1200" />`,
    `<meta property="og:image:height" content="630" />`,
    `<meta property="og:image:alt" content="AB-Cloud Research — phase resonator for the ζ zeros" />`,
    `<meta name="twitter:card" content="summary_large_image" />`,
    `<meta name="twitter:title" content="${escapeHtml(card.title)}" />`,
    `<meta name="twitter:description" content="${escapeHtml(card.description)}" />`,
    `<meta name="twitter:image" content="${escapeAttr(cover)}" />`,
  ].join('\n    ');

  const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex,follow" />
  <title>${escapeHtml(card.title)}</title>
  <meta name="description" content="${escapeHtml(card.description)}" />
  ${meta}
</head>
<body>
  <!-- Server-rendered social card for bots; humans: ${escapeHtml(pageUrl)} -->
  <noscript><a href="${escapeAttr(pageUrl)}">Open AB-Cloud Research</a></noscript>
</body>
</html>
`;

  return new Response(html, {
    status: 200,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      // edge-cache the generated card; the platform caps s-maxage at 1h
      'Cache-Control': 'public, s-maxage=300',
    },
  });
}
