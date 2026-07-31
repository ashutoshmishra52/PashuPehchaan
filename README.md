# PashuPehchaan

Image Based Breed Recognition for Cattle and Buffaloes of India — local web app.

## Run on localhost

```bash
# needs Git LFS for the AI model (~320MB)
git lfs install
git clone https://github.com/ashutoshmishra52/PashuPehchaan.git
cd PashuPehchaan
npm run setup   # optional first-time Python deps
npm run dev
```

Open **http://127.0.0.1:8000**

First run auto-creates the Python venv and installs packages.

## Features

- Upload cattle/buffalo photo (drag & drop or browse)
- **AI breed prediction** using a trained Indian bovine model
  (`ujjwal75/indian-bovine-breeds-model` — ConvNeXt-Tiny, 41 breeds)
- Details: region, milk yield, lifespan, usage
- Alternative likely matches
- Breed library for common Indian cattle & buffalo

On first setup the model (~320MB) is downloaded into `models/` (or Hugging Face cache).

## API

- `GET /` — web UI
- `GET /api/breeds` — list breeds
- `GET /api/breeds/{name}` — breed details
- `POST /api/predict` — upload image (`multipart/form-data`, field `file`)
