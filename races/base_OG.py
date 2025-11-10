Base = 5


class Being:
    """The basic class from which all living beings inherit from"""

    number_of_beings = 0

    def __init__(
        self,
        name,
        stren=Base,
        intel=Base,
        shoot_skill=Base,
        melee_skill=Base,
        res=Base,
        fort=Base,
        dex=Base,
        spd=Base,
    ):
        self.name = name
        self.stren = stren
        self.intel = intel
        self.shoot_skill = shoot_skill
        self.melee_skill = melee_skill
        self.res = res
        self.fort = fort
        self.dex = dex
        self.spd = spd
        self._attack = self.stren + self.skill
        self._magic = self.intel + self.skill
        self._deffense = self.fort + self.stren
        self._magic_deffense = self.fort + self.res
        self._initiative = self.spd + self.dex
        self.hp = Base + self.fort + self.res
        self.hit = self.dex + self.skill
        self.atribs = {
            "stren": self.stren,
            "intel": self.intel,
            "shoot_skill": self.shoot_skill,
            "melee_skill": self.melee_skill,
            "res": self.res,
            "fort": self.fort,
            "dex": self.dex,
            "spd": self.spd,
            "hp": self.hp,
            "attack": self._attack,
            "deffense": self._deffense,
            "magic deffense": self._magic_deffense,
            "init": self._initiative,
            "hit": self.hit,
            "magic": self._magic,
        }
        self.gear = {"head": None, "right_hand": None, "left_hand": None}
        print(f"{self.name} is born!")
        self.number_of_beings += 1

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_atrib(self, atrib):
        return self.atribs[atrib]

    def set_atrib(self, atrib, amt):
        self.atribs[atrib] = amt
        self.update_atribs()

    def update_atribs(self):
        self.atribs["attack"] = self.atribs["stren"] + self.atribs["skill"]
        self.atribs["magic"] = self.atribs["intel"] + self.atribs["skill"]
        self.atribs["deffense"] = self.atribs["stren"] + self.atribs["fort"]
        self.atribs["magic deffense"] = self.atribs["fort"] + self.atribs["res"]
        self.atribs["init"] = self.atribs["spd"] + self.atribs["dex"]
        self.atribs["hp"] = Base + self.atribs["fort"] + self.atribs["res"]
        self.atribs["melee_hit"] = self.atribs["dex"] + self.atribs["melee_skill"]
        self.atribs["shoot_hit"] = self.atribs["dex"] + self.atribs["shoot_skill"]

    def equip_item(self, item, place):
        self.gear[place] = item

    def get_gear(self):
        return self.gear

    def set_bonus(self, race_bonus):
        for bonus in race_bonus:
            self.set_atrib(bonus, race_bonus[bonus])

    @classmethod
    def add_beings(cls, n):
        """maybe make this add a randomly genrated being"""
        cls.number_of_beings += n

    @classmethod
    def _number_of_beings_(cls):
        return cls.number_of_beings
