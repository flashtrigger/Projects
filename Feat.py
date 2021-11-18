import Functions


class feat:

    def __init__(self, *args):

        if len(args) >= 4:
            self.type = args[0]
            self.name = args[1]
            self.description = args[2]
            self.traits = args[3]

        if len(args) >= 7:  # creates actions attached to self
            self.newActions = []
            num = int((len(args) - 4) / 3)
            i = len(args)
            for x in range(1, num):
                self.newActions[x] = Functions.addAction(args[i], args[i+1], args[i+2])
                i += 3
