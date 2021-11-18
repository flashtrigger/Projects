class Proficiency:

    def __init__(self, *args):

        if len(args) >= 4:
            self.name = args[0]
            self.stat = args[1]
            self.proficiency = args[2]
            self.bonus = args[3]
