import copy

import inquirer

from Ancestry import *
from Armor import armorLEATHER
from Background import *
from Class import *
from Heritage import *


# 11/30/21 still alive - 12/9/21 ded - 12/9/21 repurposing for building PC object - 12/20 functions alive again


# transient method modifying pickled object
from Item import itemBACKPACK
from RangeWeapon import weaponSHORTBOW
from Shield import shieldSTEEL
from Weapon import weaponGNOMEFLICKMACE, weaponDAGGER


def build(this):
    this.alignment = "Chaotic Good"
    this.ancestry = [ancestryHUMAN]
    this.ancestry[0].heritage = [heritageHALFORC, heritageAASIMAR]
    this.background = [backgroundMARTIALADEPT]
    this.languages = this.ancestry[0].languages
    this.size = this.ancestry[0].size
    this.senses = this.ancestry[0].senses
    this.classes = [classFIGHTER, classBARBARIAN]
    this.casterType = "None"
    this.casterStat = "Charisma"
    this.speed = this.ancestry[0].speed
    this.HP = max(each.hitDie for each in this.classes) + max(each.HP for each in this.ancestry)
    this.stats[0][1] = 18
    this.stats[1][1] = 18
    this.stats[2][1] = 16
    this.stats[3][1] = 14
    this.stats[4][1] = 10
    this.stats[5][1] = 10
    # feats for Ancestry Paragon(2), Classes(2)
    this.feats.append(featUNCONVENTIONALWEAPONRY)
    this.feats.append(featDRAGONSPITE)
    this.feats.append(featINTIMIDATINGGLARE)
    this.feats.append(featEXACTINGSTRIKE)
    this.equipment.append(copy.deepcopy(armorLEATHER))
    this.equipment.append(copy.deepcopy(weaponGNOMEFLICKMACE))
    this.equipment.append(copy.deepcopy(shieldSTEEL))
    this.equipment.append(copy.deepcopy(weaponSHORTBOW))
    this.equipment.append(copy.deepcopy(weaponDAGGER))
    this.equipment.append(copy.deepcopy(itemBACKPACK))
    this.worn[0].equip(this.equipment[0])
    this.worn[1].equip(this.equipment[2])
    this.worn[2].equip(this.equipment[1])


# compares 2 proficiencies and improves if current is inferior
def compareProf(current, new, skillCount):
    if new.name == current.name:
        if current.proficiency.value.__lt__(new.proficiency.value):
            current.proficiency = new.proficiency
            print(current.name + " is now " + str(current.proficiency.name))
        elif current.proficiency.equals(new.proficiency):
            print(current.name + " is already " + str(new.proficiency.name))
            if current.proficiency >= Proficiency.Trained:
                pick = getChoice(yesNo, "Should another skill be added?")
                if pick == "Yes":
                    skillCount += 1
        elif new.proficiency.__lt__(current.proficiency):
            print(current.name + " is already better than" + str(new.proficiency.name))
    return skillCount


# select from a list of choices
def getChoice(choices, theMessage):
    options = []
    for element in choices:
        options.append(element.name)
    questions = [inquirer.List('size', message=theMessage, choices=options)]
    answers = inquirer.prompt(questions)
    pick = answers["size"]
    return pick


# adds an action to calling feat, skill, ability # depreciated
def addAction(*args):
    anAction = Action(args[0], args[1], args[2])
    return anAction


# get self.proficiency, returns proficiency bonus # depreciated
# def setProfBonus(proficiency):
#    if proficiency == "Trained":
#        return 2
#    elif proficiency == "Expert":
#        return 4
#    elif proficiency == "Master":
#        return 6
#    elif proficiency == "Legendary":
#        return 8
#    else:
#       return 0


# depreciated due to Entity base class for all classes
def test(this):
    print(this.name + ". " + this.description)
