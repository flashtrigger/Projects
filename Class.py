import Functions


class Class:

    def __init__(self, *args):
        self.name = args[0]
        self.stat = args[1]
        self.specialty = args[2]
        self.hitDie = args[3]
        self.proficiency = args[4]
        self.bonus = Functions.setProfBonus(self.proficiency)
