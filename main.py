import Functions as Foo  # TODO: rename af Foo everywhere else
import Trait

# TODO: add rest of classes
traitRANGER = Trait.Trait("Ranger", "You are a Ranger")
traitROGUE = Trait.Trait("Rogue", "You are a Rogue")
traitFIGHTER = Trait.Trait("Fighter", "You are a Fighter")
traitBARBARIAN = Trait.Trait("Barbarian", "You are a Barbarian")

# TODO: add rest of races
traitORC = Trait.Trait("Orc", "You are an Orc")
traitELF = Trait.Trait("Elf", "You are an Elf")
traitHUMAN = Trait.Trait("Human", "You are a Human")
traitAASIMAR = Trait.Trait("Aasimar", "You are an Aasimar")
traitTIEFLING = Trait.Trait("Tiefling", "You are a Tiefling")

#  Alignment traits
traitCHAOTIC = Trait.Trait("Chaotic", "You are Lawful in alignment")
traitEVIL = Trait.Trait("Evil", "You are Evil in alignment")
traitGOOD = Trait.Trait("Good", "You are Good in alignment")
traitLAWFUL = Trait.Trait("Lawful", "You are Lawful in alignment")

#  trait = Trait.Trait("", "You're a ")

Foo.test(traitRANGER)
