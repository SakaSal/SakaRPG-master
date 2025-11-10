import time
from gear import machete
from races import Goblin, Human

sal = Goblin("sal")
jules = Human("jules")
# print(sal.atribs["attack"])
sal.equip_item(machete, "right_hand")
sal.fight(jules)
# print(sal.atribs["attack"])
# sal.atribs.update({"attack": 5})
# print(sal.atribs["attack"])
# print(jules.atribs)
# print(jules.gear)


def fight(classa, classb):
    print(f"{classa.name}'hp is {classa.hp}, {classb.name}'s hp is {classb.hp}")
    in_fight = True
    while in_fight:
        dmg = classa.atribs["melee_damage"] - classb.atribs["deffense"]
        classb_dmg = classb.atribs["melee_attack"] - classa.atribs["deffense"]
        classb.atribs["hp"] -= dmg
        print(
            f"{classa.name} strikes a blow dealing {dmg} dmg to {classb.name}, {classb.name}'s hp is {classb.atribs["hp"]}"
        )
        time.sleep(0.5)
        if classb.atribs["hp"] <= 0:
            in_fight = False
            print(f"{classb.name} is defeated")

        if in_fight:
            classa.atribs["hp"] -= classb_dmg
            print(
                f"{classb.name} strikes a blow dealing {classb_dmg} dmg to {classa.name}, {classa.name}'s hp is {classa.atribs["hp"]}"
            )
            time.sleep(0.5)
    classb.update_atribs()
    classa.update_atribs()
fight(sal, jules)
    