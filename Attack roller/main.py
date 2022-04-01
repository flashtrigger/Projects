import random
from DiceRoller import *

advantage = bool(int(input("Enter '1' if attacking with advantage else 0: ")))

unleash = 0
unleash += int(input("Enter '1' to Unleash Incarnation else 0: ")) 

turnOne = int(input("Enter '1' if 1st turn else 0: "))

hasteActive = bool(int(input("If Hasted enter '1' else 0: ")))
if hasteActive:
    unleash += int(input("Enter '1' to Unleash Incarnation else 0: "))

actionSurge = bool(int(input("Enter '1' to Action Surge else 0: ")))
if actionSurge:
    unleash += int(input("Enter '1' to Unleash Incarnation else 0: "))

attackType = int(input("Choose Weapon: 1-Axe, 2-Gun, or 3-Laser: ")) 

numAttacks = (2 + turnOne) + (int(actionSurge) * ((2 * int(actionSurge)) + turnOne)) + int(hasteActive) + unleash
if attackType == 1:
    twoWeapon = bool(int(input("If TWFing enter '1' else 0: ")))
    alwaysSmite = bool(int(input("Enter '1' to enable non-crit Smiting else 0: ")))
    if twoWeapon:
        numAttacks *= 2
if attackType in (2, 3):
    bSS = bool(int(input("Enter '1' to activae SharpShooter else 0: ")))
else:
    bSS = False

accuracyBonus = int(input("Enter the bonus from accuracy stance: "))

critImmunity = bool(int(input("Enter '1' if enemy immune to crits else 0: ")))

totalDamage = []
for x in range(numAttacks):

    Attack = []
    Damage = []

    if attackType == 1:
        Attack.append(["Battle Tax", "Attack"])
        Attack.append(["1", "20", str(10 + accuracyBonus)])
        Damage.append(["Battle Tax", "Damage"])
        Damage.append(["1", "8", "7", "Slashing"])
    elif attackType == 2:
        Attack.append(["Auto Pistol", "Attack"])
        Attack.append(["1", "20", str(11 + accuracyBonus)])
        Damage.append(["Auto Pistol", "Damage"])
        Damage.append(["2", "6", "7", "Piercing"])
    elif attackType == 3:
        Attack.append(["Laser Pistol", "Attack"])
        Attack.append(["1", "20", str(11 + accuracyBonus)])
        Damage.append(["Laser Pistol", "Damage"])
        Damage.append(["3", "6", "7", "Radiant"])
    if bSS:
        Attack[1][2] = str(int(Attack[1][2]) - 5)

    text, crit = AtkRoller(Attack, advantage, False, critImmunity, 20)
    print("\n" + str(x + 1)+ ": "+ text)

    bAmbush, cStrike, bSmiting = bool(turnOne), False, False
    xAcid, xCold, xFire, xLightning, xThunder  = False, False, False, False, False

    if (not critImmunity and crit) or alwaysSmite:
        thanosMode = bool(int(input("Enter '1' to activate Thanos Mode else 0: ")))
        if thanosMode:
            xAcid, xCold, xFire, xLightning, xThunder, = True, True, True, True, True
        
        cStrike = bool(int(input("Enter '1' if spending BP for 1d6 else 0: ")))

        if attackType == 1:
            bSmiting = bool(int(input("Enter '1' to Smite else 0: ")))
            if bSmiting:
                smiteSlot = int(input("Enter the spell Slot used: "))
                smiteE = int(input("Enter '1' if smiting Undead or Fiend else 0: "))
                smiteSlot += smiteE

    if (bAmbush and x == 0) or (bAmbush and actionSurge and x == 3):
        Damage.append(["1", "8", "0", Damage[1][3]])
    if bSS and attackType in (2, 3):
        Damage[1][2] = str(int(Damage[1][2]) + 10)
    if xThunder:
        Damage.append(["1", "4", "0", "Thunder"])
    if xLightning:
        Damage.append(["1", "4", "0", "Electricity"])
    if xCold:
        Damage.append(["1", "4", "0", "Cold"])
    if xFire:
        Damage.append(["1", "4", "0", "Fire"])
    if xAcid:
        Damage.append(["1", "4", "0", "Acid"])
    if cStrike:
        Damage.append(["1", "6", "0", Damage[1][3]])
    if bSmiting:
        Damage.append([str(smiteSlot + 1), "8", "0", "Radiant"])

    textOutput, damageList = DamageRoller(Damage, crit)
    print("\n" + str(x + 1)+ ": " + textOutput)
    totalDamage = combinedDamage(totalDamage, damageList)

print("Total Damage = " + printDamageList(totalDamage))