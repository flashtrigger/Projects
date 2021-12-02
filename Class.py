from Variables import *


class Class:

    def __init__(self, *args):
        self.name = args[0]
        self.stat = args[1]  # choice Variables
        self.hitDie = args[2]  # integer
        self.proficiency = Proficiency.Untrained
        self.specialty = args[3]  # class ability or null
        self.classAbilities = args[4]  # list of class abilities


# TODO: classBARBARIAN
# TODO: classFIGHTER
# TODO: classRANGER
# TODO: classROGUE
# p3TODO: input all classes

classEXAMPLE = Class("", "", 8, None, [])

classBARBARIAN = Class("Barbarian", "", 12, "Instinct", [])

classFIGHTER = Class("Fighter", "", 10, None, [])

classRANGER = Class("Ranger", "", 10, "Hunter's Edge", [])

classROGUE = Class("Rogue", "", 8, "Racket", [])
