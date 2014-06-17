# script.rpy
# Contains the script flow.

# A new game has been started, pass control to script performer.
label script_start:
    $ import random

    # Common route.
    perform "1S1"
    perform "1S2"
    perform "1S3"
    perform "1S4"
    perform "1S5"
    perform "1S6"
    perform "1S7"
    perform "1S8"
    perform "1S9"
    perform "1S10"
    perform "1S11"
    perform "1S12"
    perform "1S13"
    perform "1S14"
    perform "1S15"
    perform "1S16"
    perform "1S17"
    perform "1S18"
    perform "1S19"
    perform "1S20" independent

    perform "credits"
    return

label scene_1S20:
    perform "1S20_intro"
    $ who_explains_first = renpy.random.randint(1, 2)
    if who_explains_first == 1:
        perform "1S20_caprice_summary"
        perform "1S20_mekki_summary"
    else:
        perform "1S20_mekki_summary"
        perform "1S20_caprice_summary"
    perform "1S20_club_choice"
    choose "1S20_club_choice"
    return
