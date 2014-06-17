label scene_1S9_en:
######################
    # Act 1, Scene 9
    # As Bitter as the Coffee
    # After half of the pre-club choice writing, you finally meet (sorta) the other heroine. Still toying around with how bitter Oliver is at Mekki.
    call switch_scene_x('bg apartment bedroom night', 'bg classroom generic', { 'yalign': 0 })
    play music "music/handholding.ogg" fadein 2.5
    "Rubbing my eyes, I rue the time spent studying last night instead of sleeping. I can't remember half of the stuff I went over for my accounting class. I'm not sure why I'm struggling now, I took the intro class and passed it last year."
    "Like a moron, I didn't sleep until I felt like I had figured it all out."
    "Now I'm fighting to even keep my eyes open in the middle of class. I've always been good at math, but I feel like dying right now."

    stop music fadeout 10
    scene black
    $ renpy.transition(fastDissolve, layer='master')
    "{cps=*1.10}Don't fall{nw}"
    scene bg classroom generic blur:
        yalign 0.0
    $ renpy.transition(fastDissolve, layer='master')
    extend " asleep."

    scene black
    $ renpy.transition(dissolve, layer='master')
    "{cps=*1.45}Don't fall asle{nw}"
    scene bg classroom generic blur:
        yalign 0.0
    $ renpy.transition(fastDissolve, layer='master')
    extend "ep."

    scene black
    $ renpy.transition(dissolve, layer='master')
    "{cps=*1.75}Don't...{nw}"
    extend " fall aslee{nw}"
    scene bg classroom generic blur:
        yalign 0.0
    $ renpy.transition(fastDissolve, layer='master')
    extend "p."

    scene bg classroom generic blur:
        subpixel True
        yalign 0.0
        easein 4.5 yalign 1.0
    $ renpy.transition(dissolve, layer='master')
    window hide
    scene black
    with longDissolve
    scene bg classroom generic blur:
        yalign 1.0
        easein 0.25 yalign 0.0
    $ renpy.transition(fastDissolve, layer='master')
    scene bg classroom generic with fastDissolve:
        yalign 1.0
        easein 0.25 yalign 0.0
    window show fastDissolve

    "My head dips for a second and shock overwhelms me as I pull myself upright."
    "Maybe I should pinch myself? A slap in the face might work. I could always tell the chick next to me that she has a nice rack."
    "What I'd give for some caffeine right now."
    professor "...So make sure to study pages 245 through 255. At the end of the section, I want you to finish the work that the chapter assigns, in addition to the practices on that sheet I handed out earlier."
    "Okay good, great, awesome. Are we done? Can I go?"
    professor "I expect them to be passed in tomorrow. See {fade}you tom-"
    "That's good enough of a cue for me. I grab my bag, quickly slip my books textbook into it, and move quickly for the door."
    "Everyone goes quiet, but I don't care. I'm too tired to."
    "I need something to wake me up, pronto."

    scene bg campus reverse with fade:
        xalign 0.5
        yalign 0.5
    play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
    "The cafeteria is kind of out of the question, there's far too good of a chance I might run into some happy-house artists who escaped from their comfy, white jackets."
    "Standing outside, I take a deep breath of cold air and hope it'll help wake me up. While trying to do anything but fall asleep, I mull over places I can go and get something to help fight off this fatigue."
    "I think some students in class were talking about a café during class. What'd they call it...?"
    "The Oak Tree or something?"
    "If they at least serve coffee or have a cooler case with caffeinated drinks in it, it's good enough for me. I have an hour and a half between now and my next class... which is the writing course."
    "Yeah, I think I'll be hitting that café to help wake me up."
    stop ambiance fadeout 1.0
    
    show bg cafe outside with fade
    play ambiance "sfx/ambiance/birdchatter.ogg" fadein 0.5
    "Considering it's around ten in the morning, there aren't too many people eating outside at the little tables under the canopy."
    "After taking a quick look the cafe, I suddenly realize this isn't the kind of place I'd want to go to."
    "This is the sort of store that'd be host to all the pretentious art hippies I don't like."
    "Sometimes I wonder whether I should buy a beret or a stupid scarf so I fit in enough that people don't look down their nose at me."
    "Whatever. Coffee. Need. Now."
    play sound "sfx/door_open2.ogg"
    stop ambiance fadeout 0.5

    show bg cafe inside
    with dissolve
    play sound "sfx/door_close.ogg"
    play ambiance "sfx/ambiance/crowd_cafe.ogg" fadein 1.5
    "I push open the door and there's thankfully fewer people inside than outside. Namely, there's only a barista and some girl busing tables."
    "I take a seat at a small booth in the corner and immediately place my head on it."
    
    scene bg cafe tablesurface:
        xalign 0.0
        yalign 1.0
    with dissolve
    "It's nice and cool, which is good. I'd jump into a pool of ice if it'd wake me up."
    waitress "Excuse me?"
    oliver "Yes?"
    "I'm not even going to bother looking up. Just ask me what I want, bus-girl-waiter person."
    waitress "Would you like something to drink? We have a house special today if you're inter-"
    oliver "Can you get me something with like, three espresso in it?"
    waitress "Uhm, I...{w=0.3} I guess I can. We have lattes with one espresso, they might taste better."
    oliver "Just put extra flavoring stuff in the latte. Mocha. Three espresso and lots of mocha. Iced, too."
    waitress "Small, medium, large?"
    "Damn it, just get me my coffee."
    oliver "Medium, I guess."

    show bg cafe tablesurface:
        ease 3.5 xalign 1.0 yalign 0.0
    "I pick my head up.{w=2.0} There's a little menu on my table. I lift it and thumb through it real quick. Apparently they have a little grill in the back and they make hot or cold sandwiches."

    scene bg cafe inside
    $ renpy.transition(dissolve, layer='master')
    "My eyes wander from the menu to the rest of the coffee house."
    "There was actually someone else in the room that I didn't notice, because they were to my back when I entered. She's sitting against the front window, with a book in hand."

    scene cg mekki intro with dissolve
    "Well. While I was expecting avant-garde artists, hippies and nerds, I wasn't quite expecting someone who looks like her."
    "Honestly, she looks like a pre-law student or something."
    "She's pretty attractive. I'm not sure whether she actually reads, or if she's trying to look intelligent to offset her hair color. She's got a coffee mug near her that she isn't touching, so she probably finished her drink."

    scene bg cafe inside with dissolve
    show barista smile at mirror:
        xanchor 0.5
        xpos 0.15
    $ renpy.transition(dissolve, layer='master')
    "When the girl who was clearing tables brings me my drink in a tall, neat-looking ceramic glass, I get her attention for a moment."
    oliver "Excuse me, but could I have one of these flatbread chicken sandwiches?"
    "The bus-girl nods, jotting it down."
    oliver "Oh, and that girl over there."
    waitress "Yes?"
    oliver "Give her a refill of whatever she's drinking and charge me for it."
    waitress "Sure thing, mister."
    show barista at nflip('barista smile'):
        xanchor 0.5
        xpos 0.15
        time 0.8
        ease 1.5 xpos -0.2
    "I guess I should try what Izaac was rambling on about last night. \"Getting out of my comfort zone\", or whatever. Maybe a little flirting with this girl could help."
    "Alright, sit up straight, try to wake up. I don't think she's noticed me yet, so I can still salvage my appearance."
    "I sip my coffee and open my book full of notes, trying to look scholarly in the meantime. Don't want to look like a half-dead bozo when there's a girl I'm trying to impress."
    "Checking my periphery, I see the bus-girl bring a pot of coffee over to the girl. The girl declines at first, but the bus-girl lets her know that I'm paying for it."

    "Alright Oliver, try to be dapper. Try being the operative word."
    show mekki playingbraid surprised:
        xanchor 0.5
        xpos 0.8
        yoffset 0
    $ renpy.transition(dissolve, layer='master')
    "She looks across the room towards me and I give her a small wave and a smile."
    show mekki playingbraid smile
    $ renpy.transition(dissolve, layer='master')
    "A smile is returned, but then the girl immediately{nw}"
    show mekki playingbraid smile away
    $ renpy.transition(dissolve, layer='master')
    extend " looks away and goes back to reading her book."
    hide mekki with dissolve

    "...That's it?"
    "No \"thanks\"? Not even a wave back?"
    "She's sitting there, messing with the end of her braid and ignoring the fact I just paid for her drink. Maybe she is like the other artsy people that I can't stand. Too good for the rest of the population because they don't draw or read some outdated book."
    "What is she reading, anyways?"
    "\"Complete Works of Alexander Pushkin\"."
    "Yeah, as if there wasn't anything more pretentious sounding than some dead author's compilation."
    "Yep."
    "Waste of however much a cup of coffee costs here. I pick up the menu to see how much damage a cup will do to my wallet."
    "Three fifty for a house blend. Great."
    "She's wearing semi-formal looking clothes, so I bet she grew up with money."
    "Why doesn't she pay for my coffee? I bet she can afford it."
    "Most of my remaining time in the cafe is spent grumbling until I get my sandwich. It actually tastes pretty good, which helps lighten my spirit a bit."
    "I finish eating while going over my notes, chug the rest of my drink and decide to get the hell outta Dodge after paying my bill."
    "I check my watch. It looks like I managed to kill a half hour. Still another hour before the writing class, which I'm not exactly looking forward to."
    "Wallace didn't exactly make me feel better about the writing course, either. Maybe I'll just sit outside the class and read some notes. Or maybe I'll take a page from blondie's book – pick up some boring book and read it in front of people."
    stop ambiance fadeout 2.5

    window hide smoothDissolve
    scene black with longDissolve
return
