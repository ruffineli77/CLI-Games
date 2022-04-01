
import sqlite3
import time 
import random

lockpicking_lines = ["It worked! The door is unlocked.", "Your lockpick broke, want to use another? (Y/N): "] 
breaking_lines = ["You did it! The door is a splintered mess.", ]
magic_lines = ["The spell worked! The door flies open.", "The door didnt open. Maybe your footing was off, want to try again? (Y/N): "]



def chance_minigame(specifc_lines=None):  # this function returns True or False if the randomly selected character is equal to 15 or not.
    success = False
    remaining_attempts = 5

    while not success:
        # print(remaining_attempts)

        player_choice = input("you choose: ")
        attempt = random.randint(10,20)
        print(attempt)

        if remaining_attempts == 1:
            print("You failed to open the door...")
            time.sleep(1)
            break

        if player_choice in ["1", "2", "3"]:
            if attempt == 15:
                print("It worked!")
                time.sleep(2)
                success = True
                
            elif attempt != 15: 
                print("It didnt work try again.")
                remaining_attempts -= 1
                
            else:
                print("Not a good entry")

        elif player_choice in ["back", "b", "exit", "e"]:
            print("you step away from whatever")
            time.sleep(2)
            break

        else:
            print("not a valid selection. Try again.")

    return success


print(chance_minigame())


def unlock_door():  # add a chance event of braking the lock. Add a mercy rule if the player cant get the right random number
    door_options = "A locked door... You can 1. try to open it or 2. come back later..."
    exit_line = "You walk away from the door."
    unlock_options = "Do you want to: 1. pick the lock, 2. break the door down, 3. use a magic spell? Select (1/2/3)"
    lp_success_line = "It worked! The door is unlocked."
    lp_failure_line = "Your lockpick broke, want to use another? (Y/N): "
    br_success_line = "You did it! The door is a splintered mess."
    br_failure_line = "The door didnt break but your back might have, want to try again? (Y/N): "
    mg_success_line = "The spell worked! The door flies open."
    mg_failure_line = "The door didnt open. Maybe your footing was off, want to try again? (Y/N): "

    success_lines = [0, lp_success_line, br_success_line, mg_success_line]
    failure_lines = [0, lp_failure_line, br_failure_line, mg_failure_line]

    print(door_options)
    # print(unlock_options)

    while True:

        player_choice = input("you choose: ")
        attempt = random.randint(10,20)
        print(attempt)

        if player_choice in ["1", "2", "3"]:
            if attempt == 15:
                print(success_lines[int(player_choice)])
                return
            
            elif attempt != 15: 
                print(failure_lines[int(player_choice)])
                remaining_attempts =- 1
            
            else:
                print("Not a good entry")

        elif player_choice in ["back", "b", "exit", "e"]:
            print(exit_line)
            time.sleep(2)
            return

        
        else:
            print("not a valid selection. Try again.")


# door1 = unlock_door()
