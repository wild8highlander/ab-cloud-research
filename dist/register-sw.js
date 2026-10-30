/**
 * register-sw.js — service worker registration for the AB-Cloud portal.
 *
 * Kept as an EXTERNAL file (not inline) so the strict CSP from pxxl.toml
 * (script-src 'self') allows it without any hash/nonce bookkeeping.
 * Registration failures are silent by design: without SW the portal simply
 * behaves as a classic multi-page site.
 */
if (
  'serviceWorker' in navigator &&
  (location.protocol === 'https:' || ['localhost', '127.0.0.1', '[::1]'].includes(location.hostname))
) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js', { scope: '/' }).catch(() => {
      /* offline mode is a progressive enhancement — never break the page */
    });
  });
}
