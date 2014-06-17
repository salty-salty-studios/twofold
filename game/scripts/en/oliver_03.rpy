label scene_1S3_en:
########################
    # Act 1, Scene 3
    # One-Sided

    scene black
    play sound "sfx/alarm_clock_start.ogg"
    $ renpy.music.set_volume(0.1, channel='loopsfx')
    $ renpy.music.set_volume(0.1, channel='sound')
    play loopsfx "sfx/alarm_clock.ogg" fadein 3.0
    scene bg apartment bedroom blur with eyesr
    with dissolve

    window show dissolve
    "My vision's hazy as I open my eyes, trying to find my alarm clock. The damn thing is relentless, unwilling to stop blaring until I find it. I unsuccessfully slap{nw}"
    $ renpy.transition(vpunch, layer='master')
    play sound "sfx/thud_mute.ogg"
    extend " the end-table around the clock, trying to hit the snooze button."
    "I groan and force myself to sit up so I can locate the off button.{nw}"
    stop loopsfx
    play sound "sfx/alarm_clock_stop.ogg"
    scene cg alarmclock blur with dissolve
    $ renpy.music.set_volume(1.0, channel='sound')
    $ renpy.music.set_volume(1.0, channel='loopsfx')
    extend " When my vision clears,{nw}"
    scene cg alarmclock
    $ renpy.transition(longDissolve, layer='master')
    extend " I'm greeted by something that ties a knot in my gut."
    play music "music/panic.ogg" fadein 0.5
    "SHIT!"
    "I must have slept through my alarm a couple times. How?"
    "I don't have the time to figure out how."
    scene bg apartment bedroom with dissolve
    "I've got to get ready, or I'm going to be late."
    "There's twenty minutes before my first class begins."
    "I fall out of bed{nw}"
    play sound "sfx/body_collision.ogg"
    $ renpy.transition(hpunch, layer='master')
    extend " and start scrambling around for clothes. Throwing on a pair of jeans and one of my typical green shirts, I make a quick stop at my bathroom."
    
    scene bg apartment bathroom
    $ renpy.transition(dissolve, layer='master')
    "Hair looks neat, not greasy? Face decent?"
    "After going through a checklist of negative criticisms that I would receive, I decide I look presentable enough."
    "Still, there are noticeable dark circles beneath my eyes. I guess the double shifts at my kitchen job are finally wearing on me. I can't wait to cut my hours so I can get a decent night of sleep more than once a week."
    "I brush my teeth quickly and run back to my room."
    
    scene bg apartment bedroom
    $ renpy.transition(dissolve, layer='master')
    "Without looking, I stuff whatever books I think I need into my bag. Once done, I shoulder the pack, head for the exit and lock{nw}"
    play sound "sfx/door_close.ogg"
    extend " my apartment door behind me."
    
    scene bg apartment stairwell bike
    $ renpy.transition(dissolve, layer='master')
    "Once I'm at the bottom of the stairs, I'm greeted by my faithful mountain bike.\nIf it weren't for this thing, I'd definitely be late today."
    
    play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
    scene bg campus outskirts with dissolve
    "After an exhaustingly fast-paced ride to the campus grounds, my watch reads that I have little over five minutes before class begins. Being late to my first class isn't really a good way to start this whole 'GPA rescue' scheme."
    "This is pretty typical of me, though. Get a chance to redeem myself?\nImmediately botch it as soon as possible."
    "I'll make a note to scold myself later. Someone will do it for me, I'm sure."
    "I just have to make it to my morning history class before my professor takes attendance. Hopefully I don't slam into anyone on the way there. There are a lot of students wandering around the campus right now."
    "Locking my bike in the nearest rack, I rush off to class."
    
    stop music fadeout 3.5
    stop ambiance fadeout 1.5
    scene bg hallway 2 with dissolve
    play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 1.0
    "Thankfully, I make it to class before the instructor does. The seats are mostly filled, but the professor is nowhere to be found. I can't say whether I'll be able to stay awake during this class, though. History has never been one of my favorite courses."
    "Well, here goes nothing."
    stop ambiance fadeout 2.5
    window hide dissolve
    scene black with longDissolve
    $ renpy.pause(1.0)
    scene bg hallway 2 with longDissolve
    window show dissolve
    play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 1.0
    "By the time I leave class, I'm barely awake. Any kind of history class is way too boring, let alone \"US History to 1877\". It's stuff we all should know anyways and it's not really in the \"interesting\" or \"useful\" categories of academics."
    "Though, I am trying. I took notes instead of finding a way to sleep while appearing awake and attentive. I can't start sloppy or I'll only tumble further down the slippery slope of failure."
    "I look to the schedule Lawe printed up for me. My eyes narrow a bit.\nThe supplemental art class is next."
    "So much for having time to mentally prepare myself. I guess I'm taking a crash course in a class and skill I probably have no talent for."
    "I remember one of the last things Lawe said during my advising session."
    "\"You have a week to figure out which class you want to take, that's the longest I can manage a \"clerical error\".\""
    "Although I haven't had longer than a day to prepare myself for this class, at least I have an hour before it starts."
    "Maybe I'll go to the cafeteria and take my mind off of this with some food."
    stop ambiance fadeout 1.0

    scene bg union foyer with dissolve
    play sound "sfx/door_close2.ogg"
    "Walking into the union building, I'm reminded of the dread I felt yesterday.\nThankfully, I can brush it off."
    "Today, I'm not here to have someone tell me about how much of a failure I am.\nToday, I'm here for the other half of the union building that most students enjoy greatly; the cafeteria."
    "For a community college, the food is good enough for what they charge. I'm sure someone would say otherwise about it, though."
    "I have to give the guys who work in the cafeteria's kitchen a little credit, it's probably not easy cooking for a bunch of idiots in a community college."
    "I do a mental tally of what I have in my wallet. I'm trying to save money, so I'll probably only grab a snack and soda from the vending machines. Now I just have to find a mostly empty table to sit at."
    
    play ambiance "sfx/ambiance/crowd_cafetaria.ogg" fadein 0.5
    scene bg union cafetaria with dissolve
    "I find a table that's mostly vacant and sit down. After I open my bag of chips, I mindlessly scan the cafeteria. It's filled with the usual crowd; the dumb, the lazy, the ridiculous."
    "That observation reminds me why I don't usually like coming to the café; I don't really like people. I don't understand them."
    "People have a habit of bashing me when I've never really done anything wrong.\nI'm always told I'm at fault, that there's always something I'm doing that needs to change."
    "I think that's bull. I shouldn't have to change because of how crappy people are."
    "I guess that inability to \"adapt\" is why I don't have as many friends as other people do. I'm fine with that. Why would I want to be like them?"
    wallaceu "I didn't say you could sit here."
    "Huh?"
    
    scene cg wallace intro away with dissolve
    show wallace neutral:
        ypos -5000
        xanchor 0.5
        xpos 0.25
    "Glancing over, I see a man with a beard staring at a computer in front of him, a tablet on his lap."
    oliver "What?"
    wallaceu "Are you deaf? I'm asking you to go away."   
    "This is exactly what I mean about people and why I usually don't get along with them. Is there really a need to be like that?"
    "The guy looks like he's easily an adult, but he's acting like some teen-aged jerk."
    "I almost chew the guy out, but the words catch in my throat."
    "I want to get mad, I want to tell him off. I just can't find the effort. Not worth it, or the time."
    "Instead, I find myself glaring at my bag of chips rather than the jerk. Hopefully if I stay quiet, I won't have to go anywhere."
    show cg wallace intro awayfrown
    $ renpy.transition(dissolve, layer='master')
    "The guy next to me gives a heavy sigh."
    
    show cg wallace intro with dissolve
    wallaceu "Look, sorry."
    "Huh?"
    wallaceu "I'm just a little pissed and I probably jumped the gun there."
    oliver "...Thanks."
    "Most people never really bother to apologize. It's still nice to hear though, even if he's just saying it."
    wallaceu "Well, you looked like you were gonna cry, so I got kind of nervous."
    oliver "I was {i}not{/i} going to cry."
    show cg wallace intro away
    $ renpy.transition(dissolve, layer='master')
    wallaceu "Whatever you say, kid."
    
    "Okay, so maybe he's not as much of an asshole as I figured."
    "Hell, maybe he's even {i}nice{/i}. I'm sort of doubtful, but reflecting on the last day or so, I'm starting to think I should try to... well, make some friends."
    oliver "So, uh... why'd you get so aggressive in the first place?"
    "Wait, I don't think I'm doing it right. He's probably going to take that the wrong way and this will turn into me wasting time by arguing with someone."
    wallaceu "Well, people keep bugging me about the fact that I'm drawing{nw}"
    show cg wallace intro awayfrown
    $ renpy.transition(dissolve, layer='master')
    extend "."
    "He frowns when he realizes the trap he's fallen into. Mentioning that you dislike something people do is like inviting them to do it. I know that from experience."

    oliver "Why not go to the library? Probably quieter there."
    "His frown deepens, which I find confusing."
    wallaceu "Well, there's a bit of a \"turf dispute\" going on and I'd like to stay out of it right now. That's why I'm here, being bugged by people every five minutes."
    oliver "Turf dispute? What, does this school have {i}gangs{/i}?"
    "If so, I'm thinking maybe I should actually drop out."
    show cg wallace intro
    $ renpy.transition(dissolve, layer='master')
    wallaceu "Something like that. Not the kind that'll knife you, at least."
    oliver "That's good, I think."
    show cg wallace intro away
    $ renpy.transition(dissolve, layer='master')
    "I don't want to bug him too much, so I sort of let the conversation hang. Glancing over at what he's drawing, I see that he's sketching out a set of panels for a comic."
    "After finishing most of my chips and glancing over again, I realize he's drawing it right to left. Manga, huh? As much as I don't want to run the risk of getting him angry, I would like to at least make friendly conversation."
   
    oliver "Drawing manga? That's, uh, cool. I've seen them at a comic store I live near. Haven't read any, though. I don't think I can get into the art."
    "His response is a grumble that actually sounds more like a bear growling."
    wallaceu "So then why are you talking to me about it?"
    oliver "Just trying to be friendly, {fade=100,20}I guess..."
    
    "It's hard to tell, but it almost looks like he's embarrassed that I actually know what he's drawing. I can relate to the feeling, honestly. Maybe he had a moment of panic when I started asking about something he's shy about."
    "I'm resisting a grin, because he doesn't look the kind to like foreign media or get flustered. At first glance, he looks like the kind to paint pictures of soup cans or rocks and call it innovative."

    scene bg union cafetaria
    show wallace frown away
    with dissolve
    "The conversation ends and minutes pass before he closes his laptop, stashing it and his tablet in a nearby computer bag."
    oliver "{fade}See you around..."
    show wallace neutral
    $ renpy.transition(dissolve, layer='master')
    "The man stops for a moment, surprised by me saying goodbye."
    wallace "Yeah. Name's Wallace, too. In case you, uh, do see me around."
    "We pause for a moment, staring awkwardly at each other."
    wallace "I gotta go.{w=0.3} To my club.{w=0.5} Bye."
    hide wallace with dissolve

    "Well then. That was certainly... one of the more unusual experiences I've had so far. Maybe I shouldn't try to make friends."
    "Or at the least, maybe I should pick who I talk to more carefully."
    "Checking my watch, I should probably head to my next class, too."
    "Here goes nothing."
    "{nw}"
    stop ambiance fadeout 3.5
return
