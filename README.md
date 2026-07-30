# UEFN Virtual Pointer

UEFN Virtual Pointer (Experimental) — cross-platform pointer via Verse Enhanced Input: TouchMapping, PointerSelect, PointerZoom, swipes, pinch, screen-space deproject/trace. Bundles the virtualpointer skill.

Desktop plugin for [UEFN-Ducky](https://github.com/UEFN-Ducky/UEFN-Ducky) (`uefn-virtualpointer`).
Install or update from **Settings → Store** in the app — do not install from a zip by hand.

**Experimental:** you cannot publish an island that uses Virtual Pointer at this time. APIs may change.

## Build

```bash
py scripts/build_zip.py
```

Writes `deploy/uefn-virtualpointer-1.0.0.ducky-plugin.zip` (scripts/ and deploy/ are not packed).

## Publish (staff)

```bash
py scripts/release.py --publish --changelog "v1: Virtual Pointer Experimental skill pack"
```
