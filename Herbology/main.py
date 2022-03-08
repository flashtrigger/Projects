from Environments import *


class Object(object):
    pass


bagItems = Object()
bContinue = True


if bContinue:

    environment = getChoice(["Arctic", "Coastal/Underwater", "Desert", "Forest", "Grasslands", "Hills", "Mountains",
                            "Swamp", "Underdark"], "Where are you gathering?")

    days = float(input("How many days will you gather?"))

    traveling = getChoice(yesNo, "Are you gathering during travel?")
    if traveling == "Yes":
        days = (days / 2)

    for x in range(int(days * 2)):
        num = random.randint(1, 4)
        for y in range(0, num):
            herb, amount = herbalism(environment, 14)
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

    again = getChoice(yesNo, "Do you have another environment to gather from?")
    if again == "No":
        bContinue = False

    # z for z in dir(bagItems) if not z.startswith('__') and not callable(getattr(bagItems, z))
print(vars(bagItems))

print("Done")
