import math
from ACitem import ACItem


class Shield(ACItem):  # DONE Phase 1!

    def __init__(self, *args):

        ACItem.__init__(self, *args)
        self.hardness = args[10]  # integer
        self.HP = args[11]  # integer
        self.BT = int(math.floor(self.HP / 2))  # integer
