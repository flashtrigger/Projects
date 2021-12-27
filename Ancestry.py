from Trait import *
from Variables import *


class Ancestry(Entity):

    def __init__(self, *args):
        Entity.__init__(self, *args)
        self.traits = args[2]  # list of Traits
        self.HP = args[3]  # integer
        self.size = args[4]  # size class
        self.speed = args[5]  # integer
        self.abilityBoosts = args[6]  # list of strings
        self.abilityFlaws = args[7]  # list of strings
        self.languages = args[8]  # list of strings
        self.senses = args[9]  # list of strings
        self.other = args[10]  # list of strings
        self.heritage = args[11]  # list of Heritages


ancestryHUMAN = Ancestry("Human"
                         , "Human"
                         , [traitHUMAN, traitHUMANOID]
                         , 8
                         , Size.Medium
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
                    , 0
                    , []
                    , []
                    , ["Common"]
                    , []
                    , []
                    , [])
