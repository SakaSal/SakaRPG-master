class Gear:

    def __init__(self, name, place, attributes, quip):
        self.name = name
        self.attributes = attributes
        self.place = place
        self.quip = quip

    def __str__(self):
        return f"{self.name} : {self.quip}"

    def __repr__(self):
        return repr(self.name, self.attributes, self.quip)


class Sword(Gear):

    def __init__(self, name, place, attributes, quip):
        super().__init__(name, place, attributes, quip)


machete = Sword(
    "Machete",
    "hand",
    {"attack": 3},
    "A utilitarian blade that strikes \
fear in to the hearts of the burgoise",
)

# print(machete.quip)
