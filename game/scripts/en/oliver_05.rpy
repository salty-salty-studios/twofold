label scene_1S5_en:
######################
    # Act 1, Scene 5
    # Beef Stroganoff
    call switch_scene_s('bg hallway 1 poster', 'bg apartment frontdoor')
    play ambiance "sfx/ambiance/outside.ogg" fadein 3.0
    "I have to call today a small achievement for me. I managed to not fall asleep in any of my classes. I even managed to take notes and write down all of the homework assignments."
    "Who even assigns homework on the first day? These asshole teachers do, apparently."
    "Either way, I'm glad to be out of there and at home so I can finally sit and relax.{nw}"
    play sound "sfx/door_open2.ogg"
    scene bg apartment stairwell bike
    $ renpy.transition(dissolve, layer='master')
    extend " Fishing my key for the front door out of my pocket, I leave my bike where I always do and head to the second floor."
    
    scene bg apartment door with dissolve
    "I find my apartment key and insert it into the doorknob. When I turn it, it appears the door is already unlocked.{nw}"
    play sound "sfx/door_unlock.ogg"
    extend " A cold wave of panic surges through me. I know for a fact I locked it this morning."
    "I don't open the door. Instead, I entertain a thought:"
    play music "music/tense.ogg" fadein 1.5
    "Who is in my apartment right now?"
    "My body freezes up. My first thought is 'burglar', but what do I have worth stealing? My computer at best, but there's not much anything else."
    "Maybe my old roommate left something behind and never returned his key? The landlord should've changed my locks if that's the case, though."
    stop ambiance fadeout 0.75

    scene cg izaac burglar
    $ renpy.transition(dissolve, layer='master')
    play sound "sfx/door_shuffle.ogg"
    "Opening my door a sliver, I see someone sitting on my couch, watching my TV."
    "And they're eating something out of my tupperware?"
    "What the hell?"
    "I look around the hallway. There's nothing nearby I can use as a weapon, except for maybe that little potted plant on the outside of my neighbor's windowsill."
    "Not exactly effective or intimidating if this is a burglar..."
    "I guess if I surprise whoever it is, I'll at least have the upper-hand. Taking a deep breath,{nw}"
    play sound "sfx/door_shuffle.ogg"
    " I push the door completely open."

    scene bg apartment livingroom
    show misc tv handegg:
        xalign 0.5
        yalign 0.5
    with dissolve
    stop music fadeout 0.5
    oliver "Hey!"
    "The guy on my couch jumps, nearly{nw}"
    play sound "sfx/cutlery_fall.ogg"
    extend " flinging all the food in my tupperware container all over the floor."
    show izaac headscratch surprised
    $ renpy.transition(dissolve, layer='master')
    izaacu "Whoa! Jeez, dude - scared the crap outta me!"
    "Well, if he is a burglar, he's a bad one. He's just sitting there, staring at me in shock."
    oliver "Who're you?"
    
    show izaac headscratch laughing
    $ renpy.transition(dissolve, layer='master')
    play sound "sfx/key_jingle.ogg"
    "He lifts a pair of keys from the table and jingles them in front of me."
    play music "music/papercookies.ogg" fadein 2.0
    izaacu "Your new roomie!"
    show izaac headscratch grin
    $ renpy.transition(dissolve, layer='master')
    "He seems a little more excited about this than I am about it. First of all, he looks like the typical high-school douche."
    "Second of all,{w=0.2} he just looks like a typical douche. Dumb beanie hat, sports jersey - I'm not having a good feeling about this. I'll have to do something or this new living arrangement will become a nightmare."
    "I'm not going to let this guy think I'm a pushover."
    "He turns his focus away from me and back to my TV. He's watching some sports game, looks like football or something."
    "I stand in front of the television."

    show izaac handspockets smirk
    $ renpy.transition(dissolve, layer='master')
    oliver "I want to set some ground rules right now."
    "As sad as it sounds, I'm channeling my mom right now. Arms folded, stone-serious expression on my face. The new guy is trying to look around me, but he'll have no luck. My TV's not that big."
    show izaac handspockets smirk eyesclosed
    $ renpy.transition(dissolve, layer='master')
    izaacu "My name's Izaac, nice to meetcha."
    "Wha-? I'm not letting him change the topic by ignoring me."
    oliver "First of all, food. I'm going to organize the fridge and you're not going to touch any of my food."
    "As it is, he's eating what I planned to have for dinner tonight. Leftovers I had brought home from work earlier in the week. Good food that is now in the stomach of some jerk I don't even know."
    "He doesn't seem to be paying any attention, instead focusing on finishing off the rest of my food."
    play sound "sfx/food_grab.ogg"
    "I snatch it away angrily."

    show izaac shrug surprised
    $ renpy.transition(dissolve, layer='master')
    izaac "Hey! I was eating that."
    oliver "Yeah, my food. That I paid for."
    show izaac frown
    $ renpy.transition(dissolve, layer='master')
    izaac "Dude, I was hungry! You weren't around to help me move in, so I figured it'd be cool if I ate something from the fridge to make up for it."
    "My eyes narrow at his logic. No one even told me you were coming, how is that my fault that I couldn't help?"
    oliver "Food is going to be separated. If I find any of my food missing, I expect you to pay me back for it."
    oliver "And while I'm mentioning money, you're to leave your half of the rent on the table before rent is due. If you start missing rent, I'm going to have the landlord kick you out and find someone else who will pay rent."

    show izaac headscratch frown
    $ renpy.transition(dissolve, layer='master')
    izaac "Jeez man, why're you being such a dick?"
    oliver "How would you feel if you found some guy you don't know in your home, eating your food?"
    show izaac headscratch surprised
    $ renpy.transition(dissolve, layer='master')
    izaac "I'd probably be cool with it."
    "Good to see he understands the basics of empathy. Why would anyone be okay with something like that?"
    oliver "Not when it's the only thing in your fridge to eat."

    show izaac grin
    $ renpy.transition(dissolve, layer='master')
    izaac "Oh, don't worry 'bout that. I'm gonna be buying plenty of meat and protein stuff tomorrow. I noticed how empty your fridge is so I figured I'd help a bit."
    izaac "You can have whatever you want of my food, I don't mind sharing."
    "His smile almost makes me feel bad, which is what I'm sure he's trying to do."
    oliver "Doesn't do me any good tonight, while I'm hungry."

    show izaac shrug smirk eyesclosed
    $ renpy.transition(dissolve, layer='master')
    izaac "I'll just order some pizza then. How's that sound? We can go halfsies on it."
    oliver "Or you can pay for the pizza and treat me to it because you ate my dinner."
    show izaac shrug smirk eyesclosed
    $ renpy.transition(dissolve, layer='master')
    izaac "Fine by me! Mind if I{nw}"
    show izaac shrug smirk
    $ renpy.transition(dissolve, layer='master')
    extend ", uh, go back to watching the game?"
    oliver "Not yet. No parties or loud music at night. No chicks overnight, either. I'm not going to be kept up all night when I have classes in the morning."

    show izaac smirk
    $ renpy.transition(dissolve, layer='master')
    izaac "Got it, got it. Game?"
    "I wait a moment before moving out of the way."
    stop music fadeout 2.5

    oliver "Have I met you before?"
    "He looks a little familiar."
    show izaac headscratch surprised
    $ renpy.transition(dissolve, layer='master')
    izaac "I don't think so? A lot of people remember me from this year's orientation though. Are we in the same graduating year?"
    "When he says orientation, it clicks. I know why he seems familiar. When they announced a new building and grounds for sports, he made a huge deal out of it and nearly got thrown out."
    "He was in the same row as me, but further down. Even though he wasn't sitting next to me, I was embarrassed just to be in the room with him."
    "Now he's living with me. My earlier fears are slowly being confirmed."
    oliver "I've got homework and studies to do, so try to be quiet if you decide to freak out about your sports stuff."
    
    scene bg apartment bedroom with dissolve
    play sound "sfx/door_close.ogg"
    "I close myself into my room, grabbing a pair of headphones from nearby. Might as well listen to some music to help me focus on my classwork."
    "Accounting homework, history homework and a small assignment from business and financial mathematics."
    "Not too overwhelming, but boring as hell. I'd much prefer to surf the internet or play a video game. My computer sits in front of me on my desk, off..."
    "I have to resist the temptation. I can't go ruining my last chance so soon. I need to focus."
    "At least I have pizza to look forward to."
return
