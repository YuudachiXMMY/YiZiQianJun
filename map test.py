# Pinky!今天14:42
# No, for is still part of screen language, but you can use it to look at python things.


    grid 12 2:
        transpose True
        for stuff in ship_cargo:
            if stuff != Null:
                for number in range(stuff.quantity):
                    $ current_cargonum +=1
                    fixed:
                        xysize (78, 168)
                        add "gui/cargobay/[stuff.type_basic].png"
                        button:
                            xysize (78, 168)
                            if stuff == cargo_selected:
                                hovered NullAction()
                                unhovered NullAction()
                            else:
                                hovered SetVariable("cargo_selected", stuff)
                                unhovered SetVariable("cargo_selected", Cargo())
                            action NullAction()
                            hover_background "gui/cargobay/cargo_hovered.png"
                            selected_background "gui/cargobay/cargo_hovered.png"
                            selected cargo_selected == stuff
# This is more elaborate that what you probably need, but this is part of a grid/for loop thing I am using
# ship_cargo is a list I use, that gets filled with Cargo objects, which are custom class objects that have things like quantity that the loop can look at.

# But for your map, your objects could have an action property for example, so action stuff.action would be possible.