# DiceRoller
#
# v1
#
# takes a 3 column list and outputs text block of dice rolls
# each row in the list represents either a die roll or text to output with roll
# First row will be formatted as ["Output text", int(times to roll), int(roll sets to collate;"*" if collated)]
# Second row [int(numDice), int(dieSize), int(modifier)]
# additional rows formatted as second will be added to roll before it until
# row formatted as first indicates new line, output, rollTotal. array can be as long as needed

import random
import string


def rollBuilder(rolls):  # create a list of lists representing rolls
    bContinue = (type(rolls) == "list") and (len(rolls[0]) == 4)
    rollsList, rollsTemp = [], []
    j = 0

    if bContinue:  # separate out the sets of rolls
        for each in rolls:
            if (each[j] is not None) and (type(each[j]) != "int"):
                rollsTemp.append(each[j])
                j = j + 1
                while type(rolls[j][0]) == "int":
                    rollsTemp.append(each[j])
                    j = j + 1
                rollsList.append(rollsTemp)
                rollsTemp.clear()
                j = 0
    else:
        print("You must input a 4 column list")

    return rollsList


def roll(num, die, mod):  # perfect? takes XdY+Z and outputs total
    total = 0
    for x in range(1, num+1):
        total = total + random.randint(1, die)
    total = total + mod
    return total


def AtkRoller(theRoll, advantage, elvenAccuracy, critRange):
    theText = theRoll[0][0] + "-" + theRoll[0][1] + ": "
    if advantage:
        if elvenAccuracy:
            roll1 = roll(1, 20, int(theRoll[1][2]))
            roll2 = roll(1, 20, int(theRoll[1][2]))
            roll3 = roll(1, 20, int(theRoll[1][2]))
            thisRoll = max(roll1, roll2, roll3)
        else:
            roll1 = roll(1, 20, int(theRoll[1][2]))
            roll2 = roll(1, 20, int(theRoll[1][2]))
            thisRoll = max(roll1, roll2)
    else:
        thisRoll = roll(1, 20, int(theRoll[1][2]))
    isCrit = (thisRoll - int(theRoll[1][2]) >= critRange)
    theText = theText + str(thisRoll) + " - " + str(thisRoll - int(theRoll[1][2])) + " + " + theRoll[1][2]
    if isCrit:
        theText = theText + " " + "CRIT!"

    return theText, isCrit


def DamageRoller(theRoll, isCrit):
    theText = theRoll[0][0] + "-" + theRoll[0][1] + ": "
    text2 = ""
    damageList = []

    for x in range(1, len(theRoll)):
        damage = roll(int(theRoll[x][0]), int(theRoll[x][1]), int(theRoll[x][2]))
        if isCrit:
            damage = damage + (int(theRoll[x][0]) * int(theRoll[x][1]))
        match = False
        for each in damageList:
            if each[0] == theRoll[x][3]:
                each[1] = each[1] + damage
                match = True
        if not match:
            damageList.append([theRoll[x][3], damage])

    total = 0
    for each in damageList:
        total = total + each[1]
        text2 = text2 + str(each[1]) + " " + each[0] + " "
    theText = theText + str(total) + ": " + text2
    return theText
