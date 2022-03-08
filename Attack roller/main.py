import random
from DiceRoller import *


Attack = []
Damage = []

attack = 1  # 1 Axe, 2 Gun, 3 Laser
numAttacks = 2

if attack == 1:
    Attack.append(["Battle Tax", "Attack"])
    Attack.append(["1", "20", "10"])
    Damage.append(["War Tax", "Damage"])
    Damage.append(["1", "8", "6", "Slashing"])
elif attack == 2:
    Attack.append(["Auto Pistol", "Attack"])
    Attack.append(["1", "20", "12"])
    Damage.append(["Laser Pistol", "Damage"])
    Damage.append(["2", "6", "6", "Piercing"])
elif attack == 3:
    Attack.append(["Laser Pistol", "Attack"])
    Attack.append(["1", "20", "12"])
    Damage.append(["Auto Pistol", "Damage"])
    Damage.append(["3", "6", "6", "Radiant"])


for x in range(numAttacks):
    bAmbush, cStrike, bSS, bAcc1, bAcc2 = False, False, False, False, False
    xThunder, xLightning, xCold = False, False, False
    smite1, smite2, smite3, smiteE = False, False, False, False

    if bSS:
        Attack[1][2] = str(int(Attack[1][2]) - 5)
    if bAcc1:
        Attack[1][2] = str(int(Attack[1][2]) + 1)
    if bAcc2:
        Attack[1][2] = str(int(Attack[1][2]) + 2)

    text, crit = AtkRoller(Attack, False, False, 20)
    # text, crit = AtkRoller(warTaxAttack, True, False, 20)
    print(text)

    if crit:
        xThunder, xLightning, xCold, cStrike, = True, True, True, True,
        smite1, smite2, smite3, smiteE = False, False, True, True

    if bAmbush:
        Damage.append(["1", "8", "0", "BaseType"])
    if bSS:
        Damage[1][2] = str(int(Damage[1][2]) + 10)
    if xThunder:
        Damage.append(["1", "4", "0", "Thunder"])
    if xLightning:
        Damage.append(["1", "4", "0", "Electricity"])
    if xCold:
        Damage.append(["1", "4", "0", "Cold"])
    if cStrike:
        Damage.append(["1", "6", "0", "BaseType"])
    if smite1:
        Damage.append(["2", "8", "0", "Radiant"])
    if smite2:
        Damage.append(["3", "8", "0", "Radiant"])
    if smite3:
        Damage.append(["4", "8", "0", "Radiant"])
    if smiteE:
        Damage.append(["1", "8", "0", "Radiant"])

    print(DamageRoller(Damage, crit))
