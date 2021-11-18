import Functions


class Skill:

    def __init__(self, *args):

        if len(args) >= 4:
            self.name = args[0]
            self.stat = args[1]
            self.type = args[2]
            self.proficiency = args[3]
            self.bonus = args[4]

        if len(args) >= 8:  # creates actions attached to self
            self.newActions = []
            num = int((len(args) - 5) / 3)
            i = len(args)
            for x in range(1, num):
                self.newActions[x] = Functions.addAction(args[i], args[i + 1], args[i + 2])
                i += 3

