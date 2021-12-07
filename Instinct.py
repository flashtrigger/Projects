from Entity import Entity


class Instinct(Entity):

    def __init__(self, *args):
        Entity.__init__(self, *args)
        self.anathema = args[2]
        self.ability = args[3]
        self.specialization = args[4]
        self.ragingResistance = args[5]


instinctSPIRIT = Instinct("Spirit"
                          , "Whether you are emotionally sensitive to the spirits around you; worship ancestors or "
                            "apparitions; or are haunted by the specter of an ancestor, relative, friend, or foe, "
                            "your rage takes the form of a spiritual possession. "
                          , "Disrespecting corpses or spirits is anathema to your instinct; defending yourself "
                            "against undead creatures is not. "
                          , "While raging, you can increase the additional damage from Rage from 2 to 3 and change "
                            "its damage type to negative or positive, instead of the damage type for your weapon or "
                            "unarmed attack (choose each time you Rage). If you choose to deal negative or positive "
                            "damage, your weapon or unarmed attack gains the effects of the ghost touch property "
                            "rune, which makes it more effective against incorporeal creatures, and your Rage action "
                            "gains the divine and necromancy traits, plus negative or positive, as appropriate. "
                          , "When using spirit rage, increase the damage from Rage from 3 to 7. If you have greater "
                            "weapon specialization, instead increase the damage when using spirit rage to 13. "
                          , "You resist negative damage, as well as damage dealt by the attacks and abilities of "
                            "undead creatures, regardless of the damage type.")

instinct = Instinct(""
                    , ""
                    , ""
                    , ""
                    , ""
                    , "")
