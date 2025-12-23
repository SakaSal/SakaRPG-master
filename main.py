import curses
import random
import time
from curses import wrapper

from gear import combat_knife, fist, machete, gear_list
from races import Goblin, Human, race_list
from terminal import fight_terminal

#sal = Goblin("sal")
#jules = Human("jules")
#sal.equip_item(machete, "right_hand")
#jules.equip_item(fist, "right_hand")
# print(jules.atribs)
# print(sal.atribs)
team = []

def main():
    
    welcome()
    

    # wrapper(fight_terminal, sal, jules)

def welcome():
    print("WELCOME \n 1: create team. \n")
    choice = input("Enter choice: ")
    
    if choice == "1":
        points = 100
        team_size = 0
        print(f"You have {points} points remaining.\nRecruit\n")
        i=1
        races = {}
        for race in race_list:
            print(f"{i}: {race} (10 pts)")
            races[i] = race
            i += 1
                        
        choice = int(input("Choice: "))
        name = input("Enter hero name: ")
        hero = races[choice](name)
        print(f"You have {points} points remaining.\nselect a weapon for {name}")
        i = 1
        weapons = {}
        for weapon in gear_list:
            print(f"{i}: {weapon.name}, ({weapon.points} pts) \n")
            weapons[i] = weapon
            i += 1
        choice = int(input("Choice: "))
        hero.equip_item(weapons[choice], "right hand")
        points -= weapons[choice].points
        team.append(hero)

main()