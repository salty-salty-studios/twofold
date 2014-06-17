label scene_init_en:
    python:
        characters = {
            # Main characters.
            'oliver':     ('Oliver', '#789922'),
            'caprice':    ('Caprice', '#6e9aa1'),
            'mekki':      ('Mekki', '#6e9aa1'),
            'mekkiu':     ('Snob{=mekki}', '#6e9aa1'),
            'hayley':     ('Hayley', '#cc9351'),
            'hayleyu':    ('\'Phones', '#cc9351'),
            'izaac':      ('Izaac', '#b2678a'),
            'izaacu':     ('Burglar{=izaac}', '#b2678a'),
            
            # Side characters.
            'lawe':       ('Mr. Lawe', '#6d6862'),
            'allison':    ('Allison', '#eef0f1'),
            'allisonu':   ('Girl{=allison}', '#eef0f1'),
            'darren':     ('Darren', '#f0dd85'),
            'darrenu':    ('Pretty boy{=darren}', '#f0dd85'),
            'darrenuu':   ('Guy{=darren}', '#f0dd85'),
            'eileen':     ('Eileen', '#9a9065'),
            'eileenu':    ('Angry girl{=eileen}', '#9a9065'),
            'franklin':   ('Franklin', '#f7f3e9'),
            'franklinu':  ('Professor{=franklin}', '#f7f3e9'),
            'heather':    ('Heather', '#fab8b2'),
            'heatheru':   ('Ginger{=heather}', '#fab8b2'),
            'mom':        ('Mom', '#000000'),
            'tanya':      ('Tanya', '#a7897a'),
            'tanyau':     ('Person{=tanya}', '#a7897a'),
            'tanyauu':    ('Slayer{=tanya}', '#a7897a'),
            'wallace':    ('Wallace', '#b2678a'),
            'wallaceu':   ('Person{=wallace}', '#b2678a'),

            # Anonymous characters.
            'unknown':    ('???', '#000000'),
            'professor':  ('Professor', '#8f8671'),
            'guy':        ('Guy', '#8f8671'),
            'student':    ('Student', '#8f8671'),
            'waitress':   ('Barista', '#88a940')
        }

        character_tags = {
            'Oliver': 'oliver',
            'Mr. Lawe': 'lawe',
            'Caprice': 'caprice',
            'Mekki': 'mekki',
            'Snob{=mekki}': 'mekki_snob',
            'Allison': 'allison',
            'Girl{=allison}': 'allison_crybaby',
            'Hayley': 'hayley',
            'Wallace': 'wallace',
            'Tanya': 'tanya',
            'Eileen': 'eileen',
            'Darren': 'darren',
            'Pretty boy{=darren}': 'darren_prettyboy',
            'Heather': 'heather',
            'Student': 'student',
            'Izaac': 'izaac',
            'Guy': 'guy',
            'Girl': 'girl',
            'Professor': 'professor',
            'Franklin': 'professor',
            'Professor{=franklin}': 'professor',
            'Mom': 'mom',
            'Person{=wallace}': 'wallace_jerk',
            'Barista': 'barista',
            'Tanya': 'tanya',
            'Slayer{=tanya}': 'tanya_voice',
            'Person{=tanya}': 'tanya_shorty',
            'Heather': 'heather',
            'Ginger{=heather': 'ginger',
            '\'Phones': 'hayley_phones',
            'Burglar{=izaac}': 'izaac_burglar',
            'Angry girl{=eileen}': 'eileen_rudegirl',
            'Guy{=darren}': 'guy',
            '???': 'student' # XXX: make person textbox
        }

        scenes = collections.OrderedDict([
            # Common route.
            ('1S1', {
                'title': 'Failure Begins with an O'
            }),
            ('1S2', {
                'title': 'Momma\'s Boy'
            }),
            ('1S3', {
                'title': 'One-Sided'
            }),
            ('1S4', {
                'title': 'Capital C'
            }),
            ('1S5', {
                'title': 'Beef Stroganoff'
            }),
            ('1S6', {
                'title': 'Whoops'
            }),
            ('1S7', {
                'title': 'Towers and Walls'
            }),
            ('1S8', {
                'title': 'First Impressions'
            }),
            ('1S9', {
                'title': 'As Bitter as the Coffee'
            }),
            ('1S10', {
                'title': 'Not Quite What You Were Expecting'
            }),
            ('1S11', {
                'title': 'I\'m Not Good With Words'
            }),
            ('1S12', {
                'title': 'The Club With One Rule'
            }),
            ('1S13', {
                'title': 'Running in Circles'
            }),
            ('1S14', {
                'title': 'Hiding in the Enemy\'s Headquarters'
            }),
            ('1S15', {
                'title': 'The Price of Dignity'
            }),
            ('1S16', {
                'title': 'Pick Your Battles'
            }),
            ('1S17', {
                'title': 'The Actor'
            }),
            ('1S18', {
                'title': 'Voices in Your Head',
            }),
            ('1S19', {
                'title': 'Turf War'
            }),
            ('1S20', {
                'title': 'A Tough Decision'
            }),
            ('1S20_intro', { 
                'title': 'A Tough Decision',
                'hidden': lambda: True
            }),
            ('1S20_caprice_summary', {
                'title': 'A Tough Decision',
                'hidden': lambda: True
            }),
            ('1S20_mekki_summary', {
                'title': 'A Tough Decision',
                'hidden': lambda: True
            }),
            ('1S20_club_choice', {
                'title': 'A Tough Decision',
                'hidden': lambda: True
            })
        ])

        tracks = collections.OrderedDict([
            ('music/wellworkonit.ogg', {
                'title': 'We\'ll work on it'
            }),
            ('music/hopskipjump.ogg', {
                'title': 'A hop, a skip and a jump!'
            }),
            ('music/caps.ogg', {
                'title': 'Upward spiral'
            }),
            ('music/mek.ogg', {
                'title': 'Married to the idea'
            }),
            ('music/tense.ogg', {
                'title': 'Stress'
            }),
            ('music/tense_lawe.ogg', {
                'title': 'Stress (Lawe)'
            }),
            ('music/panic.ogg', {
                'title': 'Panic!'
            }),
            ('music/genericrelaxmusic.ogg', {
                'title': 'Tired eyes'
            }),
            ('music/handholding.ogg', {
                'title': 'Hand holding'
            }),
            ('music/capitals.ogg', {
                'title': 'Pep in your step'
            }),
            ('music/papercookies.ogg', {
                'title': 'Paper cookies'
            }),
            ('music/ringtone.mp3', {
                'title': 'Paper cookies (ringtone)'
            }),
            ('music/afternoon.mp3', {
                'title': 'Inspired'
            }),
            ('music/fauxhorror.ogg', {
                'title': 'Am I gonna die?'
            }),
            ('music/takingnotes.ogg', {
                'title': 'Taking notes'
            }),
            ('music/aroundcampus.ogg', {
                'title': 'Around campus'
            }),
            ('music/scrappedstories.ogg', {
                'title': 'Scrapped stories'
            }),
            ('music/extracurricular.ogg', {
                'title': 'Extra-curricular'
            }),
            ('music/saltytears.ogg', {
                'title': 'Salty Tears'
            }),
            ('music/credits.ogg', {
                'title': 'But we aren\'t done yet...'
            })
        ])

        intro_art = collections.OrderedDict([
            ('Calling home', {
                'file': 'cgs/oliver_callmom.png',
                'thumb': 'cgs/oliver_callmom_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S2')
            }),
            ('PANIC!', {
                'file': 'cgs/alarmclock.png',
                'thumb': 'cgs/alarmclock_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S3')
            }),
            ('Wallace introduction', {
                'file': ['cgs/wallace_intro.png', 'cgs/wallace_intro_away.png', 'cgs/wallace_intro_awayfrown.png'],
                'thumb': 'cgs/wallace_intro_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S3')
            }),
            ('Caprice introduction', {
                'file': ['cgs/caprice_intro.png', 'cgs/caprice_intro_notice.png', 'cgs/caprice_intro_smirk.png'],
                'thumb': 'cgs/caprice_intro_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S4')
            }),
            ('A burglar appears', {
                'file': 'cgs/izaac_burglar.png',
                'thumb': 'cgs/izaac_burglar_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S5')
            }),
            ('Crashed into eachother', {
                'file': 'cgs/allison_crash.png',
                'thumb': 'cgs/allison_crash_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S6')
            }),
            ('Eileen introduction', {
                'file': 'cgs/eileen_intro.png',
                'thumb': 'cgs/eileen_intro_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S7')
            }),
            ('Mekki introduction', {
                'file': 'cgs/mekki_intro.png',
                'thumb': 'cgs/mekki_intro_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S9')
            }),
            ('Monster or Maiden', {
                'file': 'cgs/tanya_intro.png',
                'thumb': 'cgs/tanya_intro_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S10')
            }),
            ('Welcome to the Art Club!', {
                'file': ['cgs/artclub_intro.png', 'cgs/artclub_intro_pushdown.png', 'cgs/artclub_intro_seated.png'],
                'thumb': 'cgs/artclub_intro_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S12')
            }),
            ('Interrupted', {
                'file': 'cgs/mekki_library.png',
                'thumb': 'cgs/mekki_library_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S14')
            }),
            ('The Writing Club!', {
                'file': 'cgs/writingclub_intro.png',
                'thumb': 'cgs/writingclub_intro_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S15')
            }),
            ('It\'s time to choose.', {
                'file': 'cgs/club_day.png',
                'thumb': 'cgs/club_day_thumb.png',
                'locked': lambda: not store.rabbl.seen_scene('1S20')
            })
        ])

        caprice_art = collections.OrderedDict([
        ])

        mekki_art = collections.OrderedDict([
        ])

        guest_art = collections.OrderedDict([
            ('Colors', {
                'file': 'vfx/guest/acotan.jpg',
                'thumb': 'vfx/guest/acotan_thumb.png',
                'native': 'vfx/guest/acotan_native.jpg',
                'artist': 'AcoTan',
                'url': '4rcher.deviantart.com',
                'size': (2560, 1440),
                'locked': lambda: not persistent.demo_completed
            }),
            ('VERY LEWD TOP HATS', {
                'file': 'vfx/guest/doomfest.jpg',
                'thumb': 'vfx/guest/doomfest_thumb.png',
                'native': 'vfx/guest/doomfest_native.jpg',
                'artist': 'Doomfest',
                'url': 'doomfest.com',
                'size': (3540, 1956),
                'locked': lambda: not persistent.demo_completed
            }),
            ('Spice Jar', {
                'file': 'vfx/guest/skrats.png',
                'thumb': 'vfx/guest/skrats_thumb.png',
                'native': 'vfx/guest/skrats_native.png',
                'artist': 'Skrats',
                'url': 'skrats.deviantart.com',
                'size': (2181, 1500),
                'locked': lambda: not persistent.demo_completed
            }),
            ('Hot Paint Play', {
                'file': 'vfx/guest/vcr.png',
                'thumb': 'vfx/guest/vcr_thumb.png',
                'native': 'vfx/guest/vcr_native.png',
                'artist': 'VCR',
                'url': 'cyzirvisheen.deviantart.com',
                'size': (4800, 2700),
                'locked': lambda: not persistent.demo_completed
            }),
            ('Nimbus', {
                'file': 'vfx/guest/timbaer.png',
                'thumb': 'vfx/guest/timbaer_thumb.png',
                'native': 'vfx/guest/timbaer_native.png',
                'artist': 'Timbaer',
                'url': 'timbaer.tumblr.com',
                'size': (3840, 2160),
                'locked': lambda: not persistent.demo_completed
            }),
            ('Maids', {
                'file': 'vfx/guest/tagicrabbu.png',
                'thumb': 'vfx/guest/tagicrabbu_thumb.png',
                'native': 'vfx/guest/tagicrabbu_native.png',
                'artist': 'tagicrabbu',
                'url': 'pixiv.me/tohkabwaka',
                'size': (1366, 768),
                'locked': lambda: not persistent.demo_completed
            }),
            ('President Shiften calling!', {
                'file': 'vfx/guest/morthiasik.png',
                'thumb': 'vfx/guest/morthiasik_thumb.png',
                'native': 'vfx/guest/morthiasik_native.png',
                'artist': 'Morthiasik',
                'url': 'morthiasik.deviantart.com',
                'size': (2666, 1500),
                'locked': lambda: not persistent.demo_completed
            }),
            ('Picnic', {
                'file': 'vfx/guest/monorus.png',
                'thumb': 'vfx/guest/monorus_thumb.png',
                'artist': 'monorus',
                'url': 'monorus.deviantart.com',
                'size': (1280, 720),
                'locked': lambda: not persistent.demo_completed
            }),
            ('Whatever You Like!', {
                'file': 'vfx/guest/shunao.png',
                'thumb': 'vfx/guest/shunao_thumb.png',
                'native': 'vfx/guest/shunao_native.png',
                'artist': 'shunao',
                'url': 'shunao.org',
                'size': (4533, 2500),
                'locked': lambda: not persistent.demo_completed
            })
        ])

        ui_text = {
            # 'Original text':
            #   'Translated text',

            # Pause menu.
            'Unknown scene':
                'Unknown scene',
            'Nothing playing':
                'Nothing playing',

            # Preferences.
            'Options':
                'Options',
            'General':
                'General',
            'Keybinds':
                'Keybinds',
            'Adult content':
                'Adult content',
            'Fullscreen':
                'Fullscreen',
            'Text speed':
                'Text speed',
            'Auto-continue':
                'Auto-continue',
            'Auto-continue wait time':
                'Auto-continue wait time',
            'Skip text':
                'Skip text',
            'Keep skipping after choices':
                'Keep skipping after choices',
            'Music volume':
                'Music volume',
            'Ambience volume':
                'Ambience volume',
            'SFX volume':
                'SFX volume',
            'Please press the keys or buttons you want to bind.':
                'Please press the keys or buttons you want to bind.',

            # Extras.
            'Extras':
                'Extras',
            'Scene Selection':
                'Scene Selection',
            'Art Gallery':
                'Art Gallery',
            'Jukebox':
                'Jukebox',
            '???':
                '???',

            # Scene selection / art gallery.
            'Intro':
                'Intro',
            'Caprice':
                'Caprice',
            'Mekki':
                'Mekki',
            'Extra':
                'Extra',

            # Yes/no dialog.
            'Are you sure you want to overwrite?':
                'Are you sure you want to overwrite?'
        }
    return

label scene_start_en:
    return

label scene_end_en:
    return
