# PointerZoom — pinch, scroll, right-stick zoom / scale

`PointerZoom` is an experimental `input_action(vector3)` in `/Verse.org/Input/UI` (FN ≥ 4120).

Pinch actions are continuous input for camera zoom and object scaling. Behavior by device:

| Device | Control | Value | Center |
|--------|---------|-------|--------|
| Touch | Two fingers pinch in/out | Speed of pinch; `0` = no change | Midpoint between fingers |
| Mouse + keyboard | Scroll wheel | `-1` to `1` by direction; freewheel feels closer to stick | Current pointer position |
| Controller | Right stick Up = zoom in, Down = zoom out | Stick deflection `-1`…`1` | Virtual Pointer position |

## Subscribe (zoom logging example)

```verse
using { /Verse.org/Input }
using { /Verse.org/Input/UI }

EnableCursorZoom(Player:player):void=
    if:
        PlayerInput := GetPlayerInput[Player]
    then:
        PlayerInput.AddInputMapping(TouchMapping)
        BeginSub := PlayerInput.GetInputEvents(PointerZoom).BeginDetectEvent.Subscribe(OnPinchBegin)
        OngoingSub := PlayerInput.GetInputEvents(PointerZoom).DetectionOngoingEvent.Subscribe(OnPinchOngoing)
        TriggerSub := PlayerInput.GetInputEvents(PointerZoom).TriggerActivationEvent.Subscribe(OnPinchTrigger)
        EndSub := PlayerInput.GetInputEvents(PointerZoom).EndDetectEvent.Subscribe(OnPinchEnd)
```

Implement `OnPinchBegin` / `OnPinchOngoing` / `OnPinchTrigger` / `OnPinchEnd` to apply camera FOV or entity scale. Keep cancelables and cancel on exit.

## Resizing a Scene Graph entity

1. Place Actors → Entities → `entity`.
2. Add `mesh_component` (e.g. Cube).
3. Wire a Verse device `@editable` entity ref (`PropToScale`) to that entity.
4. On `PointerZoom` ongoing/trigger, multiply entity transform scale by pinch delta (confirm Scene Graph transform APIs via `search_verse_digest` — never invent).

Epic’s tutorial device is often named `pinch_scale_device` — adapt into `Verse/<System>/` (never dump at Verse root). Set `PropToScale` to the scalable mesh entity in Details.
