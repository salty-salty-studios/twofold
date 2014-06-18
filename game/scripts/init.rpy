# init.rpy
# Global script initialization.

label scene_init:
    python:
        import collections

        available_languages = collections.OrderedDict({
            # 'directory': ('English language name', 'Native language name')
            'en': ('English', 'English')
        })

        sprite_offsets = {
            'caprice': 160,
            'mekki': -80,
            'izaac': 100,
            'wallace': 175,
            'generic': 200,
            'hayley': 130,
            'lawe': 150,
            'tanya': 40,
            'darren': 175,
            'heather': -50,
            'allison': -55,
            'eileen': -70
        }

    return

label scene_start:
    stop music fadeout 5.0
    return

label scene_end:
    scene black with dissolve
    return
