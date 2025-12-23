import time

Base = 5
Human_Bonus = {"intel": 7, "skill": 7, "dex": 7}


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
        fort=Base,
        dex=Base,
        spd=Base,
        points=10,
    ):
        self.name = name
        self.stren = stren
        self.intel = intel
        self.shoot_skill = shoot_skill
        self.melee_skill = melee_skill
        self.fort = fort
        self.dex = dex
        self.spd = spd
        self._melee_damage = self.stren + self.melee_skill
        self._magic = self.intel
        self._deffense = self.fort + self.stren
        self._magic_deffense = self.fort + self.intel
        self._initiative = self.spd + self.dex
        self.hp = Base + self.fort + self.stren
        self.melee_hit = self.dex + self.melee_skill
        self.atribs = {
            "stren": self.stren,
            "intel": self.intel,
            "shoot_skill": self.shoot_skill,
            "melee_skill": self.melee_skill,
            "fort": self.fort,
            "dex": self.dex,
            "spd": self.spd,
            "hp": self.hp,
            "melee_damage": self._melee_damage,
            "deffense": self._deffense,
            "magic deffense": self._magic_deffense,
            "init": self._initiative,
            "melee_hit": self.melee_hit,
            "magic": self._magic,
            "melee_attacks": 0,
        }
        self.gear = {"head": None, "right_hand": None, "left_hand": None}
        print(f"{self.name} is born!")
        self.number_of_beings += 1
        self.points = points

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
        """
        first sets the carahcters attrributes based on the stats
        before adjusting based on equipped items
        """
        self.atribs["melee_damage"] = self.atribs["stren"] + self.atribs["melee_skill"]
        self.atribs["magic"] = self.atribs["intel"]
        self.atribs["deffense"] = self.atribs["stren"] + self.atribs["fort"]
        self.atribs["magic deffense"] = self.atribs["fort"] + self.atribs["intel"]
        self.atribs["init"] = self.atribs["spd"] + self.atribs["dex"]
        self.atribs["hp"] = Base + self.atribs["fort"] + self.atribs["stren"]
        self.atribs["melee_hit"] = int(
            (self.atribs["dex"] + self.atribs["melee_skill"]) / 2
        )
        self.atribs["shoot_hit"] = int(
            (self.atribs["dex"] + self.atribs["shoot_skill"]) / 2
        )
        # sort through equipment to adjust atributes
        for slot in self.gear:
            if self.gear[slot]:
                item = self.gear[slot]
                item_attributes = item.attributes
                self.atribs.update(
                    {
                        key: (
                            self.atribs[key] + item_attributes[key]
                            if key in item_attributes
                            else self.atribs[key]
                        )
                        for key in self.atribs
                    }
                )

    def equip_item(self, item, place):
        self.gear[place] = item
        self.update_atribs()

    def get_gear(self):
        return self.gear

    def set_bonus(self, race_bonus):
        for bonus in race_bonus:
            self.set_atrib(bonus, race_bonus[bonus])

    def fight(self, classb):
        print(f"{self.name}'s hp is {self.hp}, {classb.name}'s hp is {classb.hp}")
        in_fight = True
        while in_fight:
            dmg = self.atribs["melee_damage"] - classb.atribs["deffense"]
            classb_dmg = classb.atribs["melee_damage"] - self.atribs["deffense"]
            classb.atribs["hp"] -= dmg
            print(
                f"{self.name} strikes a blow dealing {dmg} dmg to {classb.name}, {classb.name}'s hp is {classb.atribs["hp"]}"
            )
            time.sleep(0.5)
            if classb.atribs["hp"] <= 0:
                in_fight = False
                print(f"{classb.name} is defeated")

            if in_fight:
                self.atribs["hp"] -= classb_dmg
                print(
                    f"{classb.name} strikes a blow dealing {classb_dmg} dmg to {self.name}, {self.name}'s hp is {self.atribs["hp"]}"
                )
                time.sleep(0.5)
        classb.update_atribs()
        self.update_atribs()

    @classmethod
    def add_beings(cls, n):
        """maybe make this add a randomly genrated being"""
        cls.number_of_beings += n

    @classmethod
    def _number_of_beings_(cls):
        return cls.number_of_beings
