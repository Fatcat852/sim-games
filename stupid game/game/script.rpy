# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Green Daddy",who_color="#02db2a")
define p = Character("Patrick", who_color="#ff836e")
init:
    image luigi dabbing = Image("luigi/dabbing.png")
    image luigi cool = Image("luigi/cool.png")
    image bg anime = Image("anime background.jpg")

define gui.choice_button_text_idle_color = '#242424'

label start:

    scene bg anime
    with fade
    $ renpy.music_start("audio/bg music.mp3")

    show luigi dabbing
    with dissolve

    l "Hello, my darling."

    l "How are you doing on this fine day?"

menu:
    "I'm fine.":
        jump fine

    "I'm kinda feeling down in the dumps.":
        jump dumps

label fine:

    l "Well, that is certainly good to hear! At least you're not horrible! or bad!
    But I guess you're not good either."
    l "I think I know what the problem is.. You're still single."

    show luigi cool at center
    l "Hmm... I think we'll have to do something about that."

    "You look down at the ground in order to avoid his gaze. There seems to be a speck of dirt on your newly polished shoe.
    Jeez louise! It's only 5 seconds in, and you're already tired of this conversation."
    "But before you can turn tail and run..."

    jump next

label dumps:

    l "Oh fiddlesticks!! I can't believe someone so magnificent, such as yourself, could be feeling \"down in the dumps.\"
    Oh, what a horrible thing it is indeed. I reckon I could cheer you right up.
    How 'bout it, would you like to go on a date with me?"

    "Immediately, you start regretting that you'd ever revealed anything to this short green man.
    But before you can turn down his offer..."

    jump next

label next:

    show luigi dabbing at right
    show patrick at left
    $ renpy.music_stop()

    p "Howdy y'all."

    # This ends the game.

    return
