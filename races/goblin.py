from base import Base, Being, Goblin_Bonus

# from gear import machete


class Goblin(Being):
    number_of_goblins = 0

<<<<<<< HEAD
    def __init__(
        self, name, stren=Base, intel=Base, skill=Base, fort=Base, dex=Base, spd=Base
    ):
=======
    def __init__(self, name, stren=Base, intel=Base, skill=Base, fort=Base, dex=Base, spd=Base):
>>>>>>> 8c90c117476e9efa27cce8b45146baca3d142e7d
        super().__init__(name, stren, intel, skill, fort, dex, spd)
        for bonus in Goblin_Bonus:
            self.set_atrib(bonus, Goblin_Bonus[bonus])
        self.number_of_goblins += 1


# this code should be moved some where else
sal = Goblin("Sal")
# sal.equip_item(machete, 'right_hand')
print(sal.atribs)
print(sal.gear)
