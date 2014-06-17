init -500 python:
    ## Resettable animation displayables.

    # Thanks to Asceai on Freenode.
    class ResettableDisplayable(renpy.Displayable):
        def __init__(self, child, **kwargs):
            super(ResettableDisplayable, self).__init__(**kwargs)
            self.base = child
            self.child = renpy.displayable(self.base())
            self.st_reset = 0.0
            self.at_reset = 0.0
            self.reset = False

        def render(self, width, height, st, at):
            if self.reset:
                self.child = renpy.displayable(self.base())
                self.st_reset = st
                self.at_reset = at
                self.reset = False

            return renpy.render(self.child, width, height, st - self.st_reset, at - self.at_reset)

        def Reset(self):
            return SetField(self, "reset", True)

        def visit(self):
            return [ self.child ]

    def ResetDisplayable(disp):
        targetref = renpy.displayable(disp)
        targetref.find_target()
        return targetref.target.Reset()
