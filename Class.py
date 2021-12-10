from BaseProficiency import *
from ClassFeature import *
from HunterEdge import *
from Instinct import *
from Racket import *
from Skill import *


class Class(Entity):

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.stat = args[2]  # choice Variables
        self.hitDie = args[3]  # integer
        self.cProficiency = None
        self.specialty = args[4]  # class ability or null
        self.specialtyList = None
        self.classFeatures = args[5]  # list of class abilities
        self.proficiencies = proficiencyALL
        self.skills = skillPACKAGE
        self.baseSkills = args[6]  # integer
        self.perception = args[7]  # Proficiency


# p3TODO: input all classes

classEXAMPLE = Class("", "", [], 0, None, [], 0, Proficiency.Trained)

classBARBARIAN = Class("Barbarian", "", Str, 12, "Instinct", [featureRAGE], 3, Proficiency.Expert)
classBARBARIAN.specialtyList = [instinctSPIRIT]
classBARBARIAN.cProficiency = Proficiency.Trained
classBARBARIAN.proficiencies[0][0].proficiency = Proficiency.Trained
classBARBARIAN.proficiencies[0][1].proficiency = Proficiency.Trained
classBARBARIAN.proficiencies[0][3].proficiency = Proficiency.Trained
classBARBARIAN.proficiencies[0][4].proficiency = Proficiency.Trained
classBARBARIAN.proficiencies[0][5].proficiency = Proficiency.Trained
classBARBARIAN.proficiencies[0][7].proficiency = Proficiency.Trained
classBARBARIAN.proficiencies[1][0].proficiency = Proficiency.Expert
classBARBARIAN.proficiencies[1][1].proficiency = Proficiency.Trained
classBARBARIAN.proficiencies[1][2].proficiency = Proficiency.Expert
classBARBARIAN.skills[2].proficiency = Proficiency.Trained  # athletics

classFIGHTER = Class("Fighter", "", StrDex, 10, None, [featureATTACKOPPORTUNITY], 3, Proficiency.Expert)
classFIGHTER.cProficiency = Proficiency.Trained
for x in classFIGHTER.proficiencies[0]:
    classFIGHTER.proficiencies[0][x].proficiency = Proficiency.Trained
classFIGHTER.proficiencies[0][4].proficiency = Proficiency.Expert
classFIGHTER.proficiencies[0][5].proficiency = Proficiency.Expert
classFIGHTER.proficiencies[0][7].proficiency = Proficiency.Expert
classFIGHTER.proficiencies[1][0].proficiency = Proficiency.Expert
classFIGHTER.proficiencies[1][1].proficiency = Proficiency.Expert
classFIGHTER.proficiencies[1][2].proficiency = Proficiency.Trained
classFIGHTER.skills[2].proficiency = Proficiency.Trained  # athletics
# p2TODO: should be choice between acrobatics and athletics

classRANGER = Class("Ranger", "", StrDex, 10, "Hunter's Edge", [featureHUNTPREY], 4, Proficiency.Trained)
classRANGER.specialtyList = [edgeFLURRY]
classRANGER.cProficiency = Proficiency.Trained
classRANGER.proficiencies[0][0].proficiency = Proficiency.Trained
classRANGER.proficiencies[0][1].proficiency = Proficiency.Trained
classRANGER.proficiencies[0][3].proficiency = Proficiency.Trained
classRANGER.proficiencies[0][4].proficiency = Proficiency.Trained
classRANGER.proficiencies[0][5].proficiency = Proficiency.Trained
classRANGER.proficiencies[0][7].proficiency = Proficiency.Trained
classRANGER.proficiencies[1][0].proficiency = Proficiency.Expert
classRANGER.proficiencies[1][1].proficiency = Proficiency.Expert
classRANGER.proficiencies[1][2].proficiency = Proficiency.Trained
classRANGER.skills[9].proficiency = Proficiency.Trained  # nature
classRANGER.skills[15].proficiency = Proficiency.Trained  # survival

classROGUE = Class("Rogue", "", Dex, 8, "Racket", [featureSURPRISEATTACK, featureSNEAKATTACK1], 7, Proficiency.Trained)
classROGUE.specialtyList = [racketMASTERMIND]
classROGUE.cProficiency = Proficiency.Trained
classROGUE.proficiencies[0][0].proficiency = Proficiency.Trained
classROGUE.proficiencies[0][3].proficiency = Proficiency.Trained
classROGUE.proficiencies[0][4].proficiency = Proficiency.Trained
classROGUE.proficiencies[0][7].proficiency = Proficiency.Trained
classROGUE.proficiencies[1][0].proficiency = Proficiency.Trained
classROGUE.proficiencies[1][1].proficiency = Proficiency.Expert
classROGUE.proficiencies[1][2].proficiency = Proficiency.Expert
classROGUE.skills[14].proficiency = Proficiency.Trained  # stealth
classROGUE.proficiencies.append(proficiencyROGUE)
