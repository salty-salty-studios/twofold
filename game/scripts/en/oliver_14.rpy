label scene_1S14_en:
#######################
    # Act 1, Scene 14
    # Hiding in the Enemy's Headquarters
    call switch_scene('bg apartment bedroom night', 'bg library')
    play ambiance "sfx/ambiance/crowd_silent.mp3" fadein 2.0

    "Keeping in mind what Wallace said about that \"turf\" dispute, I've decided it's best that I hide in the library."
    "I mean, the art club itself wasn't as bad as I thought it'd be, but... well, seeing my shitty drawing up there with all the much better \"first\" drawings, I feel embarrassed to even be around the group."
    "I'm not cut out to consider myself an artist. And I really don't feel like dealing with the whole ugly duckling phase more than I have to."
    "All I have to do is find a quiet place to hide from Caprice. If possible, I'd like to avoid anymore pushy attempts to make me join her club."
    "Thankfully the library has its own building with enough bookshelves and chairs tucked away that I can do just that. I can unpack my laptop, get a bit of music playing, do a little studying. Browse the internet a bit."
    "Just after I sit down, I hear{nw}"
    play sound "sfx/wood_knock.ogg"
    extend " a soft knocking on a bookshelf near me."
    
    scene cg mekki library with dissolve
    $ renpy.transition(moveinright, layer='master')
    "A blonde is peeking around the bookshelf in question."
    oliver "Oh, it's you. {fade}Should've expected this, really..."
    "She giggles softly, in a way that I can't describe as anything but girly."

    scene bg library
    show mekki giggle smile:
        xanchor 0.5
        xpos 0.8
        yoffset 0
    with dissolve
    mekki "Couldn't help but notice you walk into the library. Am I interrupting anything important?"
    "Nothing you'd consider important, probably."
    oliver "Not really. Do you need something?"

    show mekki giggle hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "Ah, uh..."
    "Just spit it out, please."
    mekki "I was just wondering if you'd thought about which club you're going to pick. For the tutoring to help with your classes."
    oliver "A little."
    show mekki playingbraid surprised
    $ renpy.transition(dissolve, layer='master')
    mekki "Oh...?"
    show mekki playingbraid smile away
    $ renpy.transition(dissolve, layer='master')
    "She's twirling her braid, looking like she's in thought about something. Presumably, whether I'll pick the competitors club instead of hers."
    oliver "You know, I remember you saying you didn't want to be pushy like Caprice, but you're kind of giving me that feeling now."
    show mekki pensive surprised blush
    $ renpy.transition(dissolve, layer='master')
    "She starts blushing madly, which I didn't expect. I figured she'd get mad or start arguing with me, but she's embarrassed by what I said."
    mekki "I'm not trying to be pushy, I just..."
    show mekki handstogether pout
    $ renpy.transition(dissolve, layer='master')
    mekki "Caprice was bragging that you went to her club and that you were definitely picking hers... I just wanted to know if that was true. I'm just being stupid, really."
    oliver "Oh, uh... no, I haven't done anything like that. I did go by there, but she was holding my homework hostage."
    show mekki handstogether laughing
    $ renpy.transition(dissolve, layer='master')
    "She starts laughing, sounding more relieved than before. Why is it such a big deal to her?"
    show mekki handstogether smile
    $ renpy.transition(dissolve, layer='master')
    oliver "Are you and Caprice friends, or something?"
    show mekki thinking pfah
    $ renpy.transition(dissolve, layer='master')
    mekki "Usually. More like rivals, lately."
    "As tame as \"rival\" sounds, her expression makes me wonder if it isn't more like \"enemy\"."
    oliver "I bet you're not going to explain why?"

    show mekki thinking hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "...No, sorry. That's really just between me and her. No one really knows and I'd prefer it remain that way. It'd be great if both clubs didn't get up in arms about a private argument, but I can't control that."
    "She's fidgeting a lot. I was able to push Caprice for some of the story, but Mekki's giving me the impression I'll get less out of her."
    "I'm sighing because I know there are ulterior motives in this whole 'lets help Oliver!' thing. I'm just a means to some kind of end to this dispute between them. I'd prefer to have no part in it."
    "Even though helping me is a convenience for both of them, it is a convenience for me too."
    show mekki thinking smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Would you like to-"
    oliver "Sure."
    show mekki thinking surprised
    $ renpy.transition(dissolve, layer='master')
    mekki "What if I was going to ask you to join the club, and just got you to agree?"
    oliver "You weren't."
    show mekki thinking hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "How do you figure?"
    oliver "Somehow, you don't strike me as the underhanded type. You want me to go check out your club?"
    mekki "Yes.{w=0.1}{nw}"
    show mekki thinking smile
    $ renpy.transition(dissolve, layer='master')
    extend " But only if you want to!"
    oliver "I might as well. I hate to admit it, but I'm stuck. I'm going to need one of you to help me out."

    show mekki pensive smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    "Mekki claps her hands together in delight. I'm not sure if she's happy that I need her help, or that I'm willing to go to her club's meeting. She reaches into her backpack and gets a notebook, from which she tears a piece of paper."
    "On it, she writes something out with a red fountain pen on a nearby table."
    show mekki pensive smile
    $ renpy.transition(dissolve, layer='master')
    mekki "There's the club room number, if you forgot it. You can show up whenever, or not at all if you want."
    oliver "But you want me to go, don't you? Why are you offering the option to decline if you clearly want me to?"

    show mekki hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "What I want and what you want are different, and I respect that. I want to make sure you know you can make your decision, not be forced to choose mine."
    oliver "I'll keep that in mind, thanks."

    window hide smoothDissolve
    show note mekki club with easeinbottom
    $ renpy.pause()
    window show dissolve
    "I glance down at the paper and the room number and time period look familiar once I see it. Her handwriting is also... really, really neat. It's damn near calligraphy."
    oliver "Do you always write like this?"
    hide note with easeoutbottom

    mekki "No, not always.{nw}"
    show mekki handstogether smile
    $ renpy.transition(dissolve, layer='master')
    extend " Only when I think it's important."
    "Her smile is disarming. I have to keep questioning what exactly is more important to them. Me, or their argument? It's probably their argument, but I can't be sure."
    "The fact she seems oh-so accommodating and willing to make herself out to be \"the better choice\" only makes me feel like she only cares about being right."
    oliver "I do need to study, though."
    show mekki handstogether surprised
    $ renpy.transition(dissolve, layer='master')
    mekki "Oh, sorry. I'll go over there, if you need me. You probably won't, but -"
    oliver "It's okay."
    show mekki handstogether smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Right! Bye now."
    hide mekki with dissolve
    "Man. Why did she have to draw that heart on the note?"

    stop ambiance fadeout 2.0
return
