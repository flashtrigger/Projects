from Skill import *
from Action import *
from Spell import *


class Feat(Entity):  # DONE Phase 1?

    def __init__(self, *args):
        Entity.__init__(self, *args)
        self.level = args[2]  # integer
        self.prerequisites = args[3]  # list of objects
        self.traits = args[4]  # list of Traits
        self.spells = args[5]  # list of Spells
        self.actions = args[6]  # list of Actions


featARCANESENSE = Feat("Arcane Sense"
                       , "Your study of magic allows you to instinctively sense its presence. You can cast 1st-level "
                         "detect magic at will as an arcane innate spell. If you’re a master in Arcana, the spell is "
                         "heightened to 3rd level; if you’re legendary, it is heightened to 4th level. "
                       , 1
                       , [skillARCANA]
                       , [traitGENERAL, traitSKILL]
                       , [spellDETECTMAGIC_AS]
                       , [])
featARCANESENSE.prerequisites[0].proficiency = Proficiency.Trained

featCATFALL = Feat("Catfall"
                   , "Your catlike aerial acrobatics allow you to cushion your falls. Treat falls as 10 feet shorter. "
                     "If you’re an expert in Acrobatics, treat falls as 25 feet shorter. If you’re a master in "
                     "Acrobatics, treat them as 50 feet shorter. If you’re legendary in Acrobatics, you always land "
                     "on your feet and don’t take damage, regardless of the distance of the fall. "
                   , 1
                   , [skillACROBATICS]
                   , [traitGENERAL, traitSKILL]
                   , []
                   , [])
featCATFALL.prerequisites[0].proficiency = Proficiency.Trained

featDOUBLESLICE = Feat("Double Slice"
                       , "You lash out at your foe with both weapons. Make two Strikes, one with each of your two "
                         "melee weapons, each using your current multiple attack penalty. Both Strikes must have the "
                         "same target. If the second Strike is made with a weapon that doesn't have the agile trait, "
                         "it takes a –2 penalty.\nIf both attacks hit, combine their damage, and then add any other "
                         "applicable effects from both weapons. You add any precision damage only once, to the attack "
                         "of your choice. Combine the damage from both Strikes and apply resistances and weaknesses "
                         "only once. This counts as two attacks when calculating your multiple attack penalty. "
                       , 2
                       , []
                       , [traitFIGHTER, traitATTACK]
                       , []
                       , [actionDOUBLESLICE])

featDRAGONSPITE = Feat("Dragon Spit: Electric"
                       , "Many Tian-Dan claim to have dragon blood in their veins, and in your case, this is true—you "
                         "can spit energy, and you might have an especially visible sign of your draconic heritage. "
                         "You gain the following cantrip: electric arc "
                         "You can cast this spell as an innate arcane spell at will, and when you "
                         "cast it, the spell’s energy emerges from your mouth. "
                       , 1
                       , ["Tian-Dan Ethnicity"]
                       , [traitHUMAN]
                       , [spellELECTRICARC_DS]
                       , [])

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
                               , 1
                               , [skillSTEALTH]
                               , [traitGENERAL, traitSKILL]
                               , []
                               , [])
featEXPERIENCEDSMUGGLER.prerequisites[0].proficiency = Proficiency.Trained

featHUNTEDSHOT = Feat("Hunted Shot"
                      , "You take two quick shots against the one you hunt. Make two Strikes against your prey with "
                        "the required weapon. If both hit the same creature, combine their damage for the purpose of "
                        "resistances and weaknesses. Apply your multiple attack penalty to each Strike normally. "
                      , 1
                      , []
                      , [traitRANGER, traitFLOURISH]
                      , []
                      , [actionHUNTEDSHOT])

featINTIMIDATINGGLARE = Feat("Intimidating Glare"
                             , "You can Demoralize with a mere glare. When you do, Demoralize loses the auditory "
                               "trait and gains the visual trait, and you don’t take a penalty if the creature "
                               "doesn't understand your language. "
                             , 1
                             , [skillINTIMIDATION]
                             , [traitGENERAL, traitSKILL]
                             , []
                             , [])  # p2TODO: alternate actionDEMORALIZE
featINTIMIDATINGGLARE.prerequisites[0].proficiency = Proficiency.Trained

featMONSTERHUNTER = Feat("Monster Hunter"
                         , "You swiftly assess your prey and apply what you know. As part of the action used to Hunt "
                           "your Prey, you can attempt a check to Recall Knowledge about your prey. When you "
                           "critically succeed at identifying your hunted prey with Recall Knowledge, you note a "
                           "weakness in the creature’s defenses. You and allies you tell gain a +1 circumstance bonus "
                           "to your next attack roll against that prey. You can give bonuses from Monster Hunter only "
                           "once per day against a particular creature. "
                         , 1
                         , []
                         , [traitRANGER]
                         , []
                         , [actionHUNTPREY_MH])

# p2TODO: build a feat picker within Natural Ambition
featNATURALAMBITION = Feat("Natural Ambition"
                           , "You were raised to be ambitious and always reach for the stars, leading you to progress "
                             "quickly in your chosen field. You gain a 1st-level class feat for your class. You must "
                             "meet the prerequisites, but you can select the feat later in the character creation "
                             "process in order to determine which prerequisites you meet. "
                           , 1
                           , []
                           , [traitHUMAN]
                           , []
                           , [])

featNIMBLEDODGE = Feat("Nimble Dodge"
                       , "You deftly dodge out of the way, gaining a +2 circumstance bonus to AC against the "
                         "triggering attack. "
                       , 1
                       , []
                       , [traitROGUE, traitSWASHBUCKLER]
                       , []
                       , [actionNIMBLEDODGE])

featNIMBLEELF = Feat("Nimble Elf"
                     , "Your muscles are tightly honed. Your Speed increases by 5 feet."
                     , 1
                     , []
                     , [traitELF]
                     , []
                     , [])

featORCFEROCITY = Feat("Orc Ferocity"
                       , "Fierceness in battle runs through your blood, and you refuse to fall from your injuries. "
                         "You avoid being knocked out and remain at 1 Hit Point, and your wounded condition increases "
                         "by 1. "
                       , 1
                       , []
                       , [traitORC]
                       , []
                       , [actionORCFEROCITY])

# p3TODO: featQUICKJUMP
featQUICKJUMP = Feat(""
                     , ""
                     , 1
                     , []
                     , []
                     , []
                     , [])

# p2TODO: automate update of actionDEMORALIZE and actionSCARETODEATH
# p2TODO: feat in a feat
featRAGINGINTIMIDATION = Feat("Raging Intimidation"
                              , "Your fury fills your foes with fear. While you are raging, your Demoralize and Scare "
                                "to Death actions (from the Intimidation skill and an Intimidation skill feat, "
                                "respectively) gain the rage trait, allowing you to use them while raging. As soon as "
                                "you meet the prerequisites for the skill feats Intimidating Glare and Scare to "
                                "Death, you gain these feats. "
                              , 1
                              , []
                              , [traitBARBARIAN]
                              , []
                              , [])

featREACTIVESHIELD = Feat("Reactive Shield"
                          , "You can snap your shield into place just as you would take a blow, avoiding the hit at "
                            "the last second. You immediately use the Raise a Shield action and gain your shield’s "
                            "bonus to AC. The circumstance bonus from the shield applies to your AC when you’re "
                            "determining the outcome of the triggering attack. "
                          , 1
                          , []
                          , [traitFIGHTER]
                          , []
                          , [actionREACTIVESHIELD])

featSHIELDBLOCK = Feat("Shield Block"
                       , "You snap your shield in place to ward off a blow. Your shield prevents you from taking an "
                         "amount of damage up to the shield’s Hardness. You and the shield each take any remaining "
                         "damage, possibly breaking or destroying the shield. "
                       , 1
                       , []
                       , [traitGENERAL]
                       , []
                       , [actionSHIELDBLOCK])

featUNCONVENTIONALWEAPONRY = Feat("Unconventional Weaponry"
                                  , "You've familiarized yourself with a particular weapon, potentially from another "
                                    "ancestry or culture. Choose an uncommon simple or martial weapon with a trait "
                                    "corresponding to an ancestry (such as dwarf, goblin, or orc) or that is common "
                                    "in another culture. You gain access to that weapon, and for the purpose of "
                                    "determining your proficiency, that weapon is a simple weapon.\nIf you are "
                                    "trained in all martial weapons, you can choose an uncommon advanced weapon with "
                                    "such a trait. You gain access to that weapon, and for the purpose of determining "
                                    "your proficiency, that weapon is a martial weapon. "
                                  , 1
                                  , []
                                  , [traitHUMAN]
                                  , []
                                  , [])

feat = Feat(""
            , ""
            , 1
            , []
            , []
            , []
            , [])
