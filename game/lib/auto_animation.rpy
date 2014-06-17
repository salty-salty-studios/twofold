init python:
    ## Helper function to define an animation from a set of files in a folder.
    # This function assumes a workflow of having X intro frames and Y <= X loop frames (default Y = 3).
    import itertools

    call_function = lambda x: x()

    def animation_from_folder(name, folder, fps=12, loop_frames=3, wrapper=call_function, **kwargs):
        frame_duration = 1.0 / fps
        if kwargs:
            frames = [ (Transform(filename, **kwargs), frame_duration) for filename in sorted(renpy_listdir(folder, full_path=True)) ]
        else:
            frames = [ (filename, frame_duration) for filename in sorted(renpy_listdir(folder, full_path=True)) ]

        anim = Animation(*itertools.chain(*frames))
        renpy.image(name + '_main', anim)
        renpy.image(name + '_init', frames[0][0])

        if loop_frames:
            loop_anim = Animation(*itertools.chain(*frames[-loop_frames:]))
            renpy.image(name + '_loop', loop_anim)
            renpy.image(name, wrapper(lambda: showrepeat(name + '_main', len(frames) * frame_duration, name + '_loop', loop_frames * frame_duration)))
        else:
            renpy.image(name, wrapper(lambda: name + '_main'))
