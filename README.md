# UEFN Virtual Pointer

Cross-platform pointer input for UEFN via Verse Enhanced Input: `TouchMapping`, `PointerSelect`, `PointerZoom`, swipes, taps, pinch, screen-space deproject and world traces. Bundles the `virtualpointer` skill and three New-file Verse templates.

Desktop plugin for [UEFN-Ducky](https://github.com/UEFN-Ducky/UEFN-Ducky) (`uefn-virtualpointer`).
Install or update from **Settings → Store** in the app — do not install from a zip by hand.

## Publish status

- `TouchMapping` + `PointerSelect` (select, swipe, tap, screen-space trace): **publishable**.
- `PointerZoom` (pinch / scroll / right-stick zoom): **Experimental** — islands using it cannot be published yet; the API may change.

## Verse templates (New file → Verse)

| id | File | Notes |
|----|------|-------|
| `vp_screenspace_trace` | `screenspace_trace_device.verse` | Tap → deproject → sweep hit |
| `vp_swipe_detector` | `swipe_detector_device.verse` | Per-player swipe / tap classifier |
| `vp_pinch_scale` | `pinch_scale_device.verse` | Pinch to scale a Scene Graph entity (Experimental) |
| `virtualpointer` | all three → `Verse/VirtualPointer/` | Whole pack |

## Build

```bash
py scripts/build_zip.py
```

Writes `deploy/uefn-virtualpointer-<version>.ducky-plugin.zip` (scripts/ and deploy/ are not packed).

## Publish (staff)

```bash
py scripts/release.py --publish --changelog "v1.0.4: publish-status fix, event payloads, stasis release, 3 Verse templates"
```

## License

MIT. Copyright (c) 2026 Mindful Path Company, LLC. See [LICENSE](LICENSE).
