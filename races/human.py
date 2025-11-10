from .base import Base, Being

# from gear import machete

Human_Bonus = {"intel": 7, "melee_skill": 9, "dex": 7}


class Human(Being):
    number_of_humans = 0

    def __init__(
        self, name, stren=Base, intel=Base, melee_skill=Base, fort=Base, dex=Base, spd=Base
    ):
        super().__init__(name, stren, intel, melee_skill, fort, dex, spd)
        for bonus in Human_Bonus:
            self.set_atrib(bonus, Human_Bonus[bonus])
        self.number_of_humans += 1
