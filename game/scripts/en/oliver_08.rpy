label scene_1S8_en:
######################
    # Act 1, Scene 8
    # First Impressions
    # Oliver goes home and chats with Izaac for a while before turning in to do homework and go to sleep."
    call switch_scene_s('bg campus reverse', 'bg apartment frontdoor')
    play music "music/genericrelaxmusic.ogg" fadein 1.0
    "Normally, I'm not as excited to return home from school. Usually school and work are distractions from how empty the rest of my life is."
    "However, lately school has been a little... too much for me."
    "A little bit of nothing might be a good change."  

    play sound "sfx/door_open.ogg"
    scene bg apartment stairwell
    $ renpy.transition(dissolve, layer='master')
    "I leave my bike in the same place as always,{nw}"
    play sound2 "sfx/door_close.ogg"
    scene bg apartment stairwell bike
    $ renpy.transition(dissolve, layer='master')
    extend " leaned up against the stairwell in the front hallway."
    scene bg apartment door with dissolve
    play sound "sfx/door_open2.ogg"
    "I turn the doorknob, checking to see if Izaac is in the apartment.{nw}"
    scene bg apartment door open
    $ renpy.transition(dissolve, layer='master')
    extend " The door is unlocked, so either he is here, or he's stupid and didn't lock the door."
    
    scene bg apartment livingroom
    show misc tv on:
        xalign 0.5
        yalign 0.5
    with dissolve
    play sound "sfx/door_close3.ogg"
    "Nope, there he is sitting on the couch."
    show izaac handspockets grin
    $ renpy.transition(dissolve, layer='master')
    izaac "Yo! How was your day, dude?"
    "I dump my bag near the door, sighing as I collapse onto the couch. Izaac is watching something that I don't care about, so I grab hold of the TV remote and{nw}"
    show misc tv movie:
        xalign 0.5
        yalign 0.5
    extend " change the channel."
    show izaac shrug surprised
    $ renpy.transition(dissolve, layer='master')
    izaac "Hey!"
    oliver "I pay for the cable, deal with it."
    "After settling on some random movie from years ago, I groan."

    oliver "Today was something."
    show izaac surprised
    $ renpy.transition(dissolve, layer='master')
    izaac "C'mon, be more specific. Like what?"
    "It doesn't take long to rattle off the list of weird stuff that I've found myself knee-deep in lately. All after I've been forced to try these new classes and pay attention to 'artists'."
    oliver "{fade=40,100}I'm pretty sure{/fade} most of them are insane. At least, Caprice is. I don't see how anyone can be that energetic or loud naturally."
    oliver "And then that Wallace guy is pretty hard to deal with a majority of the time and so far Eileen seems impossible to talk to."
    oliver "I'm also too afraid to interact with Allison because she might run to her best friend and then I'll have Eileen knocking my face in or something."
    show izaac laughing
    $ renpy.transition(dissolve, layer='master')
    "Izaac starts laughing."
    izaac "All that because you suck at school?{nw}"
    show izaac shrug smirk
    $ renpy.transition(dissolve, layer='master')
    extend " C'mon man, even I'm getting better grades than you."
    "I grind my teeth, trying to ignore the potential truth in that."

    show izaac smirk
    $ renpy.transition(dissolve, layer='master')
    izaac "But lets think about it for a moment. Let me try to enlighten you. I can be your social mentor! Give you advice on all the crap you're dealing with."
    "I think the last thing I need is a \"social mentor\" like this guy."
    izaac "What if like, they're not the crazy ones?"
    "I glance sideways at Izaac."
    "Really?"
    show izaac grin
    $ renpy.transition(dissolve, layer='master')
    izaac "No, really, think about it! What if they're not crazy and you're the crazy one. They're completely sane but you're so off the deep-end you can't even tell!"
    "I put down the remote and stand up."
    oliver "I'm going to make myself some dinner and do my homework."

    show izaac headscratch surprised
    $ renpy.transition(dissolve, layer='master')
    izaac "C'mon! Don't just blow me off like that."
    oliver "I think I'll make some noodles or something."
    izaac "Ollie, please!"
    oliver "If you enjoy having cable, don't call me 'Ollie'."

    show izaac headscratch smirk eyesclosed
    $ renpy.transition(dissolve, layer='master')
    izaac "Hah, gotcha to respond."
    show izaac headscratch frown
    $ renpy.transition(dissolve, layer='master')
    izaac "But okay, I get it. You think I'm stupid, whatever. I do think that you need to shake up your life a bit, though."
    izaac "How often do you even socialize with people, anyway? I bet this is the most you have since you got here. I bet you're secretly loving all this."
    "Loving? Not the word I'd use."

    show izaac headscratch smirk

    $ renpy.transition(dissolve, layer='master')
    izaac "Plus, that girl offered to help you pass your class. What's the harm in it? Sure, there's some odd people involved, they'll get over whatever it is bugging them and you'll probably have fun."
    izaac "Don't just write it off because you're scared of new things, though."
    show izaac headscratch grin
    $ renpy.transition(dissolve, layer='master')
    izaac "Or should I say {i}draw{/i} it off?"
    oliver "I'm not scared. You're not funny, either."

    show izaac headscratch smirk
    $ renpy.transition(dissolve, layer='master')
    izaac "Yeah, yeah. Go make your noodles, noodleboy."
    oliver "That's not even an insult."
    izaac "Not 'sposed to be one, dude."

    scene bg apartment kitchen with dissolve
    "I head into the kitchen, rummaging through the cabinets. It looks like Izaac has already been populating my cabinets with food."
    "And by food, I mean protein, oats, peanut butter and boxes of \"power bars\"."
    "Somewhere at the back, are my cup noodles.\nAdd water, toss it in the microwave; now I have dinner."
    "Fork and hot food in hand, I head back to my room so I can hammer through tonight's assignments for the week."
    stop music fadeout 2.5
    scene black with dissolve

    scene bg apartment bedroom night with longDissolve
    play ambiance "sfx/ambiance/nightfall.ogg" fadein 0.8
    "Unlike my usual habits, I'm trying to get everything out of the way as soon as it's assigned, so I don't get lazy and wait until the last second anymore."
    "It's hard to get used to, but I keep telling myself about all the awful things that'll happen if I don't do well this semester."
    "That uneasy lump in my stomach regarding failure keeps me motivated from becoming one."
    "At least tomorrow is going to be easier, course-wise. All I have are two short classes and the writing course."
    "I'm hoping the whole writing course won't feel as abysmal as the art class did."
    stop ambiance fadeout 1.5
return
