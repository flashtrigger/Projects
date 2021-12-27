import inquirer

from Ancestry import *
from Armor import armorLEATHER
from Background import *
from Class import *
from Heritage import *


# 11/30/21 still alive - 12/9/21 ded - 12/9/21 repurposing for building PC object


# transient method modifying pickled object
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
    this.worn.append(armorLEATHER)
    this.worn.append(weaponGNOMEFLICKMACE)
    this.worn.append(shieldSTEEL)
    this.worn.append(weaponSHORTBOW)
    this.worn.append(weaponDAGGER)


def getChoice(choices, theMessage):
    options = []
    for element in choices:
        options.append(element.name)
    questions = [inquirer.List('size', message=theMessage, choices=options)]
    answers = inquirer.prompt(questions)
    pick = answers["size"]
    return pick


def __eq__(self, other):
    return self.name == other.name


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
