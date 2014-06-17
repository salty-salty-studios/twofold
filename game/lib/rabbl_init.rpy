## RABBL support code.

# Start of a new game.
label start:
    $ renpy.block_rollback()

    perform "start" independent
    perform "start"

    # Scene replay.
    if persistent._rabbl_scene:
        scene black
        with dissolve

        python:
            _current_scene = persistent._rabbl_scene
            persistent._rabbl_scene = None
            store.rabbl_playthrough.oneshot = True
    
        perform _current_scene
    else:
        jump script_start

    perform "end" independent
    perform "end"
    $ pass

label script_init:
    # Initialize the script.
    perform "init" independent
    perform "init"
    return

label rabbl_choice_trampoline (name, label):
    call expression label
    $ rabbl.after_choose(name)
    return
