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

## Next release: ship compiled

This plugin still ships its Python source on the Store. Its next release has to ship compiled and signed, the way Ducky Account and Roguelike do:

1. Give `scripts/release.py` and `scripts/build_zip.py` the compiled build from `uefn-plugin-account` (`build_compiled_zip`, upload by ticket, `--plain` only as an escape hatch).
2. Bump `version` and set `min_app_version` to `1.2.357` or newer (the Store keeps older apps from seeing it).
3. Publish, then check the download with the start-up license check (signature, id and version, compiled, team access), not only the signature.
4. A compiled build can't `importlib.reload` its own modules (Python raises SystemError), so reload only when running from source. Before publishing, install the source and compiled zips into a throwaway Ducky and check they register the same panel calls, tools and workflow nodes, and that those calls still work after the plugin reloads.

Remove this section once a compiled version is live.

## License

MIT. Copyright (c) 2026 Mindful Path Company, LLC. See [LICENSE](LICENSE).
