init 1 python:
    ## User-defined keymap functionality.
    # Copyright (C) 2014 Shiz.
    # Usage: Loop over _keymap_order in a screen, for every entry loop over the key entries in config.keymap.get(entry, []).
    #  RemoveKeyBinding(entry, key) is a screen action that will remove the given keymap binding.
    #  To add a key binding, add InputGrabBehaviour('target_var', exclude_displayables['confirm_button', 'cancel_button'])
    #  to a dedicated screen where the user can input their desired keybind,
    #  and use the AddKeyBinding(entry, key, joystick) screen action to add the given key to the keymap.
    #  target_var will be a tuple of (joystick, key) you can use to pass to AddKeyBinding.
    import renpy as rpy
    import pygame
    import collections
    import string

    if persistent._user_keymap:
        config.keymap = persistent._user_keymap
    else:
        persistent._user_keymap = config.keymap


    # Event types.
    MOUSE_EVENT_TYPES = { pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP }
    KEYBOARD_EVENT_TYPES = { pygame.KEYDOWN, pygame.KEYUP }
    JOYSTICK_EVENT_TYPES = { rpy.display.core.JOYEVENT }
    INPUT_EVENT_TYPES = MOUSE_EVENT_TYPES | KEYBOARD_EVENT_TYPES | JOYSTICK_EVENT_TYPES
    KEYBOARD_MODIFIERS = collections.OrderedDict([('meta', pygame.KMOD_META), ('ctrl', pygame.KMOD_CTRL), ('alt', pygame.KMOD_ALT), ('shift', pygame.KMOD_SHIFT)])

    # Human-readable keymap descriptions.
    _keymap_descriptions = dict(
        rollback=_('Roll back text'),
        screenshot=_('Take screenshot'),
        toggle_fullscreen=_('Toggle fullscreen'),
        game_menu=_('Menu'),
        hide_windows=_('Hide UI'),
        quit=_('Quit'),
        iconify=_('Minimize'),
        help=_('Help'),

        rollforward=_('Roll forward text'),
        dismiss=_('Proceed'),
        dismiss_hard_pause=_('Force proceed'),

        skip=_('Skip text'),
        toggle_skip=_('Toggle text skipping'),
        fast_skip=_('Fast skip text'),

        save_delete=_('Delete save file'),

        developer=_('Developer menu'),
        launch_editor=_('Launch editor'),
        choose_renderer=_('Renderer choice'),
        reload_game=_('Reload game'),
        inspector=_('Style inspector'),

        focus_up=_('Up'),
        focus_down=_('Down'),
        focus_left=_('Left'),
        focus_right=_('Right')
    )

    # Keymap order. None indicates vertical spacing.
    _keymap_order = [
        'dismiss',
        'rollback',
        'rollforward',
        'skip',
        'toggle_skip',
        'fast_skip',
        None,

        'hide_windows',
        'screenshot',
        'game_menu',
        'help',
        'toggle_fullscreen',
        'iconify',
        'quit',
        None,

        'focus_left',
        'focus_right',
        'focus_up',
        'focus_down'
    ]
    if config.developer:
        _keymap_order.extend([
            None,

            'developer',
            'reload_game',
            'inspector',
            'launch_editor'
        ])

    # Name for keysyms.
    _keysym_key_names = {
        'EXCLAIM': u'!',
        'QUOTE': u"'",
        'QUOTEDBL': u'"',
        'HASH': u'#',
        'DOLLAR': u'$',
        'AMPERSAND': u'&',
        'LEFTPAREN': u'(',
        'RIGHTPAREN': u')',
        'ASTERISK': u'*',
        'PLUS': u'+',
        'COMMA': u',',
        'MINUS': u'-',
        'PERIOD': u'.',
        'SLASH': u'/',
        'COLON': u':',
        'SEMICOLON': u';',
        'LESS': u'<',
        'EQUALS': u'=',
        'GREATER': u'>',
        'QUESTION': u'?',
        'AT': u'@',
        'LEFTBRACKET': u'[',
        'BACKSLASH': u'\\',
        'RIGHTBRACKET': u']',
        'CARET': u'^',
        'UNDERSCORE': u'_',
        'BACKQUOTE': u'`',
        'UP': _('Up'),
        'LEFT': _('Left'),
        'RIGHT': _('Right'),
        'DOWN': _('Down'),
        'NUMLOCK': _('Num lock'),
        'CAPSLOCK': _('Caps lock'),
        'SCROLLOCK': _('Scroll lock'),
        'LSHIFT': u'Shift',
        'RSHIFT': u'Right shift',
        'LCTRL': _('Ctrl'),
        'RCTRL': _('Right ctrl'),
        'LALT': _('Alt'),
        'RALT': _('Right alt'),
        'LMETA': _('Ctrl') if sys.platform != 'darwin' else _('Cmd'),
        'RMETA': _('Right ctrl') if sys.platform != 'darwin' else _('Cmd'),
        'LSUPER': _('Win'),
        'RSUPER': _('Win'),
        'EURO': u'€',
        'RETURN': 'Enter',
        'PAGEUP': 'Page up',
        'PAGEDOWN': 'Page down',
        'ESCAPE': 'Esc',
        'DELETE': 'Del'
    }

    _keysym_mouse_buttons = {
        '1': 'Left click',
        '2': 'Middle click',
        '3': 'Right click',
        '4': 'Scroll up',
        '5': 'Scroll down'
    }

    _keysym_symbols = { val: name for name, val in pygame.__dict__.items() if name.startswith('K_') }


    def _keyname_to_friendly(name):
        keyname = []
        suffix = ''

        # Modifier keys.
        while any(name.lower().startswith(meta + '_') for meta in ('super', 'meta', 'ctrl', 'alt', 'shift')):
            meta, name = name.split('_', 1)
            keyname.append(_keysym_key_names['L' + meta.upper()])

        # Joystick keys.
        if name.startswith('joy_'):
            joyname = renpy.game.preferences.joymap.get(name)
            if not joyname:
                return None
            name = _keyname_joy_to_friendly(joyname)
            if not name:
                return None

            keyname.append(name)
            return keyname

        # Keyboard keys.
        if name.startswith('K_'):
            # K_ENTER, K_ESCAPE...
            name = name[2:]
        if name.startswith('KP'):
            # KP0, KP_DIVIDE...
            name = name[2:].lstrip('_')
            suffix = ' (keypad)'

        if not name:
            return None

        if len(name) == 1:
            # a, A, 0...
            keyname.append(name + suffix)
            return keyname

        if name.startswith('mousedown') or name.startswith('mouseup'):
            _, button = name.split('_', 1)
            keyname.append(_keysym_mouse_buttons.get(button, 'Mouse button #{}'.format(button)))
            return keyname

        if name.startswith('F'):
            # F1, F2...
            keyname.append(name + suffix)
            return keyname

        if name in _keysym_key_names:
            keyname.append(_keysym_key_names[name] + suffix)
            return keyname

        keyname.append(name[0] + name[1:].lower() + suffix)
        return keyname

    def _keyname_joy_to_friendly(name):
        return 'Joystick ' + name

    def _event_to_keyname(event):
        if event.type in MOUSE_EVENT_TYPES:
            if event.type != pygame.MOUSEBUTTONUP:
                return (False, None)
            return (False, 'mouseup_{}'.format(event.button))
        elif event.type in KEYBOARD_EVENT_TYPES:
            if event.type != pygame.KEYDOWN:
                return (False, None)

            base = _keysym_symbols.get(event.key)
            mods = []
            for name, mod in KEYBOARD_MODIFIERS.items():
                if event.mod & mod:
                    mods.append(name)

            if base and mods:
                return (False, '_'.join(mods) + '_' + base)
            elif base:
                return (False, base)
            elif mods:
                return (False, '_'.join(mods))
            else:
                return (False, None)
        elif event.type in JOYSTICK_EVENT_TYPES:
            if not event.press:
                return (False, None)

            return (True, event.press)




    class InputGrabBehaviour(Null):
        def __init__(self, target, excludes=None, exclude_displayables=None, **kwargs):
            super(InputGrabBehaviour, self).__init__(**kwargs)
            self.target = target
            self.excludes = excludes or []
            self.exclude_displayables = exclude_displayables or []

        def event(self, ev, x, y, st):
            # Check event types.
            if ev.type not in INPUT_EVENT_TYPES:
                return

            # Check excluded events.
            for exclude in self.excludes:
                if renpy.map_event(ev, exclude):
                    return

            # Check for a mouse event in excludes displayables.
            if ev.type in MOUSE_EVENT_TYPES:
                evx, evy = ev.pos

                for displayable in self.excludes:
                    x, y, width, height = renpy.get_image_bounds(displayable)
                    # Within bounds?
                    if evx >= x and evy >= y and evx <= x + width and evy <= y + height:
                        return

            # Store event and tell Ren'Py to ignore it.
            joy, keysym = _event_to_keyname(ev)
            if keysym is not None:
                setattr(store, self.target, (joy, keysym))

            renpy.restart_interaction()
            raise renpy.IgnoreEvent()

    class RemoveKeyBinding(object):
        def __init__(self, command, binding):
            self.command = command
            self.binding = binding
            self.joy = binding.startswith('joy_')

        def __call__(self):
            if self.command in config.keymap and self.binding in config.keymap[self.command]:
                config.keymap[self.command].remove(self.binding)
                if self.joy and self.binding in renpy.game.preferences.joymap:
                    del renpy.game.preferences.joymap[self.binding]

                renpy.clear_keymap_cache()
                renpy.restart_interaction()

    class AddKeyBinding(object):
        def __init__(self, command, key, joy):
            self.command = command
            self.key = key
            self.joy = joy

        def __call__(self):
            config.keymap.setdefault(self.command, [])

            # Create a joy_user_X entry.
            if self.joy:
                i = 1
                while True:
                    key = 'joy_user_{}'.format(i)
                    if key not in renpy.game.preferences.joymap:
                        break
                    i += 1

                renpy.game.preferences.joymap[key] = self.key
                config.keymap[self.command].append(key)
            else:
                config.keymap[self.command].append(self.key)

            renpy.clear_keymap_cache()
            renpy.restart_interaction()

