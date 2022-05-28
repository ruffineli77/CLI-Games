
import random
import time
import textwrap as tr


class Player:
    pass


class Human:  # sub class of player
    pass


class Computer:  # subclass of player
    pass


class theLorax:  # subclass of Computer
    pass


class theRock:  # subclass of Computer
    pass


class edwardScissorhands:  # subclass of Computer
    pass


def print_pause(text, pause_time=2.2, extra_lines=1):   
    print(tr.fill(text, 80))
    time.sleep(pause_time)

    for lines in range(0, extra_lines):
        print()


def rps_board():
    print("~~~~~~ Rock Paper Scissors ~~~~~~")
    print()
    print("~~~~~~ OIX ~~~~~~")


def intro():
    print_pause("Welcome to my Rock Paper Scissors game!")


def rock_paper_scissors():  # a three round game of rock paper scissors.
    rps_board()


def outro():
    print_pause("Thanks for playing my Rock Paper Scissors game!")


def game():
    intro()
    rock_paper_scissors()
    outro()


game()
