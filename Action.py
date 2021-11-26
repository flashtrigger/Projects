from Trait import *


# 306 - Specialty Basic
class Action:

    def __init__(self, *args):
        """

        :rtype: object
        """
        self.name = args[0]
        self.numActions = args[1]  # integer, -1 = reaction, 0 = free
        self.description = args[2]
        self.traits = args[3]  # list of Traits
        self.type = args[4]  # encounter/exploration
        self.critFail = args[5]
        self.fail = args[6]
        self.success = args[7]
        self.critSuccess = args[8]
        self.requirements = args[9]
        self.trigger = args[10]


# basic actions
actionAID = Action("Aid"
                   , -1
                   , "You try to help your ally with a task. To use this reaction, you must first prepare to "
                     "help, usually by using an action during your turn. You must explain to the GM exactly "
                     "how you’re trying to help, and they determine whether you can Aid your ally. When you "
                     "use your Aid reaction, attempt a skill check or attack roll of a type decided by the "
                     "GM. The typical DC is 20, but the GM might adjust this DC for particularly hard or "
                     "easy tasks. The GM can add any relevant traits to your preparatory action or to your "
                     "Aid reaction depending on the situation, or even allow you to Aid checks other than "
                     "skill checks and attack rolls."
                   , []
                   , "Encounter"
                   , "Your ally takes a –1 circumstance penalty to the triggering check."
                   , None
                   , "You grant your ally a +1 circumstance bonus to the triggering check."
                   , "You grant your ally a +2 circumstance bonus to the triggering check. If you’re a master with "
                     "the check you attempted, the bonus is +3, and if you’re legendary, it’s +4."
                   , "The ally is willing to accept your aid, and you have prepared to help"
                   , "An ally is about to use an action that requires a skill check or attack roll.")

actionCRAWL = Action("Crawl"
                     , 1
                     , "You move 5 feet by crawling and continue to stay prone."
                     , [traitMOVE]
                     , "Encounter"
                     , None
                     , None
                     , None
                     , None
                     , "You are prone and your Speed is at least 10 feet."
                     , None)

actionDELAY = Action("Delay"
                     , 0
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
                     , []
                     , "Encounter"
                     , None
                     , None
                     , None
                     , None
                     , None
                     , "Your turn begins.")

actionDROPPRONE = Action("Drop Prone"
                         , 1
                         , "You fall prone."
                         , [traitMOVE]
                         , "Encounter"
                         , None
                         , None
                         , None
                         , None
                         , None
                         , None)

actionESCAPE = Action("Escape"
                      , 1
                      , "You attempt to escape from being grabbed, immobilized, or restrained. Choose one creature, "
                        "object, spell effect, hazard, or other impediment imposing any of those conditions on you. "
                        "Attempt a check using your unarmed attack modifier against the DC of the effect. This is "
                        "typically the Athletics DC of a creature grabbing you, the Thievery DC of a creature who tied "
                        "you up, the spell DC for a spell effect, or the listed Escape DC of an object, hazard, "
                        "or other impediment. You can attempt an Acrobatics or Athletics check instead of using your "
                        "attack modifier if you choose (but this action still has the attack trait). "
                      , [traitATTACK]
                      , "Encounter"
                      , "You don’t get free, and you can’t attempt to Escape again until your next turn."
                      , None
                      , "You get free and remove the grabbed, immobilized, and restrained conditions imposed by your "
                        "chosen target. "
                      , "You get free and remove the grabbed, immobilized, and restrained conditions imposed by your "
                        "chosen target. You can then Stride up to 5 feet. "
                      , None
                      , None)

actionINTERACT = Action("Interact"
                        , 1
                        , "You use your hand or hands to manipulate an object or the terrain. You can grab an "
                          "unattended or stored object, open a door, or produce some similar effect. You might have "
                          "to attempt a skill check to determine if your Interact action was successful. "
                        , [traitMANIPULATE]
                        , "Encounter"
                        , None
                        , None
                        , None
                        , None
                        , None
                        , None)

actionLEAP = Action("Leap"
                    , 1
                    ,
                    "You take a careful, short jump. You can Leap up to 10 feet horizontally if your Speed is at least "
                    "15 feet, or up to 15 feet horizontally if your Speed is at least 30 feet. You land in the space "
                    "where your Leap ends (meaning you can typically clear a 5-foot gap, or a 10-foot gap if your Speed"
                    " is 30 feet or more). If you Leap vertically, you can move up to 3 feet vertically and 5 feet "
                    "horizontally onto an elevated surface. Jumping a greater distance requires using the Athletics "
                    "skill. "
                    , [traitMOVE]
                    , "Encounter"
                    , None
                    , None
                    , None
                    , None
                    , None
                    , None)

actionREADY = Action("Ready"
                     , 2
                     , "You prepare to use an action that will occur outside your turn. Choose a single action or free "
                       "action you can use, and designate a trigger. Your turn ends. If the trigger you designated "
                       "occurs before the start of your next turn, you can use the chosen action as a reaction ("
                       "provided you still meet the requirements to use it). You can’t Ready a free action that "
                       "already has a trigger. If you have a multiple attack penalty and your readied action is an "
                       "attack action, your readied attack takes the multiple attack penalty you had at the time you "
                       "used Ready. This is one of the few times the multiple attack penalty applies when it’s not "
                       "your turn. "
                     , [traitCONCENTRATE]
                     , "Encounter"
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None)

actionRELEASE = Action("Release"
                       , 0
                       ,
                       "You release something you're holding in your hand or hands. This might mean dropping an item, "
                       "removing one hand from your weapon while continuing to hold it in another hand, releasing a "
                       "rope suspending a chandelier, or performing a similar action. Unlike most manipulate actions, "
                       "Release does not trigger reactions that can be triggered by actions with the manipulate trait "
                       "(such as Attack of Opportunity). If you want to prepare to Release something outside of your "
                       "turn, use the Ready activity. "
                       , [traitMANIPULATE]
                       , "Encounter"
                       , None
                       , None
                       , None
                       , None
                       , None
                       , None)

actionSEEK = Action("Seek"
                    , 1
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
                    , [traitCONCENTRATE, traitSECRET]
                    , "Encounter"
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
                           , 1
                           , "You try to tell whether a creature's behavior is abnormal. Choose one creature, "
                             "and assess it for odd body language, signs of nervousness, and other indicators that it "
                             "might be trying to deceive someone. The GM attempts a single secret Perception check "
                             "for you and compares the result to the Deception DC of the creature, the DC of a spell "
                             "affecting the creature's mental state, or another appropriate DC determined by the GM. "
                             "You typically can't try to Sense the Motive of the same creature again until the "
                             "situation changes significantly. "
                           , [traitCONCENTRATE, traitSECRET]
                           , "Encounter"
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
                     , 1
                     , ""
                     , [traitMOVE]
                     , "You stand up from prone."
                     , None
                     , None
                     , None
                     , None
                     , None
                     , None)

actionSTEP = Action("Step"
                    , 1
                    , "You carefully move 5 feet. Unlike most types of movement, Stepping doesn't trigger reactions, "
                      "such as Attacks of Opportunity, that can be triggered by move actions or upon leaving or "
                      "entering a square. You can't Step into difficult terrain, and you can't Step using a Speed "
                      "other than your land Speed. "
                    , [traitMOVE]
                    , "Encounter"
                    , None
                    , None
                    , None
                    , None
                    , "Your Speed is at least 10 feet."
                    , None)

actionSTRIDE = Action("Stride"
                      , 1
                      , "You move up to your Speed."
                      , [traitMOVE]
                      , "Encounter"
                      , None
                      , None
                      , None
                      , None
                      , None
                      , None)

actionSTRIKE = Action("Strike"
                      , 1
                      ,
                      "You attack with a weapon you're wielding or with an unarmed attack, targeting one creature "
                      "within your reach (for a melee attack) or within range (for a ranged attack). Roll the attack "
                      "roll for the weapon or unarmed attack you are using, and compare the result to the target "
                      "creature's AC to determine the effect. See Attack Rolls and Damage for details on calculating "
                      "your attack and damage rolls. "
                      , [traitATTACK]
                      , "Encounter"
                      , None
                      , None
                      , "You deal damage according to the weapon or unarmed attack, including any modifiers, bonuses, "
                        "and penalties you have to damage. "
                      , "As success, but you deal double damage."
                      , None
                      , None)

actionTAKECOVER = Action("Take Cover"
                         , 1
                         , "You press yourself against a wall or duck behind an obstacle to take better advantage of "
                           "cover. If you would have standard cover, you instead gain greater cover, which provides a "
                           "+4 circumstance bonus to AC; to Reflex saves against area effects; and to Stealth checks "
                           "to Hide, Sneak, or otherwise avoid detection. Otherwise, you gain the benefits of "
                           "standard cover (a +2 circumstance bonus instead). This lasts until you move from your "
                           "current space, use an attack action, become unconscious, or end this effect as a free "
                           "action. "
                         , []
                         , "Encounter"
                         , None
                         , None
                         , None
                         , None
                         , "You are benefiting from cover, are near a feature that allows you to take cover, "
                           "or are prone. "
                         , None)

# specialty basic
actionAVERTGAZE = Action("Avert gaze"
                         , 1
                         , "You avert your gaze from danger. You gain a +2 circumstance bonus to saves against visual "
                           "abilities that require you to look at a creature or object, such as a medusa's petrifying "
                           "gaze. Your gaze remains averted until the start of your next turn. "
                         , []
                         , "Encounter "
                         , None
                         , None
                         , None
                         , None
                         , None
                         , None)

actionDISMISS = Action("Dismiss"
                       , 1
                       , "You end one spell effect or magic item effect. This must be an effect you are allowed to "
                         "dismiss, as defined by the spell or item. Dismissal might end the effect entirely or might "
                         "end it just for a certain target or targets, depending on the spell or item. "
                       , [traitCONCENTRATE]
                       , "Encounter"
                       , None
                       , None
                       , None
                       , None
                       , None
                       , None)

actionGRABANEDGE = Action("Grab an Edge"
                          , -1
                          , "When you fall off or past an edge or other handhold, you can try to grab it, potentially "
                            "stopping your fall. You must succeed at a Reflex save, usually at the Climb DC. If you "
                            "grab the edge or handhold, you can then Climb up using Athletics. "
                          , [traitMANIPULATE]
                          , "Encounter"
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
                     , 1
                     , "You move onto the creature and ride it. If you’re already mounted, you can instead use this "
                       "action to dismount, moving off the mount into a space adjacent to it. "
                     , [traitMOVE]
                     , "Encounter"
                     , None
                     , None
                     , None
                     , None
                     , "You are adjacent to a creature that is at least one size larger than you and is willing to be "
                       "your mount. "
                     , None)

actionPOINTOUT = Action("Point Out"
                        , 1
                        , "You indicate a creature that you can see to one or more allies, gesturing in a direction "
                          "and describing the distance verbally. That creature is hidden to your allies, rather than "
                          "undetected. This works only for allies who can see you and are in a position where they "
                          "could potentially detect the target. If your allies can't hear or understand you, "
                          "they must succeed at a Perception check against the creature's Stealth DC or they "
                          "misunderstand and believe the target is in a different location. "
                        , [traitAUDITORY, traitMANIPULATE, traitVISUAL]
                        , "Encounter"
                        , None
                        , None
                        , None
                        , None
                        , "A creature is undetected by one or more of your allies but isn’t undetected by you."
                        , None)

action = Action(""
                , 1
                , ""
                , []
                , "Encounter"
                , None
                , None
                , None
                , None
                , None
                , None)
