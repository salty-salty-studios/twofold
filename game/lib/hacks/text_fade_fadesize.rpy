python early:
    ## Custom support for '{fade}' and '{fadesize}' tags.

    import renpy.text.text as text
    from renpy.text.text import TextSegment, SpaceSegment, DisplayableSegment, PARAGRAPH, TAG, TEXT, DISPLAYABLE
    import renpy.audio.music as music

    def salty_layout_segment(self, tokens, style, renders):
        """
        Breaks the text up into segments. This creates a list of paragraphs,
        which each paragraph being represented as a list of TextSegment, glyph
        list tuples.
        """

        # A map from an integer to the number of the hyperlink this segment 
        # is part of.
        self.hyperlink_targets = { }

        paragraphs = [ ]
        line = [ ]

        ts = TextSegment(None)

        ts.cps = style.slow_cps
        if ts.cps is None or ts.cps is True:
            ts.cps = renpy.game.preferences.text_cps

        ts.take_style(style)

        # The text segement stack.
        tss = [ ts ]

        def push():
            """
            Creates a new text segment, and pushes it onto the text segement
            stack. Returns the new text segment.
            """

            ts = TextSegment(tss[-1])
            tss.append(ts)
            return ts

        is_fading = False
        fade_count = 0
        fade_total = 0
        fade_treshold = 30.0
        fade_start = 255

        is_changing_size = False
        csize_count = 0
        csize_total = 0
        csize_treshold = 72.0
        csize_start = 16.0

        for type, text in tokens: #@ReservedAssignment

            if type == PARAGRAPH:
                # Note that this code is duplicated for the p tag, below.
                if not line:
                    line.append((tss[-1], u" "))

                paragraphs.append(line)
                line = [ ]

                continue

            elif type == TEXT:
                if is_fading or is_changing_size:
                    for ch in list(text):
                        ts = TextSegment(tss[-1])

                        if is_fading:
                            (r, g, b, a) = ts.color
                            a = int(float(fade_total - fade_count) / fade_total * (fade_start - fade_treshold) + fade_treshold)
                            ts.color = (r, g, b, a)
                            fade_count += 1
                        if is_changing_size:
                            ts.size = float(csize_count / csize_total * (csize_treshold - csize_start) + csize_start)
                            csize_count += 1

                        line.append((ts, ch))
                else:
                    line.append((tss[-1], text))
                continue

            elif type == DISPLAYABLE:
                line.append((DisplayableSegment(tss[-1], text, renders), u""))
                continue

            # Otherwise, we have a text tag.
            tag, _, value = text.partition("=")

            if tag and tag[0] == "/" and tag != "/fade" and tag != "/fadesize":
                tss.pop()

                if not tss:
                    raise Exception("%r closes a text tag that isn't open." % text)

            elif tag == "_start":
                ts = push()
                tss.pop(-2)
                self.start_segment = ts

            elif tag == "_end":
                ts = push()
                tss.pop(-2)
                self.end_segment = ts

            elif tag == "p":
                # Duplicated from the newline tag.
                if not line:
                    line.append((tss[-1], u" "))

                paragraphs.append(line)
                line = [ ]

            elif tag == "space":
                width = int(value)
                line.append((SpaceSegment(tss[-1], width=width), u""))

            elif tag == "vspace":
                # Duplicates from the newline tag.
                height = int(value)

                if line:
                    paragraphs.append(line)

                line = [ (SpaceSegment(tss[-1], height=height), u"") ]
                paragraphs.append(line)

                line = [ ]

            elif tag == "w":
                pass

            elif tag == "fast":
                pass

            elif tag == "nw":
                pass

            elif tag == "a":
                self.has_hyperlinks = True

                hyperlink_styler = style.hyperlink_functions[0]

                if hyperlink_styler:
                    hls = hyperlink_styler(value)
                else:
                    hls = style

                old_prefix = hls.prefix

                link = len(self.hyperlink_targets) + 1
                self.hyperlink_targets[link] = value

                if renpy.display.focus.argument == link:
                    hls.set_prefix("hover_")
                else:
                    hls.set_prefix("idle_")

                ts = push()
                ts.take_style(hls)
                ts.hyperlink = link

                hls.set_prefix(old_prefix)

            elif tag == "b":
                push().bold = True

            elif tag == "i":
                push().italic = True

            elif tag == "u":
                push().underline = True

            elif tag == "s":
                push().strikethrough = True

            elif tag == "plain":
                ts = push()
                ts.bold = False
                ts.italic = False
                ts.underline = False
                ts.strikethrough = False

            elif tag == "":
                style = getattr(renpy.store.style, value)
                push().take_style(style)

            elif tag == "font":
                push().font = value

            elif tag == "size":
                if value[0] in "+-":
                    push().size += int(value)
                else:
                        push().size = int(value)

            elif tag == "color":
                push().color = renpy.easy.color(value)

            elif tag == "k":
                push().kerning = float(value)

            elif tag == "rt":
                ts = push()
                ts.take_style(style.ruby_style)
                ts.ruby_top = True
                self.has_ruby = True

            elif tag == "rb":
                push().ruby_bottom = True
                # We only care about ruby if we have a top.

            elif tag == "cps":
                ts = push()

                if value[0] == "*":
                    ts.cps *= float(value[1:])
                else:
                    ts.cps = float(value)

            elif tag == "opacity":
                ts = push()

                (r, g, b, a) = ts.color

                # percentage -> 0..255
                a = float(value) * 2.55
                ts.color = (r, g, b, a)

            elif tag == "fade":
                is_fading = True

                fade_total = 0
                for (type2, text2) in tokens[tokens.index((type, text)):]:
                    if type2 == TAG:
                        tag2, _, _ = text2.partition("=")
                        if tag2 == "/fade":
                            break

                    elif type2 == TEXT:
                        fade_total += len(text2)
                fade_total = float(fade_total)

                if value:
                    if len(value.split(',')) == 2:
                        # percentage -> 0..255
                        (fade_start, fade_treshold) = (float(i) * 2.55 for i in value.split(','))
                    else:
                        # percentage -> 0..255
                        fade_treshold = float(value) * 2.55
                        fade_start = tss[-1].color[3]
                else:
                    fade_treshold = 30.0
            elif tag == "/fade":
                is_fading = False
            elif tag == "fadesize":
                is_changing_size = True

                csize_total = 0
                for (type2, text2) in tokens[tokens.index((type, text)):]:
                    if type2 == TAG:
                        tag2, _, _ = text2.partition("=")
                        if tag2 == "/fadesize":
                            break

                    elif type2 == TEXT:
                        csize_total += len(text2)
                csize_total = float(csize_total)
                csize_count = 0

                if len(value.split(',')) == 2:
                    (csize_start, csize_treshold) = (float(i) for i in value.split(','))
                else:
                    csize_treshold = float(value)
                    csize_start = tss[-1].size
            elif tag == "/fadesize":
                is_changing_size = False
            else:
                raise Exception("Unknown text tag %r" % text)

        if not line:
            line.append((ts, u" "))

        paragraphs.append(line)

        return paragraphs

    text.Layout.segment = salty_layout_segment
