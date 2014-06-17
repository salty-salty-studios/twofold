init python:
    ## Jukebox support functions.

    # Register channel.
    renpy.music.register_channel('jukebox', 'jukebox', False, tight=True)

    # Reload the screen when the queue became empty to update play status.
    def jukebox_empty():
        if not renpy.music.get_playing('jukebox'):
            if jukebox_empty.was_playing:
                jukebox_empty.was_playing = False
                renpy.restart_interaction()
        elif not jukebox_empty.was_playing:
            jukebox_empty.was_playing = True

    jukebox_empty.was_playing = False
    renpy.music.set_queue_empty_callback(jukebox_empty, channel='jukebox')

    def JukeboxPlay(track=None):
        if track:
            pl = Play('jukebox', track, fadein=2.0) 
        else:
            pl = Resume('jukebox')
        return [ Stop('music', fadeout=2.0), pl, renpy.restart_interaction ]

    def JukeboxPause():
        return Pause('jukebox')
