class Feat:

    def __init__(self, *args):

        self.type = args[0]
        self.name = args[1]
        self.description = args[2]
        self.level = args[3]  # integer
        self.traits = args[4]  # list of Traits
        self.spells = args[5]  # list of Spells
        self.actions = args[6]  # list of Actions

