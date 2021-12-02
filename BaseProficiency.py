from Variables import Proficiency


class BaseProficiency:

    def __init__(self, *args):

        self.name = args[0]
        self.type = args[1]  # category / individual (1 / 0)
        self.proficiency = Proficiency.Untrained


# basic category proficiencies
proficiencyLIGHT = BaseProficiency("Light", 1)
proficiencyMEDIUM = BaseProficiency("Medium", 1)
proficiencyHEAVY = BaseProficiency("Heavy", 1)
proficiencySIMPLE = BaseProficiency("Simple", 1)
proficiencyMARTIAL = BaseProficiency("Martial", 1)
proficiencyADVANCED = BaseProficiency("Advanced", 1)

# all basic proficiencies
proficiencyALLBASIC = [proficiencyLIGHT, proficiencyMEDIUM, proficiencyHEAVY, proficiencySIMPLE, proficiencyMARTIAL,
                       proficiencyADVANCED]
