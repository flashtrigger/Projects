from enum import Enum


# proficiency
class Proficiency(Enum):  # DONE Phase 1!

    Untrained = 0
    Trained = 2
    Expert = 4
    Master = 6
    Legendary = 8


# stat pick options
DexInt = ["Dexterity", "Intelligence"]
Free = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
StrDex = ["Strength, Dexterity"]
