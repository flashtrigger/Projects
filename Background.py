class Background:

    def __init__(self, *args):

        self.name = args[0]
        self.description = args[1]
        self.abilityBoosts = args[2]  # list of choices
        self.skills = args[3]  # list of skills
        self.lore = args[4]
        self.feat = args[5]  # list of Feats
