# PashuPehchaan

Image Based Breed Recognition for Cattle and Buffaloes of India — local web app.

## Requirements

Install these **before** cloning/running:

| Tool | Why |
|------|-----|
| **Python 3.9–3.12** | Backend + AI model |
| **Node.js 18+** (npm) | `npm run dev` launcher |
| **Git** + **Git LFS** | Clone repo and pull ~320MB model |
| **~2 GB free disk** | Python packages + model |
| **8 GB RAM** recommended | Model inference |

```bash
# macOS (Homebrew)
brew install python node git git-lfs
git lfs install

# Windows: install Python from python.org, Node from nodejs.org,
# Git from git-scm.com, then: git lfs install
```

## Run on localhost

```bash
git lfs install
git clone https://github.com/ashutoshmishra52/PashuPehchaan.git
cd PashuPehchaan
git lfs pull          # important: downloads the AI model
npm run setup         # creates .venv + installs Python deps
npm run dev
```

Open **http://127.0.0.1:8000**

> If you forgot `git lfs pull`, the app can still **auto-download** the model from Hugging Face on first start (needs internet).

## Features

- Upload cattle/buffalo photo (drag & drop or browse)
- **AI breed prediction** using a trained Indian bovine model  
  (`ujjwal75/indian-bovine-breeds-model` — ConvNeXt-Tiny, 41 breeds)
- Details: region, milk yield, lifespan, usage
- Alternative likely matches
- Breed library for common Indian cattle & buffalo

## API

- `GET /` — web UI
- `GET /api/health` — model ready status
- `GET /api/breeds` — list breeds
- `GET /api/breeds/{name}` — breed details
- `POST /api/predict` — upload image (`multipart/form-data`, field `file`)

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Model / prediction errors | `git lfs pull` or wait for Hugging Face download on first run |
| `python` / `python3` not found | Install Python 3.9–3.12 and reopen terminal |
| `npm` not found | Install Node.js 18+ |
| Port 8000 busy | Stop other apps using 8000, or change port in `scripts/dev.js` |
| Torch install fails | Use Python 3.10/3.11; avoid very new 3.13 if wheels missing |
| Slow first start | Normal — packages/model install/download once |

## Note

`.venv` and `.env` are **not** in the repo (local only). Each machine creates its own virtualenv via `npm run setup`.
