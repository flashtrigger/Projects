from Item import Item
from Trait import *


# name, description, category, subcategory, bulk, value, level. traits, actions
class Weapon(Item):

    def __init__(self, *args):
        Item.__init__(self, *args)
        self.group = args[9]
        self.damage = args[10]
        self.dType = args[11]
        self.hands = args[12]  # integer
        self.specialization = args[13]
        self.thrownRange = None


#  TODO: Initialize necessary weapons, after picking
weapon = Weapon(""
                , ""
                , "", "", 0.0, 0.00, 1
                , [], []
                , "", "", "", 1
                , "")

weaponGNOMEFLICKMACE = Weapon("Gnome Flickmace"
                              , ""
                              , "", "", 0.0, 0.00, 1
                              , [], []
                              , "", "", "", 1
                              , "")

weaponDAGGER = Weapon("Dagger"
                      , ""
                      , "Weapons", "Simple", 0.1, 0.20, 1
                      , [traitAGILE, traitFINESSE, traitTHROWN, traitVERSATILE_S], []
                      , "Knife", "1d4", "Piercing", 1
                      , "")
weaponDAGGER.thrownRange = 10
