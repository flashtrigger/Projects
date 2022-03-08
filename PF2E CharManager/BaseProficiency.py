import copy

from Entity import Entity
from Variables import Proficiency


class BaseProficiency(Entity):

    def __init__(self, *args):
        Entity.__init__(self, *args)
        self.type = args[2]  # category / individual / save / spells (1 / 0 / -1 / 2)
        self.proficiency = Proficiency.Untrained
        self.stat = None


# basic category proficiencies
proficiencyLIGHT = BaseProficiency("Light", "Proficiency with light armors.", 1)
proficiencyMEDIUM = BaseProficiency("Medium", "Proficiency with medium armors.", 1)
proficiencyHEAVY = BaseProficiency("Heavy", "Proficiency with Heavy armors.", 1)
proficiencyUNARMORED = BaseProficiency("Unarmored", "Proficiency bonus to AC when Unarmored", 1)
proficiencySIMPLE = BaseProficiency("Simple", "Proficiency with Simple weapons.", 1)
proficiencyMARTIAL = BaseProficiency("Martial", "Proficiency with Martial weapons.", 1)
proficiencyADVANCED = BaseProficiency("Advanced", "Proficiency with Advanced weapons.", 1)
proficiencyUNARMED = BaseProficiency("Unarmed", "Proficiency with Unarmed attacks and natural weapons", 1)

# Saves
proficiencyFORT = BaseProficiency("Fortitude", "Fortitude saving throws allow you to reduce the effects of abilities "
                                               "and afflictions that can debilitate the body. They use your "
                                               "Constitution modifier.", -1)
proficiencyFORT.stat = "Constitution"

proficiencyREF = BaseProficiency("Reflex", "Reflex saving throws measure how well you can respond quickly to a "
                                           "situation and how gracefully you can avoid effects that have been thrown "
                                           "at you. They use your Dexterity modifier .", -1)
proficiencyREF.stat = "Dexterity"

proficiencyWILL = BaseProficiency("Will", "Will saving throws measure how well you can resist attacks to your mind and "
                                          "spirit. They use your Wisdom modifier.", -1)
proficiencyWILL.stat = "Wisdom"

# spells
proficiencySPELLATK = BaseProficiency("Spell Attacks", "", 2)
proficiencySPELLATK.proficiency = Proficiency.Trained

proficiencySPELLDC = BaseProficiency("Spell DCs", "", 2)
proficiencySPELLDC.proficiency = Proficiency.Trained

# all basic proficiencies
proficiencyALLBASIC = [copy.deepcopy(proficiencyLIGHT), copy.deepcopy(proficiencyMEDIUM),
                       copy.deepcopy(proficiencyHEAVY), copy.deepcopy(proficiencyUNARMORED),
                       copy.deepcopy(proficiencySIMPLE), copy.deepcopy(proficiencyMARTIAL),
                       copy.deepcopy(proficiencyADVANCED), copy.deepcopy(proficiencyUNARMED)]

proficiencyALLSAVES = [copy.deepcopy(proficiencyFORT), copy.deepcopy(proficiencyREF), copy.deepcopy(proficiencyWILL)]

proficiencyINNATESPELLS = [copy.deepcopy(proficiencySPELLATK), copy.deepcopy(proficiencySPELLDC)]

proficiencyALL = [copy.deepcopy(proficiencyALLBASIC), copy.deepcopy(proficiencyALLSAVES),
                  copy.deepcopy(proficiencyINNATESPELLS)]

# individual weapon Proficiencies
proficiencyRAPIER = BaseProficiency("Rapier", "Proficiency with Rapier", 0)
proficiencyRAPIER.proficiency = Proficiency.Trained
proficiencySAP = BaseProficiency("Sap", "Proficiency with Sap", 0)
proficiencySAP.proficiency = Proficiency.Trained
proficiencySHORTBOW = BaseProficiency("Shortbow", "Proficiency with Short Bow", 0)
proficiencySHORTBOW.proficiency = Proficiency.Trained
proficiencySHORTSWORD = BaseProficiency("Shortsword", "Proficiency with Shortsword", 0)
proficiencySHORTSWORD.proficiency = Proficiency.Trained

proficiencyROGUE = [copy.deepcopy(proficiencyRAPIER), copy.deepcopy(proficiencySAP), copy.deepcopy(proficiencySHORTBOW),
                    copy.deepcopy(proficiencySHORTSWORD)]

proficiency = BaseProficiency("", "Proficiency with ", 0)
