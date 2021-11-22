from Item import Item
import math


class Armor(Item):

    def __init__(self, *args):

        Item.__init__(self, *args)
        self.AC = args[8]  # integer
        self.speedPenalty = args[9]  # integer
        if self.category == "Armor":
            self.dexCap = args[10]  # integer
            self.checkPenalty = args[11]  # integer
            self.group = args[12]
            self.minSTR = args[13]  # integer
        elif self.category == "Shield":
            self.hardness = args[10]  # integer
            self.HP = args[11]  # integer
            self.BT = int(math.floor(self.HP / 2))  # integer
