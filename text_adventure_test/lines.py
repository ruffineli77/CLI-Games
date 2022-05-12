
import time

begin_game = "Prepare yourself. Your journey is about to begin..."
change_settings = "Enter 1 to change difficulty, 2 to change 3 to change 4 to change character name"
quit_game = "Thanks for playing!"


story_overview = """You are a modern day high risk scuba diver that explores sunken ships from the
golden age of piracy. Reports of a maelstrom off the coast of Papua New Guinea led you and
your team to South East Asia to look for work. Your team consists of an archaeologist, a \n\
demolition-expert, and a marine biologist. Luckily you have been hired almost immediately by a 
mystery contact to recover all cargo held within the legendary ship Andromeda. Using sonar technology
you are able to pinpoint a massive object just a few hundred feet below the surface. Time to move out.
"""

story_line2 = "You and your team of divers finally you slip over the edge of the boat and begin the \n\
long plunge toward your fortune. As the massive outline of the ship becomes clearer, you realize \n\
this wont be as cut and dry as you thought. First you have to figure out a way to get inside the ship,\n\
but centuries underwater has transformed the glorious Andromeda into a artificial reef teeming with \n\
fish, coral, algae, and other marine life, making the hold entrance inaccesible."

story_line3 = ""


# for line in story_lines:
#     print(line)
#     time.sleep(2.5)
story_lines = ["""You are a modern day high risk scuba diver that explores sunken ships from the
golden age of piracy. Reports of a maelstrom off the coast of Papua New Guinea led you and
your team to South East Asia to look for work.""", """Your team consists of an archaeologist, a \n\
demolition-expert, and a marine biologist. Luckily you have been hired almost immediately by a 
mystery contact to recover all cargo held within the legendary ship Andromeda.""", """Using sonar technology
you are able to pinpoint a massive object just a few hundred feet below the surface. Time to move out."""]


for line in story_lines:
    print(line)
    time.sleep(2.5)


# step 1 Accepting the mission
decision_start = "Do you want to acccept the job 1 or cut your losses and go home?2 "
decison_accept = "Danger has always been a part of this profession, and an opportunity like\n"\
"this only comes once in a lifetime. "
decison_refuse = "There will be other jobs, and you surely dont trust this mysterious \n"\
"'N' character. Time to pack up and leave..."

# step 2 Entering the ship.
descison_entrance = "Do you want to 1. survey the outside of the ship to look for a porthole \n\
large enough to fit through, 2. Carefully force the hold latch open with a crowbar, or 3. Use \n\
dynamite to blast open the bow (front) of the ship?"
entrance_stealth = "After 2 laps around the ship, you manage to find a space between two portholes\n\
just big enough to squeeze through. A dark room lies before you and you hear gentle creaks somewhere \n\
in the darkness."
entrance_direct = "Armed with a large crowbar you pry the hold open with a few easy pulls. As you \n\
drop down into the hold you find yourself in the center of the gun deck, surrounded by algae \n\
covered cannons."
entrance_destroy = "After the dynamite charges are set, you and your team swim back the the top deck \n\
away from the blast zone. 3...2...1... a deafening explosion rings through the water sending a cloud of \n\
dirt and debris everywhere, exposing the front ship stores. The ship seems to be hanging more precariously \n\
on the edge of the trench, but at least now you have an entrance."

entrance_step = [entrance_stealth, entrance_direct, entrance_destroy]

# for option in entrance_step:
#     print(option)
#     time.sleep()

# print(*entrance_step, sep="\n", end=time.sleep(1))


# step 3 Exploring the ships interior. 
open_area= ""
open_area_stealth = "You find yourself in a deep dark hall "
open_area_direct = ""
open_area_destroy = ""


# step 4 Reaching the first progressing obstacle.
obstacle_primary = ""

# step 5 Reaching the main exploration area. Puzzle.

# step 6 Reaching the final area. Information drop

# step 7 Player gains access to the final room. 

# step 8 Playr locates the key item and exits the ship.

lockpicking_lines = ["It worked! The door is unlocked.", "Your lockpick broke, want to use another? (Y/N): "] 
breaking_lines = ["You did it! The door is a splintered mess.", ]


def game_intro():
    begin_game = ""
    change_settings = ""
    quit_game = ""
    intro = "Welcome to my text adventure game! to navigate you will only need your keyboard and "\
    "a brave spirit. \nTo begin enter 'e', to adjust settings enter 't', and to quit enter 'q'."
    print(intro)


def game_story():
    story_line1 = "You slip over the edge of the boat and begin the long plunge toward your fortune.\n\
As the massive outline of the ship becomes clear, you realize this wont be as simple as you first thought."
    print(story_line1)

def doorway():
    success = False  # if sucess is True the player can progress. If not they must retry the minigame.
    doorway_line1 = "You come across a suprisingly sturdy wooden door. You try pushing it open but it wont budge.\n"\
    "Do you 1 try to pick its lock or 2 try to break the door down.\nSelect (1 or 2)"
    print(doorway_line1)

    # if unlocked:
        # success = True


# game_intro()
# game_story()
# doorway()