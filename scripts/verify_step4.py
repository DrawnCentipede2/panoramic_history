"""Step 4 sanity check: blocking gate + Start button wiring (no permission yet)."""

import urllib.request

URL = "http://127.0.0.1:8765/index.html"
html = urllib.request.urlopen(URL).read().decode("utf-8")

checks = {
    "has_gate_layer": 'id="gate-layer"' in html,
    "has_start_btn": 'id="start-btn"' in html,
    "has_start_label": "Start Time Travel" in html,
    "has_brand": "TimePortal // Checkpoint Charlie" in html,
    "has_gate_hidden_class": "#gate-layer.is-hidden" in html,
    "has_blur_gate": "backdrop-filter: blur" in html,
    "has_start_click": 'startBtn.addEventListener("click"' in html,
    "has_start_experience": "function startExperience" in html,
    "no_permission_yet": "requestPermission" not in html,
    "has_preload_autoload": "autoLoad: true" in html,
    "has_step4_banner": "Step 4 check" in html,
    "ui_revealed_after_start": "body.has-started #ui-layer" in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("bytes:", len(html))
print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")
