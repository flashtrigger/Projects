class Racket:

    def __init__(self, *args):

        self.name = args[0]
        self.description = args[1]
        self.skills = args[2]  # list of Skills
        self.statChoices = args[3]  # from Variables
        self.actions = args[4]  # list of Actions
        self.proficiency = args[5]  # list of BaseProficiencies


# TODO: initialize needed Racket
