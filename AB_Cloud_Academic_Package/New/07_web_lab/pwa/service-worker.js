// AB-Cloud web lab service worker — offline-first (the lab is already offline)
const CACHE = "abcloud-lab";
self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(["../index.html"])));
  self.skipWaiting();
});
self.addEventListener("fetch", (e) => {
  e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request)));
});
