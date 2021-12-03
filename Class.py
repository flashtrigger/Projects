from Entity import Entity
from Variables import *


class Class(Entity):

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.stat = args[2]  # choice Variables
        self.hitDie = args[3]  # integer
        self.proficiency = Proficiency.Untrained
        self.specialty = args[4]  # class ability or null
        self.classAbilities = args[5]  # list of class abilities


# TODO: classBARBARIAN
# TODO: classFIGHTER
# TODO: classRANGER
# TODO: classROGUE
# p3TODO: input all classes

classEXAMPLE = Class("", "", "", 8, None, [])

classBARBARIAN = Class("Barbarian", "", "", 12, "Instinct", [])

classFIGHTER = Class("Fighter", "", 10, None, [])

classRANGER = Class("Ranger", "", "", 10, "Hunter's Edge", [])

classROGUE = Class("Rogue", "", "", 8, "Racket", [])
