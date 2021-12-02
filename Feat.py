from Skill import *
from Action import *
from Spell import *


class Feat:  # DONE Phase 1?

    def __init__(self, *args):
        self.name = args[0]
        self.description = args[1]
        self.type = args[2]
        self.level = args[3]  # integer
        self.prerequisites = args[4]  # list of objects
        self.traits = args[5]  # list of Traits
        self.spells = args[6]  # list of Spells
        self.actions = args[7]  # list of Actions


featEXPERIENCEDSMUGGLER = Feat("Experienced Smuggler"
                               , "You often smuggle things past the authorities. When the GM rolls your Stealth check "
                                 "to see if a passive observer notices a small item you have concealed, the GM uses "
                                 "the number rolled or 10—whichever is higher—as the result of your die roll, "
                                 "adding it to your Stealth modifier to determine your Stealth check result. If "
                                 "you’re a master in Stealth, the GM uses the number rolled or 15, and if you’re "
                                 "legendary in Stealth, you automatically succeed at hiding a small concealed item "
                                 "from passive observers. This provides no benefits when a creature attempts a "
                                 "Perception check while actively searching you for hidden items. Due to your "
                                 "smuggling skill, you’re more likely to find more lucrative smuggling jobs when "
                                 "using Underworld Lore to Earn Income.\nPFS Note Allows you to always Earn Income "
                                 "with the Underworld Lore with tasks of your level -1 (instead of the normal level "
                                 "-2). "
                               , "Feat"
                               , 1
                               , [skillSTEALTH]
                               , [traitGENERAL, traitSKILL]
                               , []
                               , [])
featEXPERIENCEDSMUGGLER.prerequisites[0].proficiency.name = "Trained"

# p2TODO: build a feat picker within Natural Ambition
featNATURALAMBITION = Feat("Natural Ambition"
                           , "You were raised to be ambitious and always reach for the stars, leading you to progress "
                             "quickly in your chosen field. You gain a 1st-level class feat for your class. You must "
                             "meet the prerequisites, but you can select the feat later in the character creation "
                             "process in order to determine which prerequisites you meet. "
                           , "Feat"
                           , 1
                           , []
                           , [traitHUMAN]
                           , []
                           , [])

featNIMBLEELF = Feat("Nimble Elf"
                     , "Your muscles are tightly honed. Your Speed increases by 5 feet."
                     , "Feat"
                     , 1
                     , []
                     , [traitELF]
                     , []
                     , [])

featNIMBLEDODGE = Feat("Nimble Dodge"
                       , "You deftly dodge out of the way, gaining a +2 circumstance bonus to AC against the "
                         "triggering attack. "
                       , "Feat"
                       , 1
                       , []
                       , [traitROGUE, traitSWASHBUCKLER]
                       , []
                       , [actionNIMBLEDODGE])

featARCANESENSE = Feat("Arcane Sense"
                       , "Your study of magic allows you to instinctively sense its presence. You can cast 1st-level "
                         "detect magic at will as an arcane innate spell. If you’re a master in Arcana, the spell is "
                         "heightened to 3rd level; if you’re legendary, it is heightened to 4th level. "
                       , "Feat"
                       , 1
                       , [skillARCANA]
                       , [traitGENERAL, traitSKILL]
                       , [spellDETECTMAGIC_AS]
                       , [])
featARCANESENSE.prerequisites[0].proficiency = Proficiency.Trained

featMONSTERHUNTER = Feat("Monster Hunter"
                         , "You swiftly assess your prey and apply what you know. As part of the action used to Hunt "
                           "your Prey, you can attempt a check to Recall Knowledge about your prey. When you "
                           "critically succeed at identifying your hunted prey with Recall Knowledge, you note a "
                           "weakness in the creature’s defenses. You and allies you tell gain a +1 circumstance bonus "
                           "to your next attack roll against that prey. You can give bonuses from Monster Hunter only "
                           "once per day against a particular creature. "
                         , "Feat"
                         , 1
                         , []
                         , [traitRANGER]
                         , []
                         , [actionHUNTPREY_MH])

featDRAGONSPITE = Feat("Dragon Spit: Electric"
                       , "Many Tian-Dan claim to have dragon blood in their veins, and in your case, this is true—you "
                         "can spit energy, and you might have an especially visible sign of your draconic heritage. "
                         "You gain the following cantrip: electric arc "
                         "You can cast this spell as an innate arcane spell at will, and when you "
                         "cast it, the spell’s energy emerges from your mouth. "
                       , "Feat"
                       , 1
                       , ["Tian-Dan Ethnicity"]
                       , [traitHUMAN]
                       , [spellELECTRICARC_DS]
                       , [])

featORCFEROCITY = Feat("Orc Ferocity"
                       , "Fierceness in battle runs through your blood, and you refuse to fall from your injuries. "
                         "You avoid being knocked out and remain at 1 Hit Point, and your wounded condition increases "
                         "by 1. "
                       , "Feat"
                       , 1
                       , []
                       , [traitORC]
                       , []
                       , [actionORCFEROCITY])

featDOUBLESLICE = Feat("Double Slice"
                       , "You lash out at your foe with both weapons. Make two Strikes, one with each of your two "
                         "melee weapons, each using your current multiple attack penalty. Both Strikes must have the "
                         "same target. If the second Strike is made with a weapon that doesn't have the agile trait, "
                         "it takes a –2 penalty.\nIf both attacks hit, combine their damage, and then add any other "
                         "applicable effects from both weapons. You add any precision damage only once, to the attack "
                         "of your choice. Combine the damage from both Strikes and apply resistances and weaknesses "
                         "only once. This counts as two attacks when calculating your multiple attack penalty. "
                       , "Feat"
                       , 2
                       , []
                       , [traitFIGHTER, traitATTACK]
                       , []
                       , [actionDOUBLESLICE])

featHUNTEDSHOT = Feat("Hunted Shot"
                      , "You take two quick shots against the one you hunt. Make two Strikes against your prey with "
                        "the required weapon. If both hit the same creature, combine their damage for the purpose of "
                        "resistances and weaknesses. Apply your multiple attack penalty to each Strike normally. "
                      , "Feat"
                      , 1
                      , []
                      , [traitRANGER, traitFLOURISH]
                      , []
                      , [actionHUNTEDSHOT])

# p2TODO: automate update of actionDEMORALIZE and actionSCARETODEATH
# p2TODO: feat in a feat
featRAGINGINTIMIDATION = Feat("Raging Intimidation"
                              , "Your fury fills your foes with fear. While you are raging, your Demoralize and Scare "
                                "to Death actions (from the Intimidation skill and an Intimidation skill feat, "
                                "respectively) gain the rage trait, allowing you to use them while raging. As soon as "
                                "you meet the prerequisites for the skill feats Intimidating Glare and Scare to "
                                "Death, you gain these feats. "
                              , "Feat"
                              , 1
                              , []
                              , [traitBARBARIAN]
                              , []
                              , [])

featCATFALL = Feat("Catfall"
                   , "Your catlike aerial acrobatics allow you to cushion your falls. Treat falls as 10 feet shorter. "
                     "If you’re an expert in Acrobatics, treat falls as 25 feet shorter. If you’re a master in "
                     "Acrobatics, treat them as 50 feet shorter. If you’re legendary in Acrobatics, you always land "
                     "on your feet and don’t take damage, regardless of the distance of the fall. "
                   , "Feat"
                   , 1
                   , [skillACROBATICS]
                   , [traitGENERAL, traitSKILL]
                   , []
                   , [])
featCATFALL.prerequisites[0].proficiency = Proficiency.Trained

featINTIMIDATINGGLARE = Feat("Intimidating Glare"
                             , "You can Demoralize with a mere glare. When you do, Demoralize loses the auditory "
                               "trait and gains the visual trait, and you don’t take a penalty if the creature "
                               "doesn't understand your language. "
                             , "Feat"
                             , 1
                             , [skillINTIMIDATION]
                             , [traitGENERAL, traitSKILL]
                             , []
                             , [])  # p2TODO: alternate actionDEMORALIZE
featINTIMIDATINGGLARE.prerequisites[0].proficiency = Proficiency.Trained

# p3TODO: featQUICKJUMP
featQUICKJUMP = Feat(""
                     , ""
                     , "Feat"
                     , 1
                     , []
                     , []
                     , []
                     , [])

feat = Feat(""
            , ""
            , "Feat"
            , 1
            , []
            , []
            , []
            , [])
