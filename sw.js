self.addEventListener("install", function(e) {
  e.waitUntil(
    caches.open("calculator-cache").then(function(cache) {
      return cache.addAll(["./"]);
    })
  );
});

self.addEventListener("fetch", function(e) {
  e.respondWith(
    caches.match(e.request).then(function(res) {
      return res || fetch(e.request);
    })
  );
});
