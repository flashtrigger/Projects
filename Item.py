import math


class Item:

    def __init__(self, *args):
        self.name = args[0]
        self.category = args[1]
        self.subcategory = args[2]
        self.bulk = args[3]
        self.value = args[4]
        self.level = args[5]
        self.rarity = args[6]
        self.traits = args[7]
        self.type = args[8]

        if self.category == "Weapon":  # TODO: divide into subclasses
            self.group = args[9]
            self.damage = args[10]
            self.dType = args[11]
            self.hands = args[12]
            self.specialization = args[13]
            if self.type == "Ranged":
                self.range = args[14]
                self.reload = args[15]
        elif self.category == "Armor" or "Shield":
            self.AC = args[9]
            self.speedPenalty = args[10]
            if self.category == "Armor":
                self.dexCap = args[11]
                self.checkPenalty = args[12]
                self.group = args[13]
                self.minSTR = args[14]
            elif self.category == "Shield":
                self.hardness = args[11]
                self.HP = args[12]
                self.BT = math.floor(self.HP / 2)
