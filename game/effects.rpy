# effects.rpy
# All effect (transformation/transition) definitions are stored here.

# Transistion definitions
define smoothDissolve = Dissolve(0.5, old_widget=None, new_widget=None, alpha=True)
define fastDissolve = Dissolve(0.5, old_widet=None, new_widget=None, alpha=True)
define midDissolve = Dissolve(1.5, old_widget=None, new_widget=None, alpha=True)
define midlongDissolve = Dissolve(2.0, old_widget=None, new_widget=None, alpha=True)
define longDissolve = Dissolve(3.0, old_widget=None, new_widget=None, alpha=True)
define fadeInOut = Fade(1.0, 0, 1.0)
define eyes = ImageDissolve('vfx/eyes.jpg', 2.0, ramplen=256, alpha=True, reverse=True)
define eyesr = ImageDissolve('vfx/eyes.jpg', 2.0, ramplen=256, alpha=True)

label switch_scene(old, new):
    call switch_scene_sx(old, new, True, {})
    return

label switch_scene_x(old, new, trans):
    call switch_scene_sx(old, new, True, trans)
    return

label switch_scene_s(old, new):
    call switch_scene_sx(old, new, False, {})
    return

label switch_scene_sx(old, new, long, trans):
    window hide fastDissolve
    $ renpy.scene()

    if not store.rabbl_playthrough.oneshot:
        $ renpy.show(old + ' desaturated')
        with dissolve

        if long:
            show misc clock center as clockcenter:
                xalign 0.5
                yalign 0.5
            show misc clock littlehand as clocklittlehand:
                xalign 0.5
                yanchor 1.0
                ypos 0.5
            show misc clock bighand as clockbighand:
                yanchor 1.0
                ypos 0.5
                xalign 0.5
                subpixel True
                transform_anchor True

                ease 1.0 rotate 30
                ease 1.0 rotate 60
                ease 1.0 rotate 90
                ease 1.0 rotate 120
                ease 1.0 rotate 150
            with None
            $ renpy.pause(2.0)
        else:
            $ renpy.pause(1.0)

    if trans:
        $ renpy.show(new.split()[0], what=Transform(new + ' desaturated', **trans))
    else:
        $ renpy.show(new + ' desaturated')
    $ renpy.transition(dissolve, layer='master')

    $ renpy.pause(2.0)
    if long and not store.rabbl_playthrough.oneshot:
        hide clockcenter
        hide clocklittlehand
        hide clockbighand
        with dissolve

    $ renpy.scene()
    if trans:
        $ renpy.show(new.split()[0], what=Transform(new, **trans))
    else:
        $ renpy.show(new)
    with dissolve
    window show fastDissolve
    return

transform null:
    pass

transform delayed(delay):
    alpha 0
    time delay
    alpha 1

transform showrepeat(first, firstdur, then, thendur):
    first
    time firstdur
    block:
        then
        time thendur
        repeat

transform moveto(t, x):
    subpixel True
    ease t xalign x

transform movetop(t, x):
    subpixel True
    ease t xpos x

transform trotate(alpha):
    subpixel True
    rotate alpha

transform screenshotindicator:
    yanchor 1.0
    ypos 0
    xpos 120
    ease 1.0 yanchor 0.0 ypos 0
    time 3.0
    ease 1.0 yanchor 1.0 ypos 0

transform transparent(a):
    alpha a

transform tdissolve(length):
    alpha 0.0
    linear length alpha 1.0

transform tddissolve(length, delay):
    alpha 0.0
    pause delay
    linear length alpha 1.0a

transform fadein(speed):
    alpha 0.0
    linear speed alpha 1.0

transform mirror:
    xzoom -1.0

transform flip(new):
    xzoom 1.0
    ease .4 xzoom 0.0
    new
    ease .4 xzoom -1.0

transform nflip(new):
    xzoom -1.0
    ease .4 xzoom 0.0
    new
    ease .4 xzoom 1.0

transform pflip(new):
    xzoom 1.0
    ease .4 xzoom 0.0
    new
    ease .4 xzoom 1.0

transform pnflip(new):
    xzoom -1.0
    ease .4 xzoom 0.0
    new
    ease .4 xzoom -1.0

transform lefttop:
    xanchor 0.0
    yanchor 0.0
    xpos 0
    ypos 0

transform tmoveinlefttop:
    xanchor 0.0
    yanchor 1.0
    xpos 0
    ypos 0
    ease 1.0 yanchor 0.0

transform tmoveoutlefttop:
    xanchor 0.0
    yanchor 0.0
    xpos 0
    ypos 0
    ease 1.0 yanchor 1.0
