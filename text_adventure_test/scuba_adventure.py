
# begining the game
from functions import print_pause, valid_input


def intro():
    start_options = """You can either start the game, change settings, or quit.\n"""
    select_screen1 = "1. Start game\n2. Change settings\n3. Quit Game"
    settings_options = "You can change the game diffiulty, change game mode, or change the players name."
    settings_screen = "1. Difficulty\n2. Game mode\n3. Player name"
    quit_game = "Thanks for playing!"

    settings = {"difficulty": 3, "player name": "Al Jeigh", "game mode": "timed"}
    game_difficulty = 3
    player_name = "Al Jeigh"


    print_pause(start_options)
    print(select_screen1)

    select_option = input("your choice: ")

    if select_option == "1":
        print_pause("Your journey is about to begin...")
    elif (select_option) == "2":
        print(settings_options)
        setting_select = input()
        if setting_select == "difficulty":



    elif (select_option) == "3":
        print_pause("Thanks for playing")
    else:
        print("Bad input")



def story():
    pass


# playing text adventure game
def scuba_game():
    player_health = 100
    player_oxygen = 100
    ammunition = 12
    player_inventory = []   # inventory items are strings. They are later used in f strings.

    story1 = """You are a high risk scuba diver on vacation in Indonesia.\n
    Almost immediately after you arrive in Papua New Guinea, you recieve a request for a
    job by a mystery contact! They want you to recover any valuable cargo held within 
    ???. Do you choose to accept the job? \nEnter Yes/No: """

    print(story1)

    


# ending the game
def outro():
    end_game = ""
    view_stats = ""
    play_again = ""

    outro_lines = [play_again, view_stats, end_game]
    return outro_lines


def game():
    print("Welcome to scuba diving text adventure game!")

    while True:
        intro()

    # story()
    scuba_game()
    # outro()
