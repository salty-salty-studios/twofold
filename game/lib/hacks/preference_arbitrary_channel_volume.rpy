init python:
    ## Make Preference take *any* '<channel> volume' option.
    # Useful for when you have custom channels you want to control in your preferences screen.
    old_Preference = Preference

    def Preference(name, value=None):
        name = name.lower()

        if isinstance(value, basestring):
            value = value.lower()

        if name.endswith(' volume') and name.split()[0] in renpy.audio.audio.channels and name.split()[0] not in ('music', 'sound'):
            if value is None:
                return MixerValue(name.split()[0])
            else:
                return SetMixer(name.split()[0], value)

        return old_Preference(name, value)
