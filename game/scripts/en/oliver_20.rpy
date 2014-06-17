label scene_1S20_en:
    perform "1S20" independent
    return

label scene_1S20_intro_en:
    call switch_scene('bg hallway 3', 'bg campus reverse')
    play ambiance "sfx/ambiance/outside.ogg" fadein 0.5
    "I don't have any classes this morning, yet I'm at school. Mekki mentioned the club fair today, so I'm going."
    "I'm wondering which of the two will sell me on the idea of joining their club. At this point, it seems I have to pick the lesser of two evils."

    stop ambiance fadeout 0.5
    play sound "sfx/door_open.ogg"
    scene bg gym clubday with fade:
        xalign 0.0
        subpixel True
        linear 15.0 xalign 1.0
    play sound "sfx/door_close2.ogg"
    play ambiance "sfx/ambiance/crowd_loud.mp3" fadein 1.0
    "When I arrive, most of the clubs are still setting up their little tables and booths. There's actually a surprising amount of clubs.\nJust looking around at signs, I can see some for chess, gaming, engineers, musicians, a poetry club and even a couple other art clubs."
    "There's a ton of really niche clubs too, probably related to majors."
    "Maybe I could get away joining one of those to avoid the two that've been so eager to recruit me."
    "That'd probably cause more damage than good and guarantee nothing, though."
    "I'm glad that the auditorium is getting progressively louder, or people could hear me sighing like a whiny brat."

    window hide dissolve
    scene cg club day with dissolve
    "From where I'm standing, I can see Mekki and Caprice already. Seems they got here the earliest and set up their booths smack dab in the center of the auditorium."
    "Right next to each other's."
    "It seems they're leaving their hostilities aside so they can put on their best show for potential recruits. Even though it is quite clear that they put themselves next to one another so they could channel their hostility into competition."
    "I really don't get it, personally. Why put all this effort into a club that's just going to disperse when they leave for another school or graduate?"
    "Maybe they're getting credits out of it or something. That I could understand."
    "Every now and then, I catch them glancing my way while I wander around the auditorium. I'm trying my best to not make this more awkward than it already is, but I don't think I'm succeeding."
    "It doesn't help that they have some of their club goons walking around with what I guess are fliers, trying to corral people to their leaders' booths."
    "They keep staring at me and making me feel uncomfortable. Probably because I didn't immediately run to one of their clubs and immediately claim their president as my enrollment's lord and savior."
    "Well, here goes nothing."
    window hide dissolve

    scene bg gym clubday boothless:
        xalign 0.0
        ease 5.0 xalign 0.5
    show misc clubbooths:
        yalign 1.0
        xalign 0.0
        ease 5.0 xalign 0.5
    show mekki pensive smile eyesclosed behind misc:
        xanchor 0.5
        xpos 1.2
        yoffset 18

        time 0.8
        ease 4.2 xpos 0.8
    show caprice handsbehindback smile at mirror behind misc:
        xanchor 0.5
        xpos 0.65
        yoffset -190

        ease 5.0 xpos 0.25
    with dissolve
    $ renpy.pause(2.0, hard=True)
    play music "music/extracurricular.ogg" fadein 1.5
    with longDissolve
    $ renpy.pause(2.0, hard=True)
    window show dissolve

    "After approaching the two booths, I stand myself directly between them. I don't want to show any bias, so I'm going to do this as fairly as possible."
    oliver "Alright. I'm going to have to listen to one of you try to sell me on your club. The person who picks the number I'm thinking of gets to talk to me first. One, or two?"
    show caprice hattip smile eyesclosed mouthopen:
        xzoom -1.0
        ease 0.3 yoffset -210
        ease 0.25 yoffset -190
    $ renpy.transition(dissolve, layer='master')
    "Caprice nearly leaps out of her seat."
    caprice "{b}ONE!{/b}"
    show mekki pensive smile
    show caprice handsbehindback smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Two."
    return

label scene_1S20_mekki_summary_en:
    if who_explains_first == 2:
        oliver "Mekki got it right."
        show caprice hattip attacked
        $ renpy.transition(dissolve, layer='master')
        caprice "No fair! You picked her instead of me!"
        "If I could roll my eyes any harder, I'd get dizzy."
        show caprice hattip flushed
        $ renpy.transition(dissolve, layer='master')
        oliver "No, that's the number I had in my head. Just wait your turn."

        show bg gym clubday boothless:
            ease 2.5 xalign 0.85
        show misc clubbooths:
            ease 2.5 xalign 0.85
        show mekki pensive smile eyesclosed behind misc:
            ease 2.5 xpos 0.53
        show caprice at flip('caprice handsbehindback flushed') behind misc:
            ease 2.5 xpos -0.1
        $ renpy.pause(2.5, hard=True)

        oliver "Alright, go ahead Mekki. Why should I join your club?"
    else:
        show bg gym clubday boothless:
            ease 4.5 xalign 0.85
        show misc clubbooths:
            ease 4.5 xalign 0.85
        show mekki pensive smile eyesclosed behind misc:
            ease 4.5 xpos 0.53
        show caprice handsbehindback smile at mirror behind misc:
            ease 4.5 xpos -0.1
        $ renpy.transition(dissolve, layer='master')
        $ renpy.pause(4.5, hard=True)

        oliver "Alright Mekki, I can tell you really wanted to go first, so now's your chance. Sell me on your club."

    show mekki pensive smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Alright! I think you'd be interested in joining the writing club because we want to make writing an all-inclusive hobby that anyone can pick up."
    show mekki pensive smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "It's appealing how welcoming we are to new writers. While we have some talented writers, we don't limit our club to talent. Those who are skilled always try to help fledglings get over that beginning hump."
    show mekki pensive smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Starting is always the hardest part in writing, either writing a story or getting into the hobby, so we try to ease people into it. Sometimes we do specialized writing sessions, other times we just let people do what they wish with their ideas."
    mekki "We always keep the atmosphere friendly and relaxed, which is something people really enjoy. Some of our club members find the club room more than just a club room and something of a haven, or a home."
    "That doesn't sound so bad."
    oliver "Are there any requisites to stay in the club?"
    show mekki pensive hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "Not particularly.{nw}"
    show mekki pensive smile
    $ renpy.transition(dissolve, layer='master')
    extend " I usually allow anyone to join, so long as they've written anything or intend to try. Or enjoy discussing literature. Normally, I never bar anyone from being part of the club unless they try to disrupt it repeatedly."
    "Ah, that reminds me. That giant rule poster."
    oliver "So then, what's up with the rule poster? It's massive and to be truthful, kind of frightening. How am I supposed to avoid stepping on any toes by violating one of your rules in section b, subsection two of your club constitution?"
    show mekki pensive hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "Well, all the rules are just common sense and finely outlined so there's no loopholes for abusive members to get away with."

    show mekki pensive surprised
    if who_explains_first == 1:
        show caprice hattip attacked at mirror:
            ease 1.2 xpos 0.15
    else:
        show caprice hattip attacked:
            ease 1.2 xpos 0.15
    $ renpy.transition(dissolve, layer='master')
    $ renpy.pause(1.2, hard=True)
    caprice "In other words, there's no fun allowed in her club! Rules are boring and she's boring. I mean, look at her! The most interesting thing about her is that bow."
    oliver "Hey, is it your turn? If you break the rules one more time, I'll join Mekki's club by default."
    show caprice hattip angry
    $ renpy.transition(dissolve, layer='master')
    "Caprice's glare looks like it could kill an elephant."
    if who_explains_first == 1:
        show caprice at nflip('caprice hattip angry'):
            time 0.4
            ease 1.5 xpos -0.15
    else:
        show caprice at flip('caprice hattip angry'):
            time 0.4
            ease 1.5 xpos -0.2
    $ renpy.pause(1.9, hard=True)
    show caprice handsbehindback smile at mirror:
        xpos -0.1
    oliver "Why do you enjoy writing?"
    $ renpy.transition(hpunch, layer='master')
    show mekki pensive smile
    "Mekki claps her {nw}"
    show mekki pensive starryeyed
    $ renpy.transition(dissolve, layer='master')
    extend "hands together immediately, like this is her favorite question."
    mekki "Well, don't you like to daydream?"
    "Well, I do spend a lot of time doing it."
    show mekki pensive smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "In those daydreams, you think up all sorts of things, what if's and maybes. Different scenarios, some real and some unrealistic. Right?"
    oliver "Yeah, I suppose."
    show mekki pensive smile
    $ renpy.transition(dissolve, layer='master')
    mekki "You do that a lot in writing. Your mind wanders, but you give it a direction. A reason. What story do I want to tell? No, what story needs to be told? How will I tell it?"
    show mekki thinking lookup
    $ renpy.transition(dissolve, layer='master')
    mekki "As a writer, we extend our hand to the reader, so we can lead them on a journey. Sometimes it's to a world unlike ours, sometimes it's to a place in a world exactly like ours. No matter what, the writer wants to give you an experience."
    mekki "With practice and enough focused daydreaming, we can create an experience that a reader can only have through our words. With care and precision, you can craft a finely-tuned world that a person can live a whole other life in."
    show mekki thinking smile
    $ renpy.transition(dissolve, layer='master')
    mekki "Isn't that exciting? I start getting breathless when I think about how wonderful writing is."
    "Maybe you're getting a little too excited about it, but whatever floats your boat, lady."
    oliver "Yeah, I think it could be. Now, this is more for my sake, not as a generic club recruit. How do you plan to help me pass, if I choose your club and the writing course to go with it?"
    show mekki thinking smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    mekki "Well, I'd more or less be your personal tutor. I've never tutored anyone before,{nw}"
    show mekki thinking pfah
    $ renpy.transition(dissolve, layer='master')
    extend " but I've been told I'm good at giving advice. I fancy myself fairly learned in literature and writing, so I think I should be able to help you with it."
    show mekki thinking smile
    $ renpy.transition(dissolve, layer='master')
    mekki "I'd probably start with establishing what you know, then outlining some kind of regimen to help you learn. You'd obviously have to come to each club meeting.  That way I could make sure to keep you on track."
    show mekki thinking hmm
    $ renpy.transition(dissolve, layer='master')
    mekki "I might assign you some reading, but{nw}"
    show mekki thinking smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    extend " most of it will be hands-on writing. I think you'd be capable of pulling it off."
    "The confidence in me is... well, probably misplaced, but it's refreshing."

    show mekki pensive smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    return

label scene_1S20_caprice_summary_en:
    if who_explains_first == 1:
        show caprice hattip smile eyesclosed
        show mekki pensive surprised
        $ renpy.transition(dissolve, layer='master')
        oliver "...Caprice got it right."
        "Great, of course the loud one has to be fir-"
        show mekki pensive pout
        $ renpy.transition(dissolve, layer='master')
        mekki "{fade=50,50}Why does she always get to go first?"
        show mekki pensive hmm
        $ renpy.transition(dissolve, layer='master')
        oliver "What was that? It's not your turn, so try to keep your comments to yourself unless you'd like me to join Caprice's club."
        "Mekki pouts and goes silent."

        show bg gym clubday boothless:
            ease 2.5 xalign 0.2
        show misc clubbooths:
            ease 2.5 xalign 0.2
        show caprice at nflip('caprice hattip smile eyesclosed'):
            xzoom 1.0
            ease 2.5 xalign 0.55
        show mekki:
            ease 2.5 xpos 1.1
        $ renpy.pause(2.5, hard=True)
    else:
        show bg gym clubday boothless:
            ease 4.5 xalign 0.2
        show misc clubbooths:
            ease 4.5 xalign 0.2
        show mekki pensive smile eyesclosed behind misc:
            ease 4.5 xpos 1.1
        show caprice behind misc at nflip('caprice handsbehindback smile'):
            xzoom 1.0
            ease 4.5 xpos 0.55
        $ renpy.pause(4.5, hard=True)
        oliver "Alright. Since you were having such a hard time containing yourself, I guess I have to listen to your pitch now."

    oliver "So, Caprice, why should I-"
    "Before I even finish my sentence,{nw}"
    show caprice hattip smile:
        ease 0.5 yoffset -210
    extend " Caprice stands up, {nw}"
    play sound "sfx/desk_slam.ogg"
    $ renpy.transition(vpunch, layer='master')
    extend "slamming both hands onto the table in front of her. I visibly flinch and Mekki almost falls out of her chair from shock."
 
    show caprice hattip smile eyesclosed mouthopen
    $ renpy.transition(vpunch, layer='master')
    caprice "{b}YOU SHOULD JOIN THE ART CLUB BECAUSE IT'S AMAZING!{/b}"
    "Everyone sort of stops and stares, making me feel embarrassed by association at Caprice's outburst."
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    caprice "With enough effort, you can make something that a person can absorb in a single second, but think about for days."
    "Sort of deep for a person whose head might be as hollow as her hat."
    show caprice handsbehindback curious
    $ renpy.transition(dissolve, layer='master')
    caprice "Have you ever seen a picture that just made you stop and stare, and wonder? What is the artist thinking? What do I think about this? What is this really about?"
    show caprice hattip smile eyesclosed mouthopen
    $ renpy.transition(vpunch, layer='master')
    caprice "{b}YOU CAN DO THAT.{/b} You can create a snapshot of an entire world, an entire feeling, an entire place–"
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    caprice "And force a person to experience it with a single look.{nw}"
    show caprice handsbehindback curious
    $ renpy.transition(dissolve, layer='master')
    extend "To me, art is about grabbing someone's attention. Even if they look away after a single second, I want them to keep thinking about what that work of art meant!"
    if who_explains_first == 1:
        "Mekki actually looks upset by that statement in a way that almost makes me feel guilty for that remark I made earlier. I wonder if she feels like she's always second string or something, compared to Caprice. Still, I imagine these two will bicker through the entire club fair if I enable them."

    oliver "So, uh. Caprice. How would you help me pass, exactly?"
    show caprice hattip smile eyesclosed mouthopen
    $ renpy.transition(vpunch, layer='master')
    caprice "{b}THROUGH PURE WILLPOWER!{/b}"
    oliver "Uh... I don't think that'd really do the trick."
    show caprice hattip attacked
    $ renpy.transition(dissolve, layer='master')
    caprice "Whaddya mean, don't think it'd do the trick?{nw}"
    show caprice hattip wink
    $ renpy.transition(dissolve, layer='master')
    extend " C'mon. I teach you how to draw, and motivate you so hard you'll come out like Gogh!"
    oliver "...Without an ear?"
    show caprice hattip deadpan
    $ renpy.transition(dissolve, layer='master')
    caprice "No, I meant like a genius! {nw}"
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    extend " You'll be super awesome at art if you let me tutor you. Cross my heart and hope to cry."
    oliver "Don't you mean die?"
    show caprice hattip smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    caprice "Nope! Dying is depressing and depressing things are bad, 'kay?{nw}"
    show caprice hattip curious
    $ renpy.transition(dissolve, layer='master')
    extend " I'll just cry if you don't end up extra-excellent-ordinary at art."
    "I hope she was trying to be cute or something instead of just saying extraordinary. For an artist, she sure takes creative liberty with the English language."

    show caprice handsbehindback smile
    $ renpy.transition(dissolve, layer='master')
    caprice "Look, stop getting distracted. You remember all those pictures on that wall in the clubroom?"
    oliver "Yeah. A lot of them were pretty good."
    "Especially compared to mine."
    show caprice handsbehindback smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    caprice "At least half of 'em never drew before. Only because they were scared to try.{nw}"
    show caprice handsbehindback smile
    extend " So know what I did? I asked them what I ask everyone."
    "She reaches under the table.{nw}"
    show caprice at flip('caprice megaphone grin'):
    extend ""
    "Is that a megaphone? Oh please, don't--"
    show caprice megaphone smile
    show mekki pensive frustrated
    play sound "sfx/megaphone_feedback.ogg"
    $ renpy.transition(hpunch, layer='master')
    caprice "{size=48}{b}WHY AREN'T YOU DRAWING?!{/b}{/size}"
    "If my ears weren't ringing before, they are now."
    show mekki frustrated:
        ease 1.0 xpos 0.9
    $ renpy.pause(1.0, hard=True)
    "Mekki immediately snatches{nw}"
    show caprice hattip attacked
    $ renpy.transition(dissolve, layer='master')
    extend " it away from her and in the blink of an eye, disassembles it and removes the batteries.{nw}"
    show mekki frown
    $ renpy.transition(dissolve, layer='master')
    extend " I guess she's done this before."
    show mekki at pflip('mekki left frustrated'):
        time 0.4
        ease 1.5 xpos 1.1
    $ renpy.pause(1.9, hard=True)
    show mekki pensive smile eyesclosed:
        xzoom 1.0
    oliver "Okay.{nw}"
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    extend " So you'll keep me motivated."
    show caprice hattip wink
    $ renpy.transition(dissolve, layer='master')
    caprice "Yep! Plus, I know a thing or ten about art.{nw}"
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')   
    extend ""
    "Did she just wink at me? She did, didn't she?"
    oliver "One thing, though."
    caprice "Mmmmmhm?"
    oliver "I get that an art club should draw, but don't you think that being the only \"rule\" is sort of... chaotic?"
    show caprice handsbehindback smile eyesclosed
    $ renpy.transition(dissolve, layer='master')   
    caprice "Nahhh. So long as people use their noodle, they don't have to worry. The minute they do something dumb, I usually tell them to get out."
    oliver "Yeah? Like, permanently out of the club?"
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')   
    caprice "Nope, don't you think that's a bit too extreme? I almost never ban people from my club. I usually let them back in if they apologize nicely enough."
    return

label scene_1S20_club_choice_en:
    show bg gym clubday boothless:
        ease 2.5 xalign 0.5
    show misc clubbooths:
        ease 2.5 xalign 0.5
    show mekki behind misc:
        ease 2.5 xpos 0.8
    show caprice at mirror behind misc:
        ease 2.5 xpos 0.25
    $ renpy.pause(2.5, hard=True)

    doublespeak caprice mekki "So, which club are you going to pick?"
    "All negative things aside, neither seem as awful as I thought."
    "Both of them seem talented enough, and I'd probably pass if I try hard enough."
    "It's just a matter of which girl I want to deal with more. Caprice is noisy and way too pushy, but I have the feeling Mekki might be a bit manipulative and neurotic, all things considered."
    "I wonder what mom would suggest I do."
    mom "\"Pick who you think is cuter!\""
    "Thanks, imaginary mom. You're a big help, like always."
    return

label choice_1S20_club_choice_en:
    window hide dissolve
    $ renpy.transition(dissolve)
    call screen choice_1S20_club_choice
    $ _choice = _return
    return _choice

transform arttf:
    on hover:
        time 0.1
        ease 2.5 xoffset -75
    on idle:
        time 0.1
        ease 2.5 xoffset 0

transform writetf:
    on hover:
        time 0.1
        ease 2.5 xoffset 75
    on idle:
        time 0.1
        ease 2.5 xoffset 0

screen choice_1S20_club_choice:
    frame:
        background Null()

        add "vfx/choices/club/base.png":
            xpos 375
            ypos 184

        imagebutton id "artclub" at arttf:
            idle "vfx/choices/club/artclub.png"
            hover "vfx/choices/club/artclub.png"
            focus_mask True
            hovered [
                ShowImage('bg', at_list=[moveto(2.5, 0.4)]),
                ShowImage('misc', at_list=[moveto(2.5, 0.4)]),
                ShowImage('caprice', at_list=[mirror, movetop(2.5, 0.3)]),
                ShowImage('mekki', at_list=[movetop(2.5, 0.85)])
            ]
            unhovered [
                ShowImage('bg', at_list=[moveto(2.5, 0.5)]),
                ShowImage('misc', at_list=[moveto(2.5, 0.5)]),
                ShowImage('caprice', at_list=[mirror, movetop(2.5, 0.25)]),
                ShowImage('mekki', at_list=[movetop(2.5, 0.8)])
            ]
            action Return(1)
            xpos 375
            ypos 184

        imagebutton id "writingclub" at writetf:
            idle "vfx/choices/club/writingclub.png"
            hover "vfx/choices/club/writingclub.png"
            focus_mask True
            hovered [
                ShowImage('bg', at_list=[moveto(2.5, 0.6)]),
                ShowImage('misc', at_list=[moveto(2.5, 0.6)]),
                ShowImage('caprice', at_list=[mirror, movetop(2.5, 0.2)]),
                ShowImage('mekki', at_list=[movetop(2.5, 0.75)])
            ]
            unhovered [
                ShowImage('bg', at_list=[moveto(2.5, 0.5)]),
                ShowImage('misc', at_list=[moveto(2.5, 0.5)]),
                ShowImage('caprice', at_list=[mirror, movetop(2.5, 0.25)]),
                ShowImage('mekki', at_list=[movetop(2.5, 0.8)])
            ]
            action Return(2)
            xpos 375
            ypos 184
