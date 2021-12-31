from Entity import Entity


class Currency(Entity):  # DONE Phase 1!

    def __init__(self, *args):

        Entity.__init__(self, *args)
        self.value = args[3]  # float (in gold pieces)
        self.bulk = round(args[4], 3)  # float


#  standard coinage
currencyCOPPERCOIN = Currency("Copper Piece", "A minted 1/3 ounce copper coin", 0.01, 0.001)
currencyGOLDCOIN = Currency("Gold Piece", "A minted 1/3 ounce gold coin", 1.0, 0.001)
currencyPLATINUMCOIN = Currency("Platinum Piece", "A minted 1/3 ounce platinum coin", 10.0, 0.001)
currencySILVERCOIN = Currency("Silver Piece", "A minted 1/3 ounce silver coin", 0.1, 0.001)

# currency = Currency("", "",  , )
