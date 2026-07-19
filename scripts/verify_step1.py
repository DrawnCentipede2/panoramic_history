"""Simple Step 1 sanity check: page serves and contains required shell pieces."""

import urllib.request

URL = "http://127.0.0.1:8765/index.html"
html = urllib.request.urlopen(URL).read().decode("utf-8")

checks = {
    "has_app": 'id="app"' in html,
    "has_panorama": 'id="panorama"' in html,
    "has_step1_marker": "Step 1 OK" in html,
    "has_overflow_hidden": "overflow: hidden" in html,
    "has_100dvh": "100dvh" in html,
    "has_position_fixed": "position: fixed" in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("bytes:", len(html))
print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")
