from Action import *
from Entity import Entity


class ClassFeature(Entity):

    def __init__(self, *args):
        Entity.__init__(self, *args)
        self.level = args[2]  # integer
        self.actions = None  # list of Actions
        self.functions = None  # method that updates character i.e addFeat, upgrade skill etc p2


# Barbarian
featureRAGE = ClassFeature("Rage"
                           , "You gain the Rage action, which lets you fly into a frenzy."
                           , 1)
featureRAGE.actions = [actionRAGE]

# Fighter
featureATTACKOPPORTUNITY = ClassFeature("Attack of Opportunity"
                                        , "Ever watchful for weaknesses, you can quickly attack foes that leave an "
                                          "opening in their defenses. You gain the Attack of Opportunity reaction. "
                                        , 1)
featureATTACKOPPORTUNITY.actions = [actionATTACKOPPORTUNITY]

# Ranger
featureHUNTPREY = ClassFeature("Hunt prey"
                               , "When you focus your attention on a single foe, you become unstoppable in your "
                                 "pursuit. You gain the Hunt Prey action. "
                               , 1)
featureHUNTPREY.actions = [actionHUNTPREY]

# Rogue
featureSNEAKATTACK1 = ClassFeature("Sneak Attack"
                                   , "When your enemy can’t properly defend itself, you take advantage to deal extra "
                                     "damage. If you Strike a creature that has the flat-footed condition with an "
                                     "agile or finesse melee weapon, an agile or finesse unarmed attack, or a ranged "
                                     "weapon attack, you deal an extra 1d6 precision damage. For a ranged attack with "
                                     "a thrown melee weapon, that weapon must also be agile or finesse.\nAs your "
                                     "rogue level increases, so does the number of damage dice for your sneak attack. "
                                     "Increase the number of dice by one at 5th, 11th, and 17th levels. "
                                   , 1)

featureSURPRISEATTACK = ClassFeature("Surprise Attack"
                                     , "You spring into combat faster than foes can react. On the first round of "
                                       "combat, if you roll Deception or Stealth for initiative, creatures that "
                                       "haven’t acted are flat-footed to you. "
                                     , 1)

feature = ClassFeature(""
                       , ""
                       , 1)
