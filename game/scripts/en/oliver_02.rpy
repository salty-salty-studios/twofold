label scene_1S2_en:
######################
    # Act 1, Scene 2
    # Momma's Boy
    scene bg apartment outside grayskies with dissolve
    window show dissolve
    play ambiance "sfx/ambiance/outside.ogg"
    "My head's buzzing with all sorts of thoughts during the walk back home.\nI have a chance. I have hope."

    "Hope?"
    "Yeah, that is a little unusual. Good fortune isn't exactly my best friend or my most reliable ally. More often than not, something goes horribly wrong."
    "No point in thinking about that, though. Today is different."
    "I wonder what these classes will be like.\nSince there aren't any books for either class, I can't get an idea from them."
    "I have no clue how to answer the choice of 'which class?' until I go to one of them.\nThe concept of such an important choice worries me."
    "My breath rises in front of me as I continue down the sidewalk. Salt Lake City isn't really a dull place, but the season sure makes it feel that way. Gray skies layered over the mountains in the distance and tall buildings make for a dull environment."
    stop music fadeout 1.5

    scene bg apartment frontdoor grayskies with dissolve
    "Arriving at the apartment complex, I insert the key to the front door{nw}"
    play loopsfx "sfx/door_jiggle.ogg"
    extend " and jiggle the handle."

    "Why isn't the handle turning?"
    "I continue frantically twisting the knob, hoping it'll open.\nWell, that's what happens when I start feeling relieved about my situation."
    oliver "God damn it, why...?"
    "It's cold and I really don't feel like staying outside longer than I have to."
    
    show generic newguy smile at right
    $ renpy.transition(dissolve, layer='master')
    stop loopsfx
    guy "Want some help with that?"
    "I whirl around, surprised by the voice behind me. It's just another student tenant.\nI don't say a word, but remove my keys from the lock."
    play sound "sfx/door_trickopen.ogg"
    "The person approaches the door, inserts his own keys, does some weird jiggle and lifts the doorknob a bit while turning it."
    
    "Of course. The door swings open for him."
    guy "Yeah, the landlord is too cheap to fix crap like that.\nYou new here? I haven't seen you around."
    oliver "Uh...{w=0.1} no. I've been here for at least half a year."
    show generic newguy neutral
    $ renpy.transition(dissolve, layer='master')
    guy "Oh. Guess you don't leave too often, huh?"
    "I appreciate your subtlety, stranger."
    oliver "Not really, I guess."
    hide generic
    $ renpy.transition(dissolve, layer='master')
    "I shoulder past the guy without saying much else."
    "It's true though, I don't go out very often... Don't have much to do aside from work and school."
    window hide dissolve
    scene bg apartment stairwell with midDissolve
    scene bg apartment door with midDissolve
    
    play sound "sfx/door_open.ogg"
    scene bg apartment door open with midDissolve
    window show dissolve
    "Once inside, I'm greeted to the familiar quiet of my empty apartment."
    "Semester starts tomorrow. Someone will probably need an apartment and I'll end up with a new roommate."
    "It's a crappy trade; my peace and quiet for less financial stress. The concept of a new roommate is a little daunting, too."
    "A little?"
    "The concept is {i}very{/i} daunting. I have no idea who they'll be or whether I'll get along with them. Or whether they'll make studying and doing homework impossible for me.\nI really just prefer to be left alone. People are too much of a hassle."
    
    stop ambiance fadeout 1.5
    scene bg apartment livingroom phone with midDissolve
    "I sit down on my shitty couch and{nw}"
    show misc tv on:
        xalign 0.5
        yalign 0.5
    $ renpy.transition(dissolve, layer='master')
    extend " turn on my little television. Isn't there something I was supposed to be doing right now...?"
    "Well, aside from calming my shaken nerves."
    "Oh, right!"
    "My mom managed to send me a text, saying she wanted me to call her.\nThe rest of the message was mostly a garbled mess about how she hates texting."

    scene bg apartment livingroom
    $ renpy.transition(dissolve, layer='master')
    "I grab my phone from the table{nw}"
    show misc phone as phone
    show phoneop:
        xpos 540
        ypos 280
    show contactlistearly:
        xpos 550
        ypos 320
    $ renpy.transition(easeinbottom, layer='master')
    "I grab my phone from the table{fast} and hold down one.\nWhen the screen turns to {nw}"
    hide contactlistearly
    show callmom:
        xpos 570
        ypos 380
    play loopsfx "sfx/dialout.ogg"
    "I grab my phone from the table and hold down one.\nWhen the screen turns to {fast}'Calling: Mom', I place it to my ear."
    "Come to think of it, the fact that my mother is the most consistently called person on my phone and I have her on speed-dial is kind of sad."
    "I really should make some friends."

    hide callmom
    show callingmom:
        xpos 585
        ypos 360
    stop loopsfx
    play sound "sfx/phonepickup.ogg"
    hide phone
    hide phoneop
    hide callingmom

    scene cg oliver callmom with dissolve
    show misc phone as phone:
        xalign 0.5
        ypos 1000
    mom "Hello?"
    oliver "Hey, mom. You wanted to talk?"
    mom "Yep! I received a letter in the mail."
    oliver "Oh?"
    "I'm not sure how this is important, but whatever. I've gotten calls for less important things."
    mom "They sent a letter home stating that you're in danger of failing out of college."
    play music "music/tense.ogg" fadein 1.5
    "For the love of - time for damage control. Play dumb. I've made enough dumb decisions to play the part."
    oliver "Why would they do that?"
    mom "Because the billing for your tuition is mailed here, silly. They're going to let me know when you're wasting your money and loans. Did you forget I co-signed on them?"
    "Even though she's speaking in a sweet tone, I can hear the underlying frustration in her voice. As nervous as that makes me, it's understandable. If I bury myself in loans and debt, she's going to have to deal with it too."
    "I heave a sigh."
    oliver "No, I didn't..."
    "Well, that's a lie. If I knew she'd find out, I probably wouldn't have slacked off as much."
    mom "So, what are you planning to do?"
    oliver "Well, I just finished talking to my advisor. We tweaked my schedule. I have way more classes to make up for lost credits and I have to pick an extra class. If I pass them all, I'm in the clear."
    mom "So all you have to do is apply yourself?"
    "It's not like I can't, it's just that things always get in the way."
    oliver "Yeah..."
    stop music fadeout 2.0
    mom "Such confidence! You'll be fine, Ollie. Just don't get lazy, okay?\nI'll call you every now and then to make sure you're sticking to it, alright?"
    oliver "Alright. Anything else?"
    mom "Nope! Love you."
    "I pause reluctantly. At least I don't have a roommate to laugh at me for sounding like I'm an elementary school kid talking to his mom."
    oliver "...Love you too, mom."
    mom "Bye now. Make sure to study!"
    oliver "Yeah, yeah. Talk to you later."

    scene bg apartment livingroom
    show misc phone as phone
    show phoneop:
        xpos 540
        ypos 280
    show callingmom:
        xpos 585
        ypos 360
    with dissolve
    "After pressing the {nw}"
    hide callingmom
    show contactlistearly:
        xpos 550
        ypos 320
    $ renpy.transition(dissolve, layer='master')
    play sound 'sfx/phonehangup.ogg'
    extend "'end call' button on my ancient phone,{nw}"
    hide contactlistearly
    hide phone
    hide phoneop
    $ renpy.transition(moveoutbottom, layer='master')
    extend " I plop the thing on my coffee table and lean back, wondering what to do.{nw}"
    scene bg apartment livingroom phone
    $ renpy.transition(dissolve, layer='master')
    extend " There isn't much."

    "It's freezing out, so I don't want to go for a walk or bike ride.\nI don't really have anyone to call to hang out with, either.\nSchool hasn't started so I don't have any classwork to focus on."
    "All I've got is me, myself and my thoughts."
    "What company."
    "I guess I could always just hop on my computer and surf the internet or play a game or two to help pass the time."
    "Then I guess I'll figure out what to have for dinner and fall asleep in 'anticipation' of tomorrow. A business major doesn't make for fun classes."
    "Well, might as well enjoy the last day I have to myself, I suppose.\nOr at least as much as I can without panicking."

    window hide smoothDissolve
    scene black with longDissolve
return
