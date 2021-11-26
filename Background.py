from Action import *
from Feat import *
from Skill import *
from Trait import *


class Background:

    def __init__(self, *args):
        self.name = args[0]
        self.description = args[1]
        self.abilityBoosts = args[2]  # list of choices
        self.skills = args[3]  # list of skills
        self.lore = args[4]
        self.feat = args[5]  # list of Feats
        self.traits = args[6]  # list of Traits
        self.actions = args[7]  # list of Actions


DexInt = ["Dexterity", "Intelligence"]
Free = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

backgroundCRIMINAL = Background("Criminal"
                                , "As an unscrupulous independent or as a member of an underworld organization, "
                                  "you lived a life of crime. You might have become an adventurer to seek redemption, "
                                  "to escape the law, or simply to get access to bigger and better loot. "
                                , [DexInt, Free]
                                , []  # TODO: initialize default skill objects
                                , "Underworld"
                                , []  # TODO: initialize default feat objects
                                , [traitCOMMON]
                                , [])

background = Background(""
                        , ""
                        , []
                        , []
                        , ""
                        , []
                        , []
                        , [])
