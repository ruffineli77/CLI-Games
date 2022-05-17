
# begining the game
from functions import game_phase1, print_pause, valid_input, choose_option


def intro():
    start_options = """You can either start the game, change settings, or quit.\n"""
    select_screen1 = "1. Start game\n2. Change settings\n3. Quit Game"
    settings_options = "You can change the game diffiulty, change game mode, or change the players name."
    settings_screen = "1. Difficulty\n2. Game mode\n3. Player name"
    quit_game = "Thanks for playing!"

    settings = {"difficulty": 3, "player name": "Al Jeigh", "game mode": "timed"}
    game_difficulty = 3
    player_name = "Al Jeigh"

    print("Welcome to scuba diving text adventure game!")
    print_pause(start_options)
    print(select_screen1)

    select_option = input("your choice: ")

    if select_option == "1":
        print_pause("Your journey is about to begin...")
    elif (select_option) == "2":
        print(settings_options)
        print(settings_screen)
        setting_select = input("your choice: ")
        if setting_select == "difficulty":
            print("Please enter easy, medium or hard")



    elif (select_option) == "3":
        print_pause("Thanks for playing")
        return
    else:
        print("Bad input")



def story():
    pass


# playing text adventure game
def scuba_game(player_inventory):

    # repeated lines and options
    yes_no = ["yes", "no"]

    # unique lines and options
    story1 = """You are a high risk scuba diver on vacation in Indonesia.\n
    Almost immediately after you arrive in Papua New Guinea, you recieve a request for a
    job by a mystery contact! They want you to recover any valuable cargo held within 
    ???."""

    choice1 = ("Do you choose to accept the job?", yes_no)
    choice2 = ("How would you like to enter the ship?", 
                ["Destroy the ship", "Find a quiet way in", "Try to open the hold"])


    accept_mission = choose_option(*choice1)


    if accept_mission == "no":
        print("Thanks for playing!")
    elif accept_mission == "yes":
        print_pause("A great decision! Glory and riches are coming your way!")

        


# ending the game
def outro():
    end_game = ""
    view_stats = ""
    play_again = ""

    outro_lines = [play_again, view_stats, end_game]
    return outro_lines


def play_game():
    player_health = 100
    player_oxygen = 100
    ammunition = 12
    player_choices = []  # tells each game_phase function which set of lines etc to print.
    player_inventory = []   # inventory items are strings. They are later used in f strings.
    

    # intro()
    scuba_game(player_inventory)
    # outro()



stealth_victory = ()

destruction_victory = ()

direct_victory = ()
