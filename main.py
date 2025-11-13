import curses
import random
import time
from curses import wrapper

from gear import combat_knife, fist, machete
from races import Goblin, Human
from terminal import fight_terminal

sal = Goblin("sal")
jules = Human("jules")
sal.equip_item(machete, "right_hand")
jules.equip_item(fist, "right_hand")
# print(jules.atribs)
# print(sal.atribs)


wrapper(fight_terminal, sal, jules)
