# textlog.rpy
# Maintains a nice little text log. Works through rollback and roll-forward.
# Tested in Ren'Py v6.17.3.
# Copyright (C) 2012-2014 Shiz.
# Released under the terms of the WTFPL; see http://sam.zoy.org/wtfpl/COPYING for details.

# USAGE:
# Place in your game, then call screen text_log to show the text log.
#
# Config variables:
#   - config.text_log_size: 
#     Text log size. -1 for unlimited.
#   - config.text_log_blocked_tags:
#     Do not log the text if it contains one of these tags.
#   - config.text_log_filtered_tags:
#     Tags to filter for the log.

python early:
    import re

    # Create configuration variables.
    locked = config.locked
    config.locked = False
    config.text_log_size = 100
    config.text_log_blocked_tags = [ 'nw' ]
    config.text_log_filtered_tags = [ 'w', 'fast', 'cps', 'p' ]
    config.locked = locked

    # Create styles.
    style.create('text_log', 'frame')
    style.create('text_log_choice', 'text')
    style.create('text_log_who', 'text')
    style.create('text_log_dialogue', 'text')

    # Simple buffer to hold the text log;
    # will automatically delete older logs once the limit has reached.
    class TextLog(renpy.python.NoRollback):
        def __init__(self):
            self.given_size = config.text_log_size
            self.hooks = []
            if self.given_size == -1:
                self.size = 0
                self.data = []
            else:
                self.size = self.given_size
                self.data = [ (None, None, None) for i in xrange(self.size) ]

            self.block_regexp = re.compile('(' + '|'.join(u'\{%s\}|\{%s=.*?\}|\{/%s\}' % (tag, tag, tag) for tag in config.text_log_blocked_tags) + ')')
            self.filter_regexp = re.compile('(' + '|'.join('\{%s\}|\{%s=.*?\}|\{/%s\}' % (tag, tag, tag) for tag in config.text_log_filtered_tags) + ')')

        def add_dialogue(self, who, what):
            if not what or self.block_regexp.search(what):
                return

            if self.given_size != -1:
                self.data.pop(0)
            else:
                self.size += 1
            
            self.data.append(('dialogue', who, self.filter_regexp.sub('', what)))
            for f in self.hooks:
                f('dialogue', who, what)
        
        def add_choice(self, choice):
            if self.block_regexp.search(choice):
                return

            if self.given_size != -1:
                self.data.pop(0)
            else:
                self.size += 1

            self.data.append(('choice', None, self.filter_regexp.sub('', choice)))
            for f in self.hooks:
                f('choice', choice)
        
        def get(self, i):
            return self.data[i]

        def add_hook(self, func):
            self.hooks.append(func)

init -10 python hide:
    def init():
        store.text_log = TextLog()
        renpy.block_rollback()

    config.start_callbacks.append(init)

init -1501 python:
    # Replace character classes with logging ones.
    class LoggingADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            if not renpy.game.context().seen_current(False):
                store.text_log.add_dialogue(who, what)
            super(LoggingADVCharacter, self).do_done(who, what)


    ADVCharacter = LoggingADVCharacter
    # Straight outta Ren'Py.
    adv = ADVCharacter(None, kind=adv)

    # Override the menu handler to store choices.
    def menu(items, *args, **kwargs):
        rv = renpy.display_menu(items, *args, **kwargs)

        if not renpy.game.context().seen_current(False) and (not 'interact' in kwargs.keys() or kwargs['interact']) and rv is not None:
            store.text_log.add_choice(items[rv][0])
        return rv

screen text_log:
    frame:
        style "text_log"

        vbox:
            viewport:
                mousewheel True
                scrollbars "horizontal"

                vbox:
                    for i in range(0, text_log.size):
                        $ (type, who, what) = text_log.get(i)

                        hbox:
                            if type == 'choice':
                                text what style 'text_log_choice'
                            elif type == 'dialogue':
                                if who:
                                    text who style 'text_log_who'
                                    text what style 'text_log_dialogue'
            textbutton "Return":
                action Return()

