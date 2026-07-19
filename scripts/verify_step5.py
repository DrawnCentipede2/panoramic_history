"""Step 5 sanity check: orientation permission flow + touch fallback wiring."""

import urllib.request

URL = "http://127.0.0.1:8765/index.html"
html = urllib.request.urlopen(URL).read().decode("utf-8")

checks = {
    "has_request_permission": "DeviceOrientationEvent.requestPermission" in html,
    "has_start_orientation": "viewer.startOrientation" in html,
    "has_permission_state": "permissionState" in html,
    "has_control_hint": 'id="control-hint"' in html,
    "has_fallback_hint": "Drag with your finger to look around." in html,
    "has_gyro_hint": "Move your phone to look around" in html,
    "has_step5_banner": "Step 5 UX check" in html,
    "orientation_off_by_default": "orientationOnByDefault: false" in html,
    "has_secure_context_check": "isSecureContext" in html,
    "has_top_bar": 'id="top-bar"' in html,
    "has_fullscreen_helper": "tryEnterFullscreen" in html,
    "has_viewer_resize": "viewer.resize" in html,
    "has_safety_consent": 'id="safety-check"' in html,
    "no_persistent_safety_pill": 'id="safety-alert"' not in html,
    "has_fullscreen_toggle_btn": 'id="fullscreen-btn"' in html,
    "has_toggle_fullscreen_fn": "function toggleFullscreen" in html,
    "has_enter_icon": 'class="icon-enter"' in html,
    "has_exit_icon": 'class="icon-exit"' in html,
    "hint_centered": "top: 42%" in html,
}

for name, ok in checks.items():
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

print("bytes:", len(html))
print("RESULT:", "ALL_OK" if all(checks.values()) else "FAIL")
