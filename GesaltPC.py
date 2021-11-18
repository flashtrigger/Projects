class GesaltPC:
    def __init__(self):

        self.name = ""
        self.ancestry, self.heritage, self.vHeritage, self.background, self.size = "", "", "", "", ""
        self.senses = ""
        self.classes, self.proficiencies = [], []
        self.level, self.speed = 0, 0
        self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA = 0, 0, 0, 0, 0, 0
        self.STRmod, self.DEXmod, self.CONmod, self.INTmod, self.WISmod, self.CHAmod = 0, 0, 0, 0, 0, 0
        self.fort, self.ref, self.will = 0, 0, 0
        self.actions, self.feats, self.skills, self.equipment, self.worn = [], [], [], [], []
        self.AC, self.melee, self.ranged, self.initiative = 0, 0, 0, 0
