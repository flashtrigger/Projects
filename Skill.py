class Skill:

    def __init__(self, *args):

        length = len(args)
        self.name = args[0]
        self.stat = args[1]
        self.type = args[2]
        self.proficiency = args[3]
        self.bonus = args[4]

        if length >= 6:  # actions beyond this parameter
            num = length - 5
            self.actions = []  # list of actions
            i = 5
            for x in range(0, num):
                self.actions[x] = args[i]
                i += 1
