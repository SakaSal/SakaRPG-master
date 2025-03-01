from base import Being, Base, Human_Bonus
# from gear import machete


class Human(Being):
    number_of_humans = 0

    def __init__(self, name, stren=Base, intel=Base, skill=Base,
                 fort=Base, dex=Base, spd=Base):
        super().__init__(name, stren, intel, skill,
                         fort, dex, spd)
        for bonus in Human_Bonus:
            self.set_atrib(bonus, Human_Bonus[bonus])
        self.number_of_humans += 1


sal = Human('Sal')
# sal.equip_item(machete, 'right_hand')
print(sal.atribs)
print(sal.gear)
