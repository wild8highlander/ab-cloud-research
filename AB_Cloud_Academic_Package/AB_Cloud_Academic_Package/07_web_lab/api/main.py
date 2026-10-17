"""The FastAPI face of the AB-Cloud web laboratory.

Run: python3 main.py   (or uvicorn main:app --reload)
Serves the registry read-only; the honesty layer is part of every response.
"""
import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

ROOT = Path(__file__).resolve().parent.parent.parent
REG = ROOT / "02_data" / "processed" / "research_registry.json"

app = FastAPI(
    title="AB-Cloud Web Lab API",
    description="Read-only view of the unified research registry. "
                "RH status: certified (V13, unlocked) — 0 assumptions on the path.",
)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["GET"])

@app.get("/")
def root():
    return {"programme": "AB-Cloud", "rh_status": "certified", "endpoints": ["/registry", "/verdicts", "/flagship", "/numbers", "/lab"]}

@app.get("/registry")
def registry():
    return json.loads(REG.read_text(encoding="utf-8"))

@app.get("/verdicts")
def verdicts():
    return json.loads(REG.read_text(encoding="utf-8"))["verdicts"]

@app.get("/flagship")
def flagship():
    return json.loads(REG.read_text(encoding="utf-8"))["flagship_results"]

@app.get("/numbers")
def numbers():
    return json.loads(REG.read_text(encoding="utf-8"))["numbers_registry"]

@app.get("/lab")
def lab():
    index = ROOT / "07_web_lab" / "index.html"
    if not index.exists():
        raise HTTPException(404, "index.html not found")
    return FileResponse(index, media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8321)
