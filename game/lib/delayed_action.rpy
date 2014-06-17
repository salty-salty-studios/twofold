init python:
    ## Delayed action.
    # Useful for scheduling an action for execution later in a screen.
    import threading

    class Delayed(Action):
        def __init__(self, delay, callback):
            self.delay = delay
            self.callback = callback
            self.timer = None

        def __call__(self):
            self.timer = threading.Timer(self.delay, self.do)
            self.timer.start()

        def do(self):
            try:
                for callback in self.callback:
                    try:
                        callback()
                    except TypeError:
                        raise
                    except:
                        pass
            except TypeError:
                try:
                    self.callback()
                except:
                    pass
