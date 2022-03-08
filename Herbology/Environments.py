from DiceRoller import *
import inquirer

yesNo = ["Yes", "No"]


def getChoice(choices, theMessage):
    options = []
    for element in choices:
        options.append(element)
    questions = [inquirer.List('size', message=theMessage, choices=options)]
    answers = inquirer.prompt(questions)
    pick = answers["size"]
    return pick


def elemWater():
    num = roll(1, 100, 0)
    if num <= 75:
        return True
    else:
        return False


def common():
    num = roll(2, 6, 0)
    herb, amount = "", 0
    if num in (2, 12):
        herb, amount = "Mandrake Root", 1
    elif num in (3, 4):
        herb, amount = "Quicksilver Lichen", 1
    elif num in (5, 6):
        herb, amount = "Wild Sageroot", 1
    elif num == 7:
        herb, amount = common()
    elif num in (8, 9):
        herb, amount = "Wyrmtongue Petals", 1
    elif num in (10, 11):
        herb, amount = "Milkweed Seeds", 1
    return herb, amount


def herbalism(environment, herbBonus):
    success = (roll(1, 20, herbBonus) >= 15)
    herb, amount = "", 0
    if not success:
        return "", 0

    num = roll(2, 6, 0)

    if num in (2, 3, 4, 10, 11, 12):
        if elemWater():
            return "Elemental Water", 1

    if environment == "Underdark":
        herb, amount = underdark(num)

    if num in (6, 7, 8) and environment != "Underdark":
        herb, amount = common()
        return herb, amount
    elif environment == "Arctic":
        herb, amount = arctic(num)
    elif environment == "Coastal/Underwater":
        herb, amount = coastWater(num, True)
    elif environment == "Desert":
        herb, amount = desert(num)
    elif environment == "Forest":
        herb, amount = forest(num, True)
    elif environment == "Grasslands":
        herb, amount = grasslands(num)
    elif environment == "Hills":
        herb, amount = hills(num)
    elif environment == "Mountain":
        herb, amount = mountain(num)
    elif environment == "Swamp":
        herb, amount = swamp(num)

    return herb, amount


def arctic(num):
    if num == 2:
        return "Silver Hibiscus", 1
    elif num == 3:
        return "Mortflesh Powder", 1
    elif num == 4:
        return "Ironwood Heart", 1
    elif num == 5:
        return "Frozen Seedlings", 2
    elif num == 9:
        return "Arctic Creeper", 2
    elif num == 10:
        return "Fennel Silk", 1
    elif num == 11:
        return "Fiend's Ivy", 1
    elif num == 12:
        return "Voidroot", 1


def coastWater(num, bStart):
    if bStart:
        coastal = getChoice(yesNo, "Choose yes if Coastal, no if underwater")
        if coastal == "Yes":
            coastal = True
        else:
            coastal = False
    else:
        coastal = False
    if num == 2:
        return "Hydrathistle", random.randint(1, 2)
    elif num == 3:
        if coastal:
            return "Amanita Cap", 1
        else:
            number = roll(2, 6, 0)
            return coastWater(number, False)
    elif num == 4:
        return "Hycancinth Nectar", 1
    elif num == 5:
        return "Chromus Slime", random.randint(1, 2)
    elif num == 9:
        if coastal:
            return "Lavender Sprig", 1
        else:
            number = roll(2, 6, 0)
            return coastWater(number, False)
    elif num == 10:
        if coastal:
            return "Blue Toadshade", 1
        else:
            number = roll(2, 6, 0)
            return coastWater(number, False)
    elif num == 11:
        return "Wrackwort Bulbs", 1
    elif num == 12:
        return "Cosmos Glond", random.randint(1, 2)


def desert(num):
    if num == 2:
        return "Cosmos Glond", 1
    elif num == 3:
        return "Arrow Root", 1
    elif num == 4:
        return "Dried Ephedra", 1
    elif num == 5:
        return "Cactus Juice", 2
    elif num == 9:
        return "Drakus Flower", 1
    elif num == 10:
        return "Scilia Beans", 1
    elif num == 11:
        return "Spineflower Berries", 1
    elif num == 12:
        return "Voidroot", 1


def forest(num, bStart):
    if bStart:
        night = getChoice(yesNo, "Is it night")
        if night == "Yes":
            night = True
        else:
            night = False
    else:
        night = False

    if num == 2:
        return "Harrada Leaf", 1
    elif num == 3:
        return "Nightshade Berries", 1
    elif num == 4:
        return "Emetic Wax", 1
    elif num == 5:
        return "Verdant Nettle", 1
    elif num == 9:
        return "Arrow Root", 1
    elif num == 10:
        return "Ironwood Heart", 1
    elif num == 11:
        return "Blue Toadshade", 1
    elif num == 12:
        if night:
            return "Wisp Stalks", 2
        else:
            number = roll(2, 6, 0)
            return forest(number, False)


def grasslands(num):
    if num == 2:
        return "Harrada Leaf", 1
    elif num == 3:
        return "Drakus Flower", 1
    elif num == 4:
        return "Lavender Sprig", 2
    elif num == 5:
        return "Arrow Root", 1
    elif num == 9:
        return "Scilia Beans", 2
    elif num == 10:
        return "Cactus Juice", 1
    elif num == 11:
        return "Tail Leaf", 1
    elif num == 12:
        return "Hycancinth Nectar", 1


def hills(num):
    if num == 2:
        return "Devil's Bloodleaf", 1
    elif num == 3:
        return "Nightshade Berries", 1
    elif num == 4:
        return "Tail Leaf", 1
    elif num == 5:
        return "Lavender Sprig", 1
    elif num == 9:
        return "Ironwood Heart", 1
    elif num == 10:
        return "Gengko Brush", 1
    elif num == 11:
        return "Rock Vine", 2
    elif num == 12:
        return "Harrada Leaf", 1


def mountain(num):
    if num == 2:
        return "Basilisk's Breath", 1
    elif num == 3:
        return "Frozen Seedlings", 2
    elif num == 4:
        return "Arctic Creeper", 2
    elif num == 5:
        return "Dried Ephedra", 1
    elif num == 9:
        return "Drakus Flower", 1
    elif num == 10:
        return "Luminous Dust Cap", 2
    elif num == 11:
        return "Rock Vine", 1
    elif num == 12:
        return "Primordial Balm", 1


def swamp(num):
    bRaining = getChoice(yesNo, "Is it raining")
    if bRaining == "Yes":
        thisNum = 2
    else:
        thisNum = 1

    if num == 2:
        return "Devil's Bloodleaf", 1
    elif num == 3:
        return "Spineflower Berries", 1
    elif num == 4:
        return "Emetic Wax", 1
    elif num == 5:
        return "Amanita Cap", 2
    elif num == 9:
        return "Blue Toadshade", 2
    elif num == 10:
        return "Wrackwort Bulb", 1
    elif num == 11:
        return "Hydrathistle", thisNum
    elif num == 12:
        return "Primordial Balm", 1


def underdark(num):
    if num == 2:
        return "Primordial Balm", random.randint(1, 2)
    elif num == 3:
        return "Silver Hibiscus", 1
    elif num == 4:
        return "Devil's Bloodleaf", 1
    elif num == 5:
        return "Chromus Slime", 1
    elif num == 6:
        return "Mortflesh Powder", 2
    elif num == 7:
        return "Fennel Silk", 1
    elif num == 8:
        return "Fiend's Ivy", 1
    elif num == 9:
        return "Gengko Brush", 1
    elif num == 10:
        return "Luminous Dust Cap", 2
    elif num == 11:
        return "Radiant Synthseed", 1
    elif num == 12:
        return "Wisp Stalks", 1
