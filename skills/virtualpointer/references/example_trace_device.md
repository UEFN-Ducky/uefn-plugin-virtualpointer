# Example: screenspace_trace_device

Complete Verse device that turns on Virtual Pointer mode, subscribes to Pointer Select, and reports world objects that intersect the Virtual Pointer trace.

Place under `Verse/VirtualPointer/screenspace_trace_device.verse` (or similar system folder) — never at `Content/Verse/` root.

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Verse.org/Input }
using { /Verse.org/Input/UI }
using { /Verse.org/SpatialMath }

screenspace_trace_device := class(creative_device):

    var MaybeInputCancelableBegin : ?cancelable = false

    OnBegin<override>()<suspends>:void=
        # Subscribe per player on join / button / your game mode enter
        # e.g. GetPlayspace().PlayerAddedEvent().Subscribe(OnPlayerAdded)
        ()

    StartSubscription(Agent:agent):void=
        if:
            Player := player[Agent]
            PlayerInput := GetPlayerInput[Player]
        then:
            PlayerInput.AddInputMapping(TouchMapping)
            InputCancelableDetectBegin := PlayerInput.GetInputEvents(PointerSelect).BeginDetectEvent.Subscribe(PlayerClicked)
            set MaybeInputCancelableBegin = option{InputCancelableDetectBegin}

    PlayerClicked(Arg:tuple(player, vector3)):void=
        Player := Arg(0)
        ClickPos := Arg(1)

        Ray := TraceFromClick(Player, ClickPos.Left, ClickPos.Up)
        RayOrigin := Ray.Origin
        RayDir := Ray.Direction

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

    TraceFromClick(Player:player, ClickX:float, ClickY:float)<reads>:deproject_results=
        Player.DeprojectViewportToWorld(vector3{Left := ClickX, Up := ClickY, Forward := 0.0})
```

After writing: `workspace_list_verse_errors`, then place the device and wire player join → `StartSubscription`. Exit with `RemoveInputMapping(TouchMapping)` and cancel the subscription.
