from Entity import Entity


class Instinct(Entity):

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.anathema = args[2]
        self.ability = args[3]
        self.specialization = args[4]
        self.ragingResistance = args[5]


#  TODO: Needed Instinct
