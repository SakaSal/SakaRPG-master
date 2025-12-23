import curses
import random
import time
from curses import wrapper

from gear import combat_knife, fist, machete, gear_list
from races import Goblin, Human
from terminal import fight_terminal

#sal = Goblin("sal")
#jules = Human("jules")
#sal.equip_item(machete, "right_hand")
#jules.equip_item(fist, "right_hand")
# print(jules.atribs)
# print(sal.atribs)
Team = []

def main():
    
    welcome()
    

    # wrapper(fight_terminal, sal, jules)

def welcome():
    print("WELCOME \n 1: create team. \n")
    choice = input("Enter choice: ")
    
    if choice == "1":
        
        points = 100
        team_size = 0
        print(f"You have {points} points remaining.\n1: Recruit Goblin (10 pts)\n2:Recruit Human (10 pts)\n")
        choice = input("Choice: ")
        
        if choice == "1":
            
            points -= 10
            
            while points > 5:
                
                print(f"You have {points} points remaining.")
                name = input("Enter hero name: ")
                hero = Goblin(name)
                
                print(f"select a weapon for {name}")
                i = 1
                choices = {}
                for item in gear_list:
                    print(f"{i}: {item.name}, ({item.points} pts) \n")
                    choices[i] = item
                    i += 1
                choice = int(input("Choice: "))
                hero.equip_item(choices[choice], "right hand")
                points -= choices[choice].points
                Team.append(hero)
            
        if choice == "2":
            points -= 10
            print(f"You have {points} points remaining.")
            name = input("Enter character name: ")



main()