from Trait import *


class Spell:  # DONE Phase 1!

    def __init__(self, *args):

        self.name = args[0]
        self.numActions = args[1]  # integer, -1 = reaction, 0 = free
        self.description = args[2]
        self.traits = args[3]  # list of Traits
        self.level = args[4]  # integer
        self.components = args[5]
        self.trigger = args[6]
        self.duration = args[7]  # integer rounds
        self.damage = args[8]
        self.dType = args[9]
        self.save = args[10]
        self.target = args[11]
        self.range = args[12]
        self.area = args[13]
        self.isFocus = args[14]  # boolean
        self.isInnate = args[15]  # boolean
        self.canHeighten = args[16]  # boolean
        if self.canHeighten:
            self.heightened = args[17]
            if self.isInnate:
                self.uses = args[18]
        elif self.isInnate:
            self.uses = args[17]


spellELECTRICARC = Spell("Electric Arc", 2,
                         "An arc of lightning leaps from one target to another. You deal electricity damage equal to "
                         "1d4 plus your spellcasting ability modifier.",
                         [traitCOMMON, traitCANTRIP, traitELECTRICITY, traitEVOCATION, traitARCANE, traitPRIMAL,
                          traitMANIPULATE, traitMAGICAL, traitCONCENTRATE],
                         1, "Somatic, Verbal", None, None, "1d4+stat", "Electricity", "Basic Reflex",
                         "1 or 2 Creatures", "30 ft", None, False, False, True, "(+1) 1d4")

# Dragon Spit: Electric
spellELECTRICARC_DS = Spell("Electric Arc", 2,
                            "An arc of lightning leaps from one target to another. You deal electricity damage "
                            "equal to 1d4 plus your spellcasting ability modifier.",
                            [traitCOMMON, traitCANTRIP, traitELECTRICITY, traitEVOCATION, traitARCANE, traitPRIMAL,
                             traitMANIPULATE, traitMAGICAL, traitCONCENTRATE],
                            1, "Somatic, Verbal", None, None, "1d4+stat", "Electricity", "Basic Reflex",
                            "1 or 2 Creatures", "30 ft", None, False, True, True, "(+1) 1d4", "At-Will")

spellDETECTMAGIC = Spell("Detect Magic", 2
                         , "You send out a pulse that registers the presence of magic. You receive no information "
                           "beyond the presence or absence of magic. You can choose to ignore magic you're fully "
                           "aware of, such as the magic items and ongoing spells of you and your allies.\nYou detect "
                           "illusion magic only if that magic's effect has a lower level than the level of your "
                           "detect magic spell. However, items that have an illusion aura but aren't deceptive in "
                           "appearance (such as an invisibility potion) typically are detected normally."
                         , [traitCOMMON, traitCANTRIP, traitDETECTION, traitDIVINATION, traitMAGICAL, traitMANIPULATE,
                            traitCONCENTRATE, traitARCANE, traitDIVINE, traitOCCULT, traitPRIMAL]
                         , 1, "Somatic, Verbal", None, None, None, None, None, None, None, "Self", "30 ft"
                         , False, False, True
                         , "Heightened (3rd) You learn the school of magic for the highest-level effect within range "
                           "that the spell detects. If multiple effects are equally strong, the GM determines which "
                           "you learn.\nHeightened (4th) As 3rd level, but you also pinpoint the source of the "
                           "highest-level magic. Like for an imprecise sense, you don't learn the exact location, "
                           "but can narrow down the source to within a 5-foot cube (or the nearest if larger than "
                           "that).")

# Arcane Sense
spellDETECTMAGIC_AS = Spell("Detect Magic", 2
                            , "You send out a pulse that registers the presence of magic. You receive no information "
                              "beyond the presence or absence of magic. You can choose to ignore magic you're fully "
                              "aware of, such as the magic items and ongoing spells of you and your allies.\nYou detect"
                              " illusion magic only if that magic's effect has a lower level than the level of your "
                              "detect magic spell. However, items that have an illusion aura but aren't deceptive in "
                              "appearance (such as an invisibility potion) typically are detected normally."
                            , [traitCOMMON, traitCANTRIP, traitDETECTION, traitDIVINATION, traitMAGICAL,
                               traitMANIPULATE, traitCONCENTRATE, traitARCANE, traitDIVINE, traitOCCULT, traitPRIMAL]
                            , 1, "Somatic, Verbal", None, None, None, None, None, None, None, "Self", "30 ft"
                            , False, True, True
                            , "Heightened (3rd) You learn the school of magic for the highest-level effect within range"
                            " that the spell detects. If multiple effects are equally strong, the GM determines which "
                            "you learn.\nHeightened (4th) As 3rd level, but you also pinpoint the source of the "
                            "highest-level magic. Like for an imprecise sense, you don't learn the exact location, "
                            "but can narrow down the source to within a 5-foot cube (or the nearest if larger than "
                            "that).", "At-Will")

# spell = Spell("", 2, "", [], 1, "", "", 1, "", "", "", "", "", "", "", False, False, False)
