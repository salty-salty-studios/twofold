label scene_1S11_en:
#####################
    # Act 1, Scene 11
    # I'm Not Good With Words
    # Hey look, it's a Mek
    # Scene fades in
    scene bg classroom writing with longDissolve:
        xalign 0.5
        yalign 0.5
    window show smoothDissolve

    play sound "sfx/door_open2.ogg"
    "Opening the door, I'm greeted by an empty classroom."
    "Well, almost entirely empty."    
    show mekki thinking frustrated:
        xanchor 0.5
        xpos 0.45
        yanchor 0.5
        ypos 0.7
    $ renpy.transition(dissolve, layer='master')
    "Yep."
    "I really should've guessed."

    show bg classroom writing:
        xalign 0.5
        yalign 0.5
        subpixel True
        ease 1.0 xzoom 0.92 yzoom 0.92
    show mekki thinking frustrated:
        xanchor 0.5
        ease 1.0 xzoom 0.92 yzoom 0.92
    scene black with wiperight
    play music "music/takingnotes.ogg" fadein 2.0
    play sound "sfx/door_close.ogg"
    "Instead of entering, I walk backwards out of the doorway and slowly close the door."
    "Time to weigh my choices. I can pick the art class and deal with the walking headache, or I can choose this class and constantly remember how awful I am with women."
    "I'm not on the schedule for either class until Lawe officially puts me in one, so in theory I could just skip it..."
    "I should still check this class out. It might be more tolerable as long as I can at least dodge that girl. I doubt it'd be easier to avoid Caprice..."
    "Might as well go through with the class this one time."

    scene bg classroom writing:
        xalign 0.0
        xzoom 0.9
        yzoom 0.9
        subpixel True
        ease 1.0 xzoom 1.0 yzoom 1.0
    show mekki thinking frustrated:
        xanchor 0.5
        xpos 0.45
        yanchor 0.5
        ypos 0.7
        xzoom 0.9
        yzoom 0.9
        ease 1.0 xzoom 1.0 yzoom 1.0
    with wipeleft
    play sound "sfx/door_open2.ogg"
    "I slowly open the door again and{nw}"
    scene bg classroom writing:
        xalign 0.0
        ease 2.5 xalign 1.0
    show mekki thinking frustrated:
        xanchor 0.5
        xpos 0.45
        yanchor 0.5
        ypos 0.7
        ease 2.5 xpos 0.3
    extend " immediately head towards the back of the classroom, away from that blonde girl."

    show mekki at pflip('mekki left thinking surprised'):
        xanchor 0.5
        xpos 0.3
        yanchor 0.5
        ypos 0.7
    stop music fadeout 0.5
    "Once I sit down, the girl turns around and looks at me."
    "Why."
    "Why are you looking at me?"

    show mekki left thinking smile
    $ renpy.transition(dissolve, layer='master')
    mekkiu "You can sit over here, you know."
    "Her voice isn't austere, like I figured it'd be. It's sort of soft, like she doesn't like raising her voice. She pats the chair next to her."
    "For the love of–"
    "She's smiling so sincerely that it's bothering me. As if the whole cafe thing wasn't an extremely awkward experience for the both of us."
    "I don't want to make this worse though, so..."
    show bg:
        subpixel True
        ease 2.5 xalign 0.3
    show mekki:
        subpixel True
        ease 2.5 xpos 0.4
    "Might as well sit next to her."
    "When I do, I immediately open a notebook and distance myself from her as much as possible."
    "I just want to pretend like we've never met each other."
    mekkiu "About earlier..."
    "She's not making it very easy to pretend, though."
    oliver "Did you enjoy the free coffee?{nw}"
    show mekki left thinking laughing
    $ renpy.transition(dissolve, layer='master')
    extend ""

    "I almost get up and leave, realizing that I blurted out what I was thinking."
    "Wait."
    play music "music/mek.ogg" fadein 2.0
    "...Is she laughing?"
    mekkiu "Well, I appreciated the free coffee, but I suppose I didn't like it. Their house blend isn't really that good. Thank you, though."
    "I grumble to myself."
    oliver "Could've said that when I bought it."

    show mekki left thinking hmm
    $ renpy.transition(dissolve, layer='master')
    mekkiu "Sorry about that. I didn't know what to do because people don't normally do things like buy me coffee."
    "I arch an eyebrow. Really? Somehow I doubt that."
    show mekki left thinking smile
    $ renpy.transition(dissolve, layer='master')
    mekkiu "I wanted to thank you and I've been feeling bad about it since then, so it's nice that I can now."
    oliver "If you wanted to, why didn't you then?"

    show mekki left thinking pfah
    $ renpy.transition(dissolve, layer='master')
    mekkiu "Honestly, I was a bit embarrassed. I couldn't muster up the courage. I sort of thought you were, well..."
    "Hitting on you?"
    "Ugh. I wish things I did didn't seem so transparent."
    show mekki left thinking smile
    $ renpy.transition(dissolve, layer='master')
    oliver "I just felt like being nice, don't be embarrassed over it."
    "This way I can just... sidestep the entire thing."

    show mekki left pensive smile
    $ renpy.transition(dissolve, layer='master')
    mekkiu "So, what's your name? I'm Mekki."
    "She extends a hand to shake. Eh. Is there a need for formalities? Can't you just ignore me and I ignore you?"
    "Oh well."
    "I shake her hand in return."
    oliver "Oliver Penn."
    mekki "Mekki Clarke."
    
    "So I did hear her right the first time. Mekki?"
    "Okay, so in one class there's a girl with a weird hat, and in this one, a girl with the weirdest name I've ever heard."
    oliver "Mekki?"
    show mekki left pensive smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    $ renpy.pause(0.3)
    show mekki left pensive smile
    $ renpy.transition(dissolve, layer='master')
    "She nods."
    oliver "That's not... a very common name, huh?"
    mekki "No, not really."
    oliver "Who came up with that?"
    show mekki left thinking hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "My mom."
    "Uh huh."
    oliver "Why'd she name you that? I don't even think it's a real name."
    show mekki left pensive hmm blush
    $ renpy.transition(dissolve, layer='master')
    mekki "Well... promise not to tell anyone?"
    oliver "Uh, sure."
    mekki "My parents have been together since they were kids, and she sort of wanted a boy to name after my father. So she, well..."
    mekki "My dad's name is Michael, but she's always called him \"Mikey\"."
    "Oh. Mikey, Mekki."
    "I have to stifle my laughter. As if the name wasn't weird enough, the explanation behind it is even stranger."
    show mekki left thinking pout
    $ renpy.transition(dissolve, layer='master')
    mekki "It's not funny! I used to get teased a lot because it was weird."
    oliver "Alright, sorry."
    "Now that that's over, can I get back to ignoring everything? I just want to see what this class is like. A long silence fills the mostly empty room, which I'm glad for."

    show mekki left pensive surprised
    $ renpy.transition(dissolve, layer='master')
    mekki "So, are you a writer or just looking for some extra credits?"
    "I guess not."
    "I sigh, trying to force this feeling out of my chest. The fact she even has to ask tells me a lot about what she thinks about me."
    "I doubt she thinks I'm a writer and probably just assumes I'm some loser trying to sneak in an easy class."
    "I bet I'm not up to whatever standards she has of writers. Maybe I should actually change my wardrobe to fit in with these artsy types. I should go to a thrift shop and buy a tweed jacket so I fit the bill more for her."
    oliver "Well, I'm not looking for anything easy, just trying new things. Can't say I'm much of a writer, though."

    show mekki left pensive starryeyed
    $ renpy.transition(dissolve, layer='master')
    mekki "Oh, that's good!"
    "...How is it good? Wouldn't that make this class harder if I'm not? Or less of her type of person?"
    show mekki left pensive smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "It's just always nice to see people trying out new hobbies, especially those of the creative variety."
    "I don't know how \"creative\" it is to write things that no one will ever read it. Aside from that, almost everything I've ever read has been devoid of creativity."
    oliver "And you? Judging by that fancy pen you've got, I imagine you are."
    "I'll try to avoid mentioning I think she's some pretentious writer based on that compilation of work by some writer I've never heard of. Nevermind the fact that it's probably awful and boring."

    show mekki left giggle lookup
    $ renpy.transition(dissolve, layer='master')
    mekki "Yes, I like to say I am."
    oliver "Say?"
    show mekki left giggle hmm
    $ renpy.transition(dissolve, layer='master')
    "Mekki shrugs a little."
    mekki "People have a bunch of different definitions on what makes you a writer. Some think you have to be published or make money to be a writer."
    oliver "And you don't agree with that?"
    show mekki left giggle smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    "Mekki shakes her head."
    mekki "Of course not! The minute you start creatively writing, you're a writer in my eyes."
    "Huh. Really now?"
    oliver "And what about the bad writers? The kind who write nothing but awful fanfiction?"
    "Instead of looking disgusted by the word \"fanfiction\", Mekki giggles and seems to get a little too into the discussion at hand."

    show mekki left giggle smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Everyone starts somewhere! Fanfiction can be a good way for people to start, it's easier."
    mekki "Less focus on setting, characters – lets the new writer focus on character development and the basics of writing."
    mekki "It's not always the best writing out there, but it's accessible and for that reason it's great in its own regard. Once in a while you find a great story."
    oliver "...Do you read fanfiction?"
    show mekki left giggle surprised blush
    $ renpy.transition(dissolve, layer='master')
    "She blushes a little."
    mekki "Sometimes."
    "Well, that's a bit out of line with my expectations and what she was reading earlier. Maybe she's not as pretentious as I thought."
    "Maybe."
    oliver "So, what do you write? Like, genres."

    show mekki left handstogether starryeyed with dissolve
    "Her eyes light up like it's Christmas. Oh crap, did I just open Pandora's box?"
    mekki "Well, I've tried to write a little bit of everything–-mainly because it's good to branch out. Challenges you a little and you learn a lot."
    mekki "I think the genres I like to write best are romance-{w=3.0}{nw}"
    "Well, that's expected of a girl.{w=2.5}{nw}"
    mekki "...and horror. Oh, things involving time-travel or alternate realities and universes are really fun too. So many possibilities for interesting storylines!"
    "Horror? Ehhhh. I've never been a fan of horror. Blood and gore – those sort of things make me feel nauseous when I think about them."
    "I think she's still going on about things she writes, even though I'm mostly tuning her out and nodding along with what she's saying."
    mekki "What about you? Anything you like to read?"
    "I honestly have no idea how to respond, so I respond in the only way I know how;"
    oliver "I like reading nineteenth century Russian poetry."
    show mekki left pensive surprised
    $ renpy.transition(dissolve, layer='master')
    "To anyone, the fact that I'm mocking her should be apparent. Instead, it seems to go right over her head."    
    mekki "Really? I actually really like reading–"
    "I cut her off, feeling bad that she doesn't realize I wasn't being serious."
    oliver "I was joking."

    show mekki left thinking hmm
    $ renpy.transition(dissolve, layer='master')
    "She forces a half-hearted laugh."
    mekki "Oh, alright then."
    oliver "To be honest, I don't read much."

    show mekki left thinking smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "You should!"
    oliver "Why?"
    "She seems a little disconcerted about my indifference to reading."
    show mekki left thinking lookup
    $ renpy.transition(dissolve, layer='master')
    mekki "It's like stepping into another world! Haven't you ever wanted to travel? It's an adventure."
    oliver "And if I don't like traveling?"

    show mekki left pensive pout with dissolve
    "She pouts at me. Internally, I'm chuckling at how flustered she's getting. This is vengeance for my four dollars that I'll never get back."
    mekki "Well, if you don't like traveling, then a book would be perfect for you. Traveling was just a metaphor."
    oliver "Well, metaphor or not, I don't like to read."
    mekki "\"My name's Oliver and I don't like to read because I hate fun things.\""
    "Even though it's obvious she's mocking me, she meets my glare{nw}"
    show mekki left pensive laughing
    $ renpy.transition(dissolve, layer='master')
    extend " with a large smile."
    "I halfway wonder if she's getting {i}me{/i} back for making fun of her just a little while ago."
    oliver "I like fun things, I just don't think reading is fun."
    show mekki left pensive smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Well, tough cookies! I think you just need to find something you might like. What are your interests? Fantasy? Sci-fi? Modern? Mystery, adventure?"
    oliver "I used to watch crime movies with my mom when I was a kid. She has this old tape of some movie I can't remember the name of that we watched all the time."

    show mekki left pensive starryeyed
    $ renpy.transition(dissolve, layer='master')
    mekki "Oh, that's perfect! I think I have something you might like, then."
    show mekki left handstogether smile away
    $ renpy.transition(dissolve, layer='master')
    "She reaches over into her messenger bag and fetches a book from it."
    show mekki left smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "Here!"
    "The Maltese Falcon, huh?"
    oliver "What, do you just carry a bunch of books with you?"

    show mekki left giggle smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    "Mekki laughs a little, lifting her messenger bag. There's a single leatherbound journal, a handful of textbooks, notebooks and at least a half dozen paperbacks visible."
    mekki "It's good to have variety, you know?"
    show mekki left thinking smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Now, that book is a bit slow but give it a little time and you won't want to put it down."
    oliver "Okay, uh... give it back when I'm done reading it? I have no idea when I'll finish."

    show mekki left frown
    $ renpy.transition(dissolve, layer='master')
    "Mekki huffs a little."
    mekki "I'm not loaning it to you. It's a gift. You never loan books."
    "Oh, well..."
    oliver "I'll read it sometime, then."
    show mekki left smile
    $ renpy.transition(dissolve, layer='master')
    "She seems pleased with this answer, even though I was trying to avoid thanking her{nw}"
    hide mekki
    $ renpy.transition(dissolve, layer='master')
    extend "."
    stop music fadeout 2.5

    play music "music/afternoon.mp3" fadein 2.5
    "Students start filling into the classroom and eventually,{nw}"
    play ambiance "sfx/ambiance/class_chatter.ogg" fadein 1.5
    extend " so does the professor."
    "The teacher is a stark contrast to how the art class professor looked. Blonde, neatly combed hair and a clean-shaven face."
    "Amusingly enough, he speaks with a heavy British accent as opposed to the clearly foreign-looking art professor who speaks without one."
    stop ambiance fadeout 1.0
    franklinu "Hello, class. For those of you who do not know who I am, my name is Franklin Clacher."
    franklin "Normally, you'd receive a syllabus detailing what we're doing for the semester and all that."
    franklin "I think it's a bit better if we take a practical look at creative writing, involving storybuilding and character development instead."
    franklin "However, if you want, there's a syllabus up here on my desk that you can take at the end of class. For now, I'd like us all to focus on the actual course content instead of reading droll papers about things."
    "Well, that's a refreshing take on teaching."
    franklin "Though, roll call will have to be taken, as it is in every class."
    "He goes through all the names and focuses on me after a few minutes of having reached the end of his alphabetical list."
    franklin "You, sir."
    "He points a pen directly at me while sitting on the edge of his desk at the front of the classroom."
    "Oh great, and here I was thinking I could've avoided being singled out in a new classroom."
    franklin "I don't have you on my attendance. Why is this?"
    "I clear my throat."
    oliver "I'm still deciding on this class or another, so I was told to, uh... attend before making my decision."
    "The professor seems to light up, remembering something."
    franklin "Ah, yes. I do have a note on my desk pertaining to something of that sort."
    franklin "Well then, considering you're sitting next to the college's writing club president, I'll leave it up to her to sell you on why you should pick this class over whatever else you have in mind."
    "He shoots a wink towards Mekki, who doesn't seem to do anything of the sort. She didn't even mention a writing club earlier."
    "Actually, why are there so many clubs?"
    "Are they really that easy to start? Maybe I should make one. The \"losers in danger of flunking\" club."
    "The teacher then continues on with class, beginning the topic at hand for today: interesting settings and how to create them."
    "Listening to his little speech, I'm getting the same feeling I had from the art class. In over my head. I probably couldn't write this \"believable dialogue\" the professor mentions if I tried, nevermind creating some kind of interesting setting."

    play ambiance "sfx/ambiance/class_chatter.ogg" fadein 1.0
    show mekki left with dissolve:
        xanchor 0.5
        xpos 0.3
        yanchor 0.5
        ypos 0.7
    oliver "So, I'm surprised you didn't try to conscript me at the first opportunity into your club. Or this class, for that matter."
    "Mekki giggles {nw}"
    show mekki left giggle smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    extend "a little."
    mekki "I'd rather you make that choice than me force you into something you don't like."
    "Yeah, while I'm sure that's what you mean, I bet it has something to do with the fact that you don't think I'm good enough to be a writer or part of your exclusive little club."
    "At the very least, it prevents me from having to avoid someone like the plague if I'm in the same class as them."
    oliver "Refreshing change from someone else I met earlier this week."
    stop music fadeout 2.5

    show mekki left giggle hmm
    $ renpy.transition(dissolve, layer='master')
    "Her eyes seem to narrow at me."
    mekki "Oh?"
    oliver "Yeah, girl with a top hat. Met her before?"
    show mekki left handstogether frown
    $ renpy.transition(dissolve, layer='master')
    "Her appearance visibly sours."
    mekki "Yes. I actually know her a bit too well."
    "Well, at least we have that much in common. Although I don't think I approve that much more of this girl. I feel like she's trying too hard."
    hide mekki with dissolve

    "While the class goes on, I jot down some notes involving something I will probably never find an application for."
    "I might not even pick this class."
    "How much time until I have to pick my course? It's Thursday, so I have until Monday at least."
    "I groan to myself. I haven't had enough time to really think about either of these two classes."
    "Class eventually ends and Mekki asks for me to wait outside of the classroom for her."
    "I sure hope she isn't going to ask if I want to go to that cafe."
    stop ambiance fadeout 1.0
    window hide dissolve

    scene black with longDissolve
    scene bg hallway 1
    window show dissolve
    play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 1.0
    show mekki pensive frown:
        xanchor 0.5
        xpos 0.8
    with dissolve
    oliver "So, uh... what's up?"
    mekki "Why haven't you chosen a class?"
    oliver "I thought I told you, I'm just trying new things."
    show mekki hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "It's not exactly easy to convince an advisor to put you in a class after sign-up has passed. How did you convince yours?"
    "Why are you being observant of these little details? I can't help but frown. Why does she even want to know about this?"
    oliver "I need an extra class' worth of credits to stay enrolled. My advisor is letting me have a week to find which one I'm better at so I don't fail it and screw myself."
    show mekki smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "Interesting."
    play music "music/mek.ogg" fadein 1.0
    mekki "Tell you what. Choose your writing course over the art one and I'll tutor you during my writing club so that you pass the class."
    oliver "Why? What's the catch?"
    show mekki giggle pfah
    $ renpy.transition(dissolve, layer='master')
    mekki "No catch. You avoid having to deal with Caprice and my club will get a new member. I'm sure she'd rub it in my face if it were the other way around."
    oliver "Isn't that a little... mean?"
    "Mekki huffs a bit, as if it isn't mean-spirited."
    mekki "Well, she's not exactly the nicest person to me, so I'd call it getting even."
    "How mature. I'd be willing to say it's manipulative, even. Glad to know no one actually wants to help out some guy in need, and it's just a matter of getting back at someone."
    show mekki smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Feel free to drop by my club's room. The meetings take place just down the hall, in room 115. Oh, there's a club fair this Saturday, too!"
    oliver "Club fair?"
    "Mekki nods a few times."
    show mekki smile away
    $ renpy.transition(dissolve, layer='master')
    mekki "Yep, there's a fair every year so that clubs can look for new members. I'll have information about the club if you don't want to walk into a room full of people you don't know."
    "Well, not like I haven't been doing that all week anyways."
    oliver "I'll think about it, I guess."

    "Just as I turn to walk away,{nw}"
    show tanya grin at mirror:
        xanchor 0.5
        xpos 0.2
        yanchor 0.5
        ypos 0.5
    $ renpy.transition(dissolve, layer='master')
    extend " I see that welder girl. She's ditched most of the gear from before, although she's still wearing a pair of loose overalls."
    tanyau "Yo, Mekki."
    "She raises a hand in a wave to the girl, who{nw}"
    show mekki handstogether smile
    $ renpy.transition(dissolve, layer='master')
    extend " returns it with a smile."
    mekki "Hello there, Tanya. Feel like heading to the cafeteria?"
    tanya "Yeah, sure. Got nothin' else to do until the bus shows up so I can go home."
    mekki "I'll see you around, Oliver."
    show tanya wink
    $ renpy.transition(dissolve, layer='master')
    $ renpy.pause(0.2)
    hide mekki
    hide tanya
    with dissolve
    "And there the two go, while I stand here looking flabbergasted. What's with this school? Does everyone know each other and I'm the only one who doesn't? I can't be that unsocialized."
    "...Am I?"
    "The realization hits me, just as I think about Tanya winking at me. If Tanya knows Mekki and Mekki knows Caprice and so does Tanya..."
    "Everything I had said to Tanya while laying on the hallway floor – she knew all the people involved. Including Mekki and the cafe."
    "I think I need to transfer to a different school."

    stop ambiance fadeout 2.5
    stop music fadeout 2.5
return
