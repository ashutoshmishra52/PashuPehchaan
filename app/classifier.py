"""Indian bovine breed recognition via Hugging Face ConvNeXt model.

Model: ujjwal75/indian-bovine-breeds-model (ConvNeXt-Tiny, 41 breeds)
This replaces the old colour/CLIP heuristics that kept predicting Deoni.
"""

from __future__ import annotations

import io
import json
import logging
import threading
from pathlib import Path
from typing import Any

import torch
from PIL import Image
from torchvision import transforms

from .breeds import BREEDS, get_breed_info, normalize_breed_name

logger = logging.getLogger(__name__)

HF_REPO = "ujjwal75/indian-bovine-breeds-model"
WEIGHTS_FILE = "Indian_bovine_finetuned_model.pth"
CLASSES_FILE = "classes.json"

_lock = threading.Lock()
_model = None
_classes: list[str] = []
_device = "cpu"
_ready = False
_load_error: str | None = None
_transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


def is_ready() -> bool:
    return _ready


def load_error() -> str | None:
    return _load_error


def preload() -> None:
    _ensure_model()


def _is_lfs_pointer(path: Path) -> bool:
    """True when Git LFS was not pulled and only a tiny pointer file exists."""
    try:
        if path.stat().st_size > 2048:
            return False
        head = path.read_text(encoding="utf-8", errors="ignore")[:200]
        return "git-lfs.github.com" in head or head.startswith("version https://")
    except OSError:
        return False


def _resolve_artifact(filename: str) -> Path:
    """Prefer project-local copy, then Hugging Face cache / download."""
    local = Path(__file__).resolve().parent.parent / "models" / filename
    if local.exists() and not _is_lfs_pointer(local):
        return local

    if local.exists() and _is_lfs_pointer(local):
        logger.warning(
            "%s looks like a Git LFS pointer (run: git lfs pull). "
            "Downloading model from Hugging Face instead…",
            filename,
        )

    from huggingface_hub import hf_hub_download

    try:
        path = hf_hub_download(HF_REPO, filename, local_files_only=True)
    except Exception:
        logger.info("Downloading %s from Hugging Face…", filename)
        path = hf_hub_download(HF_REPO, filename)

    # Cache into models/ for next run
    try:
        dest = local
        dest.parent.mkdir(parents=True, exist_ok=True)
        if Path(path).resolve() != dest.resolve():
            import shutil

            shutil.copy2(path, dest)
            return dest
    except OSError as exc:
        logger.warning("Could not cache model locally: %s", exc)

    return Path(path)


def _ensure_model():
    global _model, _classes, _device, _ready, _load_error
    if _ready:
        return
    with _lock:
        if _ready:
            return
        try:
            import timm

            _device = (
                "mps"
                if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available()
                else "cpu"
            )
            logger.info("Loading Indian bovine breed model on %s …", _device)

            weights_path = _resolve_artifact(WEIGHTS_FILE)
            classes_path = _resolve_artifact(CLASSES_FILE)
            with open(classes_path, encoding="utf-8") as f:
                _classes = json.load(f)

            ckpt = torch.load(weights_path, map_location="cpu", weights_only=False)
            if isinstance(ckpt, dict) and "classes" in ckpt and ckpt["classes"]:
                _classes = list(ckpt["classes"])
            state = ckpt["model_state_dict"] if isinstance(ckpt, dict) and "model_state_dict" in ckpt else ckpt

            model = timm.create_model(
                "convnext_tiny",
                pretrained=False,
                num_classes=len(_classes),
                drop_path_rate=0.2,
            )
            model.load_state_dict(state, strict=True)
            model.eval()
            model.to(_device)
            _model = model
            _ready = True
            _load_error = None
            logger.info("Bovine model ready (%d breeds)", len(_classes))
        except Exception as exc:  # noqa: BLE001
            _load_error = str(exc)
            logger.exception("Failed to load bovine model: %s", exc)
            raise


def _load_image(data: bytes) -> Image.Image:
    img = Image.open(io.BytesIO(data)).convert("RGB")
    max_side = 1024
    w, h = img.size
    scale = min(1.0, max_side / max(w, h))
    if scale < 1.0:
        img = img.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    return img


@torch.inference_mode()
def _predict_probs(img: Image.Image) -> list[tuple[str, float]]:
    _ensure_model()
    tensor = _transform(img).unsqueeze(0).to(_device)
    logits = _model(tensor)[0]
    probs = torch.softmax(logits, dim=0)
    ranked = sorted(
        ((_classes[i], float(probs[i])) for i in range(len(_classes))),
        key=lambda x: x[1],
        reverse=True,
    )
    return ranked


def predict_breed(image_bytes: bytes) -> dict[str, Any]:
    img = _load_image(image_bytes)
    ranked = _predict_probs(img)

    top_label, top_p = ranked[0]
    breed = normalize_breed_name(top_label)
    confidence = round(min(99.0, max(1.0, top_p * 100)), 1)
    info = get_breed_info(breed)

    alternatives = []
    for label, p in ranked[1:4]:
        name = normalize_breed_name(label)
        alternatives.append(
            {
                "breed": name,
                "confidence": round(min(99.0, max(0.1, p * 100)), 1),
                "type": get_breed_info(name)["type"],
            }
        )

    return {
        "breed": breed,
        "confidence": confidence,
        "animal_type": info["type"],
        "method": "convnext_bovine",
        "details": info,
        "alternatives": alternatives,
    }
