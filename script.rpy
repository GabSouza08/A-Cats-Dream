default lily = False
default pity_katie = False
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
default juju_rl = 0
default hunger_lv = 0
default ending = ""


# lynx is a black cat
# artur is pure orange energy and we all know it
# idk regarding mila
#

define cm = Character("Classmate")
define k = Character("Katie", color="5D6161")
define m = Character("Mila", color="FFFFFF")
define j = Character("Juju", color="FFDD8C")
define a = Character("Artur", color="FFAE00")
define l = Character("Lynx", color="525252")
define m_a = Character("Mila & Artur", color="FFFFFF")

define text_pool = [
    "Fight for what you believe in, okay?",
    "And we thought we could change fate.",
    "Mockery against heaven, is that what we became?",
    "Then, there was none.",
    "So, have you found a reason to fight yet?",
    "We are all slaves to history. Even after everything.",
    "Every dream we ever had could never save you.",
    "Katie, Katie, can you hear my plea?",
    "Artur is quicker than Juju. - Artur",
    "All the things she said, running through my head...",
    "Forgive me Mila, for i had a dream.",
    "Bleh.",

]


# TODO
# get some cat pics/assets
# find MORE pics of things at university
# more ao3 poems because yeah
# turn college kittens or a cats dream into a ao3 fandom
# finish chapter 1 aka prologue
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

    # 3. Exibimos a frase sorteada na tela
    show text "[lc_text]" with dissolve
    with Pause(3)

    hide text


label start:

    scene cchla_ext

    cm "Do you think, that maybe, there is a way out of this?"

    k "I think it does. But, am I truly the one meant to be answering this?"

    k "Do you take pity on me, just because i am another person soon to be jubilated?"

    menu:
        k "Do you, sir?"
        "I do not, because you deserved it, at the very end.":
            jump hardmode
        "I do, after all, we all are in this together.":
            $ pity_katie = True
            jump easymode

label hardmode:

    k "So, tell me. What is the purpose of such thing? Just to say your concept of justice is better than ours?"
    
    k "You are no different from those above us, you know that?"

    k "You are a traitor. A liar. And all... For what?"

    jump ch1

label easymode:
    
    k "I see. Then, at least at the very end you will give us a chance."

    k "Even if deep down, this is not the redemption we all hoped for."

    cm "So, its official. Love it, hate it, you are now free. For what, though? So, let it be."

    jump ch1

label ch1:

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

    show text "2 Hours later...." with dissolve
    with Pause(3)

    scene ccs_ext with dissolve
    with Pause(1)

    k "Ugh.. why do i feel.."

    k "{cps=60}WHAT-{/cps}" with vpunch

    k "{cps=60}I'm.... a cat?!?{/cps}"

    k "Great. that is all i needed."

    "You walk aimlessly by the streets of the campus."

    $ renpy.notify("You feel a little hungrier..")
    $ hunger_lv += 1

    scene demid_ext with dissolve

    k "Ugh, i am hungry. I heard some cats hijacked the RU, maybe i could join them or something."

    menu beginnings:
        k "Do i, or do i not?"
        "To be honest, i should. its easier.":
            jump ch1p2
        "Why would i do that, now that i come think of it?":
            $ a_free_soul = True
            jump ch1p2

label ch1p2:

    scene black with dissolve
    with Pause(1)

    if pity_katie:
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

    # play music "audio/in_caeli_fatuus.ogg"

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

        l "After all, those very rich cats eat from anything possibly, so can us."

        k "Yeah. So, food? How can i?"

        "Juju nuzzles by your side, as you try to get cozy in a cat's body"

        j "Aah... I guess we can find some food now."
        $ juju_rl += 1

        k "Am i that fluffy?"

        "I feel like my hunger level is at [hunger_lv]."

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
            "*You munch into the cat food. Hunger is now zero.*"
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
                "Nuzzle by Artur's side":
                    $ artur_rl += 1
                    $ nuzzlev2 = "Artur"
                    a "Heh, i knew you would quickly fall for the warmth of the cat army!"
                    l "Theres no cat army!"
                    a "Now there is!"
                    l "Fair."
                "Nuzzle by Lynx's side":
                    $ lynx_rl += 1
                    $ nuzzlev2 = "Lynx"
                    l "I love this, i cant lie. I crave the warmth of-"
                    j "Ohhh, finally something breaks the mask?"
                "Nuzzle by Juju's side":
                    $ juju_rl += 1
                    $ nuzzlev2 = "Juju"
                    j "*unintelligible noises*"

            
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


    return