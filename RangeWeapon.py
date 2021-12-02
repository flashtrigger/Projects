from Weapon import Weapon


class RangeWeapon(Weapon):

    def __init__(self, *args):

        Weapon.__init__(self, *args)
        self.range = args[13]
        self.reload = args[14]


#  TODO: Initialize necessary weapons, after picking
