from Proficiency import Proficiency


# TODO: establish a common variable list # proficiency?
class Class:

    def __init__(self, *args):
        self.name = args[0]
        self.stat = args[1]
        self.hitDie = args[3]
        self.proficiency = Proficiency.Untrained
        self.specialty = args[5]  # class ability or null
        self.classAbilities = args[6]  # list of class abilities


# TODO: classBARBARIAN
# TODO: classFIGHTER
# TODO: classRANGER
# TODO: classROGUE
