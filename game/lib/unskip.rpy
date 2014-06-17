init python:
    ## Action to skop skipping.

    class Unskip(Action):
        def __call__(self):
            if not self.get_sensitive():
                return

            if config.skipping:
                config.skipping = None
                renpy.restart_interaction()  
