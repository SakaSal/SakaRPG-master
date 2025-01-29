from base import Being, Base, Goblin_Bonus
# from gear import machete


class Goblin(Being):
    number_of_goblins = 0

    def __init__(self, name, stren=Base, intel=Base, skill=Base,
                 res=Base, cha=Base, fort=Base, dex=Base, spd=Base):
        super().__init__(name, stren, intel, skill,
                         res, cha, fort, dex, spd)
        for bonus in Goblin_Bonus:
            self.set_atrib(bonus, Goblin_Bonus[bonus])
        self.number_of_goblins += 1


sal = Goblin('Sal')
# sal.equip_item(machete, 'right_hand')
print(sal.atribs)
print(sal.gear)
