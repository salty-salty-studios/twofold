 init -1499 python:
    ## Restart interactions when a MixerValue changed.
    # This helps for when UI elements on your screen depend on the volume as set by a MixerValue,
    # so that they get updated as the bar slides.
    old_MixerValue_set_mixer = MixerValue.set_mixer

    def salty_set_mixer(self, value):
        old_MixerValue_set_mixer(self, value)
        renpy.restart_interaction()

    MixerValue.set_mixer = salty_set_mixer
