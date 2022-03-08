from Trait import *


class Heritage(Entity):  # DONE Phase 1!

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.ancestry = args[2]  # 'Versatile'
        self.traits = args[3]  # List of Traits
        self.actions = args[4]  # list of actions


# Human
heritageHALFELF = Heritage("Half-Elf",
                           "Either one of your parents was an elf, or one or both were half-elves. You have pointed "
                           "ears and other telltale signs of elf heritage. You gain the elf trait, the half-elf "
                           "trait, and low-light vision. In addition, you can select elf, half-elf, and human feats "
                           "whenever you gain an ancestry feat.",
                           "Human", [traitCOMMON, traitELF, traitHALFELF], [])

heritageHALFORC = Heritage("Half-Orc",
                           "One of your parents was an orc, or one or both were half-orcs. You have a green tinge to "
                           "your skin and other indicators of orc heritage. You gain the orc trait, the half-orc "
                           "trait, and low-light vision. In addition, you can select orc, half-orc, and human feats "
                           "whenever you gain an ancestry feat.",
                           "Human", [traitCOMMON, traitORC, traitHALFORC], [])

# Versatile
heritageAASIMAR = Heritage("Aasimar",
                           "You descend from celestials or were touched by the celestial realms, gaining an air of "
                           "awe and grace, as well as features distinctive to your celestial forebears. You gain the "
                           "aasimar trait, in addition to the traits from your ancestry. You also gain low-light "
                           "vision, or you gain darkvision if your ancestry already has low-light vision. You can "
                           "choose from aasimar feats and feats from your ancestry whenever you gain an ancestry "
                           "feat.",
                           "Versatile", [traitUNCOMMON, traitAASIMAR], [])

heritageTIEFLING = Heritage("Tiefling",
                            "You descend from fiends or bear the mark of the fiendish realms, manifesting as some "
                            "unusual feature that belies your heritage, such as horns or a tail. You gain the "
                            "tiefling trait, in addition to the traits from your ancestry. You also gain low-light "
                            "vision, or you gain darkvision if your ancestry already has low-light vision. You can "
                            "choose from tiefling feats and feats from your ancestry whenever you gain an ancestry "
                            "feat.",
                            "Versatile", [traitUNCOMMON, traitTIEFLING], [])

# heritage = Heritage("", "", "", [], [])
