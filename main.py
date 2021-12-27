from Functions import build
from GesaltPC import *
import pickle
# TODO: Initialize PC attributes, load, Tkinter

# testPC = pickle.load(open("FighterBarb.pickle", "rb"))
testPC = GesaltPC("FighterBarb", "Fighter/Spirit Barbarian")

# transient function making the changes I want at this moment
build(testPC)
# testPC.updateMODS() # working
# testPC.buildFeats() # working
# testPC.buildSkills() # working
# testPC.buildBaseProfs(1) # working
# testPC.buildBaseProfs(-1) # working
testPC.buildActions()

for each in testPC.actionList:
    for element in each:
        print(element[0].name)
    print("\n\n")

for each in testPC.activityList:
    for element in each:
        print(element[0].name)
    print("\n\n")

# print(str(testPC.stats[0][0]) + ": " + str(testPC.stats[0][1]) + " - Mod: " + str(testPC.stats[0][2]))
# print(str(testPC.stats[1][0]) + ": " + str(testPC.stats[1][1]) + " - Mod: " + str(testPC.stats[1][2]))
# print(str(testPC.stats[2][0]) + ": " + str(testPC.stats[2][1]) + " - Mod: " + str(testPC.stats[2][2]))
# print(str(testPC.stats[3][0]) + ": " + str(testPC.stats[3][1]) + " - Mod: " + str(testPC.stats[3][2]))
# print(str(testPC.stats[4][0]) + ": " + str(testPC.stats[4][1]) + " - Mod: " + str(testPC.stats[4][2]))
# print(str(testPC.stats[5][0]) + ": " + str(testPC.stats[5][1]) + " - Mod: " + str(testPC.stats[5][2]))

# for each in testPC.feats:
#    print(each.name)

# pickle.dump(testPC, open("FighterBarb.pickle", "wb"))
