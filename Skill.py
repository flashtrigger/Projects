from SkillAction import *
from Variables import Proficiency


class Skill(Entity):

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.stat = args[1]
        self.proficiency = Proficiency.Untrained
        self.bonus = 0
        self.actions = args[3]  # list of actions


skillACROBATICS = Skill("Acrobatics"
                        , "Acrobatics measures your ability to perform tasks requiring coordination and grace. When "
                          "you use the Escape basic action, you can use your Acrobatics modifier instead of your "
                          "unarmed attack modifier.", "Dexterity"
                        , [actionBALANCE, actionTUMBLETHROUGH, actionMANEUVERINFLIGHT, activitySQUEEZE])

skillARCANA = Skill("Arcana"
                    , "Arcana measures how much you know about arcane magic and creatures. Even if you’re untrained, "
                      "you can Recall Knowledge. ", "Intelligence"
                    , [actionRECALLKNOWLEDGE, activityDECIPHERWRITING, activityIDENTIFYMAGIC, activityLEARNASPELL,
                       activityBORROWARCANE])

skillATHLETICS = Skill("Athletics"
                       , "Athletics allows you to perform deeds of physical prowess. When you use the Escape basic "
                         "action, you can use your Athletics modifier instead of your unarmed attack modifier. "
                       , "Strength"
                       , [actionCLIMB, actionFORCEOPEN, actionGRAPPLE, actionHIGHJUMP, actionLONGJUMP, actionSHOVE,
                          actionSWIM, actionTRIP, actionDISARM])

skillCRAFTING = Skill("Crafting"
                      , "You can use this skill to create, understand, and repair items. Even if you're untrained, "
                        "you can Recall Knowledge. ", "Intelligence"
                      , [activityEARNINCOME, activityREPAIR, activityCRAFT, activityIDENTIFYALCHEMY])

skillDECEPTION = Skill("Deception"
                       , "You can trick and mislead others using disguises, lies, and other forms of subterfuge."
                       , "Charisma"
                       , [actionCREATEDIVERSION, activityIMPERSONATE, actionLIE, actionFEINT])

skillDIPLOMACY = Skill("Diplomacy"
                       , "You influence others through negotiation and flattery.", "Charisma"
                       , [activityGATHERINFO, activityMAKEIMPRESSION, actionREQUEST])

skillINTIMIDATION = Skill("Intimidation"
                          , "You bend others to your will using threats.", "Charisma"
                          , [activityCOERCE, actionDEMORALIZE])

skillLORE = Skill("Lore"
                  , "You have specialized information on a narrow topic. Lore features many subcategories"
                  , "Intelligence"
                  , [actionRECALLKNOWLEDGE, activityEARNINCOME])

skillMEDICINE = Skill("Medicine"
                      , "You can patch up wounds and help people recover from diseases and poisons. Even if you’re "
                        "untrained in Medicine, you can use it to Recall Knowledge. ", "Wisdom"
                      , [actionRECALLKNOWLEDGE, actionADMINISTERFIRSTAID, activityTREATDISEASE, actionTREATPOISON,
                         activityTREATWOUNDS])

skillNATURE = Skill("Nature"
                    , "You know a great deal about the natural world, and you command and train animals and magical "
                      "beasts. Even if you’re untrained in Nature, you can use it to Recall Knowledge. ", "Wisdom"
                    , [actionRECALLKNOWLEDGE, activityIDENTIFYMAGIC, activityLEARNASPELL, actionCOMMANDANIMAL])

skillOCCULTISM = Skill("Occultism"
                       , "You know a great deal about ancient philosophies, esoteric lore, obscure mysticism, "
                         "and supernatural creatures. Even if you’re untrained in Occultism, you can use it to Recall "
                         "Knowledge. ", "Intelligence"
                       , [actionRECALLKNOWLEDGE, activityDECIPHERWRITING, activityIDENTIFYMAGIC, activityLEARNASPELL])

skillPERFORMANCE = Skill("Performance"
                         , "You are skilled at a form of performance, using your talents to impress a crowd or make a "
                           "living. ", "Charisma"
                         , [activityEARNINCOME, actionPERFORM])

skillRELIGION = Skill("Religion"
                      , "The secrets of deities, dogma, faith, and the realms of divine creatures both sublime and "
                        "sinister are open to you. You also understand how magic works, though your training imparts "
                        "a religious slant to that knowledge. Even if you’re untrained in Religion, you can use it to "
                        "Recall Knowledge. ", "Wisdom"
                      , [actionRECALLKNOWLEDGE, activityDECIPHERWRITING, activityIDENTIFYMAGIC, activityLEARNASPELL])

skillSOCIETY = Skill("Society"
                     , "You understand the people and systems that make civilization run, and you know the historical "
                       "events that make societies what they are today. Further, you can use that knowledge to "
                       "navigate the complex physical, societal, and economic workings of settlements. Even if you’re "
                       "untrained in Society, you can use it for the following general skill actions. ", "Intelligence"
                     , [actionRECALLKNOWLEDGE, activitySUBSIST, activityDECIPHERWRITING, activityCREATEFORGERY])

skillSTEALTH = Skill("Stealth"
                     , "You are skilled at avoiding detection, allowing you to slip past foes, hide, or conceal an "
                       "item. ", "Dexterity"
                     , [actionCONCEALOBJECT, actionHIDE, actionSNEAK])

skillSURVIVAL = Skill("Survival"
                      , "You are adept at living in the wilderness, foraging for food and building shelter, and with "
                        "training you discover the secrets of tracking and hiding your trail. Even if you’re "
                        "untrained, you can still use Survival to Subsist. ", "Wisdom"
                      , [activitySUBSIST, activitySENSEDIRECTION, activityCOVERTRACKS, activityTRACK])

skillTHIEVERY = Skill("Thievery"
                      , "You are trained in a particular set of skills favored by thieves and miscreants", "Dexterity"
                      , [actionPALMOBJECT, actionSTEAL, actionDISABLEDEVICE, actionPICKLOCK])

skillPACKAGE = [skillACROBATICS, skillARCANA, skillATHLETICS, skillCRAFTING, skillDECEPTION, skillDIPLOMACY,
                skillINTIMIDATION, skillLORE, skillMEDICINE, skillNATURE, skillOCCULTISM, skillPERFORMANCE,
                skillRELIGION, skillSOCIETY, skillSTEALTH, skillSURVIVAL, skillTHIEVERY]
