from Feat import *
from Skill import *
from Trait import *
from Variables import *


class Background(Entity):  # DONE?

    def __init__(self, *args):
        Entity.__init__(self, *args)
        self.abilityBoosts = args[2]  # list of choices
        self.skills = args[3]  # list of skills
        self.lore = args[4]
        self.feats = args[5]  # list of Feats
        self.traits = args[6]  # list of Traits
        self.actions = args[7]  # list of Actions


backgroundCRIMINAL = Background("Criminal"
                                , "As an unscrupulous independent or as a member of an underworld organization, "
                                  "you lived a life of crime. You might have become an adventurer to seek redemption, "
                                  "to escape the law, or simply to get access to bigger and better loot. "
                                , [DexInt, Free]
                                , [copy.deepcopy(skillSTEALTH)]
                                , "Underworld"
                                , [featEXPERIENCEDSMUGGLER]
                                , [traitCOMMON]
                                , [])
backgroundCRIMINAL.skills[0].proficiency = Proficiency.Trained

backgroundMARTIALADEPT = Background("Martial Adept"
                                    , "You dedicated yourself to intense training and rigorous study to become a "
                                      "great warrior. The school you attended might have been a traditionalist "
                                      "monastery, an elite military academy, or the local branch of a prestigious "
                                      "mercenary organization. "
                                    , [StrDex, Free]
                                    , [[copy.deepcopy(skillACROBATICS), copy.deepcopy(skillATHLETICS)]]
                                    , "Warfare"
                                    , [[featCATFALL, featQUICKJUMP]]
                                    , [traitCOMMON]
                                    , [])
backgroundMARTIALADEPT.skills[0][0].proficiency = Proficiency.Trained
backgroundMARTIALADEPT.skills[0][1].proficiency = Proficiency.Trained
