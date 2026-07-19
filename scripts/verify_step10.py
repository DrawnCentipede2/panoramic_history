"""Step 10 sanity check: telemetry helpers + FastAPI mock files exist."""

import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / "index.html").read_text(encoding="utf-8")

checks = {
    "has_session_id": "createSessionId" in html,
    "has_send_telemetry": "function sendTelemetry" in html,
    "has_page_loaded": 'sendTelemetry("page_loaded")' in html,
    "has_unlock_shown_event": 'sendTelemetry("unlock_shown")' in html,
    "has_unlock_clicked_event": 'sendTelemetry("unlock_clicked")' in html,
    "has_subscribe_session": "sessionId: sessionId" in html,
    "subscribe_requires_ok": "Subscribe failed with status" in html,
    "has_backend_main": (ROOT / "backend" / "main.py").exists(),
    "has_requirements": (ROOT / "requirements.txt").exists(),
    "has_step10_banner": "Step 10 check" in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")

# Optional live check if mock is already running
try:
    health = urllib.request.urlopen("http://127.0.0.1:8765/api/v1/health", timeout=2)
    print("live_health:", health.status, health.read().decode())
except Exception as err:
    print("live_health: SKIPPED (", err, ")")
