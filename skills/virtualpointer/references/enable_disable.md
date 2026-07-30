# Enable / disable Virtual Pointer

## Enable

For Virtual Pointer to be enabled for use in-game, you must first enable touch mapping with `AddInputMapping`.

You must add your custom input maps to players for any custom input to apply in game.

```verse
using { /Verse.org/Input }
using { /Verse.org/Input/UI }

AddTouchMapping(Player:player):void=
    if:
        PlayerInput := GetPlayerInput[Player]
    then:
        PlayerInput.AddInputMapping(TouchMapping)
```

This adds the `TouchMapping` input mapping to the player, causing the player to enter virtual pointer mode. At that point, players using a gamepad will see the virtual pointer.

**Players are immobilized when in Virtual Pointer mode.**

## Device mapping (how the pointer is defined)

| Platform | Pointer source |
|----------|----------------|
| Touch | Finger contact |
| Mouse and keyboard | Existing mouse pointer |
| Controller | Virtual on-screen pointer driven by the **left stick** |

## Caveats

- Virtual Pointer does **not** work when the Fortnite game menus are open.
- Feature is **Experimental** — cannot publish islands that use it; APIs may change.
- Digest: `TouchMapping` is `@experimental` under `/Verse.org/Input/UI` (FN ≥ 4100).

## Disable

Unsubscribing from the `PointerSelect` input action will stop the system from getting screen-space coordinates. Additionally, removing the `TouchMapping` mapping will exit Virtual Pointer mode.

You do **not** have to unsubscribe from Pointer Select in order to remove `TouchMapping`.

```verse
RemoveTouchInput(Player:player):void=
    if:
        PlayerInput := GetPlayerInput[Player]
    then:
        PlayerInput.RemoveInputMapping(TouchMapping)
```

## Custom mappings

For more details about how to add and customize player input, see Epic’s “How to Add Player Input” and confirm custom `input_mapping` / `input_action` assets via digests / Content Browser — never invent names.
