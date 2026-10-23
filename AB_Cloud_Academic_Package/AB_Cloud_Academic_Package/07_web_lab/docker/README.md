<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ 07_web_lab/](../README.md) · [🏠 Root README](../../../../README.md)**

</div>
# docker/

Serve the laboratory in a container:

```dockerfile
FROM python:3.12-slim
WORKDIR /lab
COPY ../index.html /lab/index.html
EXPOSE 8000
CMD ["python3", "-m", "http.server", "8000"]
```

or simply `python3 -m http.server 8322` in `07_web_lab/` — the laboratory
is a static file and needs no server at all.

<div align="center">

<img src="../../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
