from gear import gear_list
from races import race_list

points = 50


def create_team():
    global points
    team = []
    while points > 14:
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
