class Skill:  # TODO: skill actions

    def __init__(self, *args):

        length = len(args)
        self.name = args[0]
        self.stat = args[1]
        self.type = args[2]
        self.proficiency = args[3]
        self.bonus = args[4]
        self.actions = args[5]  # list of actions
        self.activities = args[6]
