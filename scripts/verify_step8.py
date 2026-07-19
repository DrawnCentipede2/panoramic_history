"""Step 8–9 sanity check: dismissible unlock FAB + waitlist modal."""

import urllib.request

URL = "http://127.0.0.1:8765/index.html"
html = urllib.request.urlopen(URL).read().decode("utf-8")

checks = {
    "has_unlock_fab": 'id="unlock-fab"' in html,
    "has_fab_dismiss": 'id="unlock-fab-dismiss"' in html,
    "has_fab_open": 'id="unlock-fab-open"' in html,
    "has_visible_time_timer": "Visible-time timer started" in html,
    "no_gyro_required_for_fab": "Tilt/pan are NOT required" in html,
    "has_session_dismiss": "timeportal_unlock_dismissed" in html,
    "has_modal_layer": 'id="modal-layer"' in html,
    "has_waitlist_form": 'id="waitlist-form"' in html,
    "has_email_input": 'id="waitlist-email"' in html,
    "has_success_copy": "You're on the list. See you in the past." in html,
    "has_open_modal_fn": "function openWaitlistModal" in html,
    "has_auto_close_success": "function finishWaitlistSuccess" in html,
    "has_subscribed_session_key": "timeportal_waitlist_joined" in html,
    "has_step89_banner": "Steps 8–9 check" in html,
    "no_giant_unlock_bar_id": 'id="unlock-cta"' not in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("bytes:", len(html))
print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")
