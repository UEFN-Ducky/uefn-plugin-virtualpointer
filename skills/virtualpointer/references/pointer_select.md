# PointerSelect — screen-space coordinates

`PointerSelect` is an experimental `input_action(vector3)` in `/Verse.org/Input/UI` (FN ≥ 4100). The `vector3` carries screen-space position (`Left` / `Up`).

## Subscribe after enabling TouchMapping

```verse
using { /Verse.org/Input }
using { /Verse.org/Input/UI }
using { /Verse.org/SpatialMath }

var MaybeInputCancelableBegin : ?cancelable = false

StartSubscription(Player:player):void=
    if:
        PlayerInput := GetPlayerInput[Player]
    then:
        PlayerInput.AddInputMapping(TouchMapping)
        InputCancelableDetectBegin := PlayerInput.GetInputEvents(PointerSelect).BeginDetectEvent.Subscribe(PlayerClicked)
        set MaybeInputCancelableBegin = option{InputCancelableDetectBegin}

PlayerClicked(Arg:tuple(player, vector3)):void=
    Player := Arg(0)
    ClickPos := Arg(1)
    # ClickPos.Left / ClickPos.Up are screen-space coords
```

## Event surface

Use `PlayerInput.GetInputEvents(PointerSelect)` and subscribe as needed:

- `BeginDetectEvent`
- `DetectionOngoingEvent`
- `TriggerActivationEvent`
- `EndDetectEvent`

Keep cancelables and call `.Cancel()` when leaving the mode (in addition to `RemoveInputMapping(TouchMapping)` if you exit VP).

## Next steps

- World hit-test: see `screenspace_trace.md` (`DeprojectViewportToWorld` + sweep).
- Pinch: see `pinch_zoom.md` (`PointerZoom`).
