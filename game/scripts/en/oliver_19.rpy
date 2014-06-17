label _scene_1S19_lookleft:
    show bg hallway 3:
        xalign 0.0
    show eileen:
        xpos 0.83
        xanchor 0.5
    show caprice:
        xanchor 0.5
        xpos 0.7
        yoffset -160
    show allison:
        xpos 0.97
        xanchor 0.5
    show darren at mirror:
        xpos 0.3
        xanchor 0.5
        yoffset -175
    show mekki:
        xpos 0.4
        xanchor 0.5
    show heather at mirror:
        xpos 0.15
        xanchor 0.5
    $ renpy.transition(ease)
    return

label _scene_1S19_lookright:
    show bg hallway 3:
        xalign 1.0
    show caprice:
        xanchor 0.5
        xpos 0.60
        yoffset -160
    show eileen behind caprice:
        xpos 0.7
        xanchor 0.5
    show allison:
        xpos 0.85
        xanchor 0.5
    show mekki:
        xpos 0.30
        xanchor 0.5
    show darren at mirror behind mekki:
        xpos 0.17
        xanchor 0.5
        yoffset -175
    show heather at mirror:
        xpos 0.03
        xanchor 0.5
    $ renpy.transition(ease)
    return

label _scene_1S19_lookcenter:
    show bg hallway 3:
        xalign 0.5
    show caprice:
        xanchor 0.5
        xpos 0.65
        yoffset -160
    show eileen behind caprice:
        xpos 0.8
        xanchor 0.5
    show allison:
        xpos 0.92
        xanchor 0.5
    show mekki:
        xpos 0.35
        xanchor 0.5
    show darren at mirror behind mekki:
        xpos 0.20
        xanchor 0.5
        yoffset -175
    show heather at mirror:
        xpos 0.08
        xanchor 0.5
    $ renpy.transition(ease)
    return

label scene_1S19_en:
    #  Keep screen black from last scene
    call switch_scene_x('bg apartment outside', 'bg hallway 3', { 'xalign': 0.5 })
    play ambiance "sfx/ambiance/crowd_silent.mp3" fadein 1.5

    "Today was supposed to be a good day. Work was easy surprisingly easy yesterday. Not only that, but one of my classes were canceled by the professor. Now, all I have to do is escape my college without running into any questionable characters."
    "I don't think that's going to happen right now, though."

    "While leaving my now only-class-of-the-day, I can hear a familiar and headache-inducing voice from down the hallway. Squinting, I can tell it's Caprice. As if the voice wasn’t enough of a giveaway."
    "Well, alright. She probably can't see me. I'll just turn around and leave before she and her cronies get a hold of me and drag me to their dumb art thing."
    "That's when I see Mekki turn the corner I was planning to escape through, her lackeys in tow."
    "Crap, crap, crap."
    "I'm sandwiched between two groups I'd really prefer not to see today."
    "What can I do about this?"
    "Maybe I can just sneak by one of the two groups and that'll be the end of it."
    "No, odds are one of the two club leaders will stop me and then the other will end up trying to drag me away from them. Or get into a fight over me."
    "As much as girls getting into fights over me would be something of a fantasy for me, in this case it's not really because they're romantically interested."

    show bg hallway 3:
        ease 2.5 xalign 0.3
    show caprice hattip angry:
        xanchor 0.5
        xpos 1.1
        yoffset -160
        ease 4.0 xpos 0.65
    show eileen angry behind caprice:
        xpos 1.1
        xanchor 0.5
        ease 2.5 xpos 0.83
    show allison handsfolded troubled:
        xpos 1.1
        xanchor 0.5
        ease 1.5 xpos 0.97
    "Before I know it, my walking and thinking has led me to being stuck in the middle of the hallway.{nw}"
    show bg hallway 3:
        ease 4.0 xalign 0.8
    show mekki left frown:
        xpos -0.1
        xanchor 0.5
        ease 4.0 xpos 0.4
    show darren neutral at mirror behind mekki:
        xpos -0.1
        xanchor 0.5
        yoffset -175
        ease 2.5 xpos 0.3
    show heather frown at mirror:
        xpos -0.1
        xanchor 0.5
        ease 1.5 xpos 0.15
    extend " I'm boxed in, both groups barring my path on either side."
    call _scene_1S19_lookcenter
    play music "music/takingnotes.ogg" fadein 1.5
    call _scene_1S19_lookright
    caprice "Oh, looky here! It's Miss \"I'm Always Right!\""

    show mekki left pensive frustrated
    $ renpy.transition(dissolve, layer='master')
    "Mekki doesn't even respond, she just rolls her eyes."
    call _scene_1S19_lookleft
    mekki "Why don't you just turn around and go back the way you came shouting?"
    show caprice shouting angry
    call _scene_1S19_lookright
    caprice "How about you turn around and go back the way you came... being all prissy and stuff!"
    call _scene_1S19_lookleft
    mekki "Oh, how eloquent. I'm sure it took a lot of effort to come up with that. We'll even do you a favor and move so you can leave."
    show caprice hattip attacked
    call _scene_1S19_lookright
    caprice "And leave you with the new recruit? I don't think so!"
    oliver "Can I be left out of this?"
    caprice "Nope! If I leave you here with her, she'll probably try and drag you into some... some crazy worded document where you sign yourself writing club slavery!"
    oliver "I just would like to go home."
    show mekki left handstogether frown
    call _scene_1S19_lookleft
    mekki "Please, I don't have to force Oliver to choose a club, unlike you. He can make the obvious choice on his own."
    show caprice hattip angry
    call _scene_1S19_lookright
    caprice "Maybe if he liked boring girls who are uninteresting and use words he won't understand."
    oliver "I think I can understand what she says. I graduated high school."
    show caprice shouting angry
    $ renpy.transition(dissolve, layer='master')
    caprice "Hey! What's that supposed to mean?"
    oliver "It's not supposed to mean anyth-{w=0.3}"
    show mekki left pensive pfah
    call _scene_1S19_lookleft
    mekki "I think he's calling you crass and unintelligent."
    oliver "That's not what I said!"
    show caprice hattip angry
    call _scene_1S19_lookright
    caprice "Oh, ignore her. Of course that's not what you said. Mekki just thinks because she owns a thesaurus that she knows everything, including what's going on in other people's heads."
    caprice "Truth is, she couldn't empathize her way out of a paper bag, for how \"smart\" she acts."
    show mekki left pensive frustrated
    $ renpy.transition(dissolve, layer='master')
    "I think she hit a nerve with that one."
    call _scene_1S19_lookleft
    mekki "I'd rather be incorrect about something trivial than betray my best friend."
    show caprice hattip attacked
    call _scene_1S19_lookright
    caprice "Have you ever thought you're getting mad about super-duper trivial stuff?"
    show mekki left thinking frown
    call _scene_1S19_lookleft
    mekki "Maybe if you understood people better, you wouldn't think it's so trivial."

    call _scene_1S19_lookcenter
    "I really feel like there's something going on I don't understand. Actually, no, there definitely is."
    oliver "Uh, {fade}can I go now?"
    show caprice shouting angry
    doublespeak caprice mekki "{b}NO!{/b}"

    call _scene_1S19_lookleft
    show mekki behind darren
    darren "Why don't you just give it a break, Caprice? I mean, honestly – why don't you just apologize for whatever you did and just let things go back to the way they were?"
    show caprice hattip attacked
    call _scene_1S19_lookright
    show mekki behind darren
    caprice "I did nothing wrong!"
    show mekki left thinking pfah
    show caprice hattip angry
    $ renpy.transition(dissolve, layer='master')
    "Mekki's scoff earns her a nasty glare from the top-hat wearing girl."
    call _scene_1S19_lookleft
    show mekki left thinking frown behind darren
    darren "When was the last time Mekki ever held onto a grudge? To my knowledge, never. If she's unwilling to apologize for something or hasn't, I doubt the fault is majorly on her side."
    call _scene_1S19_lookright
    show mekki behind darren
    show caprice behind eileen
    show eileen handonhip angry
    eileen "Why don't you can it, prettyboy?"
    call _scene_1S19_lookleft
    show mekki behind darren
    show caprice behind eileen
    show darren smile eyesclosed
    darren "Or what, are you going to hit me?"
    show eileen handonhip browup
    call _scene_1S19_lookright
    show mekki behind darren
    show caprice behind eileen
    eileen "I could, if you're into that sort of thing."
    call _scene_1S19_lookleft
    show mekki behind darren
    show caprice behind eileen
    show darren cocksure
    darren "Whoa, whoa, calm down. Try not to flirt so openly with me, Allison might get upset."
    "Holy crap, that smug-as-hell look on his face makes {i}me{/i} want to punch him."

    call _scene_1S19_lookright
    show allison holdarm troubled
    show mekki behind darren
    show caprice behind eileen
    allison "She's not flirting with you and why would I get upset?"
    call _scene_1S19_lookleft
    show mekki behind darren
    show caprice behind eileen
    show heather handoncheek smirk
    heather "Well, you're getting flustered already. Sort of speaks volumes about your... friendship with Eileen."
    call _scene_1S19_lookright
    show mekki behind darren
    show caprice behind eileen
    show allison skirtgrab troubled
    allison "Wh-What's that supposed to mean?"
    "Oh god, what {i}is{/i} that supposed to mean?"
    show eileen handonhip eyesnarrow
    $ renpy.transition(dissolve, layer='master')
    eileen "Yeah, do tell, freckles."
    call _scene_1S19_lookleft
    show mekki behind darren
    show caprice behind eileen
    heather "Well, it clearly means that she'd be upset if she had her best friend taken away by a potential suitor, is all. What did you think I meant?"
    show allison handsfolded troubled
    call _scene_1S19_lookright
    show mekki behind darren
    show caprice behind eileen
    allison "Nothing. Mind your own business, though. This doesn't have anything to do with you."
    show eileen handonhip angry
    call _scene_1S19_lookleft
    show mekki behind darren
    show caprice behind eileen
    show heather frown
    show darren hmm
    heather "Sure it does. Our club leader is directly affected by whatever nonsense Caprice has pulled. If it hasn't yet, it'll probably affect the club."
    show caprice hattip attacked 
    show eileen behind caprice
    show darren behind mekki
    with dissolve
    call _scene_1S19_lookright
    caprice "{b}Good!{/b} That club deserves to be shut down, being lead by such a thick-headed person."
    show mekki left thinking frustrated
    call _scene_1S19_lookleft
    mekki "It's almost like you're talking about yourself."
    call _scene_1S19_lookright
    caprice "Oh, shut up!"
    call _scene_1S19_lookcenter
    "Very quickly, everything starts dissolving into mindless bickering. Maybe if I'm lucky, I can just slip by one of them and get out of here..."

    show hayley right away behind mekki:
        subpixel True
        xanchor 0.5
        xpos 0.3
        xzoom 0.9
        yzoom 0.9
        yoffset -180 # i will never understand ren'py #M: lol
        alpha 0

        parallel:
            linear 2.0 alpha 1 xzoom 1.0 yzoom 1.0
        parallel:
            ease 2.0 xpos 0.5
    show hayley behind darren
    show caprice behind hayley
    stop music fadeout 2.5
    $ renpy.pause(2.0, hard=True)
    show hayley at pflip('hayley neutral')
    $ renpy.pause(0.4, hard=True)
    show mekki behind hayley
    show darren behind mekki
    hayleyu "Hey, guys."
    "As I'm just starting to slip away, another girl moves right through the gaggle of argumentative artists."
    "It's the girl from earlier. Without an ounce of hesitation, she just walks straight into the epicenter of the storm that I've been trying to sneak away from."
    hayleyu "My classes are over. Want to go home now?"
    show mekki left hmm
    show caprice hattip flushed
    show eileen neutral
    show darren neutral
    show heather skeptical
    with dissolve
    "Simple as that, everyone just kind of... quiets down. What?"
    "Mekki sighs, reaching into her bag. From it, she fetches a pair of keys."
    mekki "Sure Hayley, we can go."
    "She seems unwilling to let the argument stop here and Caprice just sort of grumbles, but for some reason the two of them let it end."
    show hayley away
    $ renpy.transition(dissolve, layer='master')
    hayley "Try to behave, you guys."
    hide caprice
    hide mekki
    hide hayley
    with dissolve

    show eileen:
        ease 1.5 xpos 0.7
    show allison:
        ease 1.5 xpos 0.85
    show darren at mirror:
        ease 1.5 xpos 0.3
    show heather at mirror:
        ease 1.5 xpos 0.15
    "The four of them sort of mill around, not sure what to do now."
    oliver "Uh, did I miss something? Where are they going?"
    eileen "Home. They live together."
    oliver "Wait."
    oliver "Mekki and Caprice live together?"
    show allison holdarm smile
    $ renpy.transition(dissolve, layer='master')
    allison "With Hayley, yep."
    oliver "...How does that work?"
    darren "I think Hayley keeps the peace between them. They tend to stop fighting whenever she shows up."
    heather "Not entirely certain of how that works, but that's how it goes."
    show eileen at flip('eileen neutral'):
        time 0.4
        ease 3.5 xpos 1.2
    $ renpy.pause(0.05)
    show heather at nflip('heather skeptical'):
        time 0.4
        ease 2.5 xpos -0.2
    $ renpy.pause(0.05)
    show darren at nflip('darren neutral'):
        time 0.4
        ease 3.5 xpos -0.2
    $ renpy.pause(0.05)
    show allison at flip('allison handsfolded troubled'):
        time 0.4
        ease 2.5 xpos 1.2
    "They all leave in different directions, chatting about different things."
    "...Those three live together?"

    stop ambiance fadeout 1.5
return
