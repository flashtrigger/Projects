from Item import Item
import math


# TODO: Split class Armor
class ACItem(Item):

    def __init__(self, *args):

        Item.__init__(self, *args)
        self.AC = args[9]  # integer
        self.speedPenalty = args[10]  # integer
        if self.category == "Armor":
            self.dexCap = args[11]  # integer
            self.checkPenalty = args[12]  # integer
            self.group = args[13]
            self.minSTR = args[14]  # integer
        elif self.category == "Shield":
            self.hardness = args[11]  # integer
            self.HP = args[12]  # integer
            self.BT = int(math.floor(self.HP / 2))  # integer


# TODO: pick 2 armors to initialize
