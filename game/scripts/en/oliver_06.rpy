label scene_1S6_en:
######################
    # Act 1, Scene 6
    # Whoops
    # Summary: Oliver skips through his classes, then heads back to the cafeteria to talk to Wallace, hoping that the club he mentioned is also Caprice's. Leaves, slams into Allison. Moment of utter mortification, then he's going to start heading towards his next class, which is one of his major's core classes.
    call switch_scene('bg apartment bedroom', 'bg classroom generic')
    play music "music/handholding.ogg" fadein 1.0
    "They say that the mind, when presented with absolutely nothing of interest, will attempt to fill the void with creative thoughts."
    "This doesn't seem true for me, however. The last two classes have been nothing but pure monotony and I've been painfully conscious for both of them. No fun, distracting thoughts; just dull, general credit courses."
    "Though, my mind keeps wandering back to the classes I'm supposed to choose between. I've experienced one this week and the next is in a day or two."
    "If the writing one is as... odd as the art one is, I don't think I'll be able to pick one without a coin's involvement."
    "I hope the writing class is a bit more tame."
    "Thankfully, within moments of my eyes darting towards the clock, the professor informs everyone that class is over."
    
    scene bg hallway 2 with dissolve
    "My next class isn't for a couple hours. I could go home, or I could head to the cafeteria for another round of people-watching."
    "When you boil it down, my choices are being alone in an apartment while counting up all the things I dislike..."
    "...or, I can go to the cafeteria and do that about all the people around me, instead of myself."
    "I think the second of the two is a bit more appealing."
    stop music fadeout 2.5

    scene bg union cafetaria counter with dissolve
    $ renpy.music.set_volume(0.6, channel='loopsfx')
    play ambiance "sfx/ambiance/crowd_cafetaria.ogg" fadein 1.0
    "As usual, the building is loud and bustling. Surprisingly, the cafeteria's line is fairly short and I'm able to grab an order of fries for a snack."
    
    scene bg union cafetaria with dissolve
    "I chew on a few fries while facing the cafeteria's dining room. There's so many people around that I don't stick out, so I can scan over the room without really being noticed."
    "Nothing going on in the cafeteria is out of the ordinary. I'm surprised I don't see the human cannonball bouncing around, shouting at the top of her lungs, though. I'd expect her to start popping up randomly and dropping hints about her club within my listening range by now."
    "However, I do see Wallace. Sitting by himself, alone in a sea of people. I almost feel bad for him."
    "Thinking about it, I realize that's usually how I am."
    "Now I feel bad for myself."
    "Wallace did mention that he's part of an art club. I'm not sure if there are many in this school, so maybe it's Caprice's?"
    "If that's the case, I should ask and get a bit of insight on what the club is like."
    
    show wallace frown
    $ renpy.transition(dissolve, layer='master')
    "When I sit down across from him, he glances up at me and grunts."
    oliver "Nice to see you too."
    show wallace frown away
    $ renpy.transition(dissolve, layer='master')
    wallace "I'd prefer to draw in peace."
    oliver "What, do you dislike having company?"
    wallace "You know as well as I do that we both hate company."
    oliver "Me? Hating company? Surely you jest."
    show wallace frown
    $ renpy.transition(dissolve, layer='master')
    "He looks up from his laptop again, only to give me a disapproving glare. I guess humor isn't his strong suit. It's probably not mine either. I should stop trying."
    oliver "Well, I did want to ask you about something."
    "No response telling me to shut up, so I guess I'm cleared for asking."
    oliver "What art club are you part of?"
    "The barely audible scratching of his tablet pen stops for a moment."
    show wallace neutral
    $ renpy.transition(dissolve, layer='master')
    wallace "Are you planning to join an art club?"
    "Well, the jury's still out on that call."
    oliver "I might. It's why I'm asking. I have to pick an art or a writing class. A girl named Caprice is in my art class and suggests I join her art club so I have 'no chance of failing' my art course."
    "At the word 'Caprice', I can see Wallace visibly{nw}"
    show wallace frown
    $ renpy.transition(dissolve, layer='master')
    extend " cringe."

    oliver "That's very reassuring. You know her?"
    wallace "Yeah, she's the one who founded the current \"prominent\" art club. She's not exactly easy to deal with. Sure, she knows her stuff..."
    show wallace neutral
    $ renpy.transition(dissolve, layer='master')
    "He puts down his pen and leans back into his chair, sighing."
    wallace "She's usually more trouble than she's worth. In my opinion, anyways."
    "I take in a deep breath and let it go, along with my hopes for an \"easy solution\". This isn't exactly surprising. He's just confirming what Caprice's impression left on me."
    oliver "But she knows what she's doing? She's no flake who's pretending to be some super-smart art nerd or something, right?"
    "Wallace shakes his head."
    wallace "Nah, she's the real McCoy, I guess.{nw}"
    show wallace frown away
    $ renpy.transition(dissolve, layer='master')
    extend " Just a pain in the ass. A {i}loud{/i} pain in the ass."
    "I could've guessed that on my own."

    show wallace neutral
    $ renpy.transition(dissolve, layer='master')
    "Wallace opens his mouth, but stops himself."
    wallace "No, that's probably a bad idea, too."
    oliver "...What do you mean?"
    wallace "Well, you mentioned art or writing? I'd want to suggest writing, but{nw}"
    show wallace frown
    $ renpy.transition(dissolve, layer='master')
    extend " I somehow doubt it'll be any better..."

    "Great. So no matter what I choose, I'm screwed?"
    wallace "Why do you have to pick one or the other?"
    oliver "Uh... a bit of a mishap with my credit load."
    "Yeah, that's what I'll call it. A \"mishap\"."
    wallace "Well, good luck. You're probably going to need it."
    "How familiar those words are."
    "I lower my head into my hands with a sigh before lifting it again."
    oliver "Which do you think I should pick? You seem a bit more knowledgeable about these things."

    show wallace frown away
    $ renpy.transition(dissolve, layer='master')
    "Wallace returns to sketching on his tablet."
    wallace "I think it's better that you pick your own poison."
    "I finish off my fries and crumple the flimsy paper holder they were in."
    oliver "Well, thanks anyways. I was sort of expecting you to just blow me off or something."
    show wallace neutral
    $ renpy.transition(dissolve, layer='master')
    "Wallace shrugs."
    oliver "See you around."
    wallace "Yeah."
    hide wallace with dissolve

    "Standing up, I{nw}" 
    scene black
    $ renpy.transition(dissolve, layer='master')
    extend " close my eyes and take a deep breath."
    "I turn and head for the exit, only opening my eyes as I feel something{nw}"
    play sound "sfx/body_collision.ogg"
    $ renpy.transition(vpunch, layer='master')
    extend " slam into{nw}"
    play sound "sfx/shatter.ogg"
    extend " my chest."
    "The sound of something shattering causes my eyes to {nw}"
    scene cg allison crash
    $ renpy.transition(fastDissolve, layer='master')
    extend " snap open."
    window hide smoothDissolve
    $ renpy.pause()
    window show smoothDissolve

    show allison troubled:
        ypos 1000
        xanchor 0.5
        xpos 0.70
    oliver "Huh?"
    allisonu "No, no no nonono..."
    "Looks like some chick walked into me and broke something she dropped. Wallace stands up too, though I'm not sure whether he's concerned or not."
    oliver "Uh, you okay? You broke your... thing."
    allisonu "I... I can't believe... it's broken."
    "...Is she gonna cry? Crap, I think she's going to."
    "Oh man, I have no idea what I should do right now."
    oliver "Do you want me to help pick them up or something? Sorry, it was an accident, I don't know-"
    "She doesn't even respond to me."
    allisonu "I even told her I was going to be careful with these!"
    "Why get so upset? Just make another. You can't even tell what the thing was, which means it probably wasn't that great of a whatever-it-was in the first place."
    "I don't have time to be feeling this awful about an accident that I'm not at fault for. I have class to go to soon. Wait, what time is it?"
    "Looking at a clock on the wall, class is starting in less than five minutes. I have to walk across campus to get to class. A little bit of panic starts to set in."
    "Wallace looks shocked, but seems to be staying out of this little mess. I glance around at the cafeteria and some people are starting to stare at me. Oh, for the love of-"
    oliver "I didn't mean to, I uh... I really have to go to class. I'm sorry I bumped into you, try to look where you're going next time."

    scene bg union cafetaria with dissolve
    "I don't know what to do and I don't think I can handle this. Some girl is about to cry over something she spent likely only spent twenty minutes on, and the rest of the cafeteria probably thinks I attacked her or something."
    "All I can do is leave with that pitiful remark and rush to class. "

    stop ambiance fadeout 2.5
    $ renpy.music.set_volume(1.0, channel='loopsfx')
    window hide smoothDissolve
    scene black with dissolve
return
