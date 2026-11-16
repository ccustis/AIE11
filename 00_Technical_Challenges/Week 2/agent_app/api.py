"""The FastAPI app: routes and startup wiring. This file is written for you.

    uv run python -m agent_app        # starts the server on http://127.0.0.1:8000

Read it, don't rewrite it. It builds your agent ONCE at startup and holds it for the
life of the process (the "index once, not per request" point from index.py). Because
Qdrant is on disk, the first boot embeds and the next boots load from disk for free. Until
your stubs are filled, startup catches the NotImplementedError, the server still comes up,
and /ask replies 501 telling you which file to open. So /health, /docs, and the frontend
all work while you build.

Endpoints:
    GET  /         -> the starter frontend (frontend/index.html) — replace it with your own
    GET  /health   -> {"status": "ok", "agent_ready": bool}
    POST /ask      -> AskRequest in, AskResponse out (your contract, in schemas.py)
    GET  /docs     -> interactive API docs, generated from the Pydantic models for free
"""

import sys
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from . import service
from .schemas import AskRequest, AskResponse

APP_DIR = Path(__file__).resolve().parent
DATA_DIR = APP_DIR.parent / "data"
FRONTEND_DIR = APP_DIR.parent / "frontend"


def find_corpus() -> Path | None:
    """The single .txt in data/. Drop your own in and it is found; two and it won't guess."""
    found = sorted(DATA_DIR.glob("*.txt"))
    return found[0] if len(found) == 1 else None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Build the agent once, before the first request. Store it (or the reason it failed)."""
    app.state.agent = None
    app.state.startup_error = None
    corpus = find_corpus()
    if corpus is None:
        app.state.startup_error = f"Expected exactly one .txt in {DATA_DIR}/."
    else:
        try:
            app.state.agent = service.build_agent(corpus)
            print(f"[agent_app] agent ready — indexed {corpus.name}", file=sys.stderr)
        except NotImplementedError as exc:
            # A stub is still unwritten. Come up anyway so /health and /docs work.
            app.state.startup_error = str(exc)
            print(f"[agent_app] not ready yet: {exc}", file=sys.stderr)
    yield


app = FastAPI(title="Agentic Wellness Search", version="0.1.0", lifespan=lifespan)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "agent_ready": app.state.agent is not None}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    """Answer one question with the agentic-RAG graph."""
    if app.state.agent is None:
        # 501 Not Implemented: the agent could not be built. The message names the stub.
        raise HTTPException(status_code=501, detail=app.state.startup_error or "Agent not ready.")
    try:
        return service.answer_question(request, app.state.agent)
    except NotImplementedError as exc:
        raise HTTPException(status_code=501, detail=str(exc))


@app.get("/")
def frontend() -> FileResponse:
    """Serve the starter page. Students: replace frontend/index.html with your own UI."""
    return FileResponse(FRONTEND_DIR / "index.html")
