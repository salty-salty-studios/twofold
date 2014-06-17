label scene_1S10_en:
    # Act 1, Scene 10
    # Not Quite What you Were Expecting
    # Bumps into Tanya for the first time
    scene bg hallway 1 with longDissolve
    play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 1.5
    window show smoothDissolve

    "My high spirits have been consistently brought down over the last few days, now that I think about it. Even after spending my hour between classes on one of the library's computers to play games, I still feel pretty crappy."
    "I actually took a little time to look up who the author of that compilation was. Apparently, he's some old dead Russian poet. That alone speaks more than what I could probably say about it."
    "Man. Everything was looking up after that meeting with Lawe. A chance to save my enrollment! How could that be a bad thing?"
    "It seems that ever wandering out of my comfort zone is a bad thing. The minute I did, I started experiencing all kinds of absurd stuff."
    "These artists for one."
    "I remember taking art classes in high school and no one really acting like the people I've met."
    "I groan to myself."
    "I wish I hadn't enrolled in a community college."
    "Maybe the additional loans would've been worth my sanity."
    "I find myself arguing in my head about whether I'd have the GPA to get into a majority of state colleges, nevermind some of the more elite private ones."
    "Ultimately, I can't honestly tell myself I'd be able to get into anywhere else. My grades have always been average at best."
    "I open my mouth to sigh, but instead a grunt escapes my throat. Thanks to not paying attention to my surroundings, {nw}"
    $ renpy.transition(hpunch, layer='master')
    scene black
    stop ambiance fadeout 0.5
    play sound "sfx/body_collision.ogg"
    extend "I walk into something heavy and hard, causing me to reel back."
    "While trying to steady myself, I trip over my own feet and{nw}"
    play sound "sfx/body_fall.ogg"
    extend " land on my rear."
    "Great, what now?"
    "Looking at what I bumped into, I freeze in place."

    play music "music/fauxhorror.ogg" fadein 3.5
    scene cg tanya intro with longDissolve:
        yalign 1.0
        xalign 0.5
        easein 10 yalign 0.0
    "Oh crap."
    "Oh crap, oh crap."
    "Did I just step into some kind of horror movie? Is this person going to kill me with an acetylene torch?"
    "I start scurrying backwards, scrambling to back away from whoever this metal-masked murderer is without even getting up."
    "The masked figure drops their bag with a resounding thud. {nw}"
    play sound "sfx/sack_drop.ogg"
    $ renpy.transition(hpunch, layer='master')
    extend "The minute the bag hits the ground, so does my stomach."
    "What the hell is going on?"
    "They raise their hand towards me and I close my eyes out of instinct."
    scene black with eyes
    tanyauu "Hey, you okay?"

    stop music fadeout 0.75
    "...Huh?"
    scene bg hallway 1:
        yalign 0.4
    show tanya suit hmm:
        xanchor 0.5
        xpos 0.5
        yanchor 0.5
        ypos 0.38
    with eyesr
    "The figure lifts their welding mask to reveal a female's face."
    "Actually, on second look..."
    "Looking at her from a sitting position instead of leaned back,"
    "...She's not very tall at all."
    "Actually, I think I have a full head on her."
    tanyau "Need a hand up, kid?"
    "No, actually, I think I'm going to lay down for a bit."
    show bg hallway 1:
        yalign 0.4
        easein 2.5 yalign 0.7
    show tanya suit hmm:
        subpixel True
        easein 2.5 ypos 0.35
    scene black with eyes
    "Yeah, I think I'll stay down here for a while. Maybe in a little while, a class will start and everyone will ignore me so I can be trampled to death."
    tanyau "Mrmm."
    "I hear the plodding of boots and then something hard prodding me in the side."
    play sound "sfx/body_prod.ogg"
    tanyau "Am I gonna hafta call somebody? Like a doctor or somethin'?"
    "A heavy sigh, which I echo internally."

    play music "music/aroundcampus.ogg" fadein 2.0
    oliver "Nope, I just don't feel like getting up. I keep getting knocked down so I think I'm just going to stay down here."
    tanyau "...That s'posed to be a metaphor?"
    oliver "Yes."
    oliver "We'll call it that for now."
    tanyau "Well, what's got you down?"
    "Aside from Izaac, I don't really have anyone to actually talk to about things that are bothering me. And honestly, I leave out a lot of how it makes me feel when I talk to him."
    "I get the feeling like he'd just make fun of me. This person? I guess I could say they're concerned. At the least, they're uninvolved, so they know none of the people I have gripes with."
    oliver "Well, I'm nearly flunking out, I have to pick one of two dumb artsy-fartsy classes to stay enrolled,"
    oliver "Some chick wearing a top hat spent an entire class insulting me, then some of the people from her club nearly attacked me because one of their friends is a crybaby,"
    oliver "And then some snobby blonde chick blew me off at a coffeehouse after I bought her a drink."
    oliver "Now I'm laying on the ground because I walked into a small girl who I thought was a masked murderer and nearly had a heart attack because of it."
    oliver "I just feel like staying down here for awhile."
    tanyau "Snrk."
    "...Is she laughing at me?"
    tanyau "C'mon, get up."

    scene bg hallway 1:
        yalign 1.0
    show tanya suit grin: 
        xalign 0.5
        yanchor 0.5
        ypos 0.4
        xzoom 0.94
        yzoom 0.94
        subpixel True
        ease 0.8 ypos 0.6 xzoom 1.05 yzoom 1.05
        linear 0.2 ypos 0.5 xzoom 1.0 yzoom 1.0
    show bg hallway 1:
        yalign 0.7
        time 0.8
        linear 0.2 yalign 0.5
    with eyesr
    "The little girl grabs hold of my arm and yanks me to my feet, faster than I anticipated. What the hell?"
    tanyau "There ya go."
    "She pats off my vest with her huge gloves and slaps me on the back{nw}"
    $ renpy.transition(vpunch, layer='master')
    extend "."
    show tanya suit smile
    $ renpy.transition(dissolve, layer='master')
    tanyau "There, good as new."
    oliver "Uh huh."
    show tanya suit smirk
    $ renpy.transition(dissolve, layer='master')
    tanyau "Dont'cha have a class to go to?"
    "I nod slowly, regarding her with confusion."
    tanyau "Want me to walk ya to class?"
    "Her half-grin tells me she's pretty much mocking me at this point."
    tanyau "Can't have you walkin' into everything. I'll be your second pair of eyes."
    oliver "Why?"
    show tanya suit pout away
    $ renpy.transition(dissolve, layer='master')
    tanyau "No reason. Even if I had a reason, it wouldn't matter."
    "She picks up her industrial sized bag, which is probably filled with tools, based on how heavily it hit the ground.{nw}"
    hide tanya
    $ renpy.transition(dissolve, layer='master')
    extend " She positions herself behind me{nw}"
    scene bg hallway 1:
        xalign 0.5
        yalign 0.5
        subpixel True
        ease 2.5 xzoom 1.1 yzoom 1.1 ypos 0.55
    extend " and I feel hands on my back propelling me forward."
    oliver "Okay, okay, I can walk on my own."
    "Why is everyone in this school so intolerable?"

    show tanya suit smirk:
        yoffset -90
        xalign 0.5
    $ renpy.transition(dissolve, layer='master')
    tanyau "What class are you goin' to?"
    oliver "...Some writing class."
    show tanya suit pumped
    $ renpy.transition(dissolve, layer='master')
    "I hear low laughter from the little welder. I'm... not sure whether I should be worried or not."
    tanyau "So, the art club, huh? Givin' you trouble?"
    "I nod in a slow manner."
    show tanya suit smirk
    $ renpy.transition(dissolve, layer='master')
    tanyau "They're not too bad, I think."
    "I glance sideways at her."
    oliver "You're not part of their little cult, are you?"
    "The girl chuckles in a low tone. For a small person, her voice is kinda... deep."
    show tanya suit pout away
    $ renpy.transition(dissolve, layer='master')
    tanyau "Nope. I don't think I'd be able to draw well with these."
    "She lifts her hands, showing off the massive gloves. Well, yeah, but you'd... take them off. To do the drawing. Oh, whatever."
    "I don't really feel like talking, but thankfully she doesn't seem too keen on keeping a conversation up herself."
    "I double-check my schedule to make sure this is the right class."
    "Yep."
    "Room 134 in the art building."
    "Come to think of it,  why is there a welder in the arts building?"
    "Maybe there's a metalcraft as art sort of thing for a class."
    hide tanya
    $ renpy.transition(dissolve, layer='master')
    "When I go to ask her, she's gone."
    stop music fadeout 1.5
    oliver "What the-?"
    "Whatever. According to my watch, I'm at least fifteen minutes early to class. That's good, I shouldn't have to deal with the whole issue I did with the art class."
    "No judgmental artists or snobs to look down on me."

    window hide smoothDissolve
    stop music fadeout 2.5
    scene black with dissolve
return
