init python:
    ## Show image action.
    class ShowImage(Action):
        def __init__(self, image, *args, **kwargs):
            self.image = image
            self.args = args
            self.kwargs = kwargs

        def __call__(self):
            renpy.show(self.image, *self.args, **self.kwargs)
            renpy.restart_interaction()
