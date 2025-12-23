class Gear:

    def __init__(self, name, place, attributes, quip, points,):
        self.name = name
        self.attributes = attributes
        self.place = place
        self.points = points
        self.quip = quip

    def __str__(self):
        return f"{self.name} : {self.quip}"

    def __repr__(self):
        return f"{self.name},{self.place}, {self.attributes}, {self.points}, {self.quip}"


class Fists(Gear):
    def __init__(self, name, place, attributes, quip, points,):
        super().__init__(name, place, attributes, quip, points,)


class Sword(Gear):

    def __init__(self, name, place, attributes, quip, points,):
        super().__init__(name, place, attributes, quip, points,)


fist = Fists(
    "fist",
    "hand",
    {"melee_damage": 2, "melee_attacks": 4},
    "Just the ol' mitts",
    5,
)

machete = Sword(
    "Machete",
    "hand",
    {"melee_damage": 4, "melee_attacks": 3},
    "A utilitarian blade that strikes \
fear in to the hearts of the burgoise",
10,
)

combat_knife = Sword(
    "Combat knife",
    "hand",
    {"melee_damage": 6, "melee_attacks": 4},
    "Now THIS, this is a Knife!",
    15,
)

gear_list = [fist, machete, combat_knife]
# print(machete.quip)
