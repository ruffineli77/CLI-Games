
import random
import time
import textwrap as tr
from xml.dom.expatbuilder import Namespaces
from click import option
import colorama
from urllib import response

def print_pause(text, pause_time=1.5):
    print(tr.fill(text, 70))
    time.sleep(pause_time)


def print_options(input_options):
    # print("Your options are: ")
    print(f"Your options are: ")
    print(*input_options, sep=", ")
    time.sleep(1)


def valid_input(prompt, options):  # options is a list
    while True:
        user_response = input(prompt)
        for option in options:
            if option in user_response:
                return user_response
            else:
                break
        print("Please enter another response...")
        

# this function will
# tell the user what they are selecting
# print options for the user to select from
# ask the user for input, 
# if input is invalid the function runs again.



# use this function when you have a prompt and a list of options for a user to choose from.
#
# ver 2 will take some game data as an argument. Game data is made up of intro lines, outro, 
# story explanation, puzzles, objects, enemies, 
def choose_option(prompt, options):  # options is a list of each option the user can select.
    print(prompt)
    # join() is used to print concatenate strings and print each one on a new line.
    random.shuffle(options)  # randomize the order that the users options appear
    options.insert(0, 0) # one way to begin the users options at 1 instead of 0.

    options_screen = "\n".join(f"Enter {key} to select {option}." for key, option in enumerate(options[1:], 1))
    print(options_screen)

    while True: 
        select_option = input("Your choice: ")

        try:
            # print(options[int(select_option)])
            return options[int(select_option)]

        except IndexError as ie:
            # print(f"{ie}")
            print("please choose again.")

        except ValueError as ve:
            # print(f"{ve}")
            print("please choose again.")



def game_phase0(story_path):


    if story_path == "yes":
        game_phase1()

    elif story_path == "no":
        print_pause("There will be other jobs, lets just enjoy this vacation!")




def game_phase1(story_path1, items):

    if story_path1 == "Find a quiet way in":
        print_pause("It's better to be safe and quiet as you enter the ship.")



        
    if story_path1 == "Destroy the ship":
        print_pause("You decide to get right to the point and make your own path inside."\
        "You didnt drag a bag of dynamite down here for nothing.")




    if story_path1 == "Try to open the hold":
        print_pause("""The hold latch is made of solid iron but with enough force 
        you may be able to open it.""")
        



def game_phase2():
    galley = {"items": [], "doors": ["captain's cabin"], "npcs": [], 
              "obstacles": ["school of piranna"], 
              "puzzle": """find food in the galley to distract the pirana and make it to the
               door to the captains cabin"""}
    officers_quarters = {"items": [],  
                        "doors": ["captain's cabin"], "npcs": [], 
                        "obstacles": ["electric eels"],
                        "puzzle": "slowly swim through the maze of eels."}
    cargo_hold_destroyed = {"items": ["wooden planks", ""],  
                            "doors": ["captain's cabin"], 
                            "npcs": [], "obstacles": ["crewman zombies"], 
                            "puzzle": "fight off the zombies using your gun"}

    print("You are now in the rum and water stores.")
    print("You are now in the gun deck.")
    print("You are now in the galley")


def game_phase3():
    captains_cabin = {"items": ["treasure map", "secret key", "captains Aknh's journal"], 
                    "npcs": ["stalking shark", "captain Aknh's ghost"], "obstacles": ["locate item"], 
                    "puzzle": "guess password"}
    print("You are now in the captains quarters")


def open_door():
    is_locked = False

    door_key = random.choice(random.randrange(1, 10))
    attempts = 3
    while attempts != 0 and user_choice != door_key:
        user_choice = ""
        print_pause("You attempt to break open the door...")
        attempt -= 1


def fight_enemy():
    player_attack = random.choice(range(1, 10))
    enemy_health = 50

    if player_attack >= 3: 
        enemy_health -= 10

    elif player_attack >= 3: 
        enemy_health -= 10

    elif player_attack == 10: 
        enemy_health -= 50
    

def take_item():
    pass

def open_inventory():
    pass


def select_items():
    pass


def unlock_door():
    pass


def battle():
    pass


def boss_battle():
    pass


def puzzle():
    pass


def boss_puzzle():
    pass
