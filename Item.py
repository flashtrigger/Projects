from Entity import Entity


class Item(Entity):  # DONE Phase 1!

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.category = args[2]
        self.subcategory = args[3]
        self.bulk = round(args[4], 1)   # float
        self.value = args[5]  # float
        self.level = args[6]  # integer
        self.traits = args[7]  # list of Traits
        self.actions = args[8]  # list of Actions
        self.count = 1


itemBACKPACK = Item("Backpack"
                    , "A backpack holds up to 4 Bulk of items. and the first 2 Bulk of these items don't count against "
                      "your Bulk limits. If you're carrying or stowing the pack rather than wearing it on your back, "
                      "its Bulk is light instead of negligible."
                    , "Adventuring Gear", None, -2.0, 0.1, 1, [], [])
# p3TODO: initialize PHB items
