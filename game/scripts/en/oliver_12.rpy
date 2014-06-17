label scene_1S12_en:
#######################
    # Act 1, Scene 12
    # The Club With One Rule
    call switch_scene_s('bg hallway 1', 'bg study area')
    play ambiance "sfx/ambiance/crowd_silent.mp3" fadein 2.0

    "While I sit alone in one of the school's study areas, not much is on my mind."
    "Especially not how I've alienated myself from one of the groups that I'm going to have to rely on. Well, provided I choose the art class."
    "I still don't know which of the two courses I'm going to condemn myself to."
    "I might as well just pick the writing class and avoid the artists."
    "I shake the imaginary eight-ball in my head."
    "What are the odds I can get through this without it being a massive hassle?"
    "The little twenty-sided die rises from the inky depths of my mind."
    "Reply hazy, try again."
    "Lean back, cover face, groan. Repeat until you've got something figured out, Oliver."
    "I doubt I'll come up with any sort of backdoor out of this. As it is, this is my backdoor out of my last issue."
    "Damn it, why am I such a coward sometimes?"

    play music "music/papercookies.ogg" fadein 1.5
    $ renpy.transition(hpunch, layer='master')
    caprice "{size=36}{b}Oliver!{/b}{/size}"
    "I nearly leap out of my seat in surprise."

    show caprice wave smile mouthopen eyesclosed with dissolve
    oliver "Seriously, can you lower your voice?!"
    "Caprice's smile reads \"nope\"."
    show caprice chintap thinking
    $ renpy.transition(dissolve, layer='master')
    caprice "You're looking a bit more blue than green, what's got you down?"
    "Somehow I doubt she actually cares, otherwise she wouldn't be part of the problem."
    "Instead, I opt to change the topic."
    show caprice handsbehindback smile
    oliver "What's the deal with you and that Mekki girl?"

    show caprice chintap thinking
    $ renpy.transition(dissolve, layer='master')
    caprice "What{i}ever{/i} are you talking about?"
    show caprice chintap wink
    $ renpy.transition(dissolve, layer='master')
    "She looks ready to twirl in place, like this is some kind of joke. I feel like if anything is a joke, it's our interactions."
    "Last thing I want to get is caught up in some kind of comp-{w=1.0}{nw}"
    show caprice hattip smile mouthopen with dissolve
    $ renpy.transition(dissolve, layer='master')
    caprice "We're just having a little bit of a competition, you see!{w=1.5}{nw}"
    "...etition."
    "Fantastic. This is just getting better as the day goes on. I dig out the assignment from the art class so I can use it as an excuse to get her to go away."
    oliver "Honestly, I don't want to get-{w=0.5}{nw}"
    caprice "Stuck in the crossfire? No worries, don't sweat it! Nothing like that'll happen on my watch."

    show caprice hattip smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    "One hand on her hip, the other hand aiming a thumb at her chest which she puffs out like she's some kind of superhero."
    oliver "I think you're missing a cape."
    show caprice hattip flushed
    $ renpy.transition(dissolve, layer='master')
    caprice "Huh?"
    oliver "Don't worry about it."
    "I tap the paper I have on my lap."
    oliver "I have work to do, so would mind leaving me alone? You're sort of loud."
    show caprice hattip deadpan
    $ renpy.transition(dissolve, layer='master')
    caprice "No wonder Wallace was sticking up for you earlier, {nw}"
    show caprice handsbehindback smile mouthopen
    $ renpy.transition(dissolve, layer='master')
    extend " you're like two peas in a pod!"
    "Caprice grins at me, like she told a funny joke and I'm supposed to laugh. She sighs after a{nw}"
    show caprice handsbehindback neutral
    $ renpy.transition(dissolve, layer='master')
    extend " few moments of empty staring, though."
    "I guess if Wallace was sticking up for me earlier, that means the rest of the club knows about the whole Eileen fiasco."
    "I think if I could, I'd combust by now out of frustration. Things might be easier that way, at least."
    show caprice handsbehindback smile
    $ renpy.transition(dissolve, layer='master')
    caprice "Oh, c'mon, don't get grumpy. Whatcha studying? Lemme help!"
    oliver "You'd help more if you'd go away, I can't focus when you're around."
    show caprice handsbehindback flushed
    $ renpy.transition(dissolve, layer='master')
    caprice "I didn't know you felt that way about me. I'm sorry, but I don't think I can return your feelings!"
    "She pretends to be embarrassed, which makes me feel more mortified than anything."
    oliver "That's not what I meant!"
    show caprice hattip smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    caprice "Oh, you're turning red. Don't take things so seriously, Ollie."
    caprice "Is it okay if I call you Ollie?"
    "My mom calls me Ollie, so I don't think so."
    oliver "Absolutely n-{w=0.1}{nw}"
    show caprice chintap smile
    $ renpy.transition(dissolve, layer='master')
    caprice "I think I will anyway!"

    show caprice hattip smile eyesclosed mouthopen
    $ renpy.transition(dissolve, layer='master')
    "She snatches the handout I've had on my lap and been unable to pay attention to, due to her machine gun volley of verbal blasts."
    caprice "Oh, you're studying for the art class that you're definitely going to take instead of that stuffy writing course!"
    oliver "Well, I haven't chosen anything yet, but I'm planning to do the assignments for both. That way I don't end up screwed if I pick the one I didn't do the homework for."
    show caprice hattip smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    caprice "So you're picking the art class? Smart guy!"
    "I didn't say th-{w=0.1} ah, whatever."
    oliver "{fade=50,50}Yeah, well if I was smarter I wouldn't have to deal with any of this..."
    show caprice handsbehindback deadpan close:
        yoffset 800
    $ renpy.transition(dissolve, layer='master')
    "My muttered response seems to get her attention, as she leans towards me."
    caprice "Hmmm? What was that?"
    oliver "Please get out of my face."
    show caprice hattip smile eyesclosed:
        yoffset -30
    $ renpy.transition(dissolve, layer='master')
    caprice "Sure thing!"
    "Then she grabs me by the arm and tugs me from my chair. {nw}"
    $ renpy.transition(vpunch, layer='master')
    show bg:
        ease 0.3 yalign 0.4
        ease 0.2 yalign 0.5
        ease 0.3 yalign 0.3
        ease 0.2 yalign 0.4
        ease 0.3 yalign 0.2
    show caprice:
        ease 0.3 yoffset -20
        ease 0.2 yoffset -30
        ease 0.3 yoffset -10
        ease 0.2 yoffset -20
        ease 0.3 yoffset 0
    extend "She gets me to my feet before I actively start resisting her. She's looks like she weighs about as much as a bag of mixed candy, so resisting is plenty easy."
    oliver "What are you doing?"
    caprice "Helping you study!"
    oliver "I am entirely fine with studying on my own."

    show caprice hattip smile mouthopen
    $ renpy.transition(dissolve, layer='master')
    caprice "That's a funny way to say \"I desperately need your help, oh-wonderful-and-brilliant Caprice\"!"
    "I pull my arm out of her grasp and stand in the hallway."
    oliver "Look, I might need your help, but I don't need headaches. If you can't even answer me on why there seems to be animosity between you and that blonde girl, why should I join your club?"
    show caprice chintap thinking
    $ renpy.transition(dissolve, layer='master')
    "She taps her chin a few times, thinking about the response."
    show caprice handsbehindback flushed
    $ renpy.transition(dissolve, layer='master')
    caprice "Well, we had a disagreement during summer break. Since then, everything's sort of been a competition between each other to see who's \"right\"."
    show caprice handsbehindback neutral
    $ renpy.transition(dissolve, layer='master')
    caprice "It's really no big deal, but everyone's getting caught up in it.{nw}"
    show caprice hattip neutral
    $ renpy.transition(dissolve, layer='master')
    extend " I think it's pretty fun! These sort of competitions motivate people to improve, which I'm all for!"
    "...I guess that's a decent enough answer."
    oliver "I'm still going to end up caught up in the middle though, huh?"
    show caprice shrug smile
    $ renpy.transition(dissolve, layer='master')
    "Caprice shrugs, as if it's no big deal."
    show caprice hattip smile mouthopen
    $ renpy.transition(dissolve, layer='master')
    caprice "Them's the breaks! I don't think it'll be a huge fuss, unless you don't pick my club. Then I might cry."
    show caprice handsbehindback curious
    $ renpy.transition(dissolve, layer='master')
    caprice "You don't want to make a cute girl like me cry, do you?"
    "I don't respond."
    oliver "Can I have my handout back? I need it."
    show caprice hattip deadpan
    $ renpy.transition(dissolve, layer='master')
    caprice "So cold! You can get it back if you come to the club and check it out."
    show caprice at flip('caprice hattip smile'):
        time 0.7
        easeout 0.5 xpos 0.8 alpha 0
    $ renpy.transition(dissolve, layer='master')
    stop music fadeout 2.5
    "And just like that, with my art class homework held hostage, she bolts down the hallway."
    hide caprice
    $ renpy.transition(dissolve, layer='master')
    "Fine."
    stop ambiance fadeout 1.5

    window hide dissolve
    scene black with dissolve
    play sound "sfx/door_open.ogg"
    scene bg classroom art with wipeleft:
        subpixel True
        xzoom 0.92
        yzoom 0.92
        xalign 0.5
        yalign 0.5
        ease 1.5 xzoom 1.0 yzoom 1.0
    window show dissolve
    "I push open the door and find myself looking at a bunch of people I don't know, some who probably only know me as \"that jerk who broke Allison's project\"."
    "Surprisingly, I don't see anyone looking too mad at me. Although from the doorway, Eileen still looks like she's in no mood to see me enter the classroom, let alone anyone else."
    "I look around for a brief moment, then turn to Caprice, who is standing at the head of the class, behind a teacher's podium. There's a club advisor in the corner of the room, reading a magazine at his desk."
    "I recognize him as the art class' professor."
    oliver "Alright, I checked out your club. Can I have my homework back now?"
    "To my surprise, some of the club members chuckle. I figured I'd get some nasty looks from the people in here, considering my already poor history with some of the members."
    "Instead of responding, Caprice skips over to me and puts her hands on my shoulders."
    oliver "What are you doing now? I'd really just like to have my assignment back."
    scene cg artclub intro with dissolve
    "She shuffles me over to a space between the two rows of desks that run up the classroom's length."
    play sound "sfx/chair_scrape.ogg"
    "I hear the scuffling of a chair and something pressing against the back of my legs.{nw}"
    show cg artclub intro pushdown
    $ renpy.transition(dissolve, layer='master')
    extend " Caprice hops up, pressing down on my shoulders with all her weight,{nw}"
    play sound "sfx/chair_drop.ogg"
    $ renpy.transition(hpunch, layer='master')
    extend " forcing my legs to buckle."
    show cg artclub intro seated with dissolve
    "I find myself sitting against my will."

    show bg classroom art:
        xalign 0.5
        yalign 0.5
    show wallace neutral at mirror:
        xanchor 0.5
        xpos 0.15
        yoffset -175
    show eileen handonhip mouthopen behind wallace:
        xanchor 0.5
        xpos 0.9
    show allison smile:
        xanchor 0.5
        xpos 0.75
    show caprice hattip smile eyesclosed mouthopen:
        xanchor 0.5
        xpos 0.5
        yoffset -160
    $ renpy.transition(dissolve, layer='master')
    play music "music/caps.ogg" fadein 2.0
    caprice "Alright! Now then, we can start today's meeting!"
    "I look down at my watch. Well, I'll be. It's five to four o'clock. She was looking for me, wasn't she? Well, no escaping it now."
    wallace "It'll be over soon enough. Just pray you don't enjoy it, or you'll end up like the rest of us."
    "...The others look like they're enjoying themselves. Does Wallace not enjoy being happy?"
    "Caprice, at the front of the class, reaches under the podium."
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    caprice "Alright everyone! Today's challenge!"
    "She places a stereo on top of the podium with a{nw}"
    play sound "sfx/desk_thud.ogg"
    $ renpy.transition(hpunch, layer='master')
    extend " slam, which makes the art professor look up."
    professor "Please try to be gentle with that, you'll break it if you keep slamming it."
    "Caprice throws up a salute to the club's advisor, or supervisor. Whatever these clubs have."
    caprice "Sir yes sir, Mister Scott Su!"
    "He doesn't respond to her outlandish behavior, only opting to run his hand along his goatee in such a cliched manner that it's unreal."
    "Caprice takes a dramatic stance, violently pressing the play button on the stereo."

    caprice "Draw anything with these songs as the background! If you don't like this one, there's six more tracks. The CD will loop, so don't rush yourselves!"
    "She points a thumb over her shoulder."
    show caprice hattip smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    caprice "And for the new guy, we have one rule when club meetings are in session!"
    "Whatever happened to \"Ollie\"? Suddenly, I'm \"the new guy\". Thanks for making me feel welcome."
    "Regardless of my disposition, I look at the poster."
    window hide smoothDissolve
    show misc artruleposter with dissolve
    hide caprice
    $ renpy.pause()
    window show smoothDissolve
    oliver "That's... uh, more than one rule. Technically speaking, I guess."
    caprice "What, are you blind? There's only one!"
    "I guess I'll take Wallace's advice in a different situation and apply it here. No point in arguing."
    hide misc
    $ renpy.transition(dissolve, layer='master')
    "Caprice then skips towards me,{nw}"
    show bg classroom art:
        xalign 0.5
        yalign 0.5
        ease 1.5 xalign 0.9
    show eileen:
        ease 1.5 xpos 0.55
    show allison:
        ease 1.5 xpos 0.7
    with None
    hide wallace
    $ renpy.transition(dissolve, layer='master')
    extend "spinning my chair with some effort so that I can face the nearby table."
    show eileen browup
    $ renpy.transition(dissolve, layer='master')
    "Allison is sitting there and passes me some paper with a friendly smile. To her right, and to her major contrast, is the scowling Eileen."
    "Well, at least she hasn't tried assaulting me and judging by how Allison is smiling, I don't think she's holding a grudge. I should probably keep my distance if possible, though."

    hide allison
    hide eileen
    with dissolve
    show caprice hattip neutral at mirror:
        xalign 0.5
        yoffset -160
        xpos 0.15
    $ renpy.transition(dissolve, layer='master')
    oliver "So, uh... you want me to draw?"
    show caprice hattip smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    "Caprice nods vigorously."
    oliver "What am I supposed to draw exactly?"
    show caprice handsbehindback deadpan
    $ renpy.transition(dissolve, layer='master')
    caprice "C'mon, didn't you just hear me?{nw}"
    show caprice handsbehindback smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    extend " Draw with the music as inspiration!"
    oliver "I don't think I know how to do that. Or how to draw, really."
    show caprice hattip neutral
    $ renpy.transition(dissolve, layer='master')
    caprice "Pssh. Psshhsshsshhhh."
    "She's waving her hands around and making stupid sounds like it's going to change something."
    oliver "That's not very helpful, I still can't draw-"
    show caprice hattip smile eyesclosed
    $ renpy.transition(dissolve, layer='master')

    show drawing blank behind caprice with easeintop:
        yalign 0.4
        xalign 0.5
    caprice "PSSH. Anyone can draw! You just take the pencil."
    "She puts a pencil she got from who-knows-where in my hand, and closes my fingers around it."
    caprice "And move your hands. Like this!"
    "She moves my hand for me,{nw}"
    show drawing stick 
    $ renpy.transition(dissolve, layer='master')
    extend " sketching out a stick figure."
    caprice "See! Now you're an artist. You can draw!"
    oliver "Not very well, if you call that a drawing."
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    caprice "Pay less attention to that and focus on improving!"
    oliver "How do I even impr-{w=0.2}{nw}"
    show caprice hattip smile eyesclosed mouthopen
    $ renpy.transition(dissolve, layer='master')
    $ renpy.transition(vpunch, layer='master')
    caprice "{b}DRAW!{/b}"
    oliver "Okay, okay, holy crap."
    hide caprice
    $ renpy.transition(dissolve, layer='master')
    stop music fadeout 2.5

    show bg cafe tablesurface:
        xalign 0.0
        yalign 1.0
    show drawing:
        ease 2.0 yalign 0.1
    "Snickering from the club members. I can feel heat rising from beneath my collar, so I start... uh, drawing things."
    play music "music/takingnotes.ogg" fadein 1.5
    "The first song sounds like some weird kind of swing that I've never heard of before. Not really my thing."
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    play music "music/afternoon.mp3" fadein 1.5
    "The next is a lot more mellow, which I think I can get behind. I just don't know what I should draw. I do want to erase this stupid stick figure, though."
    show drawing treeriver blank with dissolve
    "She said 'use the music as inspiration'. If there's one thing I'm good at, it's daydreaming. That's a big part of the equation that lead me to this desperate attempt to stay enrolled."
    "Thankfully, music is easy to daydream to. Think up something based on the music. A picture in this case is what I need. Something simple, preferably."

    "The music is calm... so how about a{nw}"
    show drawing treeriver 01
    $ renpy.transition(dissolve, layer='master')
    extend " tree over a spring? That's a sort of place I'd like to be at right now."
    "No worries, just the sound of wind through some leaves. Maybe I'll change that spring to a river."
    show drawing treeriver 02 with longDissolve
    "I've never tried to draw landscapes or much of anything before, but thankfully I'm not finding it incredibly challenging. Everyone has seen a tree before, same with rivers."
    "I erase a couple times{nw}"
    extend ", reoutline some things. People are talking quietly, which isn't very distracting. I think this is the longest period I've seen Caprice quiet, while she's also drawing at a table overlooking the classroom."
    "She's also drawing, but it looks like she's doing so with a pretty large variety of specialized pens."
    "I mean, Wallace did vouch for her, but I just couldn't see it in my head. She seems like too much of a spaz to sit still for long enough, even though she is right now."
    show drawing treeriver 03
    $ renpy.transition(dissolve, layer='master')
    stop music fadeout 2.0
    "By the time I get back to drawing,{nw}"
    play music "music/caps.ogg" fadein 1.5
    extend " the song changes to something a lot more upbeat."
    show drawing treeriver 04
    $ renpy.transition(dissolve, layer='master')
    "Suddenly, I feel like I'm out of the groove. What do you know? It seems the music does help. Instead of finishing, I try to fix up some of the weird things about the tree. I guess it doesn't look like it's growing out of the ground properly?"
    "The 'leaves' don't really look like leaves, more like clouds on sticks. I should probably try to fix that somehow..."

    eileen "What is this shit?"
    show bg classroom art:
        xalign 0.5
        yalign 0.5
    show drawing:
        ease 2.0 yalign 0.4
    $ renpy.transition(dissolve, layer='master')
    $ renpy.pause(1.0, hard=True)
    show eileen handonhip neutral:
        xanchor 0.5
        xpos 1.2
        ease 1.5 xpos 0.8
    $ renpy.transition(easeinright, layer='master')
    "At some point, she got behind me and started appraising my so-called art."
    oliver "It's n-{w=0.1}{nw}"
    show allison handsfolded troubled at mirror:
        xanchor 0.5
        xpos -0.2
        ease 1.5 xpos 0.15
    $ renpy.transition(easeinleft, layer='master')
    "Before I can even roll out an angry remark, Allison points to a part of the tree trunk."
    allison "Look, the trunk bumps out kinda weird over here."
    show eileen handonhip browup
    $ renpy.transition(easeinright, layer='master')
    eileen "And the roots are on top of the ground, instead of growing into it."
    show allison handsfolded smile
    $ renpy.transition(easeinright, layer='master')
    allison "If you can, you should try and detail some gravel under the water, too."
    eileen "Maybe add some light reflections or something so the water looks more... water-like."
    "Well, okay."
    "I can see that making it look better, but it doesn't help me fix it. I'm not sure how to do any of that."

    show eileen at flip('eileen handonhip mouthopen'):
        xanchor 0.5
        xpos 0.8
    show drawing treeriver 05
    $ renpy.transition(dissolve, layer='master')
    "Eileen starts sketching a little ball and what looks like a lightbulb."
    show eileen handonhip mouthopen at nflip('eileen handonhip mouthopen'):
        xanchor 0.5
        xpos 0.8
    eileen "This is basic light and shading. See how the light hits it, and leaves specific shadows?"
    "I nod slowly. I sort of get that, but what am I supposed to do with that?"
    show drawing treeriver 06
    $ renpy.transition(dissolve, layer='master')
    "Eileen shades a bit underneath the tree, following the tree's shape."
    oliver "Oh."
    show allison
    $ renpy.transition(dissolve, layer='master')
    "I look over to see Allison is holding up a quick sketch with arrows pointing towards a tree's roots and how they should look."
    allison "See, it should look more like this! They grow into the ground, so you should draw the earth a bit around them."
    oliver "Hm."
    hide eileen
    hide allison
    $ renpy.transition(dissolve, layer='master')
    "I wait until the song loops back around and continue trying to finish my drawing. When I finish and look up,{nw}"
    show caprice handsbehindback smile at mirror:
        xanchor 0.5
        xpos 0.7
        yoffset -160
    $ renpy.transition(dissolve, layer='master')
    extend " I see that Caprice is going around and talking with everyone about their art."
    "Or rather, I hear it more than anything."

    show caprice handsbehindback smile eyesclosed mouthopen
    $ renpy.transition(dissolve, layer='master')
    caprice "{b}GOOD JOB!{/b}"
    caprice "Looks awesome!"
    caprice "I really like the style to this, it brings out the character's poses!"
    show caprice at nflip('caprice hattip smile'):
        xanchor 0.5
        xpos 0.7
        yoffset -160
        time 0.8
        ease 2.0 xpos 0.5
    "When she gets to me, she has this big grin on her face that makes me feel sort of uncomfortable."
    "I'm starting to{nw}"
    hide drawing
    $ renpy.transition(moveoutbottom, layer='master')
    extend "move my paper out of her reach."

    stop loopsfx fadeout 0.5
    show caprice handsbehindback attacked
    $ renpy.transition(dissolve, layer='master')
    caprice "Aw, show me! You looked so intensely focused when you were drawing. Almost brought a tear to my eye, knowing I've shown another person how exciting art is!"
    oliver "Do I have to? I think I'd prefer to just keep it to myself for now."
    show caprice handsbehindback curious
    $ renpy.transition(dissolve, layer='master')
    caprice "Pleeeeease?"
    show wallace neutral at mirror:
        xanchor 0.5
        xpos 0.0
        yoffset -175
        alpha 0.0
        parallel:
            ease 1.5 alpha 1.0
        parallel:
            ease 1.5 xpos 0.2
    show caprice hattip smile:
        xpos 0.5
        ease 1.5 xpos 0.55
        yoffset -160
    show bg classroom art:
        yalign 0.5
        ease 1.0 xalign 0.2
    "I guess Wallace had enough of being silent, so he chimes in from the table to my left."
    wallace "Let him keep the picture to himself if he wants."
    show caprice hattip attacked
    $ renpy.transition(dissolve, layer='master')
    caprice "Nope! No way, nuh-uh, not possible!"
    "I cover the picture with my forearms, while Caprice tugs at the corners of the paper."
    show wallace frown
    $ renpy.transition(dissolve, layer='master')
    wallace "Can't you just give the kid a break? You already forced him to come here, he's not part of the club. He shouldn't have to offer up his first drawing if he doesn't want to."
    "The turtleneck wearing hipster makes another one of his weird sounding grumbles."

    show caprice hattip smile eyesclosed
    $ renpy.transition(dissolve, layer='master')
    caprice "Brother bear to the rescue! You know, seeing as you mentioned that one time how you always wished you had a little brother, why don't you be Ollie's guide through the club when he joins?"
    oliver "I haven't said I'm going to join this club."
    show caprice hattip smile eyesclosed mouthopen
    $ renpy.transition(dissolve, layer='master')
    caprice "Not yet, but you will!"
    "At least she's optimistic."

    show caprice at flip('caprice hattip neutral'):
        xanchor 0.5
        xpos 0.55
        yoffset -160
        time 0.8
        ease 1.5 xpos 0.4
    with None
    show eileen angry:
        xanchor 0.5
        xpos 1.2
        ease 2.0 xpos 0.75
    show allison holdarm troubled:
        xanchor 0.5
        xpos 1.2
        ease 1.5 xpos 0.9
    $ renpy.transition(easeinright, layer='master')   
    eileen "Now that Caprice mentions it, what's up with you being all protective of this guy? He seems like a jerk and before Allison calmed down, you were trying too hard to defend him."
    "I'm not sure why this is suddenly becoming a witch-hunt as to why someone did the right thing."
    show wallace frown away
    $ renpy.transition(dissolve, layer='master')
    wallace "Because as you know now, the whole thing was an accident and we don't need you expelled for flipping out on random students."
    show eileen handonhip frown
    $ renpy.transition(dissolve, layer='master')
    eileen "Hey."
    "Oh, there's that snarl again."
    show eileen handonhip eyesnarrow
    $ renpy.transition(dissolve, layer='master')
    eileen "I will do what I want, if I have reason to."
    show allison handsfolded troubled
    $ renpy.transition(dissolve, layer='master')
    allison "Can we not argue, please? It's club time, no fighting allowed."
    "She makes a quaint little X with her arms and{nw}"
    show eileen neutral
    show wallace neutral
    show allison handsfolded smile
    $ renpy.transition(dissolve, layer='master')
    extend " Eileen seems to simmer down a bit."

    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    eileen "Fine. Anyways, the picture isn't that bad. No reason to get self-conscious over it."
    oliver "Don't you hate me or something? Why are you praising my half-assed work?"
    show eileen angry
    $ renpy.transition(dissolve, layer='master')
    "She's certainly got a lot of nasty looks in her arsenal."
    eileen "Do you really think I'm going to waste my time dwelling on that? Allison said it's not a big deal because she was planning to redo the project before she dropped them."
    allison "Yep! It's fine, I promise. I'm sorry that I overreacted. I just spent a lot of time trying to make it look great so I got really upset when it broke."
    show allison holdarm smile
    show eileen neutral
    $ renpy.transition(dissolve, layer='master')
    allison "I hope Eileen didn't give you a hard time about it. I told her to be nice to you if you came by the art club, especially since Caprice wants you to join."
    oliver "Ah, not really."
    "Honestly, I don't deserve an apology, considering it was my fault."
    "It's like Allison exudes sunshine and rainbows, or something. She's the exact sort of person I try to avoid, because they make me feel worse about myself."
    "Some days I'm pretty sure I'm incapable of being cheerful, when people like her seem incapable of being anything {i}but{/i} cheerful."

    show bg classroom art:
        ease 3.0 xalign 0.9
    show caprice hattip at mirror:
        xanchor 0.5
        xpos 0.4
        yoffset -160
        ease 3.0 xpos -0.2
    show wallace neutral at mirror:
        xanchor 0.5
        xpos 0.2
        yoffset -175
        ease 1.5 xpos -0.2
    show eileen:
        xanchor 0.5
        xpos 0.75
        ease 2.0 xpos 0.55
    show allison holdarm:
        xanchor 0.5
        xpos 0.9
        ease 3.0 xpos 0.75
    "Looking from Allison to Eileen, I'm a little confused by their closeness, considering how cheerful and unusually kind Allison seems. I'm equally confused by how anyone is actually capable of telling Eileen what to do."

    show bg classroom art:
        ease 1.5 xalign 1.0
    show eileen at flip('eileen neutral'):
        ease 2.5 xpos 1.2
    show allison holdarm:
        ease 1.5 xpos 0.6
    "When Eileen stands up to go sharpen a pencil, I figure it's a good time to try talking to Allison."
    oliver "Hey, uh... sorry about bumping into you and then running off."
    show allison smile
    $ renpy.transition(dissolve, layer='master')
    allison "It's okay! I swear. You said you had to go to class, right?"
    oliver "Yeah, I was running sorta late."
    allison "Then it's especially no big deal! School comes first, especially for you, right?"
    "Ah, crap. Did Caprice tell everyone that I'm a loser failing out of college or something?"
    oliver "Yeah, I have to make sure I do well this year."
    show allison holdarm smile
    $ renpy.transition(dissolve, layer='master')
    allison "Alright, then I'll just hold you to helping me next time I break something."
    oliver "...Does that happen often?"
    show allison skirtgrab troubled
    $ renpy.transition(dissolve, layer='master')
    allison "Mmmaybe."
    "Caprice immediately takes control of the conversation, just as Eileen returns to the table."

    show bg classroom art:
        ease 2.5 xalign 0.5
    show caprice hattip smile eyesclosed mouthopen at mirror:
        xanchor 0.5
        xpos -0.2
        yoffset -160
        ease 2.5 xpos 0.35
    show allison holdarm smile:
        xanchor 0.5
        ease 1.5 xpos 0.65
    show eileen neutral:
        xanchor 0.5
        xpos 1.2
        ease 2.0 xpos 0.85
    $ renpy.transition(dissolve, layer='master')
    caprice "Anyways, everyone did a wonderful job! Awesome! Great, fantastic, super,"
    allison "Running out of synonyms, Caprice?"
    caprice "...Amazing!"
    show eileen mouthopen
    $ renpy.transition(dissolve, layer='master')
    eileen "Any more?"
    show caprice hattip neutral
    $ renpy.transition(dissolve, layer='master')
    caprice "Hmm. Abracada-brilliant?"
    oliver "I don't think that's a word."
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    caprice "We'll have none of that from you, mister! Now gimme!"

    hide caprice
    $ renpy.transition(dissolve, layer='master')
    "She snatches the work I consider no more than a sketch, and rushes over to a corkboard. On it, there's a bunch of artwork of varying qualities."
    caprice "This here is where everyone's first drawing goes! That way you can compare it to how amazing you'll be later."
    oliver "And if I don't continue drawing? What if I never come back here?"
    show caprice hattip smile eyesclosed mouthopen at mirror:
        xanchor 0.5
        xpos 0.35
        yoffset -160
    $ renpy.transition(dissolve, layer='master')
    caprice "As if that'd happen! The only way you're getting away is if you pick the other club and I know you're going to pick mine."
    show caprice hattip smile
    $ renpy.transition(dissolve, layer='master')
    caprice "Right? Right!"
    oliver "Uh, sure."
    hide eileen
    hide caprice
    hide allison
    $ renpy.transition(dissolve, layer='master')
    "It's starting to get late and I should head home soon. I have homework to do and classes to study for. I need to get ahead of myself if I'm going to survive work this weekend."

    show wallace neutral at mirror:
        xalign 0.5
        xpos -0.2
        ease 2.5 xpos 0.1
    show bg classroom art:
        xalign 0.5
        ease 2.5 xalign 0.0
    wallace "Hey, Oliver."
    "I stop for a brief moment to look at Wallace, scratching his beard."
    wallace "Don't pay any mind to that thing Caprice said about a little brother. I,{w=0.1} well{w=0.1}, don't see you like that and stuff. I'm just trying to be helpful."
    oliver "Oh,{w=0.1} uh. Don't sweat it. I may not know her well, but I don't think it's out of reason to think Caprice exaggerates things."
    "He nods quietly and{nw}"
    show wallace at nflip('wallace neutral'):
        xzoom 1.0
        time 0.4
        ease 1.5 xpos -0.2
    $ renpy.transition(dissolve, layer='master')
    extend " I pack up my things to get going."
    "Just as I'm heading out of the club room, I hear one last thing."
    allison "Good meeting, everyone!"
    
    stop ambiance fadeout 1.5
    stop music fadeout 2.5
    window hide smoothDissolve
    scene black with dissolve
return
