class ClassAbility:

    def __init__(self, *args):

        length = len(args)
        self.name = args[0]
        self.description = args[1]
        self.traits = args[2]  # list of Traits
        self.level = args[3]  # integer

        if length >= 5:  # actions
            num = length - 4
            i = 4
            self.actions = []  # list of actions
            for x in range(0, num):
                self.actions[x] = args[i]
                i += 1
