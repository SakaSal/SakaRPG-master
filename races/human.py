from base import Base, Being, Human_Bonus

# from gear import machete


class Human(Being):
    number_of_humans = 0

<<<<<<< HEAD
    def __init__(
        self, name, stren=Base, intel=Base, skill=Base, fort=Base, dex=Base, spd=Base
    ):
        super().__init__(name, stren, intel, skill, fort, dex, spd)
=======
    def __init__(self, name, stren=Base, intel=Base, skill=Base,
                 fort=Base, dex=Base, spd=Base):
        super().__init__(name, stren, intel, skill,
                         fort, dex, spd)
>>>>>>> 8c90c117476e9efa27cce8b45146baca3d142e7d
        for bonus in Human_Bonus:
            self.set_atrib(bonus, Human_Bonus[bonus])
        self.number_of_humans += 1


sal = Human("Sal")
# sal.equip_item(machete, 'right_hand')
print(sal.atribs)
print(sal.gear)
