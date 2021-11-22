from Trait import *


class Action:

    def __init__(self, *args):
        """

        :rtype: object
        """
        self.name = args[0]
        self.numActions = args[1]  # integer, -1 = reaction, 0 = free
        self.description = args[2]
        self.traits = args[3]  # list of Traits
        self.type = args[4]  # un/trained in Skills
        self.critFail = args[5]
        self.fail = args[6]
        self.success = args[7]
        self.critSuccess = args[8]
        self.requirements = args[9]
        if (len(args) >= 10) and (self.numActions == -1):
            self.trigger = args[10]


actionAID = Action("Aid"
                   , -1
                   , "You try to help your ally with a task. To use this reaction, you must first prepare to "
                     "help, usually by using an action during your turn. You must explain to the GM exactly "
                     "how you’re trying to help, and they determine whether you can Aid your ally. When you "
                     "use your Aid reaction, attempt a skill check or attack roll of a type decided by the "
                     "GM. The typical DC is 20, but the GM might adjust this DC for particularly hard or "
                     "easy tasks. The GM can add any relevant traits to your preparatory action or to your "
                     "Aid reaction depending on the situation, or even allow you to Aid checks other than "
                     "skill checks and attack rolls."
                   , [traitNULL]
                   , "Basic"
                   , "Your ally takes a –1 circumstance penalty to the triggering check."
                   , "Nothing happens"
                   , "You grant your ally a +1 circumstance bonus to the triggering check."
                   , "You grant your ally a +2 circumstance bonus to the triggering check. If you’re a master with "
                     "the check you attempted, the bonus is +3, and if you’re legendary, it’s +4."
                   , "The ally is willing to accept your aid, and you have prepared to help"
                   , "An ally is about to use an action that requires a skill check or attack roll.")
