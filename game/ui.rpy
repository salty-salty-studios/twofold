# ui.rpy
# Contains the basic user interface screens and elements.

###
#
# Animation definitions.
#
###

init python:
    animation_from_folder('menu_newgame', 'ui/side/newgame', wrapper=ResettableDisplayable)
    animation_from_folder('menu_loadgame', 'ui/side/loadgame', wrapper=ResettableDisplayable)
    animation_from_folder('menu_loadgame_back', 'ui/side/loadgame_back', wrapper=ResettableDisplayable)
    animation_from_folder('menu_savegame', 'ui/side/savegame', wrapper=ResettableDisplayable)
    animation_from_folder('menu_savegame_back', 'ui/side/savegame_back', wrapper=ResettableDisplayable)
    animation_from_folder('menu_options', 'ui/side/options', wrapper=ResettableDisplayable)
    animation_from_folder('menu_options_back', 'ui/side/options_back', wrapper=ResettableDisplayable)
    animation_from_folder('menu_extras', 'ui/side/extras', wrapper=ResettableDisplayable)
    animation_from_folder('menu_extras_back', 'ui/side/extras_back', wrapper=ResettableDisplayable)
    animation_from_folder('menu_mainmenu', 'ui/side/mainmenu', wrapper=ResettableDisplayable)



###
#
# Screens.
#
###


########################################################################################
# Main screens.
########################################################################################

# Our main menu screen.
screen main_menu:
    tag menu

    if renpy.showing('main_menu', layer='screens') and not renpy.music.get_playing('music') and not renpy.music.get_playing('jukebox'):
        $ renpy.music.play('music/wellworkonit.ogg', fadein=1.0)
        
    window:
        style "mm_root"
        background "#000000"
        add "ui/main/bg.png" at tdissolve(1.25)
        add "ui/main/logo.png" at tdissolve(1.50):
            xoffset 50
            yoffset -68

        if renpy.get_screen('load') or renpy.get_screen('preferences') or renpy.get_screen('extras'):
            add "ui/pause/overlay.png" at tdissolve(1.5)

    frame:
        background Null()
        use side_menu

# The pause menu screen.
screen pause_menu:
    tag menu

    python:
        # Fetch current song.
        trackfile = renpy.music.get_playing('music')
        if trackfile in store.tracks:
            track = store.tracks[trackfile]['title']
        else:
            track = None
        
        # Fetch current scene.
        if store.rabbl_playthrough.current_scene in store.scenes:
            title = store.scenes[store.rabbl_playthrough.current_scene]['title']
        else:
            title = None

        if store.rabbl_playthrough.oneshot:
            title = '{color=#faf6e780}Replay:{/color} ' + title
   
        # Fetch current running time.
        runtime = renpy.get_game_runtime()
        time = "%d:%02d" % (int(runtime / 3600), int(runtime / 60) % 60)

    frame:
        background "ui/pause/overlay.png" at tdissolve(0.5)
        use side_menu

        # Our song, scene and playtime.
        add "ui/pause/scene.png":
            xpos 775
            ypos 15

        if title:
            text title id "title":
                xpos 763
                ypos 23
                text_align 1.0
                xalign 1.0
                color "#faf6e7"
        else:
            text __("Unknown scene") id "title":
                    xpos 763
                    ypos 23
                    text_align 1.0
                    xalign 1.0
                    color "#faf6e780"

        add "ui/pause/song.png":
            xpos 772
            ypos 54

        if track:
            text track id "track":
                xpos 760
                ypos 60
                text_align 1.0
                xalign 1.0
                color "#faf6e7"
        else:
            text __("Nothing playing" )id "track":
                xpos 760
                ypos 60
                text_align 1.0
                xalign 1.0
                color "#faf6e780"

        if not store.rabbl_playthrough.oneshot:
            add "ui/pause/time.png":
                xpos 767
                ypos 92

            text time id "time":
                xpos 757
                ypos 96
                text_align 1.0
                xalign 1.0
                color "#faf6e7"

screen side_menu:
    tag side_menu

    add "ui/side/menu.png":
        xanchor 1.0
        xpos 1280
        yalign 0.5

    if not store.rabbl.in_playthrough():
        imagebutton:
            idle "menu_newgame_init"
            hover "menu_newgame"
            hovered ResetDisplayable('menu_newgame')
            focus_mask "ui/side/mask1.png"
            xpos 850
            ypos 37
            action [ Stop('jukebox'), Start() ]
    elif store.rabbl_playthrough.oneshot:
        add Transform("menu_savegame_init", alpha=0.5):
            xpos 841
            ypos 28
        
        add "ui/side/lock.png":
            xpos 933
            ypos 110
    elif not renpy.get_screen('save'):
        imagebutton:
            idle "menu_savegame_init"
            hover "menu_savegame"
            hovered ResetDisplayable('menu_savegame')
            focus_mask "ui/side/mask1.png"
            xpos 841
            ypos 28
            action Show('save', fastDissolve)
    else:
        imagebutton:
            idle "menu_savegame_back_init"
            hover "menu_savegame_back"
            hovered ResetDisplayable('menu_savegame_back')
            focus_mask "ui/side/mask1.png"
            xpos 841
            ypos 28
            action Hide('save', fastDissolve)

    if not renpy.get_screen('load'):
        imagebutton:
            idle "menu_loadgame_init"
            hover "menu_loadgame"
            hovered ResetDisplayable('menu_loadgame')
            focus_mask "ui/side/mask2.png"
            xpos 1045
            ypos 174
            action Show('load', fastDissolve)
    else:
        imagebutton:
            idle "menu_loadgame_back_init"
            hover "menu_loadgame_back"
            hovered ResetDisplayable('menu_loadgame_back')
            focus_mask "ui/side/mask2.png"
            xpos 1045
            ypos 174
            action Hide('load', fastDissolve)

    if not renpy.get_screen('preferences'):
        imagebutton:
            idle "menu_options_init"
            hover "menu_options"
            hovered ResetDisplayable('menu_options')
            focus_mask "ui/side/mask3.png"
            xpos 860
            ypos 323
            action Show('preferences', fastDissolve)
    else:
        imagebutton:
            idle "menu_options_back_init"
            hover "menu_options_back"
            hovered ResetDisplayable('menu_options_back')
            focus_mask "ui/side/mask3.png"
            xpos 856
            ypos 331
            action Hide('preferences', fastDissolve)

    if store.rabbl.in_playthrough():
        imagebutton:
            idle "menu_mainmenu_init"
            hover "menu_mainmenu"
            hovered ResetDisplayable('menu_mainmenu')
            focus_mask "ui/side/mask4.png"
            xpos 1002
            ypos 452
            action MainMenu()

        imagebutton:
            idle "ui/pause/back.png"
            hover "ui/pause/back_hover.png"
            xpos 763
            ypos 241
            action Return()
    else:
        if not renpy.get_screen('extras'):
            imagebutton:
                idle "menu_extras_init"
                hover "menu_extras"
                hovered ResetDisplayable('menu_extras')
                focus_mask "ui/side/mask4.png"
                xpos 1002
                ypos 444
                action Show('extras', fastDissolve)
        else:
            imagebutton:
                idle "menu_extras_back_init"
                hover "menu_extras_back"
                hovered ResetDisplayable('menu_extras_back')
                focus_mask "ui/side/mask4.png"
                xpos 1002
                ypos 444
                action Hide('extras', fastDissolve)

        imagebutton:
            idle "ui/main/exit.png"
            hover "ui/main/exit_hover.png"
            xpos 1183
            ypos 13
            action Quit()

    add "ui/side/pins.png" at delayed(0.5):
        yoffset -6




########################################################################################
# Preferences.
########################################################################################

screen preferences:
    tag submenu
    on "show" action Show('preferences_general')
    on "replace" action Show('preferences_general')
    on "hide" action [ Hide('preferences_general'), Hide('preferences_keymap') ]
    on "replaced" action [ Hide('preferences_general'), Hide('preferences_keymap') ]

    frame:
        background Null()

        add "ui/preferences/options.png":
            xpos 160
            ypos 30

        text __("Options"):
            size 72
            color "#faf6e7"
            xpos 230
            ypos 20

        if not renpy.get_screen('preferences_general'):
            textbutton __("General"):
                text_size 36
                xpos 160
                ypos 110
                background Null()
                text_color "#faf6e7"
                action Show('preferences_general', fastDissolve)
        else:
            textbutton __("General"):
                text_size 36
                xpos 160
                ypos 110
                left_padding 9
                background "ui/preferences/sections/general.png"
                text_color "#4e585f"

        if not renpy.get_screen('preferences_keymap'):
            textbutton __("Keybinds"):
                text_size 36
                xpos 375
                ypos 110
                background Null()
                text_color "#faf6e7"
                action Show('preferences_keymap', fastDissolve)
        else:
            textbutton __("Keybinds"):
                text_size 36
                xpos 380
                ypos 106
                left_padding 8
                top_padding 3
                background "ui/preferences/sections/keybinds.png"
                text_color "#4e585f"


# General preferences.

screen preferences_general:
    tag prefmenu

    add "ui/preferences/icons/adult_content.png":
        xpos 45
        ypos 190

    text __("Adult content"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 190

    add "ui/preferences/checkbox.png":
        xpos 417
        ypos 188
        alpha 0.5

    add "ui/preferences/lock.png":
        xpos 417
        ypos 188

    add "ui/preferences/icons/fullscreen.png":
        xpos 45
        ypos 225

    text __("Fullscreen"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 225

    if game.preferences.fullscreen:
        imagebutton:
            idle "ui/preferences/checkbox_checked.png"
            hover "ui/preferences/checkbox_checked.png"
            xpos 416
            ypos 223
            action renpy.toggle_fullscreen
    else:
        imagebutton:
            idle "ui/preferences/checkbox.png"
            hover "ui/preferences/checkbox.png"
            xpos 417
            ypos 223
            action renpy.toggle_fullscreen

    add "ui/preferences/divider.png":
        xpos 40
        ypos 265

    add "ui/preferences/icons/text_speed.png":
        xpos 45
        ypos 280

    text __("Text speed"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 280

    add "ui/preferences/bar.png":
        xpos 420
        ypos 280

    bar value Preference('text speed'):
        xpos 421
        ypos 280
        xmaximum 270
        left_bar Null()
        right_bar Null()
        thumb 'ui/preferences/bar_handle.png'

    add "ui/preferences/icons/auto_continue.png":
        xpos 45
        ypos 315

    text __("Auto-continue"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 315

    if game.preferences.afm_enable:
        imagebutton:
            idle "ui/preferences/checkbox_checked.png"
            hover "ui/preferences/checkbox_checked.png"
            xpos 416
            ypos 313
            action SetField(game.preferences, 'afm_enable', False)
    else:
        imagebutton:
            idle "ui/preferences/checkbox.png"
            hover "ui/preferences/checkbox.png"
            xpos 417
            ypos 313
            action SetField(game.preferences, 'afm_enable', True)

    add "ui/preferences/icons/auto_continue_time.png":
        xpos 45
        ypos 350

    text __("Auto-continue wait time"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 350     

    add "ui/preferences/bar.png":
        xpos 420
        ypos 350

    bar value Preference('auto-forward time'):
        xpos 421
        ypos 350
        xmaximum 270
        left_bar Null()
        right_bar Null()
        thumb 'ui/preferences/bar_handle.png'

    add "ui/preferences/icons/skip.png":
        xpos 45
        ypos 385

    text __("Skip text"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 385

    if not store.rabbl.in_playthrough():
        add "ui/preferences/lock.png":
            xpos 417
            ypos 383

        imagebutton:
            idle "ui/preferences/checkbox.png"
            hover "ui/preferences/checkbox.png"
            xpos 417
            ypos 383
    elif config.skipping:
        imagebutton:
            idle "ui/preferences/checkbox_checked.png"
            hover "ui/preferences/checkbox_checked.png"
            xpos 416
            ypos 383
            action Unskip()
    else:
        imagebutton:
            idle "ui/preferences/checkbox.png"
            hover "ui/preferences/checkbox.png"
            xpos 417
            ypos 383
            action Skip()

    add "ui/preferences/icons/skip_choice.png":
        xpos 45
        ypos 420

    text __("Keep skipping after choices"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 420

    if game.preferences.skip_after_choices:
        imagebutton:
            idle "ui/preferences/checkbox_checked.png"
            hover "ui/preferences/checkbox_checked.png"
            xpos 416
            ypos 418
            action SetField(game.preferences, 'skip_after_choices', False)
    else:
        imagebutton:
            idle "ui/preferences/checkbox.png"
            hover "ui/preferences/checkbox.png"
            xpos 417
            ypos 418
            action SetField(game.preferences, 'skip_after_choices', True)

    add "ui/preferences/divider.png":
        xpos 40
        ypos 460

    add "ui/preferences/icons/volume_music.png":
        xpos 45
        ypos 475

    text __("Music volume"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 475

    add "ui/preferences/bar.png":
        xpos 420
        ypos 475

    bar value Preference('music volume'):
        xpos 421
        ypos 475
        xmaximum 270
        left_bar Null()
        right_bar Null()
        thumb 'ui/preferences/bar_handle.png'

    add "ui/preferences/icons/volume_ambience.png":
        xpos 45
        ypos 510

    text __("Ambience volume"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 510

    add "ui/preferences/bar.png":
        xpos 420
        ypos 510

    bar value Preference('ambiance volume'):
        xpos 421
        ypos 510
        xmaximum 270
        left_bar Null()
        right_bar Null()
        thumb 'ui/preferences/bar_handle.png'

    add "ui/preferences/icons/volume_sfx.png":
        xpos 45
        ypos 545

    text __("SFX volume"):
        color "#faf6e7"
        size 24
        xpos 85
        ypos 545

    add "ui/preferences/bar.png":
        xpos 420
        ypos 545

    bar value Preference('sound volume'):
        xpos 421
        ypos 545
        xmaximum 270
        left_bar Null()
        right_bar Null()
        thumb 'ui/preferences/bar_handle.png'

    if config.developer or config.testing:
        label '{} v{}-{} - {}'.format(config.name, config.version, git_version() or '[unknown]', renpy.version()):
            xpos 40
            ypos 680
            text_color "#faf6e780"


# Keybinds.

screen preferences_keymap:
    tag prefmenu
    on "hide" action Hide('preferences_kemap_add')
    on "replaced" action Hide('preferences_keymap_add')

    side "c r":
        xpos 80
        ypos 180
        xsize 680
        ysize 510

        viewport id "preferences_keymap_keys":
            mousewheel True

            vbox:
                for command in _keymap_order:
                    if command is None:
                        null height 25
                    else:
                        label _keymap_descriptions[command]:
                            text_color "#faf6e7"
                            left_padding 10
                            right_padding 20
                            text_size 36

                        hbox:
                            box_wrap True

                            for sym in config.keymap.get(command, []): 
                                $ name = _keyname_to_friendly(sym)
                                if name:
                                    label renpy_quote(' + '.join(name)):
                                        text_color "#faf6e7"
                                        xpadding 5
                                    imagebutton:
                                        idle 'ui/preferences/remove.png'
                                        hover 'ui/preferences/remove.png'
                                        right_padding 10
                                        action RemoveKeyBinding(command, sym)
                            imagebutton:
                                idle 'ui/preferences/add.png'
                                hover 'ui/preferences/add.png'
                                action Show('preferences_keymap_add', dissolve, command)

        vbar value YScrollValue('preferences_keymap_keys'):
            top_bar "ui/preferences/scrollbar.png"
            bottom_bar "ui/preferences/scrollbar.png"
            thumb "ui/preferences/scrollbar_handle.png"
            ymaximum 493
            xmaximum 30
            top_gutter 10
            bottom_gutter 10


screen preferences_keymap_add(action):
    python:
        store._keymap_action = action

        # Turn stored key combination intro a friendly key name.
        if hasattr(store, '_keymap_captured_key') and store._keymap_captured_key:
            isjoy, keyname = store._keymap_captured_key

            name = _keyname_to_friendly(keyname)
            if name:
                name = ' + '.join(name)
            else:
                name = '(nothing)'
        else:
            name = '(nothing)'

    frame:
        background "ui/pause/overlay.png"

    frame id "preferences_keymap_add_frame":
        background "ui/yesno/bg.png"
        xpadding 284
        ypadding 192

        add InputGrabBehaviour('_keymap_captured_key', exclude_displayables=['keymap_add_ok', 'keymap_add_cancel'])
        
        text __("Please press the keys or buttons you want to bind."):
            yoffset 50
            size 30
            xmaximum 680
            text_align 0.5
            xalign 0.5
            color "#000000"

        text renpy_quote(name):
            yoffset 100
            size 42
            xmaximum 680
            text_align 0.5
            xalign 0.5
            color "#000000"     
            
        imagebutton id "keymap_add_ok":
            idle "ui/yesno/yes.png"
            hover "ui/yesno/yes_hover.png"
            focus_mask True
            xoffset 455
            yoffset 181
            action [
                If(getattr(store, '_keymap_captured_key', None),
                    lambda: AddKeyBinding(store._keymap_action, store._keymap_captured_key[1], store._keymap_captured_key[0])()),
                Hide('preferences_keymap_add', fastDissolve),
                # Do this delayed so it won't be cleared while the screen is fading.
                Delayed(0.5,
                    SetVariable('_keymap_captured_key', None))
            ]
           
        imagebutton id "keymap_add_cancel":
            idle "ui/yesno/no.png"
            hover "ui/yesno/no_hover.png"
            focus_mask True
            xoffset 588
            yoffset 180
            action [
                Hide('preferences_keymap_add', fastDissolve),
                # Delay this again for above reason.
                Delayed(0.5, SetVariable('_keymap_captured_key', None))
            ]
                    




########################################################################################
# Extras.
########################################################################################

screen extras:
    tag submenu
    on "show" action Show('extras_scenes')
    on "replace" action Show('extras_scenes')
    on "hide" action [ Hide('extras_scenes'), Hide('extras_art'), Hide('extras_music') ]
    on "replaced" action [ Hide('extras_scenes'), Hide('extras_art'), Hide('extras_music') ]

    frame:
        background Null()

        add "ui/extras/extras.png":
            xpos 160
            ypos 30

        text __("Extras"):
            size 72
            color "#faf6e7"
            xpos 230
            ypos 20

        if not renpy.get_screen('extras_scenes'):
            textbutton __("Scene Selection"):
                text_size 36
                xpos 5
                ypos 110
                background Null()
                text_color "#faf6e7"
                action Show('extras_scenes', fastDissolve)
        else:
            textbutton __("Scene Selection"):
                text_size 36
                xpos 7
                ypos 110
                left_padding 9
                background "ui/extras/sections/sceneselect.png"
                text_color "#4e585f"

        if not renpy.get_screen('extras_art'):
            textbutton __("Art Gallery"):
                text_size 36
                xpos 312
                ypos 110
                background Null()
                text_color "#faf6e7"
                action Show('extras_art', fastDissolve)
        else:
            textbutton __("Art Gallery"):
                text_size 36
                xpos 318
                ypos 115
                left_padding 5
                top_padding -3
                background "ui/extras/sections/artgallery.png"
                text_color "#4e585f"

        if not renpy.get_screen('extras_music'):
            textbutton __("Jukebox"):
                text_size 36
                xpos 535
                ypos 110
                background Null()
                text_color "#faf6e7"
                action Show('extras_music', fastDissolve)
        else:
            textbutton __("Jukebox"):
                text_size 36
                xpos 542
                ypos 111
                left_padding 9
                top_padding 0
                background "ui/extras/sections/jukebox.png"
                text_color "#4e585f"

        add "ui/preferences/lock.png":
            xpos 728
            ypos 118

        textbutton __("???"):
            text_size 36
            xpos 710
            ypos 110
            left_padding 8
            top_padding 3
            background Null()
            text_color "#faf6e780"


## Scenes.

screen extras_scenes:
    tag extramenu
    on "show" action Show('extras_scenes_intro')
    on "replace" action Show('extras_scenes_intro')
    on "hide" action [ Hide('extras_scenes_intro'), Hide('extras_scenes_caprice'), Hide('extras_scenes_mekki') ]
    on "replaced" action [ Hide('extras_scenes_intro'), Hide('extras_scenes_caprice'), Hide('extras_scenes_mekki') ]

    frame:
        background Null()

        add "ui/preferences/divider.png":
            xpos 35
            ypos 170

        add "ui/extras/sections/intro.png":
            xpos 55
            ypos 178

        add "ui/extras/icons/intro_blue.png":
            xpos 50
            ypos 185

        textbutton __("Intro"):
            xpos 80
            ypos 180
            text_size 40
            background Null()
            text_color "#4e585f"

        add "ui/extras/icons/caprice.png":
            xpos 310
            ypos 185
            alpha 0.5

        label __("Caprice"):
            xpos 355
            ypos 180
            text_size 40
            text_color "#faf6e780"

        add "ui/preferences/lock.png":
            xpos 390
            ypos 190

        add "ui/extras/icons/mekki.png":
            xpos 587
            ypos 185
            alpha 0.5

        label __("Mekki"):
            xpos 635
            ypos 180
            text_size 40
            text_color "#faf6e780"

        add "ui/preferences/lock.png":
            xpos 660
            ypos 188

        add "ui/preferences/divider.png":
            xpos 35
            ypos 238

screen extras_scenes_intro:
    python:
        _scenes = collections.OrderedDict([
            (scene, meta) for (scene, meta) in store.scenes.items() if not meta.get('hidden', lambda: False)()
        ])
    use extras_scenes_gallery(scenes=_scenes)

screen extras_scenes_gallery:
    default scenes = {}
    $ ROTATIONS = [ -1.02, 0.19, -1.94, 1.18, 0.0, 1.85 ]
    $ import math
    $ row_count = int(math.ceil(len(scenes) / 3.0))

    side "c r":
        xpos 55
        ypos 250
        xsize 730
        ysize 5000
        viewport id "extras_scene_gallery":
            mousewheel True
            child_size (None, 6000)

            vbox:
                for n in range(row_count):
                    hbox:
                        xsize 700
                        yoffset -20 * n
                        for z in enumerate(scenes.items()[n * 3:n * 3 + 3]):
                            $ i, (scene, meta) = z # fuck you renpy
                            $ j = (n % 2) * 3 + i
                            $ k = n * 3 + i

                            frame:
                                background Null()
                                xsize 225
                                ysize 190
                                xoffset -10 * (i + 1)

                                if store.rabbl.seen_scene(scene):
                                    imagebutton:
                                        idle "ui/saveload/slots/{}.png".format(j + 1)
                                        hover "ui/saveload/slots/{}.png".format(j + 1)
                                        action PlayScene(scene)
                                        xoffset -15

                                    add "scripts/sceneshots/{}.png".format(scene) at trotate(ROTATIONS[j]):
                                        yoffset -30

                                    label meta['title'] at trotate(ROTATIONS[j]):
                                        xoffset 20
                                        yoffset 140
                                        text_color "#4e585f"
                                        text_size 12
                                else:
                                    add "ui/extras/locked.png"

                frame:
                    xsize 225
                    ysize row_count * 20
                    background Null()

        vbar value YScrollValue('extras_scene_gallery'):
            top_bar "ui/extras/scrollbar.png"
            bottom_bar "ui/extras/scrollbar.png"
            thumb "ui/preferences/scrollbar_handle.png"
            ymaximum 465
            xmaximum 30
            top_gutter 10
            bottom_gutter 10


## Art gallery.

screen extras_art:
    tag extramenu
    on "show" action Show('extras_art_intro')
    on "replace" action Show('extras_art_intro')
    on "hide" action [ Hide('extras_art_intro'), Hide('extras_art_extra') ]
    on "replaced" action [ Hide('extras_art_intro'), Hide('extras_art_extra') ]

    frame:
        background Null()

        add "ui/preferences/divider.png":
            xpos 35
            ypos 170

        if renpy.get_screen('extras_art_intro'):
            add "ui/extras/sections/intro.png":
                xpos 55
                ypos 178

            add "ui/extras/icons/intro_blue.png":
                xpos 50
                ypos 185

            textbutton __("Intro"):
                xpos 80
                ypos 180
                text_size 40
                background Null()
                text_color "#4e585f"
        else:
            add "ui/extras/icons/intro.png":
                xpos 50
                ypos 185

            textbutton __("Intro"):
                xpos 80
                ypos 180
                text_size 40
                background Null()
                text_color "#faf6e7"
                action Show('extras_art_intro', fastDissolve)

        add "ui/extras/icons/caprice.png":
            xpos 220
            ypos 185
            alpha 0.5

        label __("Caprice"):
            xpos 265
            ypos 180
            text_size 40
            text_color "#faf6e780"

        add "ui/preferences/lock.png":
            xpos 300
            ypos 190

        add "ui/extras/icons/mekki.png":
            xpos 420
            ypos 185
            alpha 0.5

        label __("Mekki"):
            xpos 475
            ypos 180
            text_size 40
            text_color "#faf6e780"

        add "ui/preferences/lock.png":
            xpos 510
            ypos 188

        if renpy.get_screen('extras_art_extra'):
            add "ui/extras/sections/extra.png":
                xpos 599
                ypos 182

            add "ui/extras/icons/extra_blue.png":
                xpos 590
                ypos 183

            textbutton __("Extra"):
                xpos 620
                ypos 180
                text_size 40
                text_color "#4e585f"
                background Null()
        else:
            add "ui/extras/icons/extra.png":
                xpos 590
                ypos 183

            textbutton __("Extra"):
                xpos 620
                ypos 180
                text_size 40
                background Null()
                text_color "#faf6e7"
                action Show('extras_art_extra', fastDissolve)

        add "ui/preferences/divider.png":
            xpos 35
            ypos 238

screen extras_art_intro:
    tag extraartmenu

    use extras_art_gallery(pieces=store.intro_art)

screen extras_art_caprice:
    tag extraartmenu

    use extras_art_gallery(pieces=store.caprice_art)

screen extras_art_mekki:
    tag extraartmenu

    use extras_art_gallery(pieces=store.mekki_art)

screen extras_art_extra:
    tag extraartmenu

    use extras_art_gallery(pieces=store.guest_art)

screen extras_art_gallery:
    default pieces = {}
    $ ROTATIONS = [ -1.02, 0.19, -1.94, 1.18, 0.0, 1.85 ]

    $ import math
    $ row_count = int(math.ceil(len(pieces) / 3.0))

    side "c r":
        xpos 55
        ypos 250
        xsize 730
        ysize 2500
        viewport id "extras_scene_gallery":
            mousewheel True
            child_size (None, 6000)

            vbox:
                for n in range(row_count):
                    hbox:
                        xsize 700
                        yoffset -20 * n
                        for z in enumerate(pieces.items()[n * 3:n * 3 + 3]):
                            $ i, (name, meta) = z # fuck you renpy
                            $ j = (n % 2) * 3 + i
                            $ k = n * 3 + i

                            frame:
                                background Null()
                                xsize 225
                                ysize 190
                                xoffset -10 * (i + 1)

                                if not meta.get('locked', lambda: False)():
                                    imagebutton:
                                        idle "ui/saveload/slots/{}.png".format(j + 1)
                                        hover "ui/saveload/slots/{}.png".format(j + 1)
                                        action Show('extras_art_single', dissolve, name, meta)
                                        xoffset -15

                                    add meta['thumb'] at trotate(ROTATIONS[j]):
                                        yoffset -30

                                    label name at trotate(ROTATIONS[j]):
                                        text_color "#4e585f"
                                        text_size 16
                                        xoffset 21
                                        yoffset 140

                                else:
                                    add "ui/extras/locked.png"

                frame:
                    xsize 225
                    ysize (row_count + 5) * 35
                    background Null()

        if len(pieces) > 6:
            vbar value YScrollValue('extras_scene_gallery'):
                top_bar "ui/extras/scrollbar.png"
                bottom_bar "ui/extras/scrollbar.png"
                thumb "ui/preferences/scrollbar_handle.png"
                ymaximum 465
                xmaximum 30
                top_gutter 10
                bottom_gutter 10
        else:
            null width 1

screen extras_art_single(piece, meta):
    modal True
    on "show" action SetVariable('_extras_art_single_index', 0)
    on "hide" action Hide('extras_art_single_overlay', dissolve)
    on "replaced" action Hide('extras_art_single_overlay', dissolve)

    if isinstance(meta['file'], list):
        $ f = meta['file'][_extras_art_single_index]
    elif meta.get('native'):
        $ f = meta['native']
    else:
        $ f = meta['file']

    add f:
        xalign 0.5
        yalign 0.0

    mousearea:
        area (0, 520, 1280, 200)
        hovered Show('extras_art_single_overlay', dissolve, piece, meta)
        unhovered Hide('extras_art_single_overlay', dissolve)

screen extras_art_single_overlay(piece, meta):
    add "ui/extras/gallery/overlay.png"

    label '"{}"'.format(piece):
        xpos 200
        ypos 595
        text_color "#faf6e7"
        text_size 36

    if meta.get('artist'):
        label "by":
            xpos 220
            ypos 640
            text_color "#faf6e780"
            text_size 18

        label meta['artist']:
            xpos 245
            ypos 635
            text_color "#faf6e7"
            text_size 24

    if meta.get('url'):
        label "at":
            xpos 222
            ypos 668
            text_color "#faf6e780"
            text_size 18

        label meta['url']:
            xpos 245
            ypos 663
            text_color "#faf6e7"
            text_size 24

    if isinstance(meta['file'], list):
        hbox:
            xpos 600
            ypos 600

            for entry in enumerate(meta['file']):
                $ i, f = entry
                if i == _extras_art_single_index:
                    textbutton chr(ord('A') + i):
                        background "ui/extras/gallery/abc_current.png"
                        text_size 30
                        text_color "#897664"
                else:
                    textbutton chr(ord('A') + i):
                        background "ui/extras/gallery/abc.png"
                        action SetVariable('_extras_art_single_index', i)
                        text_size 30
                        text_color "#d8deef"

    imagebutton:
        idle "ui/extras/gallery/back.png"
        hover "ui/extras/gallery/back.png"
        xpos 50
        ypos 600
        action Hide('extras_art_single', dissolve)

## Music gallery.

screen extras_music:
    on "hide" action Stop('jukebox', fadeout=2.0)
    on "replaced" action Stop('jukebox', fadeout=2.0)
    tag extramenu

    python:
        _tracks = collections.OrderedDict([
            (track, meta) for (track, meta) in store.tracks.items() if not meta.get('hidden', lambda: False)()
        ])

    frame:
        background Null()

        add "ui/preferences/divider.png":
            xpos 35
            ypos 170

        use extras_music_player(tracks=_tracks)

screen extras_music_player:
    default columns = 2
    default tracks = {}
    $ import math
    $ current = None
    $ curridx = None

    side "c r":
        xpos 80
        ypos 173
        xsize 700
        ysize 462

        viewport id "extras_music_player":
            mousewheel True

            $ piece = int(math.ceil(len(tracks) / float(columns)))

            for n in range(columns):
                vbox:
                    xpos 350 * n
                    yoffset 10
                    ysize 1000
                    spacing 10

                    for entry in enumerate(tracks.items()[piece * n:piece * (n + 1)], piece * n):
                        $ i, (track, meta) = entry

                        if renpy.music.get_playing('jukebox') == track:
                            $ current = meta['title']
                            $ curridx = i
                            textbutton meta['title']:
                                background "#faf6e7"
                                text_color "#4e585f"
                        else:
                            textbutton meta['title']:
                                background Null()
                                text_color "#faf6e7"
                                action JukeboxPlay(track)

        null width 1

    add "ui/preferences/divider.png":
        xpos 35
        ypos 633

    if current is not None:
        label current:
            xpos 40
            ypos 652
            text_size 28
            text_color "#faf6e7"
    else:
        label __("Nothing playing"):
            xpos 40
            ypos 652
            text_size 28
            text_color "#faf6e780"

    if renpy.music.get_playing('jukebox'):
        imagebutton:
            idle "ui/extras/jukebox/back.png"
            hover "ui/extras/jukebox/back.png"
            xpos 340
            ypos 650
            action JukeboxPlay(tracks.keys()[((curridx or 0) - 1) % len(tracks)])
    else:
        imagebutton at transparent(0.5):
            idle "ui/extras/jukebox/back.png"
            hover "ui/extras/jukebox/back.png"
            xpos 340
            ypos 650

    if paused('jukebox'):
        imagebutton:
            idle "ui/extras/jukebox/play.png"
            hover "ui/extras/jukebox/play.png"
            xpos 390
            ypos 650
            action [ Resume('jukebox'), renpy.restart_interaction ]
    elif renpy.music.get_playing('jukebox'):
        imagebutton:
            idle "ui/extras/jukebox/pause.png"
            hover "ui/extras/jukebox/pause.png"
            xpos 390
            ypos 650
            action [ Pause('jukebox'), renpy.restart_interaction ]
    else:
        imagebutton:
            idle "ui/extras/jukebox/play.png"
            hover "ui/extras/jukebox/play.png"
            xpos 390
            ypos 650
            action JukeboxPlay(tracks.keys()[0])

    if renpy.music.get_playing('jukebox'):
        imagebutton:
            idle "ui/extras/jukebox/forward.png"
            hover "ui/extras/jukebox/forward.png"
            xpos 440
            ypos 650
            action JukeboxPlay(tracks.keys()[((curridx or 0) + 1) % len(tracks)])
    else:
        imagebutton at transparent(0.5):
            idle "ui/extras/jukebox/forward.png"
            hover "ui/extras/jukebox/forward.png"
            xpos 440
            ypos 650

    if renpy.music.get_playing('jukebox'):
        imagebutton:
            idle "ui/extras/jukebox/stop.png"
            hover "ui/extras/jukebox/stop.png"
            xpos 490
            ypos 650
            action [ Stop('jukebox'), renpy.restart_interaction ]
    else:
        imagebutton at transparent(0.5):
            idle "ui/extras/jukebox/stop.png"
            hover "ui/extras/jukebox/stop.png"
            xpos 490
            ypos 650

    bar value Preference('jukebox volume'):
        xpos 555
        ypos 655
        xmaximum 185
        left_bar 'ui/extras/jukebox/slider.png'
        right_bar 'ui/extras/jukebox/slider.png'
        thumb 'ui/extras/jukebox/handle.png'

    if game.preferences.get_volume('jukebox') > 0:
        add "ui/extras/jukebox/volume{}.png".format(min(3, int(game.preferences.get_volume('jukebox') / 0.33 + 1))):
            xpos 750
            ypos 620




########################################################################################
# Save/load.
########################################################################################

init python:
    _current_save = None

screen saveload:
    default save = False
    default load = False
    python:
        ROTATIONS = [ -1.02, 0.19, -1.94, 1.18, 0.0, 1.85 ]
        OFFSETS = [ (0, 0), (0, 0), (-2, -2), (0, 2), (0, 0), (0, 3) ]

    mousearea:
        xpos 0
        ypos 0
        xsize 65
        ysize 720
        hovered SetVariable('_current_save', None)

    mousearea:
        xpos 755
        ypos 0
        xsize 465
        ysize 720
        hovered SetVariable('_current_save', None)

    mousearea:
        xpos 0
        ypos 0
        xsize 1280
        ysize 185
        hovered SetVariable('_current_save', None)

    mousearea:
        xpos 0
        ypos 543
        xsize 1280
        ysize 177
        hovered SetVariable('_current_save', None)  

    for i in range(1, 7):
        if FileLoadable(i):
            if save:
                $ act = FileSave(i)
            else:
                $ act = FileLoad(i)
            
            $ ttitle = store.scenes[FileJson(i, 'scene')]['title']
            mousearea:
                xpos 65 + ((i - 1) % 3) * 220
                ypos 185 + (170 if i > 3 else 0)
                xsize 250
                ysize 188
                hovered SetVariable('_current_save', i)

            imagebutton:
                idle "ui/saveload/slots/{}.png".format(i)
                hover "ui/saveload/slots/{}.png".format(i)
                xpos 55 + ((i - 1) % 3) * 220
                ypos 195 + (170 if i > 3 else 0)
                action act

            add FileScreenshot(i) at trotate(ROTATIONS[i - 1]):
                xpos 71 + ((i - 1) % 3) * 220
                ypos 162 + (170 if i > 3 else 0)

            window style "label":
                xpos 90 + ((i - 1) % 3) * 220
                ypos 333 + (170 if i > 3 else 0)

                if len(ttitle) > 25:
                    text ttitle style "label_text":
                        color "#4e585f"
                        size 12
                        xoffset -2
                else:
                    text ttitle style "label_text":
                        color "#4e585f"
                        size 14

            if _current_save == i:
                imagebutton:
                    idle "ui/saveload/slots/{}_trash.png".format(i)
                    hover "ui/saveload/slots/{}_trash.png".format(i)
                    xpos 55 + ((i - 1) % 3) * 220 + OFFSETS[i - 1][0]
                    ypos 195 + (170 if i > 3 else 0) + OFFSETS[i - 1][1]
                    focus_mask True
                    action FileDelete(i)

        else:
            mousearea:
                xpos 65 + ((i - 1) % 3) * 220
                ypos 185 + (170 if i > 3 else 0)
                xsize 250
                ysize 188
                hovered SetVariable('_current_save', None)

            if save:
                $ act = FileSave(i)
                $ slot = "ui/saveload/slots/empty.png"
                $ hvr = "ui/saveload/slots/add.png"
            else:
                $ act = None
                $ slot = "ui/saveload/slots/empty.png"
                $ hvr = "ui/saveload/slots/empty.png"

            imagebutton:
                idle slot
                hover hvr
                xpos 55 + ((i - 1) % 3) * 220
                ypos 195 + (170 if i > 3 else 0)
                action act

# The file save screen.
screen save:
    tag submenu

    frame:
        background Null()
        
        add "ui/saveload/save.png":
            xpos 102
            ypos 123
            
        text "Save":
            xpos 185
            ypos 133
            size 40

        use saveload(save=True)
        
# The file load screen.
screen load:
    tag submenu

    frame:
        background Null()
        
        add "ui/saveload/load.png":
            xpos 102
            ypos 123
            
        text "Load":
            xpos 185
            ypos 133
            size 40

        use saveload(load=True)




########################################################################################
# Misc.
########################################################################################

# General yes/no prompt.
screen yesno_prompt:
    modal True
    
    frame:
        background "ui/yesno/bg.png"
       
        xpadding 284
        ypadding 192
        
        text __(message):
            yoffset 50
            size 30
            xmaximum 680
            text_align 0.5
            xalign 0.5
            color "#000000"
            
        imagebutton:
            idle "ui/yesno/yes.png"
            hover "ui/yesno/yes_hover.png"
            focus_mask True
            xoffset 455
            yoffset 181
            action yes_action
           
        imagebutton:
            idle "ui/yesno/no.png"
            hover "ui/yesno/no_hover.png"
            focus_mask True
            xoffset 588
            yoffset 180
            action no_action

screen yesno_saveload:
    frame:
        background "ui/saveload/prompt.png"
        
        xpos 94
        ypos y
        
        text __("Are you sure you want to overwrite?"):
            xanchor 0.5
            xpos 236
            ypos 20
            xmaximum 472
            ymaximum 50
            color "#716957"
        
        imagebutton:
            idle "ui/saveload/no.png"
            hover "ui/saveload/no_hover.png"
            xanchor 0.5
            yanchor 0.5
            xpos 184
            ypos 84
            xmaximum 40
            ymaximum 40
            action Hide('yesno_saveload')
        
        imagebutton:
            idle "ui/saveload/yes.png"
            hover "ui/saveload/yes_hover.png"
            xanchor 0.5
            yanchor 0.5
            xpos 282
            ypos 84
            xmaximum 40
            ymaximum 40

            action [ SetDict(persistent.save_game_names, (int(FileCurrentPage()), i), title), FileSave(i, confirm=False), Hide('yesno_saveload') ]





########################################################################################
# HUD elements.
########################################################################################

# Choice window.
screen choice:
    window:
        style "menu_window"
        background "ui/choicebar.png"
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            xalign 0.5
            yoffset -2
            
            for caption, act, chosen in items:
                button:
                    action act
                    style "menu_choice_button"
                    text caption style "menu_choice"
                    xalign 0.5
                    yoffset 100
                    left_padding 30
                    bottom_padding 20

# The saybox.
screen say:
    default doublespeak = False

    python:
        tb = Null()
        if who:
            if doublespeak:
                bg = "ui/textbar/double/" + '_'.join(who) + '.png'
                tb = "ui/textbar/names/" + '_'.join(who) + '.png'
            elif who == 'Oliver':
                bg = "ui/textbar/oliver.png"
                tb = "ui/textbar/names/oliver.png"
            elif who in character_tags:
                # Don't ask. Just don't.
                img = renpy.game.context().scene_lists.get_displayable_by_tag('master', character_tags[who].split('_', 2)[0])
                phone = renpy.game.context().scene_lists.get_displayable_by_tag('master', 'phone')
                attributes = renpy.game.context().images.get_attributes('master', character_tags[who].split('_', 2)[0])

                if 'ui/textbar/names/' + character_tags[who] + '.png' in renpy.list_files():
                    tb = 'ui/textbar/names/' + character_tags[who] + '.png'
                if phone is not None:
                    bg = "ui/textbar/phone.png"
                elif img is None:
                    bg = "ui/textbar/default.png"
                else:
                    pos = renpy.get_placement(img)
                    
                    if pos.xpos >= 0.80:
                        bg = "ui/textbar/farright.png"
                    elif pos.xpos >= 0.70:
                        bg = "ui/textbar/midright.png"
                    elif pos.xpos > 0.5:
                        bg = "ui/textbar/right.png"
                    elif pos.xpos <= 0.20:
                        bg = "ui/textbar/farleft.png"
                    elif pos.xpos <= 0.30:
                        bg = "ui/textbar/midleft.png"
                    elif pos.xpos < 0.5: 
                        bg = "ui/textbar/left.png"
                    elif 'flip' in attributes:
                        bg = "ui/textbar/right.png"
                    else:
                        bg = "ui/textbar/left.png"
            else:
                bg = "ui/textbar/right.png"
        else:
            bg = "ui/textbar/default.png"

    window id "window":
        background bg
        yoffset 456

        frame:
            background Null()
            add tb:
                xpos 155 - 12
                ypos 38 - 10

        frame:
            background Null()
            yminimum 262
            xpadding 135
            ypadding 15
            xmaximum 1100

            if doublespeak:
                text what[0]:
                    id "what"
                    color "#352114"
                    xpos 80
                    ypos 100
                    slow (not renpy.in_rollback())
                text what[1]:
                    id "what"
                    color "#352114"
                    xpos 535
                    ypos 100
                    slow (not renpy.in_rollback())
            else:
                text what:
                    id "what"
                    color "#352114"
                    xpos 80
                    ypos 100
