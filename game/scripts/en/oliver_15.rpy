label scene_1S15_en:
#######################
    # Act 1, Scene 15
    # The Price of Dignity
    call switch_scene_s('bg library', 'bg hallway 1')
    play music "music/hopskipjump.ogg" fadein 2.5

    "As I'm leaving my class, I'm greeted by{nw}"
    show tanya smirk:
        xanchor 0.5
        xpos 0.9
        yoffset -120
    $ renpy.transition(dissolve, layer='master')
    extend " that little brown girl again."
    tanya "Hey."
    "I ignore her, but she just greets me with some sort of shit-eating grin.{nw}"
    show tanya:
        ease 0.8 xpos 0.7
    extend " I try to sidestep her, but she moves in the way."
    tanya "Mekki's really lookin' forward t'ya going to the club meeting today."
    oliver "Okay."
    show tanya:
        ease 0.8 xpos 0.5
    "Tanya takes another step into my path and I can feel a restless sigh already trying to fight its way out of me."
    oliver "I need to go."
    tanya "Where?"
    oliver "Home, mostly."
    show tanya hmm
    $ renpy.transition(dissolve, layer='master')
    tanya "What, when ya got some girl whinin' and sighin' that she doesn't think you're gonna go to her club? She keeps going on about wanting to help out, so why not just go?"
    tanya "Home can wait until after the club meeting."
    oliver "And if I don't go?"
    show tanya grin
    $ renpy.transition(dissolve, layer='master')
    tanya "I could drag ya. Do you want that? I'm pretty strong."
    "Yes, absolutely. Of course I want to be known as the guy who got dragged by a small girl half his height. You got me."
    oliver "I doubt you can drag me anywhere. I weigh more than you by a long shot, probably."
    show tanya grin eyesclosed
    $ renpy.transition(dissolve, layer='master')
    tanya "I can bench my own weight comfortably. I've maxed out at almost two hundred."
    "Well, crap. Really? I mean, her arms don't look that ripped, but they do definitely look toned. Considering how easily she got me off my feet the other day, maybe she isn't lying."
    oliver "Uh, why?"
    show tanya pumped
    $ renpy.transition(dissolve, layer='master')
    tanya "Do you know how heavy metal is? I'm barely five feet tall. If I'm gonna be able to do what I love, I gotta lift."
    oliver "What is it that you're doing, anyways? You nearly scared the life out of me with that welder's getup the first time I saw you."
    show tanya smile
    $ renpy.transition(dissolve, layer='master')
    tanya "Metal fabrication. I like to do a bit'a blacksmithing in my spare time, too. This school's got a few courses in it. I went to a trade school, but these certification courses will be handy when I go job huntin'."
    oliver "Oh. You don't write?"
    show tanya smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    tanya "Nope, just like hangin' around the club. Known Mekki for a while. Took a class with her once."
    oliver "So, I guess I'm going to that club meeting, then."
    show tanya pumped
    $ renpy.transition(dissolve, layer='master')
    tanya "Damn right y'are."
    "She aims a thumb to the right."
    tanya "Get goin'."
    stop music fadeout 2.5

    window hide dissolve
    scene black with dissolve
    play sound "sfx/door_open2.ogg"
    scene cg writingclub intro with wipeleft:
        subpixel True
        xalign 0.5
        yalign 0.5
        ease 1.5 xzoom 1.1 yzoom 1.1
    window show dissolve
    play music "music/mek.ogg" fadein 1.5
    show tanya smile:
        ypos 1000
        xanchor 0.5
        xpos 0.1
    show mekki smile:
        ypos 1000
        xanchor 0.5
        xpos 0.8
    "Entering the club room is a bit more daunting, because I have no excuse to be here. Nothing's being held ransom, except my dignity."
    "I'm a bit shocked at the genuine excitement on her face when she sees me enter the room. I can't say anyone's ever glad to see me, except for the guy I'm coming in for at work, or my mom."
    tanya "On the way back from the bathroom, I found the new guy! Figured I'd walk with him back to the club."
    "She approaches me, still wearing that huge smile."
    mekki "Welcome to the writing club, Oliver."

    scene bg classroom writing with dissolve:
        xalign 1.0
    "Gently, she takes a corner of my sleeve in her hand and tugs it towards the front of the class."
    show mekki left handstogether smile eyesclosed:
        xanchor 0.5
        xpos 0.3
    with dissolve
    mekki "These are the rules of the club. They look complex, but it's really all just common sense."
    "She's right, the rules are pretty elaborate. When you simplify them, most of it is just \"don't be rude\" or \"don't be an asshole to others\". There's also a line that encourages others to talk to club officers about conflicts and to suggest improvements for the club."
    "I wonder if they used to have a problem with people like that in the past?"
    "I'll be honest, I'm kind of a piece of shit from time to time. I hope I don't end up, well, incurring some sort of crazy wrath by being an unintentional jerk. I mean, if Tanya's as strong as she says and is a good friend of Mekki's – well, maybe she's the bouncer or something."
    "Why are community colleges so weird?"
    show mekki left handstogether smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Don't worry if you do something that goes against one of the rules, we always give more than one chance."
    "Well, at least that's sort of relieving."
    mekki "Our meetings are really relaxed. If people want to write, they can. If not, they're free to hang around and chat with other writers."
    show mekki left handstogether pfah
    $ renpy.transition(dissolve, layer='master')
    mekki "I usually help people with ideas or proofreading if possible, and sort their writing by genres and such in a big filing cabinet."
    "She motions towards a large filing cabinet on wheels in the corner of the room."

    show mekki left handstogether
    $ renpy.transition(dissolve, layer='master')
    mekki "Everyone's writing either gets photocopied or printed and put in there. People are allowed to go back and read theirs or others' work; I usually laminate them to make sure it's preserved."
    oliver "Sounds... pretty thorough. Do you want to be a librarian or something when you're done here?"
    show mekki left giggle laughing
    $ renpy.transition(dissolve, layer='master')
    "Mekki laughs, like that's a silly idea for a writer."
    show mekki left giggle smile
    $ renpy.transition(dissolve, layer='master')
    mekki "No, I'm actually a pre-law student."
    "Oh. Well, pat on the back to me. I didn't think I was actually right about her major. That explains her attire, but not her attitude."
    mekki "I just think writing is a fantastic hobby and I want to make sure everyone who starts and wants to share, can."
    oliver "Interesting, {fade}I think..."
    mekki "So, do you want to try your hand at it?"
    oliver "At, uh... what?"
    show mekki left thinking starryeyed
    $ renpy.transition(dissolve, layer='master')
    mekki "Writing! It's easy to start, I promise. I'll help, if you'd like."
    oliver "I don't know. I don't really have any \"good ideas\"."
    show mekki left thinking smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "That's fine, I can bounce some off of you and anything that you like you can change, rearrange, remix, whatever you like."
    "Compared to how meek she was earlier in the library and even further back in class, she almost seems like a different person."
    show mekki left thinking frown
    $ renpy.transition(dissolve, layer='master')
    mekki "C'mon, you came all the way out here, I might as well help you write something."
    oliver "Fine, fine. I'll try. Caprice made me draw, so I guess it's fair if I try to write something. The practice will help me understand the classes better."

    show mekki left handstogether starryeyed
    $ renpy.transition(dissolve, layer='master')
    mekki "Wonderful! Alright, so what kind of genres do you like? Did you read any of that mystery novel I gave you?"
    "Bits and pieces, but I don't want to tell her I'm at most maybe on page ten."
    oliver "Some, yeah... I've been trying to keep up with studies."
    show mekki left handstogether smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "I can respect that. So, do you like mysteries? We could try some kind of murder mystery, or something a bit more unreal if you want to avoid complicated plots."
    oliver "I like mysteries, but I think it might be easier for me to do something a little more on the surreal side. Like scary movies with ghosts and stuff. No one asks for an explanation, they just go along with it."
    "Mekki's excitability makes her look like she's going to burst right out of her head if I keep talking."
    "So I stop."

    show mekki left handstogether
    $ renpy.transition(dissolve, layer='master')
    mekki "But!{nw}"
    show mekki left thinking smile
    $ renpy.transition(dissolve, layer='master')
    extend " There's a thing about that, people accept it because the writer keeps things within a boundary of what's \"believable\"."
    show mekki left thinking smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "Immersion. Immersion is the key, really. What would you believe in something you read? Start with that for your baseline."
    show mekki left thinking smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Then think about it, what would I believe? Or someone else you know? Apply a little empathy and try to think from another person's perspective. You'll be able to start finding ways to make an idea that wouldn't be accepted in reality, accepted in fiction."
    "Empathy, huh? That's something I'm in short supply of. I don't get why she's so hyped up about this writing crap, or why Tanya had to be so insistent on dragging me here."
    mekki "Do you have any ideas? A murder thriller? Something supernatural? Psychological?"
    oliver "Uhhhh..."
    oliver "Honestly, you've got me. I've never been an exceptional idea guy."
    "She doesn't seem dissuaded by this, though. She's slipping from uncharacteristically bubbly into the quiet, thinker-type I guessed she was when I met her."
    show mekki left thinking hmm:
        ease 1.5 xpos 0.2
    stop music fadeout 2.5
    mekki "Alright, well how's this for an idea:"

    play music "music/fauxhorror.ogg" fadein 1.5
    show misc mekki story 1 as ms1:
        xanchor 0.5
        xpos 0.65
    $ renpy.transition(dissolve, layer='master')
    mekki "A young man is heading back home from his classes after they've ended."
    show misc mekki story 2 as ms2:
        xanchor 0.5
        xpos 0.65
    $ renpy.transition(dissolve, layer='master')
    mekki "On the way, he stops at a local convenience store. He's buying something, {w=0.1}a snack, {w=0.1}a drink."
    show misc mekki story 3 as ms3:
        xanchor 0.5
        xpos 0.65
    $ renpy.transition(dissolve, layer='master')
    mekki "Either way, one of the dollar bills he gets has a phone number on it. Out of pure boredom, he calls it."
    show misc mekki story 4 as ms4:
        xanchor 0.5
        xpos 0.65
    $ renpy.transition(dissolve, layer='master')
    mekki "All he gets is static until eventually the phone hangs up with a loud click."
    show misc mekki story 5 as ms5:
        xanchor 0.5
        xpos 0.65
    $ renpy.transition(dissolve, layer='master')
    mekki "After that, a lot of strange things start to happen. He starts seeing things, people act weird around him."
    show misc mekki story 6 as ms6:
        xanchor 0.5
        xpos 0.65
    $ renpy.transition(dissolve, layer='master')
    mekki "Electronics don't work properly when he uses them. TV, lights, only his phone works, but it works in strange ways."
    show misc mekki story 7 as ms7:
        xanchor 0.5
        xpos 0.65
    $ renpy.transition(dissolve, layer='master')
    mekki "His contact list is replaced with names of people he doesn't know. Maybe other people who also called the number. They're his only way to figuring out how to \"escape\" what they also accidentally started."
    mekki "Perhaps something is following him now. Whatever distributed the number."
    mekki "The rest of the story...{w=0.1}{nw}"
    hide ms1
    hide ms2
    hide ms3
    hide ms4
    hide ms5
    hide ms6
    hide ms7
    show mekki left thinking smile
    $ renpy.transition(dissolve, layer='master')
    stop music fadeout 2.0
    extend " is up to you."
    play music "music/mek.ogg" fadein 1.5
    "That's... actually pretty interesting. She just came up with that, too."
    mekki "Feel free to start playing with that idea, or an entirely different one if you'd like. I'm going to go around and see how everyone else's writing or ideas are coming along."
    show mekki at pflip('mekki smile'):
        xanchor 0.5
        xpos 0.2
        time 0.8
        ease 1.5 xpos -0.2

    "Unlike Caprice, who spent her time drawing during the club, Mekki is actively going around and helping anyone she can with their work."
    "Not sure if that actually means anything, considering Caprice did that after she was done drawing."
    "Whatever, I'll just focus on trying to write something."
    "What about making the character believable? How do I even write a character?"
    "I start scratching my head. I've never really done this sort of thing. I hardly have examples to go by. I just have a story idea that Mekki gave me."

    darrenu "Need some help?"
    "I don't look up from the empty notebook page I have in front of me."
    oliver "No, not yet. I just have to think a little."
    show darren hmm with dissolve
    "...Who is this pretty-boy?"
    darrenu "Couldn't help but overhear Mekki giving you ideas. Have you ever written before?"
    oliver "No. But I think I can figure this out, thanks."
    "Whether I can or not is pretty obvious, but I don't really want his help. Whatever help he might lend is probably just thinly-veiled pity, and I don't need any more of that than I'm already getting."
    "What's he even doing here? Maybe he's some popular guy trying to get in touch with his \"nerdy side\" or something."
    show darren smile
    $ renpy.transition(dissolve, layer='master')
    "...Why is he smiling at me?"
    darrenu "What's with the hostile tone?"
    oliver "Not being hostile, I just don't want help."
    darrenu "From me. You seem willing to accept help from the cute girl, however."
    oliver "That has nothing to do with it."
    show darren smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    darrenu "Right. Your defensiveness only reaffirms my suspicion."
    darrenu "See, Mekki told us you need help with your writing for a class. You're willing to receive help, and apparently need it, but are unwilling to accept it from me."
    darrenu "So, logic dictates that you don't want help from me.{nw}"
    show darren smile
    $ renpy.transition(dissolve, layer='master')
    extend " Why?"
    "I don't feel like having my \"logic\" dissected by you, thank you very much."
    oliver "What are you even doing here?"
    darrenu "Writing? This is the writing club, I'm pretty sure."
    oliver "You don't seem like a writer."
    darrenu "Neither do a lot of people here, which is why I like it. I'm Darren, by the way."
    "He extends a hand, which I don't shake. I need to come up with how to write this story."
    darren "I guess you don't like that answer?"
    oliver "Too convenient. I don't think you're here just for the writing."
    show darren hmm
    $ renpy.transition(dissolve, layer='master')
    "He taps his chin a few times."
    darren "What makes you think that?"
    oliver "A hunch."

    darren "Well, I guess I'll be open about it then. I guess it's because I sort of have an issue with women."
    oliver "...Oh?"
    "Somehow I don't think it's the same kind of problem that I have with women."
    show darren worried
    $ renpy.transition(dissolve, layer='master')
    darren "You see, I have something like a fan club. That'd be the proper thing to call it."
    darren "In reality, they're like six or so stalkers who have been following me around campus since I enrolled here."
    darren "I ran into Mekki while I was hiding in the library and told her about my problem. She asked if I liked to write, which seemed incredibly out of place at the time. I told her I used to, but stopped."
    darren "She told me to join the club, start writing more and she'd take care of the problem for me. This place has turned out to be a safe haven for me. They once barged into the room after Tanya stiff-armed them in the hall."
    darren "Everyone got between them and me while someone called campus security. Tanya dragged two out, one headlock per arm. Mekki managed to push a few of them out, too."
    "Well, I guess Tanya being tough as nails wasn't a joke. I'm a little surprised that Mekki got into it, though."
    oliver "So, wait. Let me get this right."
    oliver "You're hiding here because women find you so attractive, that they form a fan club in which they desperately stalk you?"
    show darren hmm
    $ renpy.transition(dissolve, layer='master')
    darren "More or less."
    oliver "Yeah, I don't think I like you."
    show darren smile mouthopen
    $ renpy.transition(dissolve, layer='master')
    "Normally people don't laugh when I talk to them like that."
    darren "It's not exactly something to be envious of, but I guess I can see why you think otherwise. You probably look so sullen for a reason."
    show darren smile
    $ renpy.transition(dissolve, layer='master')
    darren "Maybe you should try writing a romance story?"
    oliver "I don't think I should, or it'll devolve into me projecting a ton of bitterness."
    show darren hmm
    $ renpy.transition(dissolve, layer='master')
    darren "So, what's the problem you're having right now with this story?"
    oliver "I'm not exactly sure how to write dialogue."
    darren "Like, how people talk, or how to present it in the writing?"
    oliver "A bit of both."
    show darren smile
    $ renpy.transition(dissolve, layer='master')
    darren "Dialogue is easy. At least, I think so. Think about what a character would say that's believable, then just wrap it in descriptors that show what they're doing."
    darren "And a big thing a lot of new writers do is tell, not show. You want to describe how they move, not tell the reader."
    darren "\"She picked up the phone\" versus \"Her hands trembled, reaching for the phone\"."
    show darren smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    darren "One sounds better than the other."

    show darren hmm
    $ renpy.transition(hpunch, layer='master')
    "I nearly crap myself as a half-dozen thick books are dropped in front of me."
    show bg classroom writing:
        xalign 1.0
        linear 1.5 xalign 0.4
    show darren hmm:
        yoffset 0
        ease 1.5 xpos 0.6
    show heather grin eyesclosed at mirror:
        xanchor 0.5
        xpos 0.25
    $ renpy.transition(dissolve, layer='master')
    heatheru "If you want to learn, learn from the best."
    darren "Here we go. Heather and her undying love for dusty old authors."
    "Oh. Is this girl what I thought Mekki was going to be like?"
    show heather smirk
    $ renpy.transition(dissolve, layer='master')
    heather "They're considered great for a reason, Darren."
    darren "Yes, because boring scholars as old as the books think so.{nw}"
    show darren smile
    $ renpy.transition(dissolve, layer='master')
    extend " Don't get me wrong, some old works are great,{nw}"
    show darren hmm
    $ renpy.transition(dissolve, layer='master')
    extend " but not exactly good to learn from in terms of modern writing."
    oliver "Can I just write? I don't want to spend an hour reading old crap or having explanations on how to write."
    show heather handoncheek smile
    $ renpy.transition(dissolve, layer='master')
    heather "A man after Mekki's heart, I take it. She's fond of the \"just write\" mentality, too."
    oliver "Why does everyone assume I'm trying to court Mekki?"
    mekki "I can hear you guys, you know."
    "The two ignore Mekki, and Heather addresses me."
    show heather handoncheek smirk
    $ renpy.transition(dissolve, layer='master')
    heather "Shouldn't you be?"
    oliver "Uh... no?"
    show darren worried
    $ renpy.transition(dissolve, layer='master')
    darren "He has confidence issues, anyways. I don't think he'd try even if he wanted to."
    show heather handoncheek skeptical mouthopen
    $ renpy.transition(dissolve, layer='master')
    heather "Oh, one of those sort of guys. Maybe Mekki likes them pathetic?"
    oliver "What the hell? I just want to pass my writing class. Can you both go away?"

    # Show Mekki
    show bg classroom writing:
        xalign 0.5
        ease 1.5 xalign 0.0
    show darren hmm:
        xanchor 0.5
        ease 1.5 xpos 0.85
    show heather at nflip('heather grin'):
        xanchor 0.5
        xpos 0.25
        ease 2.5 xpos 0.55
    show mekki left thinking frown:
        xanchor 0.5
        xpos -0.2
        ease 2.0 xpos 0.2
    mekki "It might be easier for him to concentrate if you did."
    show heather grin away
    $ renpy.transition(dissolve, layer='master')
    heather "So, are you interested in Mr. Penn?"
    mekki "Even if I was, I don't think that's relevant. He needs help passing his class and if you aren't helping, you should focus on your writing."
    "I didn't expect the words \"Even if I was\", to irritate me as much as they do."
    show heather grin eyesclosed
    $ renpy.transition(dissolve, layer='master')
    heather "It may be relevant. Maybe you're looking for your next romance novel's inspiration. He does fit some of the characters you've written about before."
    show mekki left thinking surprised
    show darren smile
    $ renpy.transition(dissolve, layer='master')
    "What?"
    show mekki left frown
    $ renpy.transition(dissolve, layer='master')
    mekki "Heather, you promised you weren't going to do anything to embarrass me today."
    "The playful grin on Heather's face contradicts her scheming appearance."
    heather "Why are you embarrassed?"
    show mekki left thinking frustrated
    $ renpy.transition(dissolve, layer='master')
    mekki "Am I going to have to ask you to leave?"
    show heather smirk
    $ renpy.transition(dissolve, layer='master')
    "Heather puts a smug smile on, like she won some sort of unspoken battle. Mekki as a result seems a bit more flustered than she should be."

    show mekki left thinking frown:
        time 0.8
        ease 2.0 xanchor 0.5 xpos 0.4
    with None
    show heather at flip('heather smirk'):
        easeout 3.6 xpos 1.1
    show darren at flip('darren smile'):
        easeout 2.2 xpos 1.15
    # Darren and Heather go away
    $ renpy.pause(3.0, hard=True)

    mekki "Sorry about that. Heather has a bad habit of... well, trying to get a rise out of me. I'd prefer you to not see that. It's unprofessional."
    hide heather
    hide darren
    oliver "Are you supposed to be a professional?"
    show mekki left thinking hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "Well, not exactly."
    oliver "Then don't worry about it.{nw}"
    show mekki left thinking smile
    $ renpy.transition(dissolve, layer='master')
    extend " Mind giving me a hand with starting this?"
    "If anything, I'd like to stay on her good side, even if it's as simple as keeping her mind off of one of her club's members harassing her a little. Mekki may be my ticket out of this problem, anyways."
    
    window hide dissolve
    stop music fadeout 2.0
    scene black with longDissolve
    "After a bit of coaching and some shown examples of what I should or shouldn't do, the story starts to come together. It's not extremely long, or finished, but I think I like it."

    scene bg classroom writing
    window show dissolve
    play music "music/scrappedstories.ogg" fadein 1.5
    show mekki handstogether smile away:
        xanchor 0.5
        xpos 0.5
    with dissolve
    $ renpy.transition(dissolve, layer='master')
    "As everyone's leaving, they hand in their work to Mekki, who briefly skims the work and then sorts it into several piles on her desk."
    oliver "Why're{nw}"
    show mekki handstogether smile
    $ renpy.transition(dissolve, layer='master')
    extend " you doing that?"
    mekki "A little pre-work on organizing them into their specific categories. I sort everyone's writing into that filing cabinet, remember?"
    oliver "Oh, yeah."

    show mekki handstogether pfah
    $ renpy.transition(dissolve, layer='master')
    mekki "I don't just toss them in, I preserve them and make sure they're organized by genre or story if it has multiple installations. Lots of folders and sub-folders."
    oliver "Does anyone help you?"
    mekki "Sometimes, but not usually. It's easier if I do it myself, though."
    "Judging by those large stacks of writing, I'm not sure if it is easier if she does it on her own."
    show mekki thinking smile
    $ renpy.transition(dissolve, layer='master')
    #stop music fadeout 2.5
    mekki "Did you enjoy yourself today?"
    oliver "I think so."
    show mekki thinking smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "Glad to hear it. Feel free to come back whenever you want to, alright?"
    "There's that disarming smile again. There's... something off about all of this, that I can't quite put my finger on. Oh well."
    oliver "I'll keep it in mind. Thanks."
    "Well, I should get going. The day's almost over and I have a bit of a ride back home."

    stop music fadeout 1.5
    window hide smoothDissolve
    scene black with longDissolve

    scene bg apartment livingroom with dissolve
    window show dissolve
    play ambiance "sfx/ambiance/silence.ogg" fadein 1.0

    "With my assignments and syllabus spread out on the table in front of me, the outlook still doesn't seem good for me."
    "I only have a better understanding of this stuff because of what I learned from those two clubs. I don't really know what the hell I should even be doing to finish either class' homework for next week."
    "The art class' assignment is due Monday, writing class' is due next Thursday. At least the timing is nice, because I have to make my decision by Sunday.{nw}"
    play sound "sfx/door_open.ogg"
    extend " A week exactly from the day I made this arrangement with Lawe."
 
    show izaac headscratch smirk with dissolve:
        xanchor 0.5
        xpos 0.8
        yoffset -175
    izaac "Yo, dude. What's the hap'?"
    oliver "You've got the clap?"
    show izaac headscratch surprised
    $ renpy.transition(dissolve, layer='master')
    izaac "Wha-?{nw}"
    show izaac headscratch neutral
    $ renpy.transition(dissolve, layer='master')
    extend " No!"
    oliver "Might want to see a doctor if you have a rash."
    show izaac frown
    $ renpy.transition(dissolve, layer='master')
    izaac "You know, I'm not gonna let you be a Debbie Downer. I wanted to see what's up, 'cuz you look bummed out."
    oliver "Ah, just being forced into an inescapable situation where I'll have to be led by the hand through my courses."
    oliver "A typical cheery stroll through my everyday life.{nw}"
    show izaac smirk
    $ renpy.transition(dissolve, layer='master')
    extend ""
    "I think Izaac disproves of my outlook, considering that dopey look on his face."
    izaac "I don't think that's such a bad thing. Aren't you glad that you have people who'll help you?"
    oliver "They don't want to help me for the sake of helping, otherwise I'd feel better about this."
    show izaac shrug smirk eyesclosed
    $ renpy.transition(dissolve, layer='master')
    "A sigh and a shrug from Izaac."
    izaac "Well, I think you should count the good things, not the bad. No matter which way you slice it, you're coming out positive, right?"
    "I'm not sure how well he understands the concepts of numbers or what's \"positive\" or \"negative\", but sure. I'll agree to that."
    oliver "Sure. I have a feeling it'll be more of a pain than I want to deal with, but yeah. I'll end up saving my enrollment with a little luck."
    show izaac handspockets grin
    $ renpy.transition(dissolve, layer='master')
    izaac "Well, then cheer up! It'll only get better from here on out. If you need someone to talk to, you know where you can find me."
    "I imagine that is meant to be reassuring, but it just comes off kind of weird, especially seeing as he's heading towards his bedroom."
    oliver "I'll keep that in mind. Did you eat already? I'm going to make something, it's not easy to do homework hungry."
    show izaac handspockets smirk eyesclosed
    $ renpy.transition(dissolve, layer='master')
    izaac "Nah, I'm fine. Already ate."
    show izaac at flip('izaac handspockets smirk eyesclosed'):
        time 0.4
        easeout 2.0 xpos 1.15

    "Well, at least that means it'll be quiet for the rest of the night. The guy never manages to shut up whenever I'm around."
    play sound "sfx/door_close.ogg"
    $ renpy.transition(dissolve, layer='master')
    "I rub my forehead while trying to figure out how I'm going to finish this homework before I have to go to sleep. Somehow, I feel like my days are getting a lot longer."
    
    stop ambiance fadeout 1.0
return
