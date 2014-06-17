label scene_1S16_en:
#######################
    #  Scene 16
    #  Pick Your Battles
    call switch_scene('bg apartment livingroom', 'bg hallway 3')

    $ renpy.music.set_volume(0.5, channel='ambiance')
    play ambiance "sfx/ambiance/crowd_cafetaria.ogg" fadein 2.0
    "Friday. My least favorite day of the week. My schedule is set up so that I have as many free hours as possible during the weekend. This way, I can work as many hours as my boss wants me to. By that, I mean as many as he can make me work without outright killing me."
    "Today, I have only a few morning classes. Then, straight to the gulag with me."
    "By gulag, I mean kitchen."
    "First is my statistics class, then my second round of history for the week."
    "I'm not sure whether I should be annoyed that I'm finding the courses I chose for my major to be more stifling and boring than the ones I have to take to stay enrolled."
    "They're a source of anxiety and stress, but the classes are kind of refreshing. They're daunting and terrifying... but they're also sort of interesting."
    "I mean, ultimately, you're creating something. Either with words or lines and colors and metaphors – but there's a world or a story or a person you're making."
    "I can't say I've ever had any control in any aspect of my life. Not once."
    "I don't want to make myself vulnerable to a new group of people... but they seem harmless enough. I guess I can count the positive things in this, like Izaac said."
    "Whatever argument Mekki and Caprice are having, it's making both crews willing to tolerate and help me."
    "I can't say that under any other circumstance, I could be hopeful for help, being the sort of person I am."
    "Oh, there's that weird feeling again."
    "Hope."
    "Looking up, {nw}"
    show hayley right away headphones:
        xanchor 0.5
        xpos 0.2
        yoffset -175
        alpha 0.0

        parallel:
            ease 5.0 xpos 0.8
        parallel:
            ease 0.5 alpha 1.0
            time 4.0
            ease 1.0 alpha 0.0
    $ renpy.transition(dissolve, layer='master')
    extend "I see someone walking on the opposite side of the hall."
    
    "I find myself slowing to a stop after she passes by."
    hide hayley with dissolve
    "I don't know, but there's something about her I find attractive. It might've been the distant look on her face, but that confidence she walked with. Like she was focused on something. She wasn't dressed up all fancy, or too sloppy, either."
    "If I didn't know better, I'd say she's probably my ideal girl. Maybe I should go and ask for her name? Get to know her."
    "...No, I probably shouldn't. Nevermind my horrible confidence with women, my last experience with \"going after a girl\" left a bad taste in my mouth. Maybe I should just cool my jets."
    "I'm sure everyone's already after her, anyways. I'd probably have competition way out of my league."
    "Pick your battles, Oliver."
    "I don't want to be late for class. I need to focus on more important things than how lonely I am."

    stop ambiance fadeout 1.5
    $ renpy.pause(1.5, hard=True)
    $ renpy.music.set_volume(1.0, channel='ambiance')
return
