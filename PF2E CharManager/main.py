from Functions import build
from GesaltPC import *
import pickle
import PySimpleGUI as sg
# TODO: Initialize PC attributes, load, Tkinter

# testPC = pickle.load(open("FighterBarb.pickle", "rb"))
testPC = GesaltPC("FighterBarb", "Fighter/Spirit Barbarian")

# transient function making the changes I want at this moment
build(testPC)
testPC.fullBuild()

# for each in testPC.actionList:
#     for element in each:
#         print(element[0].name)
#     print("\n\n")
#
# for each in testPC.activityList:
#     for element in each:
#         print(element[0].name)
#     print("\n\n")

# print(str(testPC.stats[0][0]) + ": " + str(testPC.stats[0][1]) + " - Mod: " + str(testPC.stats[0][2]))
# print(str(testPC.stats[1][0]) + ": " + str(testPC.stats[1][1]) + " - Mod: " + str(testPC.stats[1][2]))
# print(str(testPC.stats[2][0]) + ": " + str(testPC.stats[2][1]) + " - Mod: " + str(testPC.stats[2][2]))
# print(str(testPC.stats[3][0]) + ": " + str(testPC.stats[3][1]) + " - Mod: " + str(testPC.stats[3][2]))
# print(str(testPC.stats[4][0]) + ": " + str(testPC.stats[4][1]) + " - Mod: " + str(testPC.stats[4][2]))
# print(str(testPC.stats[5][0]) + ": " + str(testPC.stats[5][1]) + " - Mod: " + str(testPC.stats[5][2]))

# for each in testPC.feats:
#    print(each.name)

event, values = sg.Window('Character Selection', [[sg.T('Which Character to you want to view?')],
                                                  [sg.In(key='fileName'), sg.FileBrowse()],
                                                  [sg.Submit(), sg.Cancel()]]).read(close=True)

Char = pickle.load(open(values['fileName'], "rb"))

sg.theme('DarkAmber')
header = [[sg.T("Name", size=(15, 1)), sg.T("Alignment", size=(15, 1)), sg.T("Level", size=(5, 1))
          , sg.T("XP", size=(5, 1))],
          [sg.T(Char.name, size=(15, 1)), sg.T(Char.alignment, size=(17, 1)), sg.T(Char.level, size=(3, 1))
          , sg.T(Char.XP, size=(5, 1))]]

statsBlock = [[sg.T("Attribute", size=(9, 1)), sg.T("Score", size=(5, 1)), sg.T("Mod", size=(3, 1))],
              [sg.T(Char.stats[0][0], size=(10, 1)), sg.T(str(Char.stats[0][1]), size=(5, 1))
              , sg.T(str(Char.stats[0][2]))],
              [sg.T(Char.stats[1][0], size=(10, 1)), sg.T(str(Char.stats[1][1]), size=(5, 1))
              , sg.T(str(Char.stats[1][2]))],
              [sg.T(Char.stats[2][0], size=(10, 1)), sg.T(str(Char.stats[2][1]), size=(5, 1))
              , sg.T(str(Char.stats[2][2]))],
              [sg.T(Char.stats[3][0], size=(10, 1)), sg.T(str(Char.stats[3][1]), size=(5, 1))
              , sg.T(str(Char.stats[3][2]))],
              [sg.T(Char.stats[4][0], size=(10, 1)), sg.T(str(Char.stats[4][1]), size=(5, 1))
              , sg.T(str(Char.stats[4][2]))],
              [sg.T(Char.stats[5][0], size=(10, 1)), sg.T(str(Char.stats[5][1]), size=(5, 1))
              , sg.T(str(Char.stats[5][2]))]]

layout = [header,
          [sg.Column(statsBlock)]]

window = sg.Window('Character Manager', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()

# pickle.dump(testPC, open("FighterBarb.pickle", "wb"))
