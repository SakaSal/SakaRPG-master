class Gear:

    def __init__(self, name, attributes, quip):
        self.name = name
        self.attributes = attributes
        self.quip = quip

    def __str__(self):
        return self.name

    def __repr__(self):
        return repr(self.name)

    # write function that tells class what to return when called as a string


class Sword(Gear):

    def __init__(self, name, hand, attributes, quip):
        super().__init__(name, attributes, quip)


machete = Sword('Machete', 'hand', {'attack': 3},
                'A utilitarian blade that strikes \
fear in to the hearts of the burgoise')

# print(machete.quip)
