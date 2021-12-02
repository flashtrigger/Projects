from ACitem import ACItem


class Armor(ACItem):  # DONE Phase 1!

    def __init__(self, *args):

        ACItem.__init__(self, *args)
        self.dexCap = args[10]  # integer
        self.checkPenalty = args[11]  # integer
        self.group = args[12]
        self.minSTR = args[13]  # integer


# name, category, subcategory, bulk, value, level, traits, actions, AC, Speed-, Armor inputs
armor = Armor("Name", "Category", "Subcategory", 0.0, 0.00, 1, [], [], 0, 0, 0, 0, "group", 0)

armorSTUDDEDLEATHER = Armor("Studded Leather", "Armor", "Light", 1.0, 3.00, 1, [], [], 2, 0, 3, -1, "Leather", 12)
