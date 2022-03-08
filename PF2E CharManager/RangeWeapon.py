from Weapon import Weapon
from Trait import *


# name, description, category, subcategory, bulk, value, level. traits, actions
# group, damage, dType, hands
class RangeWeapon(Weapon):

    def __init__(self, *args):
        Weapon.__init__(self, *args)
        self.range = args[13]
        self.reload = args[14]


weapon = RangeWeapon(""
                     , ""
                     , "", "", 0.0, 0.00, 1
                     , [], []
                     , "", "", "", 1
                     , "", 1, 10, 0)

weaponSHORTBOW = RangeWeapon("Shortbow"
                             , "This smaller bow is made of a single piece of wood and favored by skirmishers and "
                               "cavalry. "
                             , "Ranged", "Martial", 1.0, 3.00, 1
                             , [traitDEADLY10], []
                             , "Bow", "1d6", "Piercing", 3 , 60, 0)  # 3 represents 1+ hands
