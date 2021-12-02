class Trait:  # DONE Phase 1?

    def __init__(self, *args):

        self.name = args[0]
        self.description = args[1]
        self.type = args[2]


# P3TODO: untyped traits
traitARCHETYPE = Trait("Archetype", "This feat belongs to an archetype.", "Untyped")
traitATTACK = Trait("Attack", "An ability with this trait involves an attack. For each attack you make beyond the "
                              "first on your turn, you take a multiple attack penalty.", "Untyped")
traitCANTRIP = Trait("Cantrip", "A spell you can cast at will that is automatically heightened to half your level "
                                "rounded up.", "Untyped")
traitCLASS = Trait("Class", "Archetypes with the class trait fundamentally diverge from your class's specialties but "
                            "still fit within the theme of your class. You can select a class archetype only if your "
                            "class meets the criteria listed in the archetype's prerequisites. Class archetypes "
                            "always alter or replace some of a class's static class features in addition to any new "
                            "feats they offer. It might be possible to take a class archetype at 1st level if it "
                            "alters or replaces some of the class's initial class features. The 1st-level ability is "
                            "presented much like a class feature and includes the class archetype's prerequisites and "
                            "rules on how it changes your class. If you select this ability, you must take that "
                            "archetype's dedication feat at 2nd level, and you proceed normally afterward. You can "
                            "never have more than one class archetype.", "Untyped")
traitCONCENTRATE = Trait("Concentrate", "An action with this trait requires a degree of mental concentration and "
                                        "discipline.", "Untyped")
traitDETECTION = Trait("Detection", "Effects with this trait attempt to determine the presence or location of a "
                                    "person, object, or aura.", "Untyped")
traitDOWNTIME = Trait("Downtime", "An activity with this trait takes a day or more, and can be used only during "
                                  "downtime.", "Untyped")
traitEMOTION = Trait("Emotion", "This effect alters a creature's emotions. Effects with this trait always have the "
                                "mental trait as well. Creatures with special training or that have mechanical or "
                                "artificial intelligence are immune to emotion effects.", "Untyped")
traitEXPLORATION = Trait("Exploration", "An activity with this trait takes more than a turn to use, and can usually "
                                        "be used only during exploration mode.", "Untyped")
traitFEAR = Trait("Fear", "Fear effects evoke the emotion of fear. Effects with this trait always have the mental and "
                          "emotion traits as well.", "Untyped")
traitGENERAL = Trait("General", "A type of feat that any character can select, regardless of ancestry and class, "
                                "as long as they meet the prerequisites. You can select a feat with this trait when "
                                "your class grants a general feat.", "Untyped")
traitHEALING = Trait("Healing", "A healing effect restores a creature's body, typically by restoring Hit Points, "
                                "but sometimes by removing diseases or other debilitating effects.", "Untyped")
traitLINGUISTIC = Trait("Linguistic", "An effect with this trait depends on language comprehension. A linguistic "
                                      "effect that targets a creature works only if the target understands the "
                                      "language you are using.", "Untyped")
traitMANIPULATE = Trait("Manipulate", "You must physically manipulate an item or make gestures to use an action with "
                                      "this trait. Creatures without a suitable appendage can’t perform actions with "
                                      "this trait. Manipulate actions often trigger reactions.", "Untyped")
traitMAGICAL = Trait("Magical", "Something with the magical trait is imbued with magical energies not tied to a "
                                "specific tradition of magic. A magical item radiates a magic aura infused with its "
                                "dominant school of magic. Some items or effects are closely tied to a particular "
                                "tradition of magic. In these cases, the item has the arcane, divine, occult, "
                                "or primal trait instead of the magical trait. Any of these traits indicate that the "
                                "item is magical.", "Untyped")
traitMENTAL = Trait("Mental", "A mental effect can alter the target's mind. It has no effect on an object or a "
                              "mindless creature.", "Untyped")
traitMOVE = Trait("Move", "An action with this trait involves moving from one space to another.", "Untyped")
traitPRESS = Trait("Press", "Actions with this trait allow you to follow up earlier attacks. An action with the press "
                            "trait can be used only if you are currently affected by a multiple attack penalty. Some "
                            "actions with the press trait also grant an effect on a failure. The effects that are "
                            "added on a failure don't apply on a critical failure. If your press action succeeds, "
                            "you can choose to apply the failure effect instead. (For example, you may wish to do "
                            "this when an attack deals no damage due to resistance.) Because a press action requires "
                            "a multiple attack penalty, you can't use one when it's not your turn, even if you use "
                            "the Ready activity.", "Untyped")
traitMULTICLASS = Trait("Multiclass", "Archetypes with the multiclass trait represent diversifying your training into "
                                      "another class’s specialties. You can’t select a multiclass archetype’s "
                                      "dedication feat if you are a member of the class of the same name.", "Untyped")
traitSECRET = Trait("Secret", "The GM rolls the check for this ability in secret.", "Untyped")
traitSKILL = Trait("Skill", "A general feat with the skill trait improves your skills and their actions or gives you "
                            "new actions for a skill. A feat with this trait can be selected when a class grants a "
                            "skill feat or general feat. Archetype feats with the skill trait can be selected in "
                            "place of a skill feat if you have that archetype's dedication feat.", "Untyped")
traitFLOURISH = Trait("Flourish", "Flourish actions are actions that require too much exertion to perform a large "
                                  "number in a row. You can use only 1 action with the flourish trait per turn.",
                      "Untyped")

# p3TODO: add rest of classes
traitRANGER = Trait("Ranger", "This indicates abilities from the ranger class.", "Class")
traitROGUE = Trait("Rogue", "This indicates abilities from the rogue class.", "Class")
traitFIGHTER = Trait("Fighter", "This indicates abilities from the fighter class.", "Class")
traitBARBARIAN = Trait("Barbarian", "This indicates abilities from the barbarian class.", "Class")
traitSWASHBUCKLER = Trait("Swashbuckler", "This trait indicates abilities from the swashbuckler class.", "Class")

# p3TODO: class-ability traits
traitINSTINCT = Trait("Instinct", "Instinct abilities require a specific instinct; you lose access if you perform "
                                  "acts anathema to your instinct.", "Class Ability")
traitRAGE = Trait("Rage", "You must be raging to use abilities with the rage trait, and they end automatically when "
                          "you stop raging.", "Class Ability")

# p3TODO: add rest of Ancestries
traitORC = Trait("Orc", "A creature with this trait is a member of the orc ancestry. These green-skinned people tend "
                        "to have darkvision. An ability with this trait can be used or selected only by orcs. An item "
                        "with this trait is created and used by orcs.", "Ancestry")
traitELF = Trait("Elf", "A creature with this trait is a member of the elf ancestry. Elves are mysterious people with "
                        "rich traditions of magic and scholarship who typically have low-light vision. An ability "
                        "with this trait can be used or selected only by elves. A weapon with this trait is created "
                        "and used by elves.", "Ancestry")
traitHUMAN = Trait("Human", "A creature with this trait is a member of the human ancestry. Humans are a diverse array "
                            "of people known for their adaptability. An ability with this trait can be used or "
                            "selected only by humans.", "Ancestry")
traitAASIMAR = Trait("Aasimar", "A creature with this trait has the aasimar versatile heritage. Aasimars are planar "
                                "scions descended from celestial beings. An ability with this trait can be used or "
                                "selected only by aasimars.", "Ancestry")
traitTIEFLING = Trait("Tiefling", "A creature with this trait has the tiefling versatile heritage. Tieflings are "
                                  "planar scions descended from fiends. An ability with this trait can be used or "
                                  "selected only by tieflings.", "Ancestry")
traitHALFELF = Trait("Half-Elf", "A creature with this trait is part human and part elf. An ability with this trait "
                                 "can be used or selected only by half-elves.", "Ancestry")
traitHALFORC = Trait("Half-Orc", "A creature with this trait is part human and part orc. An ability with this trait "
                                 "can be used or selected only by half-orcs.", "Ancestry")

# Armor Traits
traitBULWARK = Trait("Bulwark", "The armor covers you so completely that it provides benefits against some damaging "
                                "effects. On Reflex saves to avoid a damaging effect, such as a fireball, "
                                "you add a +3 modifier instead of your Dexterity modifier.", "Armor")
traitCOMFORT = Trait("Comfort", "The armor is so comfortable that you can rest normally while wearing it.", "Armor")
traitFLEXIBLE = Trait("Flexible", "The armor is flexible enough that it doesn't hinder most actions. You don't apply "
                                  "its check penalty to Acrobatics or Athletics checks.", "Armor")
traitNOISY = Trait("Noisy", "This armor is loud and likely to alert others to your presence. The armor's check "
                            "penalty applies to Stealth checks even if you meet the required Strength score.", "Armor")

#  Alignment traits
traitCHAOTIC = Trait("Chaotic", "Chaotic effects often manipulate energy from chaos-aligned Outer Planes and are "
                                "anathema to lawful divine servants or divine servants of lawful deities. A creature "
                                "with this trait is chaotic in alignment.", "Alignment")
traitEVIL = Trait("Evil", "Evil effects often manipulate energy from evil-aligned Outer Planes and are antithetical "
                          "to good divine servants or divine servants of good deities. A creature with this trait is "
                          "evil in alignment.", "Alignment")
traitGOOD = Trait("Good", "Good effects often manipulate energy from good-aligned Outer Planes and are antithetical "
                          "to evil divine servants or divine servants of evil deities. A creature with this trait is "
                          "good in alignment.", "Alignment")
traitLAWFUL = Trait("Lawful", "Lawful effects often manipulate energy from law-aligned Outer Planes and are "
                              "antithetical to chaotic divine servants or divine servants of chaotic deities. A "
                              "creature with this trait is lawful in alignment.", "Alignment")

# p3TODO: creature type traits
traitHUMANOID = Trait("Humanoid", "Humanoid creatures reason and act much like humans. They typically stand upright "
                                  "and have two arms and two legs.", "Creature Type")

# p3TODO: energy traits
traitELECTRICITY = Trait("Electricity", "Effects with this trait deal electricity damage. A creature with this trait "
                                        "has a magical connection to electricity.", "Energy")

# p3TODO: equipment traits
traitCONSUMABLE = Trait("Consumable", "An item with this trait can be used only once. Unless stated otherwise, "
                                      "it's destroyed after activation. Consumable items include alchemical items and "
                                      "magical consumables such as scrolls and talismans. When a character creates "
                                      "consumable items, they can make them in batches of four.", "Equipment")
traitPOTION = Trait("Potion", "A potion is a magical liquid activated when you drink it.", "Equipment")
traitOIL = Trait("Oil", "Oils are magical gels, ointments, pastes, or salves that are typically applied to an object "
                        "and are used up in the process.", "Equipment")
traitSCROLL = Trait("Scroll", "A scroll contains a single spell you can cast without a spell slot.", "Equipment")

# Rarity Traits
traitCOMMON = Trait("Common", "Anything that doesn't list another rarity trait (uncommon, rare, or unique) "
                              "automatically has the common trait. This rarity indicates that an ability, item, "
                              "or spell is available to all players who meet the prerequisites for it. A creature of "
                              "this rarity is generally known and can be summoned with the appropriate summon spell. "
                              "", "Rarity")
traitRARE = Trait("Rare", "This rarity indicates that a rules element is very difficult to find in the game world. A "
                          "rare feat, spell, item or the like is available to players only if the GM decides to "
                          "include it in the game, typically through discovery during play. Creatures with this trait "
                          "are rare. They typically can't be summoned. The DC of Recall Knowledge checks related to "
                          "these creatures is increased by 5.", "Rarity")
traitUNCOMMON = Trait("Uncommon", "Something of uncommon rarity requires special training or comes from a particular "
                                  "culture or part of the world. Some character choices give access to uncommon "
                                  "options, and the GM can choose to allow access for anyone. Less is known about "
                                  "uncommon creatures than common creatures. They typically can't be summoned. The DC "
                                  "of Recall Knowledge checks related to these creature is increased by 2.", "Rarity")
traitUNIQUE = Trait("Unique", "A rules element with this trait is one-of-a-kind. The DC of Recall Knowledge checks "
                              "related to creatures with this trait is increased by 10.", "Rarity")

# Senses
traitAUDITORY = Trait("Auditory", "Auditory actions and effects rely on sound. An action with the auditory trait can "
                                  "be successfully performed only if the creature using the action can speak or "
                                  "otherwise produce the required sounds. A spell or effect with the auditory trait "
                                  "has its effect only if the target can hear it. This applies only to sound-based "
                                  "parts of the effect, as determined by the GM. This is different from a sonic "
                                  "effect, which still affects targets who can't hear it (such as deaf targets) as "
                                  "long as the effect itself makes sound.", "Senses")
traitOLFACTORY = Trait("Olfactory", "An olfactory effect can affect only creatures that can smell it. This applies "
                                    "only to olfactory parts of the effect, as determined by the GM.", "Senses")
traitVISUAL = Trait("Visual", "A visual effect can affect only creatures that can see it. This applies only to "
                              "visible parts of the effect, as determined by the GM.", "Senses")

# p3TODO: school traits
traitDIVINATION = Trait("Divination", "The divination school of magic typically involves obtaining or transferring "
                                      "information, or predicting events.", "School")
traitEVOCATION = Trait("Evocation", "Effects and magic items with this trait are associated with the evocation school "
                                    "of magic, typically involving energy and elemental forces.", "School")

# Tradition
traitARCANE = Trait("Arcane", "This magic comes from the arcane tradition, which is built on logic and rationality. "
                              "Anything with this trait is magical.", "Tradition")
traitDIVINE = Trait("Divine", "This magic comes from the divine tradition, drawing power from deities or similar "
                              "sources. Anything with this trait is magical.", "Tradition")
traitOCCULT = Trait("Occult", "This magic comes from the occult tradition, calling upon bizarre and ephemeral "
                              "mysteries. Anything with this trait is magical.", "Tradition")
traitPRIMAL = Trait("Primal", "This magic comes from the primal tradition, connecting to the natural world and "
                              "instinct. Anything with this trait is magical.", "Tradition")

# p3TODO: weapon traits
traitAGILE = Trait("Agile", "The multiple attack penalty you take with this weapon on the second attack on your turn "
                            "is –4 instead of –5, and –8 instead of –10 on the third and subsequent attacks in the "
                            "turn.", "Weapon")
traitDEADLY = Trait("Deadly", "On a critical hit, the weapon adds a weapon damage die of the listed size. Roll this "
                              "after doubling the weapon's damage. This increases to two dice if the weapon has a "
                              "greater striking rune and three dice if the weapon has a major striking rune. For "
                              "instance, a rapier with a greater striking rune deals 2d8 extra piercing damage on a "
                              "critical hit. An ability that changes the size of the weapon's normal damage dice "
                              "doesn't change the size of its deadly die.", "Weapon")
traitDISARM = Trait("Disarm", "You can use this weapon to Disarm with the Athletics skill even if you don't have a "
                              "free hand. This uses the weapon's reach (if different from your own) and adds the "
                              "weapon's item bonus to attack rolls (if any) as an item bonus to the Athletics check. "
                              "If you critically fail a check to Disarm using the weapon, you can drop the weapon to "
                              "take the effects of a failure instead of a critical failure. On a critical success, "
                              "you still need a free hand if you want to take the item.", "Weapon")
traitFINESSE = Trait("Finesse", "You can use your Dexterity modifier instead of your Strength modifier on attack "
                                "rolls using this melee weapon. You still use your Strength modifier when calculating"
                                " damage.", "Weapon")
traitGRAPPLE = Trait("Grapple", "You can use this weapon to Grapple with the Athletics skill even if you don't have a "
                                "free hand. This uses the weapon's reach (if different from your own) and adds the "
                                "weapon's item bonus to attack rolls as an item bonus to the Athletics check. If you "
                                "critically fail a check to Grapple using the weapon, you can drop the weapon to take "
                                "the effects of a failure instead of a critical failure.", "Weapon")
traitPARRY = Trait("Parry", "This weapon can be used defensively to block attacks. While wielding this weapon, "
                            "if your proficiency with it is trained or better, you can spend a single action to "
                            "position your weapon defensively, gaining a +1 circumstance bonus to AC until the start "
                            "of your next turn.", "Weapon")
traitPROPULSIVE = Trait("Propulsive", "You add half your Strength modifier (if positive) to damage rolls with a "
                                      "propulsive ranged weapon. If you have a negative Strength modifier, "
                                      "you add your full Strength modifier instead.", "Weapon")
traitRANGED = Trait("Ranged", "These attacks will either list a finite range or a range increment, which follows the "
                              "normal rules for range increments.", "Weapon")
traitREACH = Trait("Reach", "Natural attacks with this trait can be used to attack creatures up to the listed "
                            "distance away instead of only adjacent creatures. Weapons with this trait are long and "
                            "can be used to attack creatures up to 10 feet away instead of only adjacent creatures. "
                            "For creatures that already have reach with the limb or limbs that wield the weapon, "
                            "the weapon increases their reach by 5 feet.", "Weapon")
traitRELOAD = Trait("Reload", "While all weapons need some amount of time to get into position, many ranged weapons "
                              "also need to be loaded and reloaded. This entry indicates how many Interact actions it "
                              "takes to reload such weapons. This can be 0 if drawing ammunition and firing the "
                              "weapon are part of the same action. If an item takes 2 or more actions to reload, "
                              "the GM determines whether they must be performed together as an activity, or you can "
                              "spend some of those actions during one turn and the rest during your next turn.",
                    "Weapon")
traitREPEATING = Trait("Repeating", "A repeating weapon is typically a type of crossbow that has a shorter reload "
                                    "time. These weapons can't be loaded with individual bolts like other crossbows; "
                                    "instead, they require a magazine of specialized ammunition to be loaded into a "
                                    "special slot. Once that magazine is in place, the ammunition is automatically "
                                    "loaded each time the weapon is cocked to fire, reducing its reload to the value "
                                    "in its reload entry (typically 0). When the ammunition runs out, a new magazine "
                                    "must be loaded, which requires a free hand and 3 Interact actions (to remove the "
                                    "old magazine, retrieve the new magazine, and slot the new magazine in place). "
                                    "These actions don't need to be consecutive.", "Weapon")
traitSHOVE = Trait("Shove", "You can use this weapon to Shove with the Athletics skill even if you don't have a free "
                            "hand. This uses the weapon's reach (if different from your own) and adds the weapon's "
                            "item bonus to attack rolls as an item bonus to the Athletics check. If you critically "
                            "fail a check to Shove using the weapon, you can drop the weapon to take the effects of a "
                            "failure instead of a critical failure.", "Weapon")
traitTHROWN = Trait("Thrown", "You can throw this weapon as a ranged attack, and it is a ranged weapon when thrown. A "
                              "thrown weapon adds your Strength modifier to damage just like a melee weapon does. "
                              "When this trait appears on a melee weapon, it also includes the range increment. "
                              "Ranged weapons with this trait use the range increment specified in the weapon’s Range "
                              "entry.", "Weapon")
traitTWOHAND = Trait("Two-Hand", "This weapon can be wielded with two hands. Doing so changes its weapon damage die "
                                 "to the indicated value. This change applies to all the weapon's damage dice, "
                                 "such as those from striking runes.", "Weapon")
traitUNARMED = Trait("Unarmed", "An unarmed attack uses your body rather than a manufactured weapon. An unarmed "
                                "attack isn't a weapon, though it's categorized with weapons for weapon groups, "
                                "and it might have weapon traits. Since it's part of your body, an unarmed attack "
                                "can't be Disarmed. It also doesn't take up a hand, though a fist or other grasping "
                                "appendage generally works like a free-hand weapon.", "Weapon")
traitVERSATILE = Trait("Versatile", "A versatile weapon can be used to deal a different type of damage than that "
                                    "listed in the Damage entry. This trait indicates the alternate damage type. For "
                                    "instance, a piercing weapon that is versatile S can be used to deal piercing or "
                                    "slashing damage. You choose the damage type each time you make an attack.",
                       "Weapon")
traitVOLLEY = Trait("Volley", "This ranged weapon is less effective at close distances. Your attacks against targets "
                              "that are at a distance within the range listed take a –2 penalty.", "Weapon")

# trait = Trait("", "", "")
