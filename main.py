import csv
import curses
import random
import time
from curses import wrapper

from tabulate import tabulate

from gear import combat_knife, fist, machete
from races import Goblin, Human
from terminal import create_team, fight_terminal, map_terminal, map_terminal_resize

sal = Goblin("sal")
jules = Human("jules")
wasal = Human("wasal")
wajules = Goblin("wajules")
sal.equip_item(machete, "right_hand")
jules.equip_item(combat_knife, "right_hand")
wasal.equip_item(combat_knife, "right_hand")
wajules.equip_item(machete, "right_hand")
# print(jules.atribs)
# print(sal.points)


def main():
    welcome()


def welcome():
    team = []
    team.append(sal)
    team.append(jules)
    team2 = []
    team2.append(wasal)
    team2.append(wajules)

    while True:
        if team:
            print(
                "WELCOME \n 1: create NEW team. 2: save team. 3: check team. 4: play game. 5: fight demo 6: quit\n"
            )
            choice = input("Enter choice: ")

            if choice == "1":
                team = create_team()
            elif choice == "2":
                save_team(team)
            elif choice == "3":
                with open("team.csv", "r") as teamcsv:
                    reader = csv.reader(teamcsv)
                    table = []
                    for row in reader:
                        table.append(row)
                    print(
                        tabulate(
                            table,
                            headers="firstrow",
                            tablefmt="pretty",
                            showindex="always",
                        )
                    )

            elif choice == "4":
                # wrapper(map_terminal)
                wrapper(map_terminal_resize)
            elif choice == "5":
                wrapper(fight_terminal, sal, jules)
            elif choice == "6":
                break

        else:
            print("WELCOME \n 1: create team. 2: quit\n")
            choice = input("Enter choice: ")

            if choice == "1":
                team = create_team()
            elif choice == "2":
                break


def save_team(team):
    with open("team.csv", "w", newline="") as save_file:
        fieldnames = []
        for hero in team:
            for attribute in hero.atribs:
                if attribute not in fieldnames:
                    fieldnames.append(attribute)
        writer = csv.DictWriter(save_file, fieldnames=fieldnames)
        writer.writeheader()
        for hero in team:
            writer.writerow(hero.atribs)
        # https://docs.python.org/3/library/csv.html#csv.DictReader

    pass


main()
