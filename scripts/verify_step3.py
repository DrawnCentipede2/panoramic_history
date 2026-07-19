"""Step 3 sanity check: Pannellum assets, placeholder URL, spinner, viewer init."""

import urllib.request

URL = "http://127.0.0.1:8765/index.html"
html = urllib.request.urlopen(URL).read().decode("utf-8")

checks = {
    "has_pannellum_css_2_5_7": "pannellum@2.5.7/build/pannellum.css" in html,
    "has_pannellum_js_2_5_7": "pannellum@2.5.7/build/pannellum.js" in html,
    "has_placeholder_url": "assets/placeholder-panorama.jpg" in html,
    "has_panorama_url_constant": "PANORAMA_URL" in html,
    "has_autoload": "autoLoad: true" in html,
    "has_loading_overlay": 'id="loading-overlay"' in html,
    "has_spinner": 'class="spinner"' in html,
    "has_viewer_init": 'pannellum.viewer("panorama"' in html,
    "has_load_handler": 'viewer.on("load"' in html,
    "has_step3_banner": "Step 3 check" in html,
    "has_warm_bg_token": "--bg: #1a1612" in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("bytes:", len(html))
print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")
