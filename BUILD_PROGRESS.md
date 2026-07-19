# TimePortal // Checkpoint Charlie — Build Progress

This file tracks the step-by-step MVP build.  
**Rule:** Do not start the next step until the current step is marked ✅ and verified.

Last updated: 2026-07-19

---

## Build plan (overview)

| Step | Name | Status |
|------|------|--------|
| 1 | Project scaffold + full-screen HTML shell | ✅ Done |
| 2 | Dark theme CSS + z-index overlay layers | ✅ Done |
| 3 | Pannellum + loading spinner + test panorama | ⏳ Pending (placeholder image OK) |
| 4 | Onboarding gate UI (no permission yet) | ⏳ Pending |
| 5 | Device orientation permission + touch fallback | ⏳ Pending |
| 6 | Auto-rotate affordance + kill on input | ⏳ Pending |
| 7 | Persistent overlays (watermark, safety, minimap) | ⏳ Pending |
| 8 | 10s interaction timer + unlock CTA | ⏳ Pending |
| 9 | Lead-gen modal + email validation | ⏳ Pending |
| 10 | Telemetry + subscribe fetch stubs | ⏳ Pending |
| 11 | Final smoke-test on real phone | ⏳ Pending |

Status legend: ⏳ Pending · 🔄 In progress · ✅ Done · ❌ Blocked · ⏸️ Waiting on user

---

## Open questions / data needed from user

Answer these before or during later steps. Leave blank until answered.

1. **Panorama image URL or local file**  
   - Status: ✅ Decided for now  
   - User answer: Real image coming later. Use a **public Pannellum demo/placeholder** equirectangular image in Step 3; swap when ready.  
   - Swap point: one constant near top of JS (e.g. `PANORAMA_URL`).

2. **How will you open the page for phone tests?**  
   - Status: ✅ Decided  
   - User answer: Same Wi‑Fi + localhost (PC runs server; phone opens `http://<PC-LAN-IP>:port`).  
   - Note: iOS gyro permission often needs a secure context; if permission fails on plain HTTP LAN, we may need a quick HTTPS tunnel later.

3. **Backend for `/api/v1/telemetry` and `/api/v1/subscribe`**  
   - Status: ✅ Decided  
   - Decision: **Hybrid (recommended)**  
     - Frontend: always use resilient `fetch` stubs + configurable `API_BASE`.  
     - Step 10: add a tiny local FastAPI mock so Network tab shows real `200` responses for fast validation.  
     - Long term: same routes/contracts; swap mock for real FastAPI without rewriting the page.

4. **Exact brand copy confirmation**  
   - Status: ✅ Decided  
   - User answer: Keep `TimePortal // Checkpoint Charlie` for now; change anytime.

---

## Step 1 — Project scaffold + full-screen HTML shell

### Goal
Create the repo files and a minimal `index.html` that:
- Fills the visible viewport (no body scrolling)
- Uses a fixed full-screen app shell (`100dvh` with fallback)
- Contains an empty panorama container div and a visible “Step 1 OK” marker so we can verify layout

### Files created
- `BUILD_PROGRESS.md` — this progress log
- `index.html` — minimal full-screen shell only (no Pannellum yet)

### What this step intentionally does NOT include
- Pannellum
- Gyroscope / permissions
- Real UI overlays, modal, telemetry

### How to verify (you can do this in a desktop browser)
1. Open `index.html` in Chrome or Edge (double-click is fine for Step 1).
2. You should see a dark full-screen page with centered text: `Step 1 OK — full-screen shell`.
3. Try scrolling with mouse wheel or touchpad → **page must not scroll**.
4. Resize the window → the dark area should still cover the whole window (no white gaps).

### Verification result
- Agent self-check (automated): ✅ PASS  
  - Local server: `http://127.0.0.1:8765/index.html`  
  - Script: `python scripts/verify_step1.py` → `ALL_OK`  
  - Confirmed present: `#app`, `#panorama`, Step 1 marker, `overflow: hidden`, `100dvh`, `position: fixed`  
  - Could NOT verify visually (Browser MCP not connected): no-scroll + full-window fill still need your eyes
- User cross-check: ✅ Pass (popup visible, not scrollable)  
- Marked complete: ✅ Yes (2026-07-19)

### Notes / issues
- None.

---

## Step 2 — Dark theme + overlay layers

### Goal
Add CSS theme tokens and four stacked overlay layers with labeled placeholders:
- z0 `#panorama`
- z10 `#ui-layer` (watermark, safety, minimap, unlock)
- z20 `#gate-layer` (semi-transparent for visual stack check)
- z30 `#modal-layer` (preview only)

### What this step intentionally does NOT include
- Real Pannellum / panorama image
- Working Start button / permissions
- Real modal form / telemetry

### How to verify
1. Hard-refresh: `http://127.0.0.1:8765/index.html`
2. Top banner says **Step 2 check**
3. You can see/read labels: `z0`, `z10`, `z20`, `z30`
4. Gate is dimmed but UI chips underneath are still partly visible
5. Modal preview sits near the bottom **above** the gate
6. Page still does not scroll

### Verification result
- Agent self-check: ✅ `python scripts/verify_step2.py` → `ALL_OK`
- User cross-check: ✅ Pass (2026-07-19)
- Marked complete: ✅ Yes

### Notes / issues
- Gate was intentionally semi-transparent in Step 2 only.
- Design note from user: prefer warm archival / history-hint brown tones over pure black (not generic brown). Defer full palette polish to a later pass; keep CSS variables so the swap is easy.

---

## Later steps (stubs — fill in when we reach them)

### Step 3 — Pannellum + spinner + panorama
- Status: ⏳ Pending  
- Will use placeholder equirectangular image until real asset arrives  
- Verification: _TBD_

### Step 4 — Onboarding gate UI
- Status: ⏳ Pending  
- Verification: _TBD_

### Step 5 — Orientation permission flow
- Status: ⏳ Pending  
- Blocked until: HTTPS/localhost phone test method  
- Verification: _TBD_ (needs real iPhone/Android)

### Step 6 — Auto-rotate
- Status: ⏳ Pending  
- Verification: _TBD_

### Step 7 — Persistent overlays
- Status: ⏳ Pending  
- Verification: _TBD_

### Step 8 — Interaction timer + unlock CTA
- Status: ⏳ Pending  
- Verification: _TBD_

### Step 9 — Lead-gen modal
- Status: ⏳ Pending  
- Verification: _TBD_

### Step 10 — Telemetry stubs
- Status: ⏳ Pending  
- Verification: _TBD_

### Step 11 — Final smoke test
- Status: ⏳ Pending  
- Verification: real-device checklist from the build prompt

---

## Decision log
| Date | Decision |
|------|----------|
| 2026-07-19 | Build in small verified steps; stop after each step until verified. |
| 2026-07-19 | Track progress in this markdown file for future context. |
| 2026-07-19 | Use placeholder panorama until real Checkpoint Charlie asset is found. |
| 2026-07-19 | Phone testing via same Wi‑Fi localhost. |
| 2026-07-19 | Backend: resilient frontend stubs + tiny FastAPI mock at Step 10. |
| 2026-07-19 | Brand text kept; editable anytime. |
| 2026-07-19 | Color direction: warm archival brown (history hint), not pure black; polish later via CSS variables. |
| 2026-07-19 | Git: commit + push after each verified step to GitHub repo `panoramic_history` (DrawnCentipede2). |
