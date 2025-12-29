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
points = 50


def main():
    welcome()
    # wrapper(fight_terminal, sal, jules)


def welcome():
    global points
    while True:
        print("WELCOME \n 1: create team. 2: quit \n")
        choice = input("Enter choice: ")
        
        if choice == "1":
            team = create_team()
        elif choice == "2":
            break
    

def create_team():
    global points
    team = []
    while points >14:
            team_size = 0
            races = choice_list("Recruit", race_list)
            choice = int(input("Choice: "))
            name = input("Enter hero name: ")
            hero = races[choice](name)
            points -= hero.points
            

            weapons = choice_list(f"select a weapon for {name}", gear_list)
            choice = int(input("Choice: "))
            hero.equip_item(weapons[choice], "right hand")
            points -= weapons[choice].points
            team.append(hero)
            team_size += 1
    return team

def choice_list(message, list):
    print(f"You have {points} points remaining.\n{message}\n")
    i = 1
    items_dict = {}
    for item in list:
        print(f"{i}: {item.name} ({item.points} pts)")
        items_dict[i] = item
        i += 1
    return items_dict


main()
