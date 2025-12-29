from .base import Base, Being

# from gear import machete

Goblin_Bonus = {"intel": 7, "dex": 7, "fort": 7}


class Goblin(Being):
    number_of_goblins = 0
    points = 10
    name = "Goblin"

    def __init__(
        self,
        name,
        stren=Base,
        intel=Base,
        melee_skill=Base,
        fort=Base,
        dex=Base,
        spd=Base,
        points=10,
    ):
        super().__init__(name, stren, intel, melee_skill, fort, dex, spd, points)
        for bonus in Goblin_Bonus:
            self.set_atrib(bonus, Goblin_Bonus[bonus])
        self.number_of_goblins += 1
