
import random
import time
import textwrap as tr
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
# 

def choose_option(prompt, options):  # options is a list of each option the user can select
    print(prompt)
    options_screen = "\n".join(f"Enter {key} to select {option}." for key, option in enumerate(options, 1))
    print(options_screen)


choose_option("choose a color", ["red", "blue", "yellow"])


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
