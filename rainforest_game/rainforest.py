
import random
import time
import textwrap as tr


def print_pause(text, pause_time=1.4, extra_lines=1):

    dedented_text = " ".join(text.split())  # im not sure why dedent()
    # doesnt work here.
    print(tr.fill(dedented_text, 80))
    time.sleep(pause_time)

    for lines in range(0, extra_lines):
        print()


# options is a list of each option the user can select.
def select_options(prompt, options):
    dedented_prompt = " ".join(prompt.split())
    print(dedented_prompt)

    # join() is used to print combine strings.
    random.shuffle(options)  # randomize the order that users options appear
    options.insert(0, 0)  # begin the users options at 1 instead of 0.

    options_screen = "\n".join(f"Enter {key} to choose {option}."
                               for key, option
                               in enumerate(options[1:], 1))

    print()
    print(options_screen)
    print()

    while True:
        select_option = input("Your choice: ")

        try:
            # print(options[int(select_option)])
            if options[int(select_option)] == 0:
                print("please choose again.")
            else:
                return options[int(select_option)]

        except IndexError as ie:
            # print(f"{ie}")
            print("please choose again.")

        except ValueError as ve:
            # print(f"{ve}")
            print("please choose again.")


def patient_loop(items):
    count = 1
    waiting = False

    choose_cheat = select_options("""Do you want to head down the path or
    wait to be rescued?""", ["Take the path.", "Wait for help."])

    if choose_cheat == "Take the path.":
        print_pause("You start down the rainforest path.")

    elif choose_cheat == "Wait for help.":
        print_pause("""You sit down on a soft rock and wait for someone to
         come find you.""")
        waiting = True

    while waiting:
        # print(count)
        time.sleep(0.5)

        keep_waiting = select_options("Do you want to keep waiting?",
                                      ["Yes, keep waiting.",
                                       "No, head down the path."])
        if keep_waiting == "No, head down the path.":
            print_pause("Finally! Time to get going.")
            return False

        elif count == 3 and keep_waiting == "Yes, keep waiting.":
            print_pause("How much longer do you plan on waiting?")
            count += 1

        elif count == 5 and keep_waiting == "Yes, keep waiting.":
            print_pause("It might be time to get going.")
            count += 1

        elif count == 7 and keep_waiting == "Yes, keep waiting.":
            print_pause("""You hear loud rusting coming from the path in front
             of you.""")
            print_pause("""A second later a person wearing a hawaiian shirt
             carrying a backpack comes outif the rainforest.""")
            items.append("patience")
            return True

        else:
            print_pause("You contnue waiting.")
            count += 1


def stage1(items):
    berry_colors = ["wild berries", "raspberries", "blackberies", ]
    print("\n")

    print_pause("""A few hundred feet into the rainforest, you find many bushes
    full of bright berries.""")

    choose1 = select_options("""Do you want to gather some berries or
     continue on the path?""", ["Gather some berries.", "Keep walking."])

    if choose1 == "Gather some berries.":
        items.append("wild berries")
        print_pause("""You grab a handful of berries and carefully put them
         in your bag.""")
        print_pause("""You spin around towards the sound of crunching of
         twigs and leaves. You look for a while but you see nothing there.""")
        print_pause("You quickly return to the misty path and keep walking.")

    elif choose1 == "Keep walking.":
        print_pause("You keep walking down the misty path.")


def stage2(items):
    print("\n")

    print_pause("""Further down the path you come across a curtain of long
     vines before a golden light.""")
    choose2 = select_options("Do you want to see what's on the other side?",
                             ["yes", "no"])

    if choose2 == "yes":
        print_pause("""You push past the curtain of vines to find a backpack
         sitting in a small clearing.""")
        print_pause("""You take a few steps toward the bag to pick it up...""")
        print_pause("""Before you can get close enough an enormous gorilla
         drops down from the understory and stares directly at you.""")

        gorilla_choice = select_options("What do you do?",
                                        ["""Try to calm the gorilla down.""",
                                            "Try to scare the gorilla away.",
                                            "Try to escape from the gorilla"])

        gc1 = "Try to calm the gorilla down."
        if gorilla_choice == gc1 and "wild berries" in items:
            print_pause("""You quickly pull the berries out of your bag and
             toss them in front of the gorilla.""")
            print_pause("""The gorilla does a happy spin and begins eating the
             berries.""")
            print_pause("""You smoothly inch toward the bag, pick it
             up, and walk back toward the path before the gorilla finishes
              his snack.""")
            items.append("gorilla friend")

        elif gorilla_choice == "Try to calm the gorilla down.":
            print_pause("""You start swaying back and forth and singing
             'The Gambler'""")
            print_pause("""Before you can get to the chorus the gorilla
             tackles you and begins grooming you like a baby.""")
            print_pause("Looks like you'll be here for a while.")
            items.append("gorilla mom")

        elif gorilla_choice == "Try to scare the gorilla away.":
            print_pause("""You look the gorilla directly in the eyes and
             suddenly scream and shout at the top of your lungs, jump around
             everywhere, and start flailing your arms wildly!""")
            print_pause("""Suprised and threatened by your commotion the
             gorilla grabs the backpack, wildly swings it around hitting you
             in the back of the head, and runs off into the rainforest.""")
            print_pause("""You stand up dazed and off balance. Looking down
             you notice the backpack is gone.""")
            items.append("concussion")

        elif gorilla_choice == "Try to escape from the gorilla":
            print_pause("""You look at your feet, crouch down as low as you
             can, and quietly begin backing away from the gorilla back toward
             the path.""")
            print_pause("After a few moments you're back on the path.")

    elif choose2 == "no":
        print_pause("""You move on past the vines as the path begins to slope
        downhill.""")

    # print(items)


def stage3(items):

    if "gorilla mom" in items:  # the user loses if this condition is met.
        pass

    else:

        print("\n")

        print_pause("""As you walk further down the path it
        gets begins to get darker.
        You begin to feel more and more tired as the sun
        gets lower and lower.""")
        print_pause("""Now you can only see your feet and
        the path below you.""")
        print_pause("""Out of nowhere a small orb of light
        appears before you.
        It dances around for a few seconds before drifting
        off away from the path.""")
        choose3 = select_options("""Do you want to follow the
        floating light?""", ["yes", "no"])

        if choose3 == "yes":
            print_pause("""You rush out into the darkness after the
            magical light. You struggle to keep up as you trip over
            branches and plants on the ground.""")
            print_pause("""Just before the light fades from your view
            you jump out of the rainforest before a small shimmering river.""")
            print_pause("""After taking in the view you spot a wooden boat
            on the muddy shore.""")
            print_pause("""You climb inside the boat, pick up a wooden
            oar, and begin a relaxing ride down the river.""")
            items.append("wooden oar")

        elif choose3 == "no":
            print_pause("""Ignoring the light you push
             on down the path.""")
            print_pause("""Your drag yourself along the path,
            nearly collapsing from exhaustion.
            Looking up you can make out a small wooden cabin
             covered by the moonlight.""")
            print_pause("""As you approch a small lonely cabin
            you see a figure quickly
            move past a window. In the yard there are abandonded
             toys and broken dishes.""")
            print_pause("""You climb up the the steps and slowly
             approach the front door.""")

            if "gorilla friend" in items:
                print_pause("""You fish through the backback to find a rusty
                key. And it unlocks the cabin door!""")
                print_pause("""The door swings open revealing the rest of
                 your tour group! They welcome you back and you recall your
                  journey through the rainforest.""")

            else:
                print_pause("""You try to open the cabin door but it wont
                 budge. You turn around stumble back down the stairs.""")
                print_pause("""Your vison begins to blur and you look
                 up the see the same floating orb of light.""")
                print_pause("""The last thing you see is the
                 light growing brighter and brighter...""")


def intro():
    print_pause("""Oh no! You lost your group on tour group
     on a trip through the Amazon rainforest in Brazil!""")
    print_pause("""The emergency rendezous location is just a few
     miles west of where you are toward Rio Negro.""")
    print_pause("""You look around and see one path going
     into the misty rainforest.""")


def game(items):
    cheat_game = patient_loop(items)
    if not cheat_game:
        stage1(items)
        stage2(items)
        stage3(items)

    else:
        print_pause("""Your tour group came back to find you! They brought you
        food and water too!""")
        print_pause("Now you can continue on your tour.")


def outro(items):
    print("\n")

    if "backpack" in items or "wooden oar" in items or "patience" in items:
        print_pause("Great job you won the game!")

    else:
        print_pause("Sadly you didnt make it out of the rainforest.")

    review = select_options("Would you like to review your game performace?",
                            ["yes", "no"])

    if review:
        print_pause(f"You picked up: {len(items)} items.")
        print()

        for item in items:
            print(f"Award: {item.capitalize()}!")

            if item == "backpack":
                print_pause("""You made your way back to the tour group.
                 Congratulations!""")

            elif item == "wooden oar":
                print_pause("""You sailed back to Manaus, the capital of
                 Amazonas, all on your own!""")

            elif item == "gorilla friend":
                print_pause("""You made friends with a 400 pound
                 silverback gorilla WOW!""")

            elif item == "concussion":
                print_pause("""You took a hit from a gorilla! You're
                 lucky to be alive!""")

            elif item == "patience":
                print_pause("""You followed the first rule of survival
                 and it payed off!""")

            elif item == "gorilla mom":
                print_pause("""The gorilla got a little too attached
                 to you. Steve Irwin makes it look so easy right?""")

    else:
        pass

    replay = select_options("Would you like to try again?",
                            ["yes", "no"])

    if replay == "yes":
        print_pause("Get ready to play again!")
        print("\n")
        rainforest()

    elif replay == "no":
        print_pause("Thanks for playing!")


def rainforest():
    player_inventory = []

    intro()
    game(player_inventory)
    outro(player_inventory)


rainforest()
