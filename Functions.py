from Action import Action  # TODO: Retire Functions?
# DONE Phase 1? - 11/30/21 still alive


# adds an action to calling feat, skill, ability # depreciated
def addAction(*args):

    anAction = Action(args[0], args[1], args[2])
    return anAction


# get self.proficiency, returns proficiency bonus # depreciated
def setProfBonus(proficiency):
    if proficiency == "Trained":
        return 2
    elif proficiency == "Expert":
        return 4
    elif proficiency == "Master":
        return 6
    elif proficiency == "Legendary":
        return 8
    else:
        return 0


def test(this):
    print(this.name+". "+this.description)
