class Spell:

    def __init__(self, *args):

        self.name = args[0]
        self.numActions = args[1]  # integer, -1 = reaction, 0 = free
        self.description = args[2]
        self.traits = args[3]  # list of Traits
        self.level = args[4]  # integer
        self.components = args[5]
        self.trigger = args[6]
        self.duration = args[7]  # integer rounds
        self.damage = args[8]
        self.dType = args[9]
        self.save = args[10]
        self.target = args[11]
        self.range = args[12]
        self.area = args[13]
        self.save = args[14]
        self.isFocus = args[15]  # boolean
        self.canHeighten = args[16]  # boolean
        self.isInnate = args[17]  # boolean
