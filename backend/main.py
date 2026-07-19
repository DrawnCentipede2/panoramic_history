"""
Tiny FastAPI mock for TimePortal smoke tests.

Serves:
- POST /api/v1/telemetry
- POST /api/v1/subscribe
- Static frontend files from the project root (same origin → no CORS pain)

Run from the project root:
  python -m uvicorn backend.main:app --host 0.0.0.0 --port 8765

Then open on phone:
  http://<PC-LAN-IP>:8765/
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

# Project root = parent of /backend
ROOT_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="TimePortal mock API", version="0.1.0")

# Allow local/dev frontends (also fine when same-origin via StaticFiles)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TelemetryEvent(BaseModel):
    """Matches the frontend telemetry payload shape."""

    event: str
    ts: str
    sessionId: str
    userAgent: Optional[str] = None
    permission: Optional[str] = None


class SubscribeBody(BaseModel):
    """Waitlist signup payload from the email modal."""

    email: str = Field(min_length=3)
    sessionId: Optional[str] = None


# In-memory lists so you can inspect recent traffic during a smoke test
TELEMETRY_LOG: list[dict[str, Any]] = []
SUBSCRIBE_LOG: list[dict[str, Any]] = []


@app.get("/api/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/v1/telemetry")
def post_telemetry(body: TelemetryEvent) -> dict[str, Any]:
    # Keep a small ring buffer for debugging
    item = body.model_dump()
    TELEMETRY_LOG.append(item)
    if len(TELEMETRY_LOG) > 200:
        TELEMETRY_LOG.pop(0)
    print("[telemetry]", item)
    return {"ok": True}


@app.post("/api/v1/subscribe")
def post_subscribe(body: SubscribeBody) -> dict[str, Any]:
    item = body.model_dump()
    SUBSCRIBE_LOG.append(item)
    if len(SUBSCRIBE_LOG) > 200:
        SUBSCRIBE_LOG.pop(0)
    print("[subscribe]", item)
    return {"ok": True, "email": body.email}


@app.get("/api/v1/debug/recent")
def debug_recent() -> dict[str, Any]:
    """Optional helper to peek at recent events while testing."""
    return {
        "telemetry": TELEMETRY_LOG[-20:],
        "subscribe": SUBSCRIBE_LOG[-20:],
    }


# Mount static site LAST so /api routes stay available
app.mount(
    "/",
    StaticFiles(directory=str(ROOT_DIR), html=True),
    name="site",
)
