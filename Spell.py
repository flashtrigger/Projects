from Trait import *


class Spell:

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
                         [traitCOMMON, traitCANTRIP, traitELECTRICITY, traitEVOCATION, traitARCANE, traitPRIMAL],
                         1, "Somatic, Verbal", None, None, "1d4+stat", "Electricity", "Basic Reflex",
                         "1 or 2 Creatures", "30 ft", None, False, False, True, "(+1) 1d4")

spellELECTRICARC_featDS = Spell("Electric Arc", 2,
                                "An arc of lightning leaps from one target to another. You deal electricity damage "
                                "equal to 1d4 plus your spellcasting ability modifier.",
                                [traitCOMMON, traitCANTRIP, traitELECTRICITY, traitEVOCATION, traitARCANE, traitPRIMAL,
                                 traitMANIPULATE, traitMAGICAL, traitCONCENTRATE],
                                1, "Somatic, Verbal", None, None, "1d4+stat", "Electricity", "Basic Reflex",
                                "1 or 2 Creatures", "30 ft", None, False, True, True, "(+1) 1d4", "At-Will")

# spell = Spell("", 2, "", [], 1, "", "", 1, "", "", "", "", "", "", "", False, False, False)
