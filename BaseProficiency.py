from Entity import Entity
from Variables import Proficiency


class BaseProficiency(Entity):

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.type = args[2]  # category / individual (1 / 0)
        self.proficiency = Proficiency.Untrained


# basic category proficiencies
proficiencyLIGHT = BaseProficiency("Light", "Proficiency in light armors.", 1)
proficiencyMEDIUM = BaseProficiency("Medium", "Proficiency in medium armors.", 1)
proficiencyHEAVY = BaseProficiency("Heavy", "Proficiency in Heavy armors.", 1)
proficiencySIMPLE = BaseProficiency("Simple", "Proficiency in Simple weapons.", 1)
proficiencyMARTIAL = BaseProficiency("Martial", "Proficiency in Martial weapons.", 1)
proficiencyADVANCED = BaseProficiency("Advanced", "Proficiency in Advanced weapons.", 1)

# all basic proficiencies
proficiencyALLBASIC = [proficiencyLIGHT, proficiencyMEDIUM, proficiencyHEAVY, proficiencySIMPLE, proficiencyMARTIAL,
                       proficiencyADVANCED]
