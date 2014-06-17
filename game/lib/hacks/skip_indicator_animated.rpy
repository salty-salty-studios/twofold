init python:
    ## Animated skip indicator.
    # Allows you to use some sort of animation in showing/hiding the skip indicator.
    import time
    config.overlay_functions.remove(skip_indicator)
    SKIP_INDICATOR_IMAGE = 'skipind2'

    renpy.image(SKIP_INDICATOR_IMAGE, config.skip_indicator)

    # Override skip indicator.
    def skip_indicator():
        if config.skipping:
            # Is the indicator not showing or in the process of being hidden?
            if not renpy.showing(SKIP_INDICATOR_IMAGE) or skip_indicator.skip_hide_time:
                # We had a scene change that caused the indicator to be hidden; show it again.
                if skip_indicator.skipping:
                    renpy.show(SKIP_INDICATOR_IMAGE, at_list=[lefttop])
                # The user started skipping; add the image with a nice animation.
                else:
                    renpy.show(SKIP_INDICATOR_IMAGE, at_list=[tmoveinlefttop])
                # Cancel hiding.
                skip_indicator.skip_hide_time = None
        else:
            if renpy.showing(SKIP_INDICATOR_IMAGE):
                # Are we in the process of hiding the indicator?
                if skip_indicator.skip_hide_time:
                    # Has it been completely hidden? Remove it from the screen.
                    if time.time() - skip_indicator.skip_hide_time >= 1.0:
                        renpy.hide(SKIP_INDICATOR_IMAGE)
                        skip_indicator.skip_hide_time = None
                else:
                    # Start hiding the indicator with an animation that lasts 1 second.
                    # Has to be done because 'hide ... at' is not understood by Ren'Py.
                    renpy.show(SKIP_INDICATOR_IMAGE, at_list=[tmoveoutlefttop])
                    skip_indicator.skip_hide_time = time.time()

        # Update our own skipping status.
        skip_indicator.skipping = config.skipping

    skip_indicator.skipping = False
    skip_indicator.skip_hide_time = None
    config.overlay_functions.append(skip_indicator)
