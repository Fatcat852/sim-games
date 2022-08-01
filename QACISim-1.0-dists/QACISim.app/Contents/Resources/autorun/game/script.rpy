# Declare characters used by this game.

define m = Character("Melody",who_color="#b65ea5")
define g = Character("Gavin", who_color="#ff836e")
define o = Character("Mr. Ross", who_color="#3C4D6B")
define t1 = Character("Shady Guy", who_color="#F59551")
define fbt = Character("tam_who", who_color="#FCE859", dynamic=True, image="fbt")
define p = Character("player_name", who_color="#F59551", dynamic=True)
define gui.choice_button_text_idle_color = '#FFFFFF'
define Transition = Fade(0.5,1.5,0.5,color='#000000')

init:
    # melody
    image melody wave = Image("melody wave.PNG")
    image melody haha = Image("melody haha.PNG")
    image melody hmph = Image("melody hmph.PNG")
    image melody = Image("melody smile.PNG")
    # mr o
    image MrO = Image("Mr o.PNG")
    # tom
    image tom blink = Image("tom 2.png")
    image tom smile = Image("tom 4.png")
    image tom hmph = Image("tom 3.png")
    image tom = Image("tom.png")
    #fbt
    image fbt smile = Image("tammie smile.PNG")
    image fbt grr = Image("tammie grr.PNG")
    image fbt hmph = Image("tammie hmph.PNG")
    image fbt = Image("tammie.PNG")
    # backgrounds
    image bg room = Image("bg room.png")
    image game over = Image("game over.PNG")
    image gallery = Image("gallery.jpeg")
    image 507 = Image("507.JPG")
    # defaults
    define fadehold = Fade(0.5, 1.0, 0.5)
    default whiteuniform = False
    default blueuniform = False
    default nouniform = False
    default takemusic = False
    default taketheatre = False
    default takeart = False
    default pride = 0
    default passion = 0
    default persistence = 0
    default preparedness = 0
    default positivity = 0
    default principled = 0
    default gameover = False
    default variable = False
    # stat button


label start:
    show screen button
    scene bg room
    with dissolve
    play music "Audio/alarm.mp3"

    "BEEP. BEEP. BEEP. BEEP"

    play music "Audio/morning.mp3"

    "It's 8 o'clock already! You need get to school!"

    "It's your first day at your new school, the Queenland Academy for
    Creative Industries in Kelvin Grove. You're going to be late!"

    "What are you going to wear?"

    menu:
        "The full formal uniform":
            $ whiteuniform = True
            $ pride += 1

        "The blue day uniform":
            $ blueuniform = True

        "Whatever I want":
            $ nouniform = True

    "Okay, looking good. Let's go!"

    jump newschool

label newschool:
    show screen button
    scene gallery
    with Transition

    "You walk into the school but you have no idea where you're supposed to be.
    You wander around for a bit and end up in the gallery."

    show melody wave
    with dissolve
    play music "Audio/bg music.mp3"
    m "Hey, are you lost? You're in year 10 right? You missed the assembly."

    m "Say, what's your name?"

    $ player_name = renpy.input("What is your name?")

    if player_name == "":
        $ player_name = "Kyle"

    show melody
    m "Nice to meet you, [player_name]. My name's Melody. I'm in year 11.
        I'm a Matjiin house manager. What house are you in?"

    menu:
        "Matjiin":
            show melody haha
            m "Cool! We'll have so much fun together this year!"
        "Vivezza":
            show melody hmph
            m "Oh. Good luck with that."
        "Evellier":
            show melody hmph
            m "Hmm. Okay."

    if nouniform:
        show melody hmph
        m "By the way, why aren't you in your uniform? You look great,
        but you don't want to get busted by teachers on the first day."


    show melody
    m "Well, we need to get going. I can take you to your first class.
        What arts subject do you take?"

    menu:
        "Visual arts":
            $ takeart = True
            show melody haha
            m "Awesome! You'll have a great time in Mr. Ross's class."

        #"Theatre":
        #    $ taketheatre = True
        #    show melody haha
        #    m "Hey, me too! You're going to love it, Mr. Wilson is the best."

        #"Music":
        #    $ takemusic = True
        #    show melody haha
        #    m "Cool, you're going to have a lot of fun with Ms. Hopper this year!"

    jump connect1

label connect1:
    show screen button
    scene 507
    with Transition
    play music "Audio/Cheery.mp3"
    show MrO

    o "Hi everybody, welcome to connect! I'm your connect teacher, Mr. Ross."
    hide MrO

    "..."

    show tom
    t1 "Hey... You're in this connect too huh?"
    show tom hmph
    t1 "Connect is always so boring."
    show tom 2
    t1 "I want to go home."
    show tom
    t1 "Hey, what do you say we get out of here?"

    menu:
        "Yeah, let's go.":
            show tom smile
            t1 "Good..."
            $ gameover = True
            jump gameover

        "No, it's only my first day here. I need to go to class.":
            show tom hmph
            $ principled += 1
            t1 "Fine, suit yourself."

    hide tom
    show MrO

    o "Okay, everybody. It's time for your next class."
    o "[player_name], it looks like you have art next with me. Are you excited?"

    menu:
        "yes":
            $ passion += 1
            o "Awesome!"
            jump firstclass
        "no":
            $ gameover = True
            jump gameover


label firstclass:
    show screen button
    $ tam_who = "???"
    hide MrO
    scene 507
    "Where should I sit?"
    menu:
        "At the front":
            "Hmm, there isn’t anyone here."
            "Maybe you should take this opportunity to actually learn something this year."
            show fbt
            with dissolve
            fbt "Is this seat taken?"
            p "Uh, no.."
        "At the back":
            show fbt smile
            fbt "Heya! Do you want to sit here?"
            p "Yeah, Thanks."

    show fbt
    fbt "Hello, my name is Tammie, I’m in Vivezza!"
    $ tam_who = "Tammie"
    fbt @ smile "I can’t wait to start the lesson!!! Are you excited? I’m excited!"
    menu:
        "Yeah :)":
            $ positivity += 1
            fbt @ smile "Heehee, I can feel it! We are going to be best friends!"
        "Not really.":
            fbt @ hmph "Oh. Haha, I guess it's normal to also feel a little nervous."

    "..."

    hide fbt

    show MrO
    with easeinright
    o "Hey guys, I am Mr Ross. I will be your visual arts teacher this year. Welcome to Year 10 Viz arts at QACI!"
    o "This lesson we will be looking at the history behind the abstract art movement.."
    show MrO
    with Transition
    o "Alright, that's enough learning for today. Next time we'll actually be doing some drawing."
    jump lunch1

label lunch1:
    show screen button
    scene cafe
    with Transition
    play music "Audio/cafe.mp3"
    #$ variable = True
    "..."
    #$ variable = False
    "It's time for lunch. What are you having?"
    menu:
        "I'll buy something from the cafe":
            "You buy nice toasted bagel from the blue goose. Yum."
        "I packed my own lunch":
            $ preparedness += 1
            "Nice, you're super prepared for today."
            "...Besides being late, of course."
        "Nothing, I didn't bring lunch or any money":
            $ preparedness -= 1
            p "Welp. I'll guess just starve."



label gameover:
    if gameover:
        scene game over
        with Dissolve (5.0)
        play music "Audio/sad.mp3"

        "For some reason, it looks like your journey at QACI has ended."

        "Hopefully you had a good time."
    else:
        pass

    return
