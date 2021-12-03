from Entity import Entity


class HunterEdge(Entity):

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.upgrade = args[2]
