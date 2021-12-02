from Item import Item


class Weapon(Item):

    def __init__(self, *args):
        Item.__init__(self, *args)
        self.group = args[8]
        self.damage = args[9]
        self.dType = args[10]
        self.hands = args[11]
        self.specialization = args[12]


#  TODO: Initialize necessary weapons, after picking
