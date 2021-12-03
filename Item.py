from Entity import Entity


class Item(Entity):  # DONE Phase 1!

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.category = args[2]
        self.subcategory = args[3]
        self.bulk = args[4]   # float
        self.value = args[5]  # float
        self.level = args[6]  # integer
        self.traits = args[7]  # list of Traits
        self.actions = args[8]  # list of Actions


# p3TODO: initialize PHB items
