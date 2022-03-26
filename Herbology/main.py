from Environments import *


bagItems = Object()
bContinue = True


while bContinue:
    bTrue = ""

    # ["Arctic", "Coastal/Underwater", "Desert", "Forest",
    # "Grasslands", "Hills", "Mountains", "Swamp", "Underdark"])
    environment = str((input("Where are you gathering? ")))
    if environment == "Coastal/Underwater":
        bTrue = input("y if coastal ")
    elif environment == "Forest":
        bTrue = input("y if night ")
    elif environment == "Swamp":
        bTrue = input("y if raining ")

    if bTrue == "y":
        bTrue = True
    else:
        bTrue = False

    days = float(input("How many days will you gather? "))
    traveling = input("y if during travel ")
    if traveling == "y":
        days = (days / 2)



    for x in range(1, (int(days * 2)+1)):
        num = random.randint(1, 4)

        for y in range(0, num):
            herb, amount = herbalism(environment, bTrue, 14)
            print("Found " + str(amount) + " " + herb + " on day " + str(x))

            if hasattr(bagItems, herb):
                setattr(bagItems, herb, (getattr(bagItems, herb) + amount))
            else:
                setattr(bagItems, herb, amount)

            if herb == "Voidroot" and environment == "Desert":
                if hasattr(bagItems, "Elemental Water"):
                    setattr(bagItems, "Elemental Water", (getattr(bagItems, "Elemental Water") + 1))
                else:
                    setattr(bagItems, "Elemental Water", 1)

    again = input("press y to exit ")
    if again == "y":
        bContinue = False

print(vars(bagItems))
print("Done")
