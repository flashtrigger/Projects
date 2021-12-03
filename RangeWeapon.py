from Weapon import Weapon


class RangeWeapon(Weapon):

    def __init__(self, *args):

        Weapon.__init__(self, *args)
        self.range = args[14]
        self.reload = args[15]


#  TODO: Initialize necessary weapons, after picking
