import curses
import random
import time
from curses import wrapper

from gear import combat_knife, fist, machete
from races import Goblin, Human
from terminal import create_team, fight_terminal

# sal = Goblin("sal")
# jules = Human("jules")
# sal.equip_item(machete, "right_hand")
# jules.equip_item(fist, "right_hand")
# print(jules.atribs)
# print(sal.points)


def main():
    welcome()
    # wrapper(fight_terminal, sal, jules)


def welcome():
    while True:
        print("WELCOME \n 1: create team. 2: quit \n")
        choice = input("Enter choice: ")

        if choice == "1":
            team = create_team()
        elif choice == "2":
            break


main()
