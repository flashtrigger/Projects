from Item import Item


class ACItem(Item):

    def __init__(self, *args):

        Item.__init__(self, *args)
        self.AC = args[9]  # integer
        self.speedPenalty = args[10]  # integer
