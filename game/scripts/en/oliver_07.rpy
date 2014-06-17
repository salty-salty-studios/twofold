label scene_1S7_en:
######################
    # Act 1, Scene 7
    # Walls and Towers
    # Eileen defends her waifu, Wallace whaps Oliver in the back of the head for being dumb.
    scene bg hallway 3 with dissolve
    play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 1.5
    window show dissolve

    "Two lecture classes about business, done and over with. These classes are closer to life-draining beasts of myth than educational. I feel like I'm dead on my feet."
    "I could go back to the cafeteria, maybe grab an energy drink or two."
    "Then again, the idea of returning to the cafeteria isn't one I'm fond of, considering how I walked into that girl. What if she's still there, or with some of her friends?"
    "Explaining that awkward accident to them isn't something I want to do."
    "I could hit a convenience store or something on the way out, they might cheaper there than at the cafeteria."
    "My mind wanders to my bank account. I'm not doing exceptionally well on the money front. I hashed out the whole rent thing with Izaac, including when we should have our halves put together and who will give it to the landlord."
    "Now I'll have an extra few hundred dollars per month to use."
    "For now, though? I'm pretty sure I have something like thirty dollars in my checking account."
    "I guess I can spare some cash for a couple energy drinks until next paycheck. I'll need at least one for later while doing my Business Functions and Practices homework."
    "Just thinking about the name makes me sleepy."
    "I'll settle for buying from the cafeteria, I don't want to deal with going out of my way for a convenience store."
    "In and out this time, though. No chatting with Wallace or wandering around. I don't need any more college experiences."
    stop ambiance fadeout 1.5

    scene bg campus reverse with dissolve:
        xalign 0.5
        yalign 0.5
    play ambiance "sfx/ambiance/outside.ogg" fadein 0.5
    "So far, so good. No collisions, no awkward introductions. I haven't run into Caprice, either. I can call this a fairly safe venture so far."
    
    scene cg eileen intro with dissolve
    play music "music/takingnotes.ogg" fadein 1.5
    "However, when I arrive, I see Wallace and an unfamiliar girl in front of union building."
    "Judging by the fact that a smaller girl is somehow managing to intimidate Wallace,\nI think it'd be better to turn around and find an alternate way to my next class."
    
    scene bg campus reverse with dissolve:
        xalign 0.5
        yalign 0.5
    eileenu "Is that him?"
    # Sprites are hidden because Oliver isn't looking at them.
    wallace "Er, no. That isn't. That guy definitely didn't knock Allison over."
    "The last half of his sentence seems staged. I'm pretty sure he's giving me a hint and telling me to run away. Which I fully intend to do right now."
    eileenu "That looks like who you and Allison were talking about."
    show bg campus reverse:
        subpixel True
        ease 2.0 xzoom 1.5 yzoom 1.5 yalign 0.2
    "Yep, time for a brisk walking pace short of a sprint.{w=0.4}{nw}"
    eileenu "HEY!"
    "A hand grabs hold of my shoulder and spins me around."

    scene bg union outside:
        xalign 0.5
        yalign 0.5
    show eileen angry:
        xanchor 0.5
        xpos 0.4
    show wallace worried:
        xanchor 0.5
        xpos 0.8
        yoffset -175
    with dissolve
    "I'm immediately greeted by a tired, but expressively angry face."
    oliver "Wh... What?"
    "I practically shout back at her, just out of sheer nervousness."
    eileenu "Did you knock a girl over today? Sunglasses on her head?"
    oliver "Er, I {fade}don-"
    eileenu "Sweatshirt, white dress? Did you?!"
    "What the hell, why is she freaking out over this?"
    oliver "It was an accident, I didn't mean to."
    show eileen browup
    $ renpy.transition(dissolve, layer='master')
    eileenu "So you did push her?"
    oliver "No, I didn't–I bumped into her. It was an accident."
    show eileen eyesnarrow
    $ renpy.transition(dissolve, layer='master')
    eileenu "Listen. I didn't ask if it was an accident. Did you knock her over?"
    oliver "No!"
    show eileen frown
    $ renpy.transition(dissolve, layer='master')
    eileenu "So she just came to me upset as hell, with her art project in pieces because she tripped over a loser?"
    "I glance at Wallace. Art? More of you people?"
    "He gives an inaudible sigh and lifts his hands in exasperation."
    eileenu "You know, she spent a lot{nw}"
    $ renpy.transition(vpunch, layer='master')
    extend " of time on the things you broke. Do you even know what they were?"

    oliver "Uh..."
    show eileen angry
    $ renpy.transition(dissolve, layer='master')
    eileenu "I swear–"
    oliver "One looked like a tree! I think."
    "Oh crap, now she looks pissed. What's the big deal? They're just pieces of freakin' clay."

    show wallace frown away
    $ renpy.transition(dissolve, layer='master')
    wallace "Eileen, calm down. Do you honestly expect some random person to know that?"
    "She responds with a snarl.{nw}"
    show wallace neutral
    $ renpy.transition(dissolve, layer='master')
    extend " I don't think that's exactly the kind of response he was looking for, but he lets it go."

    oliver "I don't know what you want me to say, and I really think this is starting to get out of hand. It was an honest accident. Neither of us were looking where we were going."
    oliver "Could you either tell me what you want, or leave me alone?"
    show wallace facepalm facepalm
    $ renpy.transition(dissolve, layer='master')
    "Wallace places his face in his hands. What now? Screw you too, I didn't do anything wrong."

    show eileen neutral
    $ renpy.transition(dissolve, layer='master')
    eileen "Do you have anything valuable on you?"
    "Uh... what?"
    eileen "How about I {nw}"
    show eileen frown
    $ renpy.transition(dissolve, layer='master')
    extend "\"bump\" into you and smash something that you think is important, so you know how it feels?"
    eileen "How would you like that?"
    oliver "...Not at all? And I don't have anything valuable on me. Even my phone's a piece of junk."

    show eileen angry
    $ renpy.transition(dissolve, layer='master')
    eileen "Well, how about your face? Are you partial to your face? I could smash that{nw}"
    $ renpy.transition(vpunch, layer='master')
    extend " up a bit for you."

    show bg union outside:
        xalign 0.5
        yalign 0.5
        subpixel True
        ease 1.0 xzoom 0.91 yzoom 0.91
    show eileen angry:
        xanchor 0.5
        xpos 0.4
        subpixel True
        ease 1.0 xzoom 0.9 yzoom 0.9
    show wallace facepalm facepalm:
        xanchor 0.5
        xpos 0.8
        subpixel True
        ease 1.0 xzoom 0.9 yzoom 0.9 xpos 0.75
    "I take a step back. Yes, I am fairly partial to my face. Even if that threat isn't serious, I probably shouldn't push my luck."
    show wallace neutral
    $ renpy.transition(dissolve, layer='master')
    wallace "Alright, now things are starting to get out of hand. C'mon Eileen, we're going back to the clubroom."
    eileen "No, I'm not done yet, not until he at least gets a taste of his own medicine."
    "She clenches her fists, moving towards me with an expression I find sort of terrifying."

    show wallace frown
    $ renpy.transition(dissolve, layer='master')
    wallace "Alright, enough of being a bunch of fuckin' children."

    show wallace frown behind eileen:
        ease 2.0 xpos 0.5
        ease 6.5 xpos 0.8
    show eileen angry:
        time 2.0
        "eileen handonhip angry"
        ease 6.5 xpos 0.7
    "Just like that, Wallace puts both his hands on her shoulders and starts to lead her away from me."
    "Eileen's face reflects how she feels about being dragged away so easily by a much larger male.{nw}"
    $ renpy.transition(hpunch, layer='master')
    show wallace frown behind eileen:
        pass
    show eileen angry:
        pass
    extend " It earns Wallace a fierce elbow to the chest,{nw}"
    show eileen angry:
        linear 0.5 xpos 0.65
    extend " which causes him to let go."
    "She doesn't charge me or anything, which I was half-expecting."

    show eileen eyesnarrow
    $ renpy.transition(dissolve, layer='master')
    eileen "Watch where you're going in the future, got it?"
    stop music fadeout 5.0
    "She throws me a nasty glare before {nw}"
    hide eileen
    $ renpy.transition(dissolve, layer='master')
    extend "stomping off. I guess Wallace intervening was enough to make her decide this conflict wasn't worth the effort anymore."

    "Wallace stands there for a moment, rubbing his chest. {nw}"
    show wallace frown:
        xanchor 0.5
        xpos 0.75
        ease 1.25 xzoom 1.0 yzoom 1.0 xpos 0.65
    $ renpy.transition(dissolve, layer='master')
    extend "Then, he walks over and {nw}"
    play sound "sfx/slap.ogg"
    $ renpy.transition(hpunch, layer='master')
    extend "slaps me in the back of the head."
    oliver "What the hell did I do now?"
    wallace "You argued with her. That never solves anything."
    oliver "Great. What was her deal, anyways? It was an accident, I don't know how else to say that."
    wallace "Well, the person you knocked over is pretty much her best friend. If you didn't notice, she's extremely protective of her."
    "Yeah, I could tell."
    show wallace neutral
    $ renpy.transition(dissolve, layer='master')
    wallace "Considering that she has a bit of a natural mean streak to her, it doesn't help that you upset her best friend by breaking her project. Which was a gift for Eileen."
    "I grumble to myself."
    oliver "Well, how am I supposed to know that? Doesn't mean it's okay to attack me over it."
    oliver "Is she always that... aggressive of a person?"
    "The word I was reaching for was actually \"asshole\", but I don't know if they're good friends. I don't think I want to piss off the guy who just helped me out." 

    show wallace frown
    $ renpy.transition(dissolve, layer='master')
    wallace "Sometimes, but not usually that bad."
    oliver "Well, maybe you should do something about that."
    wallace "I don't think she'd listen even if I did."
    "Well, here we are, nothing to do but glare at each other."
    "I can't see this going anywhere productive, {nw}"
    scene bg campus reverse:
        xalign 0.5
        yalign 0.5
    $ renpy.transition(dissolve, layer='master')
    extend "so I figure it's time to take off."

    "Wallace calls after me while I head up the stairs to the union building."
    wallace "Still thinking about joining the art club? Eileen and Allison are both in it."
    oliver "Oh, the concept is more appealing than ever."
    
    stop ambiance fadeout 2.5
return
