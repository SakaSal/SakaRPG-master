import curses
import random
import time
import csv
from curses import wrapper

from gear import combat_knife, fist, machete
from races import Goblin, Human
from terminal import create_team, fight_terminal

sal = Goblin("sal")
jules = Human("jules")
sal.equip_item(machete, "right_hand")
jules.equip_item(fist, "right_hand")
# print(jules.atribs)
# print(sal.points)


def main():
    welcome()
    # wrapper(fight_terminal, sal, jules)


def welcome():
    team = []
    team.append(sal)
    team.append(jules)
    
    while True:
        if team:
            print("WELCOME \n 1: create NEW team. 2: save team. 3: check team. 4: quit\n")
            choice = input("Enter choice: ")
            
            if choice == "1":
                team = create_team()
            elif choice == "2":
                save_team(team)
            elif choice == "3":
                for hero in team:
                    print(hero.atribs)
            elif choice == "4":
                break
        else:
            print("WELCOME \n 1: create team. 2: quit\n")
            choice = input("Enter choice: ")

            if choice == "1":
                team = create_team()
            elif choice == "2":
                break

def save_team(team):
    with open('team.csv', 'w', newline='') as save_file:
        fieldnames = []
        for hero in team:
            for attribute in hero.atribs:
                if attribute not in fieldnames:
                    fieldnames.append(attribute)
        writer = csv.DictWriter(save_file, fieldnames=fieldnames)
        writer.writeheader()
        # https://docs.python.org/3/library/csv.html#csv.DictReader
        
    pass

main()
