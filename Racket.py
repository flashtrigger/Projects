class Racket(Entity):

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.skills = args[2]  # list of Skills
        self.statChoices = args[3]  # from Variables
        self.actions = args[4]  # list of Actions
        self.proficiency = args[5]  # list of BaseProficiencies


# TODO: initialize needed Racket
