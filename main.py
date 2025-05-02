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
