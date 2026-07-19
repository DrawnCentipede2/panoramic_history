"""Step 2 sanity check: theme tokens + overlay layer structure exist."""

import urllib.request

URL = "http://127.0.0.1:8765/index.html"
html = urllib.request.urlopen(URL).read().decode("utf-8")

checks = {
    "has_theme_vars": "--bg: #121212" in html and "--z-modal: 30" in html,
    "has_panorama": 'id="panorama"' in html,
    "has_ui_layer": 'id="ui-layer"' in html,
    "has_gate_layer": 'id="gate-layer"' in html,
    "has_modal_layer": 'id="modal-layer"' in html,
    "has_watermark": 'id="watermark"' in html,
    "has_safety": 'id="safety-alert"' in html,
    "has_minimap": 'id="minimap"' in html,
    "has_unlock": 'id="unlock-cta"' in html,
    "has_brand": "TimePortal // Checkpoint Charlie" in html,
    "has_safe_area": "safe-area-inset-top" in html,
    "has_step2_banner": "Step 2 check" in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("bytes:", len(html))
print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")
