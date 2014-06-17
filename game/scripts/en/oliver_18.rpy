label scene_1S18_en:
#######################
    # Act 1, Scene 18
    # Voices in Your Head
    scene bg campus outskirts with dissolve
    window show smoothDissolve

    play ambiance "sfx/ambiance/outside.ogg" fadein 1.5
    "Finally, the horror show of classes has finished."
    "As much as I look forward to going home, relaxing and enjoying the rest of my day, I can't."
    "I have work later tonight, starting from three in the afternoon all the way until midnight. I love that our kitchen closes at nine, but it takes so long cleaning and putting everything back the way it should be that we don't leave until much later."
    "Remembering that today is a short day at my restaurant only makes me feel worse. Normally I'd work noon to midnight, like I will be on Saturday."
    "Ah, whatever."
    "\"Look on the bright side, Ollie!\" is probably something Caprice would say. \"Yes, you'll never get anywhere with such a negative attitude.\" would be Mekki's follow-up, if she could stomach agreeing with her counterpart."
    "Someone kill me, I can already hear the two of them in my head."

    scene bg cafe outside with fade
    "Well, what's the bright side of this cold ride home?"
    "The pair of biking gloves I bought on the internet came in last night, so I get to enjoy them during the ride home. I suppose that's a small silver lining."
    "They make me feel sort of cool since they're the same brand that most professional bike racers use. Good at making sure your hands stay warm and on the handlebars."
    "It'd be nice if I didn't also feel like a loser because I'm still riding my bike places instead of being more successful, accomplished and own a car of my own."
    scene bg apartment outside with fade
    play loopsfx "sfx/cell_phone_vibrate.ogg"
    play music "music/ringtone.mp3"
    "The ride home is always uneventful. Well, except for today, I guess. My phone is buzzing in my pocket, meaning my mom's calling me. No one else does."
    "I pull over at the nearest bench and answer my phone."

    show misc phone as phone
    show phoneop:
        xpos 540
        ypos 280
    show callingmom:
        xpos 585
        ypos 360
    $ renpy.transition(easeinbottom, layer='master')
    stop music
    stop loopsfx
    play sound "sfx/phonepickup.ogg"
    oliver "Hey mom. What's up?"
    mom "Oh, just callin'. No work today and I finished cleaning my apartment so I figured I'd give you a ring!"
    oliver "Ah."
    mom "So how have you beeeeen?"
    oliver "I don't even know where to start..."
    mom "Well, how are your new classes that you have to take?"
    oliver "I probably can't pass them."
    "Ah, I was looking forward to that silence."
    oliver "Know how I have to pick a class? I can't pass either on my own, but some girl from each class is willing to tutor me so I can pass."
    mom "Ah, that's such good news! Are they cute?"
    "Man, that's not really relevant to the whole problem at hand."
    oliver "I guess, but I really don't think that's imp-"
    mom "I don't know, Ollie. If you can get a girlfriend out of the deal, you should!"
    oliver "Even if I tried, I doubt they'd be interested."
    mom "I don't think that's true! You're such a handsome young man. Plus, remember your senior prom? Some adorable girl asked you to take her to the prom."
    "I remember that, but a different way."
    "She asked me because her date dumped her at the last second and she didn't want to go without someone to fall back on. I'll be honest, I was pretty excited. My mom even had saved money for a tux."
    "\"I was expecting you to go, so I saved some money!\""
    "The girl in question spent the rest of the night dancing with some other guy and I just sat off the to the side, eating bad food."
    "I played it off to my mom that it was a great night when I got home."
    oliver "Yeah. Maybe, then."
    mom "What are their names?"
    oliver "Mekki and Caprice."
    mom "Hmm. What do they look like? They must be cuties if they're art students."
    oliver "Mom, I was kind of riding home so I could get ready for work in an hour."
    mom "Oh, oh, sorry! I totally forgot you're working today. Say hi to everyone for me! I think I'll be working tomorrow morning."
    oliver "Will do, mom."
    mom "Love you!"
    oliver "...You too."
    play sound "sfx/phonehangup.ogg"
    hide callingmom with dissolve
    hide phone
    hide phoneop
    with easeoutbottom

    "Well, today is going to be fun. Working 'til midnight and then sitting through a couple classes at eight in the morning is going to be wonderful. Especially considering that I have another long shift after my short class load this weekend."
    "Maybe I should buy a few energy drinks to get me through this."
    stop ambiance fadeout 2.5
return
