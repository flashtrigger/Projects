from enum import Enum
from functools import total_ordering


# proficiency
from Entity import Entity


@total_ordering
class Proficiency(Enum):  # DONE Phase 1!

    Untrained = 0
    Trained = 2
    Expert = 4
    Master = 6
    Legendary = 8

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        else:
            print("Error: compared types are not same")

    def equals(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        else:
            print("Error: compared types are not same")


# size
@total_ordering
class Size(Enum):

    Tiny = 1
    Small = 2
    Medium = 3
    Large = 4
    Huge = 5
    Gargantuan = 6

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        else:
            print("Error: compared types are not same")

    def equals(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        else:
            print("Error: compared types are not same")


# stat pick options
Dex = ["Dexterity"]
DexInt = ["Dexterity", "Intelligence"]
Free = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
Str = ["Strength"]
StrDex = ["Strength", "Dexterity"]

# simple choice lists such as yes/no
yes = Entity("Yes", "")
no = Entity("No", "")
yesNo = [yes, no]
# p2TODO: build array linking weapon group to specialization effect
