init python:
    ## Function to escape text for safe use in Ren'Py.

    def renpy_quote(text):
        return text.replace('[', '[[').replace('{', '{{')
