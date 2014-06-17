python early:
    ## Queue song intro and loop the song body.
    def play_li(intro, main, channel="music", fadein=0, tight=None):
        music.queue(intro, loop=False, clear_queue=True, channel=channel, fadein=fadein, tight=tight)
        music.queue(main, loop=True, clear_queue=False, channel=channel, tight=tight, fadein=0)

    renpy.play_li = play_li
