"""Step 8 sanity check: 10s interaction timer + unlock CTA fade-in."""

import urllib.request

URL = "http://127.0.0.1:8765/index.html"
html = urllib.request.urlopen(URL).read().decode("utf-8")

checks = {
    "has_unlock_cta": 'id="unlock-cta"' in html,
    "has_unlock_label": "Unlock 1961 Tank Crisis Era" in html,
    "has_goal_10s": "INTERACTION_GOAL_MS = 10000" in html,
    "has_timer_tick": "function tickInteractionTimer" in html,
    "has_show_unlock": "function showUnlockCta" in html,
    "has_visibility_pause": "visibilitychange" in html,
    "has_is_visible_class": "#unlock-cta.is-visible" in html,
    "binds_timer_on_start": "startInteractionTimer();" in html,
    "has_step8_banner": "Step 8 check" in html,
    "exposes_interaction_ms": "getInteractionMs" in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("bytes:", len(html))
print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")
