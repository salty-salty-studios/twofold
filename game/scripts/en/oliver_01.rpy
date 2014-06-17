label scene_1S1_en:
######################
    # Act 1, Scene 1
    # Failure Begins with an O
    if not rabbl_playthrough.oneshot:
        $ mouse_visible = False
        scene misc intro mainmenu as bg
        show logo:
            xpos 50
            ypos -68
        with None
        show misc intro act1 as title at left
        with midlongDissolve
        show bg apartment outside grayskies desaturated
        show misc intro side as side:
            xalign 1.0
            xoffset 5

        with midlongDissolve
        show misc intro side as side:
            ease 2.5 xpos 1.5
        with None
        hide title
        $ renpy.transition(midlongDissolve, layer='master')
        $ renpy.pause(2.0, hard=True)
        hide logo
        show bg apartment outside grayskies
        with midlongDissolve
        $ renpy.pause(2.0, hard=True)
        $ mouse_visible = True
    else:
        scene black with dissolve
        stop music fadeout 1
        scene bg apartment outside grayskies with longDissolve
    play ambiance "sfx/ambiance/wind_howling.ogg" fadein 1
    window show dissolve

    "The minute I step outside,{nw}"
    $ renpy.transition(vpunch, layer='master')
    extend " I'm almost thrown to the ground by a gust of wind."
    "I just barely keep myself from toppling over and have to wait a couple moments for the wind to die down." 
    "For a September morning, it's pretty crappy out. Cold, too – the air has a bit of winter chill to it already."
    "Aside from the windchill, there's an ugly gray cloud cover overhead. The weather forecast says there's a chance of showers, which sounds awful in this barely above-freezing weather."
    "In a way it's funny; the weather matches my mood. I turn around, making sure that I closed the door{nw}"
    play sound "sfx/door_close.ogg"
    "In a way it's funny; the weather matches my mood. I turn around, making sure that I closed the door{fast} to my apartment."
    "I take a deep breath of cold air. If it weren't for locals making apartment deals with the students, my walk would be a lot longer. I'd just take my bike, but with this wind and chance of rain, it seems better not to."
    "Having a bike and living close to school lets me save money on transportation, which is nice."  
    "Some people ask why I don't drive. My answer is usually that I just don't want to."
    "Truth is; if I had the money for a license or a car, I probably wouldn't be in a community college."
    "Money's never been an abundant resource of mine. Especially lately, thanks to my last roommate transferring to a different college last semester."
    "Because of that, I spent most of my free time this summer at my job just to afford rent and food."
    "I doubt I can handle a heavy work schedule to pay my bills and continue school at the same time. Hopefully my college arranges for someone to be my roommate, that way I only have to deal with half the rent."
    "I've got worse things to worry about, though."
    "{nw}"

    scene bg campus outskirts grayskies with fadeInOut
    
    "The closer I get to being on campus, the more a cold chill of panic grows in my chest."
    "Just a few moments away are the worn brick buildings that I've spent so much time wandering, but never paying much mind to."
    "This might be the last time I see these buildings, so I figure I should get a good look at them."
    "It's a shame they don't look that good."
    
    "Anxiety aside, my arrival is nothing short of uneventful. I almost wish something {i}would{/i} happen, just so I could avoid this meeting."
    "Nothing does, however.{w=1.0}{nw}"
    "Nothing does, however.{fast}\nLike always, nothing ever happens out of the blue to help me out." 
    "Maybe it's the weather, or maybe it's just me, but the few students I see walking around the deserted campus look as discontent as I feel right now."
    "It doesn't bode well with me, a lifeless campus filled with lifeless people.\nI feel like I'll soon be added to the ranks of the living dead walking the grounds."
    "As much as I'm trying to avoid it, I still need to go to the union building. It's the main administrative building, containing two things that bring together the student body:"
    "The food in the cafeteria and the agony of academic advising."
    "{nw}"

    scene bg union outside grayskies with fade
    "Unfortunately, I'm not here to eat."
    "The minute the union building comes into sight, my stomach clenches and nausea starts to take over. I know why my advisor asked me to meet him, as desperately as I've tried to ignore it this entire time."
    "Begrudgingly, I continue walking towards the building and up the steps. I hesitate for a moment before pulling open{nw}"
    play sound "sfx/door_open2.ogg"
    "Begrudgingly, I continue walking towards the building and up the steps. I hesitate for a moment before pulling open{fast} the door to the building."
    "{nw}"

    scene bg union foyer with fade
    stop ambiance fadeout 0.5
    play sound "sfx/door_close2.ogg"
    "Never have I felt this intimidated by such an empty lobby. The stairs will lead to my doom, I just know it."
    "I've got a good idea about how the advising is going to go.\nIt won't be to 'discuss' how I've been doing." 
    "It'll be spent {i}telling{/i} me how I've been doing.{w=.75}\nWhich is to say, not well."
    "I'm already kicking myself for letting it get to this. I did pretty well in high school without trying."
    "Why am I having such a hard time {i}now{/i}?"
    "{nw}"

    scene bg laweoffice outside with fade
    "It doesn't matter what kind of student I was, I'm right here – right now.\nOutside of Mr. Lawe's office."
    "This is what I get for slacking off."
    "I didn't have to put any effort into my work before.{w=1}\nI wonder when and why that changed.{w=1}\nMaybe I should've tried harder."
    "Should've, could've, but I didn't.\nI scratch at my head. There's an itch just under my skin that I can't get at."

    "Sitting down at one of the chairs outside of his office, all I can really do is think about all the possibilities of what this meeting will be like.\nJust about none of those possibilities are looking good."
    "To make matters worse, these chairs are cheap as hell. I can't get comfortable, so I'm doing nothing but fidgeting."

    "Anyone else passing by must think I look like a wreck.\n{w=0.33}Honestly, I feel like a wreck."
    "It feels like forever passes before the door opens{nw}"
    
    show bg laweoffice outside open
    show generic girl disgruntled as student:
        xanchor 0.5
        xpos 0.65
        yoffset -160
    $ renpy.transition(dissolve, layer='master')
    play sound "sfx/door_open2.ogg"
    "It feels like forever passes before the door opens{fast} and a disgruntled looking student exits. She looks me over once and shakes her head."
    student "Good luck. You're going to need it."
    show generic girl confused as student
    $ renpy.transition(dissolve, layer='master')
    oliver "You too. {w=0.2}{fade}I mean, uh..."

    "The student pauses and looks at me like I'm an idiot. I scowl,{nw}"
    show generic girl confused as student at flip('generic girl confused'):
        time 0.8
        ease 3.5 xpos 1.3 xzoom 1.3 yzoom 1.3

    extend " if only to get her to go away. I wish I wasn't so horrible at talking to people when I'm this stressed out."
    "I guess Lawe heard me,{nw}"
    extend " because he's craning his head from inside the room so he can see through the doorway."
    lawe "Ah. Good that you're here, Mr. Penn. Why don't you come in?"
    "{nw}"
    window hide fastDissolve
    scene black with dissolve
    scene bg laweoffice inside with wiperight:
        xalign 0.5
        yalign 0.5
        xzoom 0.91
        yzoom 0.91
        subpixel True
        ease 1.5 xzoom 1.0 yzoom 1.0

    window show fastDissolve
    "I do as he asks, entering and{nw}"
    play sound "sfx/door_close3.ogg"
    extend " closing the door behind me. As fun and demoralizing as it would be to have other people hear about my shortcomings, I'd rather they don't."
    lawe "Take a seat, get comfortable.{nw}"

    play music "music/tense_lawe.ogg" fadein 5
    lawe "Take a seat, get comfortable.{fast}"
    "I'm wondering if that's supposed to be a joke. I don't think I could feel comfortable even if they gave me a personal masseuse for the duration of this meeting."
    show lawe serious away:
        xzoom 0.65
        yzoom 0.65
        xanchor 0.5
        xpos 0.5
        yanchor 0.5
        ypos 0.4
        subpixel True
        ease 2.5 xzoom 0.75 yzoom 0.75 ypos 0.415
    show misc lawedesk:
        xalign 0.5
        yalign 0.5
        subpixel True
        ease 2.5 xzoom 1.15 yzoom 1.15
    show bg laweoffice inside:
        subpixel True
        ease 2.5 xzoom 1.15 yzoom 1.15
    $ renpy.transition(dissolve, layer='master')
    "After sitting down, I look up at Mr. Lawe. His eyes are on his computer screen, not me.  He’s resting his elbows on the table with his hands folded in front of his face, almost as if he’s praying."    
    "Maybe he's praying for my grades or for my chance of staying enrolled.\nActually, judging by how he's just letting this silence dangle between us,\nhe's probably enjoying this."
    "Prick."

    "The prolonged silence makes me feel like a prisoner of war. I'm in a small, windowless room with my interrogator and executioner. Do I at least get a figurative cigarette before my academic execution, Lawe?"
    show lawe neutral
    $ renpy.transition(dissolve, layer='master')
    lawe "Well, I've already looked over everything and can tell you this much."
    lawe "You did {nw}"
    show lawe serious
    $ renpy.transition(dissolve, layer='master')
    lawe "You did {fast}{b}very{/b} poorly last semester."

    "He doesn't even try to deliver those words in a way that's bearable. It's like he's putting spikes on the bat that I've been beating myself with the entire way here."    
    lawe "Even though we're a community college, we have a lot of students and it's hard to accommodate all of them."
    lawe "A full-time student should be earning at least twelve credits a semester from their courses and be able to maintain a grade average of around a B."
    lawe "If a fully enrolled student can't earn at least twenty credits over two semesters and maintain that GPA, we drop their enrollment."
    "The chill I had felt outside the campus grounds comes back with a vengeance. I'm probably well under that GPA.\nHe clears his throat."
    lawe "Right now you're on something called 'academic probation' because of how poorly you did last semester. It means you're in danger of being dropped and denied enrollment for at least a semester. Maybe more, depending."

    "But...{w=0.1} I've already taken out a loan for the next year of college in advance."
    "What happens to that loan? Do I just sit on it for a semester or more, unable to use it?"
    "I'll probably have to pay it off before I can take out another."
    "In the meantime, I'd have to deal with the shame of having flunked out of a {i}community college{/i}. But right now, my mind's drifting back to where I am grade-wise.\nMy grades might not be too bad."

    oliver "And I'm at...?"
    play sound "sfx/paper_shuffling.mp3"
    "Mr. Lawe shuffles his papers around{nw}"
    show lawe away
    $ renpy.transition(dissolve, layer='master')
    "Mr. Lawe shuffles his papers around{fast}, sorting them and straightening them out.\nHis next words are soft and I miss the first half of his sentence."
    lawe "{fade=0,100}... point two.{/fade}"

    "A long{w=0.5}, awkward{w=0.2} pause until I can muster up the courage to break the silence."
    oliver "What{nw}"
    show lawe serious
    $ renpy.transition(dissolve, layer='master')
    extend " point two?"
    "Mr. Lawe clears his throat."
    lawe "One. Point two. The equivalent of a D."

    oliver "...M-My credits?"
    lawe "Five."
    "Oh, for the love of...\n{b}Shit{/b}."

    "I'm so screwed. How did I let my grades slip that badly? I didn't bother checking my grades on the school's site because I was afraid of the damage."
    "Why didn't I keep an eye on my grades? I could've prevented this.\nMy head's swimming with the consequences of this catastrophe and I'm not ready for any of them."
    "I start looking at my hands while I do the math in my head. I'd need to take more than a full course load and pass all of them with at least a B to stay enrolled according to Lawe's criteria."

    oliver "Is there anything I can do? I can't... I really can't afford to have my enrollment dropped."
    show lawe sad
    $ renpy.transition(dissolve, layer='master')
    "Mr. Lawe doesn't seem hopeful, judging by how defeated he sounds."
    lawe "It doesn't seem possible, kiddo. Even if you manage to pass all your classes, you're short on credits. No classes are accepting students this close to the semester's start."
    "It feels like my head would hit the floor if I hang it any lower."
    "What... how do I explain this to my mom?\nShe's the one paying for most of my tuition in the first place."
    "I can imagine how it'll go: \"Yeah, sorry mom. You have to help me pay off the rest of my loan before I can enroll again for the next year's worth of courses.\""
    "\"Nope. We won't be able to just pay it off after I graduate and find a job like I'd planned.\""
    oliver "Well{fade}, thanks anyway..."

    "I stand up to leave. I guess that's that. Maybe I should just drop out?\nI mean, maybe I can save a bit of my own dignity and just withdraw.\nTell my mom that I just feel like college isn't my thing."
    hide lawe
    $ renpy.transition(dissolve, layer='master')
    "I could get a full-time job and just pay off the loans."
    "Blatant lies and false hope aside; if I practice enough, maybe I can convince her that's the truth."
    "Just as I reach the door to leave, I hear Mr. Lawe call out to me from within his office."
    stop music fadeout 0.5
    lawe "Wait!"

    "I pause and turn around.{nw}"
    # behind stopped working.
    show lawe idea behind misc:
        xanchor 0.5
        xpos 0.5
        yanchor 0.5
        ypos 0.415
        xzoom 0.75
        yzoom 0.75
        subpixel True

    $ renpy.transition(dissolve, layer='master')
    extend " Lawe looks like he's had a stroke of genius."
    oliver "What?"
    lawe "I think... I have an idea. It could be a bit of a long shot, but I might have a solution."
    "His hardened expression becomes a bit hopeful. I hope he's right. Instead of walking out, I turn away from the door, sitting down again. I'm not so sure whether he can save me from this mess, but I'm willing to entertain the thought."
    show lawe away with dissolve
    lawe "Well, first of all. I did go over your highschool transcripts. I usually do when I advise a student, so I can get a feel for where they stand."
    show lawe neutral with dissolve
    lawe "You should be capable of more than satisfactory grades if you focus.\nI don't even understand how you're doing so poorly right now."

    "Well, uh... junk food, staying up late and plenty of hours in a lot of different video games might be the answer to that question."
    lawe "If I'm not incorrect, you can manage your required GPA if you try.\nThe credits... that's an entirely different matter."
    lawe "Classes are beginning tomorrow, Monday. {i}Most{/i} classes are filled."
    show lawe smirk
    $ renpy.transition(dissolve, layer='master')
    lawe "Except for a select few."

    show lawe neutral with dissolve
    lawe "I didn't think of them because they're unlisted and require a teacher's recommendation."
    oliver "They sound... difficult. I probably don't meet the requirements."
    show lawe smirk with dissolve
    lawe "That's the thing. They aren't difficult. They're just kept unlisted so they're not swamped with people trying to get \"easy credits\"."
    lawe "Realistically, they're just schedule filler for some Fine Arts majors and for people interested in the arts who ask about it." 
    "Fine Arts? I can almost feel myself retching a bit.\nEven Poli-Sci students are more tolerable than art majors."
    lawe "As for the recommendation, I can easily fudge that and pull some strings to put you in one of those classes. The classes don't require books, so you don't have to worry about money either."
    "Sounds a little too good to be true."

    lawe "It's just a matter if you need them or not.{nw}"
    show lawe away
    $ renpy.transition(dissolve, layer='master')
    extend " Let's find out."
    play loopsfx "sfx/typing.ogg"
    "Lawe quickly maneuvers his mouse, occasionally typing some things out in between sessions of clicking."
    lawe "Doing a little bit of math, if I schedule you for a couple extra core classes,\nmake you retake some of your failed courses-"
    "He continues typing away, putting together salvation in schedule form."    
    lawe "I can get your credits for the term up to fourteen.\nWith what you earned last semester, that puts you at nineteen for the year."
    lawe "You need {i}one{/i} more credit."
    lawe "This is what I thought; you're going to need one of those extra classes that we keep unlisted. They're both single credit courses, meant to be extracurricular rather than something that makes or breaks your enrollment."    
    stop loopsfx
    show lawe smile with dissolve
    "He dons a grin that looks out of place on someone like him."
    lawe "Sort of funny, huh? How an insignificant course can save you from failing out."
    show lawe smirk with dissolve
    lawe "Well, the only two courses that aren't filled right now are the Character Art Creation workshop or the Creative Writing and Analysis workshop.\nWhich one do you want?"
    
    oliver "Uh... Honestly, I have no idea which one I'll be more suited for."
    oliver "I {i}really{/i} don't want to flunk out because I pick the wrong course. Is there any way I can... I don't know, test-drive one or the other first?" 
    show lawe smile
    $ renpy.transition(dissolve, layer='master')
    "Mr. Lawe nods slowly{nw}"
    show lawe smirk
    $ renpy.transition(dissolve, layer='master')
    extend "."
    lawe "I appreciate your caution, especially considering how thin the ice is here. I think I can manage a \"clerical error\" that will put you in both classes, but in a week I'll need to have it \"fixed\"."
    lawe "Our boss is rather strict about going above the norm for students. As it is, she'll get suspicious when she notices that I'm doing this sort of last-minute enrollment."
    lawe "My \"mistake\" will hopefully keep her distracted from your lack of a teacher recommendation and absence of fine art classes in your records."
    lawe "As soon as you figure out which you're better suited for, I'll fix the mistake. By then it'll be too late for my boss to realistically do anything about it."
    lawe "At most, I'll just get a slap on the wrist for helping you out."

    play music "music/genericrelaxmusic.ogg" fadein 1.5
    show lawe away with dissolve
    "This advisor – I had him pegged as someone who probably didn't care."
    "Maybe even someone who enjoys watching people flunk out of something as unglamorous as a community college."
    "Yet, here he is. Willing to use whatever powers he has to ensure I stay enrolled. He's still typing, probably going through the proper channels to have me put into the classes."    
    oliver "{fade}I can't thank you enough."
    "Mr. Lawe waves off my words."
    show lawe smile with dissolve
    lawe "Thank me by passing all these classes you're being saddled with.\nTry not to screw this up. You've only got one chance to do this right."
    "I nod frantically as he continues to explain what I need to do."
    "I definitely won't mess this up."
    "{size=14}I hope.{/size}"
    "{nw}"

    stop loopsfx
    window hide smoothDissolve
    hide lawe
    scene black
    with longDissolve
return
