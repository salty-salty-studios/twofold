# 00_config.rpy
# Basic Ren'Py game options.

python early:
    config.save_directory = "WorkInProgress-Demo"
    config.testing = False

init -1 python hide:
    # Basic settings.
    config.name = "Work in Progress Demo"
    config.version = "1.0.0"
    config.developer = True

    # Window.
    config.screen_width = 1280
    config.screen_height = 720
    config.window_title = u"Work in Progress Demo"
    config.window_icon = "ui/icon.png"
    config.windows_icon = "ui/icon-win.png"
    config.skip_indicator = "ui/hud/skip.png"
    config.default_fullscreen = False
    config.framerate = 60

    # Capabilities.
    config.gl_resize = True
    config.has_sound = True
    config.has_music = True
    config.has_voice = False
    config.main_menu_music = None
    config.has_autosave = False
    config.has_quicksave = False

    # Misc.
    config.default_text_cps = 25
    config.thumbnail_width = 193
    config.thumbnail_height = 108

    # Theme.
    theme.marker(
        widget = "#003c78",
        widget_hover = "#0050a0",
        widget_text = "#c8ffff",
        widget_selected = "#ffffc8",
        disabled = "#404040",
        disabled_text = "#c8c8c8",
        label = "#ffffff",
        frame = "#6496c8",
        mm_root = "#000000",
        gm_root = "#dcebff",
        rounded_window = False
    )
    style.default.font = "ui/SetFireToTheRain.ttf"

    # Keymap.
    config.keymap['choose_renderer'] = []

    # Default transitions.
    config.enter_transition = None
    config.exit_transition = dissolve
    config.intra_transition = None
    config.main_game_transition = dissolve
    config.game_main_transition = dissolve
    config.end_splash_transition = None
    config.end_game_transition = dissolve
    config.after_load_transition = dissolve
    config.window_show_transition = None
    config.window_hide_transition = None
    
    # Customizations/hacks.
    config.image_cache_size = 16
    store._game_menu_screen = "pause_menu"
    config.quit_action = Quit()

    # Distributions.
    build.directory_name = "WorkInProgress-Demo"
    build.executable_name = "Work in Progress Demo"
    build.include_update = False

    # What not to pack.
    build.classify('errors.txt', None)
    build.classify('log.txt', None)
    build.classify('traceback.txt', None)
    build.classify('**-e', None)
    build.classify('**.rpy', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/.DS_Store', None)
    build.classify('game/saves/**', None)
    build.classify('patches/**', None)
    build.classify('installer/**', None)

    # Need this outside the archives.
    build.classify('game/ui/icon*', 'all')

    # What to pack as data.
    build.archive('resources', 'all')
    build.classify('game/bgs/**', 'resources')
    build.classify('game/cgs/**', 'resources')
    build.classify('game/music/**', 'resources')
    build.classify('game/sfx/**', 'resources')
    build.classify('game/sprites/**', 'resources')
    build.classify('game/ui/**', 'resources')
    build.classify('game/vfx/**', 'resources')

    # What to pack as code.
    build.archive('code', 'all')
    build.classify('game/id.txt', 'code')
    build.classify('game/*.rpyb', 'code')
    build.classify('game/*.rpyc', 'code')
    build.classify('game/lib/**', 'code')

    # What to pack as the story.
    build.archive('story', 'all')
    build.classify('game/scripts/**', 'story')
