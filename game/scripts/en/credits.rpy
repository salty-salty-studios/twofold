label scene_credits_en:
##############################
    # Credits.
    # Congratulations!
    $ persistent.demo_completed = True
    stop ambiance fadeout 2.5
    stop music fadeout 2.5
    play music "music/credits.ogg" fadein 1.5

    window hide dissolve
    scene creme with longDissolve

    scene misc credits blank with longDissolve
    scene misc credits sfx with longDissolve
    $ renpy.pause(10.0)
    scene misc credits blank with longDissolve
    scene misc credits staff with longDissolve
    $ renpy.pause(15.0)
    scene misc credits blank with longDissolve
    scene misc credits unlocked with longDissolve
    if not renpy.pause(10.0):
        scene misc credits unlocked click with dissolve
        $ renpy.pause()

    stop music fadeout 2.0
    scene black with longDissolve
    return
