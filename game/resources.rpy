# resources.rpy
# Contains all resources: sprites, backgrounds, characters...

# Characters.
init python:
    adv = Character(None, ctc=At(Image("ui/textbar/arrow.png", xpos=1050, ypos=680), fadein(1.0)), ctc_position="fixed")
    narrator = Character(None, what_style='say_thought')

# Dynamically load sprites and backgrounds.
init python:
    define_images('sprites')
    define_images('bgs', [ 'bg' ], xalign=0.5, yalign=0.5)
    define_images('cgs', [ 'cg' ], xalign=0.5, yalign=0.5)
    define_images('vfx', [ 'misc' ])
    define_images('vfx/title', [ 'title' ])
    define_images('vfx/notes', [ 'note' ])
    define_images('vfx/drawings', [ 'drawing' ])

init:
    # Images and effects.
    image logo = "ui/main/logo.png"
    image white = Solid("#ffffff")
    image creme = Solid("#fffbf4")
    image phoneop = Text('{b}{font=ui/Bender.otf}{size=16}{color=#635e5d}Pepr US{/color}{/size}{/b}')
    image callmom = Text('{font=ui/Bender.otf}{b}{color=#8f8671}Calling...{/color}{/b}\n     {color=#000000}Mom{/color}')
    image callingmom = Text('{font=ui/Bender.otf}{color=#8f8671}{size=17} Talking to:{/size}{/color}\n{b}  {color=#000000}Mom{/color}{/b}')
    image contactlistearly =  Text('{font=ui/Bender.otf}{color=#635e5d} {b}Contact list{/b}{vspace=15}{/color}{color=#000000}» Mom{/color}')
