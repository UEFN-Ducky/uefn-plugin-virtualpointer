---
name: virtualpointer
description: "UEFN Virtual Pointer (Experimental) — cross-platform pointer input via Verse Enhanced Input: TouchMapping, PointerSelect, PointerZoom, swipes, pinch zoom/scale, screen-space deproject and world traces. Use when the user mentions virtual pointer, touch mapping, PointerSelect, PointerZoom, pinch, swipe, or cross-platform on-screen pointer."
license: MIT
metadata:
  label: UEFN Virtual Pointer
  version: 1
  author: UEFN-Ducky
  copyright: Copyright 2026 Mindful Path Company, LLC
  allow_redistribute: true
  managed_by: uefn-ducky
---

# UEFN Virtual Pointer (Experimental)

Add cross-platform pointer input to your UEFN island using Verse Enhanced Input, with custom input mappings, actions, and gestures.

**Experimental.** You can try it out and provide feedback. **You cannot publish a project that uses Virtual Pointer at this time.** Backward compatibility is not guaranteed; APIs may change or the feature may be removed.

## What it is

The Virtual Pointer lets players interact with on-screen elements on all supported input devices:

| Device | Pointer |
|--------|---------|
| Touch | Finger contact |
| Mouse + keyboard | Existing mouse pointer |
| Controller | Virtual on-screen pointer driven by the **left stick** |

UEFN reads the Virtual Pointer as a normal pointer. Gesture-driven input (select, swipe, pinch) stays consistent across platforms. Supports interacting with world objects via screen-space deprojection.

**Does not work** when Fortnite game menus are open.

**Players are immobilized** while in Virtual Pointer mode.

## Digest facts (verify before inventing names)

| Symbol | Module | Notes |
|--------|--------|-------|
| `TouchMapping` | `/Verse.org/Input/UI` | `input_mapping`, `@experimental`, FN ≥ 4100 |
| `PointerSelect` | `/Verse.org/Input/UI` | `input_action(vector3)`, FN ≥ 4100 |
| `PointerZoom` | `/Verse.org/Input/UI` | `input_action(vector3)`, FN ≥ 4120 |
| `GetPlayerInput` | `/Verse.org/Input` | `player` → `player_input` |
| `AddInputMapping` / `RemoveInputMapping` | on `player_input` | Enable / exit VP mode |
| `GetInputEvents` | on `player_input` | Begin / Ongoing / Trigger / End detect events |
| `DeprojectViewportToWorld` | on `player` | Screen → world ray (`deproject_results`) |

Never invent action names. Confirm with `search_verse_digest` / `get_verse_api`.

## Golden path

```
1. Warn: Experimental — island cannot be published while using Virtual Pointer
2. On player join / mode enter: GetPlayerInput[Player] → AddInputMapping(TouchMapping)
3. Subscribe PointerSelect (and/or PointerZoom) via GetInputEvents
4. On select: read screen vector3 (Left/Up) → DeprojectViewportToWorld → FindSweepHits
5. On exit: RemoveInputMapping(TouchMapping); cancel subscriptions
```

## Enable Virtual Pointer

For Virtual Pointer to be enabled in-game, enable touch mapping with `AddInputMapping`. Custom input maps must be added to players for custom input to apply.

```verse
using { /Verse.org/Input }
using { /Verse.org/Input/UI }

AddTouchMapping(Player:player):void=
    if:
        PlayerInput := GetPlayerInput[Player]
    then:
        PlayerInput.AddInputMapping(TouchMapping)
```

Gamepad players see the virtual pointer after `TouchMapping` is added. Players are immobilized in this mode.

## Disable

Unsubscribing from `PointerSelect` stops screen-space coordinate delivery. Removing `TouchMapping` exits Virtual Pointer mode. You do **not** have to unsubscribe from Pointer Select before removing `TouchMapping`.

```verse
RemoveTouchInput(Player:player):void=
    if:
        PlayerInput := GetPlayerInput[Player]
    then:
        PlayerInput.RemoveInputMapping(TouchMapping)
```

## Reference files

- `references/enable_disable.md` — Enter/exit VP mode, immobilization, menu caveat
  Load when: Turning Virtual Pointer on/off for a player
- `references/pointer_select.md` — PointerSelect subscribe + screen coords
  Load when: Click / tap / select with the virtual pointer
- `references/screenspace_trace.md` — Deproject + FindSweepHits world pick
  Load when: Hitting world objects / Scene Graph entities from the pointer
- `references/pinch_zoom.md` — PointerZoom pinch / scroll / right-stick zoom & scale
  Load when: Zoom camera or resize props/entities with pinch
- `references/swipe.md` — Swipe direction classification across devices
  Load when: Detecting swipe / flick gestures
- `references/example_trace_device.md` — Full `screenspace_trace_device` sample
  Load when: Scaffolding a complete creative_device for VP picking
