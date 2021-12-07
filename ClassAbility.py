from Entity import Entity


class ClassAbility(Entity):

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.traits = args[2]  # list of Traits
        self.level = args[3]  # integer
        self.actions = args[4]  # list of Actions


# TODO level 1 rogue/ranger/fighter/barbarian class abilities
