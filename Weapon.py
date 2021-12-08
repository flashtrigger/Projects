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
        self.thrownRange = None


weapon = Weapon(""
                , ""
                , "", "", 0.0, 0.00, 1
                , [], []
                , "", "", "", 1)

weaponGNOMEFLICKMACE = Weapon("Gnome Flickmace"
                              , "More a flail than a mace, this weapon has a short handle attached to a length of "
                                "chain with a ball at the end. The ball is propelled to its reach with the flick of "
                                "the wrist, the momentum of which brings the ball back to the wielder after the "
                                "strike. "
                              , "Weapons", "Advanced", 2.0, 3.00, 1
                              , [traitGNOME, traitREACH, traitUNCOMMON], []
                              , "Flail", "1d8", "Bludgeoning", 1)

weaponDAGGER = Weapon("Dagger"
                      , "This small, bladed weapon is held in one hand and used to stab a creature in close combat. "
                        "It can also be thrown. "
                      , "Weapons", "Simple", 0.1, 0.20, 1
                      , [traitAGILE, traitFINESSE, traitTHROWN, traitVERSATILE_S], []
                      , "Knife", "1d4", "Piercing", 1)
weaponDAGGER.thrownRange = 10
