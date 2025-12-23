import curses
import random
import time
from curses import wrapper

from gear import combat_knife, fist, gear_list, machete
from races import Goblin, Human, race_list
from terminal import fight_terminal

# sal = Goblin("sal")
# jules = Human("jules")
# sal.equip_item(machete, "right_hand")
# jules.equip_item(fist, "right_hand")
# print(jules.atribs)
# print(sal.points)
team = []


def main():

    welcome()
    # wrapper(fight_terminal, sal, jules)


points = 100


def welcome():
    print("WELCOME \n 1: create team. \n")
    choice = input("Enter choice: ")

    if choice == "1":
        team_size = 0
        races = choice_list("Recruit", race_list)
        choice = int(input("Choice: "))
        name = input("Enter hero name: ")
        hero = races[choice](name)

        weapons = choice_list("selec a weapon for {name}", gear_list)
        choice = int(input("Choice: "))
        hero.equip_item(weapons[choice], "right hand")
        points -= weapons[choice].points
        team.append(hero)
        team_size += 1


def choice_list(message, list):
    print(f"You have {points} points remaining.\n{message}\n")
    i = 1
    items_dict = {}
    for item in list:
        print(f"{i}: {item} ({item.points} pts)")
        items_dict[i] = item
        i += 1
    return items_dict


main()
