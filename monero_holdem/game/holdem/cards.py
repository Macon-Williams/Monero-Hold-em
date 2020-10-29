class Deck(object):
    pass


class Table(object):
    def __init__(self):
        self.cards = []
        self.pot = 0.0
        # Maybe use these in the future
        self.flop = False
        self.turn = False
        self.river = False

    def list_cards(self):
        for i in range(len(self.cards)):
            print(self.cards[i].name)

    def return_pot(self):
        return self.pot

    def add_pot(self, amount):
        self.pot += amount
