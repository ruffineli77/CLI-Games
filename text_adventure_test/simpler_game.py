

import random

# these are already made

def print_pause()
    pass

def select_options():
    pass
        
        
# rainforest path > blueberries > tiger > $
def path1(items):
    player_items = items  # not sure if I need this
    option1 = select_options("Do you want to pick a few berries? \n", yes_no)
    
    print_pause("You start down the left path.")
    print_pause("A few hundred feet into the rainforest, beneath a stone archway, you find bushes full of bright blue berries.")
    
    
    user_choice1 = select_options(yes_no)
    
    if user_choice1 == "yes":
        print("You grab a handful of berries and carefully put them in your bag.")
            
    if user_choice1 == "no":
        print("You keep walking down the misty path.")


# tundra path > lichen > carribou > $
def path2(items):
    player_items = items
    option1 = select_options("Do you want to gather some lichen? \n", yes_no)
    
    print_pause("You start down the center path.")
    print_pause("The ground crunches beneath your feet until you step on a soft carpet of lichen.")
    
    
    user_choice1 = select_options(yes_no)
    
    if user_choice1 == "yes":
        print("You tear up a patch of lichen and stuff it in your bag.")
        player_items.append("wad of lichen")
            
    if user_choice1 == "no":
        print("You keep walking down the chilling path.")


# swamp path > dead turtle > crococile > $
def path3(items):
    player_items = items  
    
    turtle_optons = ("Leave the turtle where it is.", "Flip the turle back on its feet.", "Pick up the turle.")
    option1 = select_options("Do you want to pick up the turtle? \n", *turtle_optons)
    
    print_pause("You start down the left path.")
    print_pause("A few hundred feet into the rainforest, beneath a stone archway, you find bushes full of bright blue berries.")
    
    
    user_choice1 = select_options(yes_no)
    
    if user_choice1 == "Leave the turtle where it is.":
        print("You step over the turle and keep moving down the muddy path.")
            
    if user_choice1 == "Help the turle back on its feet.":
        print("You gently flip the turtle over. It runs away and dives into the murky water.")
        
    if user_choice1 == "Pick up the turle.":
        print("You pick up the turtle and place it in your bag.")
        player_items.append("confused turtle")
        
    
    
    
def intro():
    pass
    
    
def game():
    player_inventory = []  # this is an argument yeah time your run a path function. It tells the function which items the player has picked up.
    
    main_paths = [("The left path goes through a dense rainforest covered in a thick fog."),
                  ("The center path crisscrosses through frozen lakes in a bitter tundra"),
                  ("The right path goes through a sweltering bog. You can see clouds of flying insects in the near distance.")]
                  
    select_options(main_paths)
    user_choice_main = input("Which path do you want to take?\n")

    if user_choice_main == "The left path goes through a dense rainforest covered in a thick fog.":
        path1(player_inventory)

    if user_choice_main == "The center path crisscrosses through frozen lakes in a bitter tundra":
        print_pause("You start down the center path.")
        path2(player_inventory)

    if user_choice_main == "The right path goes through a sweltering swamp. You can see clouds of flying insects in the distance.":
        print_pause("You start down the right path.")    
        path3(player_inventory)
    
    
def outro():
    pass
    


def scuba_adventure():
    intro()
    game()
    outro()
    
    
    
    
    
    