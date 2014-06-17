init -1601 python:
    ## Pause functionality.
    # Allows you to pause and resume audio channels.
    if not hasattr(renpy.audio.audio.Channel, '__old_init__'):
        renpy.audio.audio.Channel.__old_init__ = renpy.audio.audio.Channel.__init__

    def channel_init(self, *args, **kwargs):
        self.__old_init__(*args, **kwargs)
        self.paused = False

    def channel_pause(self):
        renpy.audio.audio.pss.pause(self.number)
        self.paused = True

    def channel_resume(self):
        renpy.audio.audio.pss.unpause(self.number)
        self.paused = False

    renpy.audio.audio.Channel.__init__ = channel_init
    renpy.audio.audio.Channel.pause = channel_pause
    renpy.audio.audio.Channel.resume = channel_resume

    class Pause(Action):
        def __init__(self, channel):
            self.channel = channel

        def __call__(self):
            ch = renpy.music.get_channel(self.channel)
            if not ch.paused:
                ch.pause()

    class Resume(Action):
        def __init__(self, channel):
            self.channel = channel

        def __call__(self):
            ch = renpy.music.get_channel(self.channel)
            if ch.paused:
                ch.resume()

    def paused(channel):
        ch = renpy.music.get_channel(channel)
        return ch.paused
