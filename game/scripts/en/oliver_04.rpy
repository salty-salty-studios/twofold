label scene_1S4_en:
########################
    # Act 1, Scene 4
    # Capital C
    scene bg hallway 1 with dissolve
    window show smoothDissolve
    play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 1.5
    play music "music/handholding.ogg" fadein 2.5
    "According to the room number on my piece of paper, the art course is just down the hall. Probably a few doors further from where I stand in the hallway."
    "I approach the door, hesitating a little at the handle. The people in this class are all probably part of some weird, artsy hipster clique.\nAnd I'll be the outsider, like always."
    "Heat flushes from my skin, but I grab hold of the door handle. GPA, failure, bills... remember that, Oliver. What's worse? Flunking out of a community college and being broke or being exposed to a group of judgmental people?"
    "I decide the latter is more bearable in that context and push open the door."
    stop ambiance fadeout 1.5

    scene bg classroom art with dissolve
    "Oh, damn it."
    "As per my usual luck, all of the tables in the back of the room are filled. Wonderful. There's one thing I hate and it's entering a class to be the last one to arrive."
    "Everyone's staring at me. I bet they're taking me apart in their head, reassembling me into a different person with all of their incorrect preconceptions.\nIn return, all I have to greet them with is a scowl."
    "Scanning the room quickly, I see an empty table, smack dab front and center. Exactly what I want."
    "To be as noticeable as possible to the professor when I'm new and know nothing about this course."
    "I heave a hapless sigh and drag my feet towards my new seat. Flipping open my notebook, I might as well doodle a little and try to seem like I fit in while I wait for class to start."
    "While I'm sketching dumb little things on notepad paper – like myself looking grumpy – I hear the sound of a chair being pulled out beside me. Someone's deciding to sit next to me."
    "I keep my head down, but in my periphery I notice them doing a double-take."
    "Great.{w=0.5}\nWonderful.{w=0.5}\nBeautiful."
    "As if lowered head and my generally discontent appearance wasn't enough of a hint, the person sitting next to me won't ignore me. Maybe this is how Wallace felt just a little while ago."
    "Either way, whoever you are; please go away."
    "Please, just go."
    scene cg caprice intro
    $ renpy.transition(dissolve, layer='master')
    "I decide to risk a sideways glance."
    "I can just make out brown hair and... a top hat? Who even wears a top hat anymore? Looking a bit closer, I can barely see a female's chest under their shirt."
    scene cg caprice intro notice
    $ renpy.transition(dissolve, layer='master')
    "My eyes scanning upwards are met by another pair of brown eyes."
    "I lock up for a brief moment and immediately glance away.{nw}"
    scene bg classroom art
    $ renpy.transition(dissolve, layer='master')
    extend " Oops. Class has already started and I'm already making a fine mess of things."
    "While I don't like people, I have an especially bitter spot for women.\nI've had some awful experiences with them and it always ends up with me being an ass or a blundering moron."
    "Odds are she'll end up making a comment about where my eyes just were and I'll respond like an ass and my first day in class will be involve an argument with some dumb girl wearing a top hat."
    "Luckily, not a moment before I end up saying something stupid, the professor enters the class. The girl turns away from me and towards the professor moving towards his desk at the front of the room."
    professor "Hello, class. I hope you're all looking forward to this coming semester in the Character Art Creation workshop. First thing we'll be doing is going over the syllabus."
    "The professor passes a chunk of the stack of papers to each desk at the front.\nEach student takes one and passes the syllabus to the back and around until everyone has a copy."
    professor "In this class, we're going to be focusing mainly on how to draw a character, in a variety of styles. Along the way, we'll learn things {fade=100,35}about perspective, lighting, proportions, muscle tone..."
    "Our professor paces along the front of the class, explaining facts on the sheet of paper, what the course is all about – but I can't seem to pay attention."
    "Am I the only one who finds it strange that our professor has a Fu Manchu goatee?"
    "Top hats, peculiar facial hair... I knew art people were weird, but I feel like this class is setting a new standard. I'm afraid to take a closer look at the rest of this class or I fear that I'll see something stranger."
    "Interrupting my thoughts, I feel a piece of paper being edged into my arm repeatedly from my left."
    "I look up towards the offender, the strange female with the stranger hat. This time, I get a better look at her."

    # Cue the Caprice CG!
    scene cg caprice intro smirk with dissolve
    "Brown hair and fiercely focused brown orbs greet me. The girl grins at me for a moment, continuing to jam the paper into my arm on the table's surface until I take it."
    "It's a little crumpled now, but I flatten it out. I'm a little worried that she's going to chew me out for earlier, but I guess I'll take my chances."
    "{nw}"
    window hide
    # After CG, show Caprice sprite
    scene bg classroom art with dissolve
    show note caprice intro with moveinbottom
    $ renpy.pause()
    #cap "| HEY! HI! I NOTICED YOU WERE LOOKING A LITTLE PALE. EITHER YOU'RE NERVOUS OR YOU DON'T GET ENOUGH SUN. IF IT'S JUST NERVES, DON'T WORRY ABOUT IT! EVERYONE HERE'S REALLY NICE. MY NAME'S CAPRICE, HOW ABOUT YOURS? |"
    window show dissolve
    "I... what? I'm not pale."
    "Narrowing my eyes at the paper, I discreetly pull back my sleeve a little."
    "Okay, so maybe I am."
    "I'm not sure whether I should be taking this as an insult, or if she's just really direct. Rereading the paper, I try to figure out if there's some kind of underlying motive here. Who just comes out of nowhere and talks to someone they barely know?"
    "I really don't want to respond to this note, but I can feel Caprice staring a hole into the side of my head. I'm not sure what's worse, the uncomfortable pressure of being stared at or the fact that I have to respond in order to satisfy this Caprice girl."
    "Eventually I decide that I'm not going to deal with this. I have better things to do than be insulted by some random girl."
    "More than anything, I need to pay attention so I can decide if this is the class I should take."
    hide note
    $ renpy.transition(moveoutbottom, layer='master')
    "I crumple the paper into a ball and make my way over to the garbage barrel as inconspicuously as I can. However, when I return, Caprice seems to have commandeered my notebook."
    "Sitting down, I'm not sure what to do. I'm right in front of the professor and this girl is busy scribbling in my notepad. It's not like I can snatch it back without being apparent."
    "Eventually, it gets plopped down in front of me."
    "{nw}"

    window hide dissolve
    show note caprice notnice with moveinbottom
    $ renpy.pause()
    window show dissolve
    #cap "| THAT WASN'T NICE! LOOK, I'M SORRY IF I SAID YOU WERE PALE AND IT BOTHERED YOU, BUT YOU ARE! ARE YOU FEELING SICK? I MADE A LITTLE DRAWING IF IT MAKES YOU FEEL BETTER. |"
    "Like she says, there's a little sketch in pen that I can only assume is supposed to be herself, holding a piece of paper or something that reads 'I'M SORRY!'."
    "I guess I'll ignore it this time and scribble back a response. Maybe she means well,\nbut I took it the wrong way. I know I've done that before."
    "I remove the piece of paper from my notebook when the professor is facing away from the class and start writing a response."
    "{nw}"

    window hide dissolve
    show note caprice notnice with moveinbottom
    $ renpy.pause(1.5)
    show note oliver intro with longDissolve
    $ renpy.pause()
    #oliver "| The drawing didn't help much, but thanks. I'm just a bit nervous. Not much of an artist, but I wound up in this class to get enough credits to pass. By the way, I'm Oliver. |"
    hide note with moveoutbottom
    window show dissolve
    "I wait until the professor looks away and I slide the piece of notebook along the shared table towards Caprice."
    "I'd like to pay attention to the professor and his introductory lecture, but my mind's wandering. Why am I even bothering to talk to this girl? I should've just kept ignoring her, I'm sure she'd have stopped staring eventually..."
    "Caprice opens the note while the instructor turns his back to us to write something on the whiteboard. Without a second of hesitation, she scribbles on the paper furiously."
    "Judging by how excitedly she's writing, I feel that responding was a bad idea."
    "I somehow doubt anything good can come of this person. She practically falls out of the sky, calls me pale and looks a few centuries behind in her headwear fashion."
    "Then again, I guess the openness is refreshing. She isn't afraid to speak her mind, like I usually am. I could admire that."
    "But the operative word is 'could'."
    "However, the reality is I don't admire it, because everyone seems to think 'Kick the Oliver' is a fun game."
    "Notebook being jammed{nw}"
    $ renpy.transition(hpunch, layer='master')
    extend " into my arm again, I take it and open it without being detected. Then again, would this professor even care if I'm reading notes in class?"
    "Although this note-passing is done half-begrudgingly, it {i}is{/i} sort of fun.\nIt's like we're spies, or something."
    "Passing secret messages back and forth, under the nose of the enemy."
    "{nw}"

    window hide dissolve
    show note caprice nicemeetingya with moveinbottom
    $ renpy.pause()
    hide note with moveoutbottom
    window show dissolve
    #cap "| NICE TO MEET YOU, OLIVER! YOUR NAME'S A BIT DRAB FOR MY TASTE, BUT I WOULDN'T TELL YOU TO CHANGE THAT! SHAME YOU'RE ONLY HERE FOR THE CREDITS, THOUGH. ART IS THE BEST! MAYBE WE SHOULD HANG OUT SOMETIME? THAT WAY I CAN PROVE IT TO YOU! |"
    "At first, I gulp hard. A girl asking me to hang out with them?\nThat's never happened before. Not without ulterior motives."
    show note caprice nicemeetingya with moveinbottom
    "I doubt she has any positive reasons for inviting me to hang out with her.\nPlus, there she goes again with the insults. Does she even realize she's doing that?"
    "Considering her tone, it almost feels like she thinks it's okay. My eyes narrow at the note. This is starting to get annoying."
    "Thank goodness this isn't a verbal exchange or I'd have choked at some point and make a fool of myself. Maybe I'll try my hand at a little bit of Caprice-bluntness this time."
    "{nw}"

    window hide dissolve
    $ renpy.pause(1.5)
    show note oliver dumbhat with longDissolve
    $ renpy.pause()
    hide note with moveoutbottom
    window show dissolve
    #oliver "| Yeah, well your hat is dumb. I don't know you and you don't know me, so I'm going to pass on that offer. Might be better that way, considering you're either actually insulting my name or that's one of the worst puns I've ever heard. |"
    "I close the notebook and carelessly slide it across the table towards her. Opening it, she grins maniacally. She reaches into the bag resting beside her chair and fetches a marker."
    "It's big and red. With a sharp pop of the marker's cap, she writes something large across the note. Capping it again with equal enthusiasm, she switches back to the soft teal pen she was writing in before."
    "The notebook is passed back to me. How can she even have anything to say at this point? I open it if only to see what sort of response she has."
    "{nw}"
    stop music fadeout .75
    window hide dissolve
    show note caprice rude with moveinbottom
    $ renpy.pause()
    window show dissolve
    play music "music/capitals.ogg" fadein 1.25
    "The note has the word 'RUDE' written in bright red ink over the entirety of my last message."
    "Rude?"
    "No. You're rude! You're rude and you're wearing a top hat! A top hat!\nWho wears one of those unless they're looking for attention?"
    "I swallow my frustration, trying to let the heat under my collar vent before continuing to read the rest of the note."
    window hide dissolve
    $ renpy.pause()
    window show dissolve

    #cap "| WELL, IN THAT CASE, I'LL HAVE TO RECONSIDER OFFERING TO HELP YOU PASS THIS CLASS. I MEAN, THAT'S ALL YOU'RE HERE FOR, RIGHT? |"
    "This gets my attention and actually makes me speak out loud."
    oliver "What do you mean?"
    "I didn't mean to speak because immediately, the instructor hears us.\nTurning towards us both, he tugs a little on the corner of his 'stache."
    hide note
    $ renpy.transition(moveoutbottom, layer='master')
    professor "Caprice, please stop taking the new art student's focus away from the class."
    "I'm a little surprised he immediately places the blame on Caprice. Does she do this often?"
    "Looking up, I then realize most of the class' eyes are trained on me."
    "Oh, please no."
    "I feel myself retracting into my cargo vest at everyone's stares.\nThen, almost like an atom bomb, the person beside me takes all the attention."
    $ renpy.transition(hpunch, layer='master')
    caprice "{size=28}{b}Sorry! I couldn't help it! I promise it won't happen again, Professor!{/b}{/size}"
    "I'm nearly blasted out of my chair. Where in the world is her volume control?\nI didn't have really any expectations of her voice, but something with the force of a jet-engine certainly was not first on my list."
    professor "Alright, Caprice. No need to shout, just talk after class, please."
    caprice "{b}Can do, professor!{/b}"
    "He winces a bit at the fact that the equivalent of a sonic boom is being directed at him."
    professor "Now, back to what I was saying..."
    stop music fadeout 3
    "It seems Caprice is done writing notes for now. It's... almost a shame. I'm sort of interested in an easy way to pass a class and get the credits I need to stay enrolled."
    "I try to listen to the professor, but it's all uninteresting stuff. Things like the foundations of art, the notable early artists, those who pioneered the artistic trade."
    "This is probably why I'm flunking out of a community college. I can barely pay any attention to any of this."
    "Thankfully by the next time I look up from my paper and mindless doodles, it's because the students are leaving and class is over for the day. Time flies when you're zoning out, I guess."
    "To my side, Caprice has already left. That's probably a good thing.\nShe sounds like more trouble than she's worth."
    "I pack up my things and sling my bag over my shoulder, heading towards the door."
    "Better to not get caught up in things against my will, anyways."
    
    scene bg hallway 1 with fade
    show caprice hattip smile eyesclosed mouthopen
    with dissolve
    play music "music/caps.ogg" fadein 0.75
    caprice "{b}Hi!{/b}{nw}"
    $ renpy.transition(hpunch, layer='master')
    extend " "
    "I flinch a little as I exit the door. Guess I spoke too soon. The walking volume hand-grenade was waiting for me."
    oliver "Oh, uh...{w=0.2} hey.{w=0.2} Caprice.{w=0.1} Sorry for getting you in trouble back there, {fade}I guess."
    show caprice wave smile mouthopen eyesclosed
    $ renpy.transition(dissolve, layer='master')
    "With one hand on her hip, she angles the other outward, giving a dismissive wave."

    caprice "Happens all the time! Not your fault. Used to happen at least once every week last year. I think the professor is used to it by now."
    show caprice hattip smile mouthopen eyesclosed
    $ renpy.transition(dissolve, layer='master')
    "She's as loud as she was in class. I'm beginning to think I really ought to run or at least try and sneak away while the conversation remains at an awkward moment where neither of us have anything to say."
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    caprice "{b}So!{/b} Are you still interested in my offer?{nw}"
    show caprice hattip wink
    $ renpy.transition(dissolve, layer='master')
    extend " Huh, are ya? {b}Are ya?{/b} C'mon, tell me!\nWanna learn the secret to passing this class?"
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    "Of course, now I'm locked into furthering the conversation by responding. Can I please go home yet? I'd like to just get my classes over with, go home and play some video games or something..."
    "Then I'm reminded that I still have a few more classes today to deal with."

    show caprice hattip attacked
    $ renpy.transition(dissolve, layer='master')
    caprice "{b}{fade=10,100}Hey! Wake up, pay att{/fade}ention!{/b} Oliver, right? C'mon, snap out of it! Want me to help you pass this class like a pro?"
    oliver "I- I mean, I suppose. How are you going to help me?\nThis isn't going to get me in trouble or anything, right?"
    show caprice hattip smile eyesclosed mouthopen
    $ renpy.transition(hpunch, layer='master')
    "A blast of laughter, like a cannon to the face."
    caprice "You won't get in trouble, promise!"
    oliver "...But how are you going to make sure I pass?"
    show caprice shrug smile
    $ renpy.transition(dissolve, layer='master')
    caprice "It won't be any fun if I just {b}TELL{/b} you, Oliver! Don't be so drab."
    "She's using that word again and dons a smile."
    "Oh, you little top hat wearing-"
    "Relax, Oliver."
    show caprice handsbehindback smile
    $ renpy.transition(dissolve, layer='master')
    caprice "If you {b}REALLY{/b} want to know, why don't you come to room 257 sometime this week?\nI won't say much other than there's a bunch of people there who can help you."
    "With that, {nw}"
    show caprice at flip('caprice hattip smile'):
        xpos 0.5
        yoffset 0
        time 0.8
        parallel:
            linear .75 xalign 0.8
        parallel:
            linear 1.0 alpha 0
    extend "she turns and bounds away, hand on her top hat to prevent it from blowing off of her head."
    hide caprice

    "As she hops down the hallway, I can't help but liken her to some kind of over-energized rabbit wearing a stupid hat. Along the way, she nearly topples over a few people, but they manage to stay standing."
    stop music fadeout 2.5
    "Well... that was something."
    "With the unusually loud girl gone, I can finally focus on other things. Personally,\nI'm glad that's over. I start walking towards my next class until something on a nearby corkboard catches my eye."
    "{nw}"

    window hide dissolve
    show misc artposter with dissolve:
        ypos -40
        xalign 0.5
    $ renpy.pause()
    window show dissolve
    "It's a rather aesthetic display of blue and light colors, with a certain style to it. Minimalistic, I guess?"
    "After reading over it, I realize this club is why she'd invited me to that particular room. Her idea of helping me with art would be to hang around her art club?"
    "Anyways, why did she keep it a secret from me if she has big, noticeable advertisements for her club on the walls of the school...?"
    "I look down to my watch. I'd go scout out the club if I didn't have class right after this one."
    "Hopefully this one is a little less... {i}loud{/i}."

    window hide dissolve
return
