default lily = False
default lynx_event = False
default mila_event = False
default juju_event = False
default artur_event = False
default let_her_go = False
default a_free_soul = False
default nuzzle = ""
default nuzzlev2 = ""
default artur_rl = 0
default lynx_rl = 0
default mila_rl = 0
default mila_rl_lynx = 0
default juju_rl = 0
default hunger_lv = 0
default lynx_pov = False
default pairing_m_l = False
default pairing_a_j = False
default pairing_k = ""
default ending = ""

init python:
    import random


# lynx is a black cat
# artur is pure orange energy and we all know it
# mila is a fluffy white cat
# juju is a tricolor cat. cool af.
# katie is a grey cat btw

#we are all witnesses to a tragedy.
#todo: write the act 3/4, and the endings. if bad = mila dies by a decorative lily, lynx follows her and eats the lily himself to join her,
#Artur loses it and sets lotta flowers on fire and accepts it, and Juju sees it and runs into the fire joining him, while Katie becomes a witness
#At last, Katie gets her expulsion revoked, thus waking up the other day as a normal person, but with all the memories of the chaos.
#also if its on the good ending, she immediately goes and gets the necessary things to contest the others expulsions, and they get revoked too.
#act 1 = yay food, act 2 is lore dumping, act 3 is separation and act 4 is finale or tragedy.

define cm = Character("Classmate")
define k = Character("Katie", color="5D6161")
define m = Character("Mila", color="FFFFFF")
define j = Character("Juju", color="FFDD8C")
define a = Character("Artur", color="FFAE00")
define l = Character("Lynx", color="525252")
define m_a = Character("Mila & Artur", color="FFFFFF")
define evr = Character("Everyone")

define text_pool = [
    "Fight for what you believe in, okay?",
    "And we thought we could change fate.",
    "Mockery against heaven, is that what we became?",
    "Then, there was none.",
    "So, have you found a reason to fight yet?",
    "We are all slaves to history. Even after everything....",
    "Every dream we ever had could never save you.",
    "Katie, Katie, can you hear my plea?",
    "Artur is quicker than Juju. - Artur",
    "All the things she said, running through my head...",
    "Forgive me Mila, for i had a dream.",
    "Bleh.",
    "Vae victis fortunarum!",
    "O luna, audi preces meas...",
    "This game is a banger, we lost 4 cats and a girl for it.",
    "Don't forget, i'm with you in the dark.",
    "We don't know no more aaaaa...?",
    "Without beginning or end, the world cycles upon the infinite.",
    "I have never hurt a fly, but i have got walls to climb!",
    "Tested on Linux, on a Google TV and on a Hackintosh. Those cats truly are lost, huh",
    "Quo vadis pater?",
    "This is not a rereading of 2023 events",
    "This is also not a rereading of 2026 events",
    "Hopefully this is also not a prophecy"
]


# TODO
# get some cat pics/assets
# find EVEN MORE pics of things at university
# more ao3 poems because yeah
# turn a cats dream into a ao3 fandom
# finish act 3
# add per cat relationship level

label splashscreen:

    scene black with dissolve

    show text "A Cat's Dream shall never die." with dissolve
    with Pause(3)

    hide text

    show text "Prototype in Development Phase." with dissolve
    with Pause(3)

    hide text

    $ lc_text = renpy.random.choice(text_pool)

    show text "[lc_text]" with dissolve
    with Pause(3)

    hide text

    scene cchla_ext

    cm "Do you think, that maybe, there is a way out of this?"

    k "I think it does. But, am I truly the one meant to be answering it?"

    k "Do you take pity on me, just because i am another person soon to be expelled?"

    k "Do you, sir?"
    
    cm "I do not, because you deserved it, at the very end."

    k "So, tell me. What is the purpose of such thing? Just to say your concept of justice is better than ours?"
    
    k "You are no different from those above us, you know that?"

    k "You are a traitor. A liar. And all... For what?"

    cm "So, its official. Love it, hate it, you are now free. For what, though? So, let it be."

    return


label start:
    jump a_dreamy_requiem #temporary testing

    scene black with dissolve
    with Pause(1)

    show text "Somewhere, in the outskirts of CCS..."
    with Pause(3)

    scene ccs_ext with dissolve
    with Pause(1)

    k "I feel weird. Why? Why did this happen? WHY?"

    "A dizzying sensation storms your heart."

    scene black
    with Pause(1)

    show text "Act 1 - Scattered Angels" with dissolve
    with Pause(3)

    show text "2 Hours later...." with dissolve
    with Pause(3)

    scene ccs_ext with dissolve
    with Pause(1)

    k "Ugh.. why do i feel.."

    k "{cps=60}WHAT-{/cps}" with vpunch

    k "{cps=60}I'm.... a cat?!?{/cps}"

    $ discord.update(state="Expelled and now turned cat.", details="Act 1/4 - Scattered Angels")

    k "Great. that is all i needed."

    "You walk aimlessly by the streets of the campus."

    $ renpy.notify("You feel a little hungrier..")
    $ hunger_lv += 1

    scene demid_ext with dissolve

    k "Ugh, i am hungry. I heard some cats hijacked the RU, maybe i could join them or something."

    menu beginnings:
        k "Do i, or do i not?"
        "To be honest, i should. It's easier.":
            pass
        "Why would i do that, now that i come think of it?":
            $ a_free_soul = True

    scene black with dissolve
    with Pause(1)

    if a_free_soul == False:
        show text "The flowers slowly bloom once more."
        with Pause(3)
    else:
        show text "The flowers wither once more."
        with Pause(3)

    hide text
    with Pause(1)
    scene ru_forest with dissolve

    "Huh? another cat? Though your appearance reignites a memory in me i seem to have forgotten..."

    k "{cps=14}Hello? \nhello?? \nWho are you? \nHi?{/cps}"

    "Well, i am myself!"

    k "Not funny, who are you?"

    "Guys, look, another friend!"

    m "I feel like she shall do a fine addition to our group!"

    m "I am Mila, and im pleased to meet you! \nThose are Artur, Juju and Lynx!"

    m "Soo, what brings you here?"

    if a_free_soul:
        k "I am just walking around here, okay."
    else:
        k "I was trying to find whoever stole food so i could have some."

    m "Ooh, i see! Well, i guess we could be companions for now and hopefully more."
    $ mila_rl += 1

    a "Do you think she could be chaotically good?"

    l "Please, Artur, just calm down for a moment."

    j "Well, the team now grows!"

    if not a_free_soul:
        k "Yeah, i guess it does. Not like i have any other option."

        k "Though im hungry. Why am i a cat? Do i eat the same as i would normally?"
        $ hunger_lv += 1

        l "Yeah, kinda. You can eat your former things, though in this form... I dont think we should."

        l "Even if those very rich cats eat from anything possibly, they have health checks and people to care, we don't."

        k "Yeah. So, food? How can i?"

        "Juju nuzzles by your side, as you try to get cozy in a cat's body"

        j "Aah... I guess we can find some food now."
        $ juju_rl += 1

        k "Am i that fluffy?"

        k "This body is so.... yeah."

        menu freepointsiguess:
            "I crave someone's warmth, i think."
            "Nuzzle by Mila's side":
                $ mila_rl += 1
                $ nuzzle = "Mila"
                m "Oh, darling. That's... You're cute, i will give you that."
            "Nuzzle by Artur's side":
                $ artur_rl += 1
                $ nuzzle = "Artur"
                a "Mmhmmmm... Okay okay, i got it, you're clingy, now lets go!"
            "Nuzzle by Lynx's side":
                $ lynx_rl += 1
                $ nuzzle = "Lynx"
                l "....I... what? Why? Uh, i guess... if you need it..."
            "Nuzzle by Juju's side":
                $ juju_rl += 1
                $ nuzzle = "Juju"
                j "Oh, this is nice.. I knew you would love this!"
            "Do nothing":
                $ nuzzle = ""
    
    "You keep wondering what this world has on store for you."

    if nuzzle != "" and not a_free_soul:

        k "I see theres at least a good thing about this."

        k "Maybe i will be cozy and this will all be alright. Hopefully."

        m "That's all we all hope, miss."
        
    m "What is your name, also, may i ask?"

    k "I'm Katie."

    m "That's a pretty name!"

    a "Could be fate. Katie, Cat, whatever. *streches himself*"

    j "Geez, Artur. Already on the jokes?"

    l "Yeah.... Artur could make jokes about anything... *yawns*"

    k "I see.."

    k "Wait, is that girl putting food there? Wasn't it banned?"

    m "Yeah, silly, it was banned. They cannot feed the cats..."

    m_a "But they did not ban discarding foods where cats could reach them!"

    menu stay_or_eat:
        "Stay by their side and wait":
            m "So, i guess we can go now."
            a "I agree, I am just as hungry."
            l "....if you were calmer, maybe you would not?"
            a "Come on, Lynx. just stop being so... tired."
 
            menu who_is_right:
                "Well, calm down both, after all..."
                "...Lynx is right about you, Artur.":
                    $ lynx_rl += 1
                "...Artur is right about you, Lynx.":
                    $ artur_rl += 1
            
            k "But both have your own opinions, so lets just eat. I am hungry!"
            "*You munch into the cat food. You feel no more hunger, for now.*"
            $ hunger_lv = 0
            
        "Eat it":
            "*You quickly go and munch into the food spilled on the floor. You feel better now.*"
            $ hunger_lv = 0

    k "Anyways, I feel better now, thank you."

    menu next_action:
        "Nuzzle on someone?":
            menu nuzzle_choice:
                "Nuzzle by Mila's side":
                    $ mila_rl += 1
                    $ nuzzlev2 = "Mila"
                    m "Mhmm, okay, okay, i see. Just relax, or i will think you like this!"
                    j "Don't you, though?"
                    m "Yeah!"
                    j "So be happy for it!!"
                    $ discord.update(state="Fangirling for Mila", details="Act 1/4 - Scattered Angels")
                "Nuzzle by Artur's side":
                    $ artur_rl += 1
                    $ nuzzlev2 = "Artur"
                    a "Heh, i knew you would quickly fall for the warmth of the cat army!"
                    l "Theres no cat army!"
                    a "Now there is!"
                    l "Fair."
                    $ discord.update(state="Rejoicing with Artur", details="Act 1/4 - Scattered Angels")
                "Nuzzle by Lynx's side":
                    $ lynx_rl += 1
                    $ nuzzlev2 = "Lynx"
                    l "I love this, i cant lie. I crave the warmth of-"
                    j "Ohhh, finally something breaks the mask?"
                    l "Ugh. I can feel, okay?"
                    $ discord.update(state="Feeling loved with Lynx", details="Act 1/4 - Scattered Angels")
                "Nuzzle by Juju's side":
                    $ juju_rl += 1
                    $ nuzzlev2 = "Juju"
                    j "*unintelligible noises*"
                    j "*more unintelligible noises*"
                    a "And i am the most chaotic here."
                    $ discord.update(state="Embracing the chaos of Juju", details="Act 1/4 - Scattered Angels")

            
            "You feel a bit closer to them now."
            
        "Sleep?":
            "*You decide to sleep peacefully.*"
            
        "Stretch and walk a little?":
            "*You walk a little, as they keep eating.*"
    
    scene black with dissolve

    show text "Some hours later..."
    with Pause(3)

    scene ru with dissolve

    a "So, what is our first adventure going to possibly be?"

    k "Adventure? I just woke up!"

    l "....zzzzz"

    m "I agree with Lynx over there."

    j "Yeah."

    k "Sooo?"

    m "We are tired, at least half of us, don't worry."

    k "Thankfully, yeah."

    m "Is there any place you want to go?"

    l "...Huh? go somewhere? *yawns*"

    m "Oh, my! Guess the sleepyhead woke up."

    l "...I smell someone. *walks inside the RU*"

    scene black

    k "I think i have seen this person somewhere."

    "From here i can see him nuzzling into her incessantly. But why?"

    "I must remember i am here to..."

    "...Why am i here...?"

    m "Are you fine? You closed your eyes while still standing!"

    scene ru with dissolve

    k "I am fine, no worry!"

    m "I really hope!"

    k "But who is she?"

    m "Someone from his past. I think."

    a "Nothing we should worry, though!"

    a "Hopefully."

    "Lynx comes back, seemingly happier."

    l "Missed me?"

    m "*looks at him surprised*"

    k "You liked that girl, didnt you? Smelling her from a mile away.."

    l "Yeah, i did. Now what? Am i not allowed to savour the scent of someone i ought to love but never could because i have been confined to this body?"

    k "No need to-"

    l "Am i not? Oh, come on. My shyness stood on my way for so long, and even if i want to go back, this form allows me to get closer to what i crave."

    j "Don't mind him, Katie! He's like a moth to the moon. No way of him to change until his love burns him down-"

    a "HEY, DONT SAY THAT!"

    j "Wow. I mean, this is chaos, but hey."

    k "What's her name?"

    l "Not saying it."

    m "Anyways... let us talk about something nicer, okay?"

    scene black with dissolve

    show text "Act 1 Finished." with dissolve
    with Pause(3)
    hide text

    show text "Act 2 - Ruptures Across Memories" with dissolve
    with Pause(3)

    $ discord.update(state="Investigating this chaos...", details="Act 2/4 - Ruptures Across Memories")
    hide text

    scene cchla_ext with fade

    a "Soooo..."

    m "Just say already what you want, Artur!"

    j "Huh? Mila? Are you alright?"

    m "This place brings me bad memories. I..."

    "I see."

    m "Ugh. it's not your fault anyways."

    m "Neither it was mine."

    a "Come on, cheer up! At least you didn't set fire to a lab accidentally!"

    evr "WHAT THE-" with vpunch

    m "WHAT DID YOU DO?" with hpunch

    j "OOOH IT WAS YOU?" with vpunch

    l "Can we please calm down?"

    m "Still not worse than the false accusations they put on me."

    m "I was such a nice person to everyone!"

    m "And what they did? They poisoned the drinks of everyone during the yearly course party!"

    l "*listening eagerly*"

    m "They blamed ME for it. \nAnd i had no reason to do it. But they didnt believe. And... and..."

    menu:
        "...."
        "Nudge Lynx to comfort her":
            l "Me? Okay."
            k "You know her more."
            "*Lynx nuzzles on her gently.*"
            l "It will be all be fine."
            $ pairing_m_l = True
            $ lynx_rl += 1
            $ discord.update(state="Being a winglady to Lynx", details="Act 2/4 - Ruptures Across Memories")

        "Try to comfort her":
            $ mila_rl += 1
            "*You nuzzle on her gently*"
            m "Thanks, Katie."
            
        "Wait":
            pass
        
    m "It was strange, though. I wanted to prove it was a lie."

    m "'Excuse me sir, there must be someone you confused me for!'"

    m "If i could only see someone who knew me or someone who cared for..."

    m "But, its better that way."

    a "Yeah. Now you have... friends!"

    if pairing_m_l == True:
        l "And love, if you try enough."
    else:
        l "No love though, Artur. And we all need it."

    a "I see. *looks at Juju.*"

    j "Why are you looking at me??"

    a "Nothing! It's not like i should look at someone in the center of the chaos!"

    j "Then come on and run from it!"

    "*She dashes away. Artur quickly follows*"

    l "Come on!"
    
    "*Mila runs behind them. And so does Lynx*"

    k "Wait for me!"

    scene black with dissolve 
    with Pause(2)
    
    show text "A few minutes later, somewhere else..."
    with Pause(3)
    
    hide text

    scene ccsa_ext with fade

    l "It was a cold and quiet day."

    l "I was just hoping this day to be like any another."

    l "But..."    

    l "A minor mistake led to a short circuit.."

    l "And that, in turn, ruined everything."

    m "*Listening intently*"

    l "It's... strange. You do a lot of good things, and no one remembers you. \nBut you do a silly mistake..."

    j "And they reduce you to that. At the end, we all have our reasons to be here. But...."

    j "Did we really deserve that? One mistake erasing all good we ever did?"

    j "It's surely an hypocrisy."

    a "Yeah. Were we all good at what we did?"

    m "That's what it looks like."

    k "Sooo..."

    k "What about you, Juju? Lynx caused a short circuit, Mila was accused of poisoning, Artur set fire... \nAnd you?"

    j "I tried to run away from this, but, okay. I..."

    j "I don't know!"

    j "It was meant to be just a silly joke!"

    j "But, some things happened, and, of course i tried to run away!"

    j "Sadly or not, i broke some things on the way and the college rep was destroyed."

    a "..."

    a "Pretty cool i guess?"    

    a "Hopefully."

    a "I mean, theres not much i can say."

    menu:
        k "Hm.."
        "*pssst* Artur, nudge on her!":
            a "Sure, seems a better idea!"
            $ pairing_a_j = True
        "Wait...":
            pass
        
    
    k "And i was expelled due to a riot. I mean, antifacist riot but-"

    l "HE WON?"

    k "Not yet, its in two days. but things seem grim."

    l "I see. But, like-"

    "*suddenly someone passing by says something and grabs artur*"

    a "Hey, let me go!"

    "*some other people also grab mila and juju, and before you know, also lynx. Leaving you, Katie, alone.*"

    k "Oh damn it. Ugh, those pesky people. I will find you."

    scene black with dissolve

    show text "Act 2 Finished." with dissolve
    with Pause(3)
    hide text

    show text "Act 3 - Across Our Lovely Reverie" with dissolve
    with Pause(3)

    hide text

    menu:
            "Who do i search..."
            "Mila":
                $ discord.update(state="Chasing a benevolent angel...", details="Act 3/4 - Across Our Lovely Reverie")
                k "I think that girl was from a close department. I will just follow her..."
                scene ce_lounge with dissolve
                m "Mhm."
                "Mila is limp on someone's arms. Guess she's truly one of these ragdoll cats."
                m "Oh, Katie, you're here."
                k "Yeah, you seem to be happy huh."
                $ mila_rl += 1
                m "I am, but even so id rather be with the rest of you."
                k "I see, thank you i guesss?"
                m "So much to wonder. Can i stay here?"
                k "Can you even leave, actually?"
                "*Mila tries to move, but to no avail*"
                k "Eh. Guess we gotta wait. I don't know the time but i guess soon they will need to go to their class and leave you here."
            "Lynx":
                $ discord.update(state="Chasing a hopeful soul...", details="Act 3/4 - Across Our Lovely Reverie")
                k "I know that guy, let me follow him now!"
                scene ru_ext with dissolve
                l "I swear people used to say black cats are a bad omen. So why did they also pick me!"
                k "You're fluffy."
                $ lynx_rl += 1
                if pairing_m_l == True:
                    l "Mila is more fluffy!"
                    k "Oh, the king can't spend a moment without talking about the queen."
                    l "*blusheyour thought on this as is and songs it reminds you of, and why?s, or would if his cat form allowed him* \nI... COME ON KATIE! \n*Sighs, though shaking his head*"
                k "So, any idea of how to get rid of... *looks at the student holding him*"
                l "No, i dont."
                "*A minute or two later, a bus passes, and the student leaves him to go on the bus*"
                l "Finally. I crave the warmth of someone, not theirs though."
                l "I wonder, though. One of they had a cross. I was taught that cats don't go to heaven, because no soul."
                "You listen intently."
                l "Does that mean we are condemned out of heaven just because we became this, no matter what our actions were?"
                k "Woah, so deep thoughts outta nowhere."
                l "I know, but, like, does a god so lovingly to make many creations decides to throw those who cannot worship him?"
                l "Why? Does the fact we became something other than what he set us as makes us a instant sin meant to be erased?"
                k "I didn't become a cat just to be still reflecting on religious things, please!"
                l "And now that i think, it's not only about cats that this applies to."
                k "What matters is not what form you have been given, only the form you see yourself as, the one you truly are."
                $ lynx_rl += 1
                l "Thanks...?"
            "Juju":
                $ discord.update(state="Chasing a lovely dream...", details="Act 3/4 - Across Our Lovely Reverie")
                k "Ugh, come on, Juju i will find you!"
                scene demid with dissolve
                "*You sighted Juju. She seems to be barely evading them. Thus you meow loudly at them*"
                j "Thanks for the distraction! *manages to run away from the colleague looking on your direction*" with hpunch
                $ juju_rl += 1
                j "They think calico is something insanely rare, but when theres literal nebelungs and york chocolates... yeah"
                k "I am a nebelung? I mean, i didn't see a mirror yet..."
                j "Yeah, a fluffy, quiet nebelung. And im what, a shorthair calico?"
                k "I didn't study it much, you know? The cat knower is lynx, wherever he is."
                j "Hey, we are fine! Don't worry, we can just find the rest now i guess!"
                k "Yeah, any ideas though?"
            "Artur":
                $ discord.update(state="Chasing a chaotic memory...", details="Act 3/4 - Across Our Lovely Reverie")
                k "Poor Artur, though maybe he will have fun with this."
                scene demid_ext with dissolve
                "*Someone is playing with Artur. As soon as he sights me, he lets a sigh of relief.*"
                a "Katie, finally! It's not the best thing to be passed around like a fluffy ball!"
                $ artur_rl += 1
                k "Yeah, i see. Though it feels nice, from a distance obviously."
                if pairing_a_j == True:
                    k "Do you think Juju already ran away from those people at this type?"
                    a "She's surely quick, i believe she is looong gone. "
                    k "You look proud of her, huh."
                    a "We must be proud of our friends!"
                    k "I know, but... Hm... Guess you found a new liking other than chemistry."
                    a "HEEEEY- \n*tries to get out to go at her, to no avail*"
                k "Guess you will be there for a long time."
                a "Noooooooooooo-"
        
    return


label at_worlds_end:

    scene black with dissolve 
    with Pause(2)
    
    show text "Without love or hope, the Angel stands at the World's Edge"
    with Pause(3)
    hide text

    show text "At heaven's gate, we stand alone, as our pleas, inevitably, go unheard."
    with Pause(3)
    hide text

    l "Artur, Mate. Eh, my heart fails to comprehend why did you do this. Ah, my time is ticking down."

    l "A hope like ours won't help me now."

    a "So go on and fight me, that's what you do best."

    a "I preferred when your codename was 'Lunaria Umbrosa', after all, you always hide beneath the moon."

    l "Says the 'Corona Vana', and 'his' fallen partner, 'Musa Mortua'."

    $ lynx_hp = 10
    $ artur_hp = 10
    $ incoming_damage = 0
    $ lynx_warned_75 = False
    $ lynx_warned_40 = False
    $ lynx_warned_10 = False
    $ artur_warned_75 = False
    $ artur_warned_40 = False
    $ artur_warned_10 = False
    while lynx_hp > 0 and artur_hp > 0:
        "Lynx: [lynx_hp]/10. Artur: [artur_hp]/10."

        menu:
            "Strike":
                $ artur_hp = max(0, artur_hp - 2)
                $ incoming_damage = 2
                "You try to strike upon him."

            "Brace":
                $ incoming_damage = 1
                "You brace for what fate will throw next."

            "Speak":
                $ incoming_damage = 1
                l "Why did you do this??"
                a "Stop talking and fight!"

        if artur_hp > 0:
            $ lynx_hp = max(0, lynx_hp - incoming_damage)
            "Artur moves before you can react."

        if artur_hp <= 7 and not artur_warned_75:
            $ artur_warned_75 = True
            a "What are you doing, 'Lynx'? Just me, and you, for what?"
        if artur_hp <= 4 and not artur_warned_40:
            $ artur_warned_40 = True
            a "No! You were meant to be a friend! Why?"
        if artur_hp <= 1 and not artur_warned_10:
            $ artur_warned_10 = True
            a "You hide in the shadows of your sins... You... You know #@*% doesn't care, right?"

        if lynx_hp <= 7 and not lynx_warned_75:
            $ lynx_warned_75 = True
            l "So, have you found someone to fight for yet?"
        if lynx_hp <= 4 and not lynx_warned_40:
            $ lynx_warned_40 = True
            l "Join me in our last dance!"
        if lynx_hp <= 1 and not lynx_warned_10:
            $ lynx_warned_10 = True
            l "Forgive me, ,{+*, for i had a dream."

    if lynx_hp <= 0:
        a "An Jack becomes a King. Whoever is dealing the cards today... Ugh."
    else:
        l "What's the purpose of this 'Corona Vana'? The Jack always fall to a King."

    $ lynx_event = True

    return

label a_dreamy_requiem:
    $ lynx_pov = True

    "You feel a weird feeling."

    "You see Mila with a flower."

    "Is that a lily?"

    scene cg1

    l "Mila, NO!"

    "But it was too late."

    l "Mila, SPIT IT, SPIT-"

    m "Why?"

    l "Didn't you read my message that day?? ITS TOXIC, GET IT OUT!"

    "*Mila rushes to spit it out*"

    l "Okay, uh, come on, its.... Its letal!"

    l "I dont think anyone can hear us."

    $ mila_event = True

    m "I want to believe this is...."

    l "Keep believing, then! Why didnt you heed my warning!"

    m "{cps=28}I....{/cps}"

    m "{cps=26}I don't know... G- Lynx.{/cps}"
    $ mila_rl_lynx = 0

    m "{cps=24}It just... just seemed nice. And pretty.{/cps}"
    $ mila_rl_lynx = 1

    m "{cps=22}I was walking and some student put it on my head..{/cps}"
    $ mila_rl_lynx = 2

    m "{cps=20}And gosh, i looked pretty.{/cps}"
    $ mila_rl_lynx = 4

    m "{cps=18}For once... i understand why did you say i made you feel alive.{/cps}"
    $ mila_rl_lynx = 6

    m "{cps=16}But it's ironic, isn't it?{/cps}"
    $ mila_rl_lynx = 8

    m "{cps=14}On the end... I am just... #my. Just another...{/cps}"
    $ mila_rl_lynx = 10

    l "Stop! You're... Come on, "

    m "{cps=12}This is so quick. Am i such a fragile doll?{/cps}"
    $ mila_rl_lynx = 20

    "You nuzzle into her. Desperately."
    $ mila_rl_lynx = 30

    m "{cps=10}No, i cant, dont give up..{/cps}"
    $ mila_rl_lynx = 40

    m "{cps=9}Despite everything, you still remain here. You're so stubborn, Lynx. Hehe. I always loved this about you.{/cps}"
    $ mila_rl_lynx = 50
    
    m "{cps=8}I didn't realize who it was at first...{/cps}"
    $ mila_rl_lynx = 60

    m "{cps=7}But deep down...{/cps}"
    $ mila_rl_lynx = 70

    m "{cps=6}As you said...{/cps}"
    $ mila_rl_lynx = 80

    m "{cps=5}You'd always find me.{/cps}"
    $ mila_rl_lynx = 100

    "You are tearing your mind apart, as you keep on trying to ground yourself in her."
    $ mila_rl_lynx = 200

    "You don't care about your omission, her errors, on the end..."
    $ mila_rl_lynx = 300

    "You just have a single question."
    $ mila_rl_lynx = 400

    l "May I Love Again? MILA?"
    $ mila_rl_lynx = 500

    m "{cps=4}So... stubborn...{/cps}"
    $ mila_rl_lynx = 1000

    m "{cps=3}But...{/cps}"
    $ mila_rl_lynx = 2000

    m "{cps=2}Just like they said..{/cps}"
    $ mila_rl_lynx = 3000

    m "{cps=1}I..{/cps}"
    $ mila_rl_lynx = 4000

    m "{cps=1}...love...{/cps}"
    $ mila_rl_lynx = 5000

    m "{cps=1}...you.{/cps}"
    $ mila_rl_lynx = 9999

    "And then, there was none."

    menu optional_name:
        "You see the lily by her side."
        "Eat the lily.":
            jump heaven
        "Eat the lily.":
            jump heaven
        "Eat the lily.":
            jump heaven
        "Eat the lily.":
            jump heaven
        "Eat the lily.":
            jump heaven
        "Eat the lily.":
            jump heaven
        "Eat the lily.":
            jump heaven
        "Eat the lily.":
            jump heaven
        "Eat the lily.":
            jump heaven
        "Eat the lily.":
            jump heaven
        "Abandon her":
            pass

    l "I... i.... aaaah!"

    "You run away."

label heaven:

    scene black with dissolve 
    with Pause(2)
    
    show text "In your heaven, I rest."
    with Pause(3)
    hide text with dissolve

    show text "In your heaven, I SHALL rest..."
    with Pause(3)
    hide text with dissolve
    
    show text "Act 749189472148 C&*#PLETE"
    with Pause(3)
    hide text with dissolve
    $ discord.update(state="Dead.", details="???????")

    show text "Act ???? - a!Ç^)_."
    $ renpy.force_autosave()
    with Pause(3)
    hide text with dissolve

    jump love


label love:
    $ fate_roll = random.SystemRandom().randint(1, 20)
    "The die lands on [fate_roll]."

    if fate_roll == 1:
        python:
            raise RuntimeError("Could not find a continuation for label 'love'.")

    $ can_leave = fate_roll >= 11
    call screen love_traceback(fate_roll, can_leave)

    if _return == "follow_artur":
        jump love_follow_artur
    elif _return == "follow_juju":
        jump love_follow_juju

    return


label love_follow_artur:
    $ lynx_pov = False
    "POV changed to Artur."
    return


label love_follow_juju:
    $ lynx_pov = False
    "POV changed to Juju"
