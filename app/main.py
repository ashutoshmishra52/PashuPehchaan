"""FastAPI app — Image Based Breed Recognition for Cattle & Buffaloes of India."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .breeds import get_breed_info, list_breeds
from .classifier import is_ready, load_error, predict_breed, preload

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"


@asynccontextmanager
async def lifespan(_app: FastAPI):
    logger.info("Loading Indian bovine AI model (first time may download ~320MB)…")
    try:
        preload()
        logger.info("AI model ready")
    except Exception as exc:  # noqa: BLE001
        logger.error("AI model failed to load: %s — colour fallback will be used", exc)
    yield


app = FastAPI(
    title="PashuPehchaan",
    description="Image Based Breed Recognition for Cattle and Buffaloes of India",
    version="1.0.0",
    lifespan=lifespan,
)

app.mount("/static", StaticFiles(directory=str(STATIC)), name="static")

ALLOWED = {"image/jpeg", "image/jpg", "image/png", "image/webp", "image/bmp"}
MAX_BYTES = 8 * 1024 * 1024  # 8 MB


@app.get("/")
async def home():
    return FileResponse(STATIC / "index.html")


@app.get("/api/health")
async def health():
    return {
        "ok": True,
        "model_ready": is_ready(),
        "model_error": load_error(),
    }


@app.get("/api/breeds")
async def breeds():
    return {"breeds": list_breeds()}


@app.get("/api/breeds/{name}")
async def breed_detail(name: str):
    info = get_breed_info(name)
    if "type" not in info:
        raise HTTPException(404, "Breed not found")
    return info


@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    if file.content_type and file.content_type.lower() not in ALLOWED:
        raise HTTPException(400, "Please upload a JPG, PNG, or WEBP image.")

    data = await file.read()
    if not data:
        raise HTTPException(400, "Empty file.")
    if len(data) > MAX_BYTES:
        raise HTTPException(400, "Image too large (max 8 MB).")

    try:
        result = predict_breed(data)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(400, f"Could not process image: {exc}") from exc

    return result
