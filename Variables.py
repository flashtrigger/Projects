from enum import Enum


# proficiency
class Proficiency(Enum):  # DONE Phase 1!

    Untrained = 0
    Trained = 2
    Expert = 4
    Master = 6
    Legendary = 8


# size
class Size(Enum):

    Tiny = 1
    Small = 2
    Medium = 3
    Large = 4
    Huge = 5
    Gargantuan = 6


# stat pick options
Dex = ["Dexterity"]
DexInt = ["Dexterity", "Intelligence"]
Free = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
Str = ["Strength"]
StrDex = ["Strength", "Dexterity"]

# p2TODO: build array linking weapon group to specialization effect
