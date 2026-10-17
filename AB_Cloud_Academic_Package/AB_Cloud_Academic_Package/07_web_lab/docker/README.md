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
