import Functions as Foo


class Class:

    def __init__(self, *args):
        self.name = args[0]
        self.stat = args[1]
        self.hitDie = args[3]
        self.proficiency = args[4]
        self.bonus = Foo.setProfBonus(self.proficiency)  # integer
        self.specialty = args[5]  # class ability or null
        self.classAbilities = args[6]  # list of class abilities
