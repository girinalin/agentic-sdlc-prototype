# Agentic SDLC Prototype

This repository is the working foundation for an AI-enabled SDLC engine. It
combines a small FastAPI and React CRUD application with governed development
assets under `.agentic/`:

- Instructions define coding, testing, deployment, and lifecycle standards.
- Prompts define repeatable task workflows.
- Skills describe reusable repository analysis, scaffolding, and test coverage capabilities.
- Agents define planner, implementer, quality, and operations responsibilities.

The CRUD application is intentionally small. It provides a stable target for
evolving the repository into an SDLC control plane without replacing the
existing foundation.

## Run Locally

### Backend

```bash
python3 -m venv backend/.venv
backend/.venv/bin/pip install -r backend/requirements.txt
backend/.venv/bin/uvicorn backend.src.main:app --reload
```

The API is available at `http://localhost:8000`. OpenAPI documentation is at
`http://localhost:8000/docs`.

### Frontend

```bash
cd frontend
npm ci
npm run dev
```

The frontend is available at `http://localhost:5173`.

## Verify

```bash
backend/.venv/bin/pytest --cov=backend/src
cd frontend && npm run build
```

## Current API

- `GET /health`
- `GET /api/items`
- `GET /api/items/{item_id}`
- `POST /api/items`
- `PUT /api/items/{item_id}`
- `DELETE /api/items/{item_id}`

Storage is currently in memory and resets when the backend process restarts.
