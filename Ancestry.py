class Ancestry:

    def __init__(self, *args):

        self.name = args[0]
        self.description = args[1]
        self.traits = args[2]  # list of Traits
        self.HP = args[3]  # integer
        self.size = args[4]
        self.abilityBoosts = args[5]  # list of strings
        self.abilityFlaws = args[6]  # list of strings
        self.languages = args[7]  # list of strings
        self.senses = args[8]  # list of strings
        self.other = args[9]  # list of strings
        self.heritage = args[10]  # list of Heritages
