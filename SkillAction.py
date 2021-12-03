from Action import Action
from Trait import *


class SkillAction(Action):  # DONE Phase 1!

    def __init__(self, *args):
        Action.__init__(self, *args)
        self.untrained = args[10]
        self.trained = args[11]
        self.expert = args[12]
        self.master = args[13]
        self.legendary = args[14]
        self.isTrained = args[15]  # boolean


# acrobatics
actionBALANCE = SkillAction("Balance"
                            , "You move across a narrow surface or uneven ground, attempting an Acrobatics check "
                            "against its Balance DC. You are flat-footed while on a narrow surface or uneven ground. "
                            , 1
                            , [traitMOVE]
                            , "You fall and your turn ends."
                            , "You must remain stationary to keep your balance (wasting the action) or you fall. If you"
                            " fall, your turn ends. "
                            , "You move up to your Speed, treating it as difficult terrain (every 5 feet costs 10 feet "
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

# Acrobatics
actionTUMBLETHROUGH = SkillAction("Tumble Through"
                                  , "You Stride up to your Speed. During this movement, you can try to move through the"
                                  " space of one enemy. Attempt an Acrobatics check against the enemy’s Reflex DC as "
                                  "soon as you try to enter its space. You can Tumble Through using Climb, Fly, Swim, "
                                  "or another action instead of Stride in the appropriate environment. "
                                  , 1
                                  , [traitMOVE]
                                  , None
                                  , "Failure Your movement ends, and you trigger reactions as if you had moved out of "
                                  "the square you started in. "
                                  , "You move through the enemy’s space, treating the squares in its space as difficult"
                                  " terrain (every 5 feet costs 10 feet of movement). If you don’t have enough Speed "
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

# Acrobatics
actionMANEUVERINFLIGHT = SkillAction("Maneuver in Flight"
                                     , "You try a difficult maneuver while flying. Attempt an Acrobatics check. The GM "
                                     "determines what maneuvers are possible, but they rarely allow you to move "
                                     "farther than your fly Speed. "
                                     , 1
                                     , [traitMOVE]
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

# Arcana, Crafting, Lore, Medicine, Nature, Occultism, Religion, Society
actionRECALLKNOWLEDGE = SkillAction("Recall Knowledge"
                                    , "You attempt a skill check to try to remember a bit of knowledge regarding a "
                                      "topic related to that skill. The GM determines the DCs for such checks and which"
                                      " skills apply. "
                                    , 1
                                    , [traitCONCENTRATE, traitSECRET]
                                    , "You recall incorrect information or gain an erroneous or misleading clue. "
                                    , None
                                    , "You recall the knowledge accurately or gain a useful clue about your current "
                                      "situation. "
                                    , "You recall the knowledge accurately and gain additional information or context"
                                    , None
                                    , None
                                    , "Name of a ruler, key noble, or major deity"
                                    , "Line of succession for a major noble family, core doctrines of a major deity"
                                    , "Genealogy of a minor noble, teachings of an ancient priest"
                                    , "Hierarchy of a genie noble court, major extraplanar temples of a deity"
                                    , "Existence of a long-lost noble heir, secret doctrines of a religion"
                                    , False)

# Acrobatics
activitySQUEEZE = SkillAction("Squeeze"
                              , "You contort yourself to squeeze through a space so small you can barely fit through. "
                              "This action is for exceptionally small spaces; many tight spaces are difficult terrain "
                              "that you can move through more quickly and without a check. "
                              , None
                              , [traitEXPLORATION, traitMOVE]
                              , "You become stuck in the tight space. While you’re stuck, you can spend 1 minute "
                              "attempting another Acrobatics check at the same DC. Any result on that check other "
                              "than a critical failure causes you to become unstuck. "
                              , None
                              , "You squeeze through in 1 minute per 5 feet."
                              , "You squeeze through the tight space in 1 minute per 10 feet of squeezing."
                              , None
                              , None
                              , None
                              , None
                              , None
                              , None
                              , None
                              , True)

# Arcana, Occultism, Religion, Society
activityDECIPHERWRITING = SkillAction("Decipher Writing"
                                      , "You attempt to decipher complicated writing or literature on an obscure topic."
                                      " This usually takes 1 minute per page of text, but might take longer (typically "
                                      "an hour per page for decrypting ciphers or the like). The text must be in a "
                                      "language you can read, though the GM might allow you to attempt to decipher "
                                      "text written in an unfamiliar language using Society instead. The DC is "
                                      "determined by the GM based on the state or complexity of the document. The GM "
                                      "might have you roll one check for a short text or a check for each section of "
                                      "a larger text. "
                                      , None
                                      , [traitCONCENTRATE, traitEXPLORATION, traitSECRET]
                                      , "You believe you understand the text on that page, but you have in fact "
                                      "misconstrued its message. "
                                      , "You can’t understand the text and take a –2 circumstance penalty to further "
                                      "checks to decipher it. "
                                      , "You understand the true meaning of the text. If it was a coded document, "
                                      "you know the general meaning but might not have a word-for-word translation. "
                                      , "You understand the true meaning of the text."
                                      , None
                                      , None
                                      , None
                                      , "Entry-level philosophy treatise"
                                      , "Complex code, such as a cipher"
                                      , "Spymaster’s code or advanced research notes"
                                      , "Esoteric planar text written in metaphor by an ancient celestial"
                                      , True)

# Arcana, Nature, Occultism, religion
activityIDENTIFYMAGIC = SkillAction("Identify Magic"
                                    , "Once you discover that an item, location, or ongoing effect is magical, you can "
                                    "spend 10 minutes to try to identify the particulars of its magic. If your "
                                    "attempt is interrupted, you must start over. The GM sets the DC for your check. "
                                    "Cursed or esoteric subjects usually have higher DCs or might even be impossible "
                                    "to identify using this activity alone. Heightening a spell doesn't increase the "
                                    "DC to identify it. "
                                    , None
                                    , [traitCONCENTRATE, traitEXPLORATION, traitSECRET]
                                    , "You misidentify the magic as something else of the GM’s choice."
                                    , "You fail to identify the magic and can’t try again for 1 day."
                                    , "For an item or location, you get a sense of what it does and learn any means of "
                                    "activating it. For an ongoing effect (such as a spell with a duration), "
                                    "you learn the effect’s name and what it does. You can’t try again in hopes of "
                                    "getting a critical success. "
                                    , "You learn all the attributes of the magic, including its name (for an effect), "
                                    "what it does, any means of activating it (for an item or location), and whether "
                                    "it is cursed. "
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , True)

# Arcana, Nature, Occultism, religion
activityLEARNASPELL = SkillAction("Learn a Spell"
                                  , "You can gain access to a new spell of your tradition from someone who knows that "
                                    "spell or from magical writing like a spellbook or scroll. If you can cast spells "
                                    "of multiple traditions, you can Learn a Spell of any of those traditions, "
                                    "but you must use the corresponding skill to do so. To learn the spell, "
                                    "you must do the following:\nSpend 1 hour per level of the spell, during which "
                                    "you must remain in conversation with a person who knows the spell or have the "
                                    "magical writing in your possession.\nHave materials with the Price indicated in "
                                    "Table 4–3.\nAttempt a skill check for the skill corresponding to your tradition "
                                    "(DC determined by the GM, often close to the DC on Table 4–3). Uncommon or rare "
                                    "spells have higher DCs.\nIf you have a spellbook, Learning a Spell lets you add "
                                    "the spell to your spellbook; if you prepare spells from a list, it's added to "
                                    "your list; if you have a spell repertoire, you can select it when you add or "
                                    "swap spells. "
                                  , None
                                  , [traitCONCENTRATE, traitEXPLORATION]
                                  , "As failure, plus you expend half the materials."
                                  , "You fail to learn the spell but can try again after you gain a level. The "
                                    "materials aren't expended. "
                                  , "You expend the materials and learn the spell."
                                  , "You expend half the materials and learn the spell."
                                  , "You have a spellcasting class feature, and the spell you want to learn is on "
                                    "your magical tradition’s spell list. "
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , True)

# Arcane
activityBORROWARCANE = SkillAction("Borrow an Arcane Spell"
                                   , "You can attempt to prepare a spell from someone else’s spellbook. The GM sets "
                                     "the DC for the check based on the spell’s level and rarity; it’s typically a "
                                     "bit easier than Learning the Spell. "
                                   , None
                                   , [traitCONCENTRATE, traitEXPLORATION]
                                   , None
                                   , "You fail to prepare the spell, but the spell slot remains available for you to "
                                     "prepare a different spell. You can’t try to prepare this spell until the next "
                                     "time you prepare spells. "
                                   , "You prepare the borrowed spell as part of your normal spell preparation."
                                   , None
                                   , "You’re an arcane spellcaster who prepares from a spellbook"
                                   , None
                                   , None
                                   , None
                                   , None
                                   , None
                                   , None
                                   , True)

# Athletics
actionCLIMB = SkillAction("Climb"
                          , "You move up, down, or across an incline. Unless it’s particularly easy, you must attempt "
                            "an Athletics check. The GM determines the DC based on the nature of the incline and "
                            "environmental circumstances. You’re flat-footed unless you have a climb Speed. "
                          , 1
                          , [traitMOVE]
                          , "You fall. If you began the climb on stable ground, you fall and land prone."
                          , None
                          , "You move up, across, or safely down the incline for 5 feet per 20 feet of your land "
                            "Speed (a total of 5 feet for most PCs, minimum 5 feet if your Speed is below 20 feet). "
                          , "You move up, across, or safely down the incline for 5 feet plus 5 feet per 20 feet of "
                            "your land Speed (a total of 10 feet for most PCs). "
                          , "You have both hands free."
                          , None
                          , "Ladder, steep slope, low-branched tree"
                          , "Rigging, rope, typical tree"
                          , "Wall with small handholds and footholds"
                          , "Ceiling with handholds and footholds, rock wall"
                          , "Smooth surface"
                          , False)

# Athletics
actionFORCEOPEN = SkillAction("Force Open"
                              , "Using your body, a lever, or some other tool, you attempt to forcefully open a door, "
                                "window, container or heavy gate. With a high enough result, you can even smash "
                                "through walls. Without a crowbar, prying something open takes a –2 item penalty to "
                                "the Athletics check to Force Open. "
                              , 1
                              , [traitATTACK]
                              , "Your attempt jams the door, window, container, or gate shut, imposing a –2 "
                                "circumstance penalty on future attempts to Force it Open. "
                              , None
                              , "You break the door, window, container, or gate open, and the door, window, "
                                "container, or gate gains the broken condition. If it’s especially sturdy, "
                                "the GM might have it take damage but not be broken. "
                              , "You open the door, window, container, or gate and can avoid damaging it in the "
                                "process. "
                              , None
                              , None
                              , "Fabric, flimsy glass"
                              , "Ice, sturdy glass"
                              , "Flimsy wooden door, wooden portcullis"
                              , "Sturdy wooden door, iron portcullis, metal bar"
                              , "Stone or iron door"
                              , False)

# Athletics
actionGRAPPLE = SkillAction("Grapple"
                            , "You attempt to grab a creature or object with your free hand. Attempt an Athletics "
                              "check against the target's Fortitude DC. You can Grapple a target you already have "
                              "grabbed or restrained without having a hand free. "
                            , 1
                            , [traitATTACK]
                            , "If you already had the target grabbed or restrained, it breaks free. Your target can "
                              "either grab you, as if it succeeded at using the Grapple action against you, "
                              "or force you to fall and land prone. "
                            , "You fail to grab your target. If you already had the target grabbed or restrained "
                              "using a Grapple, those conditions on that creature or object end. "
                            , "Your target is grabbed until the end of your next turn unless you move or your target "
                              "Escapes. "
                            , "Your target is restrained until the end of your next turn unless you move or your "
                              "target Escapes. "
                            , "You have at least one free hand or have your target grappled or restrained. Your "
                              "target isn't more than one size larger than you. "
                            , None
                            , None
                            , None
                            , None
                            , None
                            , None
                            , False)

# Athletics
actionHIGHJUMP = SkillAction("High Jump"
                             , "You Stride, then make a vertical Leap and attempt a DC 30 Athletics check to increase "
                               "the height of your jump. If you didn't Stride at least 10 feet, you automatically "
                               "fail your check. This DC might be increased or decreased due to the situation, "
                               "as determined by the GM. "
                             , 2
                             , [traitMOVE]
                             , "You don’t Leap at all, and instead you fall prone in your space."
                             , "You Leap normally."
                             , "Increase the maximum vertical distance to 5 feet."
                             , "Increase the maximum vertical distance to 8 feet, or increase the maximum vertical "
                               "distance to 5 feet and maximum horizontal distance to 10 feet. "
                             , None
                             , None
                             , None
                             , None
                             , None
                             , None
                             , None
                             , False)

# Athletics
actionLONGJUMP = SkillAction("Long Jump"
                             , "You Stride, then make a horizontal Leap and attempt an Athletics check to increase "
                               "the length of your jump. The DC of the Athletics check is equal to the total distance "
                               "in feet you’re attempting to move during your Leap (so you’d need to succeed at a DC "
                               "20 check to Leap 20 feet). You can’t Leap farther than your Speed. If you didn't "
                               "Stride at least 10 feet, or if you attempt to jump in a different direction than your "
                               "Stride, you automatically fail your check. This DC might be increased or decreased "
                               "due to the situation, as determined by the GM. "
                             , 2
                             , [traitMOVE]
                             , "You Leap normally, but then fall and land prone."
                             , "You Leap normally."
                             , "Increase the maximum horizontal distance you Leap to the desired distance."
                             , None
                             , None
                             , None
                             , None
                             , None
                             , None
                             , None
                             , None
                             , False)

# Athletics
actionSHOVE = SkillAction("Shove"
                          , "You push a creature away from you. Attempt an Athletics check against your target's "
                            "Fortitude DC. "
                          , 1
                          , [traitATTACK]
                          , "You lose your balance, fall, and land prone."
                          , None
                          , "You push your target back 5 feet. You can Stride after it, but you must move the same "
                            "distance and in the same direction. "
                          , "You push your target up to 10 feet away from you. You can Stride after it, but you must "
                            "move the same distance and in the same direction. "
                          , "You have at least one hand free. The target can’t be more than one size larger than you."
                          , None
                          , None
                          , None
                          , None
                          , None
                          , None
                          , False)

# Athletics
actionSWIM = SkillAction("Swim"
                         , "You propel yourself through water. In most calm water, you succeed at the action without "
                           "needing to attempt a check. If you must breathe air and you’re submerged in water, "
                           "you must hold your breath each round. If you fail to hold your breath, you begin to "
                           "drown. If the water you are swimming in is turbulent or otherwise dangerous, "
                           "you might have to attempt an Athletics check to Swim.\nIf you end your turn in water and "
                           "haven’t succeeded at a Swim action that turn, you sink 10 feet or get moved by the "
                           "current, as determined by the GM. However, if your last action on your turn was to enter "
                           "the water, you don’t sink or move with the current that turn. "
                         , 1
                         , [traitMOVE]
                         , "You make no progress, and if you’re holding your breath, you lose 1 round of air."
                         , None
                         , "You move through the water 5 feet, plus 5 feet per 20 feet of your land Speed (a total of "
                           "10 feet for most PCs). "
                         , "You move through the water 10 feet, plus 5 feet per 20 feet of your land Speed (a total "
                           "of 15 feet for most PCs). "
                         , None
                         , None
                         , "Lake or other still water"
                         , "Flowing water, like a river"
                         , "Swiftly flowing river"
                         , "Stormy sea"
                         , "Maelstrom, waterfall"
                         , False)

# Athletics
actionTRIP = SkillAction("Trip"
                         , "You try to knock a creature to the ground. Attempt an Athletics check against the "
                           "target’s Reflex DC. "
                         , 1
                         , [traitATTACK]
                         , "You lose your balance and fall and land prone."
                         , None
                         , "The target falls and lands prone."
                         , "The target falls and lands prone and takes 1d6 bludgeoning damage."
                         , "You have at least one hand free. Your target can’t be more than one size larger than you."
                         , None
                         , None
                         , None
                         , None
                         , None
                         , None
                         , False)

# Athletics
actionDISARM = SkillAction("Disarm"
                           , "You try to knock something out of a creature’s grasp. Attempt an Athletics check "
                             "against the target’s Reflex DC. "
                           , 1
                           , [traitATTACK]
                           , "You lose your balance and become flat-footed until the start of your next turn"
                           , None
                           , "You weaken your target's grasp on the item. Until the start of that creature's turn, "
                             "attempts to Disarm the target of that item gain a +2 circumstance bonus, and the target "
                             "takes a –2 circumstance penalty to attacks with the item or other checks requiring a "
                             "firm grasp on the item. "
                           , "You knock the item out of the target's grasp. It falls to the ground in the target's "
                             "space. "
                           , "You have at least one hand free. The target can’t be more than one size larger than you."
                           , None
                           , None
                           , None
                           , None
                           , None
                           , None
                           , True)

# Crafting, Lore, Performance
activityEARNINCOME = SkillAction("Earn Income"
                                 , "You use one of your skills to make money during downtime. The GM assigns a task "
                                   "level representing the most lucrative job available. You can search for "
                                   "lower-level tasks, with the GM determining whether you find any. Sometimes you "
                                   "can attempt to find better work than the initial offerings, though this takes "
                                   "time and requires using the Diplomacy skill to Gather Information, doing some "
                                   "research, or socializing.\nWhen you take on a job, the GM secretly sets the DC "
                                   "of your skill check. After your first day of work, you roll to determine your "
                                   "earnings. You gain an amount of income based on your result, the task’s level, "
                                   "and your proficiency rank (as listed on Table 4–2: Income Earned).\nYou can "
                                   "continue working at the task on subsequent days without needing to roll again. "
                                   "For each day you spend after the first, you earn the same amount as the first "
                                   "day, up until the task’s completion. The GM determines how long you can work at "
                                   "the task. Most tasks last a week or two, though some can take months or even "
                                   "years. "
                                 , None
                                 , [traitDOWNTIME]
                                 , "You earn nothing for your work and are fired immediately. You can’t continue at "
                                   "the task. Your reputation suffers, potentially making it difficult for you to "
                                   "find rewarding jobs in that community in the future. "
                                 , "You do shoddy work and get paid the bare minimum for your time. Gain the amount "
                                   "of currency listed in the failure column for the task level. The GM will likely "
                                   "reduce how long you can continue at the task. "
                                 , "You do competent work. Gain the amount of currency listed for the task level and "
                                   "your proficiency rank. "
                                 , "You do outstanding work. Gain the amount of currency listed for the task level + "
                                   "1 and your proficiency rank. "
                                 , None
                                 , None
                                 , None
                                 , "Bartend, do legal research"
                                 , "Curate drink selection, present minor court cases"
                                 , "Run a large brewery, present important court cases"
                                 , "Run an international brewing franchise, present a case in Hell’s courts"
                                 , True)

# Crafting
activityREPAIR = SkillAction("Repair"
                             , "You spend 10 minutes attempting to fix a damaged item, placing the item on a stable "
                               "surface and using the repair kit with both hands. The GM sets the DC, but it’s usually "
                               "about the same DC to Repair a given item as it is to Craft it in the first place. You "
                               "can’t Repair a destroyed item. "
                             , None
                             , [traitEXPLORATION, traitMANIPULATE]
                             , "You deal 2d6 damage to the item. Apply the item’s Hardness to this damage."
                             , None
                             , "You restore 5 Hit Points to the item, plus an additional 5 per proficiency rank you "
                               "have in Crafting (for a total of 10 HP if you are trained, 15 HP if you’re an expert, "
                               "20 HP if you’re a master, or 25 HP if you’re legendary). "
                             ,
                             "You restore 10 Hit Points to the item, plus an additional 10 Hit Points per proficiency "
                             "rank you have in Crafting (a total of 20 HP if you’re trained, 30 HP if you’re an "
                             "expert, 40 HP if you’re a master, or 50 HP if you’re legendary). "
                             , "You have a repair kit."
                             , None
                             , None
                             , None
                             , None
                             , None
                             , None
                             , False)

# Crafting
activityCRAFT = SkillAction("Craft"
                            , "You can make an item from raw materials. You need the Alchemical Crafting skill feat to "
                              "create alchemical items, the Magical Crafting skill feat to create magic items, "
                              "and the Snare Crafting feat to create snares.\nTo Craft an item, you must meet the "
                              "following requirements:\nThe item is your level or lower. An item that doesn't list a "
                              "level is level 0. If the item is 9th level or higher, you must be a master in Crafting, "
                              "and if it's 16th or higher, you must be legendary.\nYou have the formula for the item; "
                              "see Getting Formulas for more information.\nYou have an appropriate set of tools and, "
                              "in many cases, a workshop. For example, you need access to a smithy to forge a metal "
                              "shield, or an alchemist's lab to produce alchemical items.\nYou must supply raw "
                              "materials worth at least half the item's Price. You always expend at least that amount "
                              "of raw materials when you Craft successfully. If you're in a settlement, you can usually"
                              " spend currency to get the amount of raw materials you need, except in the case of rarer"
                              " precious materials.\nYou must spend 4 days at work, at which point you attempt a "
                              "Crafting check. The GM determines the DC to Craft the item based on its level, rarity, "
                              "and other circumstances.\nIf your attempt to create the item is successful, you expend "
                              "the raw materials you supplied. You can pay the remaining portion of the item's Price in"
                              " materials to complete the item immediately, or you can spend additional downtime days "
                              "working on it. For each additional day you spend, reduce the value of the materials you "
                              "need to expend to complete the item. This amount is determined using Table 4–2: Income "
                              "Earned, based on your proficiency rank in Crafting and using your own level instead of a"
                              " task level. After any of these downtime days, you can complete the item by spending the"
                              " remaining portion of its Price in materials. If the downtime days you spend are "
                              "interrupted, you can return to finish the item later, continuing where you left off. "
                            , None
                            , [traitDOWNTIME, traitMANIPULATE]
                            , "You fail to complete the item. You ruin 10% of the raw materials you supplied, but you "
                              "can salvage the rest. If you want to try again, you must start over. "
                            , "You fail to complete the item. You can salvage the raw materials you supplied for their "
                              "full value. If you want to try again, you must start over. "
                            , "Your attempt is successful. Each additional day spent Crafting reduces the materials "
                              "needed to complete the item by an amount based on your level and your proficiency rank. "
                            , "Your attempt is successful. Each additional day spent Crafting reduces the materials "
                              "needed to complete the item by an amount based on your level + 1 and your proficiency "
                              "rank in Crafting. "
                            , None
                            , None
                            , None
                            , None
                            , None
                            , None
                            , None
                            , True)

# Crafting
activityIDENTIFYALCHEMY = SkillAction("Identify Alchemy"
                                      , "You can identify the nature of an alchemical item with 10 minutes of testing "
                                        "using alchemist’s tools. If your attempt is interrupted in any way, "
                                        "you must start over. "
                                      , None
                                      , [traitCONCENTRATE, traitEXPLORATION, traitMANIPULATE]
                                      , "You misidentify the item as another item of the GM’s choice."
                                      , "You fail to identify the item but can try again."
                                      , "You identify the item and the means of activating it."
                                      , None
                                      , None
                                      , None
                                      , None
                                      , None
                                      , None
                                      , None
                                      , None
                                      , True)

# Deception
actionCREATEDIVERSION = SkillAction("Create a Diversion"
                                    , "With a gesture, a trick, or some distracting words, you can create a diversion "
                                      "that draws creatures' attention elsewhere. If you use a gesture or trick, "
                                      "this action gains the manipulate trait. If you use distracting words, "
                                      "it gains the auditory and linguistic traits.\nAttempt a single Deception check "
                                      "and compare it to the Perception DCs of the creatures whose attention you're "
                                      "trying to divert. Whether or not you succeed, creatures you attempt to divert "
                                      "gain a +4 circumstance bonus to their Perception DCs against your attempts to "
                                      "Create a Diversion for 1 minute. "
                                    , 1
                                    , [traitMENTAL, traitMANIPULATE, traitAUDITORY, traitLINGUISTIC]
                                    , None
                                    , "You don’t divert the attention of any creatures whose Perception DC exceeds "
                                      "your result, and those creatures are aware you were trying to trick them. "
                                    , "You become hidden to each creature whose Perception DC is less than or equal "
                                      "to your result. (The hidden condition allows you to Sneak away.) This lasts "
                                      "until the end of your turn or until you do anything except Step or use the "
                                      "Hide or the Sneak action of the Stealth skill. If you Strike a creature, "
                                      "the creature remains flat-footed against that attack, and you then become "
                                      "observed. If you do anything else, you become observed just before you act "
                                      "unless the GM determines otherwise. "
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , False)

# Deception
activityIMPERSONATE = SkillAction("Impersonate"
                                  , "You create a disguise to pass yourself off as someone or something you are not. "
                                    "Assembling a convincing disguise takes 10 minutes and requires a disguise kit, "
                                    "but a simpler, quicker disguise might do the job if you’re not trying to imitate "
                                    "a specific individual, at the GM’s discretion.\nIn most cases, creatures have a "
                                    "chance to detect your deception only if they use the Seek action to attempt "
                                    "Perception checks against your Deception DC. If you attempt to directly interact "
                                    "with someone while disguised, the GM rolls a secret Deception check for you "
                                    "against that creature’s Perception DC instead. If you’re disguised as a specific "
                                    "individual, the GM might give creatures you interact with a circumstance bonus "
                                    "based on how well they know the person you’re imitating, or the GM might roll a "
                                    "secret Deception check even if you aren't directly interacting with others. "
                                  , None
                                  , [traitCONCENTRATE, traitEXPLORATION, traitMANIPULATE, traitSECRET]
                                  , "The creature can tell you’re not who you claim to be, and it recognizes you if "
                                    "it would know you without a disguise. "
                                  , "The creature can tell you’re not who you claim to be."
                                  , "You trick the creature into thinking you’re the person you’re disguised as. You "
                                    "might have to attempt a new check if your behavior changes. "
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , False)

# Deception
actionLIE = SkillAction("Lie"
                        , "You try to fool someone with an untruth. Doing so takes at least 1 round, or longer if the "
                          "lie is elaborate. You roll a single Deception check and compare it against the Perception "
                          "DC of every creature you are trying to fool. The GM might give them a circumstance bonus "
                          "based on the situation and the nature of the lie you are trying to tell. Elaborate or "
                          "highly unbelievable lies are much harder to get a creature to believe than simpler and "
                          "more believable lies, and some lies are so big that it’s impossible to get anyone to "
                          "believe them.\nAt the GM’s discretion, if a creature initially believes your lie, "
                          "it might attempt a Perception check later to Sense Motive against your Deception DC to "
                          "realize it’s a lie. This usually happens if the creature discovers enough evidence to "
                          "counter your statements. "
                        , 3
                        , [traitAUDITORY, traitCONCENTRATE, traitLINGUISTIC, traitMENTAL, traitSECRET]
                        , None
                        , "The target doesn't believe your lie and gains a +4 circumstance bonus against your "
                          "attempts to Lie for the duration of your conversation. The target is also more likely to "
                          "be suspicious of you in the future. "
                        , "The target believes your lie."
                        , None
                        , None
                        , None
                        , None
                        , None
                        , None
                        , None
                        , None
                        , False)

# Deception
actionFEINT = SkillAction("Feint"
                          , "With a misleading flourish, you leave an opponent unprepared for your real attack. "
                            "Attempt a Deception check against that opponent’s Perception DC. "
                          , 1
                          , [traitMENTAL]
                          , "Your feint backfires. You are flat-footed against melee attacks the target attempts "
                            "against you until the end of your next turn. "
                          , None
                          , "Your foe is fooled, but only momentarily. The target is flat-footed against the next "
                            "melee attack that you attempt against it before the end of your current turn. "
                          , "You throw your enemy’s defenses against you entirely off. The target is flat-footed "
                            "against melee attacks that you attempt against it until the end of your next turn. "
                          , "You are within melee reach of the opponent you attempt to Feint."
                          , None
                          , None
                          , None
                          , None
                          , None
                          , None
                          , True)

# Diplomacy
activityGATHERINFO = SkillAction("Gather Information"
                                 , "You canvass local markets, taverns, and gathering places in an attempt to learn "
                                   "about a specific individual or topic. The GM determines the DC of the check and "
                                   "the amount of time it takes (typically 2 hours, but sometimes more), along with "
                                   "any benefit you might be able to gain by spending coin on bribes, drinks, "
                                   "or gifts. "
                                 , None
                                 , [traitEXPLORATION, traitSECRET]
                                 , "You collect incorrect information about the individual or topic."
                                 , None
                                 , "You collect information about the individual or topic. The GM determines the "
                                   "specifics. "
                                 , None
                                 , None
                                 , None
                                 , "talk of the town"
                                 , "common rumor"
                                 , "obscure rumor, poorly guarded secret"
                                 , "well-guarded or esoteric information"
                                 , "information known only to an incredibly select few, or only to extraordinary beings"
                                 , False)

# Diplomacy
activityMAKEIMPRESSION = SkillAction("Make an Impression"
                                     , "With at least 1 minute of conversation, during which you engage in "
                                       "charismatic overtures, flattery, and other acts of goodwill, you seek to make "
                                       "a good impression on someone to make them temporarily agreeable. At the end "
                                       "of the conversation, attempt a Diplomacy check against the Will DC of one "
                                       "target, modified by any circumstances the GM sees fit. Good impressions (or "
                                       "bad impressions, on a critical failure) last for only the current social "
                                       "interaction unless the GM decides otherwise. "
                                     , None
                                     , [traitAUDITORY, traitCONCENTRATE, traitEXPLORATION, traitLINGUISTIC, traitMENTAL]
                                     , "The target’s attitude toward you decreases by one step."
                                     , None
                                     , "The target’s attitude toward you improves by one step."
                                     , "The target’s attitude toward you improves by two steps."
                                     , None
                                     , None
                                     , None
                                     , None
                                     , None
                                     , None
                                     , None
                                     , False)

# diplomacy
actionREQUEST = SkillAction("Request"
                            , "You can make a request of a creature that’s friendly or helpful to you. You must couch "
                              "the request in terms that the target would accept given their current attitude toward "
                              "you. The GM sets the DC based on the difficulty of the request. Some requests are "
                              "unsavory or impossible, and even a helpful NPC would never agree to them. "
                            , 1
                            , [traitAUDITORY, traitCONCENTRATE, traitLINGUISTIC, traitMENTAL]
                            , "Not only does the target refuse the request, but their attitude toward you decreases "
                              "by one step due to the temerity of the request. "
                            , "The target refuses the request, though they might propose an alternative that is less "
                              "extreme. "
                            , "The target agrees to your request, but they might demand added provisions or "
                              "alterations to the request. "
                            , "The target agrees to your request without qualifications."
                            , None
                            , None
                            , None
                            , None
                            , None
                            , None
                            , None
                            , False)

# Intimidation
activityCOERCE = SkillAction("Coerce"
                             , "With threats either veiled or overt, you attempt to bully a creature into doing what "
                               "you want. You must spend at least 1 minute of conversation with a creature you can "
                               "see and that can either see or sense you. At the end of the conversation, attempt an "
                               "Intimidation check against the target's Will DC, modified by any circumstances the GM "
                               "determines. The attitudes referenced in the effects below are summarized in the "
                               "Changing Attitudes sidebar and described in full in the Conditions page. "
                             , [traitAUDITORY, traitCONCENTRATE, traitEMOTION, traitEXPLORATION, traitLINGUISTIC,
                                traitMENTAL]
                             , None
                             , "The target refuses to comply, becomes hostile if they weren't already, and can’t be "
                               "Coerced by you for at least 1 week. "
                             , "The target doesn't do what you say, and if they were not already unfriendly or "
                               "hostile, they become unfriendly. "
                             , "As critical success, but once the target becomes unfriendly, they might decide to act "
                               "against you—for example, by reporting you to the authorities or assisting your "
                               "enemies. "
                             , "The target gives you the information you seek or agrees to follow your directives so "
                               "long as they aren't likely to harm the target in any way. The target continues to "
                               "comply for an amount of time determined by the GM but not exceeding 1 day, "
                               "at which point the target becomes unfriendly (if they weren't already unfriendly or "
                               "hostile). However, the target is too scared of you to retaliate—at least in the short "
                               "term. "
                             , None
                             , None
                             , None
                             , None
                             , None
                             , None
                             , None
                             , False)

# Intimidation
actionDEMORALIZE = SkillAction("Demoralize"
                               , "With a sudden shout, a well-timed taunt, or a cutting putdown, you can shake an "
                                 "enemy's resolve. Choose a creature within 30 feet of you who you're aware of. "
                                 "Attempt an Intimidation check against that target's Will DC. If the target does not "
                                 "understand the language you are speaking, or you're not speaking a language, "
                                 "you take a –4 circumstance penalty to the check. Regardless of your result, "
                                 "the target is temporarily immune to your attempts to Demoralize it for 10 minutes. "
                               , 1
                               , [traitAUDITORY, traitCONCENTRATE, traitEMOTION, traitFEAR, traitMENTAL]
                               , None
                               , None
                               , "The target becomes frightened 1."
                               , "The target becomes frightened 2."
                               , None
                               , None
                               , None
                               , None
                               , None
                               , None
                               , None
                               , False)

# Medicine
actionADMINISTERFIRSTAID = SkillAction("Administer First Aid"
                                       , "You perform first aid on an adjacent creature that is dying or bleeding. If "
                                         "a creature is both dying and bleeding, choose which ailment you’re trying "
                                         "to treat before you roll. You can Administer First Aid again to attempt to "
                                         "remedy the other effect.\nStabilize Attempt a Medicine check on a creature "
                                         "that has 0 Hit Points and the dying condition. The DC is equal to 5 + that "
                                         "creature’s recovery roll DC (typically 15 + its dying value).\nStop "
                                         "Bleeding Attempt a Medicine check on a creature that is taking persistent "
                                         "bleed damage, giving them a chance to make another flat check to remove the "
                                         "persistent damage. The DC is usually the DC of the effect that caused the "
                                         "bleed. "
                                       , 2
                                       , [traitMANIPULATE]
                                       , "If you were trying to stabilize, the creature’s dying value increases by 1. "
                                         "If you were trying to stop bleeding, it immediately takes an amount of "
                                         "damage equal to its persistent bleed damage. "
                                       , None
                                       , "If you’re trying to stabilize, the creature loses the dying condition (but "
                                         "remains unconscious). If you’re trying to stop bleeding, the creature "
                                         "attempts a flat check to end the bleeding. "
                                       , None
                                       , "You are holding healer's tools, or you are wearing them and have a hand free"
                                       , None
                                       , None
                                       , None
                                       , None
                                       , None
                                       , None
                                       , False)

# Medicine
activityTREATDISEASE = SkillAction("Treat Disease"
                                   , "You spend at least 8 hours caring for a diseased creature. Attempt a Medicine "
                                     "check against the disease’s DC. After you attempt to Treat a Disease for a "
                                     "creature, you can’t try again until after that creature’s next save against the "
                                     "disease. "
                                   , None
                                   , [traitDOWNTIME, traitMANIPULATE]
                                   , "Your efforts cause the creature to take a –2 circumstance penalty to its next "
                                     "save against the disease. "
                                   , None
                                   , "You grant the creature a +2 circumstance bonus to its next saving throw against "
                                     "the disease. "
                                   , "You grant the creature a +4 circumstance bonus to its next saving throw against "
                                     "the disease. "
                                   , None
                                   , None
                                   , None
                                   , None
                                   , None
                                   , None
                                   , None
                                   , True)

# Medicine
actionTREATPOISON = SkillAction("Treat Poison"
                                , "You treat a patient to prevent the spread of poison. Attempt a Medicine check "
                                  "against the poison’s DC. After you attempt to Treat a Poison for a creature, "
                                  "you can’t try again until after the next time that creature attempts a save "
                                  "against the poison. "
                                , 1
                                , [traitMANIPULATE]
                                , "Your efforts cause the creature to take a –2 circumstance penalty to its next save "
                                  "against the poison. "
                                , None
                                , "You grant the creature a +2 circumstance bonus to its next saving throw against "
                                  "the poison. "
                                , "You grant the creature a +4 circumstance bonus to its next saving throw against "
                                  "the poison. "
                                , "You are holding healer's tools, or you are wearing them and have a hand free"
                                , None
                                , None
                                , None
                                , None
                                , None
                                , None
                                , True)

# Medicine
activityTREATWOUNDS = SkillAction("Treat Wounds"
                                  , "You spend 10 minutes treating one injured living creature (targeting yourself, "
                                    "if you so choose). The target is then temporarily immune to Treat Wounds actions "
                                    "for 1 hour, but this interval overlaps with the time you spent treating (so a "
                                    "patient can be treated once per hour, not once per 70 minutes).\nThe Medicine "
                                    "check DC is usually 15, though the GM might adjust it based on the "
                                    "circumstances, such as treating a patient outside in a storm, or treating "
                                    "magically cursed wounds. If you’re an expert in Medicine, you can instead "
                                    "attempt a DC 20 check to increase the Hit Points regained by 10; if you’re a "
                                    "master of Medicine, you can instead attempt a DC 30 check to increase the Hit "
                                    "Points regained by 30; and if you’re legendary, you can instead attempt a DC 40 "
                                    "check to increase the Hit Points regained by 50. The damage dealt on a critical "
                                    "failure remains the same.\nIf you succeed at your check, you can continue "
                                    "treating the target to grant additional healing. If you treat them for a total "
                                    "of 1 hour, double the Hit Points they regain from Treat Wounds.\nThe result of "
                                    "your Medicine check determines how many Hit Points the target regains. "
                                  , None
                                  , [traitEXPLORATION, traitHEALING, traitMANIPULATE]
                                  , "The target takes 1d8 damage."
                                  , None
                                  , "The target regains 2d8 Hit Points, and its wounded condition is removed."
                                  , "The target regains 4d8 Hit Points, and its wounded condition is removed."
                                  , "You are holding healer's tools, or you are wearing them and have a hand free"
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , True)

# Nature
actionCOMMANDANIMAL = SkillAction("Command an Animal"
                                  , "You issue an order to an animal. Attempt a Nature check against the animal's "
                                    "Will DC. The GM might adjust the DC if the animal has a good attitude toward "
                                    "you, you suggest a course of action it was predisposed toward, or you offer it a "
                                    "treat.\nYou automatically fail if the animal is hostile or unfriendly to you. If "
                                    "the animal is helpful to you, increase your degree of success by one step. You "
                                    "might be able to Command an Animal more easily with a feat like Ride.\nMost "
                                    "animals know the Drop Prone, Leap, Seek, Stand, Stride, and Strike basic "
                                    "actions. If an animal knows an activity, such as a horse's Gallop, "
                                    "you can Command the Animal to perform the activity, but you must spend as many "
                                    "actions on Command an Animal as the activity's number of actions. You can also "
                                    "spend multiple actions to Command the Animal to perform that number of basic "
                                    "actions on its next turn; for instance, you could spend 3 actions to Command an "
                                    "Animal to Stride three times or to Stride twice and then Strike. "
                                  , 1
                                  , [traitAUDITORY, traitCONCENTRATE]
                                  , "The animal misbehaves or misunderstands, and it takes some other action "
                                    "determined by the GM. "
                                  , "The animal is hesitant or resistant, and it does nothing."
                                  , "The animal is hesitant or resistant, and it does nothing."
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , False)

# Performance
actionPERFORM = SkillAction("Perform"
                            , "When making a brief performance—one song, a quick dance, or a few jokes—you use the "
                              "Perform action. This action is most useful when you want to prove your capability or "
                              "impress someone quickly. Performing rarely has an impact on its own, but it might "
                              "influence the DCs of subsequent Diplomacy checks against the observers—or even change "
                              "their attitudes—if the GM sees fit. "
                            , 1
                            , [traitAUDITORY, traitCONCENTRATE, traitLINGUISTIC, traitMANIPULATE, traitMOVE,
                               traitVISUAL]
                            , "You demonstrate only incompetence."
                            , "Your performance falls flat."
                            , "You prove yourself, and observers appreciate the quality of your performance."
                            , "Your performance impresses the observers, and they’re likely to share stories of your "
                              "ability. "
                            , None
                            , None
                            , "Audience of commoners"
                            , "Audience of artisans"
                            , "Audience of artisans"
                            , "Audience of high nobility or minor royalty"
                            , "Audience of major royalty or otherworldly beings"
                            , False)

# Society, Survival
activitySUBSIST = SkillAction("Subsist"
                              , "You try to provide food and shelter for yourself, and possibly others as well, "
                                "with a standard of living. The GM determines the DC based on the nature of the place "
                                "where you're trying to Subsist. You might need a minimum proficiency rank to Subsist "
                                "in particularly strange environments. Unlike most downtime activities, "
                                "you can Subsist after 8 hours or less of exploration, but if you do, you take a –5 "
                                "penalty. "
                              , None
                              , [traitDOWNTIME]
                              , "You attract trouble, eat something you shouldn't, or otherwise worsen your "
                                "situation. You take a –2 circumstance penalty to checks to Subsist for 1 week. You "
                                "don’t find any food at all; if you don’t have any stored up, you’re in danger of "
                                "starving or dying of thirst if you continue failing. "
                              , "You’re exposed to the elements and don’t get enough food, becoming fatigued until "
                                "you attain sufficient food and shelter. "
                              , "You find enough food and shelter with basic protection from the elements to provide "
                                "you a subsistence living. "
                              , "You either provide a subsistence living for yourself and one additional creature, "
                                "or you improve your own food and shelter, granting yourself a comfortable living. "
                              , None
                              , None
                              , "Lush forest with calm weather or large city with plentiful resources"
                              , "Typical hillside or village"
                              , "Typical mountains or insular hamlet"
                              , "Typical desert or city under siege"
                              , "Barren wasteland or city of undead"
                              , False)

# Society
activityCREATEFORGERY = SkillAction("Create Forgery"
                                    , "You create a forged document, usually over the course of a day or a week. You "
                                      "must have the proper writing material to create a forgery. When you Create a "
                                      "Forgery, the GM rolls a secret DC 20 Society check. If you succeed, "
                                      "the forgery is of good enough quality that passive observers can’t notice the "
                                      "fake. Only those who carefully examine the document and attempt a Perception "
                                      "or Society check against your Society DC can do so.\nIf the document’s "
                                      "handwriting doesn't need to be specific to a person, you need only to have "
                                      "seen a similar document before, and you gain up to a +4 circumstance bonus to "
                                      "your check, as well as to your DC (the GM determines the bonus). To forge a "
                                      "specific person’s handwriting, you need a sample of that person’s "
                                      "handwriting.\nIf your check result was below 20, the forgery has some obvious "
                                      "signs of being a fake, so the GM compares your result to each passive "
                                      "observer’s Perception DC or Society DC, whichever is higher, using the success "
                                      "or failure results below. Once the GM rolls your check for a document, "
                                      "that same result is used against all passive observers’ DCs no matter how many "
                                      "creatures passively observe that document.\nAn observer who was fooled on a "
                                      "passive glance can still choose to closely scrutinize the documents on the "
                                      "lookout for a forgery, using different techniques and analysis methods beyond "
                                      "the surface elements you successfully forged with your original check. In that "
                                      "case, the observer can attempt a Perception or Society check against your "
                                      "Society DC (if they succeed, they know your document is a forgery). "
                                    , None
                                    , [traitDOWNTIME, traitSECRET]
                                    , None
                                    , "The observer knows your document is a forgery."
                                    , "The observer does not detect the forgery."
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , None
                                    , True)

# stealth
actionCONCEALOBJECT = SkillAction("Conceal an Object"
                                  , "You hide a small object on your person (such as a weapon of light Bulk). When "
                                    "you try to sneak a concealed object past someone who might notice it, "
                                    "the GM rolls your Stealth check and compares it to this passive observer’s "
                                    "Perception DC. Once the GM rolls your check for a concealed object, "
                                    "that same result is used no matter how many passive observers you try to sneak "
                                    "it past. If a creature is specifically searching you for an item, it can attempt "
                                    "a Perception check against your Stealth DC (finding the object on success).\nYou "
                                    "can also conceal an object somewhere other than your person, such as among "
                                    "undergrowth or in a secret compartment within a piece of furniture. In this "
                                    "case, characters Seeking in an area compare their Perception check results to "
                                    "your Stealth DC to determine whether they find the object. "
                                  , 1
                                  , [traitMANIPULATE, traitSECRET]
                                  , None
                                  , "The searcher finds the object."
                                  , "The object remains undetected."
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , False)

# Stealth
actionHIDE = SkillAction("Hide"
                         , "You huddle behind cover or greater cover or deeper into concealment to become hidden, "
                           "rather than observed. The GM rolls your Stealth check in secret and compares the result "
                           "to the Perception DC of each creature you’re observed by but that you have cover or "
                           "greater cover against or are concealed from. You gain the circumstance bonus from cover "
                           "or greater cover to your check. "
                         , 1
                         , [traitSECRET]
                         , None
                         , None
                         , "If the creature could see you, you’re now hidden from it instead of observed. If you were "
                           "hidden from or undetected by the creature, you retain that condition.\nIf you "
                           "successfully become hidden to a creature but then cease to have cover or greater cover "
                           "against it or be concealed from it, you become observed again. You cease being hidden if "
                           "you do anything except Hide, Sneak, or Step. If you attempt to Strike a creature, "
                           "the creature remains flat-footed against that attack, and you then become observed. If "
                           "you do anything else, you become observed just before you act unless the GM determines "
                           "otherwise. The GM might allow you to perform a particularly unobtrusive action without "
                           "being noticed, possibly requiring another Stealth check.\nIf a creature uses Seek to make "
                           "you observed by it, you must successfully Hide to become hidden from it again. "
                         , None
                         , "Cover or concealment available"
                         , None
                         , None
                         , None
                         , None
                         , None
                         , None
                         , False)

# Stealth
actionSNEAK = SkillAction("Sneak"
                          , "You can attempt to move to another place while becoming or staying undetected. Stride up "
                            "to half your Speed. (You can use Sneak while Burrowing, Climbing, Flying, or Swimming "
                            "instead of Striding if you have the corresponding movement type; you must move at half "
                            "that Speed.)\nIf you’re undetected by a creature and it’s impossible for that creature "
                            "to observe you (for a typical creature, this includes when you’re invisible, "
                            "the observer is blinded, or you’re in darkness and the creature can’t see in darkness), "
                            "for any critical failure you roll on a check to Sneak, you get a failure instead. You "
                            "also continue to be undetected if you lose cover or greater cover against or are no "
                            "longer concealed from such a creature.\nAt the end of your movement, the GM rolls your "
                            "Stealth check in secret and compares the result to the Perception DC of each creature "
                            "you were hidden from or undetected by at the start of your movement. If you have cover "
                            "or greater cover from the creature throughout your Stride, you gain the +2 circumstance "
                            "bonus from cover (or +4 from greater cover) to your Stealth check. Because you’re "
                            "moving, the bonus increase from Taking Cover doesn't apply. You don’t get to roll "
                            "against a creature if, at the end of your movement, you neither are concealed from it "
                            "nor have cover or greater cover against it. You automatically become observed by such a "
                            "creature. "
                          , 1
                          , [traitMOVE, traitSECRET]
                          , "You’re spotted! You’re observed by the creature throughout your movement and remain so. "
                            "If you’re invisible and were hidden from the creature, instead of being observed you’re "
                            "hidden throughout your movement and remain so. "
                          , "A telltale sound or other sign gives your position away, though you still remain unseen. "
                            "You’re hidden from the creature throughout your movement and remain so. "
                          , "You’re undetected by the creature during your movement and remain undetected by the "
                            "creature at the end of it.\nYou become observed as soon as you do anything other than "
                            "Hide, Sneak, or Step. If you attempt to Strike a creature, the creature remains "
                            "flat-footed against that attack, and you then become observed. If you do anything else, "
                            "you become observed just before you act unless the GM determines otherwise. The GM might "
                            "allow you to perform a particularly unobtrusive action without being noticed, "
                            "possibly requiring another Stealth check. If you speak or make a deliberate loud noise, "
                            "you become hidden instead of undetected.\nIf a creature uses Seek and you become hidden "
                            "to it as a result, you must Sneak if you want to become undetected by that creature "
                            "again. "
                          , None
                          , None
                          , None
                          , None
                          , None
                          , None
                          , None
                          , None
                          , False)

# Survival
activitySENSEDIRECTION = SkillAction("Sense Direction"
                                     , "Using the stars, the position of the sun, traits of the geography or flora, "
                                       "or the behavior of fauna, you can stay oriented in the wild. Typically, "
                                       "you attempt a Survival check only once per day, but some environments or "
                                       "changes might necessitate rolling more often. The GM determines the DC and "
                                       "how long this activity takes (usually just a minute or so). More unusual "
                                       "locales or those you’re unfamiliar with might require you to have a minimum "
                                       "proficiency rank to Sense Direction. Without a compass, you take a –2 item "
                                       "penalty to checks to Sense Direction. "
                                     , None
                                     , [traitEXPLORATION, traitSECRET]
                                     , None
                                     , None
                                     , "You gain enough orientation to avoid becoming hopelessly lost. If you are in "
                                       "an environment with cardinal directions, you have a sense of those directions. "
                                     , "You get an excellent sense of where you are. If you are in an environment "
                                       "with cardinal directions, you know them exactly. "
                                     , None
                                     , None
                                     , "determine a cardinal direction using the sun"
                                     , "find an overgrown path in a forest"
                                     , "navigate a hedge maze"
                                     , "navigate a byzantine labyrinth or relatively featureless desert"
                                     , "navigate an ever-changing dream realm"
                                     , False)

# Survival
activityCOVERTRACKS = SkillAction("Cover Tracks"
                                  , "You cover your tracks, moving up to half your travel speed. You don’t need to "
                                    "attempt a Survival check to cover your tracks, but anyone tracking you must "
                                    "succeed at a Survival check against your Survival DC if it is higher than the "
                                    "normal DC to Track.\nIn some cases, you might Cover Tracks in an encounter. In "
                                    "this case, Cover Tracks is a single action and doesn't have the exploration "
                                    "trait. "
                                  , None
                                  , [traitCONCENTRATE, traitEXPLORATION, traitMOVE]
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , True)

# Survival
activityTRACK = SkillAction("Track"
                            , "You follow tracks, moving at up to half your travel speed. After a successful check to "
                              "Track, you can continue following the tracks at half your Speed without attempting "
                              "additional checks for up to 1 hour. In some cases, you might Track in an encounter. In "
                              "this case, Track is a single action and doesn't have the exploration trait, "
                              "but you might need to roll more often because you’re in a tense situation. The GM "
                              "determines how often you must attempt this check.\nYou attempt your Survival check "
                              "when you start Tracking, once every hour you continue tracking, and any time something "
                              "significant changes in the trail. The GM determines the DCs for such checks, "
                              "depending on the freshness of the trail, the weather, and the type of ground. "
                            , None
                            , [traitCONCENTRATE, traitEXPLORATION, traitMOVE]
                            , "You lose the trail and can’t try again for 24 hours."
                            , "You lose the trail but can try again after a 1-hour delay."
                            , "You find the trail or continue to follow the one you’re already following."
                            , None
                            , None
                            , None
                            , "The path of a large army following a road"
                            , "Relatively fresh tracks of a rampaging bear through the plains"
                            , "A nimble panther's tracks through a jungle, tracks obscured by rainfall"
                            , "Tracks obscured by winter snow, tracks of a mouse or smaller creature, tracks left on "
                              "surfaces that can't hold prints like bare rock "
                            , "Old tracks through a windy desert’s sands, tracks after a major blizzard or hurricane"
                            , True)

# Thievery
actionPALMOBJECT = SkillAction("Palm an Object"
                               , "Palming a small, unattended object without being noticed requires you to roll a "
                                 "single Thievery check against the Perception DCs of all creatures who are currently "
                                 "observing you. You take the object whether or not you successfully conceal that you "
                                 "did so. You can typically only Palm Objects of negligible Bulk, though the GM might "
                                 "determine otherwise depending on the situation. "
                               , 1
                               , [traitMANIPULATE]
                               , None
                               , "The creature notices you Palming the Object, and the GM determines the creature’s "
                                 "response. "
                               , "The creature does not notice you Palming the Object."
                               , None
                               , None
                               , None
                               , None
                               , None
                               , None
                               , None
                               , None
                               , False)

# Thievery
actionSTEAL = SkillAction("Steal"
                          , "You try to take a small object from another creature without being noticed. Typically, "
                            "you can Steal only an object of negligible Bulk, and you automatically fail if the "
                            "creature who has the object is in combat or on guard.\nAttempt a Thievery check to "
                            "determine if you successfully Steal the object. The DC to Steal is usually the "
                            "Perception DC of the creature wearing the object. This assumes the object is worn but "
                            "not closely guarded (like a loosely carried pouch filled with coins, or an object within "
                            "such a pouch). If the object is in a pocket or similarly protected, you take a –5 "
                            "penalty to your Thievery check. The GM might increase the DC of your check if the nature "
                            "of the object makes it harder to steal (such as a very small item in a large pack, "
                            "or a sheet of parchment mixed in with other documents).\nYou might also need to compare "
                            "your Thievery check result against the Perception DCs of observers other than the person "
                            "wearing the object. The GM may increase the Perception DCs of these observers if they’re "
                            "distracted. "
                          , 1
                          , [traitMANIPULATE]
                          , None
                          , "The item’s bearer notices your attempt before you can take the object, or an observer "
                            "sees you take or attempt to take the item. The GM determines the response of any "
                            "creature that notices your theft. "
                          , "You steal the item without the bearer noticing, or an observer doesn't see you take or "
                            "attempt to take the item. "
                          , None
                          , None
                          , None
                          , None
                          , None
                          , None
                          , None
                          , None
                          , False)

# Thievery
actionDISABLEDEVICE = SkillAction("Disable a Device"
                                  , "This action allows you to disarm a trap or another complex device. Often, "
                                    "a device requires numerous successes before becoming disabled, depending on its "
                                    "construction and complexity. Thieves’ tools are helpful and sometimes even "
                                    "required to Disable a Device, as determined by the GM, and sometimes a device "
                                    "requires a higher proficiency rank in Thievery to disable it.\nYour Thievery "
                                    "check result determines how much progress you make. "
                                  , 2
                                  , [traitMANIPULATE]
                                  , "You trigger the device."
                                  , None
                                  , "You disable the device, or you achieve one success toward disabling a complex "
                                    "device. "
                                  , "You disable the device, or you achieve two successes toward disabling a complex "
                                    "device. You leave no trace of your tampering, and you can rearm the device "
                                    "later, if that type of device can be rearmed. "
                                  , "Some devices require you to use thieves’ tools when disabling them."
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , None
                                  , True)

# Thievery
actionPICKLOCK = SkillAction("Pick a Lock"
                             , "Opening a lock without a key is very similar to Disabling a Device, but the DC of the "
                               "check is determined by the complexity and construction of the lock you are attempting "
                               "to pick (locks and their DCs are found in their description). Locks of higher "
                               "qualities might require multiple successes to unlock, since otherwise even an "
                               "unskilled burglar could easily crack the lock by attempting the check until they "
                               "rolled a natural 20. If you lack the proper tools, the GM might let you used "
                               "improvised picks, which are treated as shoddy tools, depending on the specifics of "
                               "the lock. "
                             , 2
                             , [traitMANIPULATE]
                             , "You break your tools. Fixing them requires using Crafting to Repair them or else "
                               "swapping in replacement picks (costing 3 sp, or 3 gp for infiltrator thieves’ tools) "
                             , None
                             , "You open the lock, or you achieve one success toward opening a complex lock."
                             , "You unlock the lock, or you achieve two successes toward opening a complex lock. You "
                               "leave no trace of your tampering. "
                             , "You have thieves’ tools."
                             , None
                             , None
                             , None
                             , None
                             , None
                             , None
                             , True)
