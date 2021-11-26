from Trait import *


class Activity:

    def __init__(self, *args):

        self.name = args[1]
        self.description = args[2]
        self.type = args[3]  # exploration / maybe downtime?
        self.traits = args[4]


