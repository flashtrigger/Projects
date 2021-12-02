from Item import Item


class Weapon(Item):

    def __init__(self, *args):
        Item.__init__(self, *args)
        self.group = args[9]
        self.damage = args[10]
        self.dType = args[11]
        self.hands = args[12]
        self.specialization = args[13]
        if self.type == "Ranged":  # TODO: Subclass RangedWeapon?
            self.range = args[14]
            self.reload = args[15]

#  TODO: Initialize necessary weapons, after picking

