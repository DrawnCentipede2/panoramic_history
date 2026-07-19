"""Step 7 sanity check: watermark polish + SVG minimap with Stand Here marker."""

import urllib.request

URL = "http://127.0.0.1:8765/index.html"
html = urllib.request.urlopen(URL).read().decode("utf-8")

checks = {
    "has_watermark": 'id="watermark"' in html,
    "has_brand_text": "TimePortal // Checkpoint Charlie" in html,
    "has_minimap": 'id="minimap"' in html,
    "has_svg_minimap": "<svg" in html and "Friedrichstr." in html,
    "has_zimmerstr": "Zimmerstr." in html,
    "has_stand_here": "Stand Here" in html,
    "has_stand_dot": "stand-dot" in html,
    "has_blink_animation": "stand-blink" in html,
    "unlock_hidden_for_now": 'id="unlock-cta"' in html and "display: none" in html,
    "has_step7_banner": "Step 7 check" in html,
    "no_minimap_placeholder_text": "Minimap placeholder" not in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("bytes:", len(html))
print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")
