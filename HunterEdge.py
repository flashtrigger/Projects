from Entity import Entity


class HunterEdge(Entity):

    def __init__(self, *args):
        Entity.__init__(self, *args)
        self.upgrade = args[2]


edge = HunterEdge(""
                  , ""
                  , "")

edgeFLURRY = HunterEdge("Flurry"
                        , "You have trained to unleash a devastating flurry of attacks upon your prey. Your multiple "
                          "attack penalty for attacks against your hunted prey is –3 (–2 with an agile weapon) on "
                          "your second attack of the turn instead of –5, and –6 (–4 with an agile weapon) on your "
                          "third or subsequent attack of the turn, instead of –10. "
                        , "You can blend your weapon mastery with skillful targeting to make a series of precise "
                          "attacks. If you have master proficiency with your weapon, your multiple attack penalty for "
                          "attacks against your hunted prey is –2 (–1 with an agile weapon) on your second attack of "
                          "the turn, and –4 (–2 with an agile weapon) on your third and subsequent attacks of the "
                          "turn.")
