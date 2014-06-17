init -9 python hide:
    ## Allow copying current line to clipboard. Requires clip.py.

    def init():
        store._last_line = None

    def overlay():
        def record():
            import lib.clip
            if store._last_line:
                lib.clip.set(store._last_line)
        ui.keymap(meta_c=record)

    config.start_callbacks.append(init)
    config.overlay_functions.append(overlay)
