import copy

from Trait import *  # p2TODO: remove unnecessary imports all around


# 306 - Specialty Basic ; 389 - Class ; 411 - Feat
class Action(Entity):  # DONE Phase 1?

    def __init__(self, *args):
        """

        :rtype: object
        """
        Entity.__init__(self, *args)
        self.numActions = args[2]  # integer, -1 = reaction, 0 = free
        self.traits = args[3]  # list of Traits
        self.critFail = args[4]
        self.fail = args[5]
        self.success = args[6]
        self.critSuccess = args[7]
        self.requirements = args[8]
        self.trigger = args[9]
        self.frequency = ""


# basic actions
actionAID = Action("Aid"
                   , "You try to help your ally with a task. To use this reaction, you must first prepare to "
                     "help, usually by using an action during your turn. You must explain to the GM exactly "
                     "how you’re trying to help, and they determine whether you can Aid your ally. When you "
                     "use your Aid reaction, attempt a skill check or attack roll of a type decided by the "
                     "GM. The typical DC is 20, but the GM might adjust this DC for particularly hard or "
                     "easy tasks. The GM can add any relevant traits to your preparatory action or to your "
                     "Aid reaction depending on the situation, or even allow you to Aid checks other than "
                     "skill checks and attack rolls."
                   , -1
                   , []
                   , "Your ally takes a –1 circumstance penalty to the triggering check."
                   , None
                   , "You grant your ally a +1 circumstance bonus to the triggering check."
                   , "You grant your ally a +2 circumstance bonus to the triggering check. If you’re a master with "
                     "the check you attempted, the bonus is +3, and if you’re legendary, it’s +4."
                   , "The ally is willing to accept your aid, and you have prepared to help"
                   , "An ally is about to use an action that requires a skill check or attack roll.")

actionCRAWL = Action("Crawl"
                     , "You move 5 feet by crawling and continue to stay prone."
                     , 1
                     , [traitMOVE]
                     , None
                     , None
                     , None
                     , None
                     , "You are prone and your Speed is at least 10 feet."
                     , None)

actionDELAY = Action("Delay"
                     , "You wait for the right moment to act. The rest of your turn doesn't happen yet. Instead, "
                       "you’re removed from the initiative order. You can return to the initiative order as a free "
                       "action triggered by the end of any other creature’s turn. This permanently changes your "
                       "initiative to the new position. You can’t use reactions until you return to the initiative "
                       "order. If you Delay an entire round without returning to the initiative order, the actions "
                       "from the Delayed turn are lost, your initiative doesn't change, and your next turn occurs at "
                       "your original position in the initiative order. When you Delay, any persistent damage or "
                       "other negative effects that normally occur at the start or end of your turn occur immediately "
                       "when you use the Delay action. Any beneficial effects that would end at any point during your "
                       "turn also end. The GM might determine that other effects end when you Delay as well. "
                       "Essentially, you can’t Delay to avoid negative consequences that would happen on your turn or "
                       "to extend beneficial effects that would end on your turn. "
                     , 0
                     , []
                     , None
                     , None
                     , None
                     , None
                     , None
                     , "Your turn begins.")

actionDROPPRONE = Action("Drop Prone"
                         , "You fall prone."
                         , 1
                         , [traitMOVE]
                         , None
                         , None
                         , None
                         , None
                         , None
                         , None)

actionESCAPE = Action("Escape"
                      , "You attempt to escape from being grabbed, immobilized, or restrained. Choose one creature, "
                        "object, spell effect, hazard, or other impediment imposing any of those conditions on you. "
                        "Attempt a check using your unarmed attack modifier against the DC of the effect. This is "
                        "typically the Athletics DC of a creature grabbing you, the Thievery DC of a creature who tied "
                        "you up, the spell DC for a spell effect, or the listed Escape DC of an object, hazard, "
                        "or other impediment. You can attempt an Acrobatics or Athletics check instead of using your "
                        "attack modifier if you choose (but this action still has the attack trait). "
                      , 1
                      , [traitATTACK]
                      , "You don’t get free, and you can’t attempt to Escape again until your next turn."
                      , None
                      , "You get free and remove the grabbed, immobilized, and restrained conditions imposed by your "
                        "chosen target. "
                      , "You get free and remove the grabbed, immobilized, and restrained conditions imposed by your "
                        "chosen target. You can then Stride up to 5 feet. "
                      , None
                      , None)

actionINTERACT = Action("Interact"
                        , "You use your hand or hands to manipulate an object or the terrain. You can grab an "
                          "unattended or stored object, open a door, or produce some similar effect. You might have "
                          "to attempt a skill check to determine if your Interact action was successful. "
                        , 1
                        , [traitMANIPULATE]
                        , None
                        , None
                        , None
                        , None
                        , None
                        , None)

actionLEAP = Action("Leap"
                    , "You take a careful, short jump. You can Leap up to 10 feet horizontally if your Speed is at "
                      "least 15 feet, or up to 15 feet horizontally if your Speed is at least 30 feet. You land in "
                      "the space where your Leap ends (meaning you can typically clear a 5-foot gap, or a 10-foot gap "
                      "if your Speed is 30 feet or more). If you Leap vertically, you can move up to 3 feet "
                      "vertically and 5 feet horizontally onto an elevated surface. Jumping a greater distance "
                      "requires using the Athletics skill. "
                    , 1
                    , [traitMOVE]
                    , None
                    , None
                    , None
                    , None
                    , None
                    , None)

actionREADY = Action("Ready"
                     , "You prepare to use an action that will occur outside your turn. Choose a single action or free "
                       "action you can use, and designate a trigger. Your turn ends. If the trigger you designated "
                       "occurs before the start of your next turn, you can use the chosen action as a reaction ("
                       "provided you still meet the requirements to use it). You can’t Ready a free action that "
                       "already has a trigger. If you have a multiple attack penalty and your readied action is an "
                       "attack action, your readied attack takes the multiple attack penalty you had at the time you "
                       "used Ready. This is one of the few times the multiple attack penalty applies when it’s not "
                       "your turn. "
                     , 2
                     , [traitCONCENTRATE]
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None)

actionRELEASE = Action("Release"
                       , "You release something you're holding in your hand or hands. This might mean dropping an "
                         "item, removing one hand from your weapon while continuing to hold it in another hand, "
                         "releasing a rope suspending a chandelier, or performing a similar action. Unlike most "
                         "manipulate actions, Release does not trigger reactions that can be triggered by actions "
                         "with the manipulate trait (such as Attack of Opportunity). If you want to prepare to "
                         "Release something outside of your turn, use the Ready activity. "
                       , 0
                       , [traitMANIPULATE]
                       , None
                       , None
                       , None
                       , None
                       , None
                       , None)

actionSEEK = Action("Seek"
                    , "You scan an area for signs of creatures or objects. If you're looking for creatures, choose an "
                      "area you're scanning. If precision is necessary, the GM can have you select a 30-foot cone or "
                      "a 15-foot burst within line of sight. You might take a penalty if you choose an area that's "
                      "far away. If you're using Seek to search for objects (including secret doors and hazards), "
                      "you search up to a 10-foot square adjacent to you. The GM might determine you need to Seek as "
                      "an activity, taking more actions or even minutes or hours if you're searching a particularly "
                      "cluttered area. The GM attempts a single secret Perception check for you and compares the "
                      "result to the Stealth DCs of any undetected or hidden creatures in the area or the DC to "
                      "detect each object in the area (as determined by the GM or by someone Concealing the Object). "
                      "A creature you detect might remain hidden, rather than becoming observed, if you're using an "
                      "imprecise sense or if an effect (such as invisibility) prevents the subject from being "
                      "observed. "
                    , 1
                    , [traitCONCENTRATE, traitSECRET]
                    , None
                    , None
                    , "If you were searching for creatures, any undetected creature you succeeded against becomes "
                      "hidden from you instead of undetected, and any hidden creature you succeeded against becomes "
                      "observed by you. If you were searching for an object, you learn its location or get a clue to "
                      "its whereabouts, as determined by the GM. "
                    , "If you were searching for creatures, any undetected or hidden creature you critically "
                      "succeeded against becomes observed by you. If you were searching for an object, you learn its "
                      "location. "
                    , None
                    , None)

actionSENSEMOTIVE = Action("Sense Motive"
                           , "You try to tell whether a creature's behavior is abnormal. Choose one creature, "
                             "and assess it for odd body language, signs of nervousness, and other indicators that it "
                             "might be trying to deceive someone. The GM attempts a single secret Perception check "
                             "for you and compares the result to the Deception DC of the creature, the DC of a spell "
                             "affecting the creature's mental state, or another appropriate DC determined by the GM. "
                             "You typically can't try to Sense the Motive of the same creature again until the "
                             "situation changes significantly. "
                           , 1
                           , [traitCONCENTRATE, traitSECRET]
                           , "You get a false sense of the creature’s intentions."
                           , "You detect what a deceptive creature wants you to believe. If they’re not being "
                             "deceptive, you believe they’re behaving normally. "
                           , "You can tell whether the creature is behaving normally, but you don’t know its exact "
                             "intentions or what magic might be affecting it. "
                           , "You determine the creature’s true intentions and get a solid idea of any mental magic "
                             "affecting it. "
                           , None
                           , None)

actionSTAND = Action("Stand"
                     , "You stand up from prone."
                     , 1
                     , [traitMOVE]
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None)

actionSTEP = Action("Step"
                    , "You carefully move 5 feet. Unlike most types of movement, Stepping doesn't trigger reactions, "
                      "such as Attacks of Opportunity, that can be triggered by move actions or upon leaving or "
                      "entering a square. You can't Step into difficult terrain, and you can't Step using a Speed "
                      "other than your land Speed. "
                    , 1
                    , [traitMOVE]
                    , None
                    , None
                    , None
                    , None
                    , "Your Speed is at least 10 feet."
                    , None)

actionSTRIDE = Action("Stride"
                      , "You move up to your Speed."
                      , 1
                      , [traitMOVE]
                      , None
                      , None
                      , None
                      , None
                      , None
                      , None)

actionSTRIKE = Action("Strike"
                      , "You attack with a weapon you're wielding or with an unarmed attack, targeting one creature "
                        "within your reach (for a melee attack) or within range (for a ranged attack). Roll the attack "
                        "roll for the weapon or unarmed attack you are using, and compare the result to the target "
                        "creature's AC to determine the effect. See Attack Rolls and Damage for details on calculating "
                        "your attack and damage rolls. "
                      , 1
                      , [traitATTACK]
                      , None
                      , None
                      , "You deal damage according to the weapon or unarmed attack, including any modifiers, bonuses, "
                        "and penalties you have to damage. "
                      , "As success, but you deal double damage."
                      , None
                      , None)

actionTAKECOVER = Action("Take Cover"
                         , "You press yourself against a wall or duck behind an obstacle to take better advantage of "
                           "cover. If you would have standard cover, you instead gain greater cover, which provides a "
                           "+4 circumstance bonus to AC; to Reflex saves against area effects; and to Stealth checks "
                           "to Hide, Sneak, or otherwise avoid detection. Otherwise, you gain the benefits of "
                           "standard cover (a +2 circumstance bonus instead). This lasts until you move from your "
                           "current space, use an attack action, become unconscious, or end this effect as a free "
                           "action. "
                         , 1
                         , []
                         , None
                         , None
                         , None
                         , None
                         , "You are benefiting from cover, are near a feature that allows you to take cover, "
                           "or are prone. "
                         , None)

actionsBASIC = [[copy.deepcopy(actionAID), "Basic"], [copy.deepcopy(actionCRAWL), "Basic"],
                [copy.deepcopy(actionDELAY), "Basic"], [copy.deepcopy(actionDROPPRONE), "Basic"],
                [copy.deepcopy(actionESCAPE), "Basic"], [copy.deepcopy(actionINTERACT), "Basic"],
                [copy.deepcopy(actionLEAP), "Basic"], [copy.deepcopy(actionREADY), "Basic"],
                [copy.deepcopy(actionRELEASE), "Basic"], [copy.deepcopy(actionSEEK), "Basic"],
                [copy.deepcopy(actionSENSEMOTIVE), "Basic"], [copy.deepcopy(actionSTAND), "Basic"],
                [copy.deepcopy(actionSTEP), "Basic"], [copy.deepcopy(actionSTRIDE), "Basic"],
                [copy.deepcopy(actionSTRIKE), "Basic"], [copy.deepcopy(actionTAKECOVER), "Basic"]]

# specialty basic
actionAVERTGAZE = Action("Avert gaze"
                         , "You avert your gaze from danger. You gain a +2 circumstance bonus to saves against visual "
                           "abilities that require you to look at a creature or object, such as a medusa's petrifying "
                           "gaze. Your gaze remains averted until the start of your next turn. "
                         , 1
                         , []
                         , None
                         , None
                         , None
                         , None
                         , None
                         , None)

actionDISMISS = Action("Dismiss"
                       , "You end one spell effect or magic item effect. This must be an effect you are allowed to "
                         "dismiss, as defined by the spell or item. Dismissal might end the effect entirely or might "
                         "end it just for a certain target or targets, depending on the spell or item. "
                       , 1
                       , [traitCONCENTRATE]
                       , "Encounter"
                       , None
                       , None
                       , None
                       , None
                       , None
                       , None)

actionGRABANEDGE = Action("Grab an Edge"
                          , "When you fall off or past an edge or other handhold, you can try to grab it, potentially "
                            "stopping your fall. You must succeed at a Reflex save, usually at the Climb DC. If you "
                            "grab the edge or handhold, you can then Climb up using Athletics. "
                          , -1
                          , [traitMANIPULATE]
                          , "You continue to fall, and if you’ve fallen 20 feet or more before you use this reaction, "
                            "you take 10 bludgeoning damage from the impact for every 20 feet fallen. "
                          , None
                          , "If you have at least one hand free, you grab the edge or handhold, stopping your fall. "
                            "You still take damage from the distance fallen so far, but you treat the fall as though "
                            "it were 20 feet shorter. If you have no hands free, you continue to fall as if you had "
                            "failed the check "
                          , "You grab the edge or handhold, whether or not you have a hand free, typically by using a "
                            "suitable held item to catch yourself (catching a battle axe on a ledge, for example). "
                            "You still take damage from the distance fallen so far, but you treat the fall as though "
                            "it were 30 feet shorter. "
                          , "Your hands are not tied behind your back or otherwise restrained"
                          , "You fall from or past an edge or handhold.")

actionMOUNT = Action("Mount"
                     , "You move onto the creature and ride it. If you’re already mounted, you can instead use this "
                       "action to dismount, moving off the mount into a space adjacent to it. "
                     , 1
                     , [traitMOVE]
                     , None
                     , None
                     , None
                     , None
                     , "You are adjacent to a creature that is at least one size larger than you and is willing to be "
                       "your mount. "
                     , None)

actionPOINTOUT = Action("Point Out"
                        , "You indicate a creature that you can see to one or more allies, gesturing in a direction "
                          "and describing the distance verbally. That creature is hidden to your allies, rather than "
                          "undetected. This works only for allies who can see you and are in a position where they "
                          "could potentially detect the target. If your allies can't hear or understand you, "
                          "they must succeed at a Perception check against the creature's Stealth DC or they "
                          "misunderstand and believe the target is in a different location. "
                        , 1
                        , [traitAUDITORY, traitMANIPULATE, traitVISUAL]
                        , None
                        , None
                        , None
                        , None
                        , "A creature is undetected by one or more of your allies but isn’t undetected by you."
                        , None)

actionRAISESHIELD = Action("Raise a Shield"
                           , "You position your shield to protect yourself. When you have Raised a Shield, you gain "
                             "its listed circumstance bonus to AC. Your shield remains raised until the start of your "
                             "next turn. "
                           , 1
                           , []
                           , None
                           , None
                           , None
                           , None
                           , "You are wielding a shield."
                           , None)

actionsSPECIAL = [[copy.deepcopy(actionAVERTGAZE), "Special"], [copy.deepcopy(actionDISMISS), "Special"],
                  [copy.deepcopy(actionGRABANEDGE), "Special"], [copy.deepcopy(actionMOUNT), "Special"],
                  [copy.deepcopy(actionPOINTOUT), "Special"], [copy.deepcopy(actionRAISESHIELD), "Special"]]

# class actions
# Barbarian
actionRAGE = Action("Rage"
                    , "You tap into your inner fury and begin raging. You gain a number of temporary Hit Points equal "
                      "to your level plus your Constitution modifier. This frenzy lasts for 1 minute, until there are "
                      "no enemies you can perceive, or until you fall unconscious, whichever comes first. You can't "
                      "voluntarily stop raging. While you are raging:\nYou deal 2 additional damage with melee "
                      "Strikes. This additional damage is halved if your weapon or unarmed attack is agile.\nYou take "
                      "a –1 penalty to AC.\nYou can't use actions with the concentrate trait unless they also have "
                      "the rage trait. You can Seek while raging.\nAfter you stop raging, you lose any remaining "
                      "temporary Hit Points from Rage, and you can't Rage again for 1 minute. "
                    , 1
                    , [traitBARBARIAN, traitCONCENTRATE, traitEMOTION, traitMENTAL]
                    , None
                    , None
                    , None
                    , None
                    , "You aren’t fatigued or raging."
                    , None)

# Fighter
actionATTACKOPPORTUNITY = Action("Attack of Opportunity"
                                 , "You lash out at a foe that leaves an opening. Make a melee Strike against the "
                                   "triggering creature. If your attack is a critical hit and the trigger was a "
                                   "manipulate action, you disrupt that action. This Strike doesn't count toward your "
                                   "multiple attack penalty, and your multiple attack penalty doesn't apply to this "
                                   "Strike."
                                 , -1
                                 , []
                                 , None
                                 , None
                                 , None
                                 , None
                                 , None
                                 , "A creature within your reach uses a manipulate action or a move action, makes a "
                                   "ranged attack, or leaves a square during a move action it’s using.")

# Ranger
actionHUNTPREY = Action("Hunt Prey"
                        , "You designate a single creature as your prey and focus your attacks against that creature. "
                          "You must be able to see or hear the prey, or you must be tracking the prey during "
                          "exploration.\nYou gain a +2 circumstance bonus to Perception checks when you Seek your "
                          "prey and a +2 circumstance bonus to Survival checks when you Track your prey. You also "
                          "ignore the penalty for making ranged attacks within your second range increment against "
                          "the prey you’re hunting.\nYou can have only one creature designated as your prey at a "
                          "time. If you use Hunt Prey against a creature when you already have a creature designated, "
                          "the prior creature loses the designation and the new prey gains the designation. Your "
                          "designation lasts until your next daily preparations. "
                        , 1
                        , [traitCONCENTRATE, traitRANGER]
                        , None
                        , None
                        , None
                        , None
                        , None
                        , None)

# Feat Actions
# Double Slice
actionDOUBLESLICE = Action("Double Slice"
                           , "You lash out at your foe with both weapons. Make two Strikes, one with each of your two "
                             "melee weapons, each using your current multiple attack penalty. Both Strikes must have "
                             "the same target. If the second Strike is made with a weapon that doesn't have the agile "
                             "trait, it takes a –2 penalty.\nIf both attacks hit, combine their damage, and then add "
                             "any other applicable effects from both weapons. You add any precision damage only once, "
                             "to the attack of your choice. Combine the damage from both Strikes and apply "
                             "resistances and weaknesses only once. This counts as two attacks when calculating your "
                             "multiple attack penalty. "
                           , 2
                           , [traitATTACK, traitFIGHTER]
                           , None
                           , None
                           , None
                           , None
                           , "You are wielding two melee weapons, each in a different hand."
                           , None)

# Exacting Strike
actionEXACTINGSTRIKE = Action("Exacting Strike"
                              , "You attack with a weapon you're wielding or with an unarmed attack, targeting one "
                                "creature within your reach (for a melee attack) or within range (for a ranged "
                                "attack). Roll the attack roll for the weapon or unarmed attack you are using, "
                                "and compare the result to the target creature's AC to determine the effect. See "
                                "Attack Rolls and Damage for details on calculating your attack and damage rolls. "
                              , 1
                              , [traitATTACK]
                              , None
                              , "This attack does not count toward your multiple attack penalty."
                              , "You deal damage according to the weapon or unarmed attack, including any modifiers, "
                                "bonuses, and penalties you have to damage. "
                              , "As success, but you deal double damage."
                              , None
                              , None)

# Hunted Shot
actionHUNTEDSHOT = Action("Hunted Shot"
                          , "You take two quick shots against the one you hunt. Make two Strikes against your prey "
                            "with the required weapon. If both hit the same creature, combine their damage for the "
                            "purpose of resistances and weaknesses. Apply your multiple attack penalty to each Strike "
                            "normally. "
                          , 1
                          , [traitFLOURISH, traitRANGER]
                          , None
                          , None
                          , None
                          , None
                          , "You are wielding a ranged weapon with reload 0."
                          , None)
actionHUNTEDSHOT.frequency = "Once per round"

# p2TODO: get this to modify recall knowledge
# monster hunter
actionHUNTPREY_MH = Action("Hunt Prey: Free Recall"
                           , "You swiftly assess your prey and apply what you know. As part of the action used to "
                             "Hunt your Prey, you can attempt a check to Recall Knowledge about your prey. When you "
                             "critically succeed at identifying your hunted prey with Recall Knowledge, you note a "
                             "weakness in the creature’s defenses. You and allies you tell gain a +1 circumstance "
                             "bonus to your next attack roll against that prey. You can give bonuses from Monster "
                             "Hunter only once per day against a particular creature. "
                           , 0
                           , [traitRANGER]
                           , None
                           , None
                           , None
                           , None
                           , None
                           , None)

# Nimble Dodge
actionNIMBLEDODGE = Action("Nimble Dodge"
                           , "You deftly dodge out of the way, gaining a +2 circumstance bonus to AC against the "
                             "triggering attack. "
                           , -1
                           , [traitROGUE, traitSWASHBUCKLER]
                           , None
                           , None
                           , None
                           , None
                           , "You are not encumbered."
                           , "A creature targets you with an attack and you can see the attacker.")

# orc ferocity
actionORCFEROCITY = Action("Orc Ferocity"
                           , "Fierceness in battle runs through your blood, and you refuse to fall from your "
                             "injuries. You avoid being knocked out and remain at 1 Hit Point, and your wounded "
                             "condition increases by 1. "
                           , -1
                           , [traitORC]
                           , None
                           , None
                           , None
                           , None
                           , None
                           , "You would be reduced to 0 Hit Points but not immediately killed.")
actionORCFEROCITY.frequency = "Once per day"

# Reactive Shield
actionREACTIVESHIELD = Action("Reactive Shield"
                              , "You can snap your shield into place just as you would take a blow, avoiding the hit "
                                "at the last second. You immediately use the Raise a Shield action and gain your "
                                "shield’s bonus to AC. The circumstance bonus from the shield applies to your AC when "
                                "you’re determining the outcome of the triggering attack. "
                              , -1
                              , [traitFIGHTER]
                              , None
                              , None
                              , None
                              , None
                              , "You are wielding a shield."
                              , "An enemy hits you with a melee Strike.")

# Shield Block
actionSHIELDBLOCK = Action("Shield Block"
                           , "You snap your shield in place to ward off a blow. Your shield prevents you from taking "
                             "an amount of damage up to the shield’s Hardness. You and the shield each take any "
                             "remaining damage, possibly breaking or destroying the shield. "
                           , -1
                           , [traitGENERAL]
                           , None
                           , None
                           , None
                           , None
                           , None
                           , "While you have your shield raised, you would take damage from a physical attack.")

action = Action(""
                , ""
                , 1
                , []
                , None
                , None
                , None
                , None
                , None
                , None)
