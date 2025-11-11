import random
import time

from gear import fist, machete
from races import Goblin, Human

sal = Goblin("sal")
jules = Human("jules")
sal.equip_item(machete, "right_hand")
jules.equip_item(fist, "right_hand")
print(jules.atribs)
print(sal.atribs)


def fight(attacker, defender):
    # announce the HP of the opponents
    print(
        f"{attacker.name}'hp is {attacker.atribs["hp"]}, {defender.name}'s hp is {defender.atribs["hp"]}"
    )
    in_fight = True
    # a Variable to keep track of the number of attacks
    attacker_strikes = 0
    defender_strikes = 0

    for attacks in range(attacker.atribs["melee_attacks"]):
        roll = random.randint(1, 10)
        if roll > 10 - attacker.atribs["melee_hit"]:
            attacker_strikes += 1
    print(f"attacker has {attacker_strikes} successful strike(s)")

    for attacks in range(defender.atribs["melee_attacks"]):
        roll = random.randint(1, 10)
        if roll > 10 - defender.atribs["melee_hit"]:
            defender_strikes += 1
    print(f"defender has {defender_strikes} successful strike(s)")

    while in_fight:
        # set the damage of the attacker and defender
        attacker_damage = attacker.atribs["melee_damage"] - defender.atribs["deffense"]
        defender_damage = defender.atribs["melee_damage"] - attacker.atribs["deffense"]

        # begin the fight
        # check if attacker has strikes
        if attacker_strikes > 0:
            print(
                f"[ATTACKER] HP: {attacker.atribs["hp"]}\nstrikes remaining: {attacker_strikes}\n[DEFENDER] HP: {defender.atribs["hp"]}\nstrikes remaining: {defender_strikes}"
            )
            selection = int(input(f"ATTACKER: [1]: Attack [2]: Parry\n"))
            if selection == 1:
                defender.atribs["hp"] -= attacker_damage
                print(
                    f"{attacker.name} strikes a blow dealing {attacker_damage} dmg to {defender.name}, {defender.name}'s hp is {defender.atribs["hp"]}"
                )
                attacker_strikes -= 1
            if selection == 2:
                defender_strikes -= 1
                attacker_strikes -= 1
            if defender.atribs["hp"] <= 0:
                in_fight = False
                print(f"{defender.name} is defeated")
                break
        # check if defender has strikes
        if defender_strikes > 0:
            print(
                f"[DEFENDER] HP: {defender.atribs["hp"]}\nstrikes remaining: {defender_strikes}\n[ATTACKER] HP: {attacker.atribs["hp"]}\nstrikes remaining: {attacker_strikes}"
            )
            selection = int(input(f"DEFENDER: [1]: Attack [2]: Parry\n"))
            if selection == 1:
                attacker.atribs["hp"] -= defender_damage
                print(
                    f"{defender.name} strikes a blow dealing {defender_damage} dmg to {attacker.name}, {attacker.name}'s hp is {attacker.atribs["hp"]}"
                )
                defender_strikes -= 1
            if selection == 2:
                attacker_strikes -= 1
                defender_strikes -= 1
            if attacker.atribs["hp"] <= 0:
                in_fight = False
                print(f"{attacker.name} is defeated")
        else:
            in_fight = False


fight(sal, jules)
