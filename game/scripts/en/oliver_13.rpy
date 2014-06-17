label scene_1S13_en:
#######################
    # Act 1, Scene 13
    # Running in Circles
    scene bg apartment livingroom with dissolve
    window show dissolve
    play ambiance "sfx/ambiance/silence.ogg"

    "When I get back, Izaac is gone. There's a note on the table."
    window hide dissolve
    show note izaac jog with easeinbottom
    $ renpy.pause()
    window show dissolve
    "Well, at least I'll get some peace and quiet."
    hide note with easeoutbottom
    "I'm pretty hungry. I should check the fridge and see what's left."
    scene bg apartment kitchen with dissolve
    "...Looks like Izaac has already filled the fridge with stuff. It's all portioned and cut up meats, though. Hardly a fruit or vegetable to be seen, or even something that's prepared already."
    "I really don't feel like cooking anything, but it doesn't look like there's any easy food I can cook. I'm feeling sort of lazy, so I don't want to make anything complex."
    "I know for a fact I can't afford to order delivery. The look I get when I don't tip is embarrassing enough to prevent me, even if I did have enough just for the food."
    "My sigh echoes in the empty apartment. I guess I'll make something on my own. One of these packages are filled with fairly thick steaks, so I could probably make a decent London broil."
    "I'll make some for Izaac too, considering I am using his food to make dinner. Plus, I can consider this practice for work. I want to move up from prep chef sometime, but I won't be able to if I can't man a grill or a stove."
    "Smoke flavoring is in the cabinet where it always is, which is good. I don't have a proper grill to get the charcoal flavor, so I'll need that. But where the hell did I leave my marinating container?"
    window hide smoothDissolve

    scene bg apartment livingroom with dissolve
    window show smoothDissolve
    "Izaac nearly busts{nw}"
    play music "music/capitals.ogg" fadein 1.5
    play sound "sfx/door_close2.ogg"
    stop ambiance fadeout 0.5
    $ renpy.transition(hpunch, layer='master')
    extend " the door down, {nw}"
    show izaac headscratch enthusiastic at mirror:
        xanchor 0.5
        xpos 0.25
        yoffset -175
    $ renpy.transition(dissolve, layer='master')
    extend "jogging in place and looking like an adrenaline-junkie who just got his fix."
    izaac "Woo! That was a good run!"

    show izaac shrug smirk eyesclosed
    $ renpy.transition(dissolve, layer='master')
    izaac "Whoa, what smells so damn good?"
    "I turn my focus back to my textbook so I can continue studying."
    oliver "I made steak."

    show izaac grin
    $ renpy.transition(dissolve, layer='master')
    izaac "Hell yeah!"
    hide izaac with dissolve

    oliver "Just don't mix the serving spoons for the sides, alright? My last roommate did that and it pissed me off to no end. You know how certain side dishes don't mix with one another?"
    izaac "Yeah, yeah, totally."
    "He's clearly not listening, instead managing to talk through a mouthful of hot food."
    izaac "Man, this is pretty freakin' good."
    izaac "I send my compliments to the chef!"
    "I'll make sure he gets them. Normally most people don't even bother saying anything about my cooking, but he won't shut up about it. I'm not sure if I like or dislike this."
    "I already ate, so I should just focus on studying."
    stop music fadeout 2.0
    window hide smoothDissolve

    play ambiance "sfx/ambiance/nightfall.ogg"
    scene black with dissolve

    scene bg apartment bedroom night with longDissolve
    window show smoothDissolve
    "I think this is enough studying. I've read almost a chapter ahead in all my courses, so I should be fine for upcoming assignments. I think I'll play some video games until I have to go to sleep. I think I've earned it."

    stop ambiance fadeout 1.5
return
