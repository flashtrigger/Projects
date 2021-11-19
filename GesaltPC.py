class GesaltPC:
    def __init__(self):

        self.name, self.alignment = "", ""
        self.ancestry, self.heritage, self.vHeritage, self.background, self.size = "", "", "", "", ""
        self.senses, self.casterType, self. casterStat = "", "", ""
        self.classes, self.proficiencies, self.spellList, self.spellSlots = [], [], [], []
        self.level, self.speed, self.heroPoints, self.XP, self.HP = 0, 0, 0, 0, 0
        self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA = 0, 0, 0, 0, 0, 0
        self.STRmod, self.DEXmod, self.CONmod, self.INTmod, self.WISmod, self.CHAmod = 0, 0, 0, 0, 0, 0
        self.fort, self.ref, self.will = 0, 0, 0
        self.actions, self.feats, self.skills, self.equipment, self.worn = [], [], [], [], []
        self.AC, self.meleeATK, self.rangeATK, self.spellATK, self.initiative = 0, 0, 0, 0, 0



# TODO: addItems method
# TODO: addTraits method
