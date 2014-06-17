label scene_1S17_en:
#######################
    # Act 1, Scene 17
    # The Actor
    # Heather is silly
    call switch_scene_sx('bg hallway 3', 'bg hallway 1', False, { 'xalign': 1.0 })
    play ambiance "sfx/ambiance/crowd_inner.ogg"

    "After classes, I suddenly feel like I'm being followed. Who or why, I'm unsure, really."
    "It could be anyone at this point. It could be either of the two clubs' lackeys, or it could just be my imagination. Maybe Eileen's come to take revenge for Allison's project, or Tanya's going to extort me for lunch money, or something."
    "I don't know."
    "I'm trying to shake them by walking faster, but I swear I can hear their footsteps behind me still."
    "Time for a little creativity."
    "I speed up my pace, heading for a stairwell. I duck underneath it quick, then pop out once they've passed. Textbook \"ditch the bully\" tactic I learned back in middleschool."
    "Ducking behind it, I can hear them speak out loud."
    unknown "...Where'd he go?"
    oliver "Excuse me."

    show heather shout:
        xanchor 0.5
        xpos 0.5
        yoffset 0
    $ renpy.transition(dissolve, layer='master')
    "The girl that comes into focus spins around in surprise."
    heather "There you are.{nw}"
    show heather skeptical
    $ renpy.transition(dissolve, layer='master')
    extend " I'm here to give you a warning."
    stop ambiance fadeout 1.5
    play music "music/tense.ogg" fadein 2.0
    "I'm not sure what kind of warning this is going to be, or whether I even want to hear it. Mostly because of how she's saying all this in such a life-or-death tone."
    oliver "I'm not going to hit on Mekki. Can you never follow me again?"
    heather "That's not the warning I'm trying to give you. Do you know what Mekki's like, as a person who is in charge of a club?"
    oliver "...No? I've been there one day. I hardly know her."
    heather "Think about it. You saw all those rules she has.{nw}"
    show heather skeptical mouthopen
    $ renpy.transition(dissolve, layer='master')
    extend " She and a few people run that club like it's some kind of dictatorship."
    "I think my look of skepticism makes her go on the offensive a bit more."
    
    show heather handoncheek skeptical mouthopen
    $ renpy.transition(dissolve, layer='master')
    heather "Look, are you really this naive?"
    oliver "Excuse me?"
    heather "You're like a big, dumb plot device for these two. You fall almost out of nowhere, right into their laps; a way to settle who's right or wrong."
    oliver "I'm pretty sure I have nothing to do with their argument."
    heather "Maybe not directly, but you're becoming a piece in their little war of attrition."
    "I've had this feeling for a while, but man – I really didn't want to hear someone else thinking it."
    show heather handoncheek skeptical
    $ renpy.transition(dissolve, layer='master')
    heather "Think about it. When have you ever come into a room filled with people who look excited to see you?"
    "I scowl, just out of instinct."
    heather "Exactly. Do you just think everyone in the writing club is just being nice because you're a new recruit? Especially after every little social faux pas that you've made along the way?"
    "I think I'd crumple if I was made of paper. No one can already know all that. She has to be fishing."
    heather "Mekki is playing you, and using everyone in her own club to make you believe it. The writing club isn't as great as she's trying to make it seem."
    show heather skeptical
    $ renpy.transition(dissolve, layer='master') 
    heather "She whined during the club intentionally to indirectly give Tanya the idea to go get you. Tanya's a good person, but not exceptionally bright and equally predictable."
    heather "She asked us all to put on our best show so that you'd pick our little group of teamsters over Caprice's. She just wants to beat Caprice, who always has one over her."
    oliver "...What do you get out of this? I don't understand."
    show heather skeptical mouthopen
    heather "Pardon?"
    oliver "This is all right up my alley of believability, and I guess you think you're some sort of wise, scholarly writer who has a complete grasp of{nw}"
    show heather smirk
    $ renpy.transition(dissolve, layer='master')
    extend " everyone she lays eyes on."
    oliver "So, naturally, I'd jump right to the most negative conclusions. I'm sure you think I've been dwelling on them, and now you're trying to reinforce them."
    show heather skeptical
    $ renpy.transition(dissolve, layer='master')
    oliver "Why?"

    "Heather seems non-commital at best."
    heather "I'm just trying to help out. I figured you should know, before you go making choices based on an elaborate facade."
    oliver "Well, I guess you underestimated how much of a cynic I am. Why would you help me, right now?"
    "Maybe I just want to disagree with her because she seems so smug and self-assured all the time. This chick feels way more suspicious than how transparent Mekki and Caprice are being about my value to them."
    show heather handoncheek skeptical mouthopen
    $ renpy.transition(dissolve, layer='master')
    oliver "Why would you try to help me now, after having played along with Mekki's wishes?"
    heather "Perhaps I'm intentionally deceiving you?"
    oliver "Probably. I still don't understand why you would, though."
    show heather handoncheek skeptical
    $ renpy.transition(dissolve, layer='master')
    heather "What if I am lying, what does that narrow things down to?"
    oliver "Not sure. This whole warning thing doesn't make sense."
    oliver "The only reason you'd lie is to keep me away from the club. Again, why?"
    show heather handoncheek grin eyesclosed
    $ renpy.transition(dissolve, layer='master')
    "Heather's laughing in a way that makes me feel like this entire thing is some elaborate web of annoying crap I just don't want to deal with right now."
    show heather smile
    $ renpy.transition(dissolve, layer='master')
    "I guess she's got my curiosity piqued, anyways."
    "Something clicks in my head."
    oliver "You were teasing Mekki when she came over to talk. This is really childish logic, but the old rule says you only tease people you like."
    oliver "How big is the writing club?"
    heather "Not extremely."
    oliver "When was it that the last person joined?"
    show heather skeptical
    $ renpy.transition(dissolve, layer='master')
    heather "... A while ago."
    "Okay, I think I can spin this into something. If she's teasing Mekki and enjoys seeing her reactions and we're going by that old rule,"
    "Heather probably is a close friend of Mekkis, or enjoys her company. Something like that. If that's irrelevant and this whole thing is a lie, then the only thing I can think of is that she's trying to scare me away for some reason."
    "Now lets see if I can say that without making a fool of myself."
    oliver "Well, either you have some strange need for Mekki's attention which you wouldn't get if she was attending to some newcomer, or you're trying to protect the club by testing new people and scaring them away if you think they might be bad for the club."
    oliver "One's selfish and one isn't as much, but both are probably hurting the club."
    heather "So, which is it?"
    oliver "I don't think which it is matters, really. I have no choice. I have to pick one of them."
    oliver "If I pick the writing club, I'm going to pick it and she's going to help me pass my class. That's the deal. I don't need someone like you trying to undermine that, so-"
    "Two other college students walk by while I'm starting to break into a rant."
    stop music fadeout 2.5

    unknown "Hey Heather!"
    show heather grin away
    $ renpy.transition(dissolve, layer='master')
    heather "Hey, how's it going?"
    unknown "Not too bad, when's the next movie night?"
    heather "Hmmm, I'm not sure! Just keep an eye out and I'm sure you'll know when the next showing is, 'kay?"
    unknown "Sounds good, see you around!"
    "...What?"
    "That was a complete personality change."
    show heather smile
    $ renpy.transition(dissolve, layer='master')
    heather "Well, Oliver,"
    heather "The truth is I was just testing you to see how you'd react. I think you reacted well. You dissected a deception, unearthed what was almost the truth. Not bad for someone like you."
    "What's that supposed to mean?"
    "Either way, she's back to being cold and calculating. Can the bubbly girl come back? She seemed more friendly and less like a b-"
    show heather skeptical
    $ renpy.transition(dissolve, layer='master')
    heather "Mekki works pretty hard just trying to keep the club from collapsing in on itself. Encouraging writing, writing her own work, keeping up with some hard classes, a job and her finances. Now she's offering to tutor you for free."
    heather "Tanya and I aren't the only ones who are trying to help her out. She's not the kind to ever ask for help, and everyone knows it. Tanya's the muscle, I'm the brains. I just wanted to see where you stood."
    oliver "Okay, great. Did I pass your dumb little test? I want to go grab some food before I go back home."
    show heather smile
    $ renpy.transition(dissolve, layer='master')
    heather "I think you did well enough."
    show heather:
        xanchor 0.5
        xpos 0.5
        yoffset 0
        ease 2.5 xpos 0.1
    $ renpy.transition(dissolve, layer='master')
    "With that, she turns and walks away, like nothing of importance happened."
    show heather at flip('heather smile')
    "Just before she's out of sight, Heather turns and does tell me one last thing."
    heather "Oh, one last thing. I was telling the truth about Mekki asking us to try to win you over."
    show heather at nflip('heather smile'):
        xzoom 1.0
        time 0.4
        ease 2.0 xpos -0.2
    "While she's walking away, I swear she's humming a tune."
    "I'd like it if I could hold a tune, but all I can do is grumble."

    window hide smoothDissolve
    scene black with dissolve
return
