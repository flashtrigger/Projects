class Item:

    def __init__(self, *args):
        self.name = args[0]
        self.category = args[1]
        self.subcategory = args[2]
        self.bulk = args[3]   # float
        self.value = args[4]  # float
        self.level = args[5]  # integer
        self.traits = args[6]  # list of Traits
        self.type = args[7]
