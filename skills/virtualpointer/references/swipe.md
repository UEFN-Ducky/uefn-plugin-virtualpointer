# Swipe detection with Virtual Pointer

You can detect when the player swipes their finger in a certain direction on the screen, or takes the equivalent action via gamepad or mouse, while Virtual Pointer mode is active (`TouchMapping` added).

## Approach

1. `AddInputMapping(TouchMapping)`.
2. Subscribe to `PointerSelect` begin → end (or ongoing), or any dedicated swipe action your FN digest exposes.
3. Record start screen position (`Left` / `Up`) on begin.
4. On end (or when displacement exceeds a threshold), classify direction from delta.

## Direction classification (pattern)

```verse
using { /Verse.org/SpatialMath }

SwipeMinDistance : float = 40.0

swipe_dir := enum{None, Left, Right, Up, Down}

ClassifySwipe(Start:vector3, End:vector3):swipe_dir=
    Dx := End.Left - Start.Left
    Dy := End.Up - Start.Up
    AbsDx := if (Dx < 0.0) then -Dx else Dx
    AbsDy := if (Dy < 0.0) then -Dy else Dy
    if (AbsDx < SwipeMinDistance and AbsDy < SwipeMinDistance):
        swipe_dir.None
    else if (AbsDx >= AbsDy):
        if (Dx >= 0.0) then swipe_dir.Right else swipe_dir.Left
    else:
        if (Dy >= 0.0) then swipe_dir.Up else swipe_dir.Down
```

Tune thresholds and axis conventions against Epic samples for your build (UI Up may differ from world). Prefer digest-confirmed event payloads over guessed types.

## Notes

- Same gesture path should work for touch swipe, mouse drag, and gamepad pointer drag.
- Does not fire while Fortnite menus are open.
- Confirm whether your FN digest exposes a dedicated swipe `input_action`; if not, derive from `PointerSelect` begin/end positions as above.
