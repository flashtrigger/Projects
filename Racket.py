from Skill import *
from Variables import *


class Racket(Entity):

    def __init__(self, *args):
        Entity.__init__(self, *args)
        self.skills = args[2]  # list of Skills
        self.statChoices = args[3]  # from Variables
        self.actions = args[4]  # list of Actions
        self.bProficiency = args[5]  # list of BaseProficiencies


racket = Racket(""
                , ""
                , []
                , []
                , []
                , [])

racketMASTERMIND = Racket("MasterMind"
                          , "Where others might use sleight of hand or a silver tongue to achieve their objectives, "
                            "you rely on your intellect to craft intricate schemes. You likely view your operations "
                            "as a chess game, always planning 10 steps ahead where others might plan three. You might "
                            "be a detective determined to solve crimes or a spymaster in the service of a powerful "
                            "family or nation. If you operate outside the law, you might be an aspiring crime lord or "
                            "information broker, excellent at directing others toward suitable jobs.\nIf you "
                            "successfully identify a creature using Recall Knowledge, that creature is flat-footed "
                            "against your attacks until the start of your next turn; if you critically succeed, "
                            "it's flat-footed against your attacks for 1 minute. "
                          , [skillSOCIETY, [skillARCANA, skillNATURE, skillOCCULTISM, skillRELIGION]]
                          , [DexInt]
                          , []
                          , [])
racketMASTERMIND.skills[0].proficiency = Proficiency.Trained
racketMASTERMIND.skills[1][0].proficiency = Proficiency.Trained
racketMASTERMIND.skills[1][1].proficiency = Proficiency.Trained
racketMASTERMIND.skills[1][2].proficiency = Proficiency.Trained
racketMASTERMIND.skills[1][3].proficiency = Proficiency.Trained
