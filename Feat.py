class Feat:

    def __init__(self, *args):

        length = len(args)
        self.type = args[0]
        self.name = args[1]
        self.description = args[2]
        self.traits = args[3]
        self.level = args[4]  # integer

        if length >= 6:  # actions
            num = length - 5
            i = 5
            self.actions = []  # list of actions
            for x in range(0, num):
                self.actions[x] = args[i]
                i += 1
