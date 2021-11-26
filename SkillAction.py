from Action import Action
from Trait import *


class SkillAction(Action):

    def __init__(self, *args):
        Action.__init__(self, *args)
        self.untrained = args[11]
        self.trained = args[12]
        self.expert = args[13]
        self.master = args[14]
        self.legendary = args[15]
        self.isTrained = args[16]  # boolean


# acrobatics
actionBALANCE = SkillAction("Balance"
                            , 1
                            ,
                            "You move across a narrow surface or uneven ground, attempting an Acrobatics check "
                            "against its Balance DC. You are flat-footed while on a narrow surface or uneven ground. "
                            , [traitMOVE]
                            , "Encounter"
                            , "You fall and your turn ends."
                            ,
                            "You must remain stationary to keep your balance (wasting the action) or you fall. If you "
                            "fall, your turn ends. "
                            ,
                            "You move up to your Speed, treating it as difficult terrain (every 5 feet costs 10 feet "
                            "of movement). "
                            , "You move up to your Speed."
                            , "You are in a square that contains a narrow surface, uneven ground, or another similar "
                              "feature. "
                            , None
                            , "tangled roots, uneven cobblestones"
                            , "wooden beam"
                            , "deep, loose gravel"
                            , "tightrope, smooth sheet of ice"
                            , "razor’s edge, chunks of floor falling in midair"
                            , False)

actionTUMBLETHROUGH = SkillAction("Tumble Through"
                                  , 1
                                  ,
                                  "You Stride up to your Speed. During this movement, you can try to move through the "
                                  "space of one enemy. Attempt an Acrobatics check against the enemy’s Reflex DC as "
                                  "soon as you try to enter its space. You can Tumble Through using Climb, Fly, Swim, "
                                  "or another action instead of Stride in the appropriate environment. "
                                  , [traitMOVE]
                                  , "Encounter"
                                  , None
                                  ,
                                  "Failure Your movement ends, and you trigger reactions as if you had moved out of "
                                  "the square you started in. "
                                  ,
                                  "You move through the enemy’s space, treating the squares in its space as difficult "
                                  "terrain (every 5 feet costs 10 feet of movement). If you don’t have enough Speed "
                                  "to move all the way through its space, you get the same effect as a failure. "
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , False)

actionMANEUVERINFLIGHT = SkillAction("Maneuver in Flight"
                                     , 1
                                     ,
                                     "You try a difficult maneuver while flying. Attempt an Acrobatics check. The GM "
                                     "determines what maneuvers are possible, but they rarely allow you to move "
                                     "farther than your fly Speed. "
                                     , [traitMOVE]
                                     , "Encounter"
                                     , "As failure, but the consequence is more dire."
                                     , "Your maneuver fails. The GM chooses if you simply can’t move or if some other "
                                       "detrimental effect happens. The outcome should be appropriate for the "
                                       "maneuver you attempted (for instance, being blown off course if you were "
                                       "trying to fly against a strong wind). "
                                     , "You succeed at the maneuver."
                                     , None
                                     , "You have a fly Speed."
                                     , None
                                     , None
                                     , "steep ascent or descent"
                                     , "fly against the wind, hover midair"
                                     , "reverse direction"
                                     , "fly through gale force winds"
                                     , True)

actionSQUEEZE = SkillAction(""
                            , 1
                            , ""
                            , []
                            , ""
                            , None
                            , None
                            , None
                            , None
                            , None
                            , None
                            , ""
                            , ""
                            , ""
                            , ""
                            , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")

action = SkillAction(""
                     , 1
                     , ""
                     , []
                     , ""
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None
                     , ""
                     , ""
                     , ""
                     , ""
                     , "")
