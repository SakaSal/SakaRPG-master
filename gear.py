class Gear:

    def __init__(self, name, place, attributes, quip):
        self.name = name
        self.attributes = attributes
        self.place = place
        self.quip = quip

    def __str__(self):
        return f"{self.name} : {self.quip}"

    def __repr__(self):
        return f"{self.name},{self.place}, {self.attributes}, {self.quip}"


class Fists(Gear):
    def __init__(self, name, place, attributes, quip):
        super().__init__(name, place, attributes, quip)


class Sword(Gear):

    def __init__(self, name, place, attributes, quip):
        super().__init__(name, place, attributes, quip)


fist = Fists(
    "fist",
    "hand",
    {"melee_damage": 2, "melee_attacks": 4},
    "Just the ol' mitts",
)

machete = Sword(
    "Machete",
    "hand",
    {"melee_damage": 4, "melee_attacks": 3},
    "A utilitarian blade that strikes \
fear in to the hearts of the burgoise",
)

combat_knife = Sword(
    "Combat knife",
    "hand",
    {"melee_damage": 6, "melee_attacks": 4},
    "Now THIS, this is a Knife!"
)

# print(machete.quip)
