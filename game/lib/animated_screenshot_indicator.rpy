init -5 python:
    import time
    import threading
    SCREENSHOT_INDICATOR_IMAGE = 'screenshotind'

    store._screenshot_taken = 0
    store._screenshot_notification_show_time = 0
    renpy.image(SCREENSHOT_INDICATOR_IMAGE, 'ui/hud/screenshot.png')

    def screenshot_callback(filename):
        store._screenshot_taken = time.time()
        renpy.restart_interaction()

    def screenshot_overlay():
        if time.time() - store._screenshot_taken < 2.0:
            renpy.show(SCREENSHOT_INDICATOR_IMAGE, at_list=[screenshotindicator])
            store._screenshot_notification_show_time = time.time()
        elif renpy.showing(SCREENSHOT_INDICATOR_IMAGE) and time.time() - store._screenshot_notification_show_time > 4.0:
            renpy.hide(SCREENSHOT_INDICATOR_IMAGE)

    config.screenshot_callback = screenshot_callback
    config.overlay_functions.append(screenshot_overlay)
