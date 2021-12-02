from Trait import *  # DONE Phase 1!


class Ancestry:

    def __init__(self, *args):
        self.name = args[0]
        self.description = args[1]
        self.traits = args[2]  # list of Traits
        self.HP = args[3]  # integer
        self.size = args[4]
        self.speed = args[5]  # integer
        self.abilityBoosts = args[6]  # list of strings
        self.abilityFlaws = args[7]  # list of strings
        self.languages = args[8]  # list of strings
        self.senses = args[9]  # list of strings
        self.other = args[10]  # list of strings
        self.heritage = args[11]  # list of Heritages


DexInt = ["Dexterity", "Intelligence"]
Free = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

ancestryHUMAN = Ancestry("Human"
                         , "Human"
                         , [traitHUMAN, traitHUMANOID]
                         , 8
                         , "Medium"
                         , 25
                         , [Free, Free]
                         , []
                         , ["Common", "Any"]
                         , []
                         , []
                         , [])

ancestry = Ancestry(""
                    , ""
                    , []
                    , 0
                    , "Medium"
                    , []
                    , []
                    , ["Common"]
                    , []
                    , []
                    , [])
