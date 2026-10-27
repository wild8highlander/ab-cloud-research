# Security Policy

## Supported surface

This is a research package: numerical code, monographs, data, and a
self-contained web laboratory. It does not run as a service, does not collect
data, and the web lab (`07_web_lab/index.html`) is fully offline — no CDN,
no telemetry, no cookies.

## Reporting a vulnerability

Please use the repository's private security advisory feature or open a
confidential issue. We commit to:

1. acknowledging within 14 days;
2. patching verified vulnerabilities in the affected code paths;
3. crediting reporters (unless anonymity is requested).

## Scope notes

- `07_web_lab/index.html` is a static file — open it locally; do not deploy
  it behind a public reverse proxy without adding CSP headers first.
- `06_code/*/run.*` scripts read only files inside this package; they do not
  accept remote input by default. If you wire the `api` mode of a runner to
  the network, you own its security posture.
- The `reproduce.sh` script is intentionally boring: it pins the seed,
  the config and the Python version, and it writes only inside `./out`.
