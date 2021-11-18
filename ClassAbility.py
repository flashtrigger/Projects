import Functions


class ClassAbility:

    def __init__(self, *args):

        if len(args) >= 3:
            self.name = args[0]
            self.description = args[1]
            self.traits = args[2]

        if len(args) >= 6:  # creates actions attached to self
            self.newActions = []
            num = int((len(args) - 3) / 3)
            i = len(args)
            for x in range(1, num):
                self.newActions[x] = Functions.addAction(args[i], args[i + 1], args[i + 2])
                i += 3
