"""Step 6 sanity check: auto-rotate affordance + kill-on-input wiring."""

import urllib.request

URL = "http://127.0.0.1:8765/index.html"
html = urllib.request.urlopen(URL).read().decode("utf-8")

checks = {
    "has_start_auto_rotate": "function startAutoRotateAffordance" in html,
    "has_stop_auto_rotate": "function stopAutoRotateAffordance" in html,
    "has_reduced_motion": "prefers-reduced-motion" in html,
    "has_kill_listeners": "function bindAutoRotateKillListeners" in html,
    "has_gyro_threshold": "GYRO_KILL_THRESHOLD" in html,
    "has_pointer_kill": 'addEventListener("pointerdown"' in html,
    "calls_start_on_begin": "startAutoRotateAffordance();" in html,
    "has_step6_banner": "Step 6 check" in html,
    "exposes_is_auto_rotating": "isAutoRotating" in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("bytes:", len(html))
print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")
