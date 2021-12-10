from Entity import Entity
from Variables import Proficiency


class GesaltPC(Entity):  # DONE Phase 1?

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.alignment = ""
        self.ancestry, self.background, self.languages = [], [], []
        self.size, self.senses, self.casterType, self.casterStat = "", [], "", ""
        self.classes, self.spellList, self.spellSlots = [], [], []
        self.level, self.speed, self.heroPoints, self.XP, self.HP = 1, 0, 0, 0, 0
        self.spellATKprof, self.spellDCprof = Proficiency.Trained, Proficiency.Trained
        self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA = 0, 0, 0, 0, 0, 0
        self.STRmod, self.DEXmod, self.CONmod, self.INTmod, self.WISmod, self.CHAmod = 0, 0, 0, 0, 0, 0
        self.fort, self.ref, self.will, self.classDCBonus, self.spellBonus = 0, 0, 0, 0, 0
        self.actionList, self.feats, self.skills, self.equipment, self.worn = [], [], [], [], []
        self.activityList, self.statusEffects = [], []
        self.AC, self.meleeATK, self.rangeATK, self.spellATK, self.initiative = 0, 0, 0, 0, 0


# P2TODO: addItems method
# P2TODO: addTraits method
