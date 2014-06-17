# init.rpy
# Initialization code for the game, and for when a new game is started.

# Persistence initialization, if ran for the first time.
init python: 
    # Initialize persistent progress data if uninitialized.
    if persistent.demo_completed is None:
        persistent.demo_completed = False

    # Misc shit.
    renpy.music.register_channel('sound2', 'sfx', False, tight=True)
    renpy.music.register_channel('loopsfx', 'sfx', True, tight=True)
    renpy.music.register_channel('ambiance', 'ambiance', True, tight=True)

label splashscreen:
    scene black

    # Determine if we're running a software renderer.
    if renpy.get_renderer_info()['renderer'] == 'sw':
        scene misc heres a nickel kid get yourself a better computer
        $ renpy.transition(dissolve)
        $ renpy.pause()
        scene black with dissolve
        $ renpy.quit()

    # Force Ren'Py to pin vital menus.
    $ renpy.cache_pin(*renpy_listdir('ui/main', full_path=True, recursive=True))
    $ renpy.cache_pin(*renpy_listdir('ui/pause', full_path=True, recursive=True))
    $ renpy.cache_pin(*renpy_listdir('ui/side', full_path=True, recursive=True))

    # Show a nice intro video.
    $ renpy.movie_cutscene("vfx/intro.ogv")
    $ renpy.transition(dissolve)
    return
