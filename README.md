# Folding@Home Monitor Integration (v8)

This is a custom [Home Assistant](https://www.home-assistant.io/) integration to **monitor and control Folding@Home** clients running version 8.x or later. It connects directly to the Folding@Home client via **WebSocket** and exposes:

- ✅ Real-time telemetry from active work units
- 🎛 Control over folding state (start/pause)
- 📊 Sensors for PPD, ETA, progress, and core type

> ⚠️ Note: This integration is **only compatible with Folding@Home v8+.** The backend architecture in v8 is completely different from v7 (replacing `FAHClient` XML with WebSocket JSON APIs).

---

## 🚧 Project Status

> This integration is under active development and not yet feature-complete. Expect breaking changes and missing features.

Planned:
- Full UI-based config via Home Assistant’s config flow
- More sensors (failed WUs, GPU state, battery status)
- HACS support
- Multi-client support

---

## 💡 Why This Project?

[Folding@Home v8](https://foldingathome.org) introduced a **new JSON-based WebSocket API**, rendering older integrations incompatible — including the excellent [`hass-foldingathomecontrol`](https://github.com/eifinger/hass-foldingathomecontrol) built for v7.

Rather than trying to retrofit the old logic, this project was written from scratch with v8's architecture in mind.

---

## 📦 Installation

1. Clone or download this repository into your Home Assistant configuration folder:

