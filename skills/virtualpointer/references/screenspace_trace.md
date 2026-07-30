# Screen-space deproject + world sweep

World objects that intersect with the Virtual Pointer trace can be detected with Verse after a `PointerSelect` click.

## Deproject

```verse
TraceFromClick(Player:player, ClickX:float, ClickY:float)<reads>:deproject_results=
    Player.DeprojectViewportToWorld(vector3{Left := ClickX, Up := ClickY, Forward := 0.0})
```

`DeprojectViewportToWorld` lives on `player` in `/Verse.org/Input` and returns `deproject_results` (Origin / Direction).

## Sweep from click

```verse
PlayerClicked(Arg:tuple(player, vector3)):void=
    Player := Arg(0)
    ClickPos := Arg(1)

    Ray := TraceFromClick(Player, ClickPos.Left, ClickPos.Up)
    RayOrigin := Ray.Origin
    RayDir := Ray.Direction

    # Sweep: ray direction * max distance
    Displacement := RayDir * 50000.0

    StartTransform := transform{Translation := RayOrigin}
    CollisionShape := collision_point{}

    Hits := for:
        Hit : GetSimulationEntity[].FindSweepHits(Displacement, StartTransform, CollisionShape)
    do:
        Hit

    if (FirstHit := Hits[0]):
        Print("HIT something at {FirstHit.ContactPosition}!")
    else:
        Print("MISS")
```

## Notes

- Prefer Scene Graph / simulation entity APIs from digests — confirm `FindSweepHits`, `collision_point`, `GetSimulationEntity` before shipping.
- Tune max distance (`50000.0` in Epic’s sample) for your island scale.
- Full device sample: `example_trace_device.md`.
