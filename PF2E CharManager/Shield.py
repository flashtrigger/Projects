import math
from ACitem import ACItem


# name, description, category, subcategory, bulk, value, level. traits, actions, AC, speed penalty
class Shield(ACItem):  # DONE Phase 1!

    def __init__(self, *args):
        ACItem.__init__(self, *args)
        self.hardness = args[11]  # integer
        self.HP = args[12]  # integer
        self.BT = int(math.floor(self.HP / 2))  # integer


shield = Shield(""
                , ""
                , "", "", 0.0, 0.00, 1
                , [], []
                , 0, 0, 0, 0)

shieldSTEEL = Shield("Steel Shield"
                     , "Like wooden shields, steel shields come in a variety of shapes and sizes. Though more "
                       "expensive than wooden shields, they are much more durable. "
                     , "Armor", "Shield", 1, 2.00, 1
                     , [], []
                     , 2, 0, 5, 20)
