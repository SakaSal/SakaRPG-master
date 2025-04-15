from gear import machete
from races import Goblin, Human

sal = Goblin("sal")
# jules = Human("jules")
sal.equip_item(machete, "right_hand")
# print(sal.atribs)
item = sal.gear["right_hand"].attributes
# print(item)
# print(jules.atribs)
# print(jules.gear)
