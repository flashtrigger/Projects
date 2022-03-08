import math

from ACitem import ACItem
from Action import *
from Armor import Armor
from BaseProficiency import *
from Class import Class
from EquipSlot import *
from Feat import Feat
import Functions as Foo
from RangeWeapon import RangeWeapon
from Skill import *
from Trait import *
from Variables import *


class GesaltPC(Entity):

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.alignment = ""
        self.ancestry, self.background, self.languages = [], [], []
        self.size, self.senses = "", []
        self.classes = []
        self.level, self.speed, self.heroPoints, self.XP, self.HP = 1, 0, 0, 0, 0
        self.spells = [["Innate", copy.deepcopy(proficiencyINNATESPELLS), "Charisma", []]]
        self.stats = [["Strength", 0, 0], ["Dexterity", 0, 0], ["Constitution", 0, 0],
                      ["Intelligence", 0, 0], ["Wisdom", 0, 0], ["Charisma", 0, 0]]
        self.baseProficiencies, self.saves = copy.deepcopy(proficiencyALLBASIC), copy.deepcopy(proficiencyALLSAVES)
        self.feats, self.skills, self.equipment = [], copy.deepcopy(skillPACKAGE), []
        self.worn = [slotARMOR, slotLEFTHAND, slotRIGHTHAND]
        self.actionList = [copy.deepcopy(actionsBASIC), copy.deepcopy(actionsSPECIAL), [], [], []]  # class/skills/feats
        self.activityList = [[], []]  # Downtime/Exploration
        self.AC = 0
        self.perception, self.percBonus = Proficiency.Untrained, 0
        self.bulkTotal, self.bulkMax, self.bulkEncumb = 0.0, 0, 0

    def addItem(self, item, count):
        bFound = False
        for each in self.equipment:
            if each.equals(item):
                each.count = each.count + count
                bFound = True
                break
        if not bFound:
            self.equipment.append(copy.deepcopy(item))
            self.addItem(item, (count-1))

    def buildActions(self):
        thisList = [self.classes, self.skills, self.feats]
        i = 1
        where = None

        for eachList in thisList:
            i = i + 1

            for each in eachList:
                Trained = False
                print("\n" + each.name)
                if type(each) == Class:
                    for elem in each.classFeatures:
                        where = elem.actions
                else:
                    where = each.actions

                for element in where:
                    if element.name == "Recall Knowledge" or element.name == "Subsist":
                        element.name = element.name + "(" + each.name + ")"
                    insert = [element, each.name]

                    if isinstance(element, SkillAction):
                        if each.proficiency.value > 1:
                            Trained = True
                        isAction = (not element.traits.__contains__(traitEXPLORATION)) and \
                                   (not element.traits.__contains__(traitDOWNTIME))

                        if ((not element.isTrained) or (element.isTrained and Trained)) and isAction:
                            if insert not in self.actionList[i]:
                                self.actionList[i].append(insert)

                        elif ((not element.isTrained) or (element.isTrained and Trained)) and not isAction:
                            if element.traits.__contains__(traitEXPLORATION):
                                self.activityList[1].append(insert)
                            elif element.traits.__contains__(traitDOWNTIME):
                                self.activityList[0].append(insert)

                    elif not isinstance(element, SkillAction):
                        if element not in self.actionList[i]:
                            self.actionList[i].append(insert)

                for j in range(len(self.actionList[i])):
                    if self.actionList[i][j][1] == each.name:
                        print(self.actionList[i][j][0].name + ", " + self.actionList[i][j][1])

    def buildBaseProfs(self, kind):  # 1=Base, -1=saves
        where = None
        if kind == 1:
            where = self.baseProficiencies
        elif kind == -1:
            where = self.saves
        for each in self.classes:
            print(each.name)
            for profList in each.proficiencies:
                for prof in profList:
                    if prof.type == kind:
                        currentProf = next(j for j in where if j.name == prof.name)
                        if currentProf.proficiency.__lt__(prof.proficiency):
                            currentProf.proficiency = prof.proficiency
                            print(currentProf.name + " is now " + currentProf.proficiency.name)
                        elif currentProf.proficiency.equals(prof.proficiency):
                            print(currentProf.name + " is already " + currentProf.proficiency.name)
                        else:
                            print(currentProf.name + " is better than " + prof.proficiency.name)

    # gets feats from list within objects in list
    def buildFeats(self):
        thisList = [self.background, self.classes]
        for each in thisList:
            for source in each:
                for feat in source.feats:
                    if isinstance(feat, Feat):
                        if feat not in self.feats:
                            self.feats.append(feat)
                        else:
                            print("Feat already in list")
                    elif type(feat) == list:
                        choice = Foo.getChoice(feat, "Which feat do you desire?")
                        for elem in feat:
                            if isinstance(elem, Feat):
                                if elem.name == choice:
                                    if elem not in self.feats:
                                        self.feats.append(elem)
                                    else:
                                        print("Feat already in list")

    def buildPerception(self):
        for each in self.classes:
            Foo.compareProf(self.perception, each.perception, 0)

    def buildSkills(self):
        Lists = [self.classes, self.background]
        i = max(cl.baseSkills for cl in self.classes)
        for each in Lists:
            for element in each:
                print(element.name)
                for skill in element.skills:
                    if type(skill) == Skill:
                        for theSkill in self.skills:
                            if skill.name == theSkill.name:
                                i = Foo.compareProf(theSkill, skill, i)
                    elif type(skill) == list:
                        choice = Foo.getChoice(skill, "Which skill do you desire?")
                        for theSkill in self.skills:
                            for elem in skill:
                                if isinstance(elem, Skill):
                                    if elem.name == choice:
                                        i = Foo.compareProf(theSkill, elem, i)
                print("\n")

        for x in range(1, i + 1):
            untrained = []
            for skills in self.skills:
                if skills.proficiency.value == 0:
                    untrained.append(skills)

            pick = Foo.getChoice(untrained, "Pick a skill to train.")
            theSkill = next((j for j in self.skills if j.name == pick))
            theSkill.proficiency = Proficiency.Trained
            print(theSkill.name + " is now " + theSkill.proficiency.name + ". You have " + str(i - x) + " more skills")

    def displayWorn(self):
        for each in self.worn:
            print(each.name)
            if each.isFull:
                print(each.item.name)
            else:
                print("Empty")
            print("\n")

    def fullBuild(self):
        self.updateMODS()
        self.buildFeats()
        self.buildSkills()
        self.buildBaseProfs(1)
        self.buildBaseProfs(-1)
        self.buildActions()
        self.updateBulk()
        self.buildPerception()

    def getATK(self, weapon):
        self.updateMODS()
        PROFmod = 0
        if weapon.traits.__contains__(traitFINESSE) or isinstance(weapon, RangeWeapon):
            STATmod = self.stats[1][2]
        else:
            STATmod = self.stats[0][2]
        for prof in self.baseProficiencies:
            if prof.name == weapon.subcategory:
                PROFmod = prof.proficiency.value
        bonus = STATmod + PROFmod
        return bonus

    def getDAM(self, weapon):
        self.updateMODS()
        if isinstance(weapon, RangeWeapon):
            bonus = self.stats[1][2]
        else:
            bonus = self.stats[0][2]
        return bonus

    def getSpellATKDC(self, spellSource):
        self.updateMODS()
        bonus = 0
        for each in self.stats:
            if each[0] == spellSource[2]:
                bonus = each[2]
        ATK = spellSource[1][0] + bonus
        DC = 10 + spellSource[1][1] + bonus
        return ATK, DC  # spellATK, SpellDC = getSpellATKDC()

    def setPercBonus(self):
        self.percBonus = self.perception.value + self.stats[4][1]

    def updateAC(self):
        self.updateMODS()
        ACmod = 0
        PROFmod = 0
        for each in self.worn:
            if isinstance(each, ACItem):
                ACmod = ACmod + each.AC
            if type(each) == Armor:
                for prof in self.baseProficiencies:
                    if prof.name == each.subcategory:
                        PROFmod = prof.proficiency.value
        self.AC = 10 + self.stats[1][2] + ACmod + PROFmod

    def updateBulk(self):
        self.bulkMax = self.stats[0][2] + 10
        self.bulkEncumb = self.bulkMax - 5
        num = 0.0
        for each in self.equipment:
            num = num + each.bulk
        self.bulkTotal = num
        print("Current Bulk: " + str(round(self.bulkTotal, 3)) + "\nEncumbered: " + str(self.bulkEncumb) + "\nMax: " +
              str(self.bulkMax))

    def updateMODS(self):
        for eachStat in self.stats:
            if eachStat[1] >= 10:
                eachStat[2] = math.floor((eachStat[1] - 10) / 2)
            elif eachStat[1] < 10:
                eachStat[2] = math.ceil((eachStat[1] - 10) / 2)


# P2TODO: addItems method
# P2TODO: addTraits method
