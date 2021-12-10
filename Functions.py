from Action import Action
from Ancestry import ancestryHUMAN
from Background import backgroundMARTIALADEPT
from Class import classBARBARIAN, classFIGHTER
from Heritage import *
from operator import attrgetter
# 11/30/21 still alive - 12/9/21 ded - 12/9/21 repurposing for building PC object


# transient method modifying pickled object
def build(this):
    this.alignment = "Chaotic Good"
    this.ancestry = [ancestryHUMAN]
    this.ancestry[0].heritage = [heritageHALFORC, heritageAASIMAR]
    this.background = [backgroundMARTIALADEPT]
    this.languages = this.ancestry[0].languages
    this.size = this.ancestry[0].size
    this.senses = this.ancestry[0].senses
    this.classes = [classBARBARIAN, classFIGHTER]
    this.casterType = "None"
    this.casterStat = "Charisma"
    this.speed = this.ancestry[0].speed
    this.HP = max(this.classes, key=attrgetter('hitDie')) + max(this.ancestry, key=attrgetter('HP'))


# adds an action to calling feat, skill, ability # depreciated
def addAction(*args):
    anAction = Action(args[0], args[1], args[2])
    return anAction


# get self.proficiency, returns proficiency bonus # depreciated
def setProfBonus(proficiency):
    if proficiency == "Trained":
        return 2
    elif proficiency == "Expert":
        return 4
    elif proficiency == "Master":
        return 6
    elif proficiency == "Legendary":
        return 8
    else:
        return 0


# depreciated due to Entity base class for all classes
def test(this):
    print(this.name+". "+this.description)
